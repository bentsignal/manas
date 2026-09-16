# Page 107 / folio 490 reviewed transcription

Completed 37 visible verse baselines as exactly 37 narrative JSONL rows, with sequential IDs `sayakbay-ms-current146:pdf107:l001` through `sayakbay-ms-current146:pdf107:l037`. All rows have best-effort Kyrgyz transcription and English translation. Schema keys match `page-106.reviewed.jsonl`; `raw` and `text` retain the same reading, and `bbox` is null.

## Visual accounting

Source: `sources/raw/manuscript-full-91-146/146.pdf`, PDF page 107 (one-based), handwritten folio 490. SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`.

Inspected a full-page 1200 × 1800 overview and high-resolution PyMuPDF crops at native coordinate scale (the PDF page is 2848 × 4272), followed by 1.2× detail crops. Rendering and image transfer used memory only; no image or scratch files were written. Broad crops covered x=580–2220 and y=380–1320, 1300–2350, 2330–3300, and 3270–3940. Detail crops covered x=600–2200 and y=380–930, 1670–2340, 2380–2760, and 3150–3460. Overlapping crop boundaries were reconciled against the overview to avoid counting a baseline twice.

Top-to-bottom count audit:

| Rows | Count | First and last baseline |
| --- | ---: | --- |
| 001–010 | 10 | Суукка тоңбос жабуусун / Башынан мүшкүл иш көргөн |
| 011–020 | 10 | Чымындай жанга күч көргөн / Бурчак болчу булуттай |
| 021–030 | 10 | Заар жүзүнө айланып / Балаасы кабат иш көрдүм |
| 031–037 | 7 | Көргөн түшүм оңкон түш / Бир мүшкүлгө калган түш |

The folio numeral 490 is metadata, not a verse row. Pencil brackets, underlining, and a small cross are not extra baselines; the underlined verse at l017 remains included. The final two lines are separate baselines. No heading, continuation fragment, or verse baseline was dropped or merged.

## Reading limits

23 rows are `visually_transcribed`; 14 are `uncertain`; none are `unreadable`. Status describes the transcription, not certification by a Kyrgyz manuscript specialist. Editorial punctuation and quotation marks aid reading and do not claim a diplomatic reproduction of every pen mark.

Uncertain rows are l001, l002, l004, l005, l006, l015, l017, l019, l021, l024, l025, l031, l034, and l035. Each JSONL note identifies the actual word, ending, or interpretation at issue. In particular, l006's epithet and l019's sword adjective remain provisional; l017/l034 retain apparent `авам` and the resulting change of voice. At l031 the apparent `оңкон` has a positive sense at odds with the ominous context; no unwritten negative syllable was inserted. The English follows that provisional reading. At l024–025 literal translations preserve the unusual phrasing instead of silently repairing it.

## Printed verification and exact overlap candidates

Local extracted printed witnesses were searched only after the manuscript overview and crops were read. The relevant witness is `sources/extracted/seytek-1991-continuation/page-333.txt`. Locations below are physical text-file line numbers, not manuscript baselines. The label page 333 is the extracted witness filename, not an independently verified printed folio.

There are 10 verbatim full-line candidates, including punctuation, and 7 additional full-line candidates whose word sequences agree exactly after ignoring punctuation and case. No spelling substitutions, fuzzy matching, or approximate sequence alignment were used to declare these candidates. They verify individual lines, not the whole page.

| Manuscript row | Witness text-file line | Agreement | Witness text |
| --- | ---: | --- | --- |
| l007 | 105 | Verbatim | Эбегей, Көгөй эки дөө, |
| l008 | 106 | Verbatim | Эсинен кетип бул экөө, |
| l009 | 107 | Exact words; punctuation differs | Башта күнү түш көргөн |
| l010 | 108 | Exact words; punctuation differs | Башынан мүшкүл иш көргөн, |
| l012 | 110 | Exact words; punctuation differs | Чын кыргыз үчүн түш көргөн. |
| l013 | 111 | Verbatim | Уялаш жолборс эгизди, |
| l014 | 112 | Exact words; punctuation differs | Эбегей, Көгөй чакырды |
| l015 | 113 | Verbatim | Эки арстан теңизди. |
| l022 | 115 | Verbatim | Экөө жетип келгенде, |
| l023 | 116 | Exact words; punctuation differs | Акырын айтып, кеп баштап, |
| l024 | 117 | Verbatim | Аяк жагын бек таштап, |
| l025 | 118 | Verbatim | Күнгө келди Эбегей, |
| l026 | 120 | Exact words; punctuation differs | Түш көрдүм, балам, жору деп, |
| l027 | 121 | Exact words; punctuation differs | Тилге келди эр Көгөй: |
| l028 | 123 | Verbatim | Эки уялаш жолборсум, |
| l029 | 124 | Verbatim | Уйкуда мүшкүл түш көрдүм, |
| l030 | 125 | Verbatim | Балаасы кабат иш көрдүм, |

The ordered correspondence covers l007–l015 with a lexical difference at l011: manuscript `жанга`, printed extraction `жангы` (witness line 109). That line is not counted as exact. The witness then resumes at manuscript l022; it does not supply the intervening l016–l021. It continues through l030, then proceeds to `Ала-Тоону кан басып` at witness line 126 rather than manuscript l031–l037. No printed lines were substituted for these manuscript passages. The opening six manuscript lines also have no exact counterpart in this located witness passage. Formulaic matches elsewhere are not claimed as passage alignment.

## Validation

Command:

```text
python3 scripts/validate-manuscript-transcription.py research/working/current146/page-107.reviewed.jsonl --pages 107 --source-id sayakbay-ms-current146 --pdf sources/raw/manuscript-full-91-146/146.pdf --require-english
```

Result: PASS (exit 0). 37 rows; 37 narrative lines; 232 English words using the validator's word-count expression; statuses: 23 visually_transcribed, 14 uncertain. Sequential IDs, source digest, page restriction, English presence, and uncertainty-note requirements pass. A separate key-set comparison confirms the page-106 schema match. Validation checks structure and coverage representation; it does not resolve uncertain handwriting.

Only `research/working/current146/page-107.reviewed.jsonl` and this report were written. Canonical extraction, corpus batches, README, and git were not edited.
