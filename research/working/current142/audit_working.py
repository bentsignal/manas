#!/usr/bin/env python3
"""Summarize and sanity-check the in-progress inventory-142 transcription."""

from collections import Counter
import json
from pathlib import Path
import re
import sys
import unicodedata


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "research/working/current142"
PRINTED = ROOT / "sources/extracted/seytek-2012.lines.jsonl"
SHA = "2b1fd33d35b9fec662724180743e44a26bc44d8b347d5f99c373acf98cb6c73f"
WORDS = re.compile(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*")
COUNTERPART = re.compile(r"Secure printed counterpart: (seytek-2012:p\d+:b\d+:l\d+)")
FIRST_PRINTED_ID = "seytek-2012:p0913:b004:l002"
LAST_PRINTED_ID = "seytek-2012:p1005:b002:l006"


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def normalized(text: str) -> str:
    text = unicodedata.normalize("NFC", text).casefold().replace("ё", "е")
    text = text.replace("[", "").replace("]", "")
    return re.sub(r"[^а-яңөүa-z0-9]+", "", text)


def main() -> None:
    printed_rows = read_jsonl(PRINTED)
    printed_ids = {row["id"] for row in printed_rows}
    printed_position = {row["id"]: index for index, row in enumerate(printed_rows)}
    printed_by_id = {row["id"]: row for row in printed_rows}
    interval_start = printed_position[FIRST_PRINTED_ID]
    interval_end = printed_position[LAST_PRINTED_ID]
    sys.path.insert(0, str(ROOT / "scripts"))
    from release_store import iter_release
    released_printed_ids = {
        source_id
        for release_row in iter_release(ROOT)
        for source_id in release_row.get("source_line_ids", [release_row["id"]])
        if source_id.startswith("seytek-2012:")
    }
    interval_ids = {
        row["id"]
        for row in printed_rows[interval_start:interval_end + 1]
        if row["id"] in released_printed_ids
    }
    assert len(interval_ids) == 7320
    pages: dict[int, list[dict]] = {}
    for path in sorted(WORK.glob("page-*.reviewed.jsonl")):
        rows = read_jsonl(path)
        assert rows, f"empty transcription: {path}"
        page = rows[0]["page"]
        assert path.name == f"page-{page:03d}.reviewed.jsonl"
        assert 4 <= page <= 148 and page not in pages
        assert all(row["page"] == page for row in rows)
        assert all(row["source_id"] == "sayakbay-ms-current142" for row in rows)
        assert all(row["pdf_sha256"] == SHA for row in rows)
        assert [row["line_in_page"] for row in rows] == list(range(1, len(rows) + 1))
        assert all(row["classification"] in {"narrative", "heading"} for row in rows)
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
            assert match.group(1) in interval_ids, f"counterpart outside inventory142 interval in {row['id']}"
            assert normalized(row["text"]) == normalized(printed_by_id[match.group(1)]["text"]), (
                f"counterpart text mismatch in {row['id']}: {match.group(1)}"
            )
            counterpart_ids.append(match.group(1))
    counterpart_positions = [printed_position[value] for value in counterpart_ids]
    inversions = sum(
        right <= left
        for left, right in zip(counterpart_positions, counterpart_positions[1:])
    )

    completed = sorted(pages)
    report = {
        "completed_pages": len(completed),
        "page_span": [completed[0], completed[-1]] if completed else None,
        "completed_page_numbers": completed,
        "missing_pages": [page for page in range(4, 149) if page not in pages],
        "physical_text_rows": len(rows),
        "catalogue_line_tally": 7668,
        "difference_from_catalogue_tally": len(rows) - 7668,
        "narrative_rows": sum(row["classification"] == "narrative" for row in rows),
        "heading_rows": sum(row["classification"] == "heading" for row in rows),
        "english_words": sum(len(WORDS.findall(row["en"])) for row in rows),
        "rows_with_recorded_printed_counterparts": len(counterpart_ids),
        "distinct_recorded_printed_counterparts": len(set(counterpart_ids)),
        "recorded_counterpart_adjacent_inversions": inversions,
        "reused_recorded_counterpart_assignments": len(counterpart_ids) - len(set(counterpart_ids)),
        "printed_interval_lines": len(interval_ids),
        "printed_interval_lines_not_yet_mapped": len(interval_ids - set(counterpart_ids)),
    }
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
