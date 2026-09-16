# Current inventory 141 completion-first coverage audit

Source: `sources/raw/manuscript-full-91-146/141.pdf`
SHA-256: `15c45ada8a04ab9c5300823d451f8954ca69d6cbadbe051f838cf51348aadfaf`

## Physical and catalogue extent

The scan has 123 PDF pages. PDF page 1 is the outside front cover, page 2 is the title/catalogue leaf, pages 3–122 are manuscript folios 2201–2320, and page 123 is the outside back cover. Thus the scan contains 120 consecutive narrative leaves. The title leaf records **6,079 lines** (`6079 строк`) and 119 pages. The foliation and scan physically contain 120 narrative leaves, so the title's page count is one lower than the direct inclusive folio count; its 6,079-line figure is retained as the catalogue/copyist narrative count.

## Exact episode boundaries and release span

The manuscript episode maps continuously to the released `seytek-2012` witness:

- opening: `Кабарга келген ат турат,` = `seytek-2012:p0910:b002:l026`, ordinal **365,365**;
- closing: `Теги жанын аябай,` = `seytek-2012:p0986:b002:l029`, ordinal **371,444**.

The inclusive released span contains **6,080 lines** and **32,177 whitespace-delimited English words** (32,158 regex word tokens). The opening 50-line manuscript leaf maps sequentially to ordinals 365,365–365,414. The closing 46-line leaf maps sequentially to ordinals 371,399–371,444. These sequence checks establish the outer monotonic crosswalk rather than relying on isolated repeated formulas.

## Completion result

| evidence class | lines | disposition |
|---|---:|---|
| secure continuous released span | 6,080 | already translated |
| catalogue minus release discrepancy | -1 | released lineation has one additional line |
| secure unique untranslated lines | 0 | none demonstrated |

The single-line difference runs in the direction of greater released coverage. With exact sequential boundary leaves and an uninterrupted printed episode, it is a count/lineation discrepancy, not evidence that the release lacks a manuscript line. Current inventory 141 is therefore completion-covered by the existing release. The compact machine-readable evidence is in `monotonic-crosswalk.json`.
