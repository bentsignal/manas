"""Content-verified JSONL shards with an atomic index checkpoint."""
import hashlib
import json
from pathlib import Path
import re


def iter_release(root):
    """Yield verified release rows without materializing the full provenance corpus."""
    directory = Path(root) / 'corpus/release'
    index = json.loads((directory / 'index.json').read_text())
    if index['format'] != 'manas-release-shards-v1':
        raise ValueError('Unsupported release storage format')
    digest = hashlib.sha256()
    total = 0
    for chunk in index['chunks']:
        name = chunk['file']
        if not re.fullmatch(r'[a-f0-9]{64}\.jsonl', name):
            raise ValueError('Invalid release shard filename')
        raw = (directory / 'chunks' / name).read_bytes()
        if hashlib.sha256(raw).hexdigest() + '.jsonl' != name:
            raise ValueError('Release shard digest mismatch')
        digest.update(raw)
        lines = raw.splitlines()
        if not raw.endswith(b'\n') or len(lines) != chunk['rows']:
            raise ValueError('Release shard row count mismatch')
        for line in lines:
            total += 1
            yield json.loads(line)
    if total != index['rows'] or digest.hexdigest() != index['sha256']:
        raise ValueError('Release checkpoint mismatch')


def read_release(root):
    directory = Path(root) / 'corpus/release'
    index = json.loads((directory / 'index.json').read_text())
    if index['format'] != 'manas-release-shards-v1':
        raise ValueError('Unsupported release storage format')
    texts = []
    total = 0
    for chunk in index['chunks']:
        name = chunk['file']
        if not re.fullmatch(r'[a-f0-9]{64}\.jsonl', name):
            raise ValueError('Invalid release shard filename')
        raw = (directory / 'chunks' / name).read_bytes()
        if hashlib.sha256(raw).hexdigest() + '.jsonl' != name:
            raise ValueError('Release shard digest mismatch')
        text = raw.decode('utf-8')
        if not text.endswith('\n') or len(text.splitlines()) != chunk['rows']:
            raise ValueError('Release shard row count mismatch')
        texts.append(text)
        total += chunk['rows']
    text = ''.join(texts)
    if total != index['rows'] or hashlib.sha256(text.encode()).hexdigest() != index['sha256']:
        raise ValueError('Release checkpoint mismatch')
    return text


def write_release(root, text, chunk_size=1000):
    if chunk_size < 1:
        raise ValueError('Positive shard size required')
    lines = text.splitlines(keepends=True)
    if any(not line.endswith('\n') or not line.strip() for line in lines):
        raise ValueError('Release must contain newline-terminated JSONL rows')
    directory = Path(root) / 'corpus/release'
    chunks_dir = directory / 'chunks'
    chunks_dir.mkdir(parents=True, exist_ok=True)
    chunks = []
    for start in range(0, len(lines), chunk_size):
        selected = lines[start:start + chunk_size]
        raw = ''.join(selected).encode()
        name = hashlib.sha256(raw).hexdigest() + '.jsonl'
        destination = chunks_dir / name
        if not destination.exists() or destination.read_bytes() != raw:
            temporary = destination.with_suffix('.tmp')
            temporary.write_bytes(raw)
            temporary.replace(destination)
        chunks.append({'file': name, 'rows': len(selected)})
    index = {'format': 'manas-release-shards-v1', 'rows': len(lines),
             'sha256': hashlib.sha256(text.encode()).hexdigest(), 'chunks': chunks}
    temporary = directory / 'index.json.tmp'
    temporary.write_text(json.dumps(index, indent=2) + '\n')
    temporary.replace(directory / 'index.json')
    # Only the parent writes releases; all consumers run after this checkpoint.
    # Before the index replacement every prior shard remains available.
    current = {chunk['file'] for chunk in chunks}
    for old in chunks_dir.glob('*.jsonl'):
        if old.name not in current:
            old.unlink()
