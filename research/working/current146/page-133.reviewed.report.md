# Current 146 manuscript page 133 / folio 516 review

- Source: `sources/raw/manuscript-full-91-146/146.pdf`
- Source SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`
- Independent visual count: **35 verse baselines**
- Output: **35 JSONL rows**, one for every visible baseline
- Method: rendered at 300 dpi and inspected through overlapping high-resolution top, middle, and bottom crops. Every baseline was directly transcribed and translated.
- Status: **17 visually transcribed**, **18 uncertain**. Each uncertain row contains a best-effort reading and English translation with an explicit uncertainty note.

## Printed-witness check

Searches of the local indexed printed continuation did not yield a secure sustained ordered counterpart for this folio. The reviewed rows therefore preserve the manuscript witness and do not silently import printed wording.

## Content and limitations

The passage laments the worsening political condition of the Kyrgyz, foreign domination, and threatened loss of Ala-Too. Dense cursive and several names or archaic expressions make rows 1, 3, 5–6, 8–9, 12, 16, 18–19, 22, 25–26, and 30–34 provisional.

## Validation

Validated with `scripts/validate-manuscript-transcription.py --pages 133 --source-id sayakbay-ms-current146 --pdf sources/raw/manuscript-full-91-146/146.pdf --require-english`.
