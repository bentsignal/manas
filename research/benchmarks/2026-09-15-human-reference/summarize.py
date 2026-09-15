"""Validate frozen judge files, unblind, and compute descriptive pilot results."""
import pathlib,json,hashlib,statistics
b=pathlib.Path(__file__).parent
key=json.loads((b/'identity-key.json').read_text());valid=json.loads((b/'validation.json').read_text())
judges=[];hashes={}
for name in ['judge-1.json','judge-2.json']:
 raw=(b/name).read_bytes();hashes[name]=hashlib.sha256(raw).hexdigest();a=json.loads(raw)['assessments']
 assert len(a)==24 and {x['candidate'] for x in a}==set(key)
 for x in a:
  assert len(x['scores'])==12 and all(type(v)==int and 0<=v<=2 for v in x['scores'])
  expected={f'P{x["candidate"][1]}U{i}' for i,v in enumerate(x['scores'],1) if v<2}
  assert expected=={v['unit'] for v in x['deductions']},x['candidate']
 judges.append({x['candidate']:x for x in a})
rows=[]
for config in sorted(set(key.values())):
 ids=sorted(k for k,v in key.items() if v==config)
 totals=[sum(sum(j[k]['scores']) for k in ids) for j in judges]
 rows.append(dict(configuration=config,judge_totals=totals,mean_points=statistics.mean(totals),maximum=96,passage_means=[statistics.mean(sum(j[k]['scores']) for j in judges) for k in ids],translated_lines=sum(v['translated_lines'] for v in valid if v['candidate'] in ids),english_words=sum(v['english_words'] for v in valid if v['candidate'] in ids)))
disagreements=[dict(candidate=k,configuration=key[k],unit=i+1,scores=[j[k]['scores'][i] for j in judges]) for k in sorted(key) for i in range(12) if judges[0][k]['scores'][i]!=judges[1][k]['scores'][i]]
result=dict(judge_sha256=hashes,source_lines_per_configuration=86,source_words_per_configuration=286,translation_runs=24,rows=sorted(rows,key=lambda x:-x['mean_points']),disagreement_count=len(disagreements),judged_cells=288,disagreements=disagreements,actual_token_usage=None,actual_cost=None,latency_measured=False)
(b/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
