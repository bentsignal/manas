# Current 146 manuscript page 130 / folio 513 review

- Source: `sources/raw/manuscript-full-91-146/146.pdf`
- Source SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`
- Independent visual count: **35 verse baselines**
- Output: **35 JSONL rows**, one row for each visible baseline
- Method: rendered at 300 dpi and inspected in overlapping top, middle, and bottom crops. Each manuscript baseline was transcribed directly and translated into English.
- Status: **20 visually transcribed**, **15 uncertain**. Uncertain rows retain a best-effort reading and translation rather than silently omitting text.

## Printed-witness check

Repository searches of the indexed continuation witness did not reveal a secure ordered counterpart for this page. No printed reading was substituted for the manuscript; all rows preserve the visible manuscript witness.

## Notes

The page continues a praise passage describing a heroic warrior and battle. Several cursive lexical forms, especially rows 2, 4, 6, 9, 12, 16, 19–22, 25–27, 29–30, remain provisional and are explicitly marked uncertain.

## Validation

Run with `scripts/validate-manuscript-transcription.py --pages 130 --source-id sayakbay-ms-current146 --pdf sources/raw/manuscript-full-91-146/146.pdf --require-english`.
