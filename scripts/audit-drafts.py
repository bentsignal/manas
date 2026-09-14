#!/usr/bin/env python3
"""Account for every extracted display line in each saved page batch.

This audits local batch coverage, not original archival completeness or translation quality.
Overlapping prefix descriptors must have identical English for shared source IDs.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
sources = {}
translations = {}
reports = []
for path in sorted((root/'corpus/batches').glob('pages-*.json')):
    b = json.loads(path.read_text())
    extraction = b['extraction']
    if extraction not in sources:
        sources[extraction] = [json.loads(s) for s in (root/extraction).read_text().splitlines()]
    english = (root/b['english']).read_text().splitlines()
    ids = b['source_ids']
    assert len(english) == len(ids) and all(s.strip() for s in english), f'{path.name}: empty or misaligned English'
    assert len(ids) == len(set(ids)), f'{path.name}: duplicated IDs'
    pages = b['transcription_check']['pdf_pages']
    region = [r for r in sources[extraction] if r['page'] in pages and r['text'].strip() != 'www.bizdin.kg']
    exclusions = b.get('excluded_source_ids', [])
    excluded = {x['id']: x for x in exclusions}
    assert len(excluded) == len(exclusions), f'{path.name}: duplicate exclusions'
    for item in exclusions:
        assert item.get('kind') in ['heading','prose','unresolved_source'] and item.get('reason'), f'{path.name}: unjustified exclusion'
    assert set(excluded).issubset({r['id'] for r in region}), f'{path.name}: exclusion outside selected pages'
    expected = [r['id'] for r in region if r['id'] not in excluded]
    assert expected == ids, f'{path.name}: source gap or reordered lines'
    for sid, en in zip(ids, english):
        assert sid not in translations or translations[sid] == en, f'{path.name}: conflicting duplicate {sid}'
        translations[sid] = en
    reports.append({'batch':path.name,'verse_display_rows':len(ids),'excluded_nonverse_rows':sum(x['kind']!='unresolved_source' for x in exclusions),'unresolved_source_fragments':sum(x['kind']=='unresolved_source' for x in exclusions)})
print(json.dumps({'scope':'Saved page batches only; opening pilot is separate. Display rows are not certified archival verses.','batches':reports,'unique_translated_display_rows':len(translations),'full_source_reconciled':False},indent=2))
