#!/usr/bin/env python3
"""Build the conservative current144 page ledger and secure printed crosswalk."""

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMAGES = ROOT / "ledger-images"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


with (ROOT / "scan-page-ledger.csv").open("w", newline="", encoding="utf-8") as out:
    writer = csv.DictWriter(
        out,
        fieldnames=["pdf_page", "observed_folio", "image", "image_sha256", "baseline_status", "secure_baselines"],
    )
    writer.writeheader()
    for pdf_page in range(3, 194):
        image = IMAGES / f"page-{pdf_page:03}.jpg"
        writer.writerow(
            {
                "pdf_page": pdf_page,
                # Do not interpolate folios: 191 verse-bearing images are present
                # for a catalogue extent of 190 pages, so the extra/repeated image
                # must be resolved visually before a complete folio sequence is claimed.
                "observed_folio": {3: 1, 4: 2, 5: 3, 193: 190}.get(pdf_page, ""),
                "image": str(image.relative_to(ROOT)),
                "image_sha256": digest(image),
                "baseline_status": "partial-manual" if pdf_page in (3, 100) else "unsegmented",
                "secure_baselines": 17 if pdf_page == 3 else (24 if pdf_page == 100 else 0),
            }
        )

opening_ids = [f"seytek-2012:p1090:b005:l{i:03}" for i in range(1, 18)]
middle_ids = [f"seytek-2012:p1123:b004:l{i:03}" for i in range(24, 41)]
middle_ids += [f"seytek-2012:p1124:b002:l{i:03}" for i in range(1, 8)]

pairs = []
for line, printed in enumerate(opening_ids, 1):
    pairs.append({"manuscript_id": f"sayakbay-ms-current144:pdf003:l{line:03}", "printed_id": printed})
for line, printed in enumerate(middle_ids, 2):
    pairs.append({"manuscript_id": f"sayakbay-ms-current144:pdf100:l{line:03}", "printed_id": printed})

payload = {
    "source": "sources/raw/manuscript-full-91-146/144.pdf",
    "source_sha256": "d8791a47f71591706ce85ccf7c0e6f9d67e1f8b7543ee0ee3aa78dc153881da8",
    "catalogue_physical_positions": 6092,
    "method": "manual visual one-to-one comparison; exact ordered printed strings; no OCR acceptance",
    "secure_pairs": len(pairs),
    "unresolved_catalogue_positions": 6092 - len(pairs),
    "pairs": pairs,
}
(ROOT / "secure-monotonic-crosswalk.json").write_text(
    json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
