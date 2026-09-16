# Sayakbay *Manas* source reconciliation

Prepared 2026-09-15. This audit reconciles the 78,616 released physical source rows against the manuscript catalogue and three incompatible published totals. It does not add inferred or duplicate lines to the corpus.

## Archival sequence

The public Manuscript Fund catalogue directly maps old inventories **911–924** to current **90–103**. Old 911–923 are wholly titled *Manas*. Old 924/current 103 is explicitly mixed, “Manas—The death of Manas; Semetey,” and cannot be assigned wholly to either part without a page-level boundary.

| Old | Current | Catalogue description | Pages | Lines |
|---:|---:|---|---:|---:|
| 911 | 90 | Manas's childhood | 294 | 5,082 |
| 912 | 91 | Manas's battles | 198 | 5,250 |
| 913 | 92 | Manas's youth | 152 | 4,256 |
| 914 | 93 | Manas's youth, continued | 153 | 4,000 |
| 915 | 94 | Manas's youth, continued | 191 | 5,900 |
| 916 | 95 | Manas's youth, continued | 167 | 5,244 |
| 917 | 96 | Manas's youth, continued | 176 | 5,808 |
| 918 | 97 | Manas's youth, continued | 157 | 4,024 |
| 919 | 98 | Great Campaign | 342 | 10,602 |
| 920 | 99 | Great Campaign | 358 | 11,000 |
| 921 | 100 | Great Campaign | 300 | 9,600 |
| 922 | 101 | Great Campaign | 311 | 9,641 |
| 923 | 102 | Great Campaign | 160 | 4,960 |
| 924 | 103 | Death of Manas; Semetey | 100 | 2,300 |

Old 911–923 total **2,959 catalogue pages and 85,367 lines**. Including the mixed boundary notebook gives 3,059 pages and 87,667 lines. The core-looking 911–923 sum exceeds 83,830 by 1,537, 84,513 by 854, and 84,830 by 537. These small but real excesses show that catalogue counts are not an edition-ready additive crosswalk: the edited text must exclude overlaps, duplicated performance matter, apparatus, or material assigned across a boundary.

Catalogue records and five-page samples are preserved in `research/manuscript-inventory.json`; the URLs have current inventory IDs 90–103 and old shelfmarks 911–924. The sequence is direct, not inferred.

## Three reported totals

The repository's 2010 edition yields 78,616 included physical text fragments (78,615 provisional grouped rows), plus 77 unresolved fragments and documented nonverse material. Its narrative ends at PDF page 1832; the glossary begins on 1833.

The resulting deficits are:

| Comparison total | Evidence | Difference from 78,616 |
|---:|---|---:|
| 83,830 | *Manas Encyclopedia*, vol. 2, p. 291, visibly printed in the Sayakbay entry | 5,214 |
| 84,513 | coherent four-part 500,553 allocation used by the project | 5,897 |
| 84,830 | national-corpus/KazNU allocation and later derivative claims | 6,214 |

The encyclopedia page was rendered and visually checked; **83,830 is not an OCR error**. It also says the first part was recorded by 1937 and attributes the transcription chiefly to Ibraiym Abdrakhmanov, with K. Zhumabaev, Zh. Risov, and K. Kydyrbaeva. Because all three totals circulate and no source provides an inventory-to-edition subtraction table, the defensible missing range is **5,214–6,214 physical rows**, not a single certified number.

The separate bilingual Internet Archive derivative visibly numbers its last narrative line 78,710 while claiming 84,830. It is based on the same Turar source family and supplies no missing Kyrgyz passage; its damaged-page location also uses an ellipsis. The 94-row difference between that printed endpoint and our 78,616 physical-fragment count is a lineation/apparatus discrepancy, not recovered text.

## Public source discoveries

### One complete manuscript scan

Current inventory 90 / old 911 has an unlinked full PDF at:

<https://manuscript.bizdin.kg/static/media/pdf/90Manas-Manastyn-bala-chagy.pdf>

It is **122,640,613 bytes, 302 PDF pages**, SHA-256 `abe0b9bd1dfdcac97d6c3b2a32f30f7efaafc12850dd283e4f71ffe98709c013`. Sampled interior pages show the expected handwritten Latin-script Kyrgyz manuscript and manuscript foliation (for example PDF 150 displays handwritten leaf 145). The catalogue says 294 pages; the eight-page PDF excess is consistent with covers/targets or scan furniture and requires a foliation audit. This is concrete recoverable primary material for the 5,082-line opening unit, but it is not itself the missing 5.2–6.2k tail: the 2010 edition already contains the opening narrative, so novelty requires line collation.

The discovery depends on an exceptional filename: unlike every other sample, current 90's `Obrazets-90Manas...pdf` becomes live when `Obrazets-` is removed. Testing the same transformation and `Full-`, `Original-`, `-full`, `-original`, authorless, and simplified variants across five likely directories found no full files for current 91–103. In total, 695 generated path variants were checked. Numeric `90.pdf`–`103.pdf` are a separate unrelated Arabic-script manuscript/book collection; cover and interior inspection rejects them as shelfmark collisions, just like the previously audited numeric 104–145 files.

All fourteen catalogue-linked `Obrazets` PDFs for current 90–103 were downloaded temporarily and verified as exactly five pages. Their hashes and byte sizes are in the companion JSON.

### Open 1984 and 1986 editions

AKIpress exposes both editions used by the national-corpus paper:

- Book I (1984): <https://cdn-1.aki.kg/st_bilimlib/3/ceb2b3937fd8a8a2741dbbe008a15fef2bb812bc.pdf>, 55,254,046 bytes, 248 pages, SHA-256 `8823051caa548206f6887d4f49e28003c97f8e38f52ccad2e8d4e1073bda6915`.
- Book II (1986): <https://cdn-1.aki.kg/st_bilimlib/4/2a0b0eaaeb2e39f9c326828b021d8367e16d9754.pdf>, 47,481,576 bytes, 265 pages, SHA-256 `29386691ae348541f1fed0f2b5bc0ed033eca8369448d7c6f70d9820a7444ff1`.

These scans are valuable comparison witnesses but are edited selections, not the complete archival transcription. Book I's editorial statement explicitly says literal repetitions and ideologically unsuitable material were omitted. A checked Book II endpoint passage is already present line-for-line in the 2010 extracted text. No defensible passage omitted from the 2010 edition was established from these books during this bounded audit.

## What the deficit means

The catalogue does not support padding 78,616 to any reported total. Its 85,367-line core sum is above every published target, while the mixed old 924 adds another 2,300 unpartitioned lines. The likely 5.2–6.2k deficit is editorially omitted, overlapping, differently divided, or boundary-shifted material distributed across the archival sequence. It cannot be localized to one notebook from line arithmetic alone.

The next concrete source step is full-scan acquisition or collation for current 91–103, followed by a diplomatic transcription and sequence alignment against the 2010 edition. Current 90 can be processed immediately as the first complete primary unit. Requests for institutional scans should cite both old 911–924 and current 90–103, and ask for the editorial subtraction/crosswalk behind each of 83,830, 84,513, and 84,830. No institution was contacted in this audit.
