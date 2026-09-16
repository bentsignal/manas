# Current 146, PDF page 50 / folio 433 — completion-first review

The source page was rendered directly from `sources/raw/manuscript-full-91-146/146.pdf` at 180 dpi (7,120 × 10,680 pixels) and inspected as a full-page color image plus enlarged, contrast-enhanced grayscale crops. Independent visual counting confirms **32 visible verse baselines**. The handwritten folio number 433 and marginal marks are page furniture and are not counted.

All 32 baselines are represented by sequential JSONL rows with best-effort English translations. The pale cursive makes several readings provisional, so every row is conservatively marked `uncertain`; no baseline is labeled unreadable and none was invented. The passage sends Kenen to scout an opponent, instructing him to determine the enemy’s strength and return safely, then describes an exceptional warrior. A nearby printed continuation counterpart supports the closing sequence beginning with “Бирөө миңге …,” but the manuscript’s wording and variants are preserved rather than silently replaced. Lines 1–6, 9–10, 12, 16–20, 22–23, 25, and 28–32 especially need later expert or adjacent-leaf review.

Validation was run with `scripts/validate-manuscript-transcription.py --require-english`.
