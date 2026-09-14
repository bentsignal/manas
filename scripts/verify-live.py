#!/usr/bin/env python3
"""Verify the published poem against the local compiled release; print paired counts."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = (sys.argv[1] if len(sys.argv) > 1 else
        'https://manas-every-line.bentsignal.chatgpt.site').rstrip('/')
WORDS = re.compile(r"[^\W\d_]+(?:[’'-][^\W\d_]+)*")


def fetch(path):
    request = urllib.request.Request(BASE + path,
                                     headers={'User-Agent': 'Manas publication verification'})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def read_chunk(digest):
    if not re.fullmatch(r'[a-f0-9]{64}', digest):
        raise ValueError('Invalid chunk digest')
    raw = fetch('/text/chunks/' + digest + '.json')
    if hashlib.sha256(raw).hexdigest() != digest:
        raise ValueError('Published chunk does not match its digest: ' + digest)
    return json.loads(raw)


local = json.loads((ROOT / 'public/text/manifest.json').read_text())
live = json.loads(fetch('/text/manifest.json'))
if live != local:
    raise ValueError('Live manifest does not yet match the compiled release')
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    rows = [row for chunk in pool.map(read_chunk, live['chunks']) for row in chunk]
if len(rows) != live['released']:
    raise ValueError('Published verse count mismatch')
if [row['ordinal'] for row in rows] != list(range(1, len(rows) + 1)):
    raise ValueError('Published ordinals contain a gap, duplicate, or ordering error')
if len({row['id'] for row in rows}) != len(rows):
    raise ValueError('Published source IDs contain duplicates')
word_count = sum(len(WORDS.findall(row['en'])) for row in rows)
if word_count != live['englishWords']:
    raise ValueError('Published English word count mismatch')
gap_count = sum(bool(row.get('gapBefore')) for row in rows)
if gap_count != live['sourceGaps']:
    raise ValueError('Published source gap markers mismatch')
print(json.dumps({'url': BASE, 'version': live['version'], 'live_draft_lines': len(rows),
                  'live_english_words': word_count, 'unresolved_source_regions': gap_count,
                  'last_source_id': rows[-1]['id'] if rows else None}))
