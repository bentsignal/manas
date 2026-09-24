#!/usr/bin/env python3
"""Append a manually translated, visually checked page batch without renumbering prior work."""
import argparse, json
from pathlib import Path
from release_store import read_release, write_release
from source_evidence import descriptor_groups, build_source_evidence
from source_order import ordered_source_rows

parser = argparse.ArgumentParser()
parser.add_argument('batch', type=Path, nargs='+', help='JSON batch descriptor(s) with explicit checked source IDs')
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
existing = [json.loads(line) for line in read_release(root).splitlines() if line.strip()]
seen = {sid for row in existing for sid in row.get('source_line_ids', [row['id']])}
appended = 0
for batch_path in args.batch:
    batch = json.loads(batch_path.read_text())
    assert existing[-1]['id'] == batch['after_id'], f'{batch_path}: batch does not follow the current checkpoint'
    assert batch['transcription_check']['method'] == 'visual-pdf-comparison'
    assert batch['transcription_check']['checked_by'] and batch['transcription_check']['date']
    groups, joiners = descriptor_groups(batch)
    contributing_ids = [sid for group in groups.values() for sid in group]
    requested = set(contributing_ids)
    extracted = {}
    extraction_order = {}
    extracted_rows = ordered_source_rows(root, [json.loads(line) for line in
        (root / batch['extraction']).open()])
    for index, row in enumerate(extracted_rows):
        extraction_order[row['id']] = index
        if row['id'] in requested:
            assert row['id'] not in extracted, f'{batch_path}: repeated extracted source fragment'
            extracted[row['id']] = row
    source = {sid: extracted[sid] for sid in contributing_ids if sid in extracted}
    assert list(source) == contributing_ids, f'{batch_path}: missing or reordered source fragments'
    anchors = [extraction_order[groups[sid][0]] for sid in batch['source_ids']]
    assert anchors == sorted(anchors) and len(anchors) == len(set(anchors)), f'{batch_path}: reordered canonical source rows'
    english = (root / batch['english']).read_text().splitlines()
    assert len(english) == len(batch['source_ids']), f'{batch_path}: translation/source count mismatch'
    assert len(set(batch['source_ids'])) == len(english), f'{batch_path}: repeated source ID'
    assert not seen.intersection(contributing_ids), f'{batch_path}: previously translated source ID'
    notes = batch.get('notes', {})
    new = []
    for sid, en in zip(batch['source_ids'], english):
        assert en.strip(), f'{batch_path}: empty translation'
        record = build_source_evidence(sid, groups[sid], joiners[sid], source,
                                       batch['source_url'], notes.get(sid))
        assert record['source']['page'] in batch['transcription_check']['pdf_pages']
        record.update(ordinal=len(existing)+len(new)+1, part=batch['part'], en=en,
            transcription_status='verified', transcription_evidence=batch['transcription_check'],
            lineation_status='provisional', status='draft',
            translation_method='AI translation directly from Kyrgyz; lexical checks; no independent specialist review')
        new.append(record)
    existing.extend(new)
    seen.update(contributing_ids)
    appended += len(new)
# Write atomically; interrupted imports cannot leave a half-written release.
write_release(root, ''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in existing))
print(json.dumps(dict(appended=appended,total=len(existing),last_id=existing[-1]['id'])))
