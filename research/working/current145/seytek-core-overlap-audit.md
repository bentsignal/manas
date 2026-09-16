# Current 145 / *Seytek* 2012 core-overlap audit

## Result

The secure map contains **990 one-to-one manuscript/edition pairs**. Every pair is globally ordered, and neither witness ID occurs more than once. The overlap begins at `sayakbay-ms-current145:pdf003:l001` = `seytek-2012:p1148:b002:l017` (`Айза сынып жоголсо`) and ends at `sayakbay-ms-current145:pdf088:l019` = `seytek-2012:p1165:b003:l034` (`Сан кара күткөн бай болду` / printed `Сан кара күткөн бай болуп`).

The exact ending matters: the printed epic text stops there. Printed page 1166 begins the glossary. Manuscript row `sayakbay-ms-current145:pdf088:l020` starts further narrative about Perizada Beibak; it and all **3,631 later manuscript rows** are outside this printed core overlap.

## Counts

- Manuscript segment tested: **2,664 physical verse rows**, PDF 3 line 1 through PDF 88 line 19.
- Edition segment tested: **1,447 extracted rows**, comprising **1,413 verse rows** and **34 running headers/page numerals**.
- Secure mapped pairs: **990**.
- Exact normalized ordered-run pairs: **849**.
- Exact normalized, witness-unique singleton pairs: **57**.
- Bounded near-exact spelling/transcription variants: **84**.
- Manuscript rows inside the boundary left unmapped: **1,674**.
- Edition verse rows inside the boundary left unmapped: **423**.
- Manuscript rows after the printed endpoint: **3,631**.

## Method

Both witnesses were NFC-normalized, lowercased, and stripped of punctuation and spacing; Kyrgyz letters were preserved. A global `SequenceMatcher` alignment was run from the known opening anchor through the last printed verse. The map admits three evidence classes internally: normalized-exact rows in ordered runs of at least two; normalized-exact singletons only when the line is unique in both bounded segments; and near-exact rows only inside an equal-length replacement gap between ordered anchors, with normalized character similarity of at least 0.85. The public JSON deliberately records only the two source IDs for each accepted pair.

The resulting assertions require strict monotonicity, unique use of every manuscript and edition ID, the known opening pair, and the independently identified endpoint pair. Printed running headers and page numerals cannot enter the map because no manuscript line aligns to them.

## Ambiguous and excluded regions

The manuscript is not a line-for-line copy of the edition. It contains long expansions on PDF pages 6–12, 27–36, 41–46, 63–72, 76–82, and 84–87, while the edition sometimes compresses or omits manuscript wording. Those regions contain isolated formulas, reordered phrases, split or merged ideas, and low-confidence cursive transcriptions. They remain unmapped unless an individual row passes the conservative ordered tests above.

One repeated exact formula, manuscript `sayakbay-ms-current145:pdf025:l027` / edition `seytek-2012:p1153:b002:l024` (`Деп ошентип эр Сейтек`), was specifically excluded: it occurs three times in each bounded witness and appears as an unanchored singleton. Similar thematic wording elsewhere was not treated as identity. False-positive duplicate exclusions are therefore avoided at the cost of leaving real but non-demonstrable parallels in the release.

The final pair is a bounded near-exact variant rather than a literal normalized match: `болду` versus `болуп`. It is secure because it immediately follows the exact mapped penultimate line in both witnesses and is the last narrative line before the edition glossary.

## Output

`seytek-core-overlap-map.json` is the machine-readable exclusion candidate. It contains only secure manuscript and edition source-ID pairs; it does not modify either extraction or any release batch.
