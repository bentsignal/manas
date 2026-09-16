# Current inventory 134 completion-first coverage audit

Source: `sources/raw/manuscript-full-91-146/134.pdf`
SHA-256: `517d7758719ae2beb23f5a361ee82faa12b1d7aab72aaa77cbd67089f539cbc3`

## Physical and catalogue extent

The scan has 220 PDF pages. PDF page 1 is the outside front cover, page 2 is the title/catalogue leaf, page 3 is a contents leaf, pages 4–219 are narrative manuscript images, and page 220 is the outside back cover. The photographed narrative runs from cumulative page 102/local page 1 through cumulative page 317/local page 216, giving **216 narrative images**. The title leaf reports **215 pages** and **6,480 lines**; the one-image excess is scan/manuscript accounting and does not displace the independently catalogued 6,480-line total. The older bibliography's `pp. 102–216 (115)` does not describe the photographed cumulative endpoint, which is visibly 317.

## Episode boundaries and released representation

The physical opening begins `Ашуусу бийик тоо ашам,`, released as `seytek-2012:p0077:b003:l001`, ordinal **299,676**. Inventory 135's earliest secure early-folio sequence begins `Кечээ Жылгындынын оюнда,` at ordinal **306,259**. Using that adjacent boundary, inventory 134's outer released envelope ends at ordinal **306,258**, `Чындаган зор бел экен,`.

The inclusive envelope contains **6,583 released lines** and **35,148 whitespace-delimited English words** (35,088 regex word tokens). It exceeds the manuscript catalogue count by 103 positions.

The terminal physical leaf demonstrates limited boundary overlap or editorial rearrangement rather than a clean one-to-one cutoff. Its ordered sequence includes `Жолборс абам Күлчоро` and `Көп адам жолборс дээр экен`, released at ordinals **306,361–306,362**, 103–104 positions after inventory 135's opening anchor. The same leaf continues through printed material beginning at least as late as ordinal 306,378. Thus the 6,583-line adjacent-boundary envelope is the best completion envelope, while terminal-leaf positions beyond it are shared/reordered boundary evidence rather than securely unique text.

## Completion result

| evidence class | lines | disposition |
|---|---:|---|
| catalogue/physical narrative count | 6,480 | title and catalogue total |
| adjacent-boundary released envelope | 6,583 | already translated |
| catalogue minus released envelope | -103 | editorial lineation/overlap discrepancy |
| securely unique untranslated lines | 0 | none demonstrated |

The close agreement between the catalogue count and the adjacent-boundary envelope, plus direct released matches at the physical opening and terminal leaf, supports completion coverage. Because the printed edition overlaps or reorders the 134/135 boundary, neither the 103-position excess nor terminal-leaf variants establish untranslated lines.

The compact evidence is recorded in `monotonic-crosswalk.json`.
