#!/usr/bin/env python3
"""Append a manually translated, visually checked page batch without renumbering prior work."""
import argparse, json
from pathlib import Path
from release_store import read_release, write_release
from source_evidence import descriptor_groups, build_source_evidence

parser = argparse.ArgumentParser()
parser.add_argument('batch', type=Path, help='JSON batch descriptor with explicit checked source IDs')
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
batch = json.loads(args.batch.read_text())
existing = [json.loads(line) for line in read_release(root).splitlines() if line.strip()]
assert existing[-1]['id'] == batch['after_id'], 'Batch does not follow the current checkpoint'
assert batch['transcription_check']['method'] == 'visual-pdf-comparison'
assert batch['transcription_check']['checked_by'] and batch['transcription_check']['date']
groups, joiners = descriptor_groups(batch)
contributing_ids = [sid for group in groups.values() for sid in group]
requested = set(contributing_ids)
source = {}
for line in (root / batch['extraction']).open():
    row = json.loads(line)
    if row['id'] in requested:
        source[row['id']] = row
assert list(source) == contributing_ids, 'Missing or reordered source fragments'
english = (root / batch['english']).read_text().splitlines()
assert len(english) == len(batch['source_ids']), 'Translation/source count mismatch'
assert len(set(batch['source_ids'])) == len(english), 'Repeated source ID'
seen = {sid for row in existing for sid in row.get('source_line_ids', [row['id']])}
assert not seen.intersection(contributing_ids), 'Previously translated source ID'
notes = batch.get('notes', {})
new = []
for sid, en in zip(batch['source_ids'], english):
    assert en.strip(), 'Empty translation'
    record = build_source_evidence(sid, groups[sid], joiners[sid], source,
                                   batch['source_url'], notes.get(sid))
    assert record['source']['page'] in batch['transcription_check']['pdf_pages']
    record.update(ordinal=len(existing)+len(new)+1, part=batch['part'], en=en,
        transcription_status='verified', transcription_evidence=batch['transcription_check'],
        lineation_status='provisional', status='draft',
        translation_method='AI translation directly from Kyrgyz; lexical checks; no independent specialist review')
    new.append(record)
# Write atomically; interrupted imports cannot leave a half-written release.
write_release(root, ''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in existing+new))
print(json.dumps(dict(appended=len(new),total=len(existing)+len(new),last_id=new[-1]['id'])))
