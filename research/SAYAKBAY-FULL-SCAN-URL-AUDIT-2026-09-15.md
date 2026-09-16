# Sayakbay full-scan URL audit

Prepared 2026-09-15. Scope: current inventories **91-146** / old inventories **912-967** on `https://manuscript.bizdin.kg`.

## Result

The hidden full scans use lowercase `web-` in place of the visible sample prefix `Obrazets-`. This recovered **54 of 56** target manuscripts. Current 113 / old 934 and current 114 / old 935 remain unresolved.

- `https://manuscript.bizdin.kg/static/media/pdf/90Manas-Manastyn-bala-chagy.pdf` — HTTP 200, 122,640,613 bytes, 302 pages, SHA-256 `abe0b9bd1dfdcac97d6c3b2a32f30f7efaafc12850dd283e4f71ffe98709c013`.

All 2,139 candidate URLs are recorded individually in `SAYAKBAY-FULL-SCAN-URL-AUDIT-2026-09-15.json`. The ledger contains 56 five-page samples and 54 complete scans, with byte count, page count, and SHA-256 for every downloaded PDF.

The 54 complete target scans total **5,153,087,442 bytes** and **12,394 PDF pages**. They are stored with stable ignored filenames `sources/raw/manuscript-full-91-146/<current>.pdf`. HTTP Content-Length exactly matches every local byte size; all 54 PDFs parse successfully.

| Cycle | Current | Old | Live samples | Complete scans |
|---|---:|---:|---:|---:|
| Manas | 91-103 | 912-924 | 13 | 13 |
| Semetey | 104-132 | 925-953 | 29 | 27 |
| Seytek | 133-146 | 954-967 | 14 | 14 |

## Search coverage

The audit re-extracted each catalogue sample filename from live records, downloaded all 56 samples, and verified byte size, page count, and SHA-256. Replacing `Obrazets-` with lowercase `web-` yielded 52 exact hits. Current 105 and 116 required filename cleanup, raising recovery to 54. Current 113 and 114 were also tested across 132 additional title, prefix, author-spelling, and transliteration variants without a hit.

The root page, 1.33 MB sitemap, bundled JavaScript, catalogue HTML, ViewerJS references, and directory responses expose no API, IIIF manifest, alternate asset manifest, or directory listing. Web-index queries for non-`Obrazets` Semetey/Seytek PDFs returned no results. `/static/media/pdf/` returns 403 to directory access, while nonexistent candidate objects return 404.

The JSON ledger is the authoritative candidate-level record. Each entry includes URL, HTTP status, inventory mapping, byte count, page count, SHA-256 when downloaded, and complete/sample classification.

Large PDF downloads are retained only under ignored `sources/raw/`; no corpus or release files were changed.
