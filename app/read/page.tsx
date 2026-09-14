'use client';
import {useEffect,useState} from 'react';
import manifest from '../../public/text/manifest.json';
type Line={ordinal:number;id:string;ky:string;en:string;status:string;source:{url:string;page:number};note?:string};
export default function Paged(){
 const [page,setPage]=useState(1);const [lines,setLines]=useState<Line[]>([]);const [error,setError]=useState('');const [retry,setRetry]=useState(0);
 useEffect(()=>{const raw=Number(new URLSearchParams(location.search).get('page')||1);setPage(Number.isInteger(raw)&&raw>0?Math.min(raw,Math.max(1,Math.ceil(manifest.released/100))):1);},[]);
 useEffect(()=>{
  if(!manifest.released)return;
  const controller=new AbortController();const start=(page-1)*100;const end=Math.min(start+100,manifest.released);const a=Math.floor(start/manifest.chunkSize),b=Math.floor((end-1)/manifest.chunkSize);
  setLines([]);setError('');
  Promise.all(Array.from({length:b-a+1},async(_,i)=>{const r=await fetch(`/text/${manifest.version}/${a+i}.json`,{signal:controller.signal});if(!r.ok)throw Error('Could not load this page.');return await r.json() as Line[];})).then(groups=>{if(!controller.signal.aborted)setLines(groups.flat().filter(l=>l.ordinal>start&&l.ordinal<=end));}).catch(e=>{if(e.name!=='AbortError')setError(e.message);});
  return()=>controller.abort();
 },[page,retry]);
 return <main className="paged"><a href="/">← Continuous reader</a><h1>Manas</h1><p>Accessible reader · 100 lines per page</p>{manifest.released===0?<p>The edition is in preparation. No translated lines have been published yet.</p>:<><nav aria-label="Page navigation">{page>1?<a href={`?page=${page-1}`}>← Previous</a>:<span/>}<span>Page {page}</span>{page*100<manifest.released?<a href={`?page=${page+1}`}>Next →</a>:<span/>}</nav>{error?<p role="alert">{error} <button onClick={()=>setRetry(x=>x+1)}>Retry</button></p>:lines.length===0?<p role="status">Loading…</p>:lines.map(l=><article key={l.id} id={`line-${l.ordinal}`}><small>Line {l.ordinal} · {l.status}</small><p>{l.en}</p><p lang="ky">{l.ky}</p>{l.note&&<p>{l.note}</p>}<a href={`${l.source.url}#page=${l.source.page}`}>Source, page {l.source.page}</a></article>)}</>}</main>;
}
