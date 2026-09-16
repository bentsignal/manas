# Completion-first gap translation audit

Prepared 2026-09-15. This is a read-only audit of all **974 inserted English rows** covering **982 source segments** in **925 gaps**.

## Result

The audit flags **249 rows** for later correction: **38 high severity** and **211 medium severity**. The JSON companion lists every flagged row with its exact source IDs, Kyrgyz, current English, reason, severity, original review note, and a suggested fix where the correction is sufficiently clear.

The dominant failure is reuse of an English line from a superficially similar Kyrgyz formula. This is especially unsafe for corrupt or rare words because a one-word difference often changes the participant, number, place, or action. The most conspicuous artifacts include “Call from mobile,” “The cow is sent from the brown,” “Happy birthday my cousin,” and “Scroll to be horse.” Repeated formulas involving Кыймалуу жактан and Уй күрөң propagated the same error to several rows.

High-severity flags cover broken or anachronistic English, dropped names such as Bukhara, Manas, and Kanykei, and clear number loss or substitution. Medium-severity flags capture every row whose own first-pass note says it was a low-confidence approximate match. These require source-context retranslation even when the English happens to be grammatical.

This audit intentionally does not polish acceptable drafts. Rows absent from the JSON were not proven correct; they simply did not trigger a clear semantic or reliability failure during this pass.

No corpus, release, batch descriptor, or source-gap file was edited.
