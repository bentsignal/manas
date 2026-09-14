'use client';
import {useCallback,useEffect,useLayoutEffect,useRef,useState} from 'react';
import {useVirtualizer} from '@tanstack/react-virtual';
import {windowFor,chunkFor,parseLine} from '../lib/reader-window.mjs';
type Line={id:string;ordinal:number;ky:string;en:string;status:'draft'|'reviewed';source:{url:string;page:number};note?:string};
type Manifest={version:string;target:number;released:number;reviewed:number;chunkSize:number;complete:boolean;chapters:{title:string;start:number}[]};
type Part={id:string;title:string;reported_lines:number};
const number=(n:number)=>n.toLocaleString('en-US');
export default function Reader({manifest:m,parts}:{manifest:Manifest;parts:Part[]}){
 const scroller=useRef<HTMLDivElement>(null);
 const cache=useRef(new Map<number,Line[]>());
 const [revision,setRevision]=useState(0);
 const [start,setStart]=useState(0);
 const [position,setPosition]=useState(0);
 const [bilingual,setBilingual]=useState(true);
 const [fontSize,setFontSize]=useState(22);
 const [dark,setDark]=useState(false);
 const [audit,setAudit]=useState(false);
 const [jump,setJump]=useState('');
 const [error,setError]=useState('');
 const [retry,setRetry]=useState(0);
 const [resume,setResume]=useState<number|null>(null);
 const anchor=useRef<{index:number;intra:number}|null>(null);
 const count=Math.min(2048,Math.max(0,m.released-start));
 const virtual=useVirtualizer({count,getScrollElement:()=>scroller.current,estimateSize:()=>bilingual?104:68,overscan:12,getItemKey:useCallback((i:number)=>start+i,[start])});
 const visible=virtual.getVirtualItems();
 const first=visible[0]?.index??0;
 const last=visible[visible.length-1]?.index??0;
 const firstChunk=chunkFor(start+first,m.chunkSize),lastChunk=chunkFor(start+last,m.chunkSize);
 useEffect(()=>{
  if(!m.released)return;
  const controller=new AbortController();
  const needed=Array.from({length:lastChunk-firstChunk+1},(_,i)=>firstChunk+i);
  let alive=true;
  void Promise.all(needed.map(async c=>{
   if(cache.current.has(c))return;
   const r=await fetch(`/text/${m.version}/${c}.json`,{signal:controller.signal});
   if(!r.ok)throw new Error('This section could not be loaded. Your position has been kept.');
   const rows:Line[]=await r.json();
   const expected=Math.min(m.chunkSize,m.released-c*m.chunkSize);
   if(rows.length!==expected||rows.some((line,i)=>line.ordinal!==c*m.chunkSize+i+1))throw new Error('This section failed its line-order check.');
   if(alive)cache.current.set(c,rows);
  })).then(()=>{
   if(!alive)return;
   for(const key of cache.current.keys())if(cache.current.size>12&&!needed.includes(key))cache.current.delete(key);
   setError('');setRevision(v=>v+1);
  }).catch(e=>{if(alive&&e.name!=='AbortError')setError(e.message);});
  return()=>{alive=false;controller.abort();};
 },[firstChunk,lastChunk,m.chunkSize,m.released,m.version,retry]);
 const go=useCallback((index:number)=>{
  if(index<0||index>=m.released)return;
  const win=windowFor(index,m.released);
  anchor.current={index,intra:0};setStart(win.start);setPosition(index);setRevision(v=>v+1);
  history.replaceState(null,'',`#line-${index+1}`);
 },[m.released]);
 useEffect(()=>{
  const requested=parseLine(location.hash,m.released);
  if(requested!==null)go(requested);
  try{const saved=JSON.parse(localStorage.getItem('manas-position')||'null');if(saved?.version===m.version&&Number.isInteger(saved.index)&&saved.index>=0&&saved.index<m.released)setResume(saved.index);}catch{}
  const handler=()=>{const i=parseLine(location.hash,m.released);if(i!==null)go(i);};
  window.addEventListener('hashchange',handler);return()=>window.removeEventListener('hashchange',handler);
 },[go,m.released,m.version]);
 useLayoutEffect(()=>{
  const a=anchor.current;if(!a)return;
  virtual.scrollToIndex(a.index-start,{align:'start'});
  if(a.intra)virtual.scrollToOffset((virtual.getOffsetForIndex(a.index-start,'start')?.[0]??0)+a.intra);
  anchor.current=null;
 },[start,revision,virtual]);
 useEffect(()=>{virtual.measure();},[bilingual,fontSize,virtual]);
 function scroll(){
  if(anchor.current||!scroller.current)return;
  const offset=scroller.current.scrollTop;
  const item=virtual.getVirtualItems().find(v=>v.end>offset);
  if(!item)return;
  const index=start+item.index;setPosition(index);
  try{localStorage.setItem('manas-position',JSON.stringify({version:m.version,index}));}catch{}
  if((item.index>1536&&start+count<m.released)||(item.index<256&&start>0)){
   const win=windowFor(index,m.released);
   if(win.start!==start){anchor.current={index,intra:offset-item.start};setStart(win.start);}
  }
 }
 const row=(index:number)=>cache.current.get(chunkFor(index,m.chunkSize))?.[index%m.chunkSize];
 function renderLine(index:number){
  const line=row(index);
  if(!line)return <p className="loading-line">{error?'Section unavailable':'Loading line…'}</p>;
  return <><a className="line-number" href={`#line-${line.ordinal}`} aria-label={`Link to line ${line.ordinal}`}>{number(line.ordinal)}</a><div className="verse"><p>{line.en}</p>{bilingual&&<p lang="ky" className="kyrgyz">{line.ky}</p>}{line.note&&<details><summary>Translator’s note</summary><p className="note">{line.note}</p></details>}</div><a className="source-link" href={`${line.source.url}#page=${line.source.page}`} target="_blank" rel="noreferrer" aria-label={`Source for line ${line.ordinal}, page ${line.source.page}`}>p. {line.source.page}</a><span className="line-status">{line.status}</span></>;
 }
 return <div className={dark?'edition night':'edition'}>
  <header><a className="wordmark" href="/">МАНАС<span>MANAS</span></a><span className="header-caption">THE KARALAEV TRANSLATION PROJECT</span><button onClick={()=>setAudit(v=>!v)} aria-expanded={audit}>Source &amp; progress <span aria-hidden>↗</span></button></header>
  <main>
   <section className="opening"><p className="eyebrow">THE KYRGYZ EPIC · SAYAKBAY KARALAEV</p><h1>Every line.<br/><em>One continuous story.</em></h1><p className="intro">Manas. Semetey. Seytek. And the generations that follow.<br/>A project to bring the full 500,553-line corpus into English.</p><div className="edition-status"><span className="status-dot"/><strong>{m.complete?'Complete edition':'Edition in preparation'}</strong><span>{number(m.released)} lines published · {number(m.reviewed)} reviewed</span></div><p className="scope-note">500,553 is the reported source target, not a count of completed translations.</p></section>
   <nav className="reading-toolbar" aria-label="Reading preferences"><div className="toggle"><button className={!bilingual?'selected':''} onClick={()=>setBilingual(false)} aria-pressed={!bilingual}>English</button><button className={bilingual?'selected':''} onClick={()=>setBilingual(true)} aria-pressed={bilingual}>English + Кыргызча</button></div><div className="reading-actions"><button aria-label="Decrease text size" disabled={fontSize<=18} onClick={()=>setFontSize(v=>v-2)}>A−</button><button aria-label="Increase text size" disabled={fontSize>=30} onClick={()=>setFontSize(v=>v+2)}>A+</button><button aria-label={dark?'Use light appearance':'Use dark appearance'} onClick={()=>setDark(v=>!v)}>{dark?'☀':'☾'}</button></div></nav>
   {m.released===0?<section className="empty-reader"><span className="chapter-number">I</span><h2>The text begins with the source.</h2><p>Four candidate volumes have been acquired. Their page order, verse boundaries, and coverage are being checked against the recorded corpus.</p><p>The English text will appear here as it is translated and reviewed. This page does not yet contain the epic.</p><button className="text-button" onClick={()=>setAudit(true)}>Read the source audit <span aria-hidden>→</span></button></section>:<>
    <div className="position-bar"><span>Line {number(position+1)} of {number(m.released)}</span><form onSubmit={e=>{e.preventDefault();const n=Number(jump);if(Number.isInteger(n)&&n>=1&&n<=m.released){go(n-1);setJump('');}else setError(`Enter a line from 1 to ${m.released}.`);}}><label htmlFor="jump">Go to line</label><input id="jump" type="number" min="1" max={m.released} value={jump} onChange={e=>setJump(e.target.value)}/><button>Go</button></form>{resume!==null&&<button onClick={()=>{go(resume);setResume(null);}}>Resume at {number(resume+1)}</button>}</div>
    <a className="accessible-link" href="/read">Open accessible paged reader</a>
    {error&&<div className="error" role="alert">{error} <button onClick={()=>setRetry(v=>v+1)}>Retry</button></div>}
    <div className="scroll-reader" ref={scroller} onScroll={scroll} tabIndex={0} aria-label="Continuous epic text" style={{'--verse-size':`${fontSize}px`} as React.CSSProperties}>
     <div style={{height:virtual.getTotalSize(),position:'relative'}}>{visible.map(item=><article key={item.key} ref={virtual.measureElement} data-index={item.index} className="verse-row" style={{position:'absolute',top:0,left:0,width:'100%',transform:`translateY(${item.start}px)`}}>{renderLine(start+item.index)}</article>)}</div>
    </div>
   </>}
   <section className="scope"><p className="eyebrow">THE COMPLETE SCOPE</p><div className="parts">{parts.map((p,i)=><div key={p.id}><span className="part-index">0{i+1}</span><h3>{p.title}</h3><p>{number(p.reported_lines)} reported lines</p></div>)}</div><p className="scope-note">The 15,186 continuation lines belong to the target. The project will not stop at the three main parts.</p></section>
   {audit&&<section className="audit" id="audit"><div className="audit-heading"><p className="eyebrow">SOURCE AUDIT · SEPTEMBER 2026</p><button onClick={()=>setAudit(false)} aria-label="Close source audit">Close ×</button></div><h2>Completeness has to be demonstrated.</h2><p>No published English translation of the entire Karalaev corpus has been identified in our searches. This is a provisional finding, not proof of priority. The <a href="https://kruia.gov.kg/news/show/manas-eposu-boyuncha-chykkan-kitepterdin-tizmesi/ky">National Academy’s 2026 bibliography</a> identifies the 1995 English edition as Orozbakov’s version.</p><p>The four acquired PDFs contain 5,874 PDF pages. Their extracted text includes introductions, headings, glossaries and possible transcription errors; those are not counted as verified verses. The full source count has not been reconciled.</p><ul><li>Manas: Turar, 2010; 1,846 PDF pages in a reflowed digital file.</li><li>Semetey: Turar, 2013; two volumes, 1,432 and 1,424 pages.</li><li>Seytek: Turar; title page dated 2012, bibliographic page dated 2013; 1,172 pages.</li><li>Continuations: their complete source text remains to be located and verified.</li></ul><p>Every released line must have a source reference, an English translation and a stated review status. Missing text will remain visible in the audit. Access to a PDF does not by itself settle publication rights.</p><a className="text-button" href="/source-audit.md" download>Download the research notes ↓</a></section>}
  </main><footer><span>МАНАС · An English translation project</span><span>Source verification in progress</span></footer>
 </div>;
}
