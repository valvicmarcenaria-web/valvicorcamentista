# -*- coding: utf-8 -*-
"""GRAN ROYALLE · CORSINO SOARES — caderno de proposta, Hettich e Blum  [11/11/2026]

⭐ [Jonathan, 11/11/2026] "pode montar a proposta linda no nosso padrão", depois de:
  · só HETTICH e BLUM, MC +3 pontos; jantar −10 pontos;
  · despensa a R$ 8.500 e gourmet a R$ 12.300 (preço fechado, em precos.py);
  · hall, varanda da master e lavabo FORA; RT 10% confirmado; suporte de vinhos nosso;
    painel da master em espelho prata.
⭐ Mesmo caderno do Haverson (A4 paisagem): as folhas da empresa, das doze etapas e da
  garantia vêm de `build-haverson-soares.py`. Fotos: os renders do caderno da arquiteta.
⚠ Prazo, pagamento e validade: o padrão da casa (90 dias, 30/20/20/30, 7 dias úteis),
  oferecido ao Jonathan e não contestado — confirmar na entrega.
⛔ Nenhum número digitado: tudo sai de `gran-royalle-corsino-soares/precos.py`.
⛔ Sem metragem e sem contagem nas descrições dos ambientes.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'gran-royalle-corsino-soares'
sys.path.insert(0, str(R)); sys.path.insert(0, str(P))
with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')
src = (P / 'build-gustavo-caderno.py').read_text(encoding='utf-8')

CLIENTE = 'Corsino Soares'
ARQ = 'Jéssica Sollero'
OBRA = 'Residência Gran Royalle'
DATA = 'Novembro de 2026'
PRAZO, VALIDADE = '90 dias corridos', '7 dias úteis'
LIN = ('Hettich', 'Blum')
GAR = {'Hettich': '10', 'Blum': '30'}
CHAMADA = {'Hettich': 'Corrediça oculta Hettich', 'Blum': 'Corrediça e dobradiça Blum'}
PAGTO = [('Entrada, na assinatura do contrato', 0.30), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.30)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
def b64(p): return 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
IMG = {p.stem: b64(p) for p in (P / 'img-gran-royalle').glob('*.jpg')}

# ── os valores: por ambiente, em real cheio; o total é a soma do que se lê ──
DESC = {
 'Sala estar e TV': ('Sala de estar', 'Rack suspenso de pontas arredondadas'),
 'Sala de jantar': ('Sala de jantar', 'Cristaleira de vidro reflecta, painel da adega e painel com a porta da despensa'),
 'Cozinha': ('Cozinha', 'Ilha, pia, torre quente, geladeira emoldurada, prateleiras iluminadas e os painéis com as portas'),
 'Despensa': ('Despensa', 'Prateleiras iluminadas em L'),
 'Lavanderia': ('Lavanderia', 'Armário superior, inferior da cuba e torre de utilidades'),
 'Espaço gourmet': ('Espaço gourmet', 'Inferiores da pia e prateleiras iluminadas'),
 'Suíte 01': ('Suíte 01', 'Roupeiro de vidro reflecta, cabeceira com brise e estofado'),
 'Banho suíte 01': ('Banho da suíte 01', 'Gabinete suspenso e armário de espelho iluminado'),
 'Suíte 02': ('Suíte 02', 'Roupeiro, painel com a porta do banho, bancada e cabeceira'),
 'Banho suíte 02': ('Banho da suíte 02', 'Gabinete suspenso e armário de espelho iluminado'),
 'Suíte master': ('Suíte master', 'Cabeceira estofada, painel espelhado com porta de correr, prateleiras e penteadeira'),
 'Banho master': ('Banho master', 'Gabinete com tulhas e armário de espelho de correr iluminado'),
 'Closet master': ('Closet master', 'Closet aberto, com gaveteiros, sapateiras e luz sob o maleiro'),
}
assert list(DESC) == PR.L.AMBIENTES
LINHAS_INV = [(DESC[a][0], DESC[a][1], {l: PR.total(l, a) for l in LIN}) for a in PR.L.AMBIENTES]
VAL = {l: [round(v[l]) for *_, v in LINHAS_INV] for l in LIN}
TOT = {l: sum(VAL[l]) for l in LIN}
for l in LIN: assert abs(TOT[l] - PR.total(l)) <= 7, (l, TOT[l], PR.total(l))
assert TOT['Hettich'] < TOT['Blum']

S, N = [], [0]
def folha(corpo, dark=False, rodape=True, foot_r=False, cls=''):
    N[0] += 1
    f = (f'<div class="foot{" r" if foot_r else ""}"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span>'
         f'<span>{N[0]:02d}</span></div>') if rodape else ''
    S.append(f'<div class="slide{" dark" if dark else ""}{" " + cls if cls else ""}">{corpo}{f}</div>')

def mv(itens):
    return ''.join(f'''<div class="mv"><span class="b"></span><span>
      <span class="t">{E(t)}</span> <span class="d">{d}</span></span></div>''' for t, d in itens)

# ── 01 · capa ───────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">Corsino<br>Soares</div>
  <div class="cv-s">A marcenaria da Residência Gran Royalle,<br>da sala ao closet.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">{E(ARQ)} Interiores</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Linhas</div><div class="v">Hettich · Blum</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['jantar-a']}" alt="" style="object-position:55% 50%"></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''', dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
folha(f'''<div class="ambw">
 <div class="band duo3" style="height:96mm"><img src="{IMG['cozinha-a']}" alt="">
   <img src="{IMG['suite01-a']}" alt=""><img src="{IMG['closet-b']}" alt="">
   <div class="tag">A casa</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">O que esta casa pede</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">Uma casa inteira. Uma só mão, do corte à montagem.</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">Contemporâneo tropical, no projeto de
    <b>{E(ARQ)}</b>: madeira quente nos painéis e nas prateleiras, tons claros nos armários,
    vidro reflecta bronze, espelhos, estofados em linho e luz embutida em cada nicho. Da sala ao
    closet da master, <b>uma só empresa responde por tudo o que está nestas folhas</b>, da
    medição à instalação. <em>Um contrato, uma data, um nome para chamar.</em></p></div>
 </div></div>''')

# ── 03 · a empresa e a infraestrutura ───────────────────────────────────
PIL = [
 ('01', 'O projeto pede mais que marcenaria.',
  'Vidro reflecta bronze, portas de espelho, estofado, iluminação em LED embutida, '
  'portas de passagem embutidas no painel. Tudo isso entra no nosso escopo, no mesmo contrato e na mesma data. '
  '<b>Vocês não contratam mais ninguém</b> para a marcenaria e para o que faz parte dela. O que '
  'fica fora vem nomeado.'),
 ('02', 'A peça sai daqui conferida.',
  'Detalhamento, programação, usinagem, montagem e conferência acontecem dentro da nossa '
  'fábrica. Cada módulo é montado aqui antes de ser embalado: porta regulada, gaveta corrida, '
  'báscula ajustada. A conferência é <b>etapa do processo</b>, não boa vontade no fim.'),
 ('03', 'Uma arquiteta responsável pelo projeto.',
  'Do orçamento aprovado à entrega, o projeto tem uma arquiteta nossa como responsável. É ela '
  'quem lê o executivo prancha por prancha, está na medição e segue as peças pela fábrica. Ela '
  f'conversa com a arquiteta {E(ARQ)} na mesma linguagem técnica. <b>Vocês explicam o projeto '
  'uma vez, a uma pessoa.</b>'),
 ('04', 'O executivo de marcenaria é nosso.',
  'Antes de cortar, a Valvic desenha. O projeto de interiores diz o que o ambiente precisa ser; '
  'o nosso executivo diz como cada móvel se constrói — estrutura, ferragem, sentido de abertura, '
  'folga das portas. É nele que a divergência aparece <em>no papel, antes de virar '
  'retrabalho</em>.'),
]
pil = '\n'.join(f'''<div class="c"><div class="n">{n}</div><div class="t">{E(t)}</div>
  <div class="d">{d}</div></div>''' for n, t, d in PIL)
folha(f'''<div class="pad">
 <div class="eyebrow">A empresa e a infraestrutura</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">A Valvic articula todas as soluções do projeto.</h1>
 <p class="lead" style="max-width:215mm">Um projeto raramente se perde na marcenaria. Ele se
  perde na costura entre os ofícios, quando cada um chega com contrato, prazo e medida
  próprios. Aqui não há essa costura para fazer: tudo o que esta proposta reúne entra no mesmo
  escopo, no mesmo contrato e na mesma data.</p>
 <div class="fr" style="margin-top:6mm;flex:1;min-height:0">{pil}</div>
 <div class="box" style="margin-top:5mm"><p style="font-size:9.4pt;color:var(--ink)">
   Na próxima folha, o caminho que o projeto percorre — etapa por etapa, até o dia em que a
   casa está em uso.</p></div>
</div>''')

# ── 04 · as doze etapas (as mesmas do caderno de referência) ────────────
src = (P / 'build-gustavo-caderno.py').read_text(encoding='utf-8')
BLOCOS = eval(re.search(r'^BLOCOS = (\[.*?\n\])', src, re.S | re.M).group(1))
assert sum(len(b[2]) for b in BLOCOS) == 12
_n = [0]
def etapa(k, t, l, e):
    _n[0] += 1
    return f'''<div class="pe"><div class="pe-n">{_n[0]:02d}</div><div class="pe-k">{E(k)}</div>
      <div class="pe-t">{E(t)}</div><div class="pe-l">{E(l)}</div><div class="pe-e">{E(e)}</div></div>'''
cols = '\n'.join(f'''<div class="pb"><div class="pb-h">{E(nm)}</div><div class="pb-s">{E(sub)}</div>
  {''.join(etapa(*e) for e in ets)}</div>''' for nm, sub, ets in BLOCOS)
folha(f'''<div class="pad" style="padding:13mm 15mm 20mm">
 <div class="eyebrow">O caminho do seu projeto</div><div class="rule"></div>
 <div style="display:flex;align-items:baseline;gap:9mm;margin-bottom:5mm">
  <h1 class="h1" style="margin:0">Doze etapas,<br>um só responsável</h1>
  <p class="lead" style="margin:0;max-width:112mm">Da sua decisão até a casa pronta são doze
    etapas — e nenhuma delas muda de dono.</p></div>
 <div class="rail"></div><div class="proc">{cols}</div>
</div>''')


# ── as folhas de ambiente, SEM preço ────────────────────────────────────
GAVETA = ('Gavetas e gavetões', 'Sobre a corrediça oculta da linha escolhida: a gaveta sai inteira e fecha amortecida.')
AMB = [
 ('A sala de estar<br>e a de jantar.', ['jantar-a'], 'Salas',
  'MDF Griss Chess e Escarlate, Arauco · interior em Branco TX · vidro reflecta bronze com alumínio slim champagne',
  [('Rack suspenso', 'Em Griss Chess, com as pontas arredondadas, gavetões de puxador chanfrado e nichos em meia esquadria.'),
   ('Cristaleira', 'Portas em vidro reflecta bronze com puxador Sotille champagne, interior em Escarlate, prateleiras de vidro, luz lateral e gavetas embaixo.'),
   ('Painel da adega', 'Moldura em Escarlate sobre a pedra, com os suportes de vinho em haste preta.'),
   ('A porta da despensa', 'Some no painel de Escarlate: porta de correr com puxador cava.')]),
 ('A cozinha.', ['cozinha-a', 'cozinha-b'], 'Cozinha',
  'MDF Griss Chess nos armários · Escarlate nos painéis e prateleiras · interior em Branco TX',
  [('A ilha', 'Gaveteiros dos dois lados e o porta-temperos, sob a pedra.'),
   ('A pia', 'Báscula que abre para baixo, gavetões e, por cima, prateleiras grossas em Escarlate com luz embutida.'),
   ('Torre quente e geladeira', 'Forno e micro-ondas embutidos, a geladeira emoldurada e os armários no alto.'),
   ('Os painéis', 'Em Escarlate do piso ao teto, com as portas da lavanderia e do lavabo embutidas: quem passa vê só a madeira.'),
   GAVETA]),
 ('A despensa<br>e a lavanderia.', ['despensa', 'lavanderia'], 'Serviço',
  'MDF Escarlate nas prateleiras · Griss Chess na lavanderia · interior em Branco TX',
  [('Despensa', 'Prateleiras grossas em L, com fixação invisível e luz sob cada uma.'),
   ('Lavanderia', 'Armário superior com cabideiro metálico, inferior da cuba com báscula e a torre de utilidades.'),
   GAVETA]),
 ('O espaço gourmet.', ['gourmet'], 'Gourmet',
  'MDF Griss Chess sob a pedra · prateleiras em Escarlate · interior em Branco TX',
  [('Sob a bancada de pedra', 'Portas de giro e gaveteiro com puxador chanfrado.'),
   ('Prateleiras', 'Grossas, em Escarlate, com fixação invisível e luz embutida por baixo.')]),
 ('A suíte 01<br>e o banho.', ['suite01-a', 'banho01-a'], 'Suíte 01',
  'MDF Frapê, Arauco · Escarlate na cabeceira · vidro reflecta bronze · estofado em linho terracota',
  [('Roupeiro', 'Portas de correr em vidro reflecta bronze com alumínio slim champagne; por dentro, maleiro, cabideiros, gaveteiros e sapateiras corrediças.'),
   ('Cabeceira', 'Brise em Escarlate com as lâminas giradas e o estofado em linho terracota, com a mesa de cabeceira.'),
   ('Banho', 'Gabinete suspenso com báscula e gavetas, e o armário de espelho com luz frontal.')]),
 ('A suíte 02<br>e o banho.', ['suite02-b', 'banho02'], 'Suíte 02',
  'MDF Frapê · Escarlate na cabeceira · espelho prata',
  [('Roupeiro', 'Portas de correr, uma em Frapê e outra em espelho, sobre maleiro, cabideiros, gavetas e sapateiras.'),
   ('Painel e bancada', 'O painel em Frapê com a porta do banho embutida, a bancada de estudo com gavetas e as prateleiras.'),
   ('Cabeceira', 'Em Escarlate, de borda arredondada, com a mesa de cabeceira.'),
   ('Banho', 'Gabinete suspenso e armário de espelho iluminado.')]),
 ('A suíte master.', ['master-a', 'master-b'], 'Suíte master',
  'MDF Frapê · Escarlate nas prateleiras · estofado em linho · espelho prata',
  [('Cabeceira', 'Estofada em linho, com as mesas de cabeceira em Frapê dos dois lados.'),
   ('Painel espelhado', 'Do piso ao teto, com a porta de correr embutida.'),
   ('Penteadeira e gaveteiro', 'Tampo de vidro temperado sobre divisórias de acrílico, e o gaveteiro de canto arredondado.'),
   ('Prateleiras', 'Grossas, em Escarlate, com as pontas arredondadas e fixação invisível.')]),
 ('O closet<br>e o banho master.', ['closet-a', 'banhomaster'], 'Master',
  'MDF Frapê · interior em Branco TX · espelho prata',
  [('Closet', 'Aberto, com maleiros iluminados por baixo, cabideiros, gaveteiros e sapateiras corrediças.'),
   ('Banho', 'Gabinete suspenso com tulhas basculantes e o armário de espelho de correr, iluminado.'),
   GAVETA]),
]
_a0 = N[0] + 1
for titulo, imgs, tag, acab, itens in AMB:
    fig = ''.join(f'<img src="{IMG[i]}" alt="">' for i in imgs)
    folha(f'''<div class="amb">
     <div class="amb-img{" duo" if len(imgs) > 1 else ""}">{fig}<div class="tag">{E(tag)}</div></div>
     <div class="amb-txt">
      <div class="eyebrow">Ambiente</div><div class="rule"></div>
      <div class="fit"><h2 class="h2" style="margin:1mm 0 4mm">{titulo}</h2>{mv(itens)}
       <div class="amb-nota" style="background:none;border-left-color:var(--line)">
         <div class="t">Acabamentos</div><p>{E(acab)}</p></div></div>
     </div></div>''', foot_r=True)
N_AMB = (_a0, N[0])

# ── a escolha: duas linhas, a diferença está na ferragem ────────────────
DIF = [
 ('Corrediça', 'Oculta Hettich: o trilho some por baixo, a gaveta abre inteira e fecha amortecida.',
  'Oculta Blum: a mesma discrição, com o curso mais macio e a maior capacidade de carga.'),
 ('Dobradiça', 'Hettich, com amortecedor e regulagem nos três sentidos.',
  'Blum, com amortecedor e regulagem nos três sentidos.'),
 ('Vidro, espelho, luz e estofado', 'Os mesmos nas duas linhas.', 'Os mesmos.'),
 ('Garantia', f"{GAR['Hettich']} anos", f"{GAR['Blum']} anos"),
]
linhas = ''.join(f'<tr><td class="l">{E(k)}</td><td class="hi" style="text-align:left;font-size:8.6pt">{E(a)}</td>'
                 f'<td style="text-align:left;font-size:8.6pt">{E(b)}</td></tr>' for k, a, b in DIF)
folha(f'''<div class="pad">
 <div class="eyebrow">Uma escolha</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Duas linhas. A diferença está na ferragem.</h1>
 <p class="lead" style="max-width:215mm">O desenho, os padrões de MDF, o vidro, os espelhos, os
   estofados e a iluminação são <b>os mesmos nas duas</b>. O que muda é a peça que vocês tocam
   todo dia — e é ela que decide quanto tempo o móvel continua fechando bem.</p>
 <table class="cmp" style="margin-top:6mm">
  <tr><th class="l" style="text-align:left"></th>
   {''.join(f'<th{" class=hi" if n == "Hettich" else ""}>{E(n)}</th>' for n in LIN)}</tr>
  {linhas}
 </table>
 <div class="box" style="margin-top:auto"><div class="t">O que não muda</div>
  <p>Os padrões Arauco especificados pela arquiteta, os puxadores usinados na própria peça, o
   vidro reflecta bronze, os espelhos, os estofados, a iluminação entregue instalada e a equipe
   própria do corte à montagem.</p></div>
</div>''')

OPC = [
 ('Hettich', 'A corrediça oculta alemã corre <b>por baixo da caixa da gaveta</b>: você abre e não vê '
  'ferragem nenhuma. A gaveta sai inteira, o fechamento é amortecido e a regulagem é fina. '
  '<em>É a nossa linha de referência para uma casa deste padrão.</em>'),
 ('Blum', 'A mesma discrição, com o <b>curso mais macio e a maior capacidade de carga</b> — é o que '
  'se sente num gavetão cheio, onde ferragem fraca aparece primeiro. A Blum é a referência do '
  'mercado, e por isso respondemos por ela <em>por trinta anos</em>.'),
]
ops = ''.join(f'''<div class="c{" hi" if k == "Hettich" else ""}">
     <div class="anos">{GAR[k]}</div><div class="unid">anos de garantia</div>
     <div class="nm">{E(CHAMADA[k])}</div><div class="x">{d}</div></div>''' for k, d in OPC)
folha(f'''<div class="pad">
 <div class="eyebrow">As duas opções</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O que vocês vão sentir na mão.</h1>
 <p class="lead" style="max-width:215mm">A ferragem é a única peça da marcenaria que <b>se usa
  todo dia e se desgasta</b>. O MDF não cansa, o vidro não cansa. A corrediça e a dobradiça,
  sim — e por isso a escolha <b>vale para a casa toda</b>: a garantia do conjunto segue a
  ferragem da linha escolhida.</p>
 <div class="gar justo duas">{ops}</div>
 <div class="box" style="margin-top:5mm"><div class="t">Como escolher</div>
  <p>Abra uma gaveta de cada linha antes de decidir — <b>em trinta segundos a mão resolve o que
   a tabela não resolve</b>. Levamos as duas amostras até vocês antes do fechamento.</p></div>
</div>''')

# ── a garantia ──────────────────────────────────────────────────────────
PASSOS = [('Vocês nos chamam', 'Por telefone, WhatsApp ou e-mail, direto com a fábrica. Sem central e sem intermediário.'),
          ('Respondemos em 24 horas', 'Esse é o nosso compromisso de retorno, contado a partir do chamado.'),
          ('Visita em até três dias úteis', 'Se não resolvermos pelo telefone, a equipe vai ao local. Dentro do prazo de garantia, visita e reparo não têm custo.')]
passos = ''.join(f'''<div class="pe"><div class="pe-n">{i:02d}</div><div class="pe-t">{E(t)}</div>
  <div class="pe-l">{E(d)}</div></div>''' for i, (t, d) in enumerate(PASSOS, 1))
folha(f'''<div class="pad">
 <div class="eyebrow">Garantia</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O termo é assinado na entrega.</h1>
 <p class="lead" style="max-width:215mm">A garantia da Valvic <b>é escalonada pela ferragem</b>:
  dez anos na Hettich e trinta na Blum, para a casa inteira. Não é promessa
  de proposta: é <b>termo assinado no dia da entrega</b>, junto com o guia de conservação do
  móvel.</p>
 <div class="three" style="margin-top:6mm">
  <div><div class="eyebrow" style="margin-bottom:3mm">Como se aciona</div>{passos}</div>
  <div><div class="eyebrow" style="margin-bottom:3mm">O que o termo cobre</div>
   <div class="term"><div class="k">Marcenaria</div>
    <div class="s">Estrutura, painéis, frentes e acabamento, pelo prazo da linha escolhida.</div></div>
   <div class="term"><div class="k">Ferragem de movimento</div>
    <div class="s">Corrediça, dobradiça, articulador e o sistema de correr, pelo prazo da linha escolhida.</div></div>
   <div class="term"><div class="k">Montagem e instalação</div>
    <div class="s">Instalações e regulagens têm garantia de dois anos em qualquer linha.</div></div></div>
  <div><div class="eyebrow" style="margin-bottom:3mm">O que fica de fora</div>
   <div class="term"><div class="k">Iluminação em LED</div>
    <div class="s">É componente eletrônico e segue a garantia do fabricante.</div></div>
   <div class="term"><div class="k">Desgaste de uso</div>
    <div class="s">Assim como o dano por umidade ou infiltração vinda da obra.</div></div>
   <div class="term"><div class="k">Alteração por terceiro</div>
    <div class="s">Feita no móvel depois da entrega.</div></div></div>
 </div></div>''')
N0 = N[0] + 1   # ⛔ a primeira folha com preço

rows = ''.join(
    f'<tr><td class="l">{E(n)} <span class="sub">· {E(d)}</span></td>'
    + ''.join(f'<td{" class=hi" if l == "Hettich" else ""}>{brs(VAL[l][i])}</td>' for l in LIN)
    + '</tr>' for i, (n, d, _v) in enumerate(LINHAS_INV))
folha(f'''<div class="pad" style="padding-top:11mm">
 <div class="eyebrow">Investimento · ambiente a ambiente</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">A casa, nas duas linhas.</h1>
 <p class="lead" style="max-width:235mm;font-size:9pt">Cada móvel foi levantado <b>peça por peça
  do caderno de marcenaria</b> — nada é rateio nem estimativa por metro quadrado. Valores em reais.</p>
 <table class="inv inv13" style="margin-top:3mm">
  <tr><th class="l">Ambiente</th>
   {''.join(f'<th{" class=hi" if l == "Hettich" else ""}>{E(l)}</th>' for l in LIN)}</tr>
  {rows}
  <tr class="tot"><td class="l">O projeto completo</td>
   {''.join(f'<td{" class=hi" if l == "Hettich" else ""}>{brs(TOT[l])}</td>' for l in LIN)}</tr>
 </table>
</div>''')

RESUMO = {'Hettich': 'Trilho oculto por baixo, gaveta que sai inteira e fechamento amortecido.',
          'Blum': 'O curso mais macio e a maior capacidade de carga.'}
cards = ''.join(f'''<div class="c{" hi" if k == "Hettich" else ""}">
     <div class="anos">{GAR[k]}</div><div class="unid">anos de garantia</div>
     <div class="nm">{E(CHAMADA[k])}</div><div class="x">{RESUMO[k]}</div>
     <div class="l"><div class="k">O projeto completo</div>
      <div class="v" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt">{br(TOT[k])}</div></div>
     <div class="l" style="margin-top:2mm"><div class="k">Entrada, na assinatura</div>
      <div class="v">{br(TOT[k] * PAGTO[0][1])}</div></div></div>''' for k in LIN)
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · as duas linhas</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Dez anos, ou trinta.</h1>
 <p class="lead" style="max-width:215mm">A mesma casa, o mesmo desenho e os mesmos padrões. A
  diferença é a <b>ferragem</b> — e o tempo pelo qual respondemos por ela.</p>
 <div class="gar justo duas">{cards}</div>
 <div class="box" style="margin-top:5mm"><div class="t">O que está incluso</div>
  <p>Projeto executivo de marcenaria, material, usinagem, ferragem da linha escolhida, o vidro
   reflecta bronze, os espelhos, os estofados, a iluminação em LED embutida, as portas de
   passagem nos painéis, os suportes de vinho, transporte, montagem e instalação — num só
   contrato, com uma só data e uma só arquiteta responsável.</p></div>
</div>''')

pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{p*100:.0f}%</td></tr>' for r, p in PAGTO)
folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Prazo, pagamento e fronteiras.</h1>
 <div class="three">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div><div class="v">{E(VALIDADE)}</div>
     <div class="s">A partir desta data.</div></div>
   <div class="term"><div class="k">Prazo de execução</div><div class="v">{E(PRAZO)}</div>
     <div class="s">Contados a partir da medição técnica no local, não da assinatura. A
       medição tem data própria no cronograma.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">Conforme a linha</div>
     <div class="s">Trinta anos na Blum e dez na Hettich. Instalação e regulagem, dois anos.
       Termo assinado na entrega.</div></div>
   <div class="term"><div class="k">Projeto executivo de marcenaria</div><div class="v">Incluso</div>
     <div class="s">Aprovado por vocês e pela arquiteta {E(ARQ)} antes de qualquer corte.</div></div>
  </div>
  <div>
   <table class="pay" style="width:100%">
    <tr><td colspan="2" style="border:none;padding-bottom:2mm"><span class="eyebrow">Formas de pagamento</span></td></tr>
    {pay}</table>
   <div style="font-size:7.4pt;color:var(--mut);margin-top:2.5mm;letter-spacing:.06em">
     Todas as parcelas por transferência bancária.</div>
   <div class="box" style="margin-top:5mm"><div class="t">A amostra das ferragens</div>
    <p>Levamos uma gaveta de cada linha até vocês antes do fechamento, para a escolha ser
     feita com a mão.</p></div>
  </div>
  <div class="fora">
   <div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>
    <li><div class="k">Pedra</div><div class="v">Bancadas, rodabancas, a ilha, os tampos dos
      banhos, a frente dos sóculos e o fundo de pedra da adega são marmoraria.</div></li>
    <li><div class="k">Hall, lavabo e varanda da master</div><div class="v">Não fazem parte
      desta proposta.</div></li>
    <li><div class="k">Eletrodomésticos e metais</div><div class="v">Cooktop, coifa, forno,
      micro-ondas, geladeira, adegas, cubas, torneiras, churrasqueira e box.</div></li>
    <li><div class="k">Obra e iluminação geral</div><div class="v">Pontos elétricos, forro,
      piso, revestimentos e pintura de parede.</div></li>
   </ul>
  </div>
 </div>
 <div class="sig"><div class="ln">{E(CLIENTE)}</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome" style="font-size:36pt">Um contrato.<br>Uma data.<br>Um nome<br>para chamar.</div>
  <div class="cv-s">Obrigado pela confiança de pôr esta casa na nossa mão. O projeto de
   {E(ARQ)} sai da nossa fábrica e chega instalado.</div>
  <div class="cv-meta">
   <div><div class="k">Proposta</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['master-b']}" alt="" style="object-position:50% 50%"></div>
</div>''', dark=True, rodape=False)

# ── estilo e montagem ───────────────────────────────────────────────────
EXTRA = re.search(r"EXTRA = '''(.*?)'''", src, re.S).group(1)
AJUSTE = re.search(r"AJUSTE = '''(.*?)'''", src, re.S).group(1)
EXTRA += '''
:root{--paper:#FCFAF5}
.slide{background:var(--paper)}
.slide.dark{background:var(--deep)}
.campo{position:absolute;inset:0;display:flex;flex-direction:column;gap:6mm;
       justify-content:center;align-items:center;padding:14mm 12mm 18mm;
       background:radial-gradient(120% 95% at 28% 22%,#F7F5EF 0%,#ECE8DD 55%,#DDD6C6 100%)}
.slide .campo img{mix-blend-mode:multiply;opacity:var(--op);min-height:0;min-width:0;
          object-fit:contain;flex:1 1 0;width:100%;height:auto}
.slide .campo.row{flex-direction:row;gap:10mm}
.slide .campo.row img{height:100%;width:auto}
.campo .leg{position:absolute;top:7mm;left:9mm;font-size:6.2pt;letter-spacing:.26em;
           text-transform:uppercase;color:#7A6F55;font-weight:600}
.campo .tag,.amb-img>.tag{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);
  font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;padding:3mm 6mm;font-weight:600}
.band .campo{padding:9mm 22mm}
.inv td .sub{font-size:7.4pt;color:var(--mut);margin-top:.6mm;font-weight:400}
.inv td.l{padding-top:2.4mm;padding-bottom:2.4mm}
.dark .h1{color:#F6F1E7}
.amb-img.duo{display:grid;grid-template-rows:1fr 1fr;gap:2mm;background:var(--paper)}
.amb-img.duo img{width:100%;height:100%;object-fit:cover;min-height:0}
.band.duo3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:2mm;position:relative}
.band.duo3 img{width:100%;height:100%;object-fit:cover;min-width:0}
.band.duo3 .tag{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);
  font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;padding:3mm 6mm;font-weight:600}
.gar.duas{grid-template-columns:1fr 1fr !important}
.inv13 td,.inv13 th{padding-top:1.05mm !important;padding-bottom:1.05mm !important;font-size:8.6pt}
.inv13 td.l{padding-top:1.05mm;padding-bottom:1.05mm;font-size:8.8pt}
.inv13 td .sub{font-size:7pt;color:var(--mut);font-weight:400}

'''
HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {E(CLIENTE)}</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
        '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S)
        + f'<script>{AJUSTE}caber();</script></body></html>')

# ── as travas ───────────────────────────────────────────────────────────
NF = len(S)
assert 'R$' not in ''.join(S[:N0 - 1]), '⛔⛔ PREÇO ANTES DA FOLHA DE VALOR'
_t = re.sub(r'<[^>]+>', ' ', re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S)))
for _c in ('Michell', 'Michelle', 'Arlei', 'Gustavo', 'Raposo', 'Haverson', 'Luiza Pacheco',
           'Phillip', 'Giselle', 'Gisele', 'Alexandre', 'Ana Carolina', 'André', 'Attos', 'Kenia', 'Fábio',
           'Orlando', 'Ivone', 'Tereza', 'Júnia', 'Rafael', 'Lagoa Santa', 'Costa Laguna', 'Residencial Árvores'):
    assert _c not in _t, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE: {_c}'
assert not [c for c in '⭐⛔⚠' if c in ''.join(S)], '⛔ marcação interna'
for _p in ('cartão', 'cartao', 'desconto', 'margem', 'telescópica', 'sensys', 'nada corta'):
    assert _p not in _t.lower(), f'⛔ a peça fala em "{_p}"'
_amb = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(S[N_AMB[0] - 1:N_AMB[1]])))
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco|seis|sete|oito|dez)\s+(portas?|folhas?|gavet\w+|básculas?|nichos?|prateleiras?)', _amb, re.I), '⛔ contagem'

OUT = R / 'proposta-gran-royalle-corsino-soares.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-gran-royalle-corsino-soares.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {NF} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
for l in LIN:
    print(f'  {l:8s} {br(TOT[l])} · entrada {br(TOT[l] * PAGTO[0][1])}')
