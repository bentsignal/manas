#!/usr/bin/env python3
"""Build current-144 extraction, conservative overlap map, and release batch."""

from collections import defaultdict
import json
from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "research/working/current144"
PRINTED = ROOT / "sources/extracted/seytek-2012.lines.jsonl"
EXTRACTION = ROOT / "sources/extracted/sayakbay-ms-current144.lines.jsonl"
OVERLAPS = WORK / "release-overlap-map.json"
BATCH = ROOT / "corpus/batches/pages-manuscript144-0003-0193.json"
ENGLISH = ROOT / "corpus/batches/pages-manuscript144-0003-0193.en.txt"
SHA = "d8791a47f71591706ce85ccf7c0e6f9d67e1f8b7543ee0ee3aa78dc153881da8"
URL = "https://manuscript.bizdin.kg/static/media/pdf/web-144-Seitek-Saiakba-Karalaev.pdf"
NOTE_COUNTERPART = re.compile(r"(seytek-2012:p\d+:b\d+:l\d+)")
WORDS = re.compile(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*")


def normalized(text: str) -> str:
    text = unicodedata.normalize("NFC", text).casefold().replace("ё", "е")
    text = text.replace("[", "").replace("]", "")
    return re.sub(r"[^а-яңөүa-z0-9]+", "", text)


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> None:
    rows = []
    for page in range(3, 194):
        path = WORK / f"page-{page:03}.reviewed.jsonl"
        page_rows = load_jsonl(path)
        assert [row["line_in_page"] for row in page_rows] == list(range(1, len(page_rows) + 1))
        assert all(row["page"] == page and row["pdf_sha256"] == SHA for row in page_rows)
        assert all(row["classification"] == "narrative" and row["en"].strip() for row in page_rows)
        rows.extend(page_rows)
    assert len(rows) == 5828
    assert len({row["id"] for row in rows}) == len(rows)

    printed = load_jsonl(PRINTED)
    printed_by_id = {row["id"]: row for row in printed}
    manuscript_by_id = {row["id"]: row for row in rows}
    manuscript_by_text: dict[str, list[dict]] = defaultdict(list)
    printed_by_text: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        manuscript_by_text[normalized(row["text"])].append(row)
    for row in printed:
        printed_by_text[normalized(row["text"])].append(row)

    mapped: dict[str, dict] = {}
    used_printed: set[str] = set()

    def add_pair(manuscript_id: str, printed_id: str, basis: str) -> None:
        if manuscript_id in mapped or printed_id in used_printed:
            return
        assert manuscript_id in manuscript_by_id
        assert printed_id in printed_by_id
        mapped[manuscript_id] = {"counterpart_id": printed_id, "basis": basis}
        used_printed.add(printed_id)

    strict = json.loads((WORK / "secure-monotonic-crosswalk.json").read_text())
    for pair in strict["pairs"]:
        add_pair(pair["manuscript_id"], pair["printed_id"], "prior manual visual crosswalk")

    # Earlier page work records individually checked printed counterparts. Accept
    # only exact normalized strings and never reuse a printed position.
    for row in rows:
        match = NOTE_COUNTERPART.search(row.get("uncertainty_note", ""))
        if not match or match.group(1) not in printed_by_id:
            continue
        target = printed_by_id[match.group(1)]
        if normalized(row["text"]) == normalized(target["text"]):
            add_pair(row["id"], target["id"], "recorded exact printed counterpart")

    # Add exact strings only when the normalized line occurs once in each
    # witness. Repeated formulas remain released unless separately anchored, so
    # repetition is never discarded merely because its words recur elsewhere.
    for row in rows:
        key = normalized(row["text"])
        candidates = printed_by_text.get(key, [])
        if len(manuscript_by_text[key]) == 1 and len(candidates) == 1:
            add_pair(row["id"], candidates[0]["id"], "unique exact normalized line")

    released = [row for row in rows if row["id"] not in mapped]
    exclusions = []
    pairs = []
    for row in rows:
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

    EXTRACTION.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    OVERLAPS.write_text(json.dumps({
        "source_id": "sayakbay-ms-current144",
        "physical_narrative_lines": len(rows),
        "secure_printed_overlaps": len(pairs),
        "released_manuscript_rows": len(released),
        "method": (
            "Prior visual crosswalks, individually recorded exact printed counterparts, "
            "and normalized strings unique in both witnesses. Repeated formulas without a "
            "position anchor are not excluded."
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
                "Completion-first direct transcription of current inventory 144. "
                "Handwritten readings and English remain provisional; bracketed phrases require review."
            )
        },
        "transcription_check": {
            "method": "visual-pdf-comparison",
            "checked_by": "Codex workers; same-agent validation",
            "date": "2026-09-16",
            "pdf_pages": list(range(3, 194)),
            "details": (
                "Every visible narrative baseline on the 191 verse-bearing images was retained in "
                "physical order. PDF pages 1-2 and 194-195 are cover, title, archive-note, or binding "
                "images. No independent specialist review."
            ),
        },
        "after_id": "seytek-1991-continuation:p0348:b002:l024",
    }
    BATCH.write_text(json.dumps(descriptor, ensure_ascii=False, indent=2) + "\n")
    ENGLISH.write_text("\n".join(row["en"] for row in released) + "\n")

    print(json.dumps({
        "physical_narrative_lines": len(rows),
        "physical_english_words": sum(len(WORDS.findall(row["en"])) for row in rows),
        "secure_overlaps": len(pairs),
        "released_lines": len(released),
        "released_english_words": sum(len(WORDS.findall(row["en"])) for row in released),
    }))


if __name__ == "__main__":
    main()
