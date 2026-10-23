import re,sys,html
def txt(s):
    s=re.sub(r'<(script|style|svg)[^>]*>.*?</\1>','',s,flags=re.S)
    s=re.sub(r'<br\s*/?>','\n',s); s=re.sub(r'</(p|div|li|tr|h\d|td|th)>','\n',s)
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
    return '\n'.join(re.sub(r'\s+',' ',l).strip() for l in s.split('\n') if l.strip())
for f in sys.argv[1:]:
    h=open(f).read()
    t=txt(h)
    print('#####',f)
    a=t.find('Perguntas frequentes'); print(t[:a][:2500] if a>0 else t[:2000])
    b=t.find('Voltar Copiar link')
    if b<0: b=t.find('Copiar link')
    c=t.find('Confira mais voos',b)
    print('--- DETALHE ---'); print(t[b:c][:3500])
    i=t.find('O que inclui'); 
    if i<0: i=t.find('Inclui')
    print('--- INCLUI ---', t[i:i+1200] if i>0 else 'n/a')
