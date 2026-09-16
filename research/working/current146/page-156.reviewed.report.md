# Current 146 manuscript page 156 / folio 539 review

- Source: `sources/raw/manuscript-full-91-146/146.pdf`
- Source SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`
- Independent visual count: **35 verse baselines**
- Output: **35 JSONL rows**, one per visible baseline
- Method: rendered at 300 dpi and inspected in overlapping high-resolution crops. Every visible baseline was directly transcribed and translated.
- Status: **18 visually transcribed**, **17 uncertain**.

## Printed-witness check

Secure ordered counterparts occur in `seytek-1991-continuation` printed page 339: manuscript rows 1–5 match printed lines 81–85; rows 10–11 match 86–87; rows 23–31 match 88–96; and rows 34–35 match 97–98. The substantial prayer expansion at rows 6–9 and 12–22, plus rows 32–33, remains distinct and provisional.

## Content and limitations

Odukan charges Kögöy while the Kyrgyz pray for their champion; the two then clash with spears and iron-headed maces. The printed text securely verifies the battle framework, while the manuscript’s expanded communal prayer contains most uncertain readings.

## Validation

Validated with `scripts/validate-manuscript-transcription.py --pages 156 --source-id sayakbay-ms-current146 --pdf sources/raw/manuscript-full-91-146/146.pdf --require-english`.
