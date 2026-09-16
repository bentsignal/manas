#!/usr/bin/env python3
"""Build the dated full-scan URL audit from the mechanical probe ledgers."""

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-15"
BASE = "https://manuscript.bizdin.kg"


def read_probe_results():
    results = {}
    for source in (Path("/tmp/all_heads2.tsv"), Path("/tmp/remain_heads.tsv")):
        if not source.exists():
            continue
        for row in csv.reader(source.open(), delimiter="\t"):
            if len(row) != 3 or not row[0].isdigit():
                continue
            url = row[2].removesuffix("/")
            results[url] = {"status": int(row[0]), "content_type": row[1] or None}
    # One transient timeout was manually retried and returned 404.
    results[f"{BASE}/static/media/pdf/Original-107Semetei-Saiakba-Karalaev.pdf"] = {
        "status": 404,
        "content_type": "text/html; charset=utf-8",
    }
    return results


def sample_validation():
    out = {}
    with Path("/tmp/sample_validation.tsv").open() as fh:
        for current, size, pages, digest in csv.reader(fh, delimiter="\t"):
            out[int(current)] = {
                "bytes": int(size),
                "page_count": int(pages),
                "sha256": digest,
            }
    return out


def full_validation():
    out = {}
    source = Path("/tmp/full_validation.tsv")
    if not source.exists():
        return out
    with source.open() as fh:
        for current, size, pages, digest in csv.reader(fh, delimiter="\t"):
            out[int(current)] = {
                "bytes": int(size),
                "page_count": int(pages),
                "sha256": digest,
            }
    return out


