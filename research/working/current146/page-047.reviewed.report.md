# Current 146, PDF page 47 / folio 430 — completion-first review

The source page was rendered directly from `sources/raw/manuscript-full-91-146/146.pdf` at 120 and 180 dpi (the latter 7,120 × 10,680 pixels) and inspected as a full-page color image plus three enlarged, overlapping contrast-enhanced grayscale crops. Independent visual counting confirms **32 visible verse baselines**. The handwritten folio number 430 and marginal pencil marks are page furniture and are not counted.

All 32 baselines are represented by sequential JSONL rows and have best-effort English translations. The pale cursive is difficult throughout, so every row is conservatively marked `uncertain`; no row is labeled unreadable and no baseline was invented. The passage concerns Kenen, Chyn Temir Khan, the forty khans, and a debate over whether Kenen could match them. Lines 1–4, 8, 11–12, 16, 18, 20, 23, and 29–31 especially need later comparison with adjacent leaves or a printed counterpart.

Validation was run with `scripts/validate-manuscript-transcription.py --require-english`.
