export function validateRelease(rows, target, sources) {
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
 const fullCoverage=rows.length===target.target_lines&&target.parts.every(p=>perPart[p.id]===p.reported_lines);
 const complete=fullCoverage&&reviewed===rows.length&&target.completeness_verified===true&&Boolean(target.reconciliation_evidence);
 return {released:rows.length,reviewed,complete,perPart};
}
