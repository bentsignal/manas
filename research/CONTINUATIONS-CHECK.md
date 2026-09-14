# Kenen continuation: positive source coverage, incomplete archival coverage

Checked 14 September 2026 UTC. **No, the full 500,553 reported verses have not been acquired or reconciled.** No physical/digital witness has been established as preserving that entire count. The four earlier PDFs' 401,930 extracted display lines are not verse counts. No word-count completeness claim is supported.

## What the scan adds

The acquired scan `sources/raw/manas-aki-candidate.pdf` is actually **Seytek, Sayakbay Karalaev's variant**, Adabiyat, Frunze. The title page says 1991; bibliographic page/copyright say 1990; retain both. It has 353 PDF pages, 352 stated printed pages, ISBN 5-660-00194-7. Compilers: R. Z. Kydyrbaeva and A. Zhainakova. Original public file: [AKI library PDF](https://cdn-1.aki.kg/st_bilimlib/8/6ba4d8da68bdb70850cc2e35ec861c0213e5b51f.pdf). Bytes: 34,770,598. SHA-256: `68bc80c49971f65cf755f6ef4d49e22396d9ca913b53b1f18aace29563f74178`.

**This scan contains a substantial Kenen/Alymsaryk/Kulansaryk continuation beyond the 2012/2013 edition.** The exact junction is established by direct visual comparison, not name matching alone:

| Scan PDF page | Printed page | Visually checked evidence |
|---|---|---|
| 314 | 313 (number not printed on inspected image) | Akjoltoy's dream interpretation and gifts conclude with the same closing verse as Turar 2012/2013 PDF 1165. |
| 315 | 314 | New headings **КЕНЕН** and **КЕНЕНДИН ТӨРӨЛҮШҮ**. New verse begins with passing days and pregnancy, followed by Kenen's birth. |
| 325 | 324 | Kenen governs; Gulayym bears twins named Kulansaryk and Alymsaryk. |
| 346 | 345 | Kenen's horse Kertulpar is killed; Kenen continues fighting. |
| 347 | 346 | Chyngtengir captures Kenen; the narrative describes Kenen's execution. |
| 348 | 347 (number not printed on inspected image) | Twins and Zhelzhetpes escape; verse then ends and a parenthesized prose summary follows. |
| 349 | 348 | Glossary begins. |
| 353 | 352 | Contents independently lists Kenen and Kenen's birth at printed 314, glossary at 348. Colophon follows. |

Thus the added printed section occupies **PDF 315–348 / printed 314–347: 34 pages**. The previous report's phrase “birth/dream material” for the 2012 ending was loose: at this exact junction the scan proceeds into the birth section after the dream/gifts episode. The 2012 file stops at that earlier junction.

## It is explicitly abridged

The preface's final paragraph, **PDF 13 / printed 12**, was rendered and read visually. It explains editorial treatment of dialect forms and explicitly states that repetitions and verses judged artistically weak were shortened, while the composition was retained. The relevant short phrase is:

> Кайталоолор, көркөмдүк сапаты начар саптар гана кыскартылып

This is direct evidence of cuts. It rules out certifying this edition as the full archival continuation, even though its addition is valuable.

The last narrative page, PDF 348, has two verse columns followed by a distinct full-width parenthesized prose paragraph. The paragraph summarizes Zhelzhetpes taking the young twins away despite their wish to fight, and hiding them between two large rivers. Do not count or translate that editorial synopsis as recovered original verse. The full verse account of this ending still requires an unabridged witness. The preface and colophon inspected here do not supply a notebook-to-line crosswalk or identify the exact omitted verses.

## Preserved extraction and verification limits

Rendered continuation pages: `tmp/pdfs/seytek-1991-continuation/page-315.png` through `page-348.png`. Boundary, ending, preface and contents images are retained in `tmp/pdfs/` with `seytek-scan-` prefixes.

OCR of all 34 continuation pages is separately preserved in `sources/extracted/seytek-1991-continuation/page-315.txt` through `page-348.txt`. Preface OCR covers PDF 6–13. Engine: Tesseract 5.5.2, Kyrgyz model, automatic page segmentation; continuation renders are 2200 pixels high. `research/continuation-ocr-index.json` records per-file hashes and source identity.

There are **3,192 nonempty OCR display lines** across the 34 continuation pages. This includes headings, page labels and prose and is **not a verified verse count** or a completeness percentage. OCR visibly makes letter errors and sometimes places a page number within the column sequence. Most verse has not received line-by-line image comparison. Nothing was added to the released corpus.

## Inventory 960 is a real lead, but the references conflict

A. Zhainakova's [Kenen encyclopedia entry](https://tamgasoft.kg/dict/index.php?lang=en&lfrom=kg&word=%D0%BA%D0%B5%D0%BD%D0%B5%D0%BD) cites inventory 960, page 145, and inventory 960 generally for later events. No original manuscript scan corresponding to that citation was acquired.

A further source was acquired through [Bizdin's encyclopedia volume 2 catalogue](https://new.bizdin.kg/kniga/manas-entsiklopediyasy-2-tom/): `sources/raw/manas-encyclopedia-2-comparison.pdf`, 26,993,018 bytes, SHA-256 `1d6561fa30e52aa61e404b79f08d97f757e53391cad5648ec3d37d4b7444a946`. Its bibliography is image-based near the end. **PDF 653 / printed 429** was rendered, OCRed and visually checked. It lists:

| Entry year | Karalaev material | Old inventory | Stated pagination |
|---|---|---|---|
| 1943 | Seytek, part 7 | 960 | 1683–2022 |
| 1945 | Seytek, parts 8–10 | 961 / 962 / 963 | 2023–2200 / 2201–2320 / 2321–2462 |
| 1946 | Seytek, part 11 | 964 | 2463–2650 |
| 1946 | Seytek and Akjoltoy's marriages to fairy daughters, continuation | 965 / 966 | 190 pages / 191–387 |

The Kenen entry's 960/page145 and this bibliography's 960/pages1683–2022 are not reconciled. Different pagination or inventory systems, or a citation error, are possibilities—not established explanations. **Do not relabel inventory 965 or 966 as the missing continuation on inference alone.** Request descriptions and a crosswalk for **960–966**, plus the exact item/page underlying the Kenen citation. The 88-record online inventory lacks an exact match for old 960. Public catalogue form searches for 960, 965 and 966 produced no manuscript links in this check; indexed searches found citations, not public full scans.

## What remains necessary

1. An institution-confirmed original manuscript/copy set underlying the reported 500,553 verses, including how alternate takes, copies and continuation boundaries were counted.
2. Full continuation scans, with clarification of the conflicting inventory references above and restoration of the omitted ending/repetitions.
3. A crosswalk between this abridged scan, the Turar 2012/2013 edition, the 2018 two-volume Seytek edition and the manuscripts. Physical 2018 holdings are identified in FULL-SOURCE-FOLLOWUP.md; their textual completeness is unverified.
4. Verified transcription and page/column lineation before translating or certifying any new source lines.

The prepared, unsent institutional request in FULL-SOURCE-FOLLOWUP.md has been updated with the new 960–966 discrepancy and the explicit 1990/1991 abridgement evidence. No correspondence was sent. This report, OCR index and separate extracts leave the shared release and source manifest unchanged.
