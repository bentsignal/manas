# Inventory 145 / printed Kenen-continuation overlap audit

## Result

The ordered printed-continuation correspondence begins at manuscript `sayakbay-ms-current145:pdf088:l020` (`Ай баксарың күн арт`, a damaged/provisional reading) against the print's first narrative line, `seytek-1991-continuation:p0315:b002:l001` (`Ай бөксөрүп күн өтүп,`). The surrounding sequence fixes the boundary: the next manuscript lines correspond in order to `Арадан эчен күн өтүп`, `Тогуз айга толуптур`, the end of the pregnancy, and Berizaada's labor.

The last secure counterpart inside inventory 145 is manuscript `sayakbay-ms-current145:pdf199:l027` (`Сары алтынга тондуруп,`) against `seytek-1991-continuation:p0325:b001:l010` (`Сары алтынга толтуруп,`). The manuscript then has ten more physical lines through `sayakbay-ms-current145:pdf199:l037`; none has a secure one-to-one counterpart before this inventory ends. The printed continuation itself continues beyond page 325, so this is the end of the overlap **inside inventory 145**, not the end of the printed text.

The conservative map contains **517 secure one-to-one counterparts**:

- 421 have strong normalized textual similarity plus ordered neighborhood support;
- 95 are weaker manuscript/print variants accepted only because close counterparts flank them on both sides in the same order;
- one boundary line is accepted by direct contextual verification;
- 135 of the accepted pairs are exact after normalization.

Within the anchored manuscript tail, `pdf088:l020` through `pdf199:l037` contains 3,631 physical rows. Of those, 517 have secure printed counterparts and **3,114 are manuscript-only relative to this printed witness**. The latter are principally material removed by print abridgement, mixed with readings whose variation is too large for a defensible one-to-one assignment. “Manuscript-only” here is witness-relative; it is not a claim that the wording appears nowhere else in the epic.

The complete row-level result is in `printed-continuation-overlap-map.json`. It lists every accepted pair, every unmatched physical manuscript ID in the anchored tail, and 212 compact contiguous unmatched runs.

## Printed coverage inside inventory 145

The accepted mappings touch printed pages 315–325 and manuscript pages 88–199. Counts by printed page are:

| Printed page | Secure counterparts |
|---:|---:|
| 315 | 43 |
| 316 | 71 |
| 317 | 67 |
| 318 | 59 |
| 319 | 43 |
| 320 | 38 |
| 321 | 41 |
| 322 | 45 |
| 323 | 57 |
| 324 | 45 |
| 325 | 8 |

The large gaps between mapped runs are real editorial compression. For example, manuscript `pdf089:l014` maps to printed page 315 line 26, while the next accepted run does not resume until manuscript page 92 against printed page 315 line 29. Similar expansion/abridgement gaps recur throughout the alignment.

## Method

Both sources were normalized to lowercase Cyrillic letters with punctuation and spacing removed; Kyrgyz `ң`, `ө`, and `ү` were preserved. Candidate line pairs were scored with character-sequence similarity. Candidates were then constrained to a strictly increasing, one-to-one manuscript/print alignment.

Acceptance was deliberately stricter than best-string matching:

1. A high-similarity candidate needed a nearby ordered counterpart.
2. A weaker reading was retained only when close accepted counterparts occurred on both sides in manuscript and print.
3. Repeated formulas and isolated exact phrases were rejected when they lacked ordered episode context.
4. The opening line was checked directly against the following pregnancy-and-birth sequence because its present manuscript transcription is visibly/provisionally corrupt but its source position is unambiguous.

The JSON map preserves the observed manuscript and printed text independently. It does not silently normalize the manuscript reading to the printed edition.

## Pre-boundary manuscript section

Rows `sayakbay-ms-current145:pdf003:l001` through `sayakbay-ms-current145:pdf088:l019` total 2,664 physical positions. They belong to the battle material preceding Kenen's birth in manuscript order. The printed continuation places a severely compressed form of related battle material later in its editorial order, especially toward page 348, but the available hits are isolated, reordered, or formulaic.

For example, manuscript `pdf003:l007` and printed `p0348:b001:l004` both read `Маңдайлашып турушуп`, but a common battle formula by itself cannot establish a unique source position. Likewise, other exact hits in the first 88 pages recur as stock travel, battle, sleep, and lament formulas. None of those candidates is included in the secure map. Consequently, these 2,664 positions remain an unresolved candidate zone rather than being labeled either duplicate or novel.

## Accounting cautions

- The 517 mappings are safe deduplication evidence, not an estimate of total literary dependence.
- The 3,114 unmatched tail rows are physical manuscript positions absent from this one-to-one printed alignment; some may be loose variants rather than wholly new verses.
- The 455 printed positions between the first narrative line and the last secure printed counterpart that lack a mapped manuscript row reflect both print-only wording and manuscript readings too divergent to pair securely.
- Headings (`КЕНЕН`, `КЕНЕНДИН ТӨРӨЛҮШҮ`), page numbers, and later prose apparatus are outside the verse alignment.
- No canonical extraction, corpus batch, release count, or README was modified by this audit.
