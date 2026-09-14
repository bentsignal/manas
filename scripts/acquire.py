"""Download publisher-provided PDFs via their current catalogue links; never guess corpus completeness."""
import concurrent.futures, datetime, hashlib, html, json, pathlib, re, urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
CATALOG={
 'manas-2010':'epos-manas-sayakbay-karalaev-polnyy-variant',
 'semetey-1-2013':'semetey-baatyrdyk-epos-1-kitep-sayakbay-karalaevdin-varianty-boyuncha',
 'semetey-2-2013':'semetey-baatyrdyk-epos-2-kitep-sayakbay-karalaevdin-varianty-boyuncha',
 'seytek-2012':'seytek-baatyrdyk-epos-sayakbay-karalaevdin-varianty-boyuncha',
}
def acquire(item):
 ident,slug=item;url='https://new.bizdin.kg/kniga/'+slug
 try:
  with urllib.request.urlopen(url,timeout=60) as r:page=r.read().decode()
  links=re.findall(r'<a[^>]+href="([^"]+)"[^>]*\bdownload\b',page)
  if not links:raise ValueError('No publisher download link')
  download=html.unescape(links[0])
  with urllib.request.urlopen(download,timeout=120) as r:data=r.read()
  if not data.startswith(b'%PDF-'):raise ValueError('Not a PDF')
  path=ROOT/'sources/raw'/f'{ident}.pdf';path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
  return dict(id=ident,catalogue_url=url,download_url=download.split('?')[0],path=str(path.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),completeness='unverified',rights='unverified')
 except Exception as e:return dict(id=ident,catalogue_url=url,error=str(e))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(acquire,CATALOG.items()))
 (ROOT/'sources/manifest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
 for row in results: print(row['id'],row.get('bytes',row.get('error')))
