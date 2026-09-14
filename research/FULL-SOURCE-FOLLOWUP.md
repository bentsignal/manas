# Full-source follow-up

Checked 14 September 2026 UTC. This is a bounded follow-up to SOURCE-AUDIT.md, not a certification of the complete corpus. No correspondence was sent.

## Result

The source bottleneck remains unresolved. No newly acquired full epic witness adds to the four existing PDFs. Three files were acquired and hashed: an identical Manas mirror, a five-page original-manuscript sample, and an official university holdings list. Their records are in `research/source-candidates.json`; the shared source manifest and releases were not changed.

The reported 500,553 archival verse count cannot be reconciled by treating extracted display lines as verses. The existing 401,930 display lines include apparatus, prose and encoding/ordering problems. The two incompatible component counts remain unresolved. The academic Manas search index independently reproduces the common four-part figures, but direct acquisition of that edition failed; this is indexed bibliographic evidence, not a locally verified full witness.

## Continuations: actual boundaries in the acquired Seytek

Source: `sources/raw/seytek-2012.pdf`, SHA-256 `786eb36c1863f3e6c5330bb98d5d1656ab2e566bc53e16128a4f982928ebee2f` ([catalogue](https://new.bizdin.kg/kniga/seytek-baatyrdyk-epos-sayakbay-karalaevdin-varianty-boyuncha)).

PDF pages 1165 and 1166 were rendered and visually inspected. Page 1165 ends the verse with Akjoltoy interpreting the dream, blessing Kenen and receiving gifts. Page 1166 begins the glossary. The extracted table of contents at 1171 lists the last narrative episode as Chongbilgich's raid; 1172 is the colophon. There is no later appended continuation after the final Kenen birth/dream material.

**Correction to the earlier search note:** the twins' names do occur outside the preface, in prose on PDF page 555. This page was also rendered and visually inspected. The prose gives Seytek → Oruzkan → Kenen → Alymsaryk/Kulansaryk and says Karalaev could narrate through their flight and settlement, but no further. This is a short prose account embedded before the Sarybay narrative resumes; it is not the 15,186-line continuation. Its genealogy differs from the direct Seytek → Kenen relationship reported elsewhere and must remain an apparatus issue, not be silently harmonized.

Searches of normalized Seytek found Alymsaryk and Kulansaryk only on pages 4 and 555; Kertulpar on 1162; no Kermekash or Chyngtemir. Name search alone is not proof of absence: inflection, spelling, extraction and ordinary adjectives matter. The page boundary and prose/verse distinction provide stronger evidence. The later Kenen exploits and twins' flight have not been located as full verse in the acquired files.

**Additional extraction failure:** on page 555, JSONL emits the right verse column before the left after the prose passage. Visual inspection establishes the opposite physical column order. Existing block order must not be used blindly for bulk Seytek translation. Scratch comparison images are `tmp/pdfs/seytek-prose-0555.png`, `seytek-ending-1165.png`, and `seytek-ending-1166.png`.

## Exact manuscript lead

The signed A. Zhainakova [Kenen encyclopedia entry](https://tamgasoft.kg/dict/index.php?lang=en&lfrom=kg&word=%D0%BA%D0%B5%D0%BD%D0%B5%D0%BD) cites manuscript-fund inventory 960, page 145, for the pregnancy narrative and inventory 960 for the subsequent Kenen/twins material. The entry's later plot includes Kenen's adult life, the twins, conflict with Chyngtemir, Kenen's death and escape. These are useful identification markers for an archive request, not substitute translation text.

The existing 88-record inventory has no exact old-inventory-960 entry. Public catalogue searches through its actual search form (`/поиск/?keyword=...`) for Сейтек, Кенен, 960 and Алымсарык returned no manuscript-record links in this session. General indexed searches likewise did not identify the item. This does not prove the archive lacks it or that its current number is 960.

The public sample for **current inventory 103 / old 924** was downloaded from the linked catalogue asset. Its PDF has **5 pages**, while the catalogue describes **100 manuscript pages / 2,300 lines**. This concretely confirms that an `Obrazets` asset must not be counted as a complete notebook. Some catalogue records also contain narrator/metadata contradictions; attribution needs record-level review.

## Academic editions and physical holdings

The [Academy's bibliography](https://kruia.gov.kg/news/show/manas-eposu-boyuncha-chykkan-kitepterdin-tizmesi/ky) lists Semetey books 1–6 (2015/2017; 556, 496, 612, 540, 608, 576 pages), Seytek volumes 1–2 (2018; 614 and 578 pages), and a 2019 Karalaev Manas edition (Dilazyk, 1024 pages). These are comparison candidates; pagination cannot establish additional verse coverage. Its duplicated 2013 Semetey entries include an apparent book-3 reference inconsistent with the surrounding two-volume records, so a third volume must not be inferred without title-page evidence.

An [Osh State University official holdings list](https://base.oshsu.kg/resurs/document/PDF-20190719123821-kitep_osu.pdf) was acquired (29 pages). It identifies both 2018 Seytek volumes under call number **82.3(2=Ки)кыр К 47**, series *Классикалык изилдөөлөр жана тексттер*, compilers A. Zhainakova, A. Akmataliev, N. Narynbaeva, publisher Poligrafbumresursy, ISBN **978-9967-12-778-4**. It lists one copy each in the IBO and philology-faculty reading rooms. This is historical holdings evidence, not a current lending confirmation.

## Practical public leads checked

- Issyk-Kul university PDF `https://api.libraryiksu.kg/elibrary/books/Karalaev_Manas1454.pdf`: acquired, 16,242,844 bytes; SHA matches `manas-2010.pdf` exactly. No new coverage.
- Jalal-Abad academic Manas book 1: [public PDF lead](https://jasulib.org.kg/wp-content/uploads/2022/07/8.-%D0%9C%D0%B0%D0%BD%D0%B0%D1%81-1-%D0%BA%D0%B8%D1%82%D0%B5%D0%BF-%D0%A1%D0%B0%D1%8F%D0%BA%D0%B1%D0%B0%D0%B9-%D0%9A%D0%B0%D1%80%D0%B0%D0%BB%D0%B0%D0%B5%D0%B2.pdf). Python fetch remained unfinished after more than two minutes and was stopped; web fetch also timed out. No retry file acquired. Existing zero-byte `manas-academic-1.pdf` is not evidence of acquisition.
- Indexed searches for Karalaev/Kenen PDF, inventory 960, Semetey sixth book and Karalaev Seytek 2018 found descriptions, existing editions and holdings, but no new full downloadable continuation or academic series.
- Manuscript catalogue form and linked sample checked as above. No authentication, payment or private endpoints used.

These specific routes are exhausted for this pass. This is not an exhaustive search of every library, and retrying the academic PDF later remains reasonable. The most productive next step is an institution-assisted crosswalk and scans, not padding the digital source or adding another narrator.

## Concrete unsent request

Route: [official Academy Institute page](https://kruia.gov.kg/content_list/show/363/ky), which lists the Ch. Aitmatov Literature Institute, manuscript-fund head **Isaeva A.**, Manas/folklore department head **Kolbaeva M. K.**, scientific secretary **Toichubek kyzy Zhazgul**. Public institute contact: **melis.a.-50@mail.ru**, **+996 (312) 39 20 23**; address **265a Chui Avenue, Bishkek**. Confirm delivery routing before sending. The request below has not been sent.

> Subject: Sayakbay Karalaev manuscript inventory 960 and complete-corpus source reconciliation
>
> Dear Manuscript Fund and Manas Studies colleagues,
>
> We are preparing a source-traceable English translation of Sayakbay Karalaev's recorded Manas corpus. Could you identify the current shelfmark corresponding to old inventory 960 (A. Zhainakova's Kenen entry cites page 145), and provide a catalogue description and information on obtaining complete scans of its Kenen, Alymsaryk and Kulansaryk material?
>
> We also need the inventory-to-edition crosswalk for the reported 500,553 verses, including old Semetey inventories 925–953. Published sources give conflicting component counts: 84,513 / 316,157 / 84,697 / 15,186 versus 84,830 / 397,775 / 17,948. Which count reflects the archival corpus, and does it include alternative recordings or copies?
>
> Which editions preserve all recorded lines? In particular, how do Semetey books 1–6 (2015/2017) and Seytek volumes 1–2 (2018, ISBN 978-9967-12-778-4) relate to the Turar 2013 editions, and where are the continuations printed? Please advise access/scan conditions and the appropriate basis for publishing an English translation with source references. We would also appreciate information about any complete English translation or current project known to the Institute.
>
> Thank you.

No new material should enter the released source corpus until its narrator, notebook/edition boundaries, overlap, lineation and publication basis are documented.
