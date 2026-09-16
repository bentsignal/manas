#!/usr/bin/env python3
"""Build inventory-143 extraction, conservative overlap map, batch, and gap evidence."""

from collections import defaultdict
import json
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "research/working/current143"
PRINTED = ROOT / "sources/extracted/seytek-2012.lines.jsonl"
EXTRACTION = ROOT / "sources/extracted/sayakbay-ms-current143.lines.jsonl"
OVERLAPS = WORK / "release-overlap-map.json"
GAP = WORK / "unreadable-gap.json"
BATCH = ROOT / "corpus/batches/pages-manuscript143-0003-0190.json"
ENGLISH = ROOT / "corpus/batches/pages-manuscript143-0003-0190.en.txt"
SHA = "db22e2a5274260d0d1a06f22082ce535758ff594af9dc4843a57782d50547221"
URL = "https://manuscript.bizdin.kg/static/media/pdf/web-143-Seitek-Saiakba-Karalaev.pdf"
NOTE_COUNTERPART = re.compile(r"(seytek-2012:p\d+:b\d+:l\d+)")
WORDS = re.compile(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*")
UNREADABLE_ID = "sayakbay-ms-current143:pdf086:l035"


def normalized(text: str) -> str:
    text = unicodedata.normalize("NFC", text).casefold().replace("ё", "е")
    text = text.replace("[", "").replace("]", "")
    return re.sub(r"[^а-яңөүa-z0-9]+", "", text)


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> None:
    rows = []
    for page in range(3, 191):
        path = WORK / f"page-{page:03}.reviewed.jsonl"
        page_rows = load_jsonl(path)
        assert [row["line_in_page"] for row in page_rows] == list(range(1, len(page_rows) + 1))
        assert all(row["page"] == page and row["pdf_sha256"] == SHA for row in page_rows)
        assert all(row["classification"] in {"narrative", "heading"} for row in page_rows)
        assert all(row["en"].strip() for row in page_rows)
        rows.extend(page_rows)
    assert len(rows) == 6859
    assert len({row["id"] for row in rows}) == len(rows)

    printed = load_jsonl(PRINTED)
    printed_by_id = {row["id"]: row for row in printed}
    manuscript_by_id = {row["id"]: row for row in rows}

    # PDF page 22 is a second scan position for the identical folio photographed
    # again at PDF page 161. Preserve it in the extraction, but never count the
    # same physical leaf twice in the release.
    p22 = [row for row in rows if row["page"] == 22]
    p161 = [row for row in rows if row["page"] == 161]
    assert len(p22) == len(p161) == 31
    assert [row["text"] for row in p22] == [row["text"] for row in p161]
    scan_duplicates = {left["id"]: right["id"] for left, right in zip(p22, p161)}

    canonical = [row for row in rows if row["page"] != 22 and row["id"] != UNREADABLE_ID]
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

    # Workers recorded individually inspected printed positions. Accept those
    # only when the normalized source string is exact and the printed position
    # has not already been used.
    for row in canonical:
        match = NOTE_COUNTERPART.search(row.get("uncertainty_note", ""))
        if not match or match.group(1) not in printed_by_id:
            continue
        target = printed_by_id[match.group(1)]
        if normalized(row["text"]) == normalized(target["text"]):
            add_pair(row["id"], target["id"], "recorded exact printed counterpart")

    # Add strings that occur exactly once in each complete witness. Formulaic
    # repetitions remain released unless separately anchored.
    for row in canonical:
        key = normalized(row["text"])
        candidates = printed_by_text.get(key, [])
        if key and len(manuscript_by_text[key]) == 1 and len(candidates) == 1:
            add_pair(row["id"], candidates[0]["id"], "unique exact normalized line")

    excluded_ids = set(scan_duplicates) | set(mapped) | {UNREADABLE_ID}
    released = [row for row in rows if row["id"] not in excluded_ids]
    assert released

    exclusions = []
    pairs = []
    for manuscript_id, counterpart_id in scan_duplicates.items():
        exclusions.append({
            "id": manuscript_id,
            "kind": "overlap",
            "reason": (
                "PDF page 22 is an out-of-order duplicate photograph of folio 2621 at PDF page 161; "
                f"retained in the extraction and not counted twice ({counterpart_id})."
            ),
            "counterpart_id": counterpart_id,
        })
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
    exclusions.append({
        "id": UNREADABLE_ID,
        "kind": "unresolved_source",
        "reason": "The source photograph cuts through this bottom narrative baseline; no honest reading is visible.",
    })

    EXTRACTION.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    OVERLAPS.write_text(json.dumps({
        "source_id": "sayakbay-ms-current143",
        "scanned_text_rows": len(rows),
        "duplicate_scan_rows": len(scan_duplicates),
        "canonical_physical_text_rows": len(rows) - len(scan_duplicates),
        "catalogue_line_tally": 6827,
        "catalogue_difference": len(rows) - len(scan_duplicates) - 6827,
        "secure_printed_overlaps": len(pairs),
        "unreadable_rows": 1,
        "released_manuscript_rows": len(released),
        "method": (
            "Exact individually recorded printed counterparts plus normalized strings unique in both witnesses. "
            "Repeated formulas without a position anchor remain released. PDF page 22 is excluded as a verified "
            "duplicate of page 161; the cut-off page-86 baseline remains an explicit unresolved source row."
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
                "Completion-first direct transcription of current inventory 143. Handwritten readings and "
                "English remain provisional; bracketed phrases require specialist review."
            )
        },
        "transcription_check": {
            "method": "visual-pdf-comparison",
            "checked_by": "Codex workers; same-agent validation and parent sampling",
            "date": "2026-09-16",
            "pdf_pages": list(range(3, 191)),
            "details": (
                "Every visible narrative or genuine heading baseline on PDF pages 3-190 was retained in source "
                "order. Page 22 duplicates page 161; expected folio 2482 is absent from the scan but is represented "
                "by the translated printed witness. One page-86 baseline is cut off and explicitly unresolved. "
                "No independent specialist review."
            ),
        },
        "after_id": "seytek-1991-continuation:p0348:b002:l024",
    }
    BATCH.write_text(json.dumps(descriptor, ensure_ascii=False, indent=2) + "\n")
    ENGLISH.write_text("\n".join(row["en"] for row in released) + "\n")

    # The gap anchors are the nearest released manuscript rows around the cut
    # position. They become adjacent after overlaps and the unreadable row are
    # excluded by the batch descriptor.
    unreadable_index = next(i for i, row in enumerate(rows) if row["id"] == UNREADABLE_ID)
    released_set = set(source_ids)
    before = next(row for row in rows[unreadable_index + 1:] if row["id"] in released_set)
    after = next(row for row in reversed(rows[:unreadable_index]) if row["id"] in released_set)
    unreadable = manuscript_by_id[UNREADABLE_ID]
    GAP.write_text(json.dumps({
        "id": "sayakbay-ms-current143:pdf086:l035:cut-off-baseline",
        "kind": "damaged",
        "status": "unresolved",
        "source_id": "sayakbay-ms-current143",
        "after_id": after["id"],
        "before_id": before["id"],
        "source_line_ids": [UNREADABLE_ID],
        "evidence": "research/working/current143/page-086.reviewed.jsonl; research/working/current143/AUDIT.md",
        "source": {
            "url": URL,
            "page": 86,
            "sha256": SHA,
            "segments": [{"id": UNREADABLE_ID, "raw": unreadable["raw"], "bbox": unreadable["bbox"]}],
        },
        "note": "The photograph cuts through the bottom narrative baseline. The source position is preserved, but no honest reading or English translation is claimed.",
    }, ensure_ascii=False, indent=2) + "\n")

    print(json.dumps({
        "scanned_text_rows": len(rows),
        "canonical_physical_text_rows": len(rows) - len(scan_duplicates),
        "physical_english_words": sum(len(WORDS.findall(row["en"])) for row in rows),
        "duplicate_scan_rows": len(scan_duplicates),
        "secure_printed_overlaps": len(pairs),
        "unreadable_rows": 1,
        "released_lines": len(released),
        "released_english_words": sum(len(WORDS.findall(row["en"])) for row in released),
        "gap_after": after["id"],
        "gap_before": before["id"],
    }))


if __name__ == "__main__":
    main()
