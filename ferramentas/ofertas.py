import json, urllib.parse
WA='5511999042043'
def brl(v):
    s=f"{v:,.2f}"; return 'R$ '+s.replace(',','X').replace('.',',').replace('X','.')
O=[
 dict(cod='PUJ', nome='Punta Cana', intl=True, img='photo-1705507972578-78537a2dda73',
  tipo='All inclusive · transfer grátis', dest='Punta Cana,<br>Caribe', hotel='Impressive Punta Cana', regime='tudo incluído',
  saida='Aéreo saindo de São Paulo (GRU)', datas='02 a 10/nov · 7 noites', preco=5964.18, taxa=1000.00,
  selo='Oferta Luvi', urg='Saída no feriado de Finados',
  inclui=['Aéreo ida e volta saindo de Guarulhos','7 noites no Impressive Punta Cana, ALL INCLUSIVE','Transfer aeroporto ↔ hotel (cortesia)','Seguro viagem'],
  fonte='https://viajandocomdesconto.com/pacotes/punta-cana-transfer-gratis-2?saida=sao-paulo',
  obs='Outra saída SP: 11 a 19/11 a partir de R$ 6.400,18 + taxas. Hotéis superiores (Majestic, Hard Rock) disponíveis com acréscimo.'),
 dict(cod='BUE', nome='Buenos Aires', intl=True, img='photo-1679417302656-9b5170584526',
  tipo='Aéreo + hotel + city tour', dest='Buenos<br>Aires', hotel='1253 Recoleta Small Hotel', regime='café da manhã',
  saida='Aéreo saindo de São Paulo', datas='20 a 24/nov · 3 noites', preco=2189.92, taxa=840.00,
  selo='Oferta Luvi', urg='Feriado da Consciência Negra',
  inclui=['Aéreo ida e volta saindo de São Paulo','3 noites no 1253 Recoleta Small Hotel com café da manhã','City tour (cortesia)'],
  fonte='https://viajandocomdesconto.com/pacotes/buenos-aires-com-city-tour-gratis-via-eze?saida=sao-paulo',
  obs='Hotel no bairro da Recoleta. Confirmar no portal se o transfer está incluso (não aparece na lista de inclusões).'),
 dict(cod='EGI', nome='Egito', intl=True, img='photo-1568322445389-f64ac2515020',
  tipo='Grupo com guia desde o Brasil', dest='Egito com<br>Cruzeiro no Nilo', hotel='Cairo, Abu Simbel, Luxor e Alexandria', regime='11 dias',
  saida='Aéreo saindo de Guarulhos', datas='16/abr/2027 · 10 noites', preco=28186.40, taxa=1722.36,
  selo='Grupo com guia', urg='Grupo fechado: vagas limitadas',
  inclui=['Aéreo internacional + voos internos','6 noites no InterContinental Citystars Cairo (café da manhã)','3 noites de cruzeiro pelo Nilo em cabine externa, pensão completa','Guia em português + acompanhante Cativa desde o Brasil','Pirâmides de Gizé, Abu Simbel, Luxor, Karnak, Vale dos Reis, Alexandria','Visto egípcio e chip de internet 5GB'],
  fonte='https://www.cativaoperadora.com.br/pacote/2027-04-16/egito-com-cruzeiro-alexandria-e-abu-simbel-2',
  obs='Valor em euro convertido (cotação Cativa de 09/09/2026): pode variar com o câmbio, confirmar antes de fechar. Grupo garantido com mínimo de 25 pessoas. Gorjeta obrigatória do cruzeiro US$ 50 paga no barco. Individual: 10x R$ 2.961,90.'),
 dict(cod='NAT', nome='Natal', intl=False, img='photo-1680015017001-fe78240a9460',
  tipo='Aéreo + hotel + transfer + passeio', dest='Natal,<br>RN', hotel='GB Hotéis Natal', regime='café da manhã',
  saida='Aéreo saindo de Campinas (VCP)', datas='06 a 12/nov · 6 noites', preco=1740.00, taxa=199.00,
  selo='Oferta Luvi', urg='Saindo de Viracopos',
  inclui=['Aéreo ida e volta saindo de Viracopos','6 noites com café da manhã','Transfer aeroporto ↔ hotel','City tour com Praia de Camurupim','Protect Travel (cancelamento involuntário até R$ 5.000)'],
  fonte='https://viajandocomdesconto.com/pacotes/natal-com-praia-de-cumurupim-pipa?saida=campinas',
  obs='Upgrade: Marsol Beach Resort 10x R$ 246 ou Praiamar 10x R$ 298 (+ taxa R$ 199). Saída de GRU em 04/12 a partir de 10x R$ 209.'),
 dict(cod='GRA', nome='Gramado', intl=False, img='photo-1628682711021-e1c1666ec089',
  tipo='Aéreo + hotel + fondue + vinícola', dest='Gramado,<br>Serra Gaúcha', hotel='Chocoland Hotel Gramado', regime='café da manhã',
  saida='Aéreo saindo de Congonhas', datas='22 a 27/fev/2027 · 5 noites', preco=1910.00, taxa=274.00,
  selo='Oferta Luvi', urg='Tour na vinícola é cortesia',
  inclui=['Aéreo ida e volta saindo de Congonhas','5 noites no Chocoland Hotel com café da manhã','Transfer aeroporto ↔ hotel','Sequência de fondue premium','Tour na Vinícola Jolimont com taça de cortesia','1 dia de Bustour'],
  fonte='https://viajandocomdesconto.com/pacotes/gramado-com-fondue-tour-vinicola-jolimont-gratis?saida=sao-paulo',
  obs='Chocoland dá 1 ingresso grátis por apto para a Fábrica dos Sonhos. Upgrade: Harmont 10x R$ 257 (+ R$ 367) ou Gran Valley 10x R$ 294 (+ R$ 257).'),
 dict(cod='REC', nome='Porto de Galinhas', intl=False, img='photo-1698760042543-1fcc7b7e9342',
  tipo='Aéreo + hotel + 3 passeios', dest='Porto de<br>Galinhas', hotel='El Aram Beach Boa Viagem', regime='café da manhã',
  saida='Aéreo saindo de Congonhas', datas='12 a 17/nov · 5 noites', preco=2450.00, taxa=199.00,
  selo='Oferta Luvi', urg='Feriado da Proclamação da República',
  inclui=['Aéreo ida e volta saindo de Congonhas','5 noites no El Aram Beach Boa Viagem com café da manhã','Transfer aeroporto ↔ hotel','City tour Olinda e Recife Antigo','Passeio a Porto de Galinhas','Passeio à Praia dos Carneiros','Protect Travel (cancelamento involuntário até R$ 4.000)'],
  fonte='https://viajandocomdesconto.com/pacotes/recife-com-city-tour-passeio-porto-de-galinhas-carneiros?saida=sao-paulo',
  obs='Transfer só vale para hotéis em Boa Viagem/Piedade. Outras saídas CGH: 25/11, 02/12, 17/02, 28/02. Upgrade: Enseada Boa Viagem 10x R$ 265 ou Kastel Manibu 10x R$ 349 (+ R$ 277).'),
 dict(cod='MVD', nome='Montevidéu', intl=True, img='photo-1721846937765-2f05a4249028',
  tipo='Aéreo + hotel + city tour', dest='Montevidéu,<br>Uruguai', hotel='Hotel Alvear', regime='Carnaval 2027',
  saida='Aéreo saindo de São Paulo', datas='05 a 09/fev/2027 · 4 noites', preco=4550.00, taxa=623.00,
  selo='Oferta Luvi', urg='Carnaval no Uruguai',
  inclui=['Aéreo ida e volta saindo de São Paulo','4 noites no Hotel Alvear','Traslados de chegada e saída','City tour por Montevidéu','Seguro viagem'],
  fonte='https://viajandocomdesconto.com/pacotes/uruguay-escapada-a-montevideo?saida=sao-paulo',
  obs='Saída no Carnaval (05/02/2027). Também há saída SP 10 a 15/11 por R$ 6.270 + taxas. Regime de alimentação não informado no portal: confirmar café da manhã.'),
]
for i,o in enumerate(O):
    pass
    o['codigo']=f"OF-{o['cod']}2310"
    parc=round(o['preco']/10,2); o['parc']=parc
    o['total_pp']=round(o['preco']+o['taxa'],2); o['total_casal']=round(2*o['total_pp'],2)
    msg=f"Oi! Quero saber da oferta {o['nome']} [{o['codigo']}]"
    o['wa']=f"https://wa.me/{WA}?text="+urllib.parse.quote(msg)
    ip,cp=f"{parc:,.2f}".replace(',','X').replace('.',',').replace('X','.').split(',')
    o['dados']={"SELO":o['selo'],"TIPO":o['tipo'],"DESTINO_HTML":o['dest'],"HOTEL":o['hotel'],"REGIME":o['regime'],
      "SAIDA":o['saida'],"DATAS":o['datas'],"LINHA_DE":"por pessoa, base apto duplo","N_PARC":"10","PARC_INT":ip,"PARC_CENT":cp,
      "LINHA_AVISTA":f"ou <b>{brl(o['preco'])}</b> + taxas de {brl(o['taxa'])}","SELO_DESCONTO":"",
      "LEGAL":"Valores por pessoa em apto duplo, mais taxas, sujeitos a disponibilidade e alteração sem aviso. Consulte condições."}
json.dump(O,open('ofertas.json','w'),ensure_ascii=False,indent=1)
for o in O: print(o['codigo'],brl(o['parc']),brl(o['total_pp']),brl(o['total_casal']))
