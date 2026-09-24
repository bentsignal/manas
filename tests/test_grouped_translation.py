"""Exercise grouped provenance and actual append/audit CLIs in an isolated corpus."""
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
from source_evidence import build_source_evidence, descriptor_groups, verify_source_evidence
from release_store import read_release, write_release


def original(ident, raw, text, page=9):
    return dict(id=ident, source_id='w', pdf_sha256='digest', page=page,
                bbox={'xMin': float(len(ident))}, raw=raw, text=text,
                normalization='legacy-font-v1')


class GroupedTranslationTests(unittest.TestCase):
    def setUp(self):
        self.rows = [original('w:previous', 'Ìàíàñ', 'Манас', 8),
                     original('w:header', 'ñåìåòåé', 'семетей'),
                     original('w:a', 'Ê', 'К'),
                     original('w:b', 'àí Ìàíàñòûí', 'ан Манастын'),
                     original('w:c', 'ºëãºí¿', 'өлгөнү'),
                     original('w:d', 'Áàäûøà', 'Бадыша')]
        self.extracted = {r['id']: r for r in self.rows}
        self.batch = dict(source_ids=['w:a', 'w:d'],
                          source_groups={'w:a': ['w:a', 'w:b', 'w:c']},
                          source_joiners={'w:a': ['', ' ']},
                          notes={'w:a': 'The separate initial К is a drop cap; the next line wraps.'},
                          part='semetey', extraction='sources/extracted/w.lines.jsonl',
                          english='corpus/batches/pages-test.en.txt', after_id='w:previous',
                          source_url='https://example.test/source.pdf',
                          transcription_check=dict(method='visual-pdf-comparison', checked_by='test', date='2026-09-14', pdf_pages=[9]),
                          excluded_source_ids=[dict(id='w:header', kind='heading', reason='Running title')])

    def evidence(self):
        groups, joins = descriptor_groups(self.batch)
        return build_source_evidence('w:a', groups['w:a'], joins['w:a'], self.extracted,
                                     self.batch['source_url'], self.batch['notes']['w:a'])

    def test_drop_cap_and_wrapped_line_reconstruct_with_every_raw_fragment(self):
        row = self.evidence()
        self.assertEqual(row['ky'], 'Кан Манастын өлгөнү')
        self.assertEqual(row['source_line_ids'], ['w:a', 'w:b', 'w:c'])
        self.assertEqual(row['source']['joiners'], ['', ' '])
        self.assertEqual([s['raw'] for s in row['source']['segments']], ['Ê', 'àí Ìàíàñòûí', 'ºëãºí¿'])
        verify_source_evidence(row, self.extracted)

    def test_old_descriptors_and_default_space_groups(self):
        groups, joins = descriptor_groups(dict(source_ids=['w:a', 'w:d']))
        self.assertEqual(groups, {'w:a': ['w:a'], 'w:d': ['w:d']})
        self.assertEqual(joins, {'w:a': [], 'w:d': []})
        row = build_source_evidence('w:b', ['w:b', 'w:c'], [' '], self.extracted, 'url')
        self.assertEqual(row['ky'], 'ан Манастын өлгөнү')
        self.assertNotIn('joiners', row['source'])
        verify_source_evidence(row, self.extracted)

    def test_invalid_group_ownership_keys_and_joiners_are_rejected(self):
        changes = [lambda b: b['source_groups'].update({'w:a': ['w:b', 'w:a']}),
                   lambda b: b['source_groups'].update({'w:d': ['w:d', 'w:b']}),
                   lambda b: b['source_groups'].update({'missing': ['missing']}),
                   lambda b: b['source_groups'].update({'w:a': ['w:a', 'w:a', 'w:c']}),
                   lambda b: b['source_joiners'].update({'w:a': ['']}),
                   lambda b: b['source_joiners'].update({'w:a': ['-', ' ']}),
                   lambda b: b['notes'].clear()]
        for change in changes:
            with self.subTest(change=change):
                b = copy.deepcopy(self.batch)
                change(b)
                with self.assertRaises(AssertionError):
                    descriptor_groups(b)

    def test_join_changes_and_mixed_source_page_or_digest_are_rejected(self):
        row = self.evidence()
        for mutation in [lambda r: r['source'].pop('joiners'),
                         lambda r: r.pop('note'),
                         lambda r: r['source'].update(joiners=['', '']),
                         lambda r: r['source']['segments'][1].update(raw='Кан')]:
            altered = copy.deepcopy(row)
            mutation(altered)
            with self.assertRaises(AssertionError):
                verify_source_evidence(altered, self.extracted)
        for field, value in [('page', 10), ('source_id', 'other'), ('pdf_sha256', 'other')]:
            altered = copy.deepcopy(self.extracted)
            altered['w:b'][field] = value
            with self.assertRaises(AssertionError):
                verify_source_evidence(row, altered)

    def prepare_cli(self, root):
        (root / 'scripts').mkdir()
        for name in ['append-translation.py', 'audit-drafts.py', 'check-alignment.py',
                     'source_evidence.py', 'source_order.py', 'extract.py', 'release_store.py']:
            shutil.copy(SCRIPTS / name, root / 'scripts' / name)
        (root / 'sources/extracted').mkdir(parents=True)
        (root / self.batch['extraction']).write_text(''.join(json.dumps(r) + '\n' for r in self.rows))
        (root / 'corpus/batches').mkdir(parents=True)
        (root / self.batch['english']).write_text('Khan Manas has died.\nThe king\n')
        path = root / 'corpus/batches/pages-test.json'
        path.write_text(json.dumps(self.batch))
        seed = build_source_evidence('w:previous', ['w:previous'], [], self.extracted, 'url')
        seed.update(ordinal=1, en='Manas', part='manas')
        write_release(root, json.dumps(seed) + '\n')
        return path

    def run_cli(self, root, name, *args, succeeds=True):
        result = subprocess.run([sys.executable, str(root / 'scripts' / name), *map(str, args)],
                                capture_output=True, text=True)
        if succeeds:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def test_append_alignment_and_progress_count_verses_once_and_all_fragments(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.prepare_cli(root)
            self.run_cli(root, 'append-translation.py', path)
            release = [json.loads(s) for s in read_release(root).splitlines()]
            self.assertEqual(len(release), 3)
            self.assertEqual(release[1]['ky'], 'Кан Манастын өлгөнү')
            alignment = json.loads(self.run_cli(root, 'check-alignment.py').stdout)
            self.assertEqual(alignment['source_display_lines'], 5)
            audit = json.loads(self.run_cli(root, 'audit-drafts.py', '--write-progress').stdout)
            self.assertEqual(audit['unique_translated_display_rows'], 2)
            self.assertEqual(audit['unique_translated_source_fragments'], 4)
            progress = json.loads((root / 'corpus/draft-progress.json').read_text())
            self.assertEqual(progress['saved_draft_rows'], 3)
            self.assertEqual(progress['saved_draft_english_words'], 7)
            self.assertEqual(progress['saved_page_ranges_by_source'], {'w': [[8, 9]]})
            # Identical historical prefixes remain allowed without double counting.
            shutil.copy(path, path.with_name('pages-copy.json'))
            self.run_cli(root, 'audit-drafts.py')
            # A new verse cannot take ownership of a previously grouped continuation.
            b = copy.deepcopy(self.batch)
            b.update(source_ids=['w:a', 'w:b', 'w:d'], source_groups={'w:b': ['w:b', 'w:c']}, source_joiners={}, notes={})
            b['english'] = 'corpus/batches/pages-conflict.en.txt'
            path.with_name('pages-conflict.json').write_text(json.dumps(b))
            (root / b['english']).write_text('K\nKhan Manas has died.\nThe king\n')
            self.run_cli(root, 'audit-drafts.py', succeeds=False)

    def test_missing_reordered_or_previously_owned_fragments_fail_before_write(self):
        for kind in ['missing', 'anchor_reordered', 'owned']:
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                path = self.prepare_cli(root)
                b = copy.deepcopy(self.batch)
                if kind == 'missing':
                    b['source_groups']['w:a'][1] = 'w:missing'
                elif kind == 'anchor_reordered':
                    b['source_ids'] = ['w:d', 'w:a']
                else:
                    b['source_ids'] = ['w:previous', 'w:d']
                    b['source_groups'] = {}
                    b['source_joiners'] = {}
                    b['notes'] = {}
                path.write_text(json.dumps(b))
                checkpoint = read_release(root)
                self.run_cli(root, 'append-translation.py', path, succeeds=False)
                self.assertEqual(read_release(root), checkpoint)


if __name__ == '__main__':
    unittest.main()
