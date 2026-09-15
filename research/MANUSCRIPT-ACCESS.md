# Sayakbay Karalaev manuscript access and inventory crosswalk

Checked 2026-09-15 against the public catalog at <https://manuscript.bizdin.kg/>.

## Inventory crosswalk

The catalog record pages expose both `Инвентарный номер` (current inventory number) and `Предыдущее название инвентаря` (previous inventory number). The verified crosswalk for this run is:

| Previous inventory | Current inventory | Note |
|---:|---:|---|
| 925 | 104 | Directly displayed on the record page. |
| 926 | 105 | Anomaly: current 105 is titled “Манас. Саякбай Каралаев,” but its page assigns authorship to Тоголок Молдо and omits the previous-inventory field. Treat 926 → 105 as an inferred sequence position, not a catalog-confirmed pair. |
| 927–944 | 106–123 | Direct, sequential one-to-one mapping: `current = previous - 821`. |
| 945–966 | 124–145 | Direct, sequential one-to-one mapping: `current = previous - 821`. |

Thus the final records map as follows: 960 → 139, 961 → 140, 962 → 141, 963 → 142, 964 → 143, 965 → 144, and 966 → 145.

## Public files are samples

The record pages link PDFs whose filenames begin with `Obrazets-`; the link title and visible button both say `Скачать образец` (“download sample”). They are embedded with ViewerJS using the same sample URL. Examples:

- Previous 925/current 104: <https://manuscript.bizdin.kg/static/media/pdf/Obrazets-104-Semetei-Kanykeidin-Bukaraga-kachyshynyn-bashy-Siakbai-Karalaev.pdf>
- Previous 960/current 139: <https://manuscript.bizdin.kg/static/media/pdf/Obrazets-139-Seitek-VII-bolum-Saiakba-Karalaev.pdf>
- Previous 961/current 140: <https://manuscript.bizdin.kg/static/media/pdf/Obrazets-140-Seitek-VIIIb-bolum-Saiakba-Karalaev.pdf>
- Previous 962/current 141: <https://manuscript.bizdin.kg/static/media/pdf/Obrazets-141-Seitek-IX-bolum-Saiakba-Karalaev.pdf>
- Previous 963/current 142: <https://manuscript.bizdin.kg/static/media/pdf/Obrazets-142-Seitek-X-bolum-Saiakba-Karalaev.pdf>
- Previous 964/current 143: <https://manuscript.bizdin.kg/static/media/pdf/Obrazets-143-Seitek-XI-bolum-Saiakba-Karalaev.pdf>
- Previous 965/current 144: <https://manuscript.bizdin.kg/static/media/pdf/Obrazets-144-Seitek-Seitek-menen-Akzholtoidun-perinin-kyzdaryna-uilonushu-ulandysy-Saiakba-Karalaev.pdf>
- Previous 966/current 145: <https://manuscript.bizdin.kg/static/media/pdf/Obrazets-145-Seitek-Saiakba-Karalaev.pdf>

The current-104 sample was downloaded temporarily for verification only. It is a valid PDF 1.5 file of 2,311,069 bytes with 5 pages and SHA-256 `ed9a6e62e5e245084d09a6792d94750b5dce7e5670d4559b1ba36115f9faa634`. The catalog metadata describes current 104 as a 203-page manuscript. The linked PDF therefore contains only a five-page sample, not the complete notebook. No scan was copied into this repository.

## Full-access blocker

No public full-notebook asset was found. The public record HTML, bundled JavaScript, sitemap, and “Открытые рукописи” listing expose catalog pages, posters, and `Obrazets` PDFs, but no IIIF manifest, image service, full-file API, cloud-storage link, or original-scan endpoint. `robots.txt` returns the site's ordinary not-found page. For current 104, the same filename without `Obrazets-` and plausible `Full-` and `Original-` variants all return HTTP 404. The public evidence supports metadata access and sample viewing only; complete scans require a different, presently undisclosed access route.

## Sample collation

### Inventories 945–952 / current 124–131

