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
