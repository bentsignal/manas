"""Regression checks for visually reviewed source order with stable line IDs."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from release_store import read_release
from source_order import ordered_source_rows


class SourceOrderTests(unittest.TestCase):
    def test_page_25_drop_cap_and_page_26_anchor(self):
        page = json.loads((ROOT / 'corpus/batches/pages-seytek-0025.json').read_text())
        representative = 'seytek-2012:p0025:b003:l001'
        self.assertEqual(page['source_joiners'][representative], [''])
        self.assertEqual(page['source_groups'][representative][-1],
                         'seytek-2012:p0025:b005:l001')
        release = [json.loads(line) for line in read_release(ROOT).splitlines()]
        row = next(row for row in release if row['id'] == representative)
        self.assertEqual(row['ky'], 'Аны мындай таштайлы,')
        self.assertEqual(row['source']['joiners'], [''])
        next_page = json.loads((ROOT / 'corpus/batches/pages-seytek-0026.json').read_text())
        self.assertEqual(next_page['after_id'], 'seytek-2012:p0025:b004:l031')

    def test_all_reviewed_pages_match_batch_release_and_extraction_order(self):
        overrides = json.loads((ROOT / 'corpus/source-order-overrides.json').read_text())['seytek-2012']
        with (ROOT / 'sources/extracted/seytek-2012.lines.jsonl').open() as stream:
            extracted = [json.loads(line) for line in stream]
        ordered = ordered_source_rows(ROOT, extracted)
        extraction_by_page = {}
        for row in ordered:
            extraction_by_page.setdefault(row['page'], []).append(row['id'])
        release = [json.loads(line) for line in read_release(ROOT).splitlines()]
        release_by_page = {}
        for row in release:
            if row['source_id'] == 'seytek-2012':
                release_by_page.setdefault(row['source']['page'], []).append(row)
        for page_key, override in overrides.items():
            page = int(page_key)
            self.assertEqual(override['blocks'], [3, 5, 4] if page == 25 else [3, 2])
            batch = json.loads((ROOT / f'corpus/batches/pages-seytek-{page:04}.json').read_text())
            ids = batch['source_ids']
            english = (ROOT / batch['english']).read_text().splitlines()
            self.assertEqual([sid for sid in extraction_by_page[page] if sid in set(ids)], ids)
            self.assertEqual([row['id'] for row in release_by_page[page]], ids)
            self.assertEqual([row['en'] for row in release_by_page[page]], english)
            self.assertEqual([row['ordinal'] for row in release_by_page[page]],
                             list(range(release_by_page[page][0]['ordinal'],
                                        release_by_page[page][0]['ordinal'] + len(ids))))

    def test_page_985_source_batch_and_release_keep_identical_id_english_pairs(self):
        batch = json.loads((ROOT / 'corpus/batches/pages-seytek-0985.json').read_text())
        english = (ROOT / batch['english']).read_text().splitlines()
        expected = ([f'seytek-2012:p0985:b003:l{i:03}' for i in range(1, 40)] +
                    [f'seytek-2012:p0985:b002:l{i:03}' for i in range(1, 41)])
        self.assertEqual(batch['source_ids'], expected)
        self.assertEqual(len(english), 79)
        with (ROOT / batch['extraction']).open() as stream:
            extracted = [json.loads(line) for line in stream]
        source = ordered_source_rows(ROOT, extracted)
        source_ids = [row['id'] for row in source if row['id'] in set(expected)]
        self.assertEqual(source_ids, expected)
        self.assertEqual(len(source), len(extracted))
        self.assertEqual({row['id'] for row in source}, {row['id'] for row in extracted})
        release = [json.loads(line) for line in read_release(ROOT).splitlines()]
        page_rows = [row for row in release if row['id'] in set(expected)]
        self.assertEqual([row['id'] for row in page_rows], expected)
        self.assertEqual([row['en'] for row in page_rows], english)
        self.assertEqual([row['ordinal'] for row in page_rows], list(range(372533, 372612)))
        self.assertEqual(release[372531]['id'], 'seytek-2012:p0984:b003:l040')
        self.assertEqual(release[372611]['id'], 'seytek-2012:p0986:b002:l001')
        next_batch = json.loads((ROOT / 'corpus/batches/pages-seytek-0986.json').read_text())
        self.assertEqual(next_batch['after_id'], expected[-1])

    def test_other_source_extraction_is_unaffected(self):
        rows = [{'source_id': 'w', 'page': 1, 'block': 1, 'id': 'w:p1:b1:l1'}]
        self.assertEqual(ordered_source_rows(ROOT, rows), rows)


if __name__ == '__main__':
    unittest.main()
