import assert from 'node:assert/strict';import test from 'node:test';
test('production worker renders a poem-only page without filler',async()=>{
 const {default:worker}=await import('../dist/server/index.js');
 for(const path of ['/','/read']){
  const response=await worker.fetch(new Request(`http://localhost${path}`,{headers:{accept:'text/html'}}),{ASSETS:{fetch:async()=>new Response('Not found',{status:404})}},{waitUntil(){},passThroughOnException(){}});
  assert.equal(response.status,200);const html=await response.text();assert.match(html,/Manas/);assert.doesNotMatch(html,/codex-preview|react-loading-skeleton/);
  assert.doesNotMatch(html,/Edition in preparation|Every line|continuous story|Source &amp; progress|og.png/);
  assert.match(html,/His forefathers were khans, every one,/);
  assert.match(html,/id="line-1"/);
 }
});
