import json
O={o['cod']:o for o in json.load(open('ofertas.json'))}
def brl(v):
    s=f"{v:,.2f}"; return 'R$ '+s.replace(',','X').replace('.',',').replace('X','.')
T={}
o=O['PUJ']; T['PUJ']=f"""🌴 *PUNTA CANA ALL INCLUSIVE* | Oferta Luvi

7 noites no *Impressive Punta Cana*, tudo incluído, com aéreo saindo de Guarulhos ✈️

📅 02 a 10 de novembro, embarque no feriado de Finados
🍹 Refeições, bebidas e lazer do resort inclusos
🚐 Transfer aeroporto ↔ hotel de cortesia
🛡️ Seguro viagem incluso

💰 *10x de {brl(o['parc'])}* por pessoa
ou {brl(o['preco'])} + taxas de {brl(o['taxa'])} (base apto duplo)

O embarque é daqui a 10 dias e os lugares no voo são limitados.

👉 Chama a Luvi e garanta o seu: {o['wa']}

_Valores por pessoa, sujeitos a disponibilidade e alteração._"""
o=O['BUE']; T['BUE']=f"""🇦🇷 *BUENOS AIRES NO FERIADÃO* | Oferta Luvi

Tango, parrilla e vinho no feriado da Consciência Negra, com aéreo saindo de São Paulo ✈️

📅 20 a 24 de novembro (3 noites)
🏨 *1253 Recoleta Small Hotel*, no charmoso bairro da Recoleta, com café da manhã
🗺️ City tour de cortesia

💰 *10x de {brl(o['parc'])}* por pessoa
ou {brl(o['preco'])} + taxas de {brl(o['taxa'])} (base apto duplo)

Feriado prolongado esgota rápido: garanta antes que o voo feche.

👉 Chama a Luvi e garanta o seu: {o['wa']}

_Valores por pessoa, sujeitos a disponibilidade e alteração._"""
o=O['EGI']; T['EGI']=f"""🐪 *EGITO COM CRUZEIRO PELO NILO* | Grupo com guia

Pirâmides de Gizé, Abu Simbel, Luxor e Alexandria em um roteiro de 11 dias, com guia acompanhando o grupo desde o Brasil ✈️

📅 Saída 16 de abril de 2027, de Guarulhos
🏨 6 noites no InterContinental Cairo + 3 noites de cruzeiro pelo Nilo com pensão completa
🗣️ Guia em português, voos internos, visto egípcio e entradas inclusas
🏛️ Vale dos Reis, Karnak, Templo de Hatshepsut e o Novo Grande Museu do Cairo

💰 *10x de {brl(o['parc'])}* por pessoa
ou {brl(o['preco'])} + taxas de {brl(o['taxa'])} (base apto duplo)

É um grupo fechado com vagas limitadas, ideal para quem quer viver o Egito com tranquilidade e tudo organizado.

👉 Chama a Luvi e reserve seu lugar: {o['wa']}

_Valores por pessoa, sujeitos a disponibilidade, câmbio e alteração._"""
o=O['NAT']; T['NAT']=f"""☀️ *NATAL SAINDO DE VIRACOPOS* | Oferta Luvi

6 noites no litoral potiguar, com aéreo saindo de Campinas, pertinho de você ✈️

📅 06 a 12 de novembro
🏨 GB Hotéis Natal com café da manhã
🚐 Transfer aeroporto ↔ hotel
🏖️ City tour com Praia de Camurupim
🛡️ Proteção contra cancelamento involuntário

💰 *10x de {brl(o['parc'])}* por pessoa
ou {brl(o['preco'])} + taxas de {brl(o['taxa'])} (base apto duplo)

Quer mais conforto? Temos opções de resort na mesma data.

👉 Chama a Luvi e garanta o seu: {o['wa']}

_Valores por pessoa, sujeitos a disponibilidade e alteração._"""
o=O['GRA']; T['GRA']=f"""🍷 *GRAMADO COM FONDUE E VINÍCOLA* | Oferta Luvi

5 noites na Serra Gaúcha, com aéreo saindo de Congonhas ✈️

📅 22 a 27 de fevereiro de 2027
🏨 *Chocoland Hotel Gramado* com café da manhã
🧀 Sequência de fondue premium
🍇 Tour na Vinícola Jolimont com taça de cortesia
🚌 1 dia de Bustour + transfer aeroporto ↔ hotel

💰 *10x de {brl(o['parc'])}* por pessoa
ou {brl(o['preco'])} + taxas de {brl(o['taxa'])} (base apto duplo)

O tour na vinícola é cortesia só nos lugares com aéreo bloqueado: quando acabarem, acabou.

👉 Chama a Luvi e garanta o seu: {o['wa']}

_Valores por pessoa, sujeitos a disponibilidade e alteração._"""
o=O['REC']; T['REC']=f"""🏖️ *PORTO DE GALINHAS NO FERIADÃO* | Oferta Luvi

Piscinas naturais, Carneiros e Olinda em 5 noites, com aéreo saindo de Congonhas ✈️

📅 12 a 17 de novembro (feriado da Proclamação da República)
🏨 El Aram Beach Boa Viagem com café da manhã
🚐 Transfer aeroporto ↔ hotel
🐠 Passeios inclusos: Porto de Galinhas, Praia dos Carneiros e city tour Olinda + Recife Antigo
🛡️ Proteção contra cancelamento involuntário

💰 *10x de {brl(o['parc'])}* por pessoa
ou {brl(o['preco'])} + taxas de {brl(o['taxa'])} (base apto duplo)

Feriado prolongado com 3 passeios inclusos: os lugares voam.

👉 Chama a Luvi e garanta o seu: {o['wa']}

_Valores por pessoa, sujeitos a disponibilidade e alteração._"""
o=O['MVD']; T['MVD']=f"""🇺🇾 *CARNAVAL EM MONTEVIDÉU* | Oferta Luvi

Troque a folia por rambla, parrilla e vinho tannat: 4 noites no Uruguai, com aéreo saindo de São Paulo ✈️

📅 05 a 09 de fevereiro de 2027
🏨 Hotel Alvear
🚐 Traslados de chegada e saída
🗺️ City tour por Montevidéu
🛡️ Seguro viagem incluso

💰 *10x de {brl(o['parc'])}* por pessoa
ou {brl(o['preco'])} + taxas de {brl(o['taxa'])} (base apto duplo)

Carnaval é a data mais disputada do ano: quem planeja antes escolhe melhor.

👉 Chama a Luvi e garanta o seu: {o['wa']}

_Valores por pessoa, sujeitos a disponibilidade e alteração._"""
S={
 'PUJ':f"Punta Cana all inclusive, 02 a 10/nov, aéreo de GRU: 10x {brl(O['PUJ']['parc'])} por pessoa + taxas. Chama aqui 👉 {O['PUJ']['wa']}",
 'BUE':f"Buenos Aires no feriado, 20 a 24/nov, aéreo de SP: 10x {brl(O['BUE']['parc'])} por pessoa + taxas. Chama aqui 👉 {O['BUE']['wa']}",
 'EGI':f"Egito com cruzeiro pelo Nilo, grupo com guia, saída 16/04/2027: 10x {brl(O['EGI']['parc'])} por pessoa + taxas. Chama aqui 👉 {O['EGI']['wa']}",
 'NAT':f"Natal saindo de Viracopos, 06 a 12/nov: 10x {brl(O['NAT']['parc'])} por pessoa + taxas. Chama aqui 👉 {O['NAT']['wa']}",
 'REC':f"Porto de Galinhas no feriado, 12 a 17/nov, aéreo de CGH: 10x {brl(O['REC']['parc'])} por pessoa + taxas. Chama aqui 👉 {O['REC']['wa']}",
 'MVD':f"Carnaval em Montevidéu, 05 a 09/fev, aéreo de SP: 10x {brl(O['MVD']['parc'])} por pessoa + taxas. Chama aqui 👉 {O['MVD']['wa']}",
 'GRA':f"Gramado com fondue e vinícola, 22 a 27/fev: 10x {brl(O['GRA']['parc'])} por pessoa + taxas. Chama aqui 👉 {O['GRA']['wa']}",
}
for k,o in O.items():
    o['grupo']=T[k]; o['status']=S[k]
    o['cobrar']=[('Por pessoa (cartão, 10x)',f"{brl(o['preco'])} = 10x {brl(o['parc'])}"),
                 ('Taxas por pessoa',brl(o['taxa'])),
                 ('Total por pessoa',brl(o['total_pp'])),
                 ('Total do casal (apto duplo)',brl(o['total_casal']))]
json.dump(list(O.values()),open('ofertas_full.json','w'),ensure_ascii=False,indent=1)
print(T['PUJ'])
