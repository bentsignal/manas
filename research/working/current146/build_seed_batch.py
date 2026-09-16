import json
from pathlib import Path

OUT = Path(__file__).with_name("pages-005-020.jsonl")
SHA = "f13de4f4bc48f2da4eb502e29e9b2b340648255ef7769b069e86d24c617319a4"

# Counts made from the 300-dpi render, page by page. Faint and overwritten strokes
# were counted as part of a line when they occupy the same baseline.
COUNTS = {5: 36, 6: 33, 7: 32, 8: 32, 9: 30, 10: 35, 11: 32, 12: 31,
          13: 34, 14: 29, 15: 29, 16: 31, 17: 31, 18: 38, 19: 36, 20: 34}

# Readable anchors are retained; bracketed ellipses mean that the remainder of
# that same physical line was not deciphered. Lines without a safe reading are
# represented explicitly rather than silently dropped.
ANCHORS = {
    (5, 1): "Бу кайран атаң арбагы",
    (5, 2): "Надишинден жер болуп,",
    (5, 3): "Мунун түп атасы кан болуп,",
    (5, 5): "Кара Кожжал арабтан,",
    (5, 6): "Боорук Кенен баатырдын,",
    (5, 8): "Калка ата кан болуп,",
    (5, 9): "Телик күлкү күн кылып,",
    (5, 10): "Теңирден журт кылып,",
    (5, 13): "Жабыркай туруп зор болуп,",
    (5, 19): "Тилге келген адамды,",
    (5, 20): "Тили менен эл кылып,",
    (5, 23): "Беттен адам баатыр,",
    (5, 24): "Берен Кенен жең деп,",
    (5, 26): "Минген аты кер тулпар,",
    (5, 29): "Кенен сурап албаган,",
    (5, 31): "Куу амалын этпеген,",
    (6, 1): "Тилге келген акылман,",
    (6, 2): "Тилегинин тил кылган,",
    (6, 3): "Каардууну калса да,",
    (6, 4): "Келбес жерин келишкен,",
    (6, 5): "Мага недир дегенин,",
    (6, 6): "Баарын жообун келишкен,",
    (6, 7): "Козголгондой чаң чыккан,",
    (6, 8): "Кобуржуган жан чыккан,",
    (6, 9): "Беттен адам баатыр,",
    (6, 10): "Бейли тар колун жайбаган,",
    (6, 12): "Жоро күтүп эр жыйып,",
    (6, 13): "Түлөгөндөн тең жыйып,",
    (6, 16): "Калган минин баатырын,",
    (6, 20): "Кабыландай каар алып,",
    (6, 21): "Кабылан Кенен атанып,",
    (6, 22): "Каармандын ок кылып,",
    (6, 25): "Кан чыгарган жок кылып,",
    (6, 28): "Койран Кожжал болду деп,",
    (6, 29): "Атабынан бабасы,",
}

with OUT.open("w", encoding="utf-8") as fh:
    for page in range(5, 21):
        folio = 383 + page  # p5=388 ... p20=403
        for n in range(1, COUNTS[page] + 1):
            text = ANCHORS.get((page, n), "[окулбайт]")
            safe = (page, n) in ANCHORS
            row = {
                "id": f"sayakbay-ms-current146:pdf{page:03d}:l{n:03d}",
                "source_id": "sayakbay-ms-current146",
                "pdf_sha256": SHA,
                "page": page,
                "folio": folio,
                "line_in_page": n,
                "raw": text,
                "text": text,
                "classification": "narrative",
                "transcription_status": "uncertain" if safe else "unreadable",
                "uncertainty_note": (
                    "Visual reading from 300-dpi render; spelling/word division needs independent Kyrgyz review."
                    if safe else
                    "Visible verse baseline counted in the 300-dpi render, but the handwriting was not safely deciphered in this pass."
                ),
                "bbox": None,
            }
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

