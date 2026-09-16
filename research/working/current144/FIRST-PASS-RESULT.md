# Current inventory 144: completed first pass

Completed 2026-09-16 from `sources/raw/manuscript-full-91-146/144.pdf`
(SHA-256 `d8791a47f71591706ce85ccf7c0e6f9d67e1f8b7543ee0ee3aa78dc153881da8`).

- PDF pages 3–193: 191 verse-bearing images, all individually represented.
- Physical narrative baselines: **5,828**.
- First-pass English words: **32,405**.
- Secure counterparts in the released 2012 Seytek witness: **2,105**.
- Manuscript rows released after overlap exclusion: **3,723 lines / 21,407 English words**.
- PDF pages 1–2 and 194–195: cover, title, archive-note, or binding images; excluded as nonverse furniture.

Every accepted page passes `scripts/validate-manuscript-transcription.py
--require-english`, including the English-collapse guard. A failed Sol-low draft
for pages 46–55 and 76–80 is retained under `rejected-sol-low/`; its English
cycled generic sentences and is not counted. Those pages were re-read from the
images, four omitted baselines were restored, and all fifteen accepted files
were replaced.

The archive catalogue reports 6,092 lines. Direct inspection found 5,828
visible narrative baselines, a difference of 264. The release preserves the
observed physical positions and does not invent rows to force the catalogue
tally. Possible causes include archival counting conventions, different
lineation, and the unresolved extra/repeated-image or foliation anomaly.

The conservative overlap map uses three evidence classes: the prior manual
visual crosswalk, exact counterparts recorded during page transcription, and
normalized lines that occur exactly once in each witness. Repeated formulas are
not excluded without a position anchor. All handwriting and English remain a
draft without independent specialist review; bracketed readings are the first
accuracy-review queue.
