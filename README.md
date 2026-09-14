# Manas — Every line

An unabridged English translation project for the complete recorded Sayakbay Karalaev corpus, targeting the reported 500,553 lines including continuations. **Not a completed translation.**

Read [the source audit](research/SOURCE-AUDIT.md) and [pilot notes](research/OPENING-PILOT.md) before translating. Current status: four candidate PDFs acquired, 401,930 unreviewed extracted text lines (not verses), zero certified archival verse counts, 380 draft English rows released. No complete English predecessor was found, but priority is not established.

## Workflows

- `python3 scripts/acquire.py`: obtain candidate editions via current publisher links and record SHA-256 provenance.
- `npm run audit:sources`: use Poppler to preserve PDF pages, blocks, bounding boxes and original characters in local JSONL. The legacy font mapping is provisional; output order is not certified verse order.
- `npm run release:compile`: validate `corpus/release.jsonl`, then emit immutable 256-line chunks plus a small manifest. Empty releases render an empty poem column.
- `npm test`: check release safeguards and bounded scroll-window traversal through all 500,553 positions using clearly synthetic test fixtures.
- `npm run dev` / `npm run build`: run/build the React reader.

## Reader architecture

Only the manifest is server-rendered. The continuous reader fetches 256-line chunks on demand, retains at most 12 chunks, and mounts only visible lines plus overscan. A moving 2,048-line virtual window avoids browser maximum scroll-height limits. The page contains only English verses in a narrow, centered Times New Roman column. Direct line links and automatic local position restoration remain available without visible controls. `/read` aliases the same reader.

Runtime scroll rebasing has unit coverage for index arithmetic but still requires browser verification with a licensed, nonempty corpus. Do not describe it as performance-tested at production scale.

Source PDFs, raw research HTML and extracted text are local-only and excluded from source pushes. Public release data must carry a documented publication basis. Research notes stay in the repository. The page now contains the opening draft; there are no padded verses or fabricated demo lines.

## Release records

Each JSONL record requires `ordinal`, permanent source `id`, `part`, `source_id`, `ky`, `en`, `transcription_status: "verified"`, `status: "draft" | "reviewed"`, and `source: {url, page}`. Reviewed records also require `review: {reviewer, evidence, date}`. The referenced source in `sources/manifest.json` must include its SHA-256 and `publication_basis`.

The `complete` flag additionally requires exact per-part coverage, every line reviewed, and explicit source reconciliation evidence in `corpus/target.json`. Repeated source text is preserved: uniqueness applies to source IDs, never to text content.

## Remaining work

Reconcile original notebook inventory and edition counts; locate full continuations; establish publication basis; verify transcription and column order; conduct pilot translation with a qualified reviewer; measure cost; run resumable bulk translation and review; populate and verify the reader; publish the complete edition only when all checks pass. See the audit for concrete library leads and unresolved count conflicts.
