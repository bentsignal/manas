#!/usr/bin/env python3
"""Apply reviewed English batch corrections to existing release rows."""
import argparse
import json
from pathlib import Path

from release_store import read_release, write_release


parser = argparse.ArgumentParser()
parser.add_argument('batch', type=Path, nargs='+')
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
rows = [json.loads(line) for line in read_release(root).splitlines() if line.strip()]
by_id = {row['id']: row for row in rows}
assert len(by_id) == len(rows), 'release contains repeated canonical row IDs'

changed = 0
reviewed = 0
for batch_path in args.batch:
    batch = json.loads(batch_path.read_text())
    review = batch.get('alignment_check') or {}
    method = review.get('method', '')
    assert method == 'same-agent source-English row comparison' or method.startswith(
        'source-English row semantic audit'
    ), f'{batch_path}: correction requires a source-English row audit'
    assert review.get('checked_by') and review.get('date')
    english = (root / batch['english']).read_text().splitlines()
    assert len(english) == len(batch['source_ids']) == review.get('rows'), (
        f'{batch_path}: reviewed/source/English row-count mismatch')
    for sid, en in zip(batch['source_ids'], english):
        assert sid in by_id, f'{batch_path}: row is not in the release: {sid}'
        assert en.strip(), f'{batch_path}: empty English row: {sid}'
        row = by_id[sid]
        assert row.get('source_line_ids', [row['id']])[0] == sid, (
            f'{batch_path}: canonical source ID mismatch: {sid}')
        if row['en'] != en:
            row['en'] = en
            changed += 1
        row['translation_review'] = review
        reviewed += 1

write_release(root, ''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
print(json.dumps({'changed': changed, 'reviewed': reviewed, 'total': len(rows)}))
