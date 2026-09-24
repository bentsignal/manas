# Seytek 2012, printed page 25: section opening and column order

Read-only source review on 2026-09-24. I rendered `sources/raw/seytek-2012.pdf` page 25 at 2200-pixel scale and compared the image with every page-25 record in `sources/extracted/seytek-2012.lines.jsonl`, `corpus/batches/pages-seytek-0025.json`, and the local release. The PDF SHA-256 recorded with the extraction is `786eb36c1863f3e6c5330bb98d5d1656ab2e566bc53e16128a4f982928ebee2f`. This note establishes reading order and row accounting; it does not retranslate the verse.

## Printed layout and exact IDs

The centered section heading, `СЕЙТЕКТИН ТӨРӨЛҮШҮ` (“Seytek's Birth”), is `seytek-2012:p0025:b002:l001`. It precedes the verse but is not a verse line. The ornate drop cap `А` is `p0025:b003:l001`; the remainder `ны мындай таштайлы,` is `p0025:b005:l001`. These two extraction segments occupy one printed verse line, **`Аны мындай таштайлы,`**. The current batch already groups them under the stable representative ID `p0025:b003:l001`, with `source_groups[p0025:b003:l001] = [p0025:b003:l001, p0025:b005:l001]`. Keep that grouping; do not create a 63rd verse row or drop the `b005:l001` source segment. The current release renders its joined Kyrgyz as `А ны мындай таштайлы,` with a spurious space, a separate normalization/display defect to correct when handling the page.

The rest of the left column consists of `p0025:b005:l002` through `p0025:b005:l031` (30 lines, xMin approximately 79). The right column consists of `p0025:b004:l001` through `p0025:b004:l031` (31 lines, xMin approximately 310). The exact physical narrative sequence is therefore:

1. Grouped drop-cap row represented by `seytek-2012:p0025:b003:l001`, consuming both `b003:l001` and `b005:l001`.
2. `seytek-2012:p0025:b005:l002` through `p0025:b005:l031`.
3. `seytek-2012:p0025:b004:l001` through `p0025:b004:l031`.

This yields the existing **62 verse rows** from 63 source text segments. The current batch and release instead put `b004:l001`–`l031` immediately after the grouped drop cap, then `b005:l002`–`l031`: 31 right-column rows interrupt the first left-column line from its continuation. Current local release ordinals for page 25 are 297120–297181; reorder those same 62 whole records and retain each English line with its source ID.

Two joins independently confirm the printed order. The first line `Аны мындай таштайлы,` (“Let us leave that matter”) is followed on the left by `Быягынан баштайлы:` (“Let us begin from here”); the current order inserts the opposite column between them. The left footer `«Канкор төрөм өлдү» – деп,` (`p0025:b005:l031`) leads to the right top `Кайра тартпас чын жайды` (`p0025:b004:l001`) as Ayçürök's lament continues. The right footer `Эр Кыяздын койнуна` (`p0025:b004:l031`) leads into printed page 26's **left** top `Ал жанында жөкөрү*` (`p0026:b003:l001`), followed by attendants who send women into Kiyaz's embrace.

## Furniture and section metadata

The batch's four excluded IDs correspond to nonverse matter: `p0025:b001:l001` is the website watermark; `p0025:b002:l001` is the section heading; `p0025:b006:l001` is `4 – 911`, a **printer's signature**, not a footnote or cross-reference marker; and `p0025:b007:l001` is folio `25`. The batch labels all four as `kind: heading`; that is a broad exclusion category, but its explanatory reason for `b006` should be corrected. The actual heading may be retained as section metadata/UI text without counting it as a verse row; its exclusion from verse count does not mean its words are absent from the printed source.

## Safe correction plan

1. Add the reviewed page-25 narrative-order override as the grouped representative ID, then left `b005:l002`–`l031`, then right `b004:l001`–`l031`. Keep the raw extraction and segment IDs unchanged; its PDF extraction order is evidence, not reading order.
2. Permute `pages-seytek-0025.json` `source_ids` and `pages-seytek-0025.en.txt` as ID–English pairs; preserve `source_groups`, per-ID notes, and the existing `after_id` connecting the previous Semetey portion. Update the furniture note for `b006` and the grouped Kyrgyz display text through the source grouping/normalization path, without altering the raw segments.
3. In `pages-seytek-0026.json`, change `after_id` from `p0025:b005:l031` to **`seytek-2012:p0025:b004:l031`**. After page 26 is itself reordered left then right, page 27's anchor should change to `p0026:b002:l040` as documented in the companion pages-26–35 audit.
4. Permute the 62 page-25 release row objects as a whole within ordinal range 297120–297181, preserving each `id`, `source_line_ids`, `source`, `en`, and metadata. Reassign the same contiguous ordinals. Verify the new first/left/right and page 25→26 joins in batch, release, and compiled reader, along with unchanged row and English-word counts. Run the alignment, draft, build, and reader checks after updating the reviewed order input that those validators consume.

No canonical file was changed in this review.
