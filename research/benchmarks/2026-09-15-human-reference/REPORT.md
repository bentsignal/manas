# Six-configuration, four-passage translation pilot

Sol low remains a reasonable next configuration to try. On this pilot, both Terra configurations made more consequential meaning errors. The small differences among Sol and Astra do not establish a reliable winner. Higher reasoning effort did not consistently improve results.

## Results

Each configuration translated the same four passages in four fresh sessions: **86 source lines / 286 source words**. All **24 runs** returned every numbered record, yielding **516 English lines / 3,063 English words** across the six configurations. No English fields were null. Record completeness does not mean every meaning was successfully translated.

Scores measure 48 prespecified shared meaning units, each worth 0–2 points, averaged across two blinded AI assessments. They are **rubric points out of 96, not accuracy percentages**.

| Configuration | Mourning /24 | Cravings /24 | Mother's plea /24 | Armed arrival /24 | Mean /96 | Judge totals | English words |
|---|---:|---:|---:|---:|---:|---|---:|
| Astra low | 24 | 24 | 24 | 23.5 | 95.5 | 96, 95 | 517 |
| Astra medium | 24 | 23 | 24 | 23.5 | 94.5 | 95, 94 | 507 |
| Sol low | 24 | 22 | 24 | 23.5 | 93.5 | 94, 93 | 534 |
| Sol medium | 24 | 22.5 | 24 | 22.5 | 93 | 94, 92 | 507 |
| Terra high | 19.5 | 22 | 23 | 20.5 | 85 | 85, 85 | 489 |
| Terra medium | 22 | 21 | 21.5 | 20.5 | 85 | 86, 84 | 509 |

Each row contains 86 output lines. Word counts use whitespace-separated English translation words and exclude uncertainty notes. No actual token usage, cost, or controlled timing was exposed/recorded, so this experiment does not quantify savings or speed.

## Human grounding and its limits

The reference is [Elmira Köçümkulkızı's attributed Karalaev translation](http://www.silkroadfoundation.org/folklore/manas/manasintro.html). Her introduction describes reviewing the English line by line with Daniel Waugh and documents omissions and combined verse lines. We selected continuous matching passages without visible omission markers from [section 1](http://www.silkroadfoundation.org/folklore/manas/manassec1.html), [section 2](http://www.silkroadfoundation.org/folklore/manas/manassec2.html), [section 3](http://www.silkroadfoundation.org/folklore/manas/manassec3.html), and [section 4](http://www.silkroadfoundation.org/folklore/manas/manassec4.html).

**These are manually matched passage parallels, not verified identical-edition translations.** The human translation uses the 1995 academic edition; our Kyrgyz is from the 2010 Karalaev edition. The selected Kyrgyz was checked against rendered PDF pages 17, 87, 129, 130 and 150. Meaning checks exclude evident geographic, tense and weapon-modifier ambiguities. This is a useful human-anchored pilot, but it does not meet the stronger standard of having the human translator's exact original Kyrgyz edition in hand. Human reference text was kept locally and is not republished here.

The two graders were fresh agents inheriting coordinator settings, not independent human Kyrgyz experts or a cross-model panel. They received the human reference, source and fixed meaning checks, but only anonymous candidate IDs. Their scores were saved before the coordinator opened the model key. They can share systematic biases despite being separately run. Source-correct alternatives should not be penalized merely for differing from the reference.

## Errors that matter

- Both Terra settings changed the excessive-tribute demand into a claim about strength, and both omitted pregnancy while retaining cravings. Terra high left opposition vocabulary untranslated; Terra medium changed the final naming statement into a claim about not having mounted a horse.
- Terra and Sol medium introduced groups of forty in the armed-arrival passage, which the shared reference does not support. Sol medium also changed the horse color. Both Terra settings turned the confrontation into receipt of news.
- Several Sol/Astra drafts rendered the difficult silk expression as literal ashes. The broad clothing check still awarded credit because another line correctly supplied the garment. This illustrates why a high score here does **not** establish reliable line-by-line literary accuracy. Those idiom concerns remain separately recorded, without silently changing the primary endpoint.

## Disagreement and sensitivity

The graders differed on **9 of 288 unit scores**. Six differences were the same disputed armor unit, applied to every configuration. The other differences concerned resistance wording, fat livestock, and fastening the stone. Every disagreement was only one point.

A clearly labeled **post-hoc sensitivity analysis** removes the disputed armor unit and senior-wife lexical-specificity unit. The original scores remain unchanged. On the remaining 92 points: Astra low and medium both score 92; Sol low 91; Sol medium 90.5; Terra medium 82.5; Terra high 81.5. This preserves the broad Terra-versus-Sol/Astra separation and removes the apparent Astra effort advantage entirely. See `sensitivity.json`.

Four short, deliberately selected early-Manas passages are not representative of the whole trilogy. There is only one run per configuration per passage, so within-prompt variability is unmeasured. Public source/reference text may have appeared in training. The meaning checks have a ceiling effect and do not exhaust all lexical or poetic decisions. There is no statistical-significance claim.

## Practical decision

This supports trying **Sol low** as the next working configuration, with source checks and uncertainty handling retained. It does not support choosing Terra for unattended translation of the full poem, or paying for higher reasoning solely on the expectation that it will improve these translations. Actual usage savings remain unmeasured. The earlier diagnostic benchmark and this different, human-anchored pilot both found more substantial errors in unaided Terra, but their scores cannot be pooled because their passages and rubrics differ.

Production translation remains paused. Benchmark outputs were not appended to the poem or deployed. The live corpus remains **149,261 lines / 830,595 English words**; acquiring and reconciling the complete 500,553-line original remains a separate unresolved requirement.

## Reproducibility

`PROTOCOL.md`, `passages.json`, source files and instructions were fixed before translation/grading; protocol SHA256 is recorded in `reference-provenance.json`. Git checkpoint `16a2104` saved the protocol before grading. All 24 translations used explicitly requested model/effort settings through the subagent tool, with fresh context and identical instructions. No weak translation was retried. Reference/tool restrictions were prompt instructions, not OS-enforced isolation; a separate full tool-log compliance audit was not performed.

Named outputs, anonymous candidates, identity key, both judge files, their hashes, validation and descriptive results are included. `blind.py` refuses to reshuffle an existing key; `summarize.py` checks all scores and deduction coverage before producing results. The human reference page hashes are retained for provenance, but its copyrighted text must be obtained separately from the cited publisher. No production-site changes were made.
