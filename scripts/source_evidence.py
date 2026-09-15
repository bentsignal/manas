"""Verify readable transcription against preserved PDF extraction evidence."""
from extract import normalize


def source_joiners(ids, joiners=None, note=None):
    """Only documented empty joins may differ from ordinary inter-line spaces."""
    assert isinstance(ids, list) and ids and all(isinstance(s, str) and s for s in ids), 'Invalid source group'
    assert len(ids) == len(set(ids)), 'Repeated source fragment'
    if joiners is None:
        joiners = [' '] * (len(ids) - 1)
    assert isinstance(joiners, list) and len(joiners) == len(ids) - 1, 'Source joiner count mismatch'
    assert all(s in ('', ' ') for s in joiners), 'Invalid source joiner'
    if '' in joiners:
        assert isinstance(note, str) and note.strip(), 'Nondefault source join requires a material note'
    return joiners


def descriptor_groups(batch):
    """Validate ownership and expand one canonical ID per translated verse."""
    ids = batch['source_ids']
    assert isinstance(ids, list) and all(isinstance(s, str) and s for s in ids), 'Invalid canonical IDs'
    assert len(ids) == len(set(ids)), 'Repeated canonical source ID'
    groups = batch.get('source_groups', {})
    joins = batch.get('source_joiners', {})
    notes = batch.get('notes', {})
    assert isinstance(groups, dict) and isinstance(joins, dict), 'Invalid source group mapping'
    assert set(groups).issubset(ids) and set(joins).issubset(ids), 'Unknown source group key'
    assert set(notes).issubset(ids), 'Note references an untranslated ID'
    expanded, boundaries, owned = {}, {}, set()
    for sid in ids:
        group = groups.get(sid, [sid])
        boundaries[sid] = source_joiners(group, joins.get(sid), notes.get(sid))
        assert group[0] == sid, 'Canonical ID must be first source fragment'
        assert not owned.intersection(group), 'Duplicate source fragment ownership'
        owned.update(group)
        expanded[sid] = group
    return expanded, boundaries


def join_readable(readable, joiners):
    return readable[0] + ''.join(separator + text for separator, text in zip(joiners, readable[1:]))


def build_source_evidence(sid, ids, joiners, extracted, url, note=None):
    """Build and verify evidence without rewriting any extracted glyphs."""
    joiners = source_joiners(ids, joiners, note)
    assert sid == ids[0], 'Canonical ID must be first source fragment'
    originals = [extracted[ident] for ident in ids]
    first = originals[0]
    row = dict(id=sid, source_id=first['source_id'], source_line_ids=ids,
               ky=join_readable([r['text'] for r in originals], joiners),
               source=dict(url=url, page=first['page'], sha256=first['pdf_sha256'],
                           segments=[dict(id=r['id'], raw=r['raw'], bbox=r['bbox'],
                                          normalization=r.get('normalization', 'identity')) for r in originals]))
    if any(s != ' ' for s in joiners):
        row['source']['joiners'] = joiners
    if note is not None:
        row['note'] = note
    verify_source_evidence(row, extracted)
    return row


def verify_source_evidence(row, extracted):
    ids = row.get('source_line_ids', [row['id']])
    joiners = source_joiners(ids, row['source'].get('joiners'), row.get('note'))
    segments = row['source']['segments']
    assert [s['id'] for s in segments] == ids, 'Segment/ID mismatch'
    readable = []
    for segment in segments:
        original = extracted[segment['id']]
        assert original['source_id'] == row['source_id'], 'Wrong source witness'
        assert original['pdf_sha256'] == row['source']['sha256'], 'Source digest mismatch'
        assert original['page'] == row['source']['page'], 'Source page mismatch'
        assert segment['raw'] == original['raw'], 'Altered raw PDF text'
        assert segment['bbox'] == original['bbox'], 'Altered source coordinates'
        method = original.get('normalization', 'identity')
        assert method in ('identity', 'legacy-font-v1'), 'Unknown font normalization'
        assert segment.get('normalization', 'identity') == method, 'Undocumented font normalization'
        text = normalize(original['raw'], method == 'legacy-font-v1')
        assert original['text'] == text, 'Extraction normalization mismatch'
        readable.append(text)
    assert join_readable(readable, joiners) == row['ky'], 'Undocumented source alteration'


def verify_gap_segment(gap, segment, original):
    """Check withheld references by digest without copying the withheld wording."""
    from hashlib import sha256
    assert segment['id'] == original['id'], 'Gap ID mismatch'
    assert segment['bbox'] == original['bbox'] and gap['source']['sha256'] == original['pdf_sha256'], 'Gap provenance mismatch'
    if gap.get('kind') == 'content_withheld':
        assert gap['status'] == 'withheld', 'Invalid withheld status'
        assert 'raw' not in segment, 'Withheld wording must not be copied'
        assert segment.get('raw_sha256') == sha256(original['raw'].encode('utf-8')).hexdigest(), 'Withheld source digest mismatch'
    else:
        assert gap['status'] == 'unresolved' and segment['raw'] == original['raw'], 'Gap provenance mismatch'
