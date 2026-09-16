# Current 146 manuscript page 136 / folio 519 review

- Source: `sources/raw/manuscript-full-91-146/146.pdf`
- Source SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`
- Independent visual count: **33 verse baselines**
- Output: **33 JSONL rows**, one per visible baseline
- Method: rendered at 300 dpi and inspected in three overlapping high-resolution crops. Every baseline was directly transcribed and translated.
- Status: **23 visually transcribed**, **10 uncertain**.

## Printed-witness check

A secure sustained counterpart appears in `sources/extracted/seytek-1991-continuation/page-337.txt`, especially printed lines 30–48 and 53–55. It confirms manuscript rows 1, 6–8, 14–19, and 21–33. The manuscript adds or varies rows 2–5, 9–13, and 20; these remain distinct and are not replaced by printed text. Orthographic variants such as manuscript `Калдайга` and the manuscript’s retained lineation are preserved.

## Content and limitations

Kenen declares that he would rather die as a sacrifice than yield his people to the enemy. The expanded manuscript-only passage near the opening contains the main cursive uncertainties, explicitly marked on the affected rows.

## Validation

Validated with `scripts/validate-manuscript-transcription.py --pages 136 --source-id sayakbay-ms-current146 --pdf sources/raw/manuscript-full-91-146/146.pdf --require-english`.
