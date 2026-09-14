#!/usr/bin/env python3
"""Check the released prefix against source display lines, not the reported corpus total."""
import json
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent.parent
rows = [json.loads(l) for l in (root/'corpus/release.jsonl').read_text().splitlines() if l.strip()]
exclusions = {}
for path in (root/'corpus/batches').glob('*.json'):
    descriptor = json.loads(path.read_text())
    for item in descriptor.get('excluded_source_ids', []):
        assert isinstance(item, dict) and item.get('id') and item.get('reason'), 'Invalid exclusion record'
        assert item.get('kind') in ['heading','prose','unresolved_source'], 'Unclassified exclusion'
        exclusions[item['id']] = item
by_source = defaultdict(list)
for row in rows:
    ids = row.get('source_line_ids', [row['id']])
    assert [s['id'] for s in row['source']['segments']] == ids, 'Segment/ID mismatch'
    assert ' '.join(s['raw'] for s in row['source']['segments']) == row['ky'], 'Undocumented source alteration'
    by_source[row['source_id']].extend(ids)
covered = omitted = 0
for source_id, published in by_source.items():
    assert len(set(published)) == len(published), 'Source display line repeated'
    raw = [json.loads(l) for l in (root/f'sources/extracted/{source_id}.lines.jsonl').open()]
    index = {r['id']:i for i,r in enumerate(raw)}
    region = raw[index[published[0]]:index[published[-1]]+1]
    expected = []
    for r in region:
        if r['text'].strip() == 'www.bizdin.kg': continue
        if r['id'] in exclusions:
            assert exclusions[r['id']]['kind'] != 'unresolved_source', 'Unresolved source gap blocks publication beyond '+r['id']
            omitted += 1
            continue
        expected.append(r['id'])
    if expected != published:
        missing = list(set(expected)-set(published))[:10]
        raise AssertionError(f'{source_id}: unexplained missing/reordered source lines: {missing}')
    covered += len(published)
print(json.dumps(dict(released_rows=len(rows),source_display_lines=covered,documented_nonverse_exclusions=omitted,scope='released prefix only; full corpus not reconciled')))
