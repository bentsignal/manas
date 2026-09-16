#!/usr/bin/env python3
"""Summarize and sanity-check the in-progress inventory-143 transcription."""

from collections import Counter
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "research/working/current143"
PRINTED = ROOT / "sources/extracted/seytek-2012.lines.jsonl"
SHA = "db22e2a5274260d0d1a06f22082ce535758ff594af9dc4843a57782d50547221"
WORDS = re.compile(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*")
COUNTERPART = re.compile(r"Secure printed counterpart: (seytek-2012:p\d+:b\d+:l\d+)")


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> None:
    printed_rows = read_jsonl(PRINTED)
    printed_ids = {row["id"] for row in printed_rows}
    printed_position = {row["id"]: index for index, row in enumerate(printed_rows)}
    pages: dict[int, list[dict]] = {}
    for path in sorted(WORK.glob("page-*.reviewed.jsonl")):
        rows = read_jsonl(path)
        assert rows, f"empty transcription: {path}"
        page = rows[0]["page"]
        assert path.name == f"page-{page:03d}.reviewed.jsonl"
        assert 3 <= page <= 190 and page not in pages
        assert all(row["page"] == page for row in rows)
        assert all(row["source_id"] == "sayakbay-ms-current143" for row in rows)
        assert all(row["pdf_sha256"] == SHA for row in rows)
        assert [row["line_in_page"] for row in rows] == list(range(1, len(rows) + 1))
        assert all(row["classification"] == "narrative" for row in rows)
        assert all(row["text"].strip() and row["en"].strip() for row in rows)
        pages[page] = rows

    rows = [row for page in sorted(pages) for row in pages[page]]
    ids = [row["id"] for row in rows]
    duplicates = [value for value, count in Counter(ids).items() if count > 1]
    assert not duplicates, f"duplicate row ids: {duplicates[:5]}"

    counterpart_ids = []
    for row in rows:
        match = COUNTERPART.search(row.get("uncertainty_note", ""))
        if match:
            assert match.group(1) in printed_ids, f"unknown counterpart in {row['id']}"
            counterpart_ids.append(match.group(1))
    counterpart_positions = [printed_position[value] for value in counterpart_ids]
    assert counterpart_positions == sorted(counterpart_positions)
    assert len(counterpart_ids) == len(set(counterpart_ids))

    completed = sorted(pages)
    missing = [page for page in range(3, 191) if page not in pages]
    report = {
        "completed_pages": len(completed),
        "page_span": [completed[0], completed[-1]] if completed else None,
        "completed_page_numbers": completed,
        "missing_pages": missing,
        "physical_narrative_lines": len(rows),
        "english_words": sum(len(WORDS.findall(row["en"])) for row in rows),
        "rows_with_recorded_printed_counterparts": len(counterpart_ids),
        "distinct_recorded_printed_counterparts": len(set(counterpart_ids)),
        "recorded_counterparts_strictly_monotonic": True,
    }
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
