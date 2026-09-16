# Current146 terminal-page metadata and classification audit (PDF 249–252)

Source inspected directly: `sources/raw/manuscript-full-91-146/146.pdf`, SHA-256 `f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4`. PDF pages 249–252 were rendered and visually checked.

## Folio evidence

| PDF page | Assigned `page + 383` value | Numeral actually photographed | Finding |
|---:|---:|---:|---|
| 249 | 632 | **630** | The upper-right manuscript numeral is legible as 630. |
| 250 | 633 | **631** | The upper-right manuscript numeral is legible as 631. |
| 251 | 634 | **632** | The upper-right manuscript numeral is legible as 632. |
| 252 | 635 | none | Outside back cover; it is not a numbered manuscript leaf. |

Thus the terminal numbered leaves follow `photographed folio = PDF page + 381`, not the assigned `page + 383` convention. The assigned values are systematically two pages too high here. Page 252 supplies no evidence for a folio number, so 635 must not be presented as a photographed numeral.

## Content and classification

- **PDF 249 / photographed folio 630:** 36 narrative baselines in `page-249.reviewed.jsonl`; no heading or page furniture should enter the verse count.
- **PDF 250 / photographed folio 631:** 34 narrative baselines in `page-250.reviewed.jsonl`; no heading or page furniture should enter the verse count.
- **PDF 251 / photographed folio 632:** exactly 12 narrative baselines (`l001`–`l012`) followed by one closing heading (`l013`, `Бүттү`, “The End”). The heading is physical source text and may remain classified as `heading`, but it is nonverse and must not increase the poem-line count. The later date, performer/scribe colophon, and archival notation are paratext rather than verse and remain excluded from the verse transcription.
- **PDF 252:** blank outside back cover. It has zero verse baselines, zero headings, and no folio numeral. The intentionally empty reviewed JSONL is correct; no placeholder or synthetic row should be created.

## Exact canonical and batch handling

1. Keep all stable source IDs and PDF page numbers unchanged.
2. In physical extraction metadata, correct pages 249–251 to photographed folios **630, 631, and 632**. Do not assign a photographed folio to page 252. If the current schema cannot represent a missing folio, leave page 252 rowless and document the cover in provenance rather than inventing 635.
3. Canonical verse content should include page 249 `l001`–`l036`, page 250 `l001`–`l034`, and page 251 `l001`–`l012` only.
4. Preserve page 251 `l013` in the physical extraction as `classification: heading`; list it in the batch's `excluded_source_ids` with kind `heading`. Do not emit it as a canonical poem line.
5. Represent page 252 only in audit/provenance coverage as a checked blank cover with zero rows. Do not add a canonical line, batch source ID, blank translation, or inferred folio.
6. The existing terminal batch pattern—12 page-251 narrative IDs, explicit exclusion of `pdf251:l013`, and no page-252 source row—is the correct verse-handling pattern. Only the terminal folio metadata needs correction where it is stored.

This handling accounts for every visible verse baseline while keeping closing and archival matter from inflating the poem count.
