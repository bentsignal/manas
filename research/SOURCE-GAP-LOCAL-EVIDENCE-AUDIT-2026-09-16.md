# Local evidence audit for the seven release source gaps

Checked 16 September 2026 against the locally recovered printed PDFs, extracted corpora, comparison witnesses, benchmark source material, and manuscript holdings. **No source-gap record can be removed from the evidence currently on disk.** The release still has one genuinely unresolved source region comprising three extraction fragments, plus six content-withheld regions comprising forty-eight readable source positions.

## Damaged Manas page 48 region

The only unresolved-source region is `manas-2010:p0048:damaged-region`, between `manas-2010:p0048:b002:l001` (`Каяшаяк бергенди`) and `manas-2010:p0048:b002:l005` (`Кайра тартып тим койбой,`). Its three extraction fragments are:

- `manas-2010:p0048:b002:l002`: `Т/*`
- `manas-2010:p0048:b002:l003`: `о`
- `manas-2010:p0048:b002:l004`: `и`

All three occupy one baseline at the same vertical position. The source PDF's decoded content stream contains no hidden or clipped wording beyond those visible fragments. The byte-identical Internet Archive copy cannot add evidence; the Turkish-English derivative prints an ellipsis at the same place; the Speak.tatar transcription repeats the corruption; and the Meikin text silently skips it. The shorter local Karalaev first-volume witness has no aligned occurrence of this expanded passage.

The human-reference benchmark initially appears promising because `research/benchmarks/2026-09-15-human-reference/passage-1.txt` contains the same preceding formula. It is not a restoration witness. That passage is the earlier sequence at `manas-2010:p0017:b002:l026` and continues `Койбой кырып таштады. / Алымын артык жороду,`; the damaged page-48 occurrence instead continues `Кайра тартып тим койбой, / Кырып салган кези экен,`. Elmira Köçümkulkızı's 1995-based English likewise represents the earlier sequence, and the benchmark protocol explicitly says its edition identity is unverified. Substituting its next line at page 48 would conflate two distinct occurrences.

A sequence search across every local extracted printed corpus found no second occurrence of `Каяшаяк бергенди` followed within the next seven source positions by `Кайра тартып тим койбой`; the only hit is the damaged page-48 sequence itself. The recovered manuscript PDFs concern later continuation material and have no established page-48 alignment. Handwriting or formula similarity alone cannot establish the missing letters, words, or number of original verses.

Accordingly, the three fragments must remain one unresolved damaged-source marker. Resolving it requires an independently readable copy of the corresponding Turar 2010 printed spread or a securely aligned manuscript/edition witness. No English verse or word can defensibly be credited from current local evidence.

## Six content-withheld regions

The other six records are not unreadable-source regions. Their forty-eight positions are preserved with source IDs, PDF digest, bounding boxes, normalization method, and raw-text digests in these batch files:

- `semetey-1-2013:p1012:b004:l026-l032:content-withheld` — 7 positions
- `semetey-1-2013:p1021:content-withheld` — 10 positions
- `semetey-1-2013:p1024:content-withheld` — 11 positions
- `semetey-1-2013:p1025:content-withheld` — 15 positions
- `semetey-1-2013:p1029:content-withheld` — 1 position
- `semetey-1-2013:p1044:content-withheld` — 4 positions

The local `semetey-1-2013.pdf` supplies the source positions, so further source recovery would not change their status. Their English is deliberately withheld under the existing content classification recorded in `corpus/source-gaps.json`. This audit does not alter that classification or count those positions as translated.

## Result

No corpus, gap-registry, line-count, or English-word-count change is supported. The exact remaining ledger is **1 unresolved region / 3 damaged fragments** and **6 withheld regions / 48 readable fragments**.
