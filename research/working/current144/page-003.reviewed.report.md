# current144 PDF page 003 review

PDF page 3 is photographed folio 1. The two-line episode heading is page furniture and is excluded. All **35 visible narrative baselines** are represented in `page-003.reviewed.jsonl`, in physical top-to-bottom order, with stable IDs `sayakbay-ms-current144:pdf003:l001`–`l035`.

The page aligns continuously to released `seytek-2012:p1090:b005:l001`–`l027` and `seytek-2012:p1090:b006:l001`–`l008`. The manuscript is faint; the printed witness supplies normalized spelling and punctuation, so all rows retain `transcription_status: uncertain` and name the exact printed counterpart in `uncertainty_note`.

Validated checkpoint: **35 narrative lines / 146 whitespace-delimited English words**.

```sh
python scripts/validate-manuscript-transcription.py research/working/current144/page-003.reviewed.jsonl --pages 3 --source-id sayakbay-ms-current144 --pdf sources/raw/manuscript-full-91-146/144.pdf --require-english
```
