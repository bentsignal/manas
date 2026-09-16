# Current 113 / old 934 and current 114 / old 935 recovery check

Checked 2026-09-16 using read-only HTTP GET requests. I re-read `scripts/build-manuscript-full-scan-audit.py`, `research/SAYAKBAY-FULL-SCAN-URL-AUDIT-2026-09-15.{md,json}`, the manuscript inventory/crosswalk, and both live catalogue pages. The earlier audit already tested 204 URL candidates for these two inventories; every full-scan candidate returned HTTP 404. The catalogue pages remain HTTP 200 and still expose only the five-page `Obrazets-` samples.

## Fresh plausible patterns tested

These 26 patterns were not relied upon as inferred successes; each was requested directly.

| URL | HTTP | Content-Type | Bytes |
|---|---:|---|---:|
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-VIt-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-VI-t-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-VItom-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-VI-tom-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-6t-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-6-t-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-6tom-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-6-tom-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-VI-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-6-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-934-Semetei-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-934-Semetei.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-113-Semetei-Saiakba-Karalaev.PDF` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/Web-113-Semetei-Saiakba-Karalaev.PDF` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Semetei-Semetei-menen-Konurbaidyn-urushu-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Semetei-Kanykeidin-sozu-Semetei-menen-Konurbaidyn-urushu-ulandysy-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Semetei-Kanykeidin-sozu-Semetei-menen-Konurbaidyn-urushu-Saiakba-Karalaev-ulandysy.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Kanykeidin-sozu-Semetei-menen-Konurbaidyn-urushu.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Semetei-Kanykeidin-sozu.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Semetei-VIIt-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Semetei-VI-tom-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Semetei-VIItom-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Semetei-7-tom-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-935-Semetei-Saiakba-Karalaev.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-935-Semetei.pdf` | 404 | `text/html; charset=utf-8` | 146 |
| `https://manuscript.bizdin.kg/static/media/pdf/web-114-Semetei-Kanykeidin-sozu-Semetei-menen-Konurbaidyn-urushu-Saiakba-Karalaev.PDF` | 404 | `text/html; charset=utf-8` | 146 |

## Accessible PDFs (samples only)

| Inventory | URL | HTTP | Bytes | Pages | SHA-256 | Classification |
|---|---|---:|---:|---:|---|---|
| current 113 / old 934 | `https://manuscript.bizdin.kg/static/media/pdf/Obrazets-113-Semetei-Saiakba-Karalaev.pdf` | 200 | 1,915,199 | 5 | `cda9ac9487387ea9765bb77d25c81321b0704f38f24c1c3e151fb3708115119a` | catalogue sample, not full inventory |
| current 114 / old 935 | `https://manuscript.bizdin.kg/static/media/pdf/Obrazets-114-Semetei-Kanykeidin-sozu-Semetei-menen-Konurbaidyn-urushu-Saiakba-Karalaev.pdf` | 200 | 2,599,603 | 5 | `87d1667a44db10bdada33494ee463b8f9c9c9599e85b2f5074fa03df98e6f3a7` | catalogue sample, not full inventory |

## Result

No full PDF was recovered. Current 113 is catalogued as 180 pages / 5,750 lines and current 114 as 144 pages / 4,500 lines, so the accessible five-page PDFs cannot satisfy completeness. The newly tested volume-number, old-inventory, title-shortening, continuation-suffix, capitalization, and `.PDF` patterns all return the same 146-byte HTML 404 response. The full scans remain unavailable at plausible public `manuscript.bizdin.kg/static/media/pdf/` paths.
