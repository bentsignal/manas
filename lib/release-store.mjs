import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const sha = raw => createHash('sha256').update(raw).digest('hex');
const loadIndex = async root => {
  const directory = new URL('corpus/release/', root);
  const index = JSON.parse(await readFile(new URL('index.json', directory), 'utf8'));
  if (index.format !== 'manas-release-shards-v1') throw Error('Unsupported release storage format');
  return {directory,index};
};
export async function readReleaseRows(root) {
  const {directory,index}=await loadIndex(root);
  const rows=[];
  const digest=createHash('sha256');
  let total=0;
  for(const chunk of index.chunks){
    if(!/^[a-f0-9]{64}\.jsonl$/.test(chunk.file))throw Error('Invalid release shard filename');
    const raw=await readFile(new URL(`chunks/${chunk.file}`,directory));
    if(`${sha(raw)}.jsonl`!==chunk.file)throw Error('Release shard digest mismatch');
    const text=raw.toString('utf8');
    if(!text.endsWith('\n')||text.split('\n').length-1!==chunk.rows)throw Error('Release shard row count mismatch');
    for(const line of text.split('\n'))if(line)rows.push(JSON.parse(line));
    digest.update(raw);
    total+=chunk.rows;
  }
  if(total!==index.rows||digest.digest('hex')!==index.sha256)throw Error('Release checkpoint mismatch');
  return {rows,sha256:index.sha256};
}
export async function readReleaseText(root) {
  const {directory,index}=await loadIndex(root);
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
