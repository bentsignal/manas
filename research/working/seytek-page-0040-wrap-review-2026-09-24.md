# Seytek 2012 page 40: wrapped final left-column verse

Focused read-only review on 2026-09-24. I rendered `sources/raw/seytek-2012.pdf` PDF/printed page 40 at 300 dpi, inspected the bottom of the left column at full resolution, and compared the extraction records, existing batch, and two English rows. PDF digest in the extraction: `786eb36c1863f3e6c5330bb98d5d1656ab2e566bc53e16128a4f982928ebee2f`.

## Finding

At the foot of the left column the source visibly prints:

> Арамдардан алалбай келдим<br>　　　　　　　　дартымды.

The first fragment is `seytek-2012:p0040:b003:l040` (`bbox.xMin=76.4`, `yMin=666.1`); the second is `p0040:b003:l041` (`xMin=189.8`, `yMin=679.7`). The second baseline is substantially **indented right**, contains only the final word and punctuation, and completes the preceding clause. It is a typographic wrap caused by the long line, not a new independent verse. The exact joined reading is **`Арамдардан алалбай келдим дартымды.`** with one ordinary space between the two fragments. The next verse in physical reading order is at the top of the right column, `p0040:b002:l001` `Тилейин жакшы угумду,`.

Page 40 thus has **81 extracted text baselines/fragments** but **80 verse units**: 40 in the left column (the final one consumes two fragments), followed by 40 in the right. The present batch has 81 `source_ids` and two English rows for this one verse. All words are represented, so this is a lineation/counting defect, not an omitted-text gap.

## Recommended source and English pairing

Use the existing `source_groups` convention, with `p0040:b003:l040` as the single canonical/display row and `p0040:b003:l041` as its second evidence segment:

```json
"source_groups": {
  "seytek-2012:p0040:b003:l040": [
    "seytek-2012:p0040:b003:l040",
    "seytek-2012:p0040:b003:l041"
  ]
}
```

Keep `l040` in `source_ids` in its reviewed left-column position and remove only the separate `l041` **display-row** entry. Do not exclude or discard `l041`: it remains fully represented in the grouped `source_line_ids` and PDF evidence segments. The default `source_joiners` value of a single space produces the source reading above; no special empty join is needed. Add a per-ID note explaining the physical wrap. This is analogous to grouped wrapped verse lines already used elsewhere in the corpus.

The current paired English rows are `From the villains I could not redress` (`l040`) and `My grief.` (`l041`). Replace them with **one complete English line** on representative ID `l040`, such as `I could not redress my grief against those villains.` The English wording should be reviewed in its surrounding lament, but the grouping decision does not depend on this exact phrasing. Remove the standalone `l041` English display row. Preserve the original two source segments under the one row, including their IDs, raw glyphs, and bounding boxes.

After the reviewed column order is applied (`b003` left before `b002` right), page 40's last narrative ID is `p0040:b002:l040`, so page 41's `after_id` should point there. Grouping `b003:l040+l041` does not change that boundary. The local release should lose **one row** when this lineation correction is applied; word count may change if the English is revised. Check page-40 ID coverage by expanding `source_groups`, not merely by counting display rows, then rerun alignment, draft audit, release compilation, and reader checks.

No canonical corpus or release file was edited in this review.
