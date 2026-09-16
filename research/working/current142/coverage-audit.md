# Current inventory 142 / old 963 completion-first coverage audit

Checked 2026-09-16. This is a source and coverage audit only. It does not add a canonical transcription, translation, batch, or release source.

## Source identity and physical extent

The recovered full scan is `sources/raw/manuscript-full-91-146/142.pdf`:

- public source: `https://manuscript.bizdin.kg/static/media/pdf/web-142-Seitek-X-bolum-Saiakba-Karalaev.pdf`
- SHA-256: `2b1fd33d35b9fec662724180743e44a26bc44d8b347d5f99c373acf98cb6c73f`
- file size: **54,792,282 bytes**
- PDF images: **149**
- catalogue identity: current **142**, old **963**, Sayakbay Karalaev, *Seytek*, part X
- encyclopedia pagination: **2321–2462**

The online catalogue/crosswalk has no line count for old 963. The manuscript's photographed title leaf supplies one directly: **7,668 lines / 141 pages**, dated **1945**. The visible notation reads `7668 строк` and `141 стр.`. This is stronger evidence than estimating lines from PDF image count, because the PDF also includes covers, title/archival matter, and extra photographs.

The opening narrative sample is continuous and agrees with the encyclopedia foliation. PDF images 4–8 show folios **2321–2325**. Each leaf carries a handwritten line total in the right margin:

| PDF image | Folio | visible recorded line total |
|---:|---:|---:|
| 4 | 2321 | 33 |
| 5 | 2322 | 36 |
| 6 | 2323 | 39 |
| 7 | 2324 | 41 |
| 8 | 2325 | 52 |
| **Sample total** | | **201** |

The scan pages were rendered and inspected directly. Temporary page renderings were removed after the boundary evidence and counts were recorded.

## Effect on the catalogue arithmetic

The earlier Seytek crosswalk treated currents 140–142 / old 961–963 as three blank catalogue counts. Its known total for old 954–966 was **76,568 lines**. Adding the physical title-leaf count for old 963 raises the known subtotal to **84,236**, only **461** below the published 84,697-line core target before either old 961 or 962 is counted.

Because old 961 and 962 are substantial 178- and 120-page units, the sequence total will necessarily exceed 84,697 when their positive counts are included. This directly disproves the earlier planning hypothesis that all three blank units together might supply only 8,129 lines. It reinforces the existing warning that catalogue manuscripts and the edited core total are not an additive one-to-one partition: overlap, editorial selection, repeated material, alternative recording layers, or boundary differences must be resolved at line level.

## Exact printed-witness boundaries

The project has **89,355 released rows** from `seytek-2012`. Direct visual comparison establishes both boundaries of inventory 142 in that witness.

- Manuscript PDF page 4 / folio 2321 begins `Каарына чыдабай,`. Its exact released counterpart is `seytek-2012:p0913:b004:l002`, ordinal **365,621**, English **“Can't stand his anger”**.
- Manuscript PDF page 148 / folio 2462 ends `Дарт кумарды чагышып,`. Its exact released counterpart is `seytek-2012:p1005:b002:l006`, ordinal **372,940**, English **“Easing our aching longing,”**.
- Current 143 begins on the immediately following released row, ordinal 372,941, `Колтукташып басышып,`. This independently confirms the terminal boundary and preserves manuscript order across the inventory break.

The opening five manuscript leaves give a substantial exact ordered check. Their manuscript tallies sum to **201 lines**, and they correspond consecutively to released ordinals **365,621–365,821**:

| manuscript PDF / folio | physical lines | released ordinals | first released line | last released line |
|---|---:|---:|---|---|
| 4 / 2321 | 33 | 365,621–365,653 | `Каарына чыдабай,` | `Кашкаңдап күлүп сүйүнүп,` |
| 5 / 2322 | 36 | 365,654–365,689 | `Эр Сарыбай баатырды,` | `Жаралып келген мерген ал.` |
| 6 / 2323 | 39 | 365,690–365,728 | `Найза жаза сайбаган,` | `Күлчоро менен жоролош` |
| 7 / 2324 | 41 | 365,729–365,769 | `Чечен менен таңдайлаш,` | `Айдап жүрүп жегидей,` |
| 8 / 2325 | 52 | 365,770–365,821 | `Арбагын көрсөң момундай,` | `Жер кетилип дуу болуп,` |

The closing manuscript leaf supplies a second exact ordered block: its **57 lines** correspond consecutively to released ordinals **372,884–372,940**, from `Караңгы жок шам жарык,` through `Дарт кумарды чагышып,`.

These checks establish a monotonic outer crosswalk with **258 sequentially checked boundary lines** and no order reversal. They do not constitute a diplomatic assertion for every interior manuscript line.

## Continuous released span

The inclusive interval from ordinal 365,621 through 372,940 contains:

- **7,320 released lines**;
- **39,020 English whitespace-delimited words**;
- **39,002 English regex word tokens**.

Every row in the interval is already translated under source ID `seytek-2012`. The manuscript's physical/copyist count is 7,668, so the gross difference is **348 lines** (`7,668 - 7,320`). That difference is only an unresolved count surplus. It may contain editorial omissions, but it can also contain split-versus-joined lineation, repeated formulas, copyist counting practice, or other witness differences.

## Release and translation coverage

Direct search of the release, batch descriptors, progress metadata, and source manifest finds:

- source IDs beginning `sayakbay-ms-current142`: **0**
- released inventory-142 manuscript rows: **0**
- direct inventory-142 English translation rows: **0**
- direct inventory-142 English word count: **0**
- continuously corresponding released printed rows: **7,320**
- English words already available for that printed interval: **39,020**

Inventory 142 is therefore wholly unreleased as a direct manuscript source, while its complete narrative interval is represented at episode level by the translated printed witness.

## Unique untranslated segment assessment

No specific unique untranslated segment is defensible yet. The evidence establishes a complete available scan, a physical source count of 7,668 lines, exact ordered checks for 258 boundary lines, and a continuous 7,320-line released interval. It does not localize the 348-line count surplus or distinguish omitted wording from lineation differences.

For completion-first accounting, inventory 142 should be classified as **represented by an existing translated printed witness; zero conservatively addable lines identified; 348 physical-count surplus unresolved**. A releaseable unique count requires complete physical transcription and a conservative ordered overlap map. Catalogue arithmetic and boundary continuity are not adequate grounds for declaring individual lines unique.

## Recommended next action

Transcribe the interior leaves with stable `sayakbay-ms-current142:pdfNNN:lNNN` IDs and align them monotonically inside ordinals 365,621–372,940. The highest-value work is to locate where the cumulative manuscript tally diverges from the released row count. Only sustained manuscript runs bounded on both sides by secure ordered printed anchors should be classified as unique omitted verse. The compact machine-readable result is `monotonic-crosswalk.json`.
