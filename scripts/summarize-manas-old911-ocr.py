#!/usr/bin/env python3
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

work = Path(sys.argv[1])
rows = []
for path in sorted((work / "ocr").glob("page-*.txt")):
    page = int(path.stem.rsplit("-", 1)[1])
    text = path.read_text(errors="replace")
    rows.append({
        "pdf_page": page,
        "image": str(work / "images" / f"page-{page:03d}.jpg"),
        "ocr_text": text,
        "ocr_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "nonblank_lines": sum(bool(x.strip()) for x in text.splitlines()),
        "status": "unreviewed-machine-ocr",
    })
checkpoint = {
    "date": date.today().isoformat(),
    "source_id": "manas-ms-old911-current90",
    "source_sha256": "abe0b9bd1dfdcac97d6c3b2a32f30f7efaafc12850dd283e4f71ffe98709c013",
    "pdf_pages_expected": 302,
    "pdf_pages_ocr_complete": len(rows),
    "ocr_engine": "tesseract 5 eng psm6 baseline",
    "warning": "Historical handwritten Latin-script Kyrgyz is outside this OCR model's reliable domain. Text is discovery-only and cannot establish novel verses without image review.",
    "pages": rows,
}
(work / "checkpoint.json").write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"pages": len(rows), "checkpoint": str(work / "checkpoint.json")}))