Manual visual comparison of these handwritten Latin-script samples with the local normalized *Semetey* witness gives three exact and three probable printed ranges. Inventories 945/124 (manuscript leaves 400–403) match printed pages 763–766, 946/125 (leaves 533–536) match pages 1082–1085, and 947/126 (leaves 258–261) match pages 906–910. Distinctive ordered anchors include `Талаага салган мунара — / Мунараны сураба`, the Күлчоро–Канчоро passage beginning `Күлчоро менен Канчоро / Экөөбүздү бөлдү деп`, and `Оймок ооз, бото көз / Ойкуштаган кара көз`.

Inventories 948/127 (leaves 880–883), 949/128 (leaves 1–4), and 950/129 (beginning at leaf 240) probably correspond respectively to printed pages 971–974, the opening of “Семетейдин өлүшү” on pages 1010–1014, and approximately pages 1172–1176. Names, formulas, and their order support those ranges, but the cursive does not justify exact page-by-page claims. The cover of 951/130 identifies it as *Семетейдин өлүмү*, II-28; its sampled leaves 361–364 have a probable Semetey-death/lament overlap, but the exact printed range remains unresolved. The cover of 952/131 likewise identifies it as *Семетейдин өлүмү*, II-29; its sampled leaves 602–605 have a probable Semetey-death/lament overlap, but the exact printed range remains unresolved. No demonstrably novel lines were found in any of the eight samples; for the unresolved samples, that means only that the available images do not establish novelty, so 951–952 support no defensible novelty claim. No duplicate or contents page was identified in the six aligned samples.

### Inventories 953–959 / current 132–138

The seven five-page samples contain 26 distinct verse-page images after excluding their covers, the contents page in 956/135, and a second crop of manuscript leaf 35 repeated in 954/133. Ordered multi-line comparison found every sampled verse page in the local normalized *Semetey* or *Seytek* witnesses and at stable positions in the released Kyrgyz text. No sampled range contains demonstrably novel manuscript lines. The samples therefore support the existing translation positions rather than adding new ones.

These manuscripts are handwritten in the older Latin-script Kyrgyz alphabet. The matching modern-Cyrillic witnesses establish content overlap, but not glyph-for-glyph identity: spelling, punctuation, line division, and minor wording may have been editorially normalized. A diplomatic transcription would require a specialist paleographic pass over the scans. Page-level anchors, checksums, and temporary OCR artifacts are recorded in the local working report at `/tmp/karalaev-953-959/report.md`; no sample scan is stored in the repository.

### Inventories 960–966 / current 139–145

Manual comparison of the five-page samples with the 2012/13 *Seytek* edition found the following overlaps. Manuscript page numbers are those written on the photographed leaves; printed page numbers refer to the 1,172-page edition.

| Previous/current inventory | Manuscript page | Transcribed anchor | Printed page |
|---|---:|---|---:|
| 960/139 | 1638 | `Урунарга тоо таппай / Урушарга жоо таппай / Кирерине чаң таппай / Тийишерге жан таппай` | 71 |
| 963/142 | 2322 | `Эр Сарыбай баатырды / Эр экен деп кенебейт / Эрдик менен шердигин / Бучкагына теңебейт` | 911–913 |
| 964/143 | 2467 | `Кабар угуп капырдан / Каткырып күлүп сүйүнүп / Жоо кийимин кийинип / Жоо бөрүсү кайран эр` | 1124 |
| 965/144 | 27 | `Күндүзү жоро, түн жыргал / Жыргап турду кайран журт / Өзөн бойлой өр тартып / Конуп турду кайран журт` | 484 |
| 966/145 | 191–192 | `Айза сынып жоголсо / Айбалтаны алышып / Кезенишкен кыраандар / Кезектешип салышып`; later, `Ажалдуу киши кайтабы / Бел боосу бар азамат / Өлүмдөн кайра кайтабы?` | 1148 |

The 961/140 and 962/141 samples probably overlap the same received text: their legible names, formulas, and battle context agree with *Seytek*, and 962 precedes the firmly aligned Sarybay material in 963. Their blurred, tightly written images do not support a unique long-string or printed-page alignment, so this remains probable rather than demonstrated.

These samples corroborate the manuscripts' incorporation into the 2012/13 *Seytek*. They add no demonstrably novel continuation lines. The inventory sequence 960–966 maps stably to current 139–145, but the sampled text comes from different narrative locations and should not be treated as one continuous passage.
