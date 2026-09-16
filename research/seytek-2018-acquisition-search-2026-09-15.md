# 2018 Karalaev *Seytek* acquisition search — 2026-09-15

## Result

No openly downloadable scan of the two-volume 2018 *Seytek* edition was located. The strongest access route is a verified, currently available complete set at Columbia University Libraries/ReCAP, catalog record **14338080**, with both volumes (`v.1-2`) held offsite and explicit **Scan**, **Pick-Up**, **Interlibrary Loan**, and **Scan & Deliver** request routes:

- Catalog: https://clio.columbia.edu/catalog/14338080
- Public JSON metadata: https://clio.columbia.edu/catalog/14338080.json
- MARC record: https://clio.columbia.edu/catalog/14338080.marc
- ReCAP scan request endpoint: https://valet.cul.columbia.edu/recap_scan/14338080
- Interlibrary-loan endpoint: https://valet.cul.columbia.edu/ill_scan/14338080
- Campus scan endpoint: https://valet.cul.columbia.edu/campus_scan/14338080
- ReCAP loan endpoint: https://valet.cul.columbia.edu/recap_loan/14338080

The live catalog reports call number **PL44.9.S45 K37 2018g**, location **Offsite**, status **Available**, and holdings **v.1-2**. Its item records identify volume 1 as barcode **CU28032993**, UUID `d32fb117-92f8-521b-91fd-6cf80fb45d87`, and volume 2 as barcode **CU28032985**, UUID `bec2086e-afc4-5cfc-bffb-3d7652c1f3a4`; the holdings UUID is `306963dc-bc48-55e6-9909-b2b40c345a0b`. This is materially stronger than a historical bibliography because it identifies a currently requestable physical set outside Kyrgyzstan.

## Identity evidence

The Columbia/Open Library record and the Osh State University bibliography independently identify the same edition:

- Title: *Саякбай Каралаев: Сейтек* / *Si︠a︡kabaĭ Karalaev: Seĭtek*
- Series: *Классикалык изилдөөлөр жана тексттер*
- Publisher/year: Полиграфбумресурсы, Бишкек, 2018
- ISBN-13: **978-9967-12-778-4**; ISBN-10: **9967-12-778-3**
- Compilers: A. Жайнакова, A. Акматалиев, Н. Нарынбаева
- OshSU call number: **82.3(2=Ки)кыр К 47**
- OshSU pagination: volume 1 **614 pages**, volume 2 **578 pages**
- OCLC: **1124979819**
- Library of Congress classification: **PL44.9.S45 K37 2018**
- Open Library edition identifier: **OL44252180M** (metadata imported from Columbia MARC)
- Google Books volume identifier: **z90kywEACAAJ**

OshSU's acquired bibliography remains at `sources/raw/oshsu-seytek-2018-holdings.pdf`, SHA-256 `3aa1e010ac2b9e0af44652ef64b977252d738f49e7befcf76d02ef288621b683`. Its extracted entries explicitly list both volumes and one copy of each in the IBO reading room and one in the philology reading room.

## Relationship to the available 2013 text and likely coverage

The existing public Turar scan (`sources/raw/seytek-2012.pdf`, SHA-256 `786eb36c1863f3e6c5330bb98d5d1656ab2e566bc53e16128a4f982928ebee2f`) is bibliographically a distinct edition: its title/copyright pages identify Turar, 2013, ISBN **978-9967-15-164-2**, compilers A. Жайнакова and A. Мамытов, and 1172 pages. It states that Karalaev's recorded *Seytek* comprises **84,697 lines**. The 2018 set totals 1192 cataloged pages and adds N. Narynbaeva as compiler.

The pagination supplies unusually strong circumstantial evidence that the 2018 publication is a two-volume repackaging of the 2013 text rather than a longer recension:

