# Manas — Every line

An unabridged English translation project for the complete recorded Sayakbay Karalaev corpus, targeting the reported 500,553 lines including continuations. **Not a completed translation.**

Read [the source audit](research/SOURCE-AUDIT.md) and [pilot notes](research/OPENING-PILOT.md) before translating. Current status: five printed candidate PDFs and 55 complete manuscript scans have been acquired. The newly discovered full-scan convention recovered 54 of the 56 target inventories 91–146; only current inventories 113 and 114 remain unavailable. The printed witnesses contain 405,122 extracted digital positions (not certified verses), and no certified crosswalk to the archival aggregate exists yet. The compiled draft contains 392,505 translated rows and 2,070,265 English words; deployment status is recorded separately from this source checkpoint. Source-gap regions remain explicitly accounted for in [draft progress](corpus/draft-progress.json) and the generated manifest. An existing Turkish–English Karalaev trilogy project has also been identified; its coverage and counts do not establish a complete 500,553-line translation. Completion-first acquisition priorities are recorded in [the current reconciliation](research/COMPLETION-PRIORITY-2026-09-15.md), and the complete URL/hash ledger is in [the full-scan audit](research/SAYAKBAY-FULL-SCAN-URL-AUDIT-2026-09-15.md).

## Workflows

- `python3 scripts/acquire.py`: obtain candidate editions via current publisher links and record SHA-256 provenance.
- `npm run audit:sources`: use Poppler to preserve PDF pages, blocks, bounding boxes and original characters in local JSONL. The legacy font mapping is provisional; output order is not certified verse order.
- `python3 scripts/audit-drafts.py`: account for every display line in saved page batches, check overlap consistency, and report unresolved source fragments. This does not certify archival completeness.
- `python3 scripts/check-alignment.py`: reject unmarked source gaps, duplicated/reordered display lines and undocumented source-text changes in the released prefix.
- `npm run release:compile`: validate the JSONL shards indexed by `corpus/release/index.json`, then emit immutable 256-line chunks plus a small manifest. Empty releases render an empty poem column.
- `npm test`: check release safeguards and bounded scroll-window traversal through all 500,553 positions using clearly synthetic test fixtures.
- `npm run dev` / `npm run build`: run/build the React reader.
- `python3 scripts/verify-live.py`: fetch the live manifest and all content-addressed chunks, verify them against the local compiled release, and report live draft lines and English words. Run after deployment succeeds.

## Reader architecture

The opening 256 lines and manifest are server-rendered. The continuous reader fetches 256-line chunks containing English, IDs, ordinals and gap markers on demand. Chunk filenames are content hashes, so later releases reuse unchanged chunks while generated assets not referenced by the current manifest are pruned. It retains at most 12 chunks, and mounts only visible lines plus overscan. A moving 2,048-line virtual window avoids browser maximum scroll-height limits. The page contains English verses in a narrow, centered Times New Roman column, with a plain editorial marker at any unresolved source gap. Markers are not counted as translated verses or words. Direct line links and automatic local position restoration remain available without visible controls. `/read` aliases the same reader.

Runtime scroll rebasing has unit coverage for index arithmetic but still requires browser verification with a licensed, nonempty corpus. Do not describe it as performance-tested at production scale.

Source PDFs, raw research HTML and extracted text are local-only and excluded from source pushes. Public release data must carry a documented publication basis. Research notes stay in the repository. The page contains the released draft verses; there are no padded verses or fabricated demo lines.

Every progress update pairs draft verse-line counts with English word counts and distinguishes saved drafts, compiled releases, and verified live content. Count alphabetic words with internal apostrophes/hyphens; exclude notes, headings, Kyrgyz text, and unresolved markers. An unidentified transliteration is not a completed English verse.

## Release records

The canonical JSONL records are stored in content-hashed shards of at most 1,000 rows, indexed by an atomic checkpoint with per-shard and total checksums. The append utility maintains this store; use `scripts/release_store.py` to read or update it.

Each JSONL record requires `ordinal`, permanent source `id`, `part`, `source_id`, `ky`, `en`, `transcription_status: "verified"`, `status: "draft" | "reviewed"`, and `source: {url, page}`. Reviewed records also require `review: {reviewer, evidence, date}`. The referenced source in `sources/manifest.json` must include its SHA-256 and `publication_basis`.

The `complete` flag additionally requires exact per-part coverage, every line reviewed, and explicit source reconciliation evidence in `corpus/target.json`. Repeated source text is preserved: uniqueness applies to source IDs, never to text content.

## Remaining work

Reconcile original notebook inventory and edition counts; locate full continuations; establish publication basis; verify transcription and column order; conduct pilot translation with a qualified reviewer; measure cost; run resumable bulk translation and review; populate and verify the reader; publish the complete edition only when all checks pass. See the audit for concrete library leads and unresolved count conflicts.

## Progress backups

Public GitHub mirror: https://github.com/bentsignal/manas (`github` remote, `main` branch).
The release coordinator commits completed translation batches and coverage metadata frequently and pushes `main` to GitHub after each checkpoint, in addition to pushing each published version to the Sites source repository. Workers save only their assigned files; the coordinator handles shared Git commits and publication. Unfinished source research and original PDFs remain local under the existing ignore rules. Do not push backup branches or use `--all`/`--mirror`; those can include superseded large release snapshots.
