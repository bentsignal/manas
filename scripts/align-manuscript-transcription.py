#!/usr/bin/env python3
"""Find exact and near-exact manuscript lines in an existing source witness.

This is a candidate generator for overlap review. It never decides that a verse
is duplicate by itself; sequence context and the page image remain authoritative.
"""

import argparse
import difflib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path


PLACEHOLDERS = {"[окулбайт]", "[окулбады]", "[unreadable]"}


def norm(value: str) -> str:
    value = unicodedata.normalize("NFC", value).casefold()
    value = re.sub(r"[^\w]+", "", value, flags=re.UNICODE)
    return value


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("witness", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--threshold", type=float, default=0.76)
    args = parser.parse_args()

    manuscript = [
        row for row in read_jsonl(args.manuscript)
        if row.get("classification") in {"narrative", "heading"}
        and row.get("text") not in PLACEHOLDERS
        and norm(row.get("text", ""))
    ]
    witness = [row for row in read_jsonl(args.witness) if norm(row.get("text", ""))]
    exact: dict[str, list[int]] = defaultdict(list)
    for index, row in enumerate(witness):
        exact[norm(row["text"])].append(index)

    candidates = []
    for row in manuscript:
        key = norm(row["text"])
        if key in exact:
            matches = [{"index": i, "id": witness[i]["id"], "text": witness[i]["text"], "score": 1.0}
                       for i in exact[key]]
        else:
            scored = []
            # Length filtering makes the simple matcher practical for large witnesses.
            for index, other in enumerate(witness):
                other_key = norm(other["text"])
                if abs(len(key) - len(other_key)) > max(5, len(key) // 2):
                    continue
                score = difflib.SequenceMatcher(None, key, other_key).ratio()
                if score >= args.threshold:
                    scored.append((score, index, other))
            matches = [
                {"index": index, "id": other["id"], "text": other["text"], "score": round(score, 4)}
                for score, index, other in sorted(scored, reverse=True)[:5]
            ]
        candidates.append({
            "manuscript_id": row["id"],
            "manuscript_text": row["text"],
            "matches": matches,
        })

    report = {
        "manuscript": str(args.manuscript),
        "witness": str(args.witness),
        "threshold": args.threshold,
        "readable_manuscript_lines": len(manuscript),
        "lines_with_candidates": sum(bool(item["matches"]) for item in candidates),
        "exact_match_lines": sum(any(match["score"] == 1 for match in item["matches"]) for item in candidates),
        "candidates": candidates,
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
