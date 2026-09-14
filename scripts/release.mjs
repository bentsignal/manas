import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {validateRelease,sourceGapLabel} from '../lib/release.mjs';
const root=new URL('../',import.meta.url);
const read=async p=>JSON.parse(await readFile(new URL(p,root),'utf8'));
const target=await read('corpus/target.json');const sources=await read('sources/manifest.json');
const text=await readFile(new URL('corpus/release.jsonl',root),'utf8');
const rows=text.split('\n').filter(x=>x.trim()).map(x=>JSON.parse(x));
const gaps=await read('corpus/source-gaps.json');
const audit=validateRelease(rows,target,sources,gaps);
await writeFile(new URL('corpus/progress.json',root),JSON.stringify({
  released_draft_rows:audit.released,
  released_english_words:audit.englishWords,
  independently_reviewed:audit.reviewed,
  last_source_id:rows.at(-1)?.id??null,
  complete:audit.complete,
  full_source_reconciled:target.completeness_verified===true&&Boolean(target.reconciliation_evidence),
  background_translation_job:false,
  source_gaps:gaps.length,
  scope:'Compiled release candidate; production deployment must be verified separately.',
  gap_policy:'Publish readable drafts with explicit source-position marker; marker excluded from translated lines and English words; completeness blocked.'
},null,2)+'\n');
const gapBefore=new Map(gaps.map(g=>[g.before_id,sourceGapLabel(g)]));
const renderRows=rows.map(({id,ordinal,en})=>({id,ordinal,en,...(gapBefore.has(id)?{gapBefore:gapBefore.get(id)}:{})}));
const version=rows.length?createHash('sha256').update('reader-chunks-v2\n'+text+JSON.stringify(gaps)).digest('hex').slice(0,16):'audit-2026-09-14';
const directory=new URL(`public/text/${version}/`,root);await mkdir(directory,{recursive:true});
const chunkSize=256;
for(let i=0;i<rows.length;i+=chunkSize)await writeFile(new URL(`${i/chunkSize}.json`,directory),JSON.stringify(renderRows.slice(i,i+chunkSize))+'\n');
const manifest={version,target:target.target_lines,...audit,chunkSize,chapters:target.parts.flatMap(p=>{const r=rows.find(r=>r.part===p.id);return r?[{title:p.title,start:r.ordinal}]:[];})};
await writeFile(new URL('public/text/initial.json',root),JSON.stringify(renderRows.slice(0,chunkSize).map(({id,ordinal,en,gapBefore})=>({id,ordinal,en,...(gapBefore?{gapBefore}: {})})))+'\n');
const destination=new URL('public/text/manifest.json',root);await writeFile(destination,JSON.stringify(manifest,null,2)+'\n');
console.log(JSON.stringify(audit));
