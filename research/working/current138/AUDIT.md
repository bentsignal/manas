# Current inventory 138 completion-first coverage audit

Source: `sources/raw/manuscript-full-91-146/138.pdf`
SHA-256: `c65d805e5d8e8d6fce26f796b920f317e683dfbcc1493e7a856ba98db6f84ab4`

## Physical and catalogue extent

The scan has 211 PDF pages. PDF page 1 is the outside cover, page 2 is the title/catalogue leaf, the photographed narrative begins on PDF page 3 at folio 1223 and ends on PDF page 209 at folio 1427, page 210 is the closing count/date leaf, and page 211 is the back cover. The 207 narrative images therefore contain two extra photographs or duplicates relative to the inclusive **205-folio** range 1223–1427; image count must not be substituted for narrative extent.

The title leaf has an older `20600 строк` crossed out and corrected to **`5326 строк`**. The closing leaf independently records **5,326**, and the catalogue assigns the same count to old inventory 959/current inventory 138 (*Seytek*, part VI). This three-way agreement is the stable physical narrative count.

## Episode boundaries and released representation

The exact opening counterpart is `Өчкөн оттор жагылып,`, released as `seytek-2012:p0996:b002:l037`, ordinal **372,251**. The terminal episode ends with `Теги муңайсаң боло мен үчүн.`, `seytek-2012:p0644:b003:l011`, ordinal **344,121**, immediately before current inventory 139 opens with `Чыңаалаган душмандын` at ordinal 344,122. The terminal leaf also visibly preserves the nearby ordered anchor `Айбатың артык, заарың күч` (ordinal 344,097), supporting that closing placement.

These endpoints are reversed in the 2012 edition: the physical opening maps to the later printed position. Consequently there is **no defensible continuous released span in manuscript order**. The smallest monotonic printed envelope containing both exact endpoints is ordinals 344,121–372,251, inclusive: **28,131 released lines**, **144,444 whitespace-delimited English words** (144,293 regex word tokens). It is an editorial envelope containing intervening reordered or interleaved material, not 28,131 direct counterparts.

## Completion result

| evidence class | lines | disposition |
|---|---:|---|
| catalogue/physical narrative count | 5,326 | independently recorded on title and closing leaves |
| endpoint-containing printed envelope | 28,131 | already translated, but not a continuous manuscript-order span |
| catalogue minus printed envelope | -22,805 | editorial-order discrepancy, not a missing-line count |
| securely unique untranslated lines | 0 | none demonstrated |

The endpoint reversal prevents a one-to-one omission calculation. It also supplies positive evidence that inventory 138 is represented in the released witness at both physical ends. No line or segment can be securely classified as unique and untranslated from the present evidence.

The compact evidence is recorded in `monotonic-crosswalk.json`.
