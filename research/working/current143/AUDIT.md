# Current inventory 143 completion-first coverage audit

Source: `sources/raw/manuscript-full-91-146/143.pdf`  
SHA-256: `db22e2a5274260d0d1a06f22082ce535758ff594af9dc4843a57782d50547221`

## Completed physical pass

The 192-page PDF contains covers/catalogue material on pages 1–2 and 191–192. Every visible narrative or genuine textual-heading baseline on PDF pages 3–190 has been represented in `page-NNN.reviewed.jsonl`, translated into provisional English, and checked by the manuscript validator.

The direct pass found **6,859 scanned text rows / 39,664 English words**: 6,856 narrative rows and three genuine heading rows. This is a source-position count, before removing a duplicated scan leaf. One position, `pdf086:l035`, is explicitly unreadable because the photograph cuts through the bottom baseline; its English marker is an accounting notice, not a translation.

The earlier compact audit's boundary counts were wrong. PDF page 3 contains 33 narrative baselines, not 35; the next two printed-witness lines begin on manuscript page 4. PDF page 190 contains 36 narrative baselines, not 39, and ends with `Билгичтиги ушундай.` Direct leaf readings take precedence over the preliminary endpoint estimate.

## Scan-order anomaly and catalogue count

PDF page 22 visibly bears folio **2621** and is a line-for-line duplicate photograph of the leaf again present at PDF page 161. Expected folio **2482** is absent between pages 21 (folio 2481) and 23 (folio 2483). Both PDF source positions remain in the extraction, while page 22's 31 text rows are excluded from release as documented overlaps with page 161.

Removing that duplicate leaves **6,828 canonical physical text rows**, one more than the title leaf's `6827 строк` tally. The direct pass does not delete a visible row merely to force catalogue agreement. Folio 2482's episode content remains represented by the already translated printed `seytek-2012` witness, but the manuscript scan itself does not contain that leaf.

## Conservative printed-witness reconciliation

The manuscript episode runs from `Колтукташып басышып,` to `Билгичтиги ушундай.` and is substantially represented in the released `seytek-2012` edition. `build_release_inputs.py` accepts a printed overlap only when either:

- an individually recorded printed position has the same normalized source string and has not already been used; or
- the normalized string occurs exactly once in each complete witness.

Repeated formulas without a positional anchor remain in the manuscript release. This deliberately favors completion over aggressive deduplication.

| evidence class | rows | disposition |
|---|---:|---|
| scanned text positions | 6,859 | preserved in physical extraction |
| duplicate page-22 positions | 31 | excluded against identical page-161 rows |
| canonical physical text rows | 6,828 | one above catalogue tally |
| secure printed counterparts | 4,535 | already translated; excluded as overlaps |
| cut-off unreadable baseline | 1 | explicit unresolved-source gap |
| manuscript rows released | 2,292 | provisional direct English, 13,742 words |

The machine-readable decisions are in `release-overlap-map.json`; the full extraction is `sources/extracted/sayakbay-ms-current143.lines.jsonl`. The batch is `corpus/batches/pages-manuscript143-0003-0190.json`.

All English remains a completion-first draft without independent specialist review. Bracketed readings and line-specific uncertainty notes identify passages that need later philological improvement.
