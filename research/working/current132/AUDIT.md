# Current inventory 132 completion-first coverage audit

Source: `sources/raw/manuscript-full-91-146/132.pdf`
SHA-256: `ac6083d95fc662b730e76c12c8530f8a51cd6b2d50f3065c90402a628113e7fb`

## Physical and catalogue extent

The scan has 209 PDF pages. PDF page 1 is the outside front cover, page 2 is the title/catalogue leaf, pages 3–206 contain the photographed narrative, page 207 is blank, page 208 is a closing archival/count leaf with a pasted terminal excerpt, and page 209 is the outside back cover. The 204 narrative photographs exceed the title's **203 pages** by one scan image. The title and catalogue independently record **7,714 lines**, and the closing leaf repeats both 203 pages and 7,714 lines. That repeated line figure is the stable physical narrative count.

The catalogue identifies old inventory 953/current inventory 132 as *Semetey: continuation of Semetey's death*.

## Episode boundaries and released representation

The earliest securely collated opening-folio sequence begins `Кечээ кабарыңда бар бекен,`, released as `semetey-2-2013:p1322:b003:l016`, ordinal **288,461**. The same opening folio preserves the ordered Ak Taigan/Akshumkar mourning sequence, including exact counterparts `Айып болду ак тайган` and `Кайып болду ак тайган` at ordinals 288,469 and 288,471.

The closing leaf preserves the final printed sequence beginning `Ээ... адам, балбан болот экен деп,` and continuing through the terminal `Мөрөйдү алган Карадөө.`, `semetey-2-2013:p1418:b004:l035`, ordinal **295,923**. This is the last `semetey-2-2013` row; `seytek-2012` begins at the following release ordinal 295,924.

The inclusive released envelope contains **7,463 lines** and **42,321 whitespace-delimited English words** (42,393 regex word tokens). It is 251 positions shorter than the 7,714-line catalogue count.

## Completion result

| evidence class | lines | disposition |
|---|---:|---|
| catalogue/physical narrative count | 7,714 | repeated on title and closing leaves |
| released outer envelope | 7,463 | directly represented in `semetey-2-2013` |
| catalogue minus released envelope | 251 | unresolved lineation/variant difference |
| securely unique untranslated lines | 0 | none individually demonstrated |

The outer boundary anchors establish released representation from the opening folio through the manuscript terminal and the end of the printed Semetey witness. The 251-line shortfall is not by itself proof of 251 omissions: the opening anchor is the earliest securely collated sequence rather than a diplomatic reading of the faint first baseline, and manuscript/edition line division and variants can change totals. No particular physical line or continuous segment is securely shown to be absent from the release.

The compact evidence is recorded in `monotonic-crosswalk.json`.
