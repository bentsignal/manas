# Inventory 142: folio boundary audit, 2026-09-23

Source: `sources/raw/manuscript-full-91-146/142.pdf`, SHA-256
`2b1fd33d35b9fec662724180743e44a26bc44d8b347d5f99c373acf98cb6c73f`.
PDF page numbers below are one-based image positions. The scan, not the printed
edition or a release ordinal, determines the folio labels.

## Verified extra leaf and metadata correction

Direct renders of PDF pages 60–70 show that pages **61 and 62 both bear the
handwritten folio number 2378**. They are distinct narrative leaves, not two
photographs of the same leaf: their visible writing differs throughout, and
their handwritten marginal line counts are 58 and 46 respectively. The
existing page files have exactly 58 and 46 rows. PDF page 63 bears folio 2379;
pages 64–70 continue 2380–2386. Further direct renders confirmed page 80 =
2396, page 85 = 2401, pages 89–91 = 2405–2407, and pages 95–100 = 2411–2416.

The previous page-file metadata assigned `folio = page + 2317` across this
interval. That is correct for page 61 but one too high after the extra leaf.
The `folio` field has now been corrected to `page + 2316` on **all 2,322 rows
of PDF pages 62–100**. No IDs, Kyrgyz text, English text, counterpart claims,
or line counts were changed. This fixes a locator error only; it does not
certify their translations or scan alignment.

## Later draft range remains invalid

Direct renders show PDF pages 101–104 bearing folios **2417–2420** with
handwritten marginal counts **69, 70, 55, 48**. Their existing files have
those row counts, but incorrectly claim folios **2415–2418**. This agrees with
the earlier handoff's warning that pages 101–112 used unstable release
ordinals. Matching a page's row count is not enough to validate its individual
Kyrgyz baselines or printed counterparts. These files remain unreleased and
must be rebuilt from the images and stable source IDs. Their metadata was left
untouched so they cannot be mistaken for corrected files. A later direct count
of PDF page 101 found 58 distinct photographed baselines, page 102 has 61,
and page 103 has 52. Their apparent 69, 70, and 55 margin marks and same-sized
invalid draft files are not valid physical verse counts. See
`BOUNDARY-101-102-2026-09-23.md`, `BOUNDARY-102-103-2026-09-23.md`, and
`BOUNDARY-103-104-2026-09-23.md`.

The page-124 and page-125 draft files are another clear invalid-range clue:
they have identical opening and closing Kyrgyz lines, while the photographed
pages show distinct folios 2438 and 2439 with different handwriting. Page 125
still belongs to the rebuild range.

After the locator correction, a closer inspection of PDF page 100 found a
separate text-alignment risk. The file's last row is `Оодарышса кол өтпөйт,`
with asserted printed counterpart `seytek-2012:p0979:b004:l002`; the writing
at the photographed bottom of folio 2416 does not securely support that row.
The photo also needs an independent check at its opening baseline. Therefore
the pages 53–100 draft must not be treated as line-verified merely because its
stable printed IDs are monotonic and its marginal row counts agree. The
release-input builder now fails closed until the photographed boundaries and
invalid ranges are resolved.

## Implications for the next pass

1. Preserve both leaves numbered 2378 unless a line-by-line comparison proves
   they repeat content. A repeated folio label alone is not duplicate
   photography and cannot explain away 46 lines of the 329-row tally surplus.
2. Rebuild pages 101–112 and 125–136 against each scan image. Verify the
   first and last baseline, physical line count, and each printed counterpart
   before using English inherited from the printed edition.
3. Recheck the folio sequence and page boundaries in pages 53–61 and 101–148.
   This audit sampled those ranges; it did not establish a full physical
   extent or an archival line count.

Inventory 142 still contributes **zero** newly released lines and English
words. The compiled and live release totals are unchanged.
