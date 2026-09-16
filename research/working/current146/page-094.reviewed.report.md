# Current 146 manuscript page 94 / folio 477 review

- Source: `sources/raw/manuscript-full-91-146/146.pdf`
- PDF SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`
- Independent visual count: **36 verse baselines**.
- Method: rendered at 400 dpi and read directly from the manuscript image. One JSONL row was made for every visible baseline; no reconstructed or invisible lines were added.
- Status: 18 visually transcribed rows and 18 explicitly provisional rows. The opening elaboration and several compressed idioms have difficult cursive or archaic wording, so their readings and translations remain marked uncertain rather than silently normalized.

## Cross-witness check

The closing ordered run has secure counterparts in `seytek-1991-continuation` page 332: manuscript rows 30–32 correspond to `p0332:b001:l047`–`l049`; rows 33–35 correspond to `p0332:b003:l001`–`l003`. The manuscript preserves lexical variants (`Ал бадырак`, `Кыргыздан доочу`) and compresses the following deadline wording into row 36, so those forms were retained. The earlier page material is a substantial manuscript-specific expansion around the printed command to submit and pay tribute (`p0332:b001:l045`–`l046`); it was not forced into one-to-one alignment. Seytek 2012 was searched broadly, but no more secure ordered counterpart was used.

## Validation

Validated with `scripts/validate-manuscript-transcription.py --require-english` for page 94.
