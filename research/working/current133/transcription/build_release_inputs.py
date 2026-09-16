#!/usr/bin/env python3
"""Build the line-accounted unique current-133 prefix and release descriptor."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
WORK = ROOT / "research/working/current133/transcription"
EXTRACTION = ROOT / "sources/extracted/sayakbay-ms-current133.lines.jsonl"
BATCH = ROOT / "corpus/batches/pages-manuscript133-missing-prefix.json"
ENGLISH = ROOT / "corpus/batches/pages-manuscript133-missing-prefix.en.txt"
SHA = "c276b5bb9f9e4a45ceaf79726e4eee0b0cf062b1c30407cda33740dce1840b4d"
URL = "https://manuscript.bizdin.kg/static/media/pdf/web-133-Seitek-1-bolum-Saiakba-Karalaev.pdf"


def read_page(page: int) -> list[dict]:
    path = WORK / f"page-{page:03}.reviewed.jsonl"
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> None:
    translated = []
    for page in range(6, 38):
        rows = read_page(page)
        assert [row["line_in_page"] for row in rows] == list(range(1, len(rows) + 1))
        assert all(row["page"] == page and row["pdf_sha256"] == SHA for row in rows)
        assert all(row["raw"] == row["text"] and row["en"].strip() for row in rows)
        translated.extend(rows)

    withheld = []
    for line_no in range(1, 37):
        withheld.append({
            "id": f"sayakbay-ms-current133:pdf004:l{line_no:03}",
            "source_id": "sayakbay-ms-current133",
            "pdf_sha256": SHA,
            "page": 4,
            "folio": 1,
            "line_in_page": line_no,
            "raw": "[?]",
            "text": "[?]",
            "en": "",
            "classification": "narrative",
            "transcription_status": "unreadable",
            "uncertainty_note": "Position preserved in page-004.withheld.md; dependable source reading and English remain unavailable.",
            "bbox": None,
        })
    missing_leaf = {
        "id": "sayakbay-ms-current133:folio002:missing-scan",
        "source_id": "sayakbay-ms-current133",
        "pdf_sha256": SHA,
        "page": 5,
        "folio": 2,
        "line_in_page": 1,
        "raw": "[folio 2 absent from recovered scan; narrative line count unknown]",
        "text": "[folio 2 absent from recovered scan; narrative line count unknown]",
        "en": "",
        "classification": "nonverse",
        "transcription_status": "unreadable",
        "uncertainty_note": "PDF pages 4 and 5 are duplicate photographs of folio 1; the next distinct image is folio 3.",
        "bbox": None,
    }
    extraction = withheld + [missing_leaf] + translated
    EXTRACTION.parent.mkdir(parents=True, exist_ok=True)
    EXTRACTION.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in extraction))

    source_ids = [row["id"] for row in translated]
    exclusions = [{
        "id": row["id"],
        "kind": "unresolved_source",
        "reason": "Source position is registered in the unresolved manuscript-prefix gap; no English translation or release credit is assigned.",
    } for row in withheld + [missing_leaf]]
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
            source_ids[0]: "Completion-first direct transcription of the securely missing pre-edition prefix; historical Latin-script readings remain provisional."
        },
        "transcription_check": {
            "method": "visual-pdf-comparison",
            "checked_by": "Codex",
            "date": "2026-09-16",
            "pdf_pages": list(range(6, 38)),
            "details": "Every visible main-leaf narrative baseline on PDF pages 6-37 was retained; exposed underlying-leaf repetitions were excluded. PDF page 4 is explicitly unresolved and page 5 duplicates it; folio 2 is absent from the recovered scan.",
        },
        "after_id": "semetey-2-2013:p1418:b004:l035",
    }
    BATCH.write_text(json.dumps(descriptor, ensure_ascii=False, indent=2) + "\n")
    ENGLISH.write_text("\n".join(row["en"] for row in translated) + "\n")
    words = sum(len(re.findall(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*", row["en"])) for row in translated)
    print(json.dumps({"translated_lines": len(translated), "english_words": words,
                      "unreadable_positions": len(withheld), "missing_leaf_sentinels": 1}))


if __name__ == "__main__":
    main()
