# Completion priority after component-count reconciliation

Prepared 15 September 2026 and corrected after manuscript-level checks. This note sets acquisition priority; it does not claim that the 500,553-line source is complete.

## Secure total, unresolved part boundaries

The institutionally repeated target remains **500,553 lines**. Tashpolot Sadykov and Bakyt Sharshembaev, “«Манас» эпосунун улуттук корпусун түзүү жөнүндө,” prints this Sayakbay row on PDF page 155:

| Part | Reported lines |
| --- | ---: |
| Manas | 84,830 |
| Semetey | 218,787 |
| Seytek | 196,936 |
| **Total** | **500,553** |

Source: <https://www.kaznu.kz/content/files/news/folder23214/%D0%91%D0%BE%D0%BB%D0%B0%D1%82%D0%B1%D0%B5%D0%BA%20%D0%9C..pdf>, PDF page 155; web-extracted lines 8446–8451.

This table must **not** be treated as a literal acquisition allocation. The next page says the corpus project loaded the previously published Sayakbay editions: *Manas* books I–II (1984/1986), *Semetey* books I–II (1987/1989), and *Seytek* (1991). It does not explain its part boundaries or assign its counts to archival inventories.

The widely repeated four-part archival breakdown is incompatible:

| Part | Reported lines |
| --- | ---: |
| Manas | 84,513 |
| Semetey | 316,157 |
| Seytek | 84,697 |
| Kenen, Alymsaryk, Kulansaryk | 15,186 |
| **Total** | **500,553** |

The Manas Encyclopedia assigns *Semetey* old inventories 925–953 and calls them 316,157 lines. The live catalogue makes that count physically implausible and instead points near 216,157. The acquired 2013 *Seytek* edition expressly states that Sayakbay's recorded *Seytek* is 84,697 lines. These facts make it unsafe to call the project's entire deficit “missing Seytek” or “missing Semetey.”

## Why the earlier Seytek allocation was rejected

The public manuscript catalogue supplies line counts for old *Semetey* inventories 927–953 totaling **198,100** lines. Old 925/current 104 and old 926/current 105 have 203 and 400 pages but no online line counts. Those two units cannot plausibly supply the **118,057** lines needed to reach 316,157; they could plausibly supply the **18,057** needed to reach 216,157. The 2013 edition's 216,333 extracted source rows independently sit near that corrected scale. No public evidence currently supports a 100,000-line *Semetey* deficit.

For *Seytek*, the terminal pair old 966/current 145 (**6,186 lines**) and old 967/current 146 (**9,000 lines**) sums exactly to the independently reported **15,186-line continuation**. Removing old 966 from the core leaves 70,382 known lines in old 954–965; the three blank counts in old 961–963 need a plausible 14,315 lines to reach the 84,697-line core target. The catalogue therefore supports the normal 84,697 + 15,186 boundary far better than the 196,936 classification.

These checks show that the 218,787 / 196,936 table uses different boundaries, includes additional material, or contains a classification/counting error. Its former arithmetic agreement with the project's pre-first-pass 113,095-row deficit was not evidence that the missing text was all *Seytek*.

## Current measurable coverage

| Released section | Source rows |
| --- | ---: |
| Manas | 78,689 |
| Semetey | 217,234 |
| Seytek | 89,355 |
| Kenen, Alymsaryk, Kulansaryk witness | 3,154 |
| **Total** | **388,432** |

The site is therefore **112,121 rows short of the 500,553 target**, but source rows from modern editions are not automatically identical to archival verse-line counts. The total deficit is operationally useful; its division among parts is not yet certified. All 925 formerly semantic-unresolved regions now have completion-first English, adding 974 released rows. Seven source-gap regions remain explicit rather than being counted as translations: one damaged region with three fragments and six policy-withheld regions with 48 fragments.

## Completion-first acquisition order

1. Obtain complete scans or transcriptions of old 966–967/current 145–146. Their catalogue total is 15,186 lines; the released 3,154-row printing explicitly cut repetitions and weaker lines and ends in prose. Old 966 begins 1,409 released *Seytek* rows before the edition endpoint, so the provisional overlap-corrected continuation target is 13,777 positions and the provisional missing remainder is 10,623. These are planning estimates until the full manuscripts establish their own lineation; see `SAYAKBAY-OLD966-OVERLAP-AUDIT-2026-09-15.md`.
2. Obtain the archive's notebook-to-line crosswalk and counting protocol for the aggregate 500,553 claim, including alternate takes, copies, repeated performances, prose, and section boundaries. The public component arithmetic currently leaves an unexplained 100,000-line contradiction.
3. Verify the blank counts for old *Semetey* 925–926 and compare full old 925–953 scans against the 2013 edition. Treat approximately 216,000 lines as the evidenced scale unless manuscript comparison proves omissions.
4. Reconcile the smaller *Manas* difference and any edition-versus-archive lineation differences.
5. Treat the six-volume 2015/2017 *Semetey* and two-volume 2018 *Seytek* editions as candidate witnesses until page/line comparison proves whether either adds source text.

Translation-quality issues remain registered in batch notes and the completion-first audit. The 925 semantically unresolved regions have received a first pass; its 38 high-severity findings were corrected immediately and 211 medium-severity rows remain queued for the later accuracy pass. Explicit withheld and irrecoverably damaged regions remain registered separately in `corpus/source-gaps.json`.
