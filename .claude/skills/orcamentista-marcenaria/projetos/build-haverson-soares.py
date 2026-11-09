# -*- coding: utf-8 -*-
"""HAVERSON SOARES — caderno de proposta nas TRÊS LINHAS  [09/11/2026]

⭐ [Jonathan, 09/11/2026] "pode criar a proposta", depois de fechar os números:
  · as três linhas da casa — Telescópica, Hettich e Blum — no lugar da Häfele;
  · a sala separada em dois itens: "rack com a torre de nichos" e "portas com
    sistema mão amiga";
  · a cozinha existente a preço fechado de R$ 3.900, igual nas três linhas;
  · MC 4 pontos abaixo no geral e 15 no rack (tudo em `haverson-soares/precos.py`).
⭐ Estrutura do caderno do ICA na versão do Gustavo (A4 paisagem), com as folhas das
  três linhas: a escolha · as três opções ANTES de qualquer valor · a garantia ·
  o investimento item a item nas três linhas · a decisão · condições.
⭐ Sem render na cozinha e no gourmet: as folhas usam as ELEVAÇÕES COLORIDAS do
  executivo, sem texto. A sala usa o render que o Jonathan pôs no Drive.
⚠ Pagamento, prazo e validade não foram ditos para este cliente: seguem os do
  caderno do Gustavo (mesma arquiteta) e vão como dúvida na entrega.
⛔ Nenhum número digitado: tudo sai de `haverson-soares/precos.py`.
⛔ Sem metragem e sem contagem nas descrições dos ambientes.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'haverson-soares'
sys.path.insert(0, str(R)); sys.path.insert(0, str(P))
with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')

CLIENTE = 'Haverson Soares'
ARQ = 'Luiza Pacheco'
OBRA = 'Residencial Árvores · Alphaville'
DATA = 'Novembro de 2026'
PRAZO, VALIDADE = '60 dias corridos', '7 dias úteis'          # ⚠ a confirmar
LIN = ('Telescópica', 'Hettich', 'Blum')                       # da entrada ao topo
GAR = {'Telescópica': '2', 'Hettich': '10', 'Blum': '30'}
CHAMADA = {'Telescópica': 'Corrediça telescópica', 'Hettich': 'Corrediça oculta Hettich',
           'Blum': 'Corrediça e dobradiça Blum'}
PAGTO = [('Entrada, na assinatura do contrato', 0.30), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.30)]   # ⚠ a confirmar
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
def b64(p):
    mime = 'image/png' if p.suffix == '.png' else 'image/jpeg'
    return f'data:{mime};base64,' + base64.b64encode(p.read_bytes()).decode()
IMG = {p.stem: b64(p) for p in (P / 'img-haverson-soares').glob('*.jpg')}

# ── os valores: cada linha da tabela em real cheio, o total é a soma do que se lê ──
SALA_RACK = ('Sala', 'Rack com a torre de nichos')
SALA_PORTAS = ('Sala', 'Portas de correr com sistema mão amiga')
(EXIST, EXIST_M), FIXO = next(iter(PR.FIXOS.items()))
LINHAS_INV = [
 ('Cozinha', 'Inferiores sob a pedra, torre quente, superiores, bancada com adega, '
  'geladeira emoldurada, painel e colmeia de vinhos',
  {l: PR.total(l, 'Cozinha', fixos=False) for l in LIN}),
 ('Gourmet', 'Cristaleira, inferiores sob a pedra, nicho com básculas e torre quente',
  {l: PR.total(l, 'Gourmet', fixos=False) for l in LIN}),
 ('Sala · rack com a torre de nichos', 'Rack grafite com portas de vidro e luz por baixo, '
  'e a torre de nichos iluminados em Freijó', {l: PR.TAB[l][SALA_RACK]['pv'] for l in LIN}),
 ('Sala · portas de correr', 'Em Freijó, com o sistema mão amiga',
  {l: PR.TAB[l][SALA_PORTAS]['pv'] for l in LIN}),
 ('Cozinha existente', 'Troca das portas dos inferiores e módulo complementar, em Branco TX '
  'com puxador cava Rometal', {l: FIXO for l in LIN}),
]
VAL = {l: [round(v[l]) for *_, v in LINHAS_INV] for l in LIN}
# ⛔ o total é o que foi APRESENTADO ao Jonathan (77.304 · 93.800 · 112.999): o resíduo do
#   arredondamento vai para a maior linha, e a soma do que se lê fecha nele
for l in LIN:
    _r = round(PR.total(l)) - sum(VAL[l])
    assert abs(_r) <= 3, ('⛔ resíduo grande demais', l, _r)
    VAL[l][max(range(len(VAL[l])), key=lambda i: VAL[l][i])] += _r
TOT = {l: sum(VAL[l]) for l in LIN}
assert TOT == {'Telescópica': 77304, 'Hettich': 93800, 'Blum': 112999}, TOT
assert TOT['Telescópica'] < TOT['Hettich'] < TOT['Blum']

S, N = [], [0]
def folha(corpo, dark=False, rodape=True, foot_r=False, cls=''):
    N[0] += 1
    f = (f'<div class="foot{" r" if foot_r else ""}"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span>'
         f'<span>{N[0]:02d}</span></div>') if rodape else ''
    S.append(f'<div class="slide{" dark" if dark else ""}{" " + cls if cls else ""}">{corpo}{f}</div>')

def mv(itens):
    return ''.join(f'''<div class="mv"><span class="b"></span><span>
      <span class="t">{E(t)}</span> <span class="d">{d}</span></span></div>''' for t, d in itens)

def campo(*imgs, op=.95, tag=None, legenda=None, row=False):
    """O desenho do executivo multiplicado sobre um campo claro: o branco do papel some."""
    figs = ''.join(f'<img src="{IMG[i]}" alt="">' for i in imgs)
    t = f'<div class="tag">{E(tag)}</div>' if tag else ''
    lg = f'<div class="leg">{E(legenda)}</div>' if legenda else ''
    return f'<div class="campo n{len(imgs)}{" row" if row else ""}" style="--op:{op}">{figs}{lg}{t}</div>'

# ── 01 · capa ───────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">Haverson<br>Soares</div>
  <div class="cv-s">A cozinha, o gourmet e a sala da casa,<br>
     em três linhas de ferragem.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">Arquiteta {E(ARQ)}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Linhas</div><div class="v">Telescópica · Hettich · Blum</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['sala']}" alt="" style="object-position:62% 50%"></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''', dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
folha(f'''<div class="ambw">
 <div class="band" style="height:96mm">{campo('des-cz-a', 'des-cz-c', 'des-gm-b', op=.9, row=True)}
   <div class="tag">A casa</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">O que esta casa pede</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">Três ambientes. Uma só mão, do corte à montagem.</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">A cozinha em azul, o gourmet em
    Freijó e a sala de TV — um só projeto da arquiteta <b>{E(ARQ)}</b>, com puxador cava
    usinado, gavetas que saem inteiras, vidro reflecta bronze, iluminação embutida e portas de
    correr que abrem juntas. E, junto, a renovação da cozinha que já existe. <b>Uma só empresa
    responde por tudo o que está nestas folhas</b>, da medição à instalação. <em>Um contrato,
    uma data, um nome para chamar.</em></p></div>
 </div></div>''')

# ── 03 · a empresa e a infraestrutura ───────────────────────────────────
PIL = [
 ('01', 'O projeto pede mais que marcenaria.',
  'Vidro reflecta bronze, iluminação em LED embutida, sistema de correr sincronizado, '
  'articulador de báscula. Tudo isso entra no nosso escopo, no mesmo contrato e na mesma data. '
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

# ── 05… · as folhas de ambiente, SEM preço ──────────────────────────────
GAVETA = ('Gavetas e gavetões', 'Sobre a corrediça da linha escolhida: a diferença entre as três '
          'está explicada mais adiante, antes dos valores.')
CAVA = ('Puxador cava', 'Usinado na própria frente: nenhuma peça de metal interrompe o desenho.')
AMB = [
 ('A cozinha,<br>a pia e a geladeira.', ['des-cz-a', 'des-cz-b'], 'Cozinha',
  'MDF azul, no tom a definir com a arquiteta · interior em Branco TX · puxador cava',
  [('Sob a bancada de pedra', 'Da pia ao cooktop e na parede da geladeira: gavetões, gavetas e '
    'o porta-temperos, sobre o sóculo existente.'),
   ('Básculas sob as cubas', 'Abrem para baixo e ficam paradas onde você soltar, com pistão '
    'amortecido.'),
   ('A geladeira emoldurada', 'Máscara em MDF azul e armário de portas de giro por cima, '
    'fechando o vão até o forro.'),
   GAVETA, CAVA]),
 ('A cozinha,<br>a torre e a bancada.', ['des-cz-c'], 'Cozinha',
  'MDF azul · Freijó Puro na colmeia · interior em Branco TX · puxador cava',
  [('Torre quente', 'Micro-ondas e forno embutidos, armário no alto e gavetão embaixo.'),
   ('Armários superiores', 'Sobre a bancada, com portas de giro e prateleira por dentro.'),
   ('Bancada em MDF azul', 'Com o nicho da adega e um armário de portas de giro.'),
   ('Painel e colmeia', 'O painel fixo do piso ao teto e a colmeia de vinhos em Freijó, '
    'encaixada na ilha de pedra.')]),
 ('O gourmet.', ['des-gm-a', 'des-gm-b'], 'Gourmet',
  'MDF Freijó Puro · Essencial Wood Duratex · MDF azul sob a pedra · interior em Branco TX',
  [('Cristaleira', 'Em Freijó, do piso ao forro: porta de vidro reflecta bronze com perfil '
    'bronze, prateleiras iluminadas por dentro e o nicho da adega embaixo.'),
   ('Sob a bancada de pedra', 'Gavetões, gavetas e básculas em MDF azul, na área molhada e na '
    'churrasqueira.'),
   ('Nicho e armário superior', 'Em Freijó, com básculas que abrem para cima sobre articulador '
    'de molas: a porta sobe sozinha e para onde você soltar.'),
   ('Torre quente', 'Em Freijó, com os eletros emoldurados, armário no alto e gavetão embaixo.')]),
]
for titulo, imgs, tag, acab, itens in AMB:
    folha(f'''<div class="amb">
     <div class="amb-img">{campo(*imgs, op=.95, tag=tag, legenda='Elevação · desenho do projeto')}</div>
     <div class="amb-txt">
      <div class="eyebrow">Ambiente</div><div class="rule"></div>
      <div class="fit"><h2 class="h2" style="margin:1mm 0 4mm">{titulo}</h2>{mv(itens)}
       <div class="amb-nota" style="background:none;border-left-color:var(--line)">
         <div class="t">Acabamentos</div><p>{E(acab)}</p></div></div>
     </div></div>''', foot_r=True)
SALA = [
 ('Rack', 'Em grafite, com a ponta arredondada, portas de vidro reflecta bronze, portas com cava '
  'no alto e uma faixa de luz por baixo, que deixa o móvel flutuar sobre o piso.'),
 ('Torre de nichos', 'Em Freijó, do piso ao teto, com os nichos iluminados por dentro e o vão do '
  'subwoofer embaixo, alinhado ao rack.'),
 ('Portas de correr mão amiga', 'Em Freijó, do piso ao teto, com puxador concha. As folhas '
  'correm sincronizadas: puxa uma e a outra acompanha.'),
]
folha(f'''<div class="amb">
 <div class="amb-img"><img src="{IMG['sala']}" alt="" style="object-position:60% 50%">
  <div class="tag">Sala</div></div>
 <div class="amb-txt">
  <div class="eyebrow">Ambiente</div><div class="rule"></div>
  <div class="fit"><h2 class="h2" style="margin:1mm 0 4mm">A sala.</h2>{mv(SALA)}
   <div class="amb-nota" style="background:none;border-left-color:var(--line)">
     <div class="t">Acabamentos</div><p>MDF grafite · MDF Freijó · vidro reflecta bronze ·
     LED embutido · sistema de correr sincronizado</p></div>
   <div class="amb-nota" style="background:none;border-left-color:var(--gold);margin-top:3mm">
     <div class="t">E a cozinha que já existe</div><p>Trocamos as portas dos armários inferiores
     e fabricamos um módulo complementar, em Branco TX com puxador cava Rometal.</p></div></div>
 </div></div>''', foot_r=True)
N_AMB = (5, N[0])

# ── a escolha: três linhas, a diferença está na ferragem ────────────────
DIF = [
 ('Corrediça',
  'Telescópica, com o trilho aparente na lateral da gaveta e sem amortecedor de fechamento.',
  'Oculta Hettich: o trilho some por baixo, a gaveta abre inteira e fecha amortecida.',
  'Oculta Blum: a mesma discrição, com o curso mais macio e a maior capacidade de carga das três.'),
 ('Dobradiça', 'Nacional, de caneco.',
  'Hettich, com amortecedor e regulagem nos três sentidos.',
  'Blum, com amortecedor e regulagem nos três sentidos.'),
 ('Básculas', 'Articulador de molas nas que abrem para cima e pistão amortecido nas que abrem '
  'para baixo. Iguais nas três linhas.', 'Os mesmos.', 'Os mesmos.'),
 ('Vidro, luz e correr', 'O vidro reflecta bronze, o LED embutido e o sistema mão amiga são os '
  'mesmos nas três linhas.', 'Os mesmos.', 'Os mesmos.'),
 ('Garantia', f"{GAR['Telescópica']} anos", f"{GAR['Hettich']} anos", f"{GAR['Blum']} anos"),
]
linhas = ''.join(
    f'<tr><td class="l">{E(k)}</td><td style="text-align:left;font-size:8.4pt">{E(a)}</td>'
    f'<td class="hi" style="text-align:left;font-size:8.4pt">{E(b)}</td>'
    f'<td style="text-align:left;font-size:8.4pt">{E(c)}</td></tr>'
    for k, a, b, c in DIF)
folha(f'''<div class="pad">
 <div class="eyebrow">Uma escolha</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Três linhas. A diferença está na ferragem.</h1>
 <p class="lead" style="max-width:215mm">O desenho, os padrões de MDF, o vidro, a iluminação e o
   acabamento são <b>os mesmos nas três</b>. O que muda é a peça que vocês tocam todo dia — e é
   ela que decide quanto tempo o móvel continua fechando bem.</p>
 <table class="cmp" style="margin-top:6mm">
  <tr><th class="l" style="text-align:left"></th>
   {''.join(f'<th{" class=hi" if n == "Hettich" else ""}>{E(n)}</th>' for n in LIN)}</tr>
  {linhas}
 </table>
 <div class="box" style="margin-top:auto"><div class="t">O que não muda</div>
  <p>Os padrões de MDF especificados pela arquiteta, o puxador cava usinado na própria peça, o
   vidro reflecta bronze, a iluminação entregue instalada, o sistema de correr da sala e a equipe
   própria do corte à montagem.</p></div>
</div>''')

# ── as três opções, antes de qualquer valor ─────────────────────────────
OPC = [
 ('Telescópica',
  'A corrediça telescópica corre sobre esferas e <b>mostra o trilho na lateral da gaveta</b> '
  'quando ela abre. Não tem amortecedor: a gaveta fecha no impulso que você der. É a ferragem '
  'que a maior parte do mercado entrega como padrão — <em>o que muda é por quanto tempo</em>.'),
 ('Hettich',
  'A corrediça oculta alemã corre <b>por baixo da caixa da gaveta</b>: você abre e não vê '
  'ferragem nenhuma. A gaveta sai inteira, o fechamento é amortecido e a regulagem é fina. '
  '<em>É a linha mais próxima do que o projeto da arquiteta especifica.</em>'),
 ('Blum',
  'A mesma discrição da alemã, com o <b>curso mais macio e a maior capacidade de carga</b> das '
  'três — é o que se sente num gavetão cheio, onde ferragem fraca aparece primeiro. A Blum é a '
  'referência do mercado, e por isso respondemos por ela <em>por trinta anos</em>.'),
]
ops = ''.join(
    f'''<div class="c{" hi" if k == "Hettich" else ""}">
     <div class="anos">{GAR[k]}</div><div class="unid">anos de garantia</div>
     <div class="nm">{E(CHAMADA[k])}</div><div class="x">{d}</div></div>''' for k, d in OPC)
folha(f'''<div class="pad">
 <div class="eyebrow">As três opções</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O que vocês vão sentir na mão.</h1>
 <p class="lead" style="max-width:215mm">A ferragem é a única peça da marcenaria que <b>se usa
  todo dia e se desgasta</b>. O MDF não cansa, o vidro não cansa, a furação não cansa. A
  corrediça e a dobradiça, sim — e por isso a escolha entre as três linhas <b>vale para a casa
  toda</b>: a garantia do conjunto segue a ferragem da linha escolhida.</p>
 <div class="gar justo">{ops}</div>
 <div class="box" style="margin-top:5mm"><div class="t">Como escolher</div>
  <p>Abra uma gaveta de cada linha antes de decidir — <b>em trinta segundos a mão resolve o que
   a tabela não resolve</b>. Levamos as três amostras até vocês antes do fechamento, sem
   compromisso.</p></div>
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
  dois anos na telescópica, dez na Hettich e trinta na Blum, para a casa inteira. Não é promessa
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

# ── investimento, item a item, nas três linhas ──────────────────────────
IGUAIS = [n for n, _d, v in LINHAS_INV if len({round(v[l]) for l in LIN}) == 1]
assert [n for n in IGUAIS] == ['Sala · portas de correr', 'Cozinha existente'], IGUAIS
rows = ''.join(
    f'<tr><td class="l">{E(n)}<div class="sub">{E(d)}</div></td>'
    + ''.join(f'<td{" class=hi" if l == "Hettich" else ""}>{brs(VAL[l][i])}</td>' for l in LIN)
    + '</tr>' for i, (n, d, _v) in enumerate(LINHAS_INV))
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · item a item</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">A casa, nas três linhas.</h1>
 <p class="lead" style="max-width:215mm">Cada móvel foi levantado <b>peça por peça do projeto
  executivo</b> — nada é rateio nem estimativa por metro quadrado. Valores em reais.</p>
 <table class="inv" style="margin-top:5mm">
  <tr><th class="l">Item</th>
   {''.join(f'<th{" class=hi" if l == "Hettich" else ""}>{E(l)}</th>' for l in LIN)}</tr>
  {rows}
  <tr class="tot"><td class="l">O projeto completo</td>
   {''.join(f'<td{" class=hi" if l == "Hettich" else ""}>{brs(TOT[l])}</td>' for l in LIN)}</tr>
 </table>
 <div class="box" style="margin-top:auto"><p style="font-size:8.4pt">
  <b>As portas de correr da sala e a cozinha existente têm o mesmo valor nas três linhas:</b>
  não levam corrediça nem dobradiça, que é onde as linhas se diferenciam.</p></div>
</div>''')

# ── a decisão: as três linhas, um valor cada ────────────────────────────
RESUMO = {'Telescópica': 'Trilho aparente na lateral da gaveta e fechamento sem amortecedor.',
          'Hettich': 'Trilho oculto por baixo, gaveta que sai inteira e fechamento amortecido.',
          'Blum': 'O curso mais macio e a maior capacidade de carga das três.'}
cards = ''.join(
    f'''<div class="c{" hi" if k == "Hettich" else ""}">
     <div class="anos">{GAR[k]}</div><div class="unid">anos de garantia</div>
     <div class="nm">{E(CHAMADA[k])}</div><div class="x">{RESUMO[k]}</div>
     <div class="l"><div class="k">O projeto completo</div>
      <div class="v" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt">{br(TOT[k])}</div></div>
     <div class="l" style="margin-top:2mm"><div class="k">Entrada, na assinatura</div>
      <div class="v">{br(TOT[k] * PAGTO[0][1])}</div></div></div>''' for k in LIN)
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · as três linhas</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Dois anos, dez, ou trinta.</h1>
 <p class="lead" style="max-width:215mm">A mesma casa, o mesmo desenho e os mesmos padrões. A
  diferença é a <b>ferragem</b> — e o tempo pelo qual respondemos por ela.</p>
 <div class="gar justo">{cards}</div>
 <div class="box" style="margin-top:5mm"><div class="t">O que está incluso</div>
  <p>Projeto executivo de marcenaria, material, usinagem, ferragem da linha escolhida, o vidro
   reflecta bronze, a iluminação em LED embutida, o sistema de correr mão amiga, transporte,
   montagem e instalação — num só contrato, com uma só data e uma só arquiteta responsável.</p></div>
</div>''')

# ── condições ───────────────────────────────────────────────────────────
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
     <div class="s">Trinta anos na Blum, dez na Hettich e dois na telescópica. Instalação e
       regulagem, dois anos. Termo assinado na entrega.</div></div>
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
    <li><div class="k">Pedra</div><div class="v">As bancadas existentes, o complemento de
      bancada, a ilha, o frontão e a frente dos sóculos são marmoraria.</div></li>
    <li><div class="k">Eletrodomésticos e metais</div><div class="v">Cooktop, coifa, forno,
      micro-ondas, geladeira, adegas, cubas, torneiras e a churrasqueira.</div></li>
    <li><div class="k">Sala</div><div class="v">A televisão, o subwoofer e o revestimento da
      parede.</div></li>
    <li><div class="k">Obra e iluminação geral</div><div class="v">Pontos elétricos, forro,
      piso e pintura de parede.</div></li>
   </ul>
  </div>
 </div>
 <div class="sig"><div class="ln">{E(CLIENTE)}</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

# ── encerramento ────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome" style="font-size:36pt">Um contrato.<br>Uma data.<br>Um nome<br>para chamar.</div>
  <div class="cv-s">Obrigado pela confiança de pôr esta casa na nossa mão. O desenho da
   arquiteta {E(ARQ)} sai da nossa fábrica e chega instalado.</div>
  <div class="cv-meta">
   <div><div class="k">Proposta</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['sala']}" alt="" style="object-position:82% 50%"></div>
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
for _c in ('Michell', 'Michelle', 'Jéssica', 'Jessica', 'Arlei', 'Gustavo', 'Raposo',
           'Phillip', 'Giselle', 'Ana Carolina', 'André', 'Attos', 'Kenia', 'Fábio', 'Mateus',
           'Tereza', 'Júnia', 'Rafael', 'Lagoa Santa', 'Vale dos Pinhais', 'Costa Laguna'):
    assert _c not in _t, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE: {_c}'
assert not [c for c in '⭐⛔⚠' if c in ''.join(S)], '⛔ marcação interna'
for _p in ('cartão', 'cartao', 'desconto', 'häfele', 'hafele', 'margem'):
    assert _p not in _t.lower(), f'⛔ a peça fala em "{_p}"'
_amb = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(S[N_AMB[0] - 1:N_AMB[1]])))
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco|seis|sete|oito|dez)\s+(portas?|folhas?|gavet\w+|básculas?|nichos?|prateleiras?)', _amb, re.I), '⛔ contagem'
assert 'mão amiga' in _t and 'Cozinha existente' in _t

OUT = R / 'proposta-haverson-soares.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-haverson-soares.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {NF} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
for l in LIN:
    print(f'  {l:12s} {br(TOT[l])} · entrada {br(TOT[l] * PAGTO[0][1])} · ' + ' · '.join(brs(v) for v in VAL[l]))
