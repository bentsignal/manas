# Current 146 manuscript page 111 / folio 494 review

- Source: `sources/raw/manuscript-full-91-146/146.pdf`
- PDF SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`
- Independent visual count: **37 verse baselines**.
- Method: rendered at 400 dpi and inspected in three overlapping high-resolution crops. Every visible verse baseline has one JSONL row; folio 494 is excluded as furniture.
- Status: 16 visually transcribed rows and 21 explicitly uncertain rows. All rows have completion-first English, with difficult cursive and manuscript-specific epithets explicitly marked.

## Printed-witness verification

Rows 1–4 securely correspond in order to `seytek-1991-continuation:p0334:b004:l005`–`l008`. Rows 26–29 resume the printed passage at `p0334:b004:l009`–`l012`, and rows 36–37 correspond to `p0334:b004:l013`–`l014`. The manuscript inserts substantial praise and warrior epithets between those runs; they are preserved as independent lines rather than forced into the print sequence.

## Validation

Validated with `scripts/validate-manuscript-transcription.py --require-english` for page 111.
