#!/usr/bin/env python3
"""Account for every extracted display line in each saved page batch.

This audits local batch coverage, not original archival completeness or translation quality.
Overlapping prefix descriptors must have identical English for shared source IDs.
"""
from release_store import iter_release
from source_evidence import descriptor_groups, build_source_evidence
import argparse
import json
import re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--write-progress", action="store_true")
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
sources = {}
translations = {}
fragment_owners = {}
translation_evidence = {}
reports = []
covered_pages = {}
unresolved = set()
withheld = set()
for path in sorted((root/'corpus/batches').glob('pages-*.json')):
    b = json.loads(path.read_text())
    extraction = b['extraction']
    if extraction not in sources:
        sources[extraction] = [json.loads(s) for s in (root/extraction).read_text().splitlines()]
    english = (root/b['english']).read_text().splitlines()
    ids = b['source_ids']
    groups, joiners = descriptor_groups(b)
    contributing_ids = [sid for group in groups.values() for sid in group]
    extracted = {r['id']: r for r in sources[extraction]}
    assert set(b.get('notes',{})).issubset(ids), f'{path.name}: note references an untranslated ID'
    assert len(english) == len(ids) and all(s.strip() for s in english), f'{path.name}: empty or misaligned English'
    assert len(ids) == len(set(ids)), f'{path.name}: duplicated IDs'
    pages = b['transcription_check']['pdf_pages']
    source_id = sources[extraction][0]['source_id']
    covered_pages.setdefault(source_id, set()).update(pages)
    exclusions = b.get('excluded_source_ids', [])
    excluded = {x['id']: x for x in exclusions}
    # A registered damaged or missing boundary leaf can sit immediately before
    # or after the translated page range. Keep those explicit positions in the
    # audited region instead of forcing them into a translated page number.
    region = [r for r in sources[extraction]
              if r['page'] in pages or r['id'] in excluded]
    unresolved.update(x['id'] for x in exclusions if x.get('kind') == 'unresolved_source')
    withheld.update(x['id'] for x in exclusions if x.get('kind') == 'content_withheld')
    assert len(excluded) == len(exclusions), f'{path.name}: duplicate exclusions'
    for item in exclusions:
        assert item.get('kind') in ['heading','prose','overlap','unresolved_source','content_withheld'] and item.get('reason'), f'{path.name}: unjustified exclusion'
    assert set(excluded).issubset({r['id'] for r in region}), f'{path.name}: exclusion outside selected pages'
    expected = [r['id'] for r in region if r['id'] not in excluded and r['text'].strip() != 'www.bizdin.kg']
    assert set(expected) == set(contributing_ids), f'{path.name}: source gap or unexpected fragment'
    positions = {sid:index for index,sid in enumerate(expected)}
    anchors = [positions[groups[sid][0]] for sid in ids]
    assert anchors == sorted(anchors) and len(anchors) == len(set(anchors)), f'{path.name}: reordered canonical rows'
    for sid, en in zip(ids, english):
        evidence = build_source_evidence(sid, groups[sid], joiners[sid], extracted,
                                         b['source_url'], b.get('notes', {}).get(sid))
        signature = (tuple(groups[sid]), tuple(joiners[sid]), evidence['ky'])
        assert sid not in translation_evidence or translation_evidence[sid] == signature, f'{path.name}: conflicting duplicate evidence {sid}'
        translation_evidence[sid] = signature
        for fragment in groups[sid]:
            assert fragment not in fragment_owners or fragment_owners[fragment] == sid, f'{path.name}: conflicting fragment ownership {fragment}'
            fragment_owners[fragment] = sid
        assert sid not in translations or translations[sid] == en, f'{path.name}: conflicting duplicate {sid}'
        translations[sid] = en
    reports.append({'batch':path.name,'verse_display_rows':len(ids),'translated_source_fragments':len(contributing_ids),'excluded_nonverse_rows':sum(x['kind'] in ['heading','prose'] for x in exclusions),'withheld_source_fragments':sum(x['kind']=='content_withheld' for x in exclusions),'unresolved_source_fragments':sum(x['kind']=='unresolved_source' for x in exclusions)})
print(json.dumps({'scope':'Saved page batches only; opening pilot is separate. Display rows are not certified archival verses.','batches':reports,'unique_translated_display_rows':len(translations),'unique_translated_source_fragments':len(fragment_owners),'full_source_reconciled':False},indent=2))

if args.write_progress:
    opening = []
    released_rows = 0
    released_words = 0
    for row in iter_release(root):
        released_rows += 1
        released_words += len(re.findall(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*", row['en']))
        if not any(sid in fragment_owners for sid in row.get('source_line_ids', [row['id']])):
            opening.append(row)
    for r in opening:
        covered_pages.setdefault(r['source_id'],set()).add(r['source']['page'])
    ranges_by_source = {}
    for source_id, pages in covered_pages.items():
        ranges = []
        for page in sorted(pages):
            if ranges and page == ranges[-1][1]+1: ranges[-1][1] = page
            else: ranges.append([page,page])
        ranges_by_source[source_id] = ranges
    path = root/'corpus/draft-progress.json'
    progress = json.loads(path.read_text()) if path.exists() else {}
    words = lambda text: len(re.findall(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*",text))
    progress.update(saved_draft_rows=len(translations)+len(opening), saved_draft_english_words=sum(words(en) for en in translations.values())+sum(words(r['en']) for r in opening), released_draft_rows=released_rows, released_english_words=released_words, word_count_method='Alphabetic English words; internal apostrophes/hyphens retained. Notes, headings, source markers and Kyrgyz excluded.', saved_page_ranges=ranges_by_source.get('manas-2010',[]), saved_page_ranges_scope='Legacy field: manas-2010 only. Use saved_page_ranges_by_source for every volume.', saved_page_ranges_by_source=ranges_by_source, unresolved_source_regions=sorted(unresolved), withheld_source_fragments=sorted(withheld), full_source_reconciled=False, complete=False)
    path.write_text(json.dumps(progress,indent=2)+'\n')
