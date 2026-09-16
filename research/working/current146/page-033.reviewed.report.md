# Current 146, PDF page 33 (folio 416)

- Counted **35 visible verse baselines** independently from the manuscript image.
- Accounted for all 35 as narrative rows; no heading or folio mark was counted as verse.
- Produced **204 English words**.
- Status: **10 visually transcribed**, **25 uncertain**, **0 unreadable**.
- PDF SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`.

The handwriting is legible enough to retain a best-effort reading for every baseline, but several proper names and compressed phrases remain provisional. Lines 15–17 have a clear near-verbatim printed counterpart at continuation extraction positions 2892–2894 (`Маңдайлашып турушуп / Мылтык атып, жаа тартып / Былчылдашып урушуп`); the manuscript spelling and lineation are preserved here. Nearby printed text was used only as a reading aid.

Validation passed with:

```text
python3 scripts/validate-manuscript-transcription.py research/working/current146/page-033.reviewed.jsonl --pages 33 --source-id sayakbay-ms-current146 --pdf sources/raw/manuscript-full-91-146/146.pdf --require-english
```
