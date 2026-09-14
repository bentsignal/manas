# Manas: source and translation audit

Research started 13 September 2026 (America/New_York); downloads dated 14 September UTC.

## Finding

No published English translation of the entire 500,553-line Sayakbay Karalaev corpus was identified in the bibliographic searches performed. This is NOT proof that nobody has ever made one. Unpublished translations, ongoing projects and poorly indexed editions remain unverified. No scholar or institution has yet been contacted.

Do not advertise this as the first complete English translation until the claim has been checked with specialists and publication is actually complete.

## Exact target

The commonly cited breakdown is:

| Part | Reported lines |
|---|---:|
| Manas | 84,513 |
| Semetey | 316,157 |
| Seytek | 84,697 |
| Kenen, Alymsaryk, Kulansaryk | 15,186 |
| Total | 500,553 |

The main three parts total 485,367. The continuations cannot be omitted. These are reported archival counts, not counts established from our digital files. Do not pad, deduplicate recurring verses, combine narrators, count front matter, or silently alter the target to make the figures match.

Sources: [Manas encyclopedia, volume 1](https://new.bizdin.kg/media/books/manas-ensclpd.pdf), [encyclopedia mirror at Manas Discovery](https://manas-discovery.kg/wp-content/uploads/2023/04/Манас-энциклопедиясы_1-том.pdf), [Osh State University research article, 2023](https://journal.oshsu.kg/index.php/vestnik/article/download/655/430).

## Existing English translations

- **Walter May (1995)**: two English volumes identified as the Sagymbai Orozbakov version in the National Academy's bibliography. This is not evidence of a complete Karalaev translation. The precise extent must be checked in the books, not inferred from their title.
- **Arthur T. Hatto**: The Memorial Feast for Kökötöy-Khan (1977) and The Manas of Wilhelm Radloff (1990), representing other recorded texts.
- **Daniel Prior**: The Semetey of Kenje Kara (2006), a distinct performance; The Memorial Feast for Kökötöy Khan (Penguin, 2022), an episode of Orozbakov's telling.
- **Elmira Köçümkulkïzï**: her own introduction says she translated the first eight episodes from Karalaev's academic edition, sometimes combining lines and omitting repetitions. Relevant comparison material, but not a complete translation.
- **Akylay Baimatova (2018), Tales of Manas**: English work based on a Russian edition, identified by Columbia. Full textual scope still requires primary-edition inspection; a reader's claim of completeness is not sufficient.
- **Aikol Manas**: Aigine's English publication describes itself as a translation of the first volume of a different telling. Not our target corpus.

Sources: [National Academy bibliography, 16 February 2026](https://kruia.gov.kg/news/show/manas-eposu-boyuncha-chykkan-kitepterdin-tizmesi/ky), [WorldCat: May](https://search.worldcat.org/pt/title/1412761282), [Columbia World Epics](https://edblogs.columbia.edu/worldepics/project/manas/), [Köçümkulkïzï's introduction](https://www.silkroadfoundation.org/folklore/manas/manasintro.html), [Penguin: Prior](https://www.penguin.com.au/books/the-memorial-feast-for-kkty-khan-9780141998831), [Aigine](https://aigine.kg/images/Aikol_Manas.PDF).

Searches included English, Russian and Kyrgyz terms for complete translation, Karalaev, English, Manas, Semetey, Seytek, and the exact reported count. Search results were treated as leads; catalogue entries and publisher/translator statements were preferred for conclusions. This is an initial bibliographic audit, not an exhaustive worldwide catalogue search.

## Acquired candidate source files

Downloaded through current links on the Bizdin catalogue pages. The old indexed `/media/books/` URLs returned 404; the live pages now provide time-limited object-storage download URLs. `scripts/acquire.py` resolves the current links without storing access signatures. Downloaded PDFs and extracted full text stay local and are excluded from Git and the website.

| Source | PDF pages | Extracted text lines | Verified verse lines |
|---|---:|---:|---:|
| Manas, Turar 2010 | 1,846 | 79,974 | 0 |
| Semetey, book 1, Turar 2013 | 1,432 | 114,247 | 0 |
| Semetey, book 2, Turar 2013 | 1,424 | 114,555 | 0 |
| Seytek, Turar 2012/2013 | 1,172 | 93,154 | 0 |
| Total | 5,874 | 401,930 | 0 |

Text lines include titles, prose, notes, page labels, and glossary entries; they are NOT verse counts. Extraction defects can split or merge source lines. No coverage percentage can be certified from these figures.

Catalogue pages:
- [Manas 2010](https://new.bizdin.kg/kniga/epos-manas-sayakbay-karalaev-polnyy-variant)
- [Semetey book 1](https://new.bizdin.kg/kniga/semetey-baatyrdyk-epos-1-kitep-sayakbay-karalaevdin-varianty-boyuncha)
- [Semetey book 2](https://new.bizdin.kg/kniga/semetey-baatyrdyk-epos-2-kitep-sayakbay-karalaevdin-varianty-boyuncha)
- [Seytek](https://new.bizdin.kg/kniga/seytek-baatyrdyk-epos-sayakbay-karalaevdin-varianty-boyuncha)

The independently located Manas copy embedded in [Batken State University's library page](https://sites.google.com/view/batsulibraru/көркөм-адабият) has the same SHA-256 as the Bizdin copy: `53bb71b63a0ad255e815b57f23fb41c8f3160cf05fd7b374add3516c7ccd99d7`. This corroborates file identity, not completeness.

## Textual problems found

1. **Manas 2010 is reflowed.** The file has 1,846 PDF pages, while its bibliographic page says 1,006 printed pages and the Academy catalogue lists 1,008. It includes obvious transcription defects, including inconsistent Kyrgyz letters and missing initial characters. PDF page numbers cannot be treated as original printed page numbers.
2. **Semetey and Seytek use legacy font encoding.** Direct extraction produces Latin-looking characters. A deterministic candidate mapping recovers Cyrillic, including special Kyrgyz letters. It has been spot-checked against a rendered Semetey page, not verified across the whole corpus. The original extracted characters are retained alongside every normalized line.
3. **Two-column verse must be read down each column.** `pdftotext -layout` puts two verses on the same visual row. The structured extraction retains blocks and bounding boxes to support correct reading-order review; current block order is provisional, not a certified verse sequence.
4. **Publication history matters.** Semetey book 1, page 10, explicitly describes cuts to earlier editions and discusses an academic publication. Its preface cannot be replaced with a catalogue's broad statement that all events are present.
5. **Conflicting reported counts exist.** The Manas 2010 afterword reports 84,830 / 397,775 / 17,948 for the three parts, also summing to 500,553 but very different from the common breakdown. The source and meaning of that alternative must be resolved rather than silently selecting convenient numbers.
6. **Seytek dates disagree internally.** Title page: 2012. Bibliographic/copyright page: 2013. Preserve both rather than inventing a single certain date.
7. **Continuations remain unlocated as a verified full text.** Mentions of Kenen in a preface or the last chapter do not prove inclusion of all 15,186 continuation lines.

## Next source leads

The Academy's 2026 list identifies a six-book Semetey academic series (2015/2017; 556, 496, 612, 540, 608, 576 pages), and a two-volume Seytek edition (2018; 614 and 578 pages). These are candidates to inspect, not automatically missing portions to concatenate with the acquired editions.

[University library accession list](https://jasulib.org.kg/wp-content/uploads/2023/12/за-Ноябрь-2023.pdf) identifies physical holdings of the academic Semetey books. [Bizdin manuscript catalogue](https://manuscript.bizdin.kg/поиск-по-тегу/?tag=Саякбай+Каралаев) lists original notebooks and inventory numbers. The encyclopedia associates Semetey with old inventory 925–953. Crosswalk old/current inventory numbers before requesting or reconciling scans. We retrieved 88 linked catalogue records into `research/manuscript-inventory.json`; many assets are explicitly named Obrazets (sample), and must not be mistaken for complete notebook scans. For example, current inventory 103 maps to old 924 and reports 100 pages / 2,300 lines.

Necessary scholarly questions: which exact notebooks underlie the 500,553 count; whether it counts alternate takes or copied passages; which printed edition preserves every line; where the continuation manuscripts are; whether a complete English translation or active project exists; and the appropriate basis for translating and republishing source text.

## Translation and release rules

Translate from verified Kyrgyz, using explanatory Russian material only as a secondary aid. Preserve repetition, formulas, names, numbers, relationships, tone and ambiguity. Do not replace poetry with a synopsis. Record source ID, page, region, transcription changes, translation status and review evidence.

A representative pilot precedes bulk translation. Measure token use and review corrections on that pilot. Keep a glossary and contextual summaries, cache stable instructions, checkpoint every batch, and regenerate only passages that require changes. Machine output remains a draft until reviewed; agreement between models is not independent proof of accuracy.

Completion requires source reconciliation, every target line accounted for, all continuations, a documented publication basis and reviewed English for every line. Merely producing 500,553 numbered rows does not qualify.

## Current status

Four PDFs acquired; structured extraction complete. Opening pilot: 92 draft English rows cover every verse display line on PDF pages 16–17, with one provisional wrapped-line join. Digital-witness transcription visually checked; archival lineation and full-corpus completeness remain unverified. See [opening pilot notes](OPENING-PILOT.md). No paid bulk translation run has started. No expert review or institutional correspondence has occurred. Source completeness remains unresolved. A traditional-folklore publication basis is documented for the opening pilot only; rights in modern editorial material and the full edition remain unverified.

## Continuing draft — 14 September 2026

380 English draft rows now cover PDF pages 16–23. Pages 18–23 were visually compared with the digital witness. Their 288 display lines are preserved in order, with difficult readings flagged in record notes. All remain unreviewed drafts. Traditional-verse publication basis is extended to these checked pages; modern editorial material remains excluded.

A newly located encyclopedia entry for Kenen cites manuscript inventory 960, page 145, for his birth narrative and inventory 960 more generally for subsequent events: https://tamgasoft.kg/dict/index.php?lang=en&lfrom=kg&word=%D0%BA%D0%B5%D0%BD%D0%B5%D0%BD . This is a concrete archive lead, not an acquired continuation. No exact old-inventory-960 match occurs in our existing 88-record catalogue inventory.

956 draft rows now cover pages 16–35. Full source-display-line alignment passes for this prefix. Later batches are being translated in parallel; a probable corrupted verse on page48 is explicitly unresolved and blocks publication past that point until recovered. Source follow-up: [FULL-SOURCE-FOLLOWUP.md](FULL-SOURCE-FOLLOWUP.md).

## Checkpoint: PDF page 47

1,531 draft rows now released, representing 1,532 source display lines and one explicitly excluded running heading. Workers finished drafts through page75 (2,865 total draft verse rows including unpublished work). Publication stops before the damaged source region on page48. No full-source reconciliation or specialist review claimed. Page16 line11 now uses the documented пирге emendation in TEXTUAL-CORRECTIONS.md while preserving base raw text.

## Current draft inventory and priority lead

5,218 draft rows saved: sourcepages16–118 and159–164; workers assigned119–158. Of these,1,531 remain live through47. All are unreviewed AI drafts; lineation provisional. Saved-page coverage and published-prefix audits pass. An actual existing Turkish–English Karalaev project has been identified on Internet Archive; source worker inspected an English PDF and found derivative source files, a page48 ellipsis, and count conflicts. No first-complete-translation claim is justified. See SOURCE-PRIORITY-UPDATE.md for inspected files, exact hashes and the limits of the recorded publication date.

## Draft checkpoint: 10,421 rows

Saved page ranges16–227 and248–253; activeworkerassignments228–247,254–273,274–293. All saved batch display lines accounted for by scripts/audit-drafts.py; headings separately preserved and the three damagedpage48fragments explicitly unresolved. Releasedprefix remains1,531rows through47. No certifiedversecount or independentreview claimed. See corpus/draft-progress.json for generated counts.

## Publishing drafts past explicit source gaps

Following the request to publish as translation proceeds, the reader now inserts plain editorial markers at source gaps, stored separately in corpus/source-gaps.json. Markers carry no translated-line ordinal and do not contribute English-word totals. The damaged page48region and uninterpreted whole utterance183:l001 prevent completeness certification. The latter was removed from English counts: transliteration is not translation. Current releasecandidate10,132draftrows /56,721Englishwords through227. No omitted gaps are permitted by the rangeaudit; no expert-review claim.
