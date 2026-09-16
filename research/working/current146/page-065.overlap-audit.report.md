# Current 146 page 65 — bounded overlap audit

## Result

The existing `page-065.reviewed.jsonl` remains valid. The cross-witness check did not reveal a transcription or English-translation error requiring a replacement reviewed JSONL.

This bounded audit identifies **16 secure one-to-one counterparts** in a globally ordered mapping against the printed continuation. It deliberately does not map plausible formula-level similarities, manuscript additions, relocated lines that would break the ordered alignment, or repetitions without a unique printed mate.

## Secure ordered mapping

| Manuscript ID | Manuscript text | Printed ID | Printed text | Relationship |
|---|---|---|---|---|
| `sayakbay-ms-current146:pdf065:l005` | Ала-Тоонун кыргызын, | `seytek-1991-continuation:p0327:b002:l004` | Ала-Тоодо кыргыздын | Secure grammatical variant in the same episode |
| `sayakbay-ms-current146:pdf065:l010` | Абайлап көргүн Кененди, | `seytek-1991-continuation:p0327:b002:l015` | — Абайлап көрдүм Кененди, | Secure imperative/past-tense variant opening the ordered run |
| `sayakbay-ms-current146:pdf065:l011` | Арстан, жолборс эренди, | `seytek-1991-continuation:p0327:b002:l016` | Арстан, жолборс эренди, | Exact |
| `sayakbay-ms-current146:pdf065:l012` | Абайладым беренди, | `seytek-1991-continuation:p0327:b002:l017` | Абайладым беренди, | Exact |
| `sayakbay-ms-current146:pdf065:l013` | Сырты кара, боору көк, | `seytek-1991-continuation:p0327:b002:l018` | Сырты кара, боору көк, | Exact |
| `sayakbay-ms-current146:pdf065:l014` | Кол куушуруп, кулдук деп, | `seytek-1991-continuation:p0327:b002:l019` | Кол куушуруп, кулдук деп, | Exact |
| `sayakbay-ms-current146:pdf065:l015` | Өзүңө кулдук кылдык деп, | `seytek-1991-continuation:p0327:b002:l020` | Өзүңө кулдук кылдык деп, | Exact |
| `sayakbay-ms-current146:pdf065:l016` | Багына берчү уул эмес, | `seytek-1991-continuation:p0327:b002:l021` | Багына берчү уул эмес, | Exact |
| `sayakbay-ms-current146:pdf065:l017` | Бир башы жоктун бири эмес, | `seytek-1991-continuation:p0327:b002:l022` | Бир башы жоктун бири эмес, | Exact |
| `sayakbay-ms-current146:pdf065:l018` | Айдоого көнүп берүүчү, | `seytek-1991-continuation:p0327:b002:l023` | Айдоого көнүп берүүчү | Exact apart from punctuation |
| `sayakbay-ms-current146:pdf065:l019` | Шибе, тыргоот эл эмес, | `seytek-1991-continuation:p0327:b002:l024` | Шибе, тыргоот эл эмес, | Exact |
| `sayakbay-ms-current146:pdf065:l022` | Кытайдан эл көп эмес, | `seytek-1991-continuation:p0327:b002:l025` | Кытайдын эли көп эмес, | Secure inflectional variant |
| `sayakbay-ms-current146:pdf065:l023` | Ак кыргыздан журт чоң эмес. | `seytek-1991-continuation:p0327:b002:l026` | Ал кыргыздын журту чөп эмес. | Secure contextual counterpart with material lexical variation |
| `sayakbay-ms-current146:pdf065:l025` | Баатыр Теңир, тилимди ал, | `seytek-1991-continuation:p0327:b002:l027` | Баатыр Теңир, тилимди ал, | Exact |
| `sayakbay-ms-current146:pdf065:l032` | Жазы жаак, жалпак тил, | `seytek-1991-continuation:p0327:b002:l028` | Жазы жаак, жалпак тил | Exact apart from punctuation |
| `sayakbay-ms-current146:pdf065:l033` | Жаңылбаган чечендин, | `seytek-1991-continuation:p0327:b002:l029` | Жаңылбаган чеченден, | Secure case-ending variant |

The mapping is monotonic in both witnesses. Manuscript rows 20–21 interrupt the print's 19→22 transition, rows 24 and 26–31 interrupt its 23→25→32 transition, and are preserved as manuscript material rather than forced into printed positions.

## Unmapped manuscript rows

- **Rows 1–4:** introductory universal-rule and Chyng Temir padishah lines; no unique local printed counterpart in the audited window.
- **Rows 6–7:** close counterparts to printed `p0327:b002:l032` and `p0327:b002:l037`, but the manuscript moves them before the Kenen description. Mapping them would cross the secure 10–33 alignment, so they remain explicitly unmapped as reordered material.
- **Rows 8–9:** counsel/injunction lines without unique one-to-one mates in the local printed passage.
- **Rows 20–21:** manuscript comments on valor and Chyng Temir's thunder; absent from the corresponding printed run.
- **Row 24:** a manuscript warning against rash action; no secure printed mate.
- **Rows 26–31:** additional counsel and repeated characterization of the heroic people; no unique ordered printed mates. Row 31 repeats row 28, and neither is assigned speculatively.
- **Rows 34–36:** additional description of an eloquent defender descended from heroes and standing under the banner; absent from the audited printed continuation window.

## Editorial decision

No `page-065.overlap-audit.reviewed.jsonl` was created because the existing reviewed transcription and translation remain defensible. For release deduplication, only the 16 mapped rows above should be treated as secure printed-edition overlap from this audit; all 20 unmapped rows should remain manuscript additions or unresolved variants.
