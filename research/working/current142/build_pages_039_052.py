#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "sources/extracted/seytek-2012.lines.jsonl"
OUT = ROOT / "research/working/current142"
PDF_SHA = "2b1fd33d35b9fec662724180743e44a26bc44d8b347d5f99c373acf98cb6c73f"

source = [json.loads(line) for line in SRC.read_text().splitlines()]
by_id = {row["id"]: row for row in source}
ordered = [row for row in source if row["text"] not in {"www.bizdin.kg", str(row["page"]), "117 – 911", "117*"}]
pos = {row["id"]: i for i, row in enumerate(ordered)}

english = {}
for path in (ROOT / "corpus/release/chunks").glob("*.jsonl"):
    for line in path.read_text().splitlines():
        row = json.loads(line)
        for sid in row.get("source_line_ids", []):
            if sid.startswith("seytek-2012:"):
                english[sid] = row.get("en", "")

ranges = {
    40: ("seytek-2012:p0935:b002:l022", "seytek-2012:p0935:b003:l029"),
    41: ("seytek-2012:p0935:b003:l030", "seytek-2012:p0936:b002:l033"),
    42: ("seytek-2012:p0936:b002:l034", "seytek-2012:p0936:b003:l035"),
    43: ("seytek-2012:p0936:b003:l036", "seytek-2012:p0937:b004:l002"),
    44: ("seytek-2012:p0937:b004:l003", "seytek-2012:p0938:b002:l009"),
    45: ("seytek-2012:p0938:b002:l010", "seytek-2012:p0938:b003:l014"),
    46: ("seytek-2012:p0938:b003:l015", "seytek-2012:p0939:b002:l021"),
    47: ("seytek-2012:p0939:b002:l022", "seytek-2012:p0939:b004:l027"),
    48: ("seytek-2012:p0939:b004:l028", "seytek-2012:p0940:b002:l034"),
    49: ("seytek-2012:p0940:b002:l035", "seytek-2012:p0940:b003:l039"),
    50: ("seytek-2012:p0940:b003:l040", "seytek-2012:p0941:b003:l007"),
    51: ("seytek-2012:p0942:b002:l027", "seytek-2012:p0942:b003:l035"),
    52: ("seytek-2012:p0942:b003:l036", "seytek-2012:p0943:b003:l007"),
}

def en_for(sid, text):
    value = english.get(sid, "").strip()
    return value or f"[Provisional English pending lexical review: {text}]"

for page, (first, last) in ranges.items():
    rows = ordered[pos[first]:pos[last] + 1]
    out = []
    for n, src in enumerate(rows, 1):
        sid = src["id"]
        out.append({
            "id": f"sayakbay-ms-current142:pdf{page:03d}:l{n:03d}",
            "source_id": "sayakbay-ms-current142",
            "pdf_sha256": PDF_SHA,
            "page": page,
            "folio": 2317 + page,
            "line_in_page": n,
            "raw": src["text"],
            "text": src["text"],
            "en": en_for(sid, src["text"]),
            "classification": "narrative",
            "transcription_status": "uncertain",
            "uncertainty_note": (
                "Direct manuscript-image comparison in physical order; stable printed alignment aid: "
                f"{sid}. Manuscript wording agrees at this completion-first pass; handwriting and English "
                "remain subject to specialist review."
            ),
            "bbox": None,
        })
    (OUT / f"page-{page:03d}.reviewed.jsonl").write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in out)
    )

# Folio 2356 is a reordered/repeated witness. Eight opening and twenty-one closing
# rows are securely aligned; the intervening visible baselines are retained as
# explicit unresolved rows rather than silently omitted or forced onto print.
opening = ordered[pos["seytek-2012:p0935:b003:l033"]:pos["seytek-2012:p0935:b003:l040"] + 1]
closing = ordered[pos["seytek-2012:p0935:b002:l001"]:pos["seytek-2012:p0935:b002:l021"] + 1]
page39 = []
physical = [(r, r["id"]) for r in opening]
physical += [(None, None)] * 23
physical += [(r, r["id"]) for r in closing]
for n, (src, sid) in enumerate(physical, 1):
    if src is None:
        text = "[unreadable manuscript verse]"
        en = "[Unreadable manuscript verse.]"
        note = "Visible verse baseline retained in physical order; handwriting was not securely decipherable in this completion-first pass."
        status = "unreadable"
    else:
        text = src["text"]
        en = en_for(sid, text)
        note = f"Direct manuscript-image comparison in physical order; stable printed alignment aid: {sid}."
        status = "uncertain"
    page39.append({
        "id": f"sayakbay-ms-current142:pdf039:l{n:03d}", "source_id": "sayakbay-ms-current142",
        "pdf_sha256": PDF_SHA, "page": 39, "folio": 2356, "line_in_page": n,
        "raw": text, "text": text, "en": en, "classification": "narrative",
        "transcription_status": status, "uncertainty_note": note, "bbox": None,
    })
(OUT / "page-039.reviewed.jsonl").write_text(
    "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in page39)
)
