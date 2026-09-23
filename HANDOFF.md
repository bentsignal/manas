# Project handoff

Last updated: 2026-09-23.

This repository publishes a completion-first English draft of the Sayakbay
Karalaev Manas trilogy as one virtualized, continuously scrollable page. The
public site is:

<https://manas-every-line.bentsignal.chatgpt.site>

The last verified public release is version `1dcaee9eb5050035`:

- 408,269 translated lines
- 2,163,346 English words
- 9 explicit unresolved source regions
- last released source row `sayakbay-ms-current146:pdf251:l012`

The deployment was verified with:

```bash
python scripts/verify-live.py https://manas-every-line.bentsignal.chatgpt.site
```

## Local correction checkpoint, not deployed

On 2026-09-23, 19 mistranslated English rows on printed Seytek page 972
were corrected in the page batch and canonical release. The local compiled
release now has **408,269 rows and 2,163,378 English words** (+32 words);
the verified live version above still has 2,163,346 words. The corrections
are recorded in `research/SEYTEK-0972-TRANSLATION-CORRECTIONS-2026-09-23.json`.
Alignment, draft audit, release compilation, tests, and production build passed.
No inventory-142 row was released, and the complete flag remains false.

Local Cyrillic handwriting OCR trials for inventory 142 are recorded in
`research/working/current142/OCR-BENCHMARK-2026-09-23.md`. Both the
line-level TrOCR model and region-level Rukopys model were too inaccurate in
Kyrgyz to count as source transcription.

GitHub is `https://github.com/bentsignal/manas.git`, branch `main`. Local
`.grok/` data is scratch material and must not be committed.

## Durable completed checkpoint

Current inventory 143 has a complete first visual pass over PDF pages 3–190.
Its 6,859 scanned text rows were reconciled conservatively against the printed
witness, including the duplicated 31-line scan leaf and one cut-off unreadable
baseline. It contributed 2,292 released manuscript rows and 13,742 English
words. Its audit and release construction live in
`research/working/current143/`. This work is included in the verified public
totals above.

All checks passed at that checkpoint:

```bash
python scripts/check-alignment.py
python scripts/audit-drafts.py --write-progress
npm test
npm run build
```

## Inventory 142: unfinished and not released

Do **not** publish inventory 142 in its current state. None of its manuscript
rows have been inserted into the release, source manifest, source-gap registry,
or live site.

The authoritative scan is:

```text
sources/raw/manuscript-full-91-146/142.pdf
SHA-256 2b1fd33d35b9fec662724180743e44a26bc44d8b347d5f99c373acf98cb6c73f
149 PDF images
```

Do not use `sources/raw/manuscripts/142.pdf`; that is an unrelated 176-page
Arabic-script document with SHA-256
`7556eece7b23e617958f6bfedb073ed667c173dc1045bd10b8d768f075eaa4a6`.

The title leaf reports 7,668 lines / 141 pages. The narrative folios run
2321–2462. A full set of page JSONL files currently exists for PDF pages
4–148, but the set is mixed: some ranges have been corrected from stable
source IDs and direct scan inspection, while other ranges retain an invalid
first attempt based on mutable release ordinals. Consequently the current
`audit_working.py` totals, duplicate-counterpart count, and inversion count are
diagnostics only and are not canonical corpus figures.

### Corrected or directly transcribed ranges

- Pages 4–24: corrected from the authoritative scan and stable
  `seytek-2012` source IDs; 1,090 physical rows and 5,403 whitespace English
  words.
- Pages 25–38: direct visual first pass; 745 physical rows and 4,355 English
  words; 6 explicitly unreadable/clipped rows.
- Pages 39–52: direct visual first pass; 661 physical rows and 3,873 English
  words. Page 39 is a reordered/repeated leaf with 23 explicit unreadable
  baselines. Page 52 ends at `seytek-2012:p0943:b003:l007`; page 53 begins at
  `seytek-2012:p0943:b003:l008`.
- Pages 53–100: rebuilt from stable source IDs after the ordinal error; 2,874
  physical rows and 15,424 English words. A direct scan audit established
  distinct pages 61 and 62 both numbered folio 2378. The `folio` metadata of
  all 2,322 rows on pages 62–100 was corrected on 2026-09-23; no verse text or
  English was changed. A direct boundary check proves PDF page 100 ends at
  `seytek-2012:p0974:b003:l006` and page 101 begins at the next printed row;
  the saved page-100 file wrongly ends at `seytek-2012:p0979:b004:l002`.
  The range needs a full image/boundary rebuild. See
  `research/working/current142/BOUNDARY-100-101-2026-09-23.md` and
  `research/working/current142/folio-boundary-audit-2026-09-23.md`.
- Pages 113–124 and 137–148: a partial direct-scan correction written before
  the worker stopped. These files validate structurally and are preserved as
  work in progress. They still need independent visual sampling and continuity
  checks.

### Invalid or incomplete ranges

- Pages 101–112 and 125–136 still contain the invalid first attempt and must be
  rebuilt from the authoritative scan. The scan confirms PDF pages 101–104 are
  folios 2417–2420, while those draft files label them 2415–2418. Draft pages
  124 and 125 also repeat the same text despite distinct photographed leaves.
- Pages 113–124 and 137–148 must be treated as provisional until independently
  checked; the correction job did not finish the surrounding range.
- The physical-extent audit is unfinished. The current page files sum to 7,997
  rows, 329 above the title-leaf tally of 7,668. The scan contains extra or
  reordered photography, and at least page 39 is anomalous. Identify every
  duplicated/extra leaf by comparing images and text before deciding the
  canonical physical count.
- Current audit output reports repeated counterparts and two inversions because
  corrected and invalid ranges are mixed. Do not interpret these as manuscript
  facts.

The page validator is:

```bash
python scripts/validate-manuscript-transcription.py \
  research/working/current142/page-NNN.reviewed.jsonl \
  --pages NNN \
  --source-id sayakbay-ms-current142 \
  --pdf sources/raw/manuscript-full-91-146/142.pdf \
  --require-english
```

The working audit and release-input builder are:

```text
research/working/current142/audit_working.py
research/working/current142/build_release_inputs.py
```

`build_release_inputs.py` must not be used for publication until the mixed page
set and physical-extent discrepancy are resolved. It currently raises a
release-readiness error before writing any output.

## Safe resume sequence

1. Rebuild pages 101–112 and 125–136 from actual PDF images in the authoritative
   scan. Use visible folios and stable `seytek-2012:p...` IDs; never use compiled
   release ordinals.
2. Independently sample pages 113–124 and 137–148 against their images, then
   check every page boundary from 100 through 148.
3. Audit the complete PDF for repeated or extra photographed leaves and
   reconcile the page-row sum with the title-leaf 7,668-line tally. Preserve
   real manuscript repetition; exclude only demonstrated duplicate photography.
4. Run `research/working/current142/audit_working.py`. Resolve unexpected reused
   counterparts and inversions. Page 39 is the only presently documented
   monotonicity exception.
5. Only after that, run `build_release_inputs.py`, review every overlap and
   unreadable exclusion, add inventory 142 to `sources/manifest.json`, merge its
   unresolved rows into `corpus/source-gaps.json`, and insert the batch after
   `seytek-1991-continuation:p0348:b002:l024` so it precedes inventory 143.
6. Run alignment, draft, test, and production-build checks. Commit and push the
   exact result, deploy that exact commit, and verify the public URL with
   `scripts/verify-live.py`.

The broader project is still incomplete. `corpus/source-gaps.json`, per-source
audit documents under `research/working/`, and `corpus/progress.json` are the
machine-readable starting points for all remaining coverage work.
