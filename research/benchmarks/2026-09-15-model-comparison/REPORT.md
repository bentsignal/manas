# Translation model comparison

Four fresh sub-agents translated the same54 consecutive Kyrgyz verses from Semetey1 PDF956, blocks6–7. Models/reasoning were explicitly selected through the sub-agent tool. Translation workers for the main project remained paused. The contestants received the same short context, extracted Kyrgyz and instructions, with no dictionary or existing English translation. All returned54 aligned records, with no null translations.

The coordinator fixed a rubric, randomly relabeled the completed outputsA–D without displaying the identity key, graded them against the Kyrgyz and primary lexical evidence, saved the scores, then revealed the key. This was an anonymous coordinator review, not an independent specialist evaluation. The score file before reveal had SHA2564129685404b018c2321cb83758307fb125de306bd767c015d1d4baf498e1c387.

| Configuration | Rubric score /100 | Semantic /80 | Uncertainty /10 | Structure /10 |
|---|---:|---:|---:|---:|
| astra-medium | 92.4 | 74.4 | 8 | 10 |
| sol-low | 88.8 | 72.8 | 6 | 10 |
| sol-medium | 86.8 | 71.8 | 5 | 10 |
| terra-medium | 71.5 | 59.5 | 2 | 10 |

These are editorial rubric scores, not accuracy percentages. Small score gaps are not significant evidence from a single run. The sample deliberately includes difficult vocabulary; it is not a random sample of the entire poem.

## Findings

- Astra medium handled joining/rejoicing instead of mourning, marten fur, Karabair horse designation, and uncertain constructions better overall. It still mistranslated otter as beaver and slender waist as moonlike waist.
- Sol low and Sol medium were close. Both correctly translated otter and copper forelegs, but used sable for marten and laments for joining together. Sol low’s small lead does not establish that low reasoning is generally better.
- Terra medium made substantially more source-level mistakes. It rendered two “more X than Y” comparisons as “X from Y,” turned camp geography into deep thought, mistranslated otter as sable and sable as ermine, and rendered horse forelegs as bronze arms.
- All four missed the specific millet/barley grain category and the fearless-warrior meaning of kara kok. Most rendered the slender-waist idiom too literally. Shared errors make agreement among models an insufficient correctness test.

## Recommendation

Sol low is a promising cost-conscious candidate for the next comparison using the project's actual glossary and source-checking workflow. Sol medium is also viable, with no demonstrated advantage over low in this small sample. Astra medium had a modest lead here and could be reserved for disputed passages. Terra medium was weaker enough that this test does not support putting it in charge of bulk unaided translation.

Before changing bulk work, test a larger representative sample with identical primary lexical aids, preferably with a Kyrgyz specialist checking a subset. This experiment did not measure billable token usage or actual Codex quota cost: the tool exposed neither, and wall time was not instrumented. No speed/cost winner is claimed.

## Artifacts

- [Source and context](source.txt), [source provenance](source-provenance.json), [identical instructions](instructions.txt)
- [Rubric](rubric.md), [anonymous candidates](blinded-candidates.json), [line-by-line blind scores](blind-scores.json), [identity key](identity-key.json), [structured results](results.json)
- [Terra medium output](terra-medium.json), [Sol medium output](sol-medium.json), [Sol low output](sol-low.json), [Astra medium output](astra-medium.json)

Primary lexical references are recorded in rubric.md. Current official model descriptions: [Sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol), [Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra). Their general descriptions do not supply a Kyrgyz epic translation benchmark.

No candidate output was published as poem text. Main translation remains paused pending user choice. The live poem remains149261 translated verses/830595 English words through Semetey1 PDF958.
