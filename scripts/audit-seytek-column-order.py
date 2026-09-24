#!/usr/bin/env python3
"""Audit printed Seytek page-batch order against PDF extraction coordinates.

Read-only. Emits JSON to stdout; redirect it to save a report. The coordinate
patterns are leads, while the four annotated PDF samples were checked visually.
"""
import collections
import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTRACTION = ROOT / "sources/extracted/seytek-2012.lines.jsonl"
BATCH_GLOB = str(ROOT / "corpus/batches/pages-seytek-*.json")
RELEASE_INDEX = ROOT / "corpus/release/index.json"


def read_jsonl(path):
    with path.open() as stream:
        for line in stream:
            yield json.loads(line)


def main():
    source = {row["id"]: row for row in read_jsonl(EXTRACTION)}
    index = json.loads(RELEASE_INDEX.read_text())
    release_pos = {}
    ordinal = 0
    for chunk in index["chunks"]:
        for row in read_jsonl(ROOT / "corpus/release/chunks" / chunk["file"]):
            for source_id in row.get("source_line_ids", [row["id"]]):
                if source_id.startswith("seytek-2012:p"):
                    release_pos.setdefault(source_id, ordinal)
            ordinal += 1

    pages = []
    patterns = collections.Counter()
    category_rows = collections.Counter()
    category_released = collections.Counter()
    for path in sorted(map(Path, glob.glob(BATCH_GLOB))):
        batch = json.loads(path.read_text())
        ids = batch["source_ids"]
        page = int(re.search(r"(\d{4})\.json$", path.name).group(1))
        sides = ["L" if source[id]["bbox"]["xMin"] < 250 else "R" for id in ids]
        pattern = "".join(side for i, side in enumerate(sides) if i == 0 or side != sides[i - 1]) or "empty"
        category = {"RL": "geometry_right_before_left", "LR": "geometry_left_before_right", "empty": "empty"}.get(
            pattern, "mixed_geometry_requires_individual_review"
        )
        present = [id for id in ids if id in release_pos]
        record = {
            "page": page, "category": category, "column_transition_pattern": pattern,
            "batch_status": batch["status"], "batch_rows": len(ids),
            "release_rows_present": len(present),
        }
        if category not in ("empty", "geometry_left_before_right"):
            left = [id for id, side in zip(ids, sides) if side == "L"]
            right = [id for id, side in zip(ids, sides) if side == "R"]
            record.update({
                "left_rows": len(left), "right_rows": len(right),
                "first_source_id": ids[0], "last_source_id": ids[-1],
                "first_left_id": left[0] if left else None,
                "first_right_id": right[0] if right else None,
                "release_order_matches_batch": (
                    all(release_pos[ids[i]] < release_pos[ids[i + 1]] for i in range(len(ids) - 1))
                    if len(present) == len(ids) else None
                ),
            })
        pages.append(record)
        patterns[pattern] += 1
        category_rows[category] += len(ids)
        category_released[category] += len(present)

    samples = [
        {"page": 26, "geometry_pattern": "RL", "finding": "verified right-before-left narrative-order error",
         "visual_anchor": "PDF left begins Ал жанында жөкөрү*; right begins Коктудан туман табылат,; batch begins right.",
         "continuity_anchor": "Page 25 right ends Эр Кыяздын койнуна; page 26 left begins Ал жанында жөкөрү*."},
        {"page": 104, "geometry_pattern": "LR", "finding": "verified left-before-right control",
         "visual_anchor": "PDF and batch both begin on left with Көңүлү кетти бөлүнүп,; right begins Толтура сөйкө таш кайрат.",
         "continuity_anchor": "Page 103 right ends Ак ордого киргенде; page 104 left begins Көңүлү кетти бөлүнүп,."},
        {"page": 744, "geometry_pattern": "RL", "finding": "verified right-before-left narrative-order error",
         "visual_anchor": "PDF left begins Семетей уулу эр Сейтек,; right begins Жадааланган доңузуң; batch begins right.",
         "continuity_anchor": "Page 743 right ends Алманбет уулу Күлчоро,; page 744 left begins Семетей уулу эр Сейтек,."},
        {"page": 985, "geometry_pattern": "RL", "finding": "verified right-before-left narrative-order error",
         "visual_anchor": "PDF left begins Таш майданда чабыштың,; right begins Сынчыларга каратып,; batch begins right.",
         "continuity_anchor": "Page 985 left ends Минтип жанын күйгүзүп,; its right begins Сынчыларга каратып,."},
    ]
    report = {
        "source_pdf": "sources/raw/seytek-2012.pdf",
        "extraction": str(EXTRACTION.relative_to(ROOT)),
        "release_index": str(RELEASE_INDEX.relative_to(ROOT)),
        "method": "Classify each batch source ID by extracted bbox.xMin < 250 (left), then collapse adjacent side labels. Check each ID and its order in local release shards. Geometry alone does not prove narrative order; visual and syntax anchors prove the listed samples.",
        "scope_note": "The local release candidate is not necessarily the live deployment. Manually review mixed pages, annotations, and each page before canonical reordering.",
        "batch_count": len(pages),
        "pattern_counts": dict(patterns),
        "category_row_counts": dict(category_rows),
        "category_release_row_counts": dict(category_released),
        "visual_samples": samples,
        "pages": pages,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
