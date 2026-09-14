export const SOURCE_GAP_LABEL='[Source text damaged; translation unresolved]';
export const sourceGapLabel=gap=>gap.kind==='meaning_unresolved'?'[Source wording unresolved; translation pending]':SOURCE_GAP_LABEL;
export const countEnglishWords=rows=>rows.reduce((sum,r)=>sum+(r.en.match(/\p{L}+(?:[’'-]\p{L}+)*/gu)?.length??0),0);
export function validateRelease(rows, target, sources, gaps=[]) {
 const ids=new Set();const perPart=Object.fromEntries(target.parts.map(p=>[p.id,0]));let reviewed=0;
 for(const [i,r] of rows.entries()){
  if(r.ordinal!==i+1)throw new Error(`Missing or reordered ordinal at ${i+1}`);
  if(!r.id||ids.has(r.id))throw new Error('Missing or duplicate source line ID');ids.add(r.id);
  if(!r.ky?.trim()||!r.en?.trim())throw new Error(`Untranslated line ${r.id}`);
  if(!['draft','reviewed'].includes(r.status))throw new Error('Invalid review status');
  if(!Object.hasOwn(perPart,r.part))throw new Error('Unknown corpus part');perPart[r.part]++;
  const source=sources.find(s=>s.id===r.source_id);
  if(!source||!source.sha256||!source.publication_basis)throw new Error('Missing source or publication basis');
  if(r.transcription_status!=='verified'||!r.source?.url?.startsWith('https://')||!Number.isInteger(r.source.page)||r.source.page<1)throw new Error('Unverified transcription or invalid provenance');
  if(r.status==='reviewed'){
   if(!r.review?.reviewer||!r.review?.evidence||!r.review?.date)throw new Error('Reviewed status requires documented review');reviewed++;
  }
 }
 if(rows.length>target.target_lines)throw new Error('Release exceeds unreconciled corpus target');
 const sourceIds=new Set(rows.flatMap(r=>r.source_line_ids??[r.id]));
 const gapIds=new Set();const gapAnchors=new Set();
 for(const gap of gaps){
  const after=rows.findIndex(r=>r.id===gap.after_id),before=rows.findIndex(r=>r.id===gap.before_id);
  const source=sources.find(s=>s.id===gap.source_id);
  if(gap.status!=='unresolved'||!['damaged','meaning_unresolved'].includes(gap.kind??'damaged')||!gap.evidence||!gap.source_line_ids?.length||!source||gap.source?.sha256!==source.sha256)throw new Error('Undocumented source gap');
  if(after<0||before!==after+1||rows[after].source_id!==gap.source_id||rows[before].source_id!==gap.source_id)throw new Error('Source gap must sit between adjacent translated rows');
  if(gapAnchors.has(gap.before_id))throw new Error('Adjacent unresolved verses must share one source gap region');
  gapAnchors.add(gap.before_id);
  if(gap.source?.segments?.map(s=>s.id).join('|')!==gap.source_line_ids.join('|'))throw new Error('Source gap segment mismatch');
  for(const id of gap.source_line_ids){if(sourceIds.has(id)||gapIds.has(id))throw new Error('Source gap overlaps translated or duplicate source IDs');gapIds.add(id);}
 }
 const fullCoverage=rows.length===target.target_lines&&target.parts.every(p=>perPart[p.id]===p.reported_lines);
 const complete=gaps.length===0&&fullCoverage&&reviewed===rows.length&&target.completeness_verified===true&&Boolean(target.reconciliation_evidence);
 return {released:rows.length,englishWords:countEnglishWords(rows),reviewed,complete,perPart,sourceGaps:gaps.length};
}
