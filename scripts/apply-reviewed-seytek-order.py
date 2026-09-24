#!/usr/bin/env python3
"""Move reviewed two-column Seytek pages into printed reading order.

Only pages explicitly named on the command line are changed. Their visual
evidence must already be recorded in a repository file. A dry run is the
default; --apply writes batches, source-order overrides, and release shards.
"""
import argparse
import json
import re
from pathlib import Path

from release_store import read_release, write_release


ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--pages', nargs='+', type=int, required=True)
parser.add_argument('--evidence', required=True, help='Repository-relative visual review note')
parser.add_argument('--apply', action='store_true')
args = parser.parse_args()

pages = sorted(set(args.pages))
assert len(pages) == len(args.pages) and all(1 <= page <= 1172 for page in pages)
evidence_path = ROOT / args.evidence
assert evidence_path.is_file() and evidence_path.resolve().is_relative_to(ROOT)
evidence = evidence_path.read_text()
for page in pages:
    assert re.search(rf'\b(?:page|p)\s*0*{page}\b', evidence, re.I), (
        f'Evidence file does not name page {page}')

source = {row['id']: row for line in
          (ROOT / 'sources/extracted/seytek-2012.lines.jsonl').open()
          if (row := json.loads(line))}
release = [json.loads(line) for line in read_release(ROOT).splitlines()]
assert all(row['ordinal'] == i + 1 for i, row in enumerate(release))
overrides_path = ROOT / 'corpus/source-order-overrides.json'
overrides = json.loads(overrides_path.read_text())
seytek_overrides = overrides.setdefault('seytek-2012', {})
batch_dir = ROOT / 'corpus/batches'
all_batches = {path: json.loads(path.read_text())
               for path in batch_dir.glob('pages-seytek-*.json')}
batch_edits = {}
english_edits = {}
summary = []

for page in pages:
    key = str(page)
    assert key not in seytek_overrides, f'Already reviewed: {page}'
    batch_path = batch_dir / f'pages-seytek-{page:04}.json'
    batch = all_batches[batch_path]
    old_ids = batch['source_ids']
    assert len(old_ids) == len(set(old_ids)) and len(old_ids) >= 2
    assert not batch.get('source_groups'), f'Grouped lines need manual review: {page}'
    assert all(source[sid]['page'] == page for sid in old_ids)
    blocks = {block: [sid for sid in old_ids if source[sid]['block'] == block]
              for block in (3, 2)}
    assert all(blocks.values()) and len(blocks[3]) + len(blocks[2]) == len(old_ids)
    assert old_ids == blocks[2] + blocks[3], f'Unexpected old order: {page}'
    assert max(source[sid]['bbox']['xMin'] for sid in blocks[3]) < 250
    assert min(source[sid]['bbox']['xMin'] for sid in blocks[2]) >= 250
    new_ids = blocks[3] + blocks[2]
    english_path = ROOT / batch['english']
    old_english = english_path.read_text().splitlines()
    assert len(old_english) == len(old_ids) and all(old_english)
    english_by_id = dict(zip(old_ids, old_english))
    new_english = [english_by_id[sid] for sid in new_ids]

    positions = [i for i, row in enumerate(release) if row['id'] in set(old_ids)]
    assert positions == list(range(positions[0], positions[0] + len(old_ids)))
    assert [release[i]['id'] for i in positions] == old_ids
    rows_by_id = {release[i]['id']: release[i] for i in positions}
    assert all(rows_by_id[sid]['en'] == english_by_id[sid] for sid in old_ids)
    for i, sid in zip(positions, new_ids):
        release[i] = rows_by_id[sid]
        release[i]['ordinal'] = i + 1

    old_last, new_last = old_ids[-1], new_ids[-1]
    for path, other in all_batches.items():
        if other.get('after_id') == old_last:
            other['after_id'] = new_last
            batch_edits[path] = other
    batch['source_ids'] = new_ids
    batch['transcription_check']['details'] = (
        f'Printed left block 3 precedes right block 2; visually reviewed in '
        f'{args.evidence}. All {len(new_ids)} source IDs remain paired with '
        'their prior English lines. Nonverse exclusions are unchanged.')
    batch_edits[batch_path] = batch
    english_edits[english_path] = '\n'.join(new_english) + '\n'
    seytek_overrides[key] = {
        'blocks': [3, 2],
        'evidence': f'Printed left/right columns and neighboring joins reviewed in {args.evidence}.'
    }
    summary.append({'page': page, 'rows': len(new_ids),
                    'first_ordinal': positions[0] + 1,
                    'last_ordinal': positions[-1] + 1,
                    'old_last': old_last, 'new_last': new_last})

assert all(row['ordinal'] == i + 1 for i, row in enumerate(release))
print(json.dumps({'apply': args.apply, 'pages': summary,
                  'release_rows': len(release)}, indent=2))
if args.apply:
    for path, batch in batch_edits.items():
        path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n')
    for path, english in english_edits.items():
        path.write_text(english)
    overrides_path.write_text(json.dumps(overrides, ensure_ascii=False, indent=2) + '\n')
    write_release(ROOT, ''.join(json.dumps(row, ensure_ascii=False) + '\n'
                                for row in release))