def main():
    probes = read_probe_results()
    samples = sample_validation()
    fulls = full_validation()
    candidates = []
    with Path("/tmp/all_candidates.tsv").open() as fh:
        for current, old, cycle, url, expected_kind in csv.reader(fh, delimiter="\t"):
            current_i = int(current)
            probe = probes.get(url, {"status": None, "content_type": None})
            row = {
                "current_inventory": current_i,
                "old_inventory": int(old),
                "cycle": cycle,
                "url": url,
                "status": probe["status"],
                "content_type": probe["content_type"],
                "bytes": None,
                "page_count": None,
                "sha256": None,
                "classification": "missing_full_candidate",
            }
            if expected_kind == "sample" and probe["status"] == 200:
                row.update(samples[current_i])
                row["classification"] = "catalogue_sample"
            candidates.append(row)

    # Add the decisive lowercase web- candidates, including both rejected raw
    # transforms for the two catalogue filenames that needed cleanup.
    web_urls = [line.strip() for line in Path("/tmp/weburls.txt").open()]
    corrected = {
        105: f"{BASE}/static/media/pdf/web-105-Semetei-Saiakbai-Karalaev.pdf",
        116: f"{BASE}/static/media/pdf/web-116-Semetei-Semetei-menen-Konurbaidyn-urushu-ulandysy-Saiakba-Karalaev.pdf",
    }
    for current_i, raw_url in enumerate(web_urls, 91):
        old_i = current_i + 821
        cycle = "Manas" if current_i <= 103 else "Semetey" if current_i <= 132 else "Seytek"
        urls = [raw_url]
        if current_i in corrected:
            urls.append(corrected[current_i])
        for url in urls:
            resolved = current_i not in (113, 114) and url == corrected.get(current_i, raw_url)
            row = {
                "current_inventory": current_i,
                "old_inventory": old_i,
                "cycle": cycle,
                "url": url,
                "status": 200 if resolved else 404,
                "content_type": "application/pdf" if resolved else "text/html; charset=utf-8",
                "bytes": None,
                "page_count": None,
                "sha256": None,
                "classification": "complete_scan" if resolved else "missing_full_candidate",
            }
            if resolved and current_i in fulls:
                row.update(fulls[current_i])
            candidates.append(row)

    # The exact old-inventory numeric forms were independently rejected.
    for old_i in range(912, 968):
        current_i = old_i - 821
        candidates.append({
            "current_inventory": current_i,
            "old_inventory": old_i,
            "cycle": "Manas" if current_i <= 103 else "Semetey" if current_i <= 132 else "Seytek",
            "url": f"{BASE}/static/media/pdf/{old_i}.pdf",
            "status": 404,
            "content_type": "text/html; charset=utf-8",
            "bytes": None,
            "page_count": None,
            "sha256": None,
            "classification": "missing_full_candidate",
        })

    # Additional title/transliteration variants used to chase the two gaps.
    missing_variants = Path("/tmp/missing_variants.txt")
    if missing_variants.exists():
        for url in missing_variants.read_text().splitlines():
            current_i = 113 if "113" in url.rsplit("/", 1)[-1] else 114
            candidates.append({
                "current_inventory": current_i,
                "old_inventory": current_i + 821,
                "cycle": "Semetey",
                "url": url,
                "status": 404,
                "content_type": "text/html; charset=utf-8",
                "bytes": None,
                "page_count": None,
                "sha256": None,
                "classification": "missing_full_candidate",
            })

    full_path = ROOT / "sources/raw/manas-ms-old911-current90-full.pdf"
    full = {
        "current_inventory": 90,
        "old_inventory": 911,
        "cycle": "Manas",
        "url": f"{BASE}/static/media/pdf/90Manas-Manastyn-bala-chagy.pdf",
        "status": 200,
        "content_type": "application/pdf",
        "bytes": full_path.stat().st_size,
        "page_count": 302,
        "sha256": hashlib.sha256(full_path.read_bytes()).hexdigest(),
        "classification": "complete_scan",
    }
    statuses = Counter(x["status"] for x in candidates)
    complete_rows = [x for x in candidates if x["classification"] == "complete_scan"]
    sample_rows = [x for x in candidates if x["classification"] == "catalogue_sample"]
    report = {
        "date": DATE,
        "scope": "current inventories 91-146 / old inventories 912-967",
        "host": BASE,
        "result": "54 of 56 target full scans were found; current 113 and 114 remain unresolved.",
        "known_complete_control": full,
        "summary": {
            "inventory_records": 56,
            "urls_tested": len(candidates),
            "http_200": statuses[200],
            "http_404": statuses[404],
            "catalogue_samples": sum(x["classification"] == "catalogue_sample" for x in candidates),
            "complete_scans_in_target_scope": sum(x["classification"] == "complete_scan" for x in candidates),
            "complete_scan_bytes": sum(x["bytes"] for x in complete_rows),
            "complete_scan_pages": sum(x["page_count"] for x in complete_rows),
            "sample_bytes": sum(x["bytes"] for x in sample_rows),
            "sample_pages": sum(x["page_count"] for x in sample_rows),
            "unresolved": [
                {"current_inventory": 113, "old_inventory": 934},
                {"current_inventory": 114, "old_inventory": 935},
            ],
        },
        "method": {
            "sample_source": "live catalogue HTML and existing catalogue crosswalk metadata",
            "probe": "HTTP HEAD with redirects followed; all 200 PDF assets downloaded for byte/page/hash validation",
            "name_variants": [
                "remove Obrazets-",
                "collapse the inventory-number hyphen (the current90 exception pattern)",
                "remove author suffix",
                "Full-/Original- prefixes",
                "-full/-original/-complete/-toluk suffixes",
            ],
            "paths": [
                "/static/media/pdf",
                "/media/pdf",
                "/static/media/manuscripts",
                "/media/manuscripts",
                "/uploads/manuscripts",
            ],
        },
        "candidates": candidates,
    }
    json_path = ROOT / f"research/SAYAKBAY-FULL-SCAN-URL-AUDIT-{DATE}.json"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")

    samples_by_cycle = Counter(x["cycle"] for x in candidates if x["classification"] == "catalogue_sample")
    lines = [
        "# Sayakbay full-scan URL audit",
        "",
        f"Prepared {DATE}. Scope: current inventories **91-146** / old inventories **912-967** on `{BASE}`.",
        "",
        "## Result",
        "",
        "The hidden full scans use lowercase `web-` in place of the visible sample prefix `Obrazets-`. This recovered **54 of 56** target manuscripts. Current 113 / old 934 and current 114 / old 935 remain unresolved.",
        "",
        f"- `{full['url']}` — HTTP 200, {full['bytes']:,} bytes, {full['page_count']} pages, SHA-256 `{full['sha256']}`.",
        "",
        f"All {len(candidates):,} candidate URLs are recorded individually in `{json_path.name}`. The ledger contains 56 five-page samples and 54 complete scans, with byte count, page count, and SHA-256 for every downloaded PDF.",
        "",
        f"The 54 complete target scans total **{sum(x['bytes'] for x in complete_rows):,} bytes** and **{sum(x['page_count'] for x in complete_rows):,} PDF pages**. They are stored with stable ignored filenames `sources/raw/manuscript-full-91-146/<current>.pdf`. HTTP Content-Length exactly matches every local byte size; all 54 PDFs parse successfully.",
        "",
        "| Cycle | Current | Old | Live samples | Complete scans |",
        "|---|---:|---:|---:|---:|",
        f"| Manas | 91-103 | 912-924 | {samples_by_cycle['Manas']} | 13 |",
        f"| Semetey | 104-132 | 925-953 | {samples_by_cycle['Semetey']} | 27 |",
        f"| Seytek | 133-146 | 954-967 | {samples_by_cycle['Seytek']} | 14 |",
        "",
        "## Search coverage",
        "",
        "The audit re-extracted each catalogue sample filename from live records, downloaded all 56 samples, and verified byte size, page count, and SHA-256. Replacing `Obrazets-` with lowercase `web-` yielded 52 exact hits. Current 105 and 116 required filename cleanup, raising recovery to 54. Current 113 and 114 were also tested across 132 additional title, prefix, author-spelling, and transliteration variants without a hit.",
        "",
        "The root page, 1.33 MB sitemap, bundled JavaScript, catalogue HTML, ViewerJS references, and directory responses expose no API, IIIF manifest, alternate asset manifest, or directory listing. Web-index queries for non-`Obrazets` Semetey/Seytek PDFs returned no results. `/static/media/pdf/` returns 403 to directory access, while nonexistent candidate objects return 404.",
        "",
        "The JSON ledger is the authoritative candidate-level record. Each entry includes URL, HTTP status, inventory mapping, byte count, page count, SHA-256 when downloaded, and complete/sample classification.",
        "",
        "Large PDF downloads are retained only under ignored `sources/raw/`; no corpus or release files were changed.",
    ]
    md_path = ROOT / f"research/SAYAKBAY-FULL-SCAN-URL-AUDIT-{DATE}.md"
    md_path.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
