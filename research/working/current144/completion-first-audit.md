# Current inventory 144 completion-first audit

Prepared 2026-09-16. This is a research checkpoint only; it does not add manuscript rows to the corpus.

## Identification and physical extent

- Current inventory **144** is old inventory **965**, *Seytek and Akzholtoi marry fairy maidens (continuation)*, recorded in 1946.
- Full scan: `sources/raw/manuscript-full-91-146/144.pdf`, SHA-256 `d8791a47f71591706ce85ccf7c0e6f9d67e1f8b7543ee0ee3aa78dc153881da8`.
- The full PDF has **195 images**. PDF 1 is the outside front cover; PDF 2 is the archival title leaf; PDF 195 is the outside back cover. PDF 3 begins photographed folio 1, and PDF 193 is photographed folio 190. PDF 194 is an inside-cover/archive-note image rather than verse. PDF 3–193 contain 191 verse-bearing images for the catalogue's 190 manuscript pages, so one extra/repeated image or foliation anomaly remains unresolved; the page ledger deliberately does not interpolate folio numbers.
- The title leaf explicitly records **190 pages** and **6,092 lines** (`6092 строк`). The catalogue/crosswalk independently carries the same 6,092-line figure. Accordingly, **6,092 is the best supported physical narrative-line count**, but it remains the archive's physical tally rather than a new baseline-by-baseline transcription count. No complete current144 extraction exists from which to recompute it independently.

## Existing release representation

There is no `sayakbay-ms-current144` source ID in the extracted sources or release. The manuscript is nevertheless represented at episode/content level by the released `seytek-2012` witness:

- PDF 3 / folio 1 begins `Кара жерге кан тамса`; its following lines match the printed sequence at `seytek-2012:p1090:b005:l001` onward (`Кандан кызыл беттүүдөн`, `Калемдей каны чийилген`, `Канттан ширин сөздүүдөн`, etc.).
- The previously audited sample at manuscript folio 27 contains `Күндүзү жоро, түн жыргал / Жыргап турду кайран журт`, released as `seytek-2012:p0484:b002:l031`–`l032`. This also shows that manuscript order cannot be reduced to one continuous printed-page interval.
- A fresh middle check at PDF 100 (folio 97) matches the printed sequence around pages 1122–1123: manuscript `Эребай сенин кебиң... / Келген экен Бээжин... / Калк дүрбөткөн канаты... / Ар качандан Чоң-Бээжин / Чатак баштап, чыр кылган / Атадан калган адаты / Издесе келбес ал душман / Чабуулга өзү келгени...` corresponds to the normalized printed text at lines 52072–52094 and released `seytek-2012` rows.
- PDF 193 / folio 190 ends with the sequence released at `seytek-2012:p1148:b002:l006`–`l016`, ending `Мүшкүл жаңжал кылышып`. The next printed line, `Айза сынып жоголсо`, is the opening of current inventory 145, so the 144/145 boundary is directly corroborated.

These opening, interior, sampled, and ending witnesses support existing edition coverage. They do **not** prove a one-to-one accounting of all 6,092 physical manuscript positions: the printed edition normalizes wording and lineation and reorders at least some material. A complete transcription/alignment would still be required before claiming exact row coverage.

## Conservative untranslated-segment decision

**No unique untranslated segment is established by this audit.** Every legible test passage checked in the opening, middle, prior five-page sample, and ending has a released printed counterpart. Treating an unmatched cursive string as novel without a full diplomatic transcription and ordered alignment would create a false novelty risk. Current144 should therefore be marked **represented at witness/content level, exact physical coverage unresolved**, rather than added as 6,092 missing lines.

## Existing English count

The released `seytek-2012` witness contains **89,355 rows and 465,749 whitespace-delimited English words**. This is the existing English-bearing witness that contains all demonstrated current144 counterparts. It is not a current144-only word count because no certified manuscript-to-edition map isolates all and only inventory 144 rows.

## Strict one-to-one checkpoint

`scan-page-ledger.csv` hashes all 191 verse-bearing scan images and records manual baseline status without inventing a folio sequence. `secure-monotonic-crosswalk.json` contains the **41** physical positions that currently meet the strict standard of a visually inspected baseline, an exact ordered printed counterpart, and a released target row: 17 opening positions on PDF 3 and 24 positions on PDF 100. Their released ordinals increase monotonically from 379,746 to 381,942 and neither side is reused.

Against the archival 6,092-position tally, **6,051 positions remain unresolved**. The clear terminal sequence and the folio-27 sample provide strong content-overlap evidence, but they are excluded from the strict one-to-one count because the terminal page's full baseline numbering and the sample's globally monotonic placement have not been established. OCR was tested only as an aid and rejected for acceptance: Tesseract's Kyrgyz model does not read this cursive reliably. No catalogue position is assigned merely to make the page ledger sum to 6,092.
