#!/usr/bin/env python3
"""Apply reviewed one-row English corrections to batches and the release."""
import argparse
import json
import re
from pathlib import Path

from release_store import read_release, write_release


parser = argparse.ArgumentParser()
parser.add_argument("correction", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
correction_path = args.correction.resolve()
data = json.loads(correction_path.read_text())
corrections = data["corrections"]
by_id = {item["id"]: item for item in corrections}
assert len(by_id) == len(corrections), "Repeated correction ID"
assert all(item.get("en", "").strip() for item in corrections), "Blank correction"

owners = {}
changed_batch_rows = 0
for batch_path in sorted((root / "corpus/batches").glob("*.json")):
    batch = json.loads(batch_path.read_text())
    hits = [sid for sid in batch.get("source_ids", []) if sid in by_id]
    if not hits:
        continue
    english_path = root / batch["english"]
    english = english_path.read_text().splitlines()
    assert len(english) == len(batch["source_ids"]), batch_path
    for index, sid in enumerate(batch["source_ids"]):
        if sid not in by_id:
            continue
        assert sid not in owners, f"Correction has multiple batch owners: {sid}"
        owners[sid] = str(batch_path.relative_to(root))
        english[index] = by_id[sid]["en"].strip()
        batch.setdefault("notes", {})[sid] = (
            "Completion-first first pass corrected after targeted high-severity "
            f"source-context review: {by_id[sid]['note'].strip()}"
        )
        changed_batch_rows += 1
    review = batch.setdefault("alignment_check", {})
    review["gap_first_pass_high_severity_qa_2026_09_15"] = {
        "method": "targeted source-English semantic review",
        "checked_by": "Codex Sol low translation worker",
        "date": data["date"],
        "rows_checked": len(hits),
        "changed_source_ids": hits,
        "audit": "research/GAP-FIRST-PASS-AUDIT-2026-09-15.json",
        "corrections": str(correction_path.relative_to(root)),
    }
    words = sum(len(re.findall(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*", line))
                for line in english)
    if "english_words" in batch.get("counts", {}):
        batch["counts"]["english_words"] = words
    english_path.write_text("\n".join(english) + "\n")
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n")

assert set(owners) == set(by_id), f"Missing batch owners: {set(by_id) - set(owners)}"

rows = [json.loads(line) for line in read_release(root).splitlines() if line.strip()]
release_by_id = {row["id"]: row for row in rows}
assert len(release_by_id) == len(rows), "Repeated release ID"
for sid, correction in by_id.items():
    assert sid in release_by_id, f"Correction missing from release: {sid}"
    row = release_by_id[sid]
    row["en"] = correction["en"].strip()
    row["translation_review"] = {
        "method": "targeted source-English semantic review",
        "checked_by": "Codex Sol low translation worker",
        "date": data["date"],
        "severity": "high",
        "note": correction["note"].strip(),
        "audit": "research/GAP-FIRST-PASS-AUDIT-2026-09-15.json",
    }

write_release(root, "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
print(json.dumps({
    "corrected_rows": len(by_id),
    "changed_batch_rows": changed_batch_rows,
    "release_rows": len(rows),
}))
