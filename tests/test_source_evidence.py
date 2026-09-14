import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from source_evidence import verify_source_evidence


class SourceEvidenceTests(unittest.TestCase):
    def fixture(self, legacy=False):
        original = dict(id='w:p0009:b002:l001', source_id='w',
                        pdf_sha256='digest', page=9, bbox={'xMin':1.0},
                        raw='ñåìåòåé' if legacy else 'Манас',
                        text='семетей' if legacy else 'Манас',
                        normalization='legacy-font-v1' if legacy else 'identity')
        segment = {k:original[k] for k in ('id','raw','bbox')}
        if legacy:
            segment['normalization'] = 'legacy-font-v1'
        row = dict(id=original['id'], source_id='w', ky=original['text'],
                   source=dict(sha256='digest',page=9,segments=[segment]))
        return row, {original['id']:original}

    def test_existing_identity_evidence_needs_no_migration(self):
        verify_source_evidence(*self.fixture())

    def test_legacy_glyphs_remain_raw_while_kyrgyz_is_readable(self):
        row, extracted = self.fixture(True)
        verify_source_evidence(row, extracted)
        self.assertEqual(row['source']['segments'][0]['raw'], 'ñåìåòåé')
        self.assertEqual(row['ky'], 'семетей')

    def test_missing_legacy_declaration_is_rejected(self):
        row, extracted = self.fixture(True)
        del row['source']['segments'][0]['normalization']
        with self.assertRaisesRegex(AssertionError, 'Undocumented font'):
            verify_source_evidence(row, extracted)

    def test_raw_coordinates_digest_and_reading_cannot_be_silently_changed(self):
        row, extracted = self.fixture(True)
        mutations = [lambda r:r.update(ky='different'),
                     lambda r:r['source'].update(sha256='wrong'),
                     lambda r:r['source']['segments'][0].update(raw='different'),
                     lambda r:r['source']['segments'][0].update(bbox={'xMin':2.0})]
        for change in mutations:
            with self.subTest(change=change):
                altered = copy.deepcopy(row)
                change(altered)
                with self.assertRaises(AssertionError):
                    verify_source_evidence(altered, extracted)

    def test_unrecognized_or_altered_extraction_normalization_is_rejected(self):
        for field,value in [('normalization','unknown'),('text','wrong')]:
            row, extracted = self.fixture(True)
            extracted[row['id']][field] = value
            with self.assertRaises(AssertionError):
                verify_source_evidence(row, extracted)


if __name__ == '__main__':
    unittest.main()
