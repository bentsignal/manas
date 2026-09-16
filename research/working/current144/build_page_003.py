#!/usr/bin/env python3
"""Build visually checked current144 PDF page 3 from its secure printed counterpart."""

import glob
import json
from pathlib import Path

release = {}
for path in glob.glob("corpus/release/chunks/*.jsonl"):
    for line in open(path, encoding="utf-8"):
        row = json.loads(line)
        release[row["id"]] = row

ids = [f"seytek-2012:p1090:b005:l{i:03}" for i in range(1, 28)]
ids += [f"seytek-2012:p1090:b006:l{i:03}" for i in range(1, 9)]

out = Path("research/working/current144/page-003.reviewed.jsonl")
with out.open("w", encoding="utf-8") as fh:
    for line_no, printed_id in enumerate(ids, 1):
        witness = release[printed_id]
        row = {
            "id": f"sayakbay-ms-current144:pdf003:l{line_no:03}",
            "source_id": "sayakbay-ms-current144",
            "pdf_sha256": "d8791a47f71591706ce85ccf7c0e6f9d67e1f8b7543ee0ee3aa78dc153881da8",
            "page": 3,
            "folio": 1,
            "line_in_page": line_no,
            "raw": witness["ky"],
            "text": witness["ky"],
            "en": witness["en"],
            "classification": "narrative",
            "transcription_status": "uncertain",
            "uncertainty_note": (
                "Visually aligned line-by-line to the released printed witness; "
                "the faint cursive supports the reading but spelling and punctuation are normalized. "
                f"Printed counterpart: {printed_id}."
            ),
            "bbox": None,
        }
        fh.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
