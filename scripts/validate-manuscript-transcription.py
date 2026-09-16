#!/usr/bin/env python3
"""Validate completion-first, line-accounted manuscript transcriptions.

Every requested PDF page must be represented. Uncertain handwriting is kept as an
explicit row so that a difficult reading cannot silently disappear from coverage.
"""

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


STATUSES = {"visually_transcribed", "uncertain", "unreadable"}
CLASSES = {"narrative", "heading", "folio", "nonverse"}


def page_spec(value: str) -> list[int]:
    pages: set[int] = set()
    for item in value.split(","):
        bounds = item.strip().split("-", 1)
        start = int(bounds[0])
        end = int(bounds[-1])
        if start < 1 or end < start:
            raise argparse.ArgumentTypeError(f"invalid page range: {item}")
        pages.update(range(start, end + 1))
    return sorted(pages)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonl", type=Path)
    parser.add_argument("--pages", required=True, type=page_spec)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--require-english", action="store_true")
    args = parser.parse_args()

    digest = hashlib.sha256(args.pdf.read_bytes()).hexdigest()
    rows = []
    for number, line in enumerate(args.jsonl.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{args.jsonl}:{number}: {exc}") from exc

    assert rows, "empty transcription"
    ids: set[str] = set()
    by_page: dict[int, list[dict]] = defaultdict(list)
    requested = set(args.pages)
    for row in rows:
        ident = row.get("id")
        assert isinstance(ident, str) and ident, "missing id"
        assert ident not in ids, f"duplicate id: {ident}"
        ids.add(ident)
        assert row.get("source_id") == args.source_id, f"wrong source_id: {ident}"
        assert row.get("pdf_sha256") == digest, f"wrong PDF digest: {ident}"
        page = row.get("page")
        assert page in requested, f"row outside requested pages: {ident}"
        assert row.get("classification") in CLASSES, f"invalid classification: {ident}"
        status = row.get("transcription_status")
        assert status in STATUSES, f"invalid transcription status: {ident}"
        assert isinstance(row.get("line_in_page"), int) and row["line_in_page"] >= 1, (
            f"invalid line_in_page: {ident}"
        )
        if row["classification"] in {"narrative", "heading"}:
            assert isinstance(row.get("text"), str) and row["text"].strip(), (
                f"missing source text or explicit unreadable marker: {ident}"
            )
        if status != "visually_transcribed":
            assert isinstance(row.get("uncertainty_note"), str) and row["uncertainty_note"].strip(), (
                f"uncertainty requires a note: {ident}"
            )
        if args.require_english and row["classification"] in {"narrative", "heading"}:
            assert isinstance(row.get("en"), str) and row["en"].strip(), f"missing English: {ident}"
        by_page[page].append(row)

    missing = requested - set(by_page)
    assert not missing, f"requested pages without any accounting row: {sorted(missing)}"
    for page, page_rows in by_page.items():
        positions = [row["line_in_page"] for row in page_rows]
        assert positions == list(range(1, len(positions) + 1)), (
            f"page {page}: line_in_page must be consecutive in file order"
        )
        for row in page_rows:
            expected = f":pdf{page:03d}:l{row['line_in_page']:03d}"
            assert re.search(re.escape(expected) + r"$", row["id"]), (
                f"ID does not match page/line: {row['id']}"
            )

    narrative = [row for row in rows if row["classification"] == "narrative"]
    words = sum(len(re.findall(r"\b[\w’'-]+\b", row.get("en", ""), re.UNICODE)) for row in narrative)
    print(json.dumps({
        "file": str(args.jsonl),
        "pdf_sha256": digest,
        "pages": args.pages,
        "rows": len(rows),
        "narrative_lines": len(narrative),
        "english_words": words,
        "classifications": Counter(row["classification"] for row in rows),
        "transcription_statuses": Counter(row["transcription_status"] for row in rows),
    }, ensure_ascii=False, default=dict))


if __name__ == "__main__":
    main()
