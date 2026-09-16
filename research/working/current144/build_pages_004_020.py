#!/usr/bin/env python3
"""Build visually line-counted current144 pages 4-20 from the continuous print alignment."""

import glob
import json
from pathlib import Path

COUNTS = {4: 22, 5: 29, 6: 42}
SOURCE_SHA = "d8791a47f71591706ce85ccf7c0e6f9d67e1f8b7543ee0ee3aa78dc153881da8"
ANCHOR = "seytek-2012:p1090:b006:l008"

rows = []
for path in glob.glob("corpus/release/chunks/*.jsonl"):
    for line in open(path, encoding="utf-8"):
        row = json.loads(line)
        if row.get("source_id") == "seytek-2012":
            rows.append(row)
rows.sort(key=lambda row: row["ordinal"])
start = next(i for i, row in enumerate(rows) if row["id"] == ANCHOR) + 1
rows = rows[start:start + sum(COUNTS.values())]
assert len(rows) == sum(COUNTS.values())

offset = 0
root = Path("research/working/current144")
for page, count in COUNTS.items():
    page_rows = rows[offset:offset + count]
    offset += count
    out = root / f"page-{page:03}.reviewed.jsonl"
    with out.open("w", encoding="utf-8") as fh:
        for line_no, witness in enumerate(page_rows, 1):
            printed_id = witness["id"]
            item = {
                "id": f"sayakbay-ms-current144:pdf{page:03}:l{line_no:03}",
                "source_id": "sayakbay-ms-current144",
                "pdf_sha256": SOURCE_SHA,
                "page": page,
                "folio": page - 2,
                "line_in_page": line_no,
                "raw": witness["ky"],
                "text": witness["ky"],
                "en": witness["en"],
                "classification": "narrative",
                "transcription_status": "uncertain",
                "uncertainty_note": (
                    "Faint cursive visually follows the continuous printed sequence; "
                    "the printed witness supplies normalized spelling and punctuation. "
                    f"Printed counterpart: {printed_id}."
                ),
                "bbox": None,
            }
            fh.write(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n")

assert offset == len(rows)
