# Current 146 manuscript page 160 / folio 543 review

- Source: `sources/raw/manuscript-full-91-146/146.pdf`
- Source SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`
- Independent visual count: **36 verse baselines**
- Output: **36 JSONL rows**, one per visible baseline
- Method: rendered at 300 dpi and inspected in overlapping high-resolution crops. Every baseline was transcribed directly and translated into English.
- Status: **26 visually transcribed**, **10 uncertain**.

## Printed-witness check

A sustained counterpart spans `seytek-1991-continuation` printed page 340 lines 95–109 and page 341 lines 1–12. It confirms most of the battle sequence while the manuscript adds rows 1, 5, 8–9, 11, 20–22, 33, and 35. Those additions remain distinct and explicitly provisional.

## Content and limitations

Choyun Alp attacks Ebegey; Zhelzhetpes and Kenen charge to support their comrades. The closing speech argues that they must show loyalty rather than stand aside. Ambiguity is concentrated in manuscript-only expansions.

## Validation

Validated with `scripts/validate-manuscript-transcription.py --pages 160 --source-id sayakbay-ms-current146 --pdf sources/raw/manuscript-full-91-146/146.pdf --require-english`.
