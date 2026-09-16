# Old inventory 911 / current 90 full-scan collation checkpoint

Prepared 2026-09-15 from the newly located complete scan at <https://manuscript.bizdin.kg/static/media/pdf/90Manas-Manastyn-bala-chagy.pdf>. The ignored local source is `sources/raw/manas-ms-old911-current90-full.pdf`, 122,640,613 bytes, 302 PDF pages, SHA-256 `abe0b9bd1dfdcac97d6c3b2a32f30f7efaafc12850dd283e4f71ffe98709c013`.

## Complete processing pass

All 302 PDF pages were rendered and passed through a resumable OCR pipeline. The page-level output, text hashes, image paths, and nonblank-line counts are preserved in `research/working/manas-old911/tesseract-checkpoint-2026-09-15.json`; it records 302/302 completed pages and 4,446 nonblank OCR lines. The reusable pipeline is `scripts/ocr-manas-old911.sh`, with checkpoint generation in `scripts/summarize-manas-old911-ocr.py`.

The scan has five front-matter/scan-furniture pages, then a continuous manuscript run: PDF page 6 is handwritten leaf 1 and PDF page 299 is leaf 294. Thus `leaf = PDF page − 5` for all 294 manuscript leaves. PDF pages 300–302 are terminal scan furniture. This reconciles the catalogue's 294 manuscript pages with the PDF's 302 pages.

Tesseract does not reliably recognize this connected historical Latin-script Kyrgyz hand. Its text is suitable only for finding possible anchors; it cannot support a diplomatic transcription or a novelty claim. A tested general English handwritten-text model also produced language-model substitutions rather than reliable Kyrgyz readings and was rejected. Apparent OCR-only differences are excluded from the candidate list.

## Boundary alignment

The first narrative leaf aligns directly to the 2010 edition's opening at PDF page 16, source ID `manas-2010:p0016:b003:l001`. Visually legible sequential anchors include:

- `Түп атасы Түгөл кан,`
- `түбүнөн Кыдыр даарыган,`
- `Башкы атасы баары кан,`
- `Башынан Кыдыр даарыган.`
- `Түнөп өткөн жерине`
- `Түптүү мазар орногон`
- `Муну түбүнөн кудай оңдогон.`

The final manuscript leaf aligns to the 2010 edition at PDF page 144 and released ordinals 6,153–6,169. Its distinctive continuous sequence includes `Бул Алтай сага жер эмес`, `Бул Ошпур сага эл эмес`, `Ошпурдун тилин сен алсаң`, the paired cloth formulas `Кызыл-тазыл кырмызы / Кыргагын тартсам бөлүнбөйт` and `Жашыл ала тал жибек / Жан-жанын тытсам бөлүнбөйт`, and the Ошпур warning through `Жылкысын айтат: «Мөрүн» — деп`. These are released under source IDs `manas-2010:p0144:b002:l023` through `l039`.

Both boundaries therefore occupy the same narrative sequence as the 2010 edition. The final leaf occurs substantially later than the catalogue's rounded 5,082-line figure when measured using the release's physical lineation, which reaches ordinal 6,169 at the endpoint. Catalogue line counts and printed physical rows are not interchangeable.

## Novel-line decision

No defensibly novel manuscript verse is established yet. The machine-readable candidate file is `research/MANAS-OLD911-CANDIDATE-NOVEL-LINES-2026-09-15.json`; its candidate array is deliberately empty. The complete OCR pass supplies page coverage, while direct image review establishes both boundaries. It does not establish that every interior handwritten line is represented in the printed edition because 292 interior leaves still require diplomatic image-to-text collation.

The next reliable pass must review leaves 2–293 against the corresponding 2010 opening span, retaining manuscript image coordinates and accepting a novel candidate only when a readable manuscript line is absent after orthographic normalization and contextual alignment. The present evidence supports sequence identity and rejects padding, but it cannot certify zero internal omissions.
