# Semetey book 1: translation entry and extraction audit

Date: 2026-09-14. This is a bounded preparation audit, not a translated batch or a certification of the volume's verse total.

## Source and reproducibility

- Source ID: `semetey-1-2013`.
- PDF: `sources/raw/semetey-1-2013.pdf`, 1,432 PDF pages.
- PDF SHA-256: `7884fe5c1ab6a6b472b8125212b5cfdc02021f73cd74e44a5cbe927b45141ddc` (recomputed).
- Preserved extraction: `sources/extracted/semetey-1-2013.lines.jsonl`.
- Extraction SHA-256: `07878f10290e57c7d34fc0fab6df78f2d0c24c7d6f192733182e6c0c103e2d16` (recomputed).
- Extraction contains 114,247 text records across 1,432 pages. These are not 114,247 certified verses.
- Bibliographic text at PDF 2, block 7 identifies *Semetey*, heroic epic, second part of *Manas*, book 1, Sayakbay Karalaev's variant; compiled by A. Zhaynakova, glossary by R. Sarypbekov, illustrations by T. Herzen, Bishkek: Turar, 2013, 1,432 pages. ISBN 978-9967-15-232-8.

Individually rendered and visually inspected PDF pages 22, 23, 24, 25, 26 and 27. Renderings are at `tmp/pdfs/semetey1-opening/page-0022.png` through `page-0027.png` (Poppler, scale 1800). Extraction and block boundaries were inspected for pages 24–43, plus page 44's opening. Later pages have not been visually certified by this audit.

## First narrative page

PDF 1 is the title page, PDF 2 bibliographic matter, PDF 3 starts `КИРИШ СӨЗ` (introduction). The introduction ends on PDF 22, visually confirmed by the prose conclusion and Aynek Zhaynakova's signature. PDF 23 is a full-page illustration of a mounted man, **not a blank page**: its mere three extracted decorative/header records do not describe its actual image content. Poetic quotations inside the introduction must not become duplicated narrative verses.

The continuous narrative begins on **PDF page 24**, also printed page 24. A three-line chapter heading precedes the poem:

> КАНЫКЕЙДИН СЕМЕТЕЙДИ БУКАРГА
> АЛЫП КАЧЫШЫ, ТАЙТОРУНУ ЧАПКАНЫ,
> СЕМЕТЕЙДИН ТАЛАСКА КАЙРА КАЙТКАНЫ

Heading IDs are `semetey-1-2013:p0024:b003:l001` through `l003`. Preserve them as heading evidence, outside the verse count.

The first verse is:

> Кан Манастын өлгөнү кырк күн боло элек,

It requires three ordered source records:

| ID suffix (all prefixed `semetey-1-2013:`) | Preserved raw glyphs | Deterministically normalized text |
| --- | --- | --- |
| `p0024:b004:l001` | `Ê` | `К` |
| `p0024:b005:l001` | `àí Ìàíàñòûí ºëãºí¿ êûðê ê¿í` | `ан Манастын өлгөнү кырк күн` |
| `p0024:b005:l002` | `áîëî ýëåê,` | `боло элек,` |

The first record is a large decorative drop cap forming **the same word** as the beginning of the next record. Join the first two with an empty separator and the third with one space. Do not count the drop cap as a separate verse, discard it as decoration, or produce `К ан` in readable Kyrgyz. Preserve all three original IDs, raw strings and bounding boxes in the resulting verse provenance. The canonical verse ID can be the first contributing ID, subject to the shared schema convention.

Subsequent first verses start at `p0024:b005:l003` (`Бадыша* өтүп кеткени –`) and `p0024:b005:l004` (`Кырк күнгө мезгил толо элек.`). Asterisks are glossary markers, not extra verses; retain their source evidence while translating the actual words.

## Columns, wraps and nonverse records

Read the **entire left column downward, then the entire right column downward**. Do not sort all lines by y-coordinate, which would alternate columns and corrupt the poem. Pages 24–27 were visually checked against their extraction order:

| PDF page | Left narrative block(s) | Right narrative block | Intervening nonverse record |
| --- | --- | --- | --- |
| 24 | 4 (drop cap), 5 | 6 | none |
| 25 | 3 | 5 | block 4: `4 – 1018`, printer's signature |
| 26 | 3 | 4 | none |
| 27 | 3 | 5 | block 4: `4*`, printer's signature |

On these pages the extraction already groups each column in the correct sequence; select the correct blocks rather than interleaving them. Page 24 left column starts x≈77.52, right x≈307.44. Odd pages 25/27 shift those margins slightly to x≈79 and x≈310. A global x threshold or fixed block number is not a complete classification policy.

