# Prior translation and Internet Archive source update

Checked 14 September 2026 UTC. **A publicly available Turkish-English Karalaev translation project is now verified by downloaded files and sampled body text. Claims that no English project exists should be withdrawn. Neither its completeness nor a “first complete” translation has been established.** This is a separate update; SOURCE-AUDIT.md and the release were not edited.

## What exists, and what its dates mean

[IA Turkish-English trilogy](https://archive.org/details/manas-trilogy-bilingual-tr-en-karalaev), credited to **Gazâ'nın Neferi**, has an IA `publicdate`/`addeddate` of **2026-08-27 12:26:27**. Its metadata lists one Manas PDF, 21 Semetey PDFs and nine Seytek PDFs. The item claims 401,259 verses across 11,413 pages, partitioned 84,830 / 227,102 / 89,327. These are uploader claims, not audited counts.

The current metadata was saved as `research/manas-trilogy-bilingual-tr-en-karalaev-metadata.json` (SHA-256 `90c1e9268e266adfc775a0fcdf96b3c173fbdb4b58ed40772edbf06cee3b9d5e`). IA's recorded public date establishes item chronology; it does not independently prove the date every current file version became available, a pre-IA publication date, or priority over all other translations.

## Checked file evidence

| Acquired artifact | Bytes | SHA-256 |
|---|---:|---|
| `sources/raw/manas-ia-tr-en-comparison.pdf` | 49,167,782 | `9a5c0b1467ceb077f217f1a2b37d1a5b6244bc6c7f78525ff4973c42a9292a50` |
| `sources/raw/seytek-ia-tr-en-ix-comparison.pdf` | 7,413,519 | `0c13a87a20fba79001532215906e336cf540935f9b4c03c5fb6e4a446a576109` |

The Manas file has **2200 PDF pages**; Seytek IX has **189**. Both identify WeasyPrint 69.0 as PDF producer; that identifies rendering software, **not** whether AI generated their text. No human/AI production method was established. Their English text is present in the body, not only an English preface. Source attribution points to Turar editions, not an independently documented manuscript transcription. The copyright/source page and English preface describe a bilingual translation but do not establish a fully audited direct-from-Kyrgyz English workflow.

Specific completeness checks:

- **Manas PDF 53** replaces our damaged page-48 region with an ellipsis in both columns. No missing Kyrgyz text is recovered. Visually checked image: `tmp/pdfs/ia-tr-en-gap-053.png`.
- **Manas PDF 2198**, its last narrative page, visibly labels the ending **78710**, despite the claimed 84830. This is an unresolved internal numbering discrepancy; the number alone is not an audited verse total. Image: `tmp/pdfs/ia-tr-en-ending.png`.
- **Seytek IX PDF 187** ends with Akjoltoy's dream interpretation and gifts, matching the boundary of our Turar Seytek PDF 1165. PDF 188 declares the ending. It does **not** extend into the 34 Kenen continuation pages located in the older scan. Direct extraction: `sources/extracted/seytek-ia-tr-en-ix-direct.txt`; image: `tmp/pdfs/ia-seytek-ix-ending-187.png`.
- A downloaded IA OCR derivative of Semetey XXI contains English through its transition to Seytek. This is a sampled text check, not full PDF/translation verification. File: `sources/extracted/semetey-ia-tr-en-ending.txt`, SHA-256 `9ba0837e16591a8fd2dad80f9de2c788a8e6d597437d369e1a44021fb76e9438`.

These checks establish a substantial existing project and material gaps in its completeness evidence. They do not measure overall translation quality, certify every listed volume, or warrant copying its translation into our independent work.

## The Kyrgyz IA item adds no original source

[IA Kyrgyz trilogy](https://archive.org/details/manas-trilogy-sayakbay-karalaev-ky) has `publicdate` **2026-09-03 19:01:27**. Its Manas PDF was downloaded as `sources/raw/manas-ia-comparison.pdf`: 16,242,844 bytes, SHA-256 `53bb71b63a0ad255e815b57f23fb41c8f3160cf05fd7b374add3516c7ccd99d7`, exactly matching our base file. For the other PDFs, the public file-manifest SHA-1 values match our local files:

| IA original filename | Matching local source | SHA-1 |
|---|---|---|
| manas-vol-1.pdf | manas-2010.pdf | 9b27047aa660e258ea442a7d1b179caf615b3073 |
| semetey-vol-2.pdf | semetey-1-2013.pdf | 40b51b5e0b74e47bf1a8ea0ff712bfe1512d7bc4 |
| semetey-vol-3.pdf | semetey-2-2013.pdf | b7b3ada33392c7f3a4d8a35ab9cc50217839e8d5 |
| seytek-vol-4.pdf | seytek-2012.pdf | 3418858046deb1dcde8e008c6fabd32eb7591dd4 |

Metadata snapshot: `research/manas-trilogy-sayakbay-karalaev-ky-metadata.json`, SHA-256 `71a35f9489f8c66a4424d91bb7e65f6df66480745ba84d0ef3f1d2268fdbe7a9`. No IA file establishes the full 500,553 reported verses. The remaining source acquisition and reconciliation requirements in CONTINUATIONS-CHECK.md still apply.
