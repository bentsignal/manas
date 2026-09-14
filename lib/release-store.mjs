import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const sha = raw => createHash('sha256').update(raw).digest('hex');
export async function readReleaseText(root) {
  const directory = new URL('corpus/release/', root);
  const index = JSON.parse(await readFile(new URL('index.json', directory), 'utf8'));
  if (index.format !== 'manas-release-shards-v1') throw Error('Unsupported release storage format');
  const buffers = [];
  let total = 0;
  for (const chunk of index.chunks) {
    if (!/^[a-f0-9]{64}\.jsonl$/.test(chunk.file)) throw Error('Invalid release shard filename');
    const raw = await readFile(new URL(`chunks/${chunk.file}`, directory));
    if (`${sha(raw)}.jsonl` !== chunk.file) throw Error('Release shard digest mismatch');
    const text = raw.toString('utf8');
    if (!text.endsWith('\n') || text.split('\n').length - 1 !== chunk.rows) throw Error('Release shard row count mismatch');
    buffers.push(raw);
    total += chunk.rows;
  }
  const raw = Buffer.concat(buffers);
  if (total !== index.rows || sha(raw) !== index.sha256) throw Error('Release checkpoint mismatch');
  return raw.toString('utf8');
}
