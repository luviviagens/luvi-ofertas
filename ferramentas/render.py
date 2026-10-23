import json,sys
from playwright.sync_api import sync_playwright
d=json.load(open(sys.argv[1],encoding='utf-8'))
h=open('template.html',encoding='utf-8').read()
for k,v in d.items(): h=h.replace('{{%s}}'%k,str(v))
open('_render.html','w',encoding='utf-8').write(h)
import os
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
  pg.goto('file://'+os.path.abspath('_render.html')); pg.wait_for_timeout(600)
  pg.screenshot(path=sys.argv[2]); b.close()