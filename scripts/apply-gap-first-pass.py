#!/usr/bin/env python3
"""Insert best-effort translations for documented semantic source gaps.

Correction files contain ``{"corrections": [...]}``.  Each correction names a
gap and partitions all of its source fragments into one or more translated
rows.  The script updates the owning batch descriptors, their English files,
the release checkpoint, and the source-gap registry together.
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

from release_store import read_release, write_release
from source_evidence import build_source_evidence, descriptor_groups


parser = argparse.ArgumentParser()
parser.add_argument("correction", type=Path, nargs="+")
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent

gaps_path = root / "corpus/source-gaps.json"
gaps = json.loads(gaps_path.read_text())
gap_by_id = {gap["id"]: gap for gap in gaps}
assert len(gap_by_id) == len(gaps), "Repeated source-gap ID"

corrections = {}
for path in args.correction:
    data = json.loads(path.read_text())
    for correction in data["corrections"]:
        gap_id = correction["gap_id"]
        assert gap_id not in corrections, f"Repeated correction: {gap_id}"
        assert gap_id in gap_by_id, f"Unknown source gap: {gap_id}"
        gap = gap_by_id[gap_id]
        assert gap["kind"] == "meaning_unresolved", (
            f"Only semantic gaps can receive first-pass translations: {gap_id}")
        rows = correction["rows"]
        assert rows and all(row.get("en", "").strip() for row in rows), (
            f"Empty correction row: {gap_id}")
        flattened = [sid for row in rows for sid in row["source_line_ids"]]
        assert flattened == gap["source_line_ids"], (
            f"Correction must partition source IDs in order: {gap_id}")
        assert all(row["source_line_ids"] for row in rows), (
            f"Correction row lacks source IDs: {gap_id}")
        correction["review_note"] = correction.get("review_note", "").strip()
        corrections[gap_id] = correction

resolved_ids = {
    sid for gap_id in corrections for sid in gap_by_id[gap_id]["source_line_ids"]
}
correction_rows = {
    row["source_line_ids"][0]: (gap_id, row)
    for gap_id, correction in corrections.items() for row in correction["rows"]
}
assert len(correction_rows) == sum(len(c["rows"]) for c in corrections.values())

owners = defaultdict(list)
descriptor_updates = []
extraction_cache = {}
for batch_path in sorted((root / "corpus/batches").glob("*.json")):
    batch = json.loads(batch_path.read_text())
    excluded = batch.get("excluded_source_ids", [])
    owned_resolved = {
        item["id"] for item in excluded
        if item.get("kind") == "unresolved_source" and item["id"] in resolved_ids
    }
    if not owned_resolved:
        continue

    relevant = []
    for gap_id, correction in corrections.items():
        for row in correction["rows"]:
            ids = row["source_line_ids"]
            if set(ids).issubset(owned_resolved):
                relevant.append((gap_id, row))
                owners[gap_id].append(batch_path)
            else:
                assert not set(ids).intersection(owned_resolved), (
                    f"Partial corrected row in {batch_path}: {gap_id}")

    extraction_path = root / batch["extraction"]
    if extraction_path not in extraction_cache:
        extraction_order = {}
        resolved_extracted = {}
        for index, line in enumerate(extraction_path.open()):
            extracted_row = json.loads(line)
            extraction_order[extracted_row["id"]] = index
            if extracted_row["id"] in resolved_ids:
                resolved_extracted[extracted_row["id"]] = extracted_row
        extraction_cache[extraction_path] = (extraction_order, resolved_extracted)
    extraction_order, resolved_extracted = extraction_cache[extraction_path]
    old_groups, _ = descriptor_groups(batch)
    old_english = (root / batch["english"]).read_text().splitlines()
    assert len(old_english) == len(batch["source_ids"])
    english_by_id = dict(zip(batch["source_ids"], old_english))
    groups = dict(old_groups)
    notes = dict(batch.get("notes", {}))

    for gap_id, row in relevant:
        sid = row["source_line_ids"][0]
        assert sid not in english_by_id
        english_by_id[sid] = row["en"].strip()
        groups[sid] = row["source_line_ids"]
        original_note = gap_by_id[gap_id]["note"]
        review_note = corrections[gap_id]["review_note"]
        notes[sid] = original_note + (
            " Completion-first first pass: " + review_note if review_note else
            " Completion-first first pass; retain for later philological audit."
        )

    source_ids = sorted(english_by_id, key=lambda sid: extraction_order[groups[sid][0]])
    batch["source_ids"] = source_ids
    batch["source_groups"] = {
        sid: groups[sid] for sid in source_ids if len(groups[sid]) > 1
    }
    batch["source_joiners"] = {
        sid: joiners for sid, joiners in batch.get("source_joiners", {}).items()
        if sid in batch["source_groups"]
    }
    batch["notes"] = {sid: notes[sid] for sid in source_ids if sid in notes}
    batch["excluded_source_ids"] = [
        item for item in excluded if item["id"] not in owned_resolved
    ]
    for key in ("unresolved_source", "unresolved_passages"):
        remaining = []
        for item in batch.get(key, []):
            ids = item.get("source_ids", item.get("source_line_ids", []))
            if ids and set(ids).issubset(resolved_ids):
                continue
            assert not set(ids).intersection(resolved_ids), (
                f"Partial unresolved record in {batch_path}: {ids}")
            remaining.append(item)
        if key in batch:
            batch[key] = remaining

    new_english = [english_by_id[sid] for sid in source_ids]
    counts = batch.get("counts", {})
    word_count = sum(len(re.findall(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*", en))
                     for en in new_english)
    if "english_words" in counts:
        counts["english_words"] = word_count
    for key in ("english_verse_rows", "translated_verse_rows"):
        if key in counts:
            counts[key] = len(source_ids)
    if "translated_source_fragments" in counts:
        counts["translated_source_fragments"] = sum(len(groups[sid]) for sid in source_ids)
    if "unresolved_source_rows" in counts:
        counts["unresolved_source_rows"] = sum(
            item.get("kind") == "unresolved_source"
            for item in batch["excluded_source_ids"])
    if "unresolved_source_verses" in counts:
        counts["unresolved_source_verses"] = len(batch.get("unresolved_source", []))

    requested = {sid for _, row in relevant for sid in row["source_line_ids"]}
    extracted = {sid: resolved_extracted[sid] for sid in requested}
    descriptor_updates.append((batch_path, batch, root / batch["english"], new_english,
                               extracted, relevant))

for gap_id in corrections:
    assert owners[gap_id], f"No batch descriptor owns corrected gap: {gap_id}"

new_records = {}
for batch_path, batch, _, _, extracted, relevant in descriptor_updates:
    groups, joiners = descriptor_groups(batch)
    for gap_id, row in relevant:
        sid = row["source_line_ids"][0]
        if sid in new_records:
            assert new_records[sid]["en"] == row["en"].strip(), (
                f"Conflicting overlapping correction: {sid}")
            continue
        evidence = build_source_evidence(
            sid, groups[sid], joiners[sid], extracted,
            batch["source_url"], batch.get("notes", {}).get(sid))
        evidence.update(
            part=batch["part"], en=row["en"].strip(),
            transcription_status="verified",
            transcription_evidence=batch["transcription_check"],
            lineation_status="provisional", status="draft",
            translation_method=(
                "AI completion-first translation directly from Kyrgyz; "
                "semantic uncertainty retained in note; no independent specialist review"))
        new_records[sid] = evidence

release = [json.loads(line) for line in read_release(root).splitlines() if line.strip()]
position = {row["id"]: index for index, row in enumerate(release)}
insert_after = {}
for gap_id, correction in corrections.items():
    gap = gap_by_id[gap_id]
    assert position[gap["before_id"]] == position[gap["after_id"]] + 1, (
        f"Gap anchors are no longer adjacent: {gap_id}")
    assert gap["after_id"] not in insert_after, (
        f"Multiple gap regions share an insertion anchor: {gap_id}")
    insert_after[gap["after_id"]] = [
        new_records[row["source_line_ids"][0]] for row in correction["rows"]
    ]

rebuilt = []
for row in release:
    rebuilt.append(row)
    rebuilt.extend(insert_after.get(row["id"], []))
for ordinal, row in enumerate(rebuilt, 1):
    row["ordinal"] = ordinal

# All validation above precedes mutations.  Write descriptors and text first;
# the release index replacement remains the final atomic publication checkpoint.
for batch_path, batch, english_path, english, _, _ in descriptor_updates:
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n")
    english_path.write_text("\n".join(english) + "\n")
gaps_path.write_text(json.dumps(
    [gap for gap in gaps if gap["id"] not in corrections],
    ensure_ascii=False, indent=2) + "\n")
write_release(root, "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rebuilt))
print(json.dumps({
    "resolved_regions": len(corrections),
    "inserted_rows": len(new_records),
    "remaining_source_gaps": len(gaps) - len(corrections),
    "release_rows": len(rebuilt),
}))
