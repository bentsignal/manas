# Targeted textual comparisons: Manas PDF pages 16, 21 and 48

Checked 14 September 2026 UTC. Shared release rows and source manifest were not edited.

## Decisions

| Source location | Decision | Basis |
|---|---|---|
| `manas-2010:p0048:b002:l002`–`l004` | **Keep `unresolved_source`; no reconstructed verse supplied.** | Image contains `Т/*`, `о`, `и` on one baseline; another online text repeats these exact fragments. |
| `manas-2010:p0016:b003:l011` | **Recommend an explicitly documented emendation of `бирге` to `пирге`.** | Earlier Karalaev first-volume digital witness, PDF 22, visually reads `пирге*`; encyclopedia also cites Karalaev volume 1, printed p.27. Preserve original raw text. |
| `manas-2010:p0021:b002:l035` | **No textual correction established; preserve `Он эки кылым салбаптыр,` with an interpretation note.** | Online comparison repeats this wording; older first-volume witness does not provide a directly matched line. |

## Page 48: a gap remains

Inspected `tmp/pdfs/pages-0036-0055/page-0048.png` visually. Immediately after `Каяшаяк бергенди`, the next baseline contains three disconnected fragments. The following intelligible verse is `Кайра тартып тим койбой,`. This proves corruption in the digital witness, but not the original wording, the number of lost words, or that an entire independent verse existed there. Treat the three extraction IDs as one unresolved source region; do not manufacture three verse rows and do not dismiss the region as non-verse.

[Speak.tatar section 03](https://speak.tatar/en/lit/kir/text/manas-sayakbay-karalaev-01-03/) repeats the exact three damaged fragments at this location. This is strong evidence of common digital ancestry, not independent corroboration. [Meikin page 10](https://www.meikin.org/epos/aikol-manas-baiany?content_page=10) moves straight from the preceding line to the following intelligible line. Its surrounding wording follows the same digital text; no independent scan, transcription method or source-edition provenance was established. Deletion there therefore cannot establish that the fragments are dispensable.

The new Karalaev first-volume comparison file has a substantially shorter early narrative. Exact searches for the following intact line, its distinctive beginning, and the Shibe/Dongo passage did not locate a directly comparable passage. Its absence cannot repair the 2010 witness.

Next decisive evidence: a photograph/scan of the corresponding **printed Turar 2010 page**, or an independently documented manuscript/academic edition preserving this expanded passage. Supply the archive with preceding/following verse and Dongo's subsequent speech. Until then the published text needs a visible damaged-source marker, and continuity/completeness claims must retain the gap.

## Page 16: supported `пирге`

Downloaded [Bizdin's Karalaev first volume](https://new.bizdin.kg/kniga/epos-manas-pervyy-tom/), 439 PDF pages, to `sources/raw/manas-first-volume-bizdin.pdf`. SHA-256: `c34030215a8fd8957636b592d8aa26ee31b05c3ee0939fd483e9b1b35c35927c`. It is another reflowed digital witness, not a scan of the printed page. The preface is signed S. Musaev, 5 May 1982; the publication year has not been securely identified from the file. Do not label it an acquired academic 1995 edition.

PDF 22 was rendered and visually inspected (`tmp/pdfs/firstvolume-opening-022.png`). Its complete raw line is:

> Оң эки пирге* кол берип,

The local witness has its own `Оң` typo, so use it to support the specific `пирге` reading, not wholesale replacement of the whole line. [The indexed Manas encyclopedia, volume 2](https://new.bizdin.kg/media/books/%D0%9C%D0%B0%D0%BD%D0%B0%D1%81_%D1%8D%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F%D1%81%D1%8B._2_%D1%82%D0%BE%D0%BC.pdf), associates the formula with Karalaev volume 1, printed p.27. [Yudakhin's dictionary](https://el-sozduk.kg/%D0%BF%D0%B8%D1%80/) explains giving one's hand to a pir as becoming the follower of a spiritual guide. Thus an English rendering such as **“He pledged himself to twelve spiritual guides”** is supported, with a note that the base PDF reads `бирге` and the reading has been corrected by comparison. This is a documented editorial emendation, not proof that the base PDF glyph is itself `п`.

[Speak.tatar section 02](https://speak.tatar/ru/lit/kir/text/manas-sayakbay-karalaev-01-02/) repeats the base PDF's erroneous `бирге`, further weakening it as an independent witness.

## Page 21: wording unresolved in context

Speak.tatar section 02 repeats the same complete line and the next three lines. No independently documented correction was found in this pass. A [later Karalaev volume's indexed text](https://new.bizdin.kg/media/books/Manas-eposu-2-tom_t7Xe9ZO.pdf) has the related formula `Он эки кылым салбаган,` followed by `Кайыр айтуучу калбаган.` This is a parallel, not a witness to the page-21 line and not an acquired scan.

[Yudakhin's `кылым` entry](https://el-sozduk.kg/%D0%BA%D1%8B%D0%BB%D1%8B%D0%BC/) documents epic meanings including world/universe and all people, alongside century/epoch. Therefore a literal “twelve centuries” should not be treated as uniquely established. The exact construction and translation remain for specialist review; do not silently change `кылым` or `салбаптыр` based on conjecture.

## Other acquisition from this search

`https://cdn-1.aki.kg/st_bilimlib/8/6ba4d8da68bdb70850cc2e35ec861c0213e5b51f.pdf` was downloaded under `sources/raw/manas-aki-candidate.pdf` (34,770,598 bytes; SHA-256 `68bc80c49971f65cf755f6ef4d49e22396d9ca913b53b1f18aace29563f74178`). Despite the initial search context, visual inspection identifies **Seytek, Karalaev's variant**, not Manas. Title page says Frunze, Adabiyat, 1991; bibliographic page says 1990, 352 printed pages, ISBN 5-660-00194-7. Local text extraction is empty; it is an image scan requiring OCR/transcription. No completeness or additional verse coverage is inferred. Metadata for both acquired files was appended only to `research/source-candidates.json`.

## Page243:l006 English correction

Changed “All the strength of the Almighty” to “All the strength he had”. Yudakhin бардигер/бардыгер means all available and cites this exact strength-gathering formula: https://el-sozduk.kg/БАРД/. Kyrgyz witness and ID unchanged.

The same formula correction applies at123:l038: “When the Almighty exerted His power,” becomes “When they used all their strength,”. The 2015 dictionary quotes this exact two-line passage about children being seized.
