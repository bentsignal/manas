"""Validate all 24 outputs and shuffle labels without printing model key."""
import pathlib,json,secrets,hashlib,re
b=pathlib.Path(__file__).parent
configs=['terra-medium','terra-high','sol-low','sol-medium','astra-low','astra-medium']
meta=json.loads((b/'passages.json').read_text()); key={}; candidates=[];validation=[]
assert not (b/'identity-key.json').exists(), 'Do not reshuffle after grading begins'
for p in meta:
 number=p['passage'];order=configs.copy();secrets.SystemRandom().shuffle(order)
 for label,config in zip('ABCDEF',order):
  candidate=f'P{number}{label}';path=b/f'{config}-p{number}.json';data=json.loads(path.read_text());rows=data['lines']
  assert [r['line'] for r in rows]==list(range(1,p['source_lines']+1)),path
  assert all(isinstance(r.get('note'),str) and (r['english'] is None or isinstance(r['english'],str) and r['english'].strip()) for r in rows),path
  key[candidate]=config
  candidates.append(dict(candidate=candidate,passage=number,lines=rows))
  validation.append(dict(candidate=candidate,source_lines=len(rows),translated_lines=sum(r['english'] is not None for r in rows),english_words=sum(len(r['english'].split()) for r in rows if r['english']),null_lines=[r['line'] for r in rows if r['english'] is None],output_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
for file,data in [('identity-key.json',key),('blinded-candidates.json',candidates),('validation.json',validation)]:
 (b/file).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Validated and blinded all 24 outputs; key not printed.')
