# Current 145 folio 231/367 audit

## Finding

PDF page 43 is the physical leaf in the folio-231 position, but the photographed numeral at its upper right reads **367**. The numeral is not plausibly a visual reading of 231: at full-resolution review it has the same three digit forms as a written 367, and there is no clear underlying or overwritten 231. This is best treated as a scribal/archival foliation error on an otherwise normally sequenced leaf.

PDF page 179 is the genuine folio 367 in the later sequence. Pages 43 and 179 are different photographs with different verse text, so page 43 is neither a duplicate image nor an alternate copy of page 179.

## Evidence

The immediate scan sequence is conclusive for physical placement:

| PDF page | photographed numeral | expected sequential folio | reviewed text boundary |
|---:|---:|---:|---|
| 42 | 230 | 230 | begins `Секирдүү тоонун боорундай,`; ends `Баатырдын уулу шер келип,` |
| 43 | **367** | **231** | begins `Кулансур менен Кулукер`; ends `Түпкү журтка билинип` |
| 44 | 232 | 232 | begins `Бетин адам барабы`; ends `Ордосу бүлүнүп айланды` |
| 178 | 366 | 366 | begins `Букасын огуз үй кылып,`; ends `Ар кылса менин шамалдан,` |
| 179 | 367 | 367 | begins `Барган оюмду Кудайым`; ends `Күн чагы келген бекен` |
| 180 | 368 | 368 | begins `Ак кайың журт берүүдө`; ends `Журтка кызмат кылды` |

Across the scan, the ordinary relation is `folio = PDF page + 188`: page 42 gives 230, page 44 gives 232, page 178 gives 366, page 179 gives 367, and page 180 gives 368. Page 43 is the sole break at the disputed location. No other reviewed page carries photographed folio 231; two reviewed pages currently carry 367 only because page 43 records the erroneous visible numeral.

Direct image comparison also rules out duplication. Page 43 and page 179 have different handwriting layouts, different opening and closing text, and different neighboring leaves. Page 43 sits physically between the photographed 230 and 232 leaves; page 179 sits between 366 and 368. The p43 numeral appears as an uncorrected 367 rather than an overwritten 231.

## Recommended accounting

Keep `page-043.reviewed.jsonl` diplomatically faithful with `folio: 367`, because that field currently records what is visibly written. Do not merge, deduplicate, or discard either page 43 or page 179.

For canonical physical ordering, assign page 43 the **logical folio 231** (or an explicit foliation-correction override) while retaining the photographed value as evidence. Order this run as PDF42/logical230, PDF43/logical231, PDF44/logical232. Keep PDF179 as the sole canonical folio367 leaf in the later run between 366 and 368.

The manifest/integration layer should therefore distinguish `photographed_folio: 367` from `logical_folio: 231` for PDF43. If the current schema cannot preserve both, use PDF page order as canonical and document the p43 scribal foliation error rather than silently changing the photographed numeral.
