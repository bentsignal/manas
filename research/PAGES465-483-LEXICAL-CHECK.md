# Lexical gaps at Manas2010 pages465 and483

Checked 2026-09-14 against the Kyrgyz source only; no prior English translation used. Both remain unresolved. Do not treat a spelling conjecture as an attested correction.

Source: `sources/raw/manas-2010.pdf`, SHA256 `53bb71b63a0ad255e815b57f23fb41c8f3160cf05fd7b374add3516c7ccd99d7`. Images inspected: `tmp/pdfs/pages-0463-0482/page-0465.png` and `tmp/pdfs/page-0483-lexical.png`. The latter was rendered anew at1800pixels. Raw extraction remains unchanged.

## 465:b001:l021 — Ататтарын оркойтуп,

The page visibly prints **Ататтарын**, not аттарын, аяттарын or атактарын. The sequence is battle preparation: weapons readied, preparation for killing, this line, spears projecting, axes displayed, bag-like noses swelling. The verb is understandable: [Yudakhin оркой-/оркойт-](https://el-sozduk.kg/оркой/) concerns protruding/projecting, causatively making something project. It does not identify the noun.

The [Yudakhin атат- entry](https://el-sozduk.kg/атат/) gives a causative verb concerning acquisition/allocation, with an Altay land example. It supplies no nominal weapon or equipment meaning that fits the inflection here. Candidate corrections require changing what is printed:

- **аттарын**: their horses/names, from [ат](https://el-sozduk.kg/ат/). Horses fit the preparation context, but deletion of an extra *ат* is uncorroborated. The source already has separate horse preparation lines; repetition is possible and proves nothing.
- **аталарын**: their fathers, from [ата](https://el-sozduk.kg/ата/). Different morphology and poor contextual fit.
- **аяттарын**: their Quranic verses or amulets, from [аят](https://el-sozduk.kg/аят/). The amulet sense could occur in martial religion, but no visible я or matching parallel supports it.
- **атактарын**: their fame/titles, from [атак](https://el-sozduk.kg/атак/). Requires a different consonant; a figurative reading is possible in principle but unattested here.

Exact-form and related-string search in the four locally extracted Kyrgyz works found no repairing parallel. [Speak.tatar’s Karalaev section18](https://speak.tatar/ru/lit/kir/text/manas-sayakbay-karalaev-01-18/) reproduces Ататтарын оркойтуп and the same surroundings; it is not an independent scan establishing a correction. A direct fetch was403, while search-index text exposed the passage. Search results from unrelated Kazakh educational material do not establish Kyrgyz epic usage.

**Action completed:** Removed `manas-2010:p0465:b001:l021` from the English file and ordered translated IDs in `corpus/batches/pages-0463-0482.json`. Classified it `unresolved_source`, with raw text and transliteration **Atattaryn orkoytup,** separately retained in `unresolved_passages`. The prior partial rendering “Their atat held high,” is retained only as uncounted partial English, not published translation.

Gap anchors:

- before: `manas-2010:p0465:b001:l020` — Кырылышка камынып,
- gap: `manas-2010:p0465:b001:l021`
- after: `manas-2010:p0465:b001:l022` — Айзаларын коркойтуп,

Batch now has **834translated verse rows /4355alphabetic English-token words**,168per-ID translation notes, one separately translated heading, one unresolved verse. Its source universe still contains835verse rows and one heading. All original835pairs were read before exclusion; no new English substitute has been inserted.

## 483:b001:l027 — Тоорактуу жоргодо,

The image visibly prints **Тоорактуу жоргодо,** after **Кең Алтайдын тоорагы,** and before **Он экиге толгондо**. The immediate speaker recalls fighting at age twelve in Altay and taking tea loaded on a thousand camels.

[Karalaev section19](https://speak.tatar/ru/lit/kir/text/manas-sayakbay-karalaev-01-19/) reproduces both lines exactly. Thus online text does not independently support жерге/жерде. Searches of local Kyrgyz extractions found no second occurrence of this phrase.

Тоорак is a flora term: the [Manas encyclopedia volume2](https://new.bizdin.kg/media/books/Манас_энциклопедиясы._2_том.pdf) explicitly lists it among shrub names in the epic. The more precise identification as black poplar was supplied in the root task; this check did not recover an independent dictionary entry proving that botanical specificity. Тоорактуу has the expected “having/with тоорак” structure.

[Yudakhin жорго](https://el-sozduk.kg/жорго/) gives pacing horse and pacing gait; figurative extensions concern smooth speech and related movement. None establishes a ground/place sense. Reading the printed words compositionally as something like “on a poplar-bearing pacer” fails to explain the combination. No evidence establishes a proper place-name Jorgo here. The plausible geographic sense “in poplar-covered ground” would require an explicitly conjectural replacement of жоргодо by жерде; it is not an English translation of the printed reading.

**Recommendation communicated:** Preserve483:l027 as an unresolved source verse and exclude it from translated counts. No root batch file edited by this worker. Leave483:l026 and:l028 at their source positions; do not combine them to conceal the gap.

Proposed gap anchors:

- before: `manas-2010:p0483:b001:l026` — Кең Алтайдын тоорагы,
- gap: `manas-2010:p0483:b001:l027` — Тоорактуу жоргодо,
- after: `manas-2010:p0483:b001:l028` — Он экиге толгондо

Preservable transliteration: **Tooraktuu zhorgodo,**. Resolution needs an independent Karalaev printed/manuscript witness or qualified lexical interpretation; neither is established by matching derivative web text.
