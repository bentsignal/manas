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

## Independent index and server checks (2026-09-16, second pass)

This pass avoided re-requesting the URL candidates listed above and in the main URL-audit JSON.

| Mechanism | Query/result | Interpretation |
|---|---|---|
| Live catalogue HTML | Re-fetched both catalogue records; each still embeds only its `Obrazets-` URL. No API, alternate download, or hidden full-scan link appears in the rendered HTML. | No new origin-side locator. |
| Django/API probes | `/api/`, `/api/materials/113/`, and `/api/manuscripts/113/` each return the site's ordinary HTTP 404 page (13,390 bytes). `/static/media/pdf/` and `/media/` return HTTP 403 directory responses (146 bytes). | There is no exposed catalogue API or directory index from which to enumerate the missing names. |
| Legacy sitemap hostname | The live sitemap names `lib.bizdin.kg`, but DNS resolution for that hostname now fails. | The legacy hostname cannot currently serve or enumerate scans. |
| Internet Archive item search | Advanced Search for `113-Semetei-Saiakba-Karalaev` or `114-Semetei-Kanykeidin-sozu` returns `numFound: 0`. | No separately deposited Archive.org item was indexed under either filename stem. |
| Wayback CDX | The CDX endpoint returned Internet Archive's `Temporarily Offline` page during this pass. | Historical URL enumeration remains inconclusive and should be retried when CDX is healthy. |
| Arquivo.pt | Exact version-history lookup for the current-113 sample URL returns `estimated_nr_results: 0`; filename searches yielded no scan locator. | No independent Portuguese Web Archive capture was found. |
| Common Crawl indexes | Wildcard lookups for the two numeric filename stems across representative 2020–2026 indexes produced no capture record when the index responded; several older index calls returned transient 503/connectivity errors. | No recoverable Common Crawl capture was found; partial index outages make this negative result non-exhaustive. |
| GitHub public code search | Exact searches for the current-113 sample filename and `web-113-Semetei` return only this repository's audit/research files. | No public repository contains a second locator found by exact filename search. |

The two sample PDFs were also inspected for embedded provenance. Both have exactly five pages, no title/author/custom metadata or metadata stream, and identify only `ABBYY FineReader 12` as producer. Their creation timestamps are 2016-10-17 07:28:50 EDT (current 113) and 07:29:46 EDT (current 114), consistent with adjacent batch processing but revealing no original or full-scan filename.

No full scan was recovered in this second pass. The strongest remaining public-web avenue is a later retry of Wayback CDX after its service outage; otherwise recovery requires the archive operator or another holding institution rather than additional blind filename expansion.
