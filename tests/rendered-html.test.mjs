import assert from 'node:assert/strict';import test from 'node:test';
test('production worker renders honest zero-line edition and accessible alternative',async()=>{
 const {default:worker}=await import('../dist/server/index.js');
 for(const path of ['/','/read']){
  const response=await worker.fetch(new Request(`http://localhost${path}`,{headers:{accept:'text/html'}}),{ASSETS:{fetch:async()=>new Response('Not found',{status:404})}},{waitUntil(){},passThroughOnException(){}});
  assert.equal(response.status,200);const html=await response.text();assert.match(html,/Manas/);assert.doesNotMatch(html,/codex-preview|react-loading-skeleton/);
  if(path==='/'){assert.match(html,/Edition in preparation/);assert.match(html,/500,553/);assert.match(html,/0<!-- --> lines published|0 lines published/);}
 }
});
