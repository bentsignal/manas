# Current 146 manuscript page 140 / folio 523 review

- Source: `sources/raw/manuscript-full-91-146/146.pdf`
- Source SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`
- Independent visual count: **34 verse baselines**
- Output: **34 JSONL rows**, one per visible baseline
- Method: rendered at 300 dpi and inspected through overlapping high-resolution crops. Every manuscript baseline was transcribed and translated.
- Status: **28 visually transcribed**, **6 uncertain**.

## Printed-witness check

The complete page has a sustained ordered counterpart spanning `seytek-1991-continuation` printed page 337 lines 100–101 and page 338 lines 1–32. This witness securely confirms the sequence and most readings. Manuscript lexical variants and its final compressed line remain preserved rather than normalized to the print. Rows 1, 4–5, 10, 28, and 34 retain explicit uncertainty where the cursive or wording differs.

## Content note

This is an enemy commander’s violent order to exterminate and enslave the Kyrgyz. The English translates every visible baseline directly; no violent line is omitted or softened into a placeholder.

## Validation

Validated with `scripts/validate-manuscript-transcription.py --pages 140 --source-id sayakbay-ms-current146 --pdf sources/raw/manuscript-full-91-146/146.pdf --require-english`.
