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
