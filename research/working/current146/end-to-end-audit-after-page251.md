# Inventory 146 end-to-end audit after page 251 integration

Audit date: 2026-09-16. This was a read-only audit of the working transcriptions, canonical physical extraction, batch metadata, release chunks, inventory README, root README, and target metadata.

## Result

Inventory 146 is internally complete at the physical, batch, and release layers.

- Source PDF SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`.
- Canonical physical extraction: **8,734 rows**, consisting of **8,733 narrative baselines** and **1 heading**.
- Physical page range: PDF pages **5–251**, with every page present. IDs are unique and every page has contiguous `l001...lNNN` numbering.
- PDF page **252** is documented as the blank outside back cover. Its reviewed JSONL is intentionally empty and its report records zero visible text/verse baselines.
- The only heading is `sayakbay-ms-current146:pdf251:l013`, text `Бүттү`. It is preserved in the physical extraction and excluded exactly once from verse/release counting as `kind: heading`.
- Batch layer: **7,838 included IDs** plus **896 excluded physical IDs** equals all **8,734 physical rows** exactly. The exclusions are **895 secure printed-witness overlaps** and the single closing heading. Included and excluded sets are disjoint and individually duplicate-free.
- Release layer: **7,838 unique inventory-146 rows**, exactly equal to the batch included-ID set. No release duplicate was found.
- Batch ordering is strictly increasing in physical order. Every batch `after_id` correctly links to the preceding *included release row*; this intentionally skips physical rows excluded as printed-witness overlaps.
- Inventory README: all 248 page-table entries (pages 5–252) exactly match canonical narrative counts, including page 251 = 12 and page 252 = 0. Its total of **8,733** narrative baselines is correct.

## Working JSONL comparison and cleanup

The canonical physical extraction is fully supported by the working files: every one of the **8,734 canonical rows** has at least one working JSONL row with exactly matching `raw`, `text`, `en`, and `classification` values.

The initial audit found **67 stale historical IDs** outside the canonical physical set:

- `page-005.reviewed.jsonl` retains stale `pdf005:l037`; canonical page 5 ends at l036.
- The obsolete aggregate `pages-241-250.jsonl` retains **66 superseded high-numbered IDs** on pages 241–250 after the later per-page recounts. The excess by page is: p241 6, p242 5, p243 6, p244 7, p245 6, p246 7, p247 5, p248 8, p249 7, p250 9.

The scan disproves `pdf005:l037`: the page ends with l036, while the alleged extra baseline is marginal notation. That row was removed. The superseded aggregate file was also removed because its pages now have reviewed per-page files. After cleanup, the preferred page files contain exactly **8,734 unique rows**, and their ID set exactly equals the canonical physical extraction.

## Target and status metadata

The root README states the project target as **500,553 lines**, matching `corpus/target.json` (`target_lines: 500553`). Inventory 146 does not by itself certify or reconcile that archival aggregate.

The root README and `corpus/progress.json` both report **396,270 translated rows and 2,093,429 English words** after final integration.

Direct image review also corrected PDF pages 249–251 from provisional folios 632–634 to photographed folios **630–632**. This metadata correction does not alter source IDs, English text, line counts, or word counts.