The visual wrap convention places continuations toward the right edge of their own column. Examples on page 24 that should be reconstructed as single verses after review:

- `b005:l018` + `l019`: `Кыйының Манастан калган журт эле,`
- `b005:l028` + `l029`: `«Абыке балам, тоюң* менен топот түш,`
- `b006:l005` + `l006`: `Баякы, жылмайган Бакай экен – деп,–`
- `b006:l008` + `l009`: `Кечээ, менин жыргалым Манас кеп айткан:`

Each wrap still needs its own visual decision. Indentation alone must not automatically merge unrelated verses. Keep every contributing record in `source_line_ids`/segments; count the reconstructed verse once.

At the column transition, page 24 ends its left column `Тозооку Бакай дедиртип,` (`b005:l031`) and starts its right column `Оюнуңа кантип барамын?` (`b006:l001`). Page 25 ends its left column `Калмакча көөкөр* менен бир арак` (`b003:l039`) and continues right with `Камынтпай Жакып куйду эле,` (`b005:l001`). Page 24's last narrative record is `b006:l031`, `Бакай кан Абыке жолго салды эми.`; page 25 begins `b003:l001`, `Аргын кандын Ажыбай,`.

Exclude/classify watermark `www.bizdin.kg`, decorative `k семетей K`, decorative folios such as `v 24 V`, chapter headings, printer's signatures and later editorial apparatus separately. Decorative font letters `k`, `K`, `v`, `V` do not represent actual verse letters. The signature block interrupts extraction order on pages 25, 27, 33, 35, 41 and 43; it must not receive an English verse. Modern glosses remain source aids, outside the poem's verse count.

Pages 24–43 contain **1,615 raw extraction records**. The narrative-body block candidates total **1,546 physical text fragments**, including the drop cap and wrapped continuations. Neither figure is a certified verse count. The rest are heading/header/folio/signature records. This classification is based on block inspection across the range; individual visual classification remains required for pages 28–43.

## Legacy font normalization

The existing `scripts/extract.py` declares `legacy-font-v1` for this source. It converts characters U+00C0–U+00FF through CP1251, plus six explicit Kyrgyz glyph mappings:

| Raw glyph | Readable Kyrgyz |
| --- | --- |
| `¢` | `ң` |
| `ª` | `Ө` |
| `º` | `ө` |
| `¯` | `Ү` |
| `¿` | `ү` |
| `¡` | `Ң` |

Recomputing this exact function on **all 114,247 extracted records produced zero mismatches** with saved `text`. This verifies reproducibility, not that every PDF glyph is semantically correct. The visual opening confirms ordinary Cyrillic and Kyrgyz letters in the samples above, and `ªçºí` → `Өзөн`, `¯ç¿ð` → `Үзүр`, `Êûéûíû¢` → `Кыйының`. No fresh OCR or external translation service was used.

Each final segment must declare `normalization: legacy-font-v1` and retain exact extracted `raw`, `bbox`, source ID, page and PDF SHA. Readable Kyrgyz derives from that mapping, not by overwriting raw evidence. The source verifier's ordinary space join requires a narrow explicit exception for the drop cap: a declared per-boundary join list such as `["", " "]`, checked against the segment count and a material note. Do not relax arbitrary raw or normalized-text equality to accommodate it. Root has been notified and owns schema changes; this report does not alter shared validation code.

## Recommended first translation assignments

Use disjoint source-specific files to avoid collisions with existing Manas batches:

1. PDF **24–43** → `corpus/batches/pages-semetey1-0024-0043.{json,en.txt}`.
2. PDF **44–63** → `corpus/batches/pages-semetey1-0044-0063.{json,en.txt}`.
3. PDF **64–83** → `corpus/batches/pages-semetey1-0064-0083.{json,en.txt}`.

The first boundary remains mid-speech: page 43's last body record is `p0043:b005:l039`, `Жесир менен жетимди`; page 44 begins `p0044:b003:l001`, `Желкелеп кантип чабабыз?`. Workers should read neighboring context without duplicating ownership. Ranges 44–83 are proposed work allocations, not visually certified page layouts.

A twenty-page Semetey assignment has roughly twice as many physical body rows as a twenty-page single-column Manas assignment. Keep the same individual-image review, exact provenance and final Kyrgyz–English pair review; reduce the internal drafting group size if needed. Report translated verses **and English words**, with separately enumerated unresolved source verses. Nothing in this opening audit establishes the complete trilogy's 500,553-line total or closes an existing source gap.
