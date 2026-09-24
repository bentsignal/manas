# Seytek printed-column order: representative samples and scope screen

Source: `sources/raw/seytek-2012.pdf`, SHA-256 `786eb36c1863f3e6c5330bb98d5d1656ab2e566bc53e16128a4f982928ebee2f`. Coordinates below come from `sources/extracted/seytek-2012.lines.jsonl`; I also rendered printed PDF pages 600 and 985 and inspected their typography and narrative joins. This note diagnoses **sequence**, not missing verses or the semantic quality of individual English lines.

## Confirmed sample: printed page 600

On the rendered page, `b003` is visibly the **left** verse column (`xMin` approximately 76), while `b002` is the **right** (`xMin` approximately 308). The page follows ordinary left-column-then-right-column reading. Three joins support that order:

| Join in printed reading order | Kyrgyz evidence | Why it matters |
| --- | --- | --- |
| PDF 599 right footer → PDF 600 left top | `Кармап алса тырмагын,` → `Кабыргага батырган.` | Claws catching and driving into ribs complete the same action. |
| PDF 600 left footer → PDF 600 right top | `Көргөн баатыр качкандай,` → `Беттешкенди баскандай,` | Parallel predicates continue the portrayal. |
| PDF 600 right footer → PDF 601 left top | `Эрениң байлап кул кылып,` → `Каканды чаап кан кылып,` | Consecutive action phrases continue across the page edge. |

`pages-seytek-0600.json` and the local release instead emit all 40 `b002` right-column rows before all 40 `b003` left-column rows. Thus this page's 80 line records are present but read in the wrong block order.

## Confirmed sample: printed page 985

The rendered page again shows `b003` on the **left** (`xMin` approximately 79) and `b002` on the **right** (`xMin` approximately 310). The left column opens `Таш майданда чабыштың,` and runs through Sarybay's speech. Its final line, `Минтип жанын күйгүзүп,` ('Thus tormenting his soul'), leads into the right column's opening `Сынчыларга каратып,` ('Turning toward the horse judges') and the ensuing action. The right footer, `Күйгүзгөнү чочконун,`, then continues into printed page 986's left-column `Сөксөөлдүн чогундай,`. The current `pages-seytek-0985.json` and release put the right block first. The manuscript draft crosswalk for inventory 142 was **not** used as evidence here.

## Scope screen, not a page-by-page certification

I enumerated extracted pages with both `b002` and `b003` containing at least 30 rows, a batch file with both blocks, and `b002` physically right of `b003`. **666 pages** meet these criteria. In every one, the batch and local `corpus/release/index.json` order put `b002` before `b003`; those blocks comprise **53,261 released line records**. Of the 666 flagged pages, 659 fall from printed pages 26–744 and seven are 772, 823, 905, 916, 945, 985, and 995. Page 745, for example, has a heading mixed into `b002` and was excluded by the two-verse-block filter. The count is a reproducible *candidate scope* based on block coordinates and emitted order, not proof that I visually inspected all 666 pages or that all have identical narrative continuity.

The p600 and p985 rendered pages, together with neighboring joins, confirm a genuine order error in separated parts of the volume. Because the 666-page screen is broad, the release compiler should derive reading order from physical columns and handle headings, footnotes, and unusual layouts separately. Reorder **whole source/English line records together**, retaining each ID and translation. Before publishing a repaired release, independently inspect a stratified set across the long early run and the seven later outliers, verify boundary joins, and rerun line accounting and release checks. Do not infer that a line is absent merely from this ordering defect.
