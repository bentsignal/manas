'use client';
import {useCallback,useEffect,useLayoutEffect,useRef,useState} from 'react';
import {useVirtualizer} from '@tanstack/react-virtual';
import {windowFor,chunkFor,parseLine} from '../lib/reader-window.mjs';
type Line={id:string;ordinal:number;en:string;gapBefore?:string};
type Manifest={version:string;target:number;released:number;reviewed:number;chunkSize:number;chunks:string[];complete:boolean;chapters:{title:string;start:number}[]};
export default function Reader({manifest:m,initialLines}:{manifest:Manifest;initialLines:Line[]}){
 const scroller=useRef<HTMLDivElement>(null);
 const cache=useRef(new Map<number,Line[]>(initialLines.length?[[0,initialLines]]:[]));
 const [revision,setRevision]=useState(0);
 const [start,setStart]=useState(0);
 const [error,setError]=useState('');
 const [retry,setRetry]=useState(0);
 const anchor=useRef<{index:number;intra:number}|null>(null);
 const count=Math.min(2048,Math.max(0,m.released-start));
 const virtual=useVirtualizer({count,initialRect:{width:512,height:800},getScrollElement:()=>scroller.current,estimateSize:()=>18,overscan:12,getItemKey:useCallback((i:number)=>start+i,[start])});
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
   const hash=m.chunks[c];
   if(!/^[a-f0-9]{64}$/.test(hash??''))throw new Error('This section is missing from the text index.');
   const r=await fetch(`/text/chunks/${hash}.json`,{signal:controller.signal});
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
 },[firstChunk,lastChunk,m.chunkSize,m.chunks,m.released,m.version,retry]);
 const go=useCallback((index:number)=>{
  if(index<0||index>=m.released)return;
  const win=windowFor(index,m.released);
  anchor.current={index,intra:0};setStart(win.start);setRevision(v=>v+1);
  history.replaceState(null,'',`#line-${index+1}`);
 },[m.released]);
 useEffect(()=>{
  const requested=parseLine(location.hash,m.released);
  if(requested!==null)go(requested);
  try{const saved=JSON.parse(localStorage.getItem('manas-position')||'null');if(saved?.version===m.version&&Number.isInteger(saved.index)&&saved.index>=0&&saved.index<m.released)requested===null&&go(saved.index);}catch{}
  const handler=()=>{const i=parseLine(location.hash,m.released);if(i!==null)go(i);};
  window.addEventListener('hashchange',handler);return()=>window.removeEventListener('hashchange',handler);
 },[go,m.released,m.version]);
 useLayoutEffect(()=>{
  const a=anchor.current;if(!a)return;
  virtual.scrollToIndex(a.index-start,{align:'start'});
  if(a.intra)virtual.scrollToOffset((virtual.getOffsetForIndex(a.index-start,'start')?.[0]??0)+a.intra);
  anchor.current=null;
 },[start,revision,virtual]);
 function scroll(){
  if(anchor.current||!scroller.current)return;
  const offset=scroller.current.scrollTop;
  const item=virtual.getVirtualItems().find(v=>v.end>offset);
  if(!item)return;
  const index=start+item.index;
  try{localStorage.setItem('manas-position',JSON.stringify({version:m.version,index}));}catch{}
  if((item.index>1536&&start+count<m.released)||(item.index<256&&start>0)){
   const win=windowFor(index,m.released);
   if(win.start!==start){anchor.current={index,intra:offset-item.start};setStart(win.start);}
  }
 }
 const row=(index:number)=>cache.current.get(chunkFor(index,m.chunkSize))?.[index%m.chunkSize];
 return <main aria-label="Manas">
  {error&&<p role="alert">{error} <button onClick={()=>setRetry(v=>v+1)}>Retry</button></p>}
  {m.released>0&&<div className="scroll-reader" ref={scroller} onScroll={scroll} tabIndex={0} aria-label="Poem">
   <div className="poem" style={{height:virtual.getTotalSize(),position:'relative'}}>{visible.map(item=>{
    const line=row(start+item.index);
    return <div key={item.key} ref={virtual.measureElement} data-index={item.index} id={`line-${start+item.index+1}`} className="verse" aria-busy={!line} style={{position:'absolute',top:0,left:0,width:'100%',transform:`translateY(${item.start}px)`}}>{line?.gapBefore&&<div>{line.gapBefore}</div>}{line?.en}</div>;
   })}</div>
  </div>}
 </main>;
}
