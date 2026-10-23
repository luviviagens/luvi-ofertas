import json,base64,io,html,sys
from PIL import Image
titulo=sys.argv[1]; intro=sys.argv[2]
O=json.load(open('ofertas_full.json'))
css=open('fila_css.txt').read(); js=open('fila_js.txt').read()
e=html.escape; cards=[]
for o in O:
    im=Image.open(f"luvi-{o['cod'].lower()}.png").convert('RGB').resize((720,1280),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'JPEG',quality=82); src='data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
    rows=''.join(f'<div class="row{" tot" if "casal" in k else ""}"><span>{e(k)}</span><b>{e(v)}</b></div>' for k,v in o['cobrar'])
    inc=''.join(f'<li>{e(x)}</li>' for x in o['inclui'])
    tag='Internacional' if o['intl'] else 'Nacional'
    ig=o.get('ig','Story agendado no Instagram')
    cards.append(f'''
<article class="oferta" id="of-{o['cod'].lower()}">
  <div class="arte"><img src="{src}" alt="Arte da oferta {e(o['nome'])}" width="360" height="640"><p class="dica">No celular: toque e segure a imagem para salvar.</p></div>
  <div class="info">
    <header class="cab"><span class="hora">{o['hora']}</span><span class="chip {'intl' if o['intl'] else 'nac'}">{tag}</span><span class="chip">{e(ig)}</span><span class="cod">{o['codigo']}</span></header>
    <h2>{e(o['nome'])} <small>{e(o['datas'])}</small></h2>
    <section class="cobrar" aria-label="Quanto cobrar"><h3>Quanto cobrar <em>interno</em></h3>{rows}
      <p class="obs">{e(o['obs'])}</p><details><summary>O que inclui</summary><ul>{inc}</ul></details>
      <a class="fonte" href="{e(o['fonte'])}" target="_blank" rel="noopener">Ver no portal da Cativa ↗</a></section>
    <section class="txt"><div class="txt-cab"><h3>Grupo do WhatsApp</h3><button type="button" class="copiar" data-alvo="g-{o['cod']}">Copiar texto</button></div><pre id="g-{o['cod']}">{e(o['grupo'])}</pre></section>
    <section class="txt"><div class="txt-cab"><h3>Legenda do status</h3><button type="button" class="copiar" data-alvo="s-{o['cod']}">Copiar legenda</button></div><pre id="s-{o['cod']}" class="curto">{e(o['status'])}</pre></section>
  </div>
</article>''')
agenda=''.join(f'<li><a href="#of-{o["cod"].lower()}"><b>{o["hora"]}</b>{e(o["nome"])}</a></li>' for o in O)
page=f'''<title>Fila de Ofertas Luvi</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap">
<style>{css}</style>
<div class="wrap">
 <header class="topo"><h1>{e(titulo)}</h1><p>{e(intro)}</p><ul class="agenda">{agenda}</ul></header>
 {''.join(cards)}
 <p class="rod">Fotos: Unsplash · Fonte das ofertas: viajandocomdesconto.com e cativaoperadora.com.br</p>
</div>
<script>{js}</script>
'''
open('fila-ofertas-luvi.html','w').write(page)
