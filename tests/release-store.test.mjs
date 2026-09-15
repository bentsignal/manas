import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,readFile,writeFile,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import {readReleaseRows,readReleaseText} from '../lib/release-store.mjs';
const scripts=fileURLToPath(new URL('../scripts/',import.meta.url));
test('Python shard writes and JavaScript reads preserve Unicode, order, and checkpoint integrity',async()=>{
  const directory=await mkdtemp(join(tmpdir(),'manas-release-store-'));
  const root=pathToFileURL(directory+'/');
  const run=code=>execFileSync('python',['-c',`import sys\nsys.path.insert(0,sys.argv[1])\nfrom release_store import read_release,write_release\nfrom pathlib import Path\nroot=Path(sys.argv[2])\n${code}`,scripts,directory],{encoding:'utf8',stdio:['ignore','pipe','pipe']});
  const first='{"ordinal":1,"en":"A lion’s oath","ky":"Манас"}\n{"ordinal":2,"en":"A repeated oath"}\n';
  const text=first+'{"ordinal":3,"en":"A repeated oath"}\n';
  try {
    run(`write_release(root,${JSON.stringify(first)},chunk_size=2)`);
    const before=JSON.parse(await readFile(new URL('corpus/release/index.json',root),'utf8'));
    run(`write_release(root,${JSON.stringify(text)},chunk_size=2)`);
    const index=JSON.parse(await readFile(new URL('corpus/release/index.json',root),'utf8'));
    assert.equal(index.chunks[0].file,before.chunks[0].file);
    assert.equal(await readReleaseText(root),text);
    assert.deepEqual((await readReleaseRows(root)).rows,text.trim().split('\n').map(JSON.parse));
    assert.equal(run('print(read_release(root),end="")'),text);
    // An interrupted write before the index switch keeps the prior checkpoint readable.
    run(`from unittest.mock import patch\nwith patch.object(Path,'write_bytes',side_effect=OSError('interrupted')):\n try:\n  write_release(root,'{"ordinal":1,"en":"different"}\\n',chunk_size=2)\n except OSError:\n  pass\nassert read_release(root)==${JSON.stringify(text)}`);
    assert.equal(await readReleaseText(root),text);
    const shard=new URL('corpus/release/chunks/'+index.chunks[0].file,root);
    await writeFile(shard,'corrupt\n');
    await assert.rejects(()=>readReleaseText(root),/digest mismatch/);
    assert.throws(()=>run('read_release(root)'),/digest mismatch/);
  } finally {await rm(directory,{recursive:true,force:true});}
});
