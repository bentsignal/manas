#!/usr/bin/env python3
"""Check the released prefix against source display lines, not the reported corpus total."""
from release_store import read_release
from source_evidence import verify_source_evidence
import json
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent.parent
rows = [json.loads(l) for l in read_release(root).splitlines() if l.strip()]
gap_path = root/'corpus/source-gaps.json'
gaps = json.loads(gap_path.read_text()) if gap_path.exists() else []
gap_ids = {}
positions = {r['id']:i for i,r in enumerate(rows)}
for gap in gaps:
    assert gap['status'] == 'unresolved' and gap.get('evidence'), 'Undocumented source gap'
    assert gap['after_id'] in positions and positions.get(gap['before_id']) == positions[gap['after_id']]+1, 'Gap marker is not between adjacent translations'
    assert [s['id'] for s in gap['source']['segments']] == gap['source_line_ids'], 'Gap segment mismatch'
    for segment in gap['source']['segments']:
        assert segment['id'] not in gap_ids, 'Duplicate gap fragment'
        gap_ids[segment['id']] = (gap,segment)
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
    assert not set(ids).intersection(gap_ids), 'Gap fragment counted as translated'
    assert [s['id'] for s in row['source']['segments']] == ids, 'Segment/ID mismatch'
    by_source[row['source_id']].extend(ids)
covered = omitted = damaged = 0
for source_id, published in by_source.items():
    assert len(set(published)) == len(published), 'Source display line repeated'
    raw = [json.loads(l) for l in (root/f'sources/extracted/{source_id}.lines.jsonl').open()]
    extracted = {r['id']:r for r in raw}
    for row in rows:
        if row['source_id'] == source_id:
            verify_source_evidence(row, extracted)
    index = {r['id']:i for i,r in enumerate(raw)}
    region = raw[index[published[0]]:index[published[-1]]+1]
    expected = []
    for r in region:
        if r['text'].strip() == 'www.bizdin.kg': continue
        if r['id'] in exclusions:
            if exclusions[r['id']]['kind'] == 'unresolved_source':
                assert r['id'] in gap_ids, 'Unmarked unresolved source gap: '+r['id']
                gap, segment = gap_ids[r['id']]
                assert segment['raw'] == r['raw'] and segment['bbox'] == r['bbox'] and gap['source']['sha256'] == r['pdf_sha256'], 'Gap provenance mismatch'
                damaged += 1
                continue
            omitted += 1
            continue
        expected.append(r['id'])
    if expected != published:
        missing = list(set(expected)-set(published))[:10]
        raise AssertionError(f'{source_id}: unexplained missing/reordered source lines: {missing}')
    covered += len(published)
assert damaged == len(gap_ids), 'Gap registry contains fragments outside accounted source'
print(json.dumps(dict(released_rows=len(rows),source_display_lines=covered,documented_nonverse_exclusions=omitted,unresolved_source_regions=len(gaps),unresolved_source_fragments=damaged,scope='released source range only; marked gaps are NOT translations; full corpus not reconciled')))
