"""Apply visually reviewed page order without altering raw PDF extraction records."""
import json
from pathlib import Path


def ordered_source_rows(root, rows):
    """Return extraction rows in source reading order, keeping every stable ID."""
    path = Path(root) / 'corpus/source-order-overrides.json'
    if not path.exists():
        return rows
    overrides = json.loads(path.read_text())
    ordered = list(rows)
    positions = {}
    for index, row in enumerate(rows):
        positions.setdefault((row['source_id'], str(row['page'])), []).append(index)
    source_ids = {row['source_id'] for row in rows}
    for source_id, pages in overrides.items():
        if source_id not in source_ids:
            continue
        for page, override in pages.items():
            selected = positions.get((source_id, page))
            assert selected, f'Source-order override names an absent page: {source_id}:{page}'
            assert selected == list(range(selected[0], selected[-1] + 1)), (
                f'Source page is not contiguous: {source_id}:{page}')
            blocks = override['blocks']
            assert len(blocks) == len(set(blocks)) and len(blocks) >= 2
            assert override.get('evidence'), 'Source-order override requires visual evidence'
            by_block = {block: [rows[index] for index in selected
                                if rows[index]['block'] == block] for block in blocks}
            assert all(by_block.values()), f'Empty block in source-order override: {source_id}:{page}'
            replace_at = [index for index in selected if rows[index]['block'] in blocks]
            replacement = [row for block in blocks for row in by_block[block]]
            assert len(replace_at) == len(replacement)
            for index, row in zip(replace_at, replacement):
                ordered[index] = row
    assert len(ordered) == len(rows)
    assert len({row['id'] for row in ordered}) == len(ordered), 'Repeated source ID'
    return ordered
