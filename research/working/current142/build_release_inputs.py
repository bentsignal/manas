#!/usr/bin/env python3
"""Build inventory-142 extraction, conservative overlap map, batch, and gap evidence."""

from collections import defaultdict
import json
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "research/working/current142"
PRINTED = ROOT / "sources/extracted/seytek-2012.lines.jsonl"
EXTRACTION = ROOT / "sources/extracted/sayakbay-ms-current142.lines.jsonl"
OVERLAPS = WORK / "release-overlap-map.json"
GAPS = WORK / "unreadable-gaps.json"
BATCH = ROOT / "corpus/batches/pages-manuscript142-0004-0148.json"
ENGLISH = ROOT / "corpus/batches/pages-manuscript142-0004-0148.en.txt"
SHA = "2b1fd33d35b9fec662724180743e44a26bc44d8b347d5f99c373acf98cb6c73f"
URL = "https://manuscript.bizdin.kg/static/media/pdf/web-142-Seitek-X-bolum-Saiakba-Karalaev.pdf"
FIRST_PRINTED_ID = "seytek-2012:p0913:b004:l002"
LAST_PRINTED_ID = "seytek-2012:p1005:b002:l006"
NOTE_COUNTERPART = re.compile(r"(seytek-2012:p\d+:b\d+:l\d+)")
WORDS = re.compile(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*")


def normalized(text: str) -> str:
    text = unicodedata.normalize("NFC", text).casefold().replace("ё", "е")
    text = text.replace("[", "").replace("]", "")
    return re.sub(r"[^а-яңөүa-z0-9]+", "", text)


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> None:
    rows = []
    for page in range(4, 149):
        path = WORK / f"page-{page:03}.reviewed.jsonl"
        page_rows = load_jsonl(path)
        assert [row["line_in_page"] for row in page_rows] == list(range(1, len(page_rows) + 1))
        assert all(row["page"] == page and row["pdf_sha256"] == SHA for row in page_rows)
        assert all(row["classification"] in {"narrative", "heading"} for row in page_rows)
        assert all(row["en"].strip() for row in page_rows)
        rows.extend(page_rows)
    assert len({row["id"] for row in rows}) == len(rows)

    printed_all = load_jsonl(PRINTED)
    printed_all_by_id = {row["id"]: index for index, row in enumerate(printed_all)}
    start = printed_all_by_id[FIRST_PRINTED_ID]
    end = printed_all_by_id[LAST_PRINTED_ID]
    assert start <= end
    printed = printed_all[start:end + 1]
    assert len(printed) == 7320
    printed_by_id = {row["id"]: row for row in printed}
    manuscript_by_id = {row["id"]: row for row in rows}
    unreadable_ids = {
        row["id"] for row in rows if row.get("transcription_status") == "unreadable"
    }
    canonical = [row for row in rows if row["id"] not in unreadable_ids]

    manuscript_by_text: dict[str, list[dict]] = defaultdict(list)
    printed_by_text: dict[str, list[dict]] = defaultdict(list)
    for row in canonical:
        manuscript_by_text[normalized(row["text"])].append(row)
    for row in printed:
        printed_by_text[normalized(row["text"])].append(row)

    mapped: dict[str, dict] = {}
    used_printed: set[str] = set()

    def add_pair(manuscript_id: str, printed_id: str, basis: str) -> None:
        if manuscript_id in mapped or printed_id in used_printed:
            return
        assert manuscript_id in manuscript_by_id and printed_id in printed_by_id
        mapped[manuscript_id] = {"counterpart_id": printed_id, "basis": basis}
        used_printed.add(printed_id)

    # Accept worker-recorded positions only when the source strings agree exactly
    # after punctuation/case normalization and the position lies within this
    # inventory's securely bounded printed interval.
    for row in canonical:
        match = NOTE_COUNTERPART.search(row.get("uncertainty_note", ""))
        if not match or match.group(1) not in printed_by_id:
            continue
        target = printed_by_id[match.group(1)]
        if normalized(row["text"]) == normalized(target["text"]):
            add_pair(row["id"], target["id"], "recorded exact printed counterpart")

    # Exact strings occurring once in each bounded witness are unambiguous
    # overlaps. Formulaic repetitions remain released unless position-anchored.
    for row in canonical:
        key = normalized(row["text"])
        candidates = printed_by_text.get(key, [])
        if key and len(manuscript_by_text[key]) == 1 and len(candidates) == 1:
            add_pair(row["id"], candidates[0]["id"], "unique exact normalized line in bounded episode")

    excluded_ids = set(mapped) | unreadable_ids
    released = [row for row in rows if row["id"] not in excluded_ids]
    assert released

    exclusions = []
    pairs = []
    for row in canonical:
        overlap = mapped.get(row["id"])
        if not overlap:
            continue
        pairs.append({"manuscript_id": row["id"], **overlap})
        exclusions.append({
            "id": row["id"],
            "kind": "overlap",
            "reason": (
                "Secure manuscript counterpart of already released row "
                f"{overlap['counterpart_id']}; retained in the physical extraction and not counted twice."
            ),
            "counterpart_id": overlap["counterpart_id"],
        })
    for row in rows:
        if row["id"] in unreadable_ids:
            exclusions.append({
                "id": row["id"],
                "kind": "unresolved_source",
                "reason": row.get("uncertainty_note", "The manuscript baseline is unreadable."),
            })

    EXTRACTION.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    OVERLAPS.write_text(json.dumps({
        "source_id": "sayakbay-ms-current142",
        "scanned_text_rows": len(rows),
        "catalogue_line_tally": 7668,
        "catalogue_difference": len(rows) - 7668,
        "secure_printed_overlaps": len(pairs),
        "unreadable_rows": len(unreadable_ids),
        "released_manuscript_rows": len(released),
        "method": (
            "Exact individually recorded positions plus normalized strings unique in both the complete manuscript "
            "and its securely bounded 7,320-line printed interval. Repeated formulas without a position anchor "
            "remain released; unreadable baselines remain explicit unresolved source rows."
        ),
        "pairs": pairs,
    }, ensure_ascii=False, indent=2) + "\n")

    source_ids = [row["id"] for row in released]
    descriptor = {
        "part": "seytek",
        "status": "draft",
        "extraction": str(EXTRACTION.relative_to(ROOT)),
        "source_url": URL,
        "english": str(ENGLISH.relative_to(ROOT)),
        "source_ids": source_ids,
        "source_groups": {},
        "excluded_source_ids": exclusions,
        "notes": {
            source_ids[0]: (
                "Completion-first direct transcription of current inventory 142. Handwritten readings and "
                "English remain provisional and require specialist review."
            )
        },
        "transcription_check": {
            "method": "visual-pdf-comparison",
            "checked_by": "Codex workers; same-agent validation and parent sampling",
            "date": "2026-09-16",
            "pdf_pages": list(range(4, 149)),
            "details": (
                "Every visible narrative or genuine heading baseline on PDF pages 4-148 was retained in source "
                "order. The full direct pass was reconciled conservatively against the securely bounded printed "
                "episode. No independent specialist review."
            ),
        },
        "after_id": "seytek-1991-continuation:p0348:b002:l024",
    }
    BATCH.write_text(json.dumps(descriptor, ensure_ascii=False, indent=2) + "\n")
    ENGLISH.write_text("\n".join(row["en"] for row in released) + "\n")

    released_set = set(source_ids)
    gap_records = []
    for index, row in enumerate(rows):
        if row["id"] not in unreadable_ids:
            continue
        before = next((candidate for candidate in rows[index + 1:] if candidate["id"] in released_set), None)
        after = next((candidate for candidate in reversed(rows[:index]) if candidate["id"] in released_set), None)
        assert before and after, f"unreadable row lacks released anchors: {row['id']}"
        gap_records.append({
            "id": f"{row['id']}:unreadable-baseline",
            "kind": "damaged",
            "status": "unresolved",
            "source_id": "sayakbay-ms-current142",
            "after_id": after["id"],
            "before_id": before["id"],
            "source_line_ids": [row["id"]],
            "evidence": f"research/working/current142/page-{row['page']:03d}.reviewed.jsonl",
            "source": {
                "url": URL,
                "page": row["page"],
                "sha256": SHA,
                "segments": [{"id": row["id"], "raw": row["raw"], "bbox": row.get("bbox")}],
            },
            "note": row.get("uncertainty_note", "The manuscript baseline is unreadable."),
        })
    GAPS.write_text(json.dumps(gap_records, ensure_ascii=False, indent=2) + "\n")

    print(json.dumps({
        "scanned_text_rows": len(rows),
        "catalogue_line_tally": 7668,
        "catalogue_difference": len(rows) - 7668,
        "physical_english_words": sum(len(WORDS.findall(row["en"])) for row in rows),
        "secure_printed_overlaps": len(pairs),
        "unreadable_rows": len(unreadable_ids),
        "released_lines": len(released),
        "released_english_words": sum(len(WORDS.findall(row["en"])) for row in released),
    }))


if __name__ == "__main__":
    main()
