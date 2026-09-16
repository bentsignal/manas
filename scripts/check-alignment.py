#!/usr/bin/env python3
"""Check the released prefix against source display lines, not the reported corpus total."""
from release_store import read_release
from source_evidence import verify_source_evidence, verify_gap_segment
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
    assert ((gap.get('kind') == 'content_withheld' and gap['status'] == 'withheld') or (gap.get('kind') != 'content_withheld' and gap['status'] == 'unresolved')) and gap.get('evidence'), 'Undocumented source gap'
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
        assert item.get('kind') in ['heading','prose','overlap','unresolved_source','content_withheld'], 'Unclassified exclusion'
        exclusions[item['id']] = item
by_source = defaultdict(list)
for row in rows:
    ids = row.get('source_line_ids', [row['id']])
    assert not set(ids).intersection(gap_ids), 'Gap fragment counted as translated'
    assert [s['id'] for s in row['source']['segments']] == ids, 'Segment/ID mismatch'
    by_source[row['source_id']].extend(ids)
covered = omitted = damaged = withheld = 0
for source_id, published in by_source.items():
    assert len(set(published)) == len(published), 'Source display line repeated'
    raw = [json.loads(l) for l in (root/f'sources/extracted/{source_id}.lines.jsonl').open()]
    extracted = {r['id']:r for r in raw}
    for row in rows:
        if row['source_id'] == source_id:
            verify_source_evidence(row, extracted)
    index = {r['id']:i for i,r in enumerate(raw)}
    anchors = [index[row.get('source_line_ids', [row['id']])[0]]
               for row in rows if row['source_id'] == source_id]
    assert anchors == sorted(anchors), 'Translated source anchors are reordered'
    # Include registered leading/trailing gaps for a source even when no
    # translated row exists on the damaged or missing opening/closing leaf.
    gap_positions = [index[ident] for ident, (gap, _) in gap_ids.items()
                     if gap['source_id'] == source_id and ident in index]
    bounds = [index[published[0]], index[published[-1]], *gap_positions]
    region = raw[min(bounds):max(bounds)+1]
    expected = []
    for r in region:
        if r['text'].strip() == 'www.bizdin.kg': continue
        if r['id'] in exclusions:
            if exclusions[r['id']]['kind'] in ['unresolved_source','content_withheld']:
                assert r['id'] in gap_ids, 'Unmarked unresolved source gap: '+r['id']
                gap, segment = gap_ids[r['id']]
                assert (exclusions[r['id']]['kind'] == 'content_withheld') == (gap.get('kind') == 'content_withheld'), 'Withheld category mismatch'
                verify_gap_segment(gap, segment, r)
                if gap.get('kind') == 'content_withheld': withheld += 1
                else: damaged += 1
                continue
            omitted += 1
            continue
        expected.append(r['id'])
    # Explicit source groups can join a drop cap or continuation fragment that
    # the PDF extractor emitted after the surrounding text block. Preserve the
    # visually verified group order while requiring identical source coverage.
    if set(expected) != set(published):
        missing = list(set(expected)-set(published))[:10]
        raise AssertionError(f'{source_id}: unexplained missing source lines: {missing}')
    covered += len(published)
assert damaged + withheld == len(gap_ids), 'Gap registry contains fragments outside accounted source'
print(json.dumps(dict(released_rows=len(rows),source_display_lines=covered,documented_nonverse_exclusions=omitted,unresolved_source_regions=sum(g.get('kind')!='content_withheld' for g in gaps),unresolved_source_fragments=damaged,withheld_source_regions=sum(g.get('kind')=='content_withheld' for g in gaps),withheld_source_fragments=withheld,scope='released source range only; marked gaps are NOT translations; full corpus not reconciled')))
