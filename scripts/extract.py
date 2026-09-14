"""Preserve every PDF text line, page, and bounding box. Output is NOT certified verse."""
import concurrent.futures, hashlib, json, pathlib, subprocess, xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parents[1]
SPECIAL={'¢':'ң','ª':'Ө','º':'ө','¯':'Ү','¿':'ү','¡':'Ң'}
def normalize(text,legacy):
 if not legacy:return text
 return ''.join(SPECIAL.get(c,bytes([ord(c)]).decode('cp1251') if '\u00c0'<=c<='\u00ff' else c) for c in text)
def extract(source):
 ident=source['id'];pdf=ROOT/source['path'];out=ROOT/'sources/extracted'/f'{ident}.bbox.html'
 subprocess.run(['pdftotext','-bbox-layout',str(pdf),str(out)],check=True)
 root=ET.parse(out).getroot();ns={'h':'http://www.w3.org/1999/xhtml'}
 dest=ROOT/'sources/extracted'/f'{ident}.lines.jsonl';count=0;pages=0
 with dest.open('w') as f:
  for page_index,page in enumerate(root.findall('.//h:page',ns),1):
   pages+=1
   for block_index,block in enumerate(page.findall('.//h:block',ns),1):
    for line_index,line in enumerate(block.findall('h:line',ns),1):
     raw=' '.join(w.text or '' for w in line.findall('h:word',ns))
     record=dict(id=f'{ident}:p{page_index:04}:b{block_index:03}:l{line_index:03}',source_id=ident,pdf_sha256=source['sha256'],page=page_index,block=block_index,line_in_block=line_index,bbox={k:float(v) for k,v in line.attrib.items()},raw=raw,text=normalize(raw,ident!='manas-2010'),classification='unreviewed',transcription_status='unreviewed',normalization='legacy-font-v1' if ident!='manas-2010' else 'identity')
     f.write(json.dumps(record,ensure_ascii=False)+'\n');count+=1
 return dict(source_id=ident,pages=pages,extracted_text_lines=count,verified_verse_lines=0,extraction_sha256=hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':
 manifest=json.loads((ROOT/'sources/manifest.json').read_text())
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(extract,[s for s in manifest if 'path' in s]))
 (ROOT/'research/line-extraction.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
