# Current146 page 27 / folio 410: bounded Astra audit

Independently rendered PDF page 27 with Poppler at 200 dpi and inspected the full page and enlarged crops. SHA-256: `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`. The handwritten folio is 410.

Recount: **33 real verse baselines**, all narrative, no heading, no added or dropped row. Every baseline has an English rendering. Output: `page-027.astra-audit.jsonl`, 33 rows and 202 whitespace-delimited English words. Seventeen rows are visually transcribed; sixteen retain explicit reading or interpretation uncertainty. Seven severely uncertain renderings are bracketed in the English itself (l001, l003, l014, l015, l017, l018, l027).

This is a materially improved draft, not a certified transcription. In particular, l014–15 and l017–18 remain poor readings and need a Kyrgyz manuscript specialist or clearer witness. Their English is provisional and must not be treated as established narrative detail.

## Printed counterparts

The following ordered passage is securely the same passage as the 1991 continuation. The printed OCR was used to resolve letterforms, but the manuscript was checked and its visible variants retained.

| Manuscript row | Printed continuation row | Assessment |
|---|---|---|
| l005 | p0325:b005:l036 | Same forty-doored gate line |
| l006 | p0325:b005:l037 | Same opening-one-door line |
| l007 | p0325:b005:l038 | Same eighty-years-of-provisions line |
| l008 | p0325:b005:l039 | Same travel-provisions line; manuscript separates Күл азыктан |
| l009 | p0325:b005:l040 | Same pack-animal line |
| l010 | p0325:b005:l041 | Same saddle-sore mule line |
| l011 | p0325:b005:l042 | Same question about khan; manuscript Ханга vs print Канга |
| l012 | p0326:b001:l001 | Same distress-of-people line |
| l019 | p0326:b001:l002 | Same gathering-everyone line; manuscript жыйнаптыр vs print жыйыптыр |

These nine rows are defensible counterpart exclusions from *additional unique* verse counts. l013–18 are genuine intervening manuscript baselines absent from this short printed span; do not exclude them merely because the surrounding passage overlaps. l022 resembles the later p0326:b001:l016 (Калың кытай кырк кан эл), but occurs in a different local sequence and ends журт; this is only a formulaic/possible counterpart candidate and is **not recommended for exclusion** without broader alignment. No counterpart claim is made for the other rows.

## Significant draft corrections

- l005–06 concern the forty-doored gateway and opening a door, not Karakhan and moving a sleeve.
- l007 concerns provisions sufficient for eighty years, not the passing of eighty years.
- l009–10 concern pack animals and mules, not banners.
- l011 asks what happened to the khan; it does not mention an envoy.
- l020–21 name Суурулган (Suurulgan).
- l022 concerns Kytai people of forty khans, not a Kyrgyz khan destroying people.
- l023 is distress (заманасы куурулган).
- l030 describes despair for one's life, not souls descending.
- l032–33 describe an army pouring forth and clamor rising skyward, not a bridge-maker and deliverance.

Validation: `validate-manuscript-transcription.py ... --pages 27 --source-id sayakbay-ms-current146 --pdf sources/raw/manuscript-full-91-146/146.pdf --require-english` passed with 33 sequential IDs, matching source hash, and English for all rows. `raw == text` holds throughout. No shared corpus or release files edited.
