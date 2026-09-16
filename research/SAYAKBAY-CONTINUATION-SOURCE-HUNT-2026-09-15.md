# Sayakbay continuation source acquisition — 2026-09-15

## Result

Complete public scans of both target shelf units were found. The hidden full-file convention is lowercase `web-` replacing the sample prefix `Obrazets-`.

| Current / old inventory | Full URL | Pages | Bytes | SHA-256 |
|---|---|---:|---:|---|
| 145 / 966 | https://manuscript.bizdin.kg/static/media/pdf/web-145-Seitek-Saiakba-Karalaev.pdf | 200 | 72,231,106 | `70a939883646a0893194f7a67db9f8b4b58bfa978bcf94fa595190f0e28ece92` |
| 146 / 967 | https://manuscript.bizdin.kg/static/media/pdf/web-146-Seitek-Saiakba-Karalaev.pdf | 252 | 131,467,767 | `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4` |

Local files are `sources/raw/manuscript-full-91-146/145.pdf` and `sources/raw/manuscript-full-91-146/146.pdf`. Both terminate with valid `%%EOF` and parse with Poppler. They are complete high-resolution color photographs of handwritten Kyrgyz Cyrillic notebooks, not the five-page samples.

Inventory 145 has 200 PDF images. The catalogue says physical pp. 191–387 (197 pages); visual inspection of PDF page 198 shows handwritten folio 386, with binding and adjacent leaf visible. Inventory 146 has 252 PDF images; visual inspection of PDF page 250 shows handwritten folio 631. Thus it necessarily includes the encyclopedia's cited inventory-146 p. 401. These endpoint anchors support complete-unit coverage.

## Coverage and first transcription target

The scans acquire the nominal 6,186 + 9,000 = **15,186 manuscript lines**. They do not yet certify the prior **10,623 missing-position estimate**, because manuscript lineation must be aligned directly to the 89,355-row released *Seytek* and the 3,154-row abridged print continuation.

Old 966/current 145 begins in released core text at `Айза сынып жоголсо`; its exact manuscript-side Kenen boundary is still unlocated. Therefore no whole initial range of 145 should yet be labeled novel. A rough line-density extrapolation would place the boundary tens of leaves into 145, but it is unsuitable for source certification.

Old 967/current 146 is wholly beyond the released core *Seytek* boundary and is the safest first transcription unit. Start with **inventory 146 PDF pages 1–10**, including the pages represented by the public sample. The sample's opening anchor `Бу кайран атаң арбагы` was absent verbatim from both released *Seytek* and the extracted 1991 continuation. This range is definitely additional relative to released core and is the best first range for locating alignment against the abridged continuation. Whether every line is novel relative to the 3,154 printed rows cannot be certified until that alignment is performed.

Next, transcribe inventory 146 around handwritten folio **401** (the encyclopedia's twins-birth citation), then its final ten text pages through folio 631. These anchors will establish the internal episode map and show how much narrative the print omitted. In parallel, inspect 145 sequentially from its opening overlap until the Kenen heading to fix the true boundary.

## Extraction feasibility

The PDFs report ACDSee / ABBYY FineReader 12 metadata and 2848 × 4272-point pages, but contain no extractable text layer: `pdftotext` returns form feeds only. Kyrgyz Tesseract on 2200-pixel renders of first and terminal pages produced mostly unusable text because the source is cursive handwriting. Resolution is sufficient for human reading and model-assisted handwriting recognition.

The recommended workflow is page rendering, handwriting recognition or assisted manual transcription, and reviewed alignment, retaining inventory, PDF page, handwritten folio, and line coordinates. Conventional OCR output should not enter the corpus without line-level review.

## Other public editions checked

A complete 262-page 1960 *Seytek* scan was downloaded from https://new.bizdin.kg/kniga/seytek-1960-g to `sources/raw/continuation-source-hunt/seytek-1960-bizdin.pdf` (4,095,788 bytes; SHA-256 `af7a17e9484a29c2001736a790ddc3cf110cfe58e62ac7e731d495844f856067`). It ends under `СӨЗ АЯГЫ` with Seytek before Kenen's birth and adds zero continuation rows.

The 2026 Internet Archive corpus at https://archive.org/details/manas-semetey-seytek-karalaev-kirgizca-turkce reports 89,327 *Seytek* verses. Its downloaded OCR text is 5,338,010 bytes, SHA-256 `a79bd8505c99e6800b65a685d1b8778fa0dbf552bfb6cd0a3f39873db1ec1a06`, and ends at `San kara kütkön bay bolup.`, the known pre-continuation endpoint. It also adds zero continuation rows.

No corpus or release file was changed, and no external request was submitted.