- 2018 volume 1 has 614 pages.
- In the 2013 scan, page 614 closes the passage containing Sarybay's ultimatum and demands for tribute and women.
- Page 615 begins a new section headed `СЕМЕТЕЙДИН САРЫБАЙГА АЛЫ ЖЕТПЕЙ, АРМАН КЫЛГАНЫ. САРЫБАЙ КҮРКҮРӨП, ЭЛДИ КЫРЫП ТУРГАН ЖЕРИ` (approximately, “Semetey's lament when he cannot overcome Sarybay; Sarybay roaring and slaughtering the people”). The 614/615 division is therefore a plausible editorial volume break.
- The balance of the 2013 book from pages 615 through 1172 is 558 pages. Adding 20 pages of new volume-title, series, copyright, contents, and other preliminary matter gives exactly the 578 pages cataloged for 2018 volume 2: `614 + 558 + 20 = 1192`.

This does **not** prove textual identity: the Columbia MARC has no contents note, volume-level pagination, or edition statement that links the text to 2013, and no scan of the 2018 title, contents, first/last textual pages, or volume boundary was found. It does, however, make substantial additional verse unlikely. At present there is no evidence that the 2018 set contains material beyond the 2013 edition or could fill any of the reported **104,427 missing Seytek lines**; the best-supported working hypothesis is that it contributes **zero new poetic lines**. That missing-line figure also exceeds the edition's own statement of 84,697 lines for Karalaev's recorded *Seytek*, so the project's source accounting should be rechecked before treating 104,427 as an edition-specific deficit. Corpus source-row counts are not directly interchangeable with printed verse-line counts because extraction may include headings, preliminaries, or differently segmented rows.

Confidence is high for the edition's bibliographic identity, Columbia holdings, and access status; moderate-to-high for the repackaging hypothesis; and low for any assertion of exact textual identity until representative pages of both 2018 volumes are inspected.

## Access and digitization mechanics

All four Valet request URLs redirect an unauthenticated visitor to `https://valet.cul.columbia.edu/sign_in`; they are not anonymous public digitization forms. Columbia's official Electronic Document Delivery policy at https://library.columbia.edu/bts/recap/edd.html says that direct requests require an active UNI and borrowing privileges, scanning is free for an article or book chapter up to **10% of a work**, and a requester must supply start and end pages. Delivered files are normally 300 dpi and remain in a secure download area for 14 days. If a scan cannot be completed, the physical volume is delivered for consultation. The general offsite-service page is https://library.columbia.edu/services/request/off-site.html.

For a researcher without a Columbia UNI, the strongest public route is a physical interlibrary-loan request made through the researcher's home library, citing **OCLC 1124979819**, call number **PL44.9.S45 K37 2018g**, and the volume-specific barcodes above. A Columbia-affiliated or otherwise eligible reader could request both physical volumes or targeted scans within the 10% limit. Columbia staff can mediate requests for patrons lacking a UNI, but no request or contact was submitted during this audit. ReCAP is a shared preservation facility used by Columbia, Princeton, NYPL, and Harvard; the discovered item record is Columbia-owned, and no independently cataloged partner copy was verified.

## Searches and rejections

- Internet Archive Advanced Search: exact ISBN/ISBN-10, Cyrillic and Latin title plus 2018, and Karalaev creator/title queries returned **0 records**.
- Open Library: bibliographic record `OL44252180M` exists, sourced from Columbia MARC, but has no digital scan or lending file: https://openlibrary.org/books/OL44252180M
- Google Books View API resolves the ISBN/OCLC to volume `z90kywEACAAJ`, with `preview: noview`, `embeddable: false`, and no PDF or EPUB download.
- HathiTrust discovery rejected the automated query with HTTP 403; this supplies no evidence of a holding or digital copy.
- Library of Congress digitized-books search returned no copy.
- Crossref bibliographic ISBN query returned **0 works**.
- Exact ISBN, ISBN-10, page-count, publisher, title, and filename-variant web searches found the OshSU bibliography and catalog metadata only, not book files.
- Public Telegram indexes and the `@Manaseposu` archive were searched. Messages 226–227 contain the known 2013 two-volume *Semetey* scans; no 2018 *Seytek* file was present in the indexed archive.
- WordPress upload/media-index queries for Cyrillic/Latin title, Karalaev, ISBN, and 2018 PDF variants returned no candidate.
- Kyrgyz National Electronic Library (`neb.kg`), KYRLIBNET/open archive (`kyrlibnet.kg`, `arch.kyrlibnet.kg`), and Kyrgyz library-domain exact-ISBN searches returned related Manas scholarship and older media, but no record or file for the target set.
- Current Kyrgyz Academy publication lists confirm the 2013 Turar 1172-page edition and the surrounding 2018 series, but expose no scan for ISBN 978-9967-12-778-4.

No candidate was downloaded because no newly discovered URL exposed a public book file. No institution was contacted and no scan, loan, or ILL request was submitted.
