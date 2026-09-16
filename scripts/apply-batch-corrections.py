#!/usr/bin/env python3
"""Apply reviewed English batch corrections to existing release rows."""
import argparse
import json
import re
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
    english = (root / batch['english']).read_text().splitlines()
    assert len(english) == len(batch['source_ids']), (
        f'{batch_path}: source/English row-count mismatch')
    base_is_semantic = method == 'same-agent source-English row comparison' or method.startswith(
        'source-English row semantic audit'
    )
    top_review_rows = review.get('rows', review.get('rows_checked'))
    is_full_review = base_is_semantic and top_review_rows == len(english)
    targeted_reviews = [
        value for key, value in review.items()
        if 'targeted_qa' in key and isinstance(value, dict)
    ]
    if base_is_semantic and top_review_rows and not is_full_review:
        targeted_reviews.insert(0, review)
    assert is_full_review or targeted_reviews, (
        f'{batch_path}: correction requires a source-English row audit')
    if is_full_review:
        assert review.get('checked_by') and review.get('date')
        assert len(english) == review.get('rows', review.get('rows_checked')), (
            f'{batch_path}: reviewed/source/English row-count mismatch')
        reviewed += len(english)
    else:
        for targeted in targeted_reviews:
            assert targeted.get('checked_by') and targeted.get('date')
            assert len(targeted['page_range']) == 2
            assert targeted.get('rows_checked', 0) > 0
            reviewed += targeted['rows_checked']
    for sid, en in zip(batch['source_ids'], english):
        assert sid in by_id, f'{batch_path}: row is not in the release: {sid}'
        assert en.strip(), f'{batch_path}: empty English row: {sid}'
        row = by_id[sid]
        assert row.get('source_line_ids', [row['id']])[0] == sid, (
            f'{batch_path}: canonical source ID mismatch: {sid}')
        if row['en'] != en:
            if not is_full_review:
                match = re.search(r':p(\d{4}):', sid)
                page = int(match.group(1)) if match else -1
                matching_reviews = [
                    targeted for targeted in targeted_reviews
                    if (targeted['page_range'][0] <= page <= targeted['page_range'][1]
                        or sid in targeted.get('changed_source_ids', []))
                ]
                assert matching_reviews, (
                    f'{batch_path}: changed row lies outside targeted audit: {sid}')
            row['en'] = en
            changed += 1
            row['translation_review'] = (
                review if is_full_review else matching_reviews[-1])
        elif is_full_review:
            row['translation_review'] = review

write_release(root, ''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
print(json.dumps({'changed': changed, 'reviewed': reviewed, 'total': len(rows)}))
