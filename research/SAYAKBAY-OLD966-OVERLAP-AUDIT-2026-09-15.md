# Sayakbay old 966/current 145 boundary and continuation overlap audit — 2026-09-15

## Finding

Current inventory **145 / old 966 does not begin at the Kenen continuation boundary**. Its catalogue sample begins with `Айза сынып жоголсо,`, which occurs exactly in the released 2013 *Seytek* text at `seytek-2012:p1148:b002:l017`. From that row through the released endpoint at `seytek-2012:p1165:b003:l034` are **1,409 included edition rows**. Consequently, treating all 6,186 catalogue lines of old 966 as missing continuation overcounts the missing source.

The 1990/1991 printed witness establishes the editorial boundary independently. Printed page 314 ends with Akzholtoy's interpretation of Seytek's dream of a future son, Kenen, and the same final line as the 2013 edition, `Сан кара күткөн бай болуп.` Printed page 315 immediately starts `КЕНЕН` / `КЕНЕНДИН ТӨРӨЛҮШҮ` and Kenen's birth. The corpus continuation begins at that heading and contains **3,154 source rows**, through page 348.

No episode-scale duplicate was found between those 3,154 continuation rows and the 89,355 released *Seytek* rows. All 3,154 are therefore useful additional source positions for coverage, although 415 rows use individual lines also found elsewhere in *Seytek* and short stock formulas recur. “Useful additional” here means a distinct continuation witness position, not globally unique wording.

## Exact boundary evidence

| Witness | Anchor | Position/result |
|---|---|---|
| current 145 / old 966 five-page sample | `Айза сынып жоголсо,` | exact match at `seytek-2012:p1148:b002:l017` |
| released 2013 *Seytek* | same anchor through final included row | 1,409 rows, pages 1148–1165 |
| released 2013 *Seytek* ending | `Сан кара күткөн бай болуп.` | `seytek-2012:p1165:b003:l034` |
| 1990/1991 print | same closing passage and line | printed p. 314 |
| 1990/1991 print continuation | `КЕНЕН` / `КЕНЕНДИН ТӨРӨЛҮШҮ` | printed p. 315; corpus `seytek-1991-continuation:p0315:b001:l001–l002` |

The old-966 sample's terminal catalogue anchor is `Букара чаар кабылан`; it was not found verbatim in either extracted witness. Old 967/current 146 begins `Бу кайранатаң арбагы` and ends `Жаткан жери мына ушул`; neither occurs verbatim in the extracted witnesses. These negative searches, together with old 966's exact opening overlap, show that 145 crosses from released core into later material, while the public samples do not expose the precise manuscript-side Kenen heading or line count at the junction.

## Core-to-print overlap test

Inputs were the exact ordered `source_ids` from all `pages-seytek-*.json` batches and all `pages-continuation-*.json` batches, resolved against their source JSONL files:

- released *Seytek*: 89,355 distinct included source IDs;
- printed continuation: 3,154 distinct included source IDs.

Normalization applied NFC and lowercase, stripped punctuation, and flattened `ң/ө/ү` to `н/о/у` to tolerate common OCR variation. Exact consecutive-window results were:

| Window length | Matching windows |
|---:|---:|
| 2 lines | 52 (26 distinct continuation starts) |
| 3 lines | 3 |
| 4 lines | 1 |
| 5+ lines | 0 |

The longest exact run is the four-line sleep formula at released p. 512 / continuation p. 331: `Чыканактап уйку алып` through `Жантайып уйку кандырып`. Another three-line run is the conventional suffering formula `Кең дүнүйө тар болуп` through `Бир жутууга зар болуп` at released p. 1135 / continuation p. 343.

At single-line level, 415 of 3,154 continuation positions have normalized wording found somewhere in the 89,355-row core; they represent 361 distinct normalized strings. Many are highly recurrent formulas. For example, `Акырын сүйлөп бек таштап` occurs 36 times in the core and five times in the continuation.

A fuzzy five-line-window check retrieved candidates by shared normalized tokens and ranked their joined text with character `SequenceMatcher` similarity. Its strongest candidate scores were 0.9903 and 0.9854. Both are the same stock battle sequence (`Мылтык атып, жаа тартып ... Кан төгүлүп шыркырап`) with OCR differences such as `жаанын/җаанын`; related versions occur at several core locations. The next strong result, 0.8704, is the sleep formula above with a differing first line. These are formula reuse inside different episodes, not evidence that the Kenen narrative was copied from the released core. There is no long boundary-aligned run, and no exact run of five lines.

## Coverage accounting

The catalogue arithmetic remains 6,186 + 9,000 = **15,186** lines for old 966–967. It is an archival shelf-unit total, not a proven total of unique post-*Seytek* continuation lines.

| Quantity | Count | Status |
|---|---:|---|
| released rows from exact old-966 opening anchor to 2013 endpoint | 1,409 | exact edition-row count |
| nominal old-966/967 catalogue total | 15,186 | archival catalogue count |
| provisional unique continuation target, `15,186 − 1,409` | 13,777 | estimate only |
| recovered printed continuation rows | 3,154 | exact corpus source-position count |
| provisional still-missing amount, `13,777 − 3,154` | 10,623 | estimate only |
| uncorrected raw difference, `15,186 − 3,154` | 12,032 | known overestimate if treated as wholly missing |

The 1,409 figure counts edited edition rows, not manuscript lines. The 1990/1991 print is explicitly abridged, and manuscript, edition, and OCR lineation need not map one-to-one. Therefore **10,623 is the best current planning estimate, not a certified missing-line count**. The exact unique total requires the complete scans of 145 and 146, followed by direct alignment across the Kenen heading and the abridged print.

## Sources and reproducibility

- current 145 record: https://manuscript.bizdin.kg/рукопись/СейтекN/
- current 145 sample: https://manuscript.bizdin.kg/static/media/pdf/Obrazets-145-Seitek-Saiakba-Karalaev.pdf — SHA-256 `3dfed3b53d3fe153c16b4b25de26b150dba281056e8d704e7dad972020ea43d2`
- current 146 record: https://manuscript.bizdin.kg/рукопись/СейтекE/
- current 146 sample: https://manuscript.bizdin.kg/static/media/pdf/Obrazets-146-Seitek-Saiakba-Karalaev.pdf — SHA-256 `6c4e8d0ac8bb63d138a323413d98109399751feed6f719f8f1a95764216c217c`
- 1990/1991 printed witness: `sources/raw/manas-aki-candidate.pdf` — SHA-256 `68bc80c49971f65cf755f6ef4d49e22396d9ca913b53b1f18aace29563f74178`
- released source: `sources/extracted/seytek-2012.lines.jsonl`
- continuation source: `sources/extracted/seytek-1991-continuation.lines.jsonl`

No corpus or release file was changed, and no external request was submitted.
