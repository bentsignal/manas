# Current inventory 143 completion-first coverage audit

Source: `sources/raw/manuscript-full-91-146/143.pdf`
SHA-256: `db22e2a5274260d0d1a06f22082ce535758ff594af9dc4843a57782d50547221`

## Physical extent and count

The full scan has 192 PDF pages. PDF page 1 is the outside front cover, page 2 is the title/catalogue leaf, PDF pages 3–190 are 188 photographed narrative-leaf positions, page 191 is the reverse/closing leaf, and page 192 is the outside back cover.

The scan is not a completely consecutive run of distinct leaves. PDF page 22 visibly bears folio number **2621** and is a duplicate photograph of the leaf also present at PDF page 161. Expected folio **2482** is absent between PDF pages 21 (folio 2481) and 23 (folio 2483). The diplomatic pass preserves both scanned source positions and will exclude one copy as a documented duplicate during release compilation; the absent folio requires an explicit source-gap record. This corrects the earlier compact audit's assumption that every page from 3 through 190 mapped mechanically to folios 2463 through 2650.

The physical narrative count is **6,827 lines**. This is stated on the title leaf (`6827 строк`) and is supported by the manuscript's own per-leaf line tallies: for example, PDF page 3 is marked 35 and contains 35 narrative baselines; PDF page 190 is marked 39 and contains 39 narrative baselines. The average implied density is 36.31 lines across 188 narrative leaves, consistent with the scan. This audit treats 6,827 as the physical/copyist count; it does not force that total onto the edited witness's different lineation.

## Existing release representation

The manuscript is already represented in the release through the printed `seytek-2012` witness.

- Manuscript opening: `Колтукташып басышып,`
- Release opening: ordinal **372,941**, `seytek-2012:p1005:b002:l007`, same text, English `Walking arm in arm,`
- Manuscript closing: `Билгичтиги ушундай.`
- Release closing: ordinal **379,743**, `seytek-2012:p1090:b003:l007`, same text, English `Such is the knowledge.`
- Inclusive released interval: **6,803 lines**
- Existing English in that interval: **36,782 whitespace-delimited words** (36,740 regex word tokens)

The boundary alignment is stronger than isolated phrase matching. The first manuscript leaf has 35 lines and corresponds in order to the 35 released lines beginning at ordinal 372,941. The last manuscript leaf has 39 lines and corresponds in order to the final 39 released lines, ordinals 379,705–379,743.

## Conservative completion decision

No unique untranslated segment is securely demonstrated by the present evidence. The 24-line difference between the physical/copyist total (6,827) and the edited released interval (6,803) may reflect manuscript-versus-edition lineation, omitted repetitions, or editorial compression. It is not safe to interpret it as 24 novel lines without a complete leaf-by-leaf transcription and collation.

For completion-first release accounting, current inventory 143 should therefore be classified as **represented by an existing translated printed witness; zero conservatively addable lines identified in this audit**. A later diplomatic collation may recover unique variants or omitted lines, but adding the manuscript wholesale now would duplicate a continuous released episode.

## Completion-evidence collation result

The compact machine-readable crosswalk is `monotonic-crosswalk.json`. The fullest defensible mapping from the evidence now available is:

| evidence class | lines | disposition |
|---|---:|---|
| secure released episode mapping | 6,803 | already translated in `seytek-2012`, ordinals 372,941–379,743 |
| unresolved physical-count surplus | 24 | not assignable to absent text without diplomatic interior transcription |
| secure unique untranslated lines | 0 | none demonstrated |

“Secure released episode mapping” is an episode-level coverage result, not a claim that all 6,803 manuscript lines have been diplomatically transcribed one by one. Exact sequential checks cover the 35-line opening leaf and 39-line closing leaf. Together with the exact terminal anchors and uninterrupted printed episode, they establish the monotonic outer crosswalk. The interior 24-count discrepancy remains explicitly unresolved rather than being converted into speculative additions.
