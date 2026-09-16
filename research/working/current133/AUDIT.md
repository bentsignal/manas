# Current inventory 133 completion-first coverage audit

Source: `sources/raw/manuscript-full-91-146/133.pdf`
SHA-256: `c276b5bb9f9e4a45ceaf79726e4eee0b0cf062b1c30407cda33740dce1840b4d`

## Physical and catalogue extent

The scan has 103 PDF pages. The title records **101 pages** and **3,500 lines**. Covers/title material account for the basic scan excess, and the scan also contains a known duplicate photograph of the same opening leaf in different crops. The 3,500-line title figure is retained as the catalogue narrative count; duplicated scan images must not be counted twice.

## Released boundary and coverage anomaly

The decisive boundary is manuscript folio **35**. Its ordered text begins `А ны мындай таштайлы,`, exactly `seytek-2012:p0025:b003:l001`, ordinal **295,924**. This is also the first `seytek-2012` row present anywhere in the compiled release.

Therefore manuscript folios **1–34 precede the first released printed-witness line**. Direct page review recovered **1,196 translated narrative baselines / 6,643 English words** from PDF pages 6–37. PDF page 4 contributes 36 visible positions that remain explicitly unresolved after Sol-low, Astra-low, and a bounded Astra-medium attempt; page 5 is an exact duplicate of page 4. The next distinct image is marked folio 3, so folio 2 is absent from the recovered scan and its line extent remains unknown.

The next secure inventory boundary is current 135 at ordinal 306,259. The released envelope from current 133's folio-35 anchor through the row immediately before that boundary contains **10,335 lines** and **54,873 whitespace-delimited English words** (54,773 regex word tokens). This envelope combines the released remainder of current 133 with current 134 because no defensible internal 133/134 division has yet been established. It must not be reported as current 133's standalone released line count.

## Completion result

| evidence class | count | disposition |
|---|---:|---|
| whole-inventory catalogue count | 3,500 lines | physical extent |
| secure missing printed-witness segment | folios 1–34 | precedes the first released `seytek-2012` row |
| newly translated manuscript rows | 1,196 lines / 6,643 English words | PDF pages 6–37; first-pass uncertain readings |
| unresolved visible positions | 36 | PDF page 4 / folio 1; zero translation credit |
| missing scan extent | folio 2, line count unknown | page 5 duplicates folio 1; completeness remains blocked |
| combined released 133–134 envelope | 10,335 lines / 54,873 English words | already translated; cannot be divided securely between inventories |
| standalone current-133 discrepancy | unresolved | no exact 133/134 printed boundary |

This inventory is **not completion-covered** because the 36 folio-1 positions and absent folio 2 remain unresolved. The 1,196 translated rows are now inserted immediately before the first printed `seytek-2012` row. The compact boundary evidence is in `monotonic-crosswalk.json`; exact page accounting is under `transcription/`.
