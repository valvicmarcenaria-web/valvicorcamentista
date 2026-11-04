# -*- coding: utf-8 -*-
"""RAFAEL · Cozinha, Jantar e Serviço — caderno de proposta  [04/11/2026]

⭐ Estrutura do caderno do MICHELL (Jéssica e Michell, ICA), na versão já
  revisada do Gustavo Raposo: A4 paisagem, a empresa, as doze etapas, a
  página da arquiteta, as folhas de ambiente sem preço, a escolha das linhas,
  a garantia, o investimento e as condições.
⛔ Só a ESTRUTURA vem de lá. Nenhum nome, número ou imagem de outro cliente.
⛔ Nenhum número digitado: os valores saem de `rafael-cozinha/escada.py`.
⛔ Sem metragem e sem contagem nas descrições de móvel.
⭐ Forma de pagamento: a ESCALA DE DESCONTO PADRÃO da casa, a pedido do
  Jonathan em 04/11 ("formatos de pagamento com escala de desconto padrão").
  Diferente do Gustavo, onde ele mandou tirar o cartão.
"""
import pathlib, subprocess, os, base64, html, re, runpy, math, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'rafael-cozinha'
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')

CLIENTE = 'Rafael'
OBRA = 'Apartamento · social, 1º pavimento'
ARQ, ARQ_CURTO = 'Clara Dobscha Arquitetura & Interiores', 'Clara Dobscha'
DATA = 'Novembro de 2026'
PRAZO, VALIDADE = '45 a 60 dias úteis', '7 dias úteis'
LIN = ('Telescópica', 'Hettich')

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: 'R$ ' + f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))

def uri(n):
    return ('data:image/jpeg;base64,' + base64.b64encode(
        (P / 'img-rafael-cozinha' / f'{n}.jpg').read_bytes()).decode())
IMG = {p.stem: uri(p.stem) for p in (P / 'img-rafael-cozinha').glob('*.jpg')}

# ── os números, todos do motor ─────────────────────────────────────────
with contextlib.redirect_stdout(io.StringIO()):
    ESC = runpy.run_path(str(R / 'escada.py'), run_name='lib')
    LEV = {}
    for linha in ('silver', 'gold'):
        os.environ['LINHA'] = linha
        LEV[linha] = runpy.run_path(str(R / 'levantamento.py'), run_name='lib')
CEN = {}
with contextlib.redirect_stdout(io.StringIO()):
    for nome, linha, alvo in (('Telescópica', 'silver', 0.33), ('Hettich', 'gold', 0.38)):
        C, cheio, linhas = ESC['versao'](nome, linha, alvo)
        CEN[nome] = dict(cd=C, cheio=cheio, escada=linhas, lev=LEV[linha])
CEN['Telescópica']['gar'] = '2 anos'
CEN['Hettich']['gar'] = '10 anos'
CEN['Telescópica']['chamada'] = 'Linha Telescópica'
CEN['Hettich']['chamada'] = 'Linha Hettich · oculta alemã'

# ── o preço por ambiente: rateio pelo custo de cada móvel ──────────────
GRUPOS = [('Cozinha · armários', ('3 ', '4 ', '5 ', '6 ', '7 ')),
          ('Cozinha · prateleiras suspensas', ('1 ',)),
          ('Jantar · prateleira', ('2 ',)),
          ('Serviço', ('8 ', '9 ', '10 '))]

def custo_movel(L):
    """Chapa pelo custo médio do m² da própria chave, fita pela peça,
    ferragem e serviço pelo móvel. O resto (corte, consumíveis, frete,
    embalagem) entra na proporção — a soma bate o custo direto."""
    m2 = {k: L['chapas'][k] * L['CHAPA'][k] / L['area'][k] for k in L['area']}
    c = {}
    for p in L['pecas']:
        a = p['c'] * p['l'] / 1e4 * p['qtd']
        tf = p['tf'] if p['tf'] != 'cor' or 'Branco' not in p['chapa'] else 'branco'
        f = p['fita'] * p['qtd']
        v = a * m2[p['chapa']] + f * (1 + L['FITA_PERD']) * L['FITA'][tf][0] + f * L['FITA'][tf][1]
        c[p['movel']] = c.get(p['movel'], 0) + v
    for o in L['outras']:
        c[o['movel']] = c.get(o['movel'], 0) + o['qtd'] * o['pu']
    k = L['CD'] / sum(c.values())
    return {m: v * k for m, v in c.items()}

for n in LIN:
    cm = custo_movel(CEN[n]['lev'])
    g = [sum(v for m, v in cm.items() if m.startswith(pref)) for _t, pref in GRUPOS]
    assert abs(sum(g) - CEN[n]['cd']) < 0.01
    vals = [round(CEN[n]['cheio'] * x / sum(g), -1) for x in g]
    vals[0] += CEN[n]['cheio'] - sum(vals)        # o resíduo vai para o maior
    assert sum(vals) == CEN[n]['cheio']
    CEN[n]['amb'] = vals

S, N = [], [0]
def folha(corpo, dark=False, rodape=True, foot_r=False):
    N[0] += 1
    f = (f'<div class="foot{" r" if foot_r else ""}">'
         f'<span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span>'
         f'<span>{N[0]:02d}</span></div>') if rodape else ''
    S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')

def mv(itens):
    return ''.join(f'''<div class="mv"><span class="b"></span><span>
      <span class="t">{E(t)}</span> <span class="d">{E(d)}</span></span></div>'''
                   for t, d in itens)

# ── 01 · capa ───────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">Cozinha,<br>jantar<br>e serviço.</div>
  <div class="cv-s">Uma área social inteira,<br>
     do primeiro desenho ao dia da instalação.</div>
  <div class="cv-meta">
   <div><div class="k">Cliente</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Projeto</div><div class="v">{E(ARQ_CURTO)}</div></div>
   <div><div class="k">Local</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['vista5']}" alt="" style="object-position:30% 50%"></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''',
      dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
folha(f'''<div class="ambw">
 <div class="band" style="height:104mm"><img src="{IMG['vista4']}" alt="">
   <div class="tag">Hall, cozinha e jantar</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">O que este projeto pede</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">Três ambientes que se veem. Uma empresa só.</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">A cozinha, o jantar e o serviço
    deste apartamento são um espaço só, e o projeto da <b>{E(ARQ_CURTO)}</b> os trata assim:
    o mesmo azul profundo, a mesma madeira clara, prateleiras que flutuam presas em
    metal preto e uma luz quente que nasce de dentro da própria peça. Marcenaria,
    serralheria e iluminação em LED saem da mesma fábrica, pela mesma equipe — e
    <b>uma só empresa responde por tudo o que está nestas folhas</b>.
    <em>Um contrato, uma data, um nome para chamar.</em></p></div>
 </div></div>''')

# ── 03 · a empresa e a infraestrutura ───────────────────────────────────
PIL = [
 ('01', 'O projeto pede mais que marcenaria.',
  'As prateleiras deste projeto vencem o vão presas na parede e em montantes de '
  'metalon preto, com a luz embutida na própria peça. Nada disso é só marcenaria — '
  'e tudo isso entra no nosso escopo, no mesmo contrato e na mesma data. '
  '<b>Vocês não contratam mais ninguém</b> para a marcenaria, a serralheria que a '
  'sustenta e a luz que a acende. O que fica fora vem nomeado — a pedra, por exemplo, '
  'é marmoraria: vocês não descobrem depois.'),
 ('02', 'A peça sai daqui conferida.',
  'Detalhamento, programação, usinagem, montagem e conferência acontecem dentro da '
  'nossa fábrica. Cada módulo é montado aqui antes de ser embalado: porta regulada, '
  'gaveta corrida, LED ligado para ver a luz. O que chega na obra chega para ser '
  'instalado, não para ser resolvido. A conferência é <b>etapa do processo</b>, não '
  'boa vontade no fim.'),
 ('03', 'Uma arquiteta responsável pelo projeto.',
  'Do orçamento aprovado à entrega, o projeto tem uma arquiteta nossa como '
  'responsável. É ela quem lê o executivo prancha por prancha, está na medição no '
  f'local e segue as peças pela fábrica até a instalação. Ela não substitui a {E(ARQ_CURTO)} '
  '— conversa com ela, na mesma linguagem técnica. <b>Vocês explicam o projeto uma '
  'vez, a uma pessoa.</b>'),
 ('04', 'O executivo de marcenaria é nosso.',
  'Antes de cortar, a Valvic desenha. O projeto de interiores diz o que o ambiente '
  'precisa ser; o nosso executivo de marcenaria diz como cada móvel se constrói — '
  'estrutura, ferragem, sentido de abertura, passagem de fiação, folga para o forno, '
  'a lava-louças e a bancada. É nele que a divergência aparece <em>no papel, antes '
  'de virar retrabalho</em>.'),
]
pil = '\n'.join(f'''<div class="c"><div class="n">{n}</div>
  <div class="t">{E(t)}</div><div class="d">{d}</div></div>''' for n, t, d in PIL)
folha(f'''<div class="pad">
 <div class="eyebrow">A empresa e a infraestrutura</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">A Valvic articula todas as soluções do projeto.</h1>
 <p class="lead" style="max-width:215mm">Um projeto raramente se perde na marcenaria.
  Ele se perde na costura entre os ofícios, quando cada um chega com contrato próprio,
  prazo próprio e medida própria. Aqui não há essa costura para fazer: os ofícios que
  esta proposta reúne entram no mesmo escopo, no mesmo contrato e na mesma data.</p>
 <div class="fr" style="margin-top:6mm;flex:1;min-height:0">{pil}</div>
 <div class="box" style="margin-top:5mm"><p style="font-size:9.4pt;color:var(--ink)">
   Na próxima folha, o caminho que o projeto percorre — etapa por etapa, até o dia
   em que a cozinha está em uso.</p></div>
</div>''')

# ── 04 · o processo, as doze etapas (as mesmas do caderno de referência) ─
BLOCOS = [
 ('Partida', 'da decisão ao contrato', [
  ('Decisão', 'Aprovação', 'Escopo, acabamentos e ferragens definidos. Nada entra em produção sem essa decisão.', 'Escopo fechado, móvel por móvel.'),
  ('Registro', 'Contrato', 'Contrato assinado, prazos e responsabilidades registrados. Tudo o que foi dito fica escrito.', 'Contrato e cronograma com datas.')]),
 ('Engenharia', 'da obra ao arquivo de máquina', [
  ('Parede', 'Medição técnica', 'Nossa equipe mede a obra no local. O projeto passa a conversar com a parede real.', 'Medidas da obra construída, não do desenho.'),
  ('Desenho', 'Detalhamento', 'Fechamos com vocês e com a arquitetura cada decisão de execução antes de cortar nada.', 'Nenhuma decisão de execução em aberto.'),
  ('Arquivo', 'Programação', 'O detalhamento vira arquivo de máquina. O erro é corrigido na tela, não na chapa.', 'Plano de corte e usinagem programado.')]),
 ('Fábrica', 'onde o móvel nasce e é testado', [
  ('Corte', 'Usinagem', 'Corte, furação, fresa e acabamento de borda. Tudo acontece dentro da nossa fábrica.', 'Peças prontas e identificadas, uma por uma.'),
  ('Encaixe', 'Montagem em fábrica', 'O móvel é montado aqui antes de ir para a obra. Problema de encaixe morre aqui.', 'Móvel montado e testado antes de sair.'),
  ('Checklist', 'Conferência', 'Peça por peça contra o projeto: medida, cor, ferragem, sentido de abertura, luz.', 'Checklist assinado antes do carregamento.')]),
 ('Entrega', 'da nossa fábrica à sua casa', [
  ('Carga', 'Transporte', 'Embalagem, carregamento e transporte são nossos, da fábrica até a porta da sua casa.', 'Móvel embalado e carregado por quem o montou.'),
  ('Prumo', 'Instalação', 'Equipe própria instala, nivela e regula. A obra recebe móvel pronto, não peça solta.', 'Móveis no lugar, nivelados e regulados.'),
  ('Teste', 'Vistoria técnica', 'Com vocês, abrimos tudo: cada porta, cada gaveta, cada luz. Nada passa sem testar.', 'Ajustes finais feitos na frente de vocês.'),
  ('Casa', 'Entrega final', 'Ambiente limpo, móvel em uso e termo de garantia na mão de vocês. O projeto virou casa.', 'Termo de garantia emitido e assinado.')]),
]
assert sum(len(b[2]) for b in BLOCOS) == 12
_n = [0]
def etapa(k, t, l, e):
    _n[0] += 1
    return f'''<div class="pe"><div class="pe-n">{_n[0]:02d}</div>
      <div class="pe-k">{E(k)}</div><div class="pe-t">{E(t)}</div>
      <div class="pe-l">{E(l)}</div><div class="pe-e">{E(e)}</div></div>'''
cols = '\n'.join(f'''<div class="pb"><div class="pb-h">{E(nm)}</div>
      <div class="pb-s">{E(sub)}</div>{''.join(etapa(*e) for e in ets)}</div>'''
                 for nm, sub, ets in BLOCOS)
folha(f'''<div class="pad" style="padding:13mm 15mm 20mm">
 <div class="eyebrow">O caminho do seu projeto</div><div class="rule"></div>
 <div style="display:flex;align-items:baseline;gap:9mm;margin-bottom:5mm">
  <h1 class="h1" style="margin:0">Doze etapas,<br>um só responsável</h1>
  <p class="lead" style="margin:0;max-width:112mm">Da decisão de vocês até a cozinha
    pronta são doze etapas — e nenhuma delas muda de dono.</p></div>
 <div class="rail"></div>
 <div class="proc">{cols}</div>
</div>''')

# ── 05 · a arquiteta responsável ────────────────────────────────────────
folha(f'''<div class="amb">
 <div class="amb-img"><img src="{IMG['vista6']}" alt="">
   <div class="tag">Jantar e cozinha</div></div>
 <div class="amb-txt" style="padding:15mm 15mm 21mm 12mm">
  <div class="eyebrow">Quem responde</div><div class="rule"></div>
  <h2 class="h2" style="margin:1mm 0 5mm">Uma arquiteta responsável, do começo ao fim</h2>
  <div style="color:var(--soft);font-size:9pt">
   <p style="margin:0 0 3mm">Do orçamento aprovado à entrega, o seu projeto tem uma
    <b>arquiteta responsável</b>. É ela que está na obra no dia da medição, detalha a
    execução junto com a {E(ARQ_CURTO)}, confere o móvel montado na fábrica e está na
    sua casa no dia da instalação.</p>
   <p style="margin:0 0 3mm">Você não explica o seu projeto duas vezes. Fala sempre com
    a mesma pessoa — e essa pessoa conhece o projeto inteiro, não um pedaço dele.</p>
   <p style="margin:0 0 3mm">Quando o móvel junta mais de um ofício — a prateleira de
    madeira, o montante de metal e a luz embutida — é com ela que você trata, e só com
    ela. Chega tudo na sua casa instalado, no mesmo acerto.</p></div>
  <div class="amb-nota" style="margin-top:auto"><div class="t">A fábrica</div>
   <p>Cinco das doze etapas acontecem dentro da nossa fábrica: detalhamento,
    programação, usinagem, montagem e conferência. O que chega na sua obra já
    funcionou uma vez — aqui.</p></div>
 </div></div>''', foot_r=True)

# ── 06 · índice ─────────────────────────────────────────────────────────
IDX = [('Cozinha · armários', 'MDF Azul Secreto e Tauari'),
       ('Cozinha · prateleiras suspensas', 'MDF Tauari e Mostrato, metal preto'),
       ('Jantar · prateleira', 'MDF Tauari, metal preto'),
       ('Serviço', 'MDF Azul Secreto, Tauari e Mostrato')]
assert [g for g, _ in IDX] == [g for g, _ in GRUPOS]
ix = ''.join(f'<div class="ix"><span class="ix-n">{i:02d}</span><span class="ix-t">{E(t)}</span>'
             f'<span class="ix-d">{E(d)}</span></div>' for i, (t, d) in enumerate(IDX, 1))
folha(f'''<div class="pad">
 <div class="eyebrow">Os ambientes</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">Cozinha, jantar e serviço,<br>um projeto só.</h1>
 <p class="lead" style="margin-bottom:5mm">Uma folha para cada conjunto, com o que a
    Valvic executa ali e em que material cada peça sai.</p>
 <div style="display:grid;grid-template-columns:1.1fr 1fr;gap:0 12mm;flex:1;min-height:0">
  <div>{ix}</div>
  <div class="amb-img" style="background:#fff;border:1px solid var(--hair)">
   <img src="{IMG['iso-prateleiras']}" alt="" style="object-fit:contain;padding:6mm">
   <div class="tag">Prateleiras da cozinha e do jantar</div></div>
 </div></div>''')

# ── 07…09 · as folhas de ambiente, SEM preço ────────────────────────────
PG = [
 ('A cozinha,<br>os armários.', ['iso-inferior01', 'vista5', 'iso-bancada02'], 'Cozinha',
  'MDF Azul Secreto Duratex · MDF Tauari Guararapes · interno em Branco TX',
  [('Armário da bancada do cooktop', 'Em Azul Secreto, com nicho para o forno de embutir, gavetas, gavetões de tempero e portas com puxador cava usinado na própria frente.'),
   ('Prateleiras em meia-lua', 'Na ponta da bancada, no mesmo azul, com a borda inteira arredondada.'),
   ('Armário da pia', 'Portas em Azul Secreto e o vão da lava-louças de embutir, medido pelo manual do aparelho.'),
   ('Armário superior azul', 'Portas com puxador cava na borda de baixo e interior livre para volumes maiores.'),
   ('Armário superior em Tauari', 'Portas basculantes que sobem e param onde você soltar, com luz em LED embutida por baixo.'),
   ('Prateleira de acabamento', 'Tampo espesso em Tauari sobre os armários superiores, com luz em LED encostada na parede.')]),
 ('A cozinha e o jantar,<br>as prateleiras.', ['vista4', 'iso-prateleiras'], 'Cozinha e jantar',
  'MDF Tauari Guararapes · MDF Mostrato Berneck · metalon preto · LED 3000K',
  [('Prateleiras suspensas da cozinha', 'Prateleiras espessas em Tauari e Mostrato, com as pontas em semicírculo, presas na parede por fixação invisível e em montantes de metal preto. A de baixo abre o espaço do depurador e acomoda o micro-ondas.'),
   ('Prateleira do jantar', 'Uma linha só em Tauari, de parede a parede, no mesmo desenho de borda arredondada e fixação invisível.'),
   ('Luz embutida', 'Fita de LED quente embutida no topo de cada prateleira, encostada na parede — a luz lava o revestimento e não aparece.')]),
 ('O serviço.', ['iso-vertical', 'vista7', 'iso-servico'], 'Serviço',
  'MDF Azul Secreto Duratex · MDF Tauari Guararapes · MDF Mostrato Berneck · interno em Branco TX',
  [('Armário de vassouras e despensa', 'Em Azul Secreto, portas altas com puxador redondo usinado, prateleiras de um lado e vão livre do outro.'),
   ('Gavetão de roupa suja', 'Na base do armário, frente ripada e vazada em Tauari, para a roupa respirar.'),
   ('Prateleira sobre a janela', 'Tampo espesso em Tauari que nasce no armário e atravessa a janela, com LED embutido.'),
   ('Trio de prateleiras', 'Em Tauari e Mostrato, com a borda acompanhando a parede e a ponta em semicírculo, presas em metal preto.'),
   ('Armário sob a bancada', 'Suspenso, em Tauari, com porta de abertura ampla ao lado da lava e seca.')]),
]
for titulo, imgs, tag, acab, itens in PG:
    band = ''.join(f'<img src="{IMG[i]}" alt="" style="flex:1;min-width:0;object-fit:'
                   f'{"contain;background:#fff" if i.startswith("iso") else "cover"}">'
                   for i in imgs)
    meio = (len(itens) + 1) // 2
    alt = 88 if len(itens) <= 4 else 76
    folha(f'''<div class="ambw">
     <div class="band" style="height:{alt}mm;display:flex;gap:2mm;background:#fff">{band}
       <div class="tag">{E(tag)}</div></div>
     <div class="low" style="display:block;padding:7mm 18mm 17mm">
      <div class="fitw">
       <div class="eyebrow">Ambiente</div><div class="rule"></div>
       <h2 class="h2" style="margin:1mm 0 3mm">{titulo}</h2>
       <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 11mm">
        <div>{mv(itens[:meio])}</div><div>{mv(itens[meio:])}</div></div>
       <div class="amb-nota" style="background:none;border-left-color:var(--line)">
         <div class="t">Acabamentos</div><p>{E(acab)}</p></div>
      </div>
     </div></div>''')

# ── 10 · a escolha: duas linhas, a diferença está na ferragem ───────────
DIF = [
 ('Corrediça',
  'Telescópica, com o trilho aparente na lateral da gaveta e sem amortecedor de fechamento.',
  'Oculta alemã: o trilho some por baixo, a gaveta abre inteira, fecha amortecida e não mostra ferragem na lateral.'),
 ('Dobradiça',
  'Nacional, com amortecimento no fechamento.',
  'Alemã, com amortecedor integrado e regulagem nos três sentidos.'),
 ('Básculas', 'Articulador premium de molas: a porta sobe e para onde você soltar. O mesmo nas duas linhas.',
  'O mesmo articulador premium.'),
 ('Iluminação', 'LED quente embutido na própria peça, entregue instalado. O mesmo nas duas linhas.',
  'O mesmo LED, entregue instalado.'),
 ('Garantia', CEN['Telescópica']['gar'], CEN['Hettich']['gar']),
]
linhas = ''.join(
    f'<tr><td class="l">{E(k)}</td><td style="text-align:left;font-size:8.6pt">{E(a)}</td>'
    f'<td class="hi" style="text-align:left;font-size:8.6pt">{E(b)}</td></tr>'
    for k, a, b in DIF)
folha(f'''<div class="pad">
 <div class="eyebrow">Uma escolha</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Duas linhas. A diferença está na ferragem.</h1>
 <p class="lead" style="max-width:215mm">O desenho, os padrões de MDF, as prateleiras,
   o metal e a luz são <b>os mesmos nas duas</b>. O que muda é a peça que vocês tocam
   todo dia — e é ela que decide quanto tempo o móvel continua fechando bem.</p>
 <table class="cmp" style="margin-top:6mm">
  <tr><th class="l" style="text-align:left"></th>
   {''.join(f'<th{" class=hi" if n == "Hettich" else ""}>{E(n)}</th>' for n in LIN)}</tr>
  {linhas}
 </table>
 <div class="box" style="margin-top:auto"><div class="t">O que o projeto especifica</div>
  <p>O executivo da {E(ARQ_CURTO)} pede <b>ferragem com amortecimento em toda a
   marcenaria</b>. A linha Hettich cumpre essa especificação nas portas e nas gavetas;
   a linha Telescópica é a versão econômica, com gaveta sem amortecedor.</p></div>
</div>''')

# ── 11 · a garantia ─────────────────────────────────────────────────────
PASSOS = [('Vocês nos chamam', 'Por telefone, WhatsApp ou e-mail, direto com a fábrica. Não há central, não há protocolo e não há intermediário.'),
          ('Respondemos em 24 horas', 'Esse é o nosso compromisso de retorno, contado a partir do chamado.'),
          ('Visita em até três dias úteis', 'Se não resolvermos pelo telefone, a equipe vai ao local. Dentro do prazo de garantia, a visita e o reparo não têm custo.')]
passos = ''.join(f'''<div class="pe"><div class="pe-n">{i:02d}</div>
     <div class="pe-t">{E(t)}</div><div class="pe-l">{E(d)}</div></div>'''
                 for i, (t, d) in enumerate(PASSOS, 1))
folha(f'''<div class="pad">
 <div class="eyebrow">Garantia</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O termo é assinado na entrega.</h1>
 <p class="lead" style="max-width:215mm">A garantia da Valvic <b>é escalonada pela
  ferragem</b>: dois anos na linha Telescópica, dez na linha Hettich. Não é promessa de
  proposta: é <b>termo assinado no dia da entrega</b>, junto com o guia de conservação
  do móvel.</p>
 <div class="three" style="margin-top:6mm">
  <div><div class="eyebrow" style="margin-bottom:3mm">Como se aciona</div>{passos}</div>
  <div><div class="eyebrow" style="margin-bottom:3mm">O que o termo cobre</div>
   <div class="term"><div class="k">Marcenaria</div>
    <div class="s">Estrutura, painéis, frentes e acabamento, pelo prazo da linha escolhida.</div></div>
   <div class="term"><div class="k">Ferragem de movimento</div>
    <div class="s">Corrediça, dobradiça e articulador, pelo prazo da linha escolhida.</div></div>
   <div class="term"><div class="k">Montagem e instalação</div>
    <div class="s">As instalações e regulagens têm garantia de dois anos em qualquer linha.</div></div></div>
  <div><div class="eyebrow" style="margin-bottom:3mm">O que fica de fora</div>
   <div class="term"><div class="k">Iluminação em LED</div>
    <div class="s">É componente eletrônico e segue a garantia do fabricante.</div></div>
   <div class="term"><div class="k">Desgaste de uso</div>
    <div class="s">Assim como o dano por umidade ou infiltração vinda da obra.</div></div>
   <div class="term"><div class="k">Alteração por terceiro</div>
    <div class="s">Feita no móvel depois da entrega.</div></div></div>
 </div></div>''')
N0 = N[0] + 1   # ⛔ a primeira folha com preço

# ── 12 · investimento, ambiente a ambiente, nas duas linhas ─────────────
rows = ''.join(
    f'<tr><td class="l">{E(g)}</td>'
    + ''.join(f'<td{" class=hi" if n == "Hettich" else ""}>{brs(CEN[n]["amb"][i])}</td>'
              for n in LIN) + '</tr>' for i, (g, _p) in enumerate(GRUPOS))
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · ambiente a ambiente</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O projeto, nas duas linhas.</h1>
 <p class="lead" style="max-width:215mm">Cada móvel foi levantado <b>peça por peça do
  projeto executivo</b> — nada é rateio nem estimativa por metro quadrado.</p>
 <div style="display:grid;grid-template-columns:1.25fr 1fr;gap:0 12mm;margin-top:6mm;flex:1;min-height:0">
  <table class="inv" style="align-self:start">
   <tr><th class="l">Ambiente</th>
    {''.join(f'<th{" class=hi" if n == "Hettich" else ""}>{E(n)}</th>' for n in LIN)}</tr>
   {rows}
   <tr class="tot"><td class="l">O projeto completo</td>
    {''.join(f'<td{" class=hi" if n == "Hettich" else ""}>{brs(CEN[n]["cheio"])}</td>' for n in LIN)}</tr>
  </table>
  <div class="amb-img" style="background:#fff;border:1px solid var(--hair)">
   <img src="{IMG['vista8']}" alt=""><div class="tag">Serviço</div></div>
 </div>
 <div class="box" style="margin-top:5mm"><p style="font-size:8.4pt">Valores de tabela,
  com entrada e saldo parcelado no cartão. <b>A folha de condições traz os descontos
  da casa para cada forma de pagamento.</b></p></div>
</div>''')

# ── 13 · a decisão ──────────────────────────────────────────────────────
RESUMO = {'Telescópica': 'Trilho aparente na lateral da gaveta e fechamento sem amortecedor. A versão econômica do projeto.',
          'Hettich': 'Trilho oculto, gaveta que sai inteira e fechamento amortecido em portas e gavetas. <em>É a linha que cumpre a especificação do projeto.</em>'}
# ⭐ [Jonathan 04/11] a folha da decisão mostra ENTRADA + PARCELA MENSAL no
#   cartão, não o montante. Sai do degrau de valor cheio da escala: 30% + 10×.
_lab, _d, _p, _mc = CEN['Telescópica']['escada'][0]
assert _d == 0 and '30%' in _lab and '10×' in _lab
PARC_N = 10
ENTR = {k: round(CEN[k]['cheio'] * 0.30, 2) for k in LIN}
PARC = {k: round((CEN[k]['cheio'] - ENTR[k]) / PARC_N, 2) for k in LIN}
for k in LIN:
    assert abs(ENTR[k] + PARC_N * PARC[k] - CEN[k]['cheio']) < 0.05
cards = ''.join(f'''<div class="c{" hi" if k == "Hettich" else ""}">
     <div class="anos">{E(CEN[k]['gar'].split()[0])}</div>
     <div class="unid">anos de garantia</div>
     <div class="nm">{E(CEN[k]['chamada'])}{' · a recomendação da casa' if k == 'Hettich' else ''}</div>
     <div class="x">{RESUMO[k]}</div>
     <div class="l"><div class="k">Entrada, na assinatura</div>
      <div class="v" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt">{br(ENTR[k])}</div>
      <div class="k" style="margin-top:2.5mm">Mais {PARC_N} parcelas mensais no cartão de crédito</div>
      <div class="v" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt">{PARC_N}× de {br(PARC[k])}</div></div></div>''' for k in LIN)
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · as duas linhas</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Dois anos, ou dez.</h1>
 <p class="lead" style="max-width:215mm">O mesmo projeto, o mesmo desenho e os mesmos
  padrões. A diferença é a <b>ferragem</b> — e o tempo pelo qual respondemos por ela.</p>
 <div class="gar justo" style="grid-template-columns:1fr 1fr">{cards}</div>
 <div class="box" style="margin-top:5mm"><div class="t">O que está incluso</div>
  <p>Projeto executivo de marcenaria, material, usinagem, ferragem, a estrutura em metal
   preto das prateleiras e a iluminação em LED embutida, transporte, montagem e
   instalação — num só contrato, com uma só data e uma só arquiteta responsável.
   A diferença entre as duas linhas está inteira na corrediça e na dobradiça.
   As demais formas de pagamento estão na folha de condições.</p></div>
</div>''')

# ── 14 · condições, com a escala de desconto padrão ─────────────────────
def pay(n):
    return ''.join(f'<tr><td>{E(lab)}</td><td class="d" style="color:var(--mut);font-weight:600">'
                   f'{"—" if d == 0 else f"−{d*100:.0f}%"}</td><td class="d">{br(p)}</td></tr>'
                   for lab, d, p, _mc in CEN[n]['escada'])
folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Prazo, pagamento e fronteiras.</h1>
 <div class="three" style="grid-template-columns:.85fr 1.5fr .95fr">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div><div class="v">{E(VALIDADE)}</div>
     <div class="s">A partir desta data.</div></div>
   <div class="term"><div class="k">Prazo de execução</div><div class="v">{E(PRAZO)}</div>
     <div class="s">Contados da aprovação do detalhamento de execução, não da assinatura.
       A medição técnica entra antes e tem data própria no cronograma.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">Conforme a linha</div>
     <div class="s">Dez anos na linha Hettich e dois na Telescópica. Instalação e regulagem,
       dois anos. Termo assinado na entrega.</div></div>
   <div class="term"><div class="k">Projeto executivo de marcenaria</div><div class="v">Incluso</div>
     <div class="s">Aprovado por vocês e pela {E(ARQ_CURTO)} antes de qualquer corte.</div></div>
  </div>
  <div>
   <div class="eyebrow" style="margin-bottom:2mm">Formas de pagamento · linha Hettich</div>
   <table class="pay" style="width:100%">{pay('Hettich')}</table>
   <div class="eyebrow" style="margin:5mm 0 2mm">Formas de pagamento · linha Telescópica</div>
   <table class="pay" style="width:100%">{pay('Telescópica')}</table>
   <div style="font-size:7.4pt;color:var(--mut);margin-top:2.5mm;letter-spacing:.04em">
     A entrada é paga na assinatura do contrato, por transferência ou PIX.</div>
  </div>
  <div class="fora">
   <div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>
    <li><div class="k">Pedra</div><div class="v">As bancadas em granilite da cozinha e do
      serviço, os sóculos e o canto alemão são marmoraria e obra, e não entram no escopo
      da Valvic. A marcenaria é medida depois da bancada no lugar.</div></li>
    <li><div class="k">Gaveteiro sob a escada</div><div class="v">Não entra nesta
      proposta e pode ser levantado à parte.</div></li>
    <li><div class="k">Eletrodomésticos e metais</div><div class="v">Cooktop, forno,
      micro-ondas, depurador, geladeira, lava-louças, lava e seca, cubas, tanque,
      torneiras e lixeira.</div></li>
    <li><div class="k">Obra civil e instalações</div><div class="v">Alvenaria, elétrica,
      hidráulica, revestimentos, forro e pintura de parede.</div></li>
    <li><div class="k">Decoração</div><div class="v">Mesa e cadeiras do jantar, varal,
      persiana, cortinas, tapetes, vasos e objetos.</div></li>
   </ul>
  </div>
 </div>
 <div class="sig"><div class="ln">{E(CLIENTE)}</div>
   <div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

# ── 15 · encerramento ───────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome" style="font-size:36pt">Um contrato.<br>Uma data.<br>Um nome<br>para chamar.</div>
  <div class="cv-s">Obrigado pela confiança de pôr este projeto na nossa mão.
   O desenho da {E(ARQ_CURTO)} sai da nossa fábrica e chega instalado.</div>
  <div class="cv-meta">
   <div><div class="k">Proposta</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['vista7']}" alt=""></div>
</div>''', dark=True, rodape=False)

# ── estilo: o mesmo EXTRA do caderno de referência ──────────────────────
src = (P / 'build-gustavo-caderno.py').read_text(encoding='utf-8')
EXTRA = re.search(r"EXTRA = '''(.*?)'''", src, re.S).group(1)
AJUSTE = re.search(r"AJUSTE = '''(.*?)'''", src, re.S).group(1)
EXTRA += '''
.pay td{font-size:8.2pt;padding:1.7mm 0}
.pay td.d{padding-left:4mm;white-space:nowrap}
.gar .c .selo{margin-bottom:2mm}
'''
HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {E(CLIENTE)} · Cozinha</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
        '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S)
        + f'<script>{AJUSTE}caber();</script></body></html>')

# ── as travas ───────────────────────────────────────────────────────────
NF = 15
assert len(S) == NF, len(S)
assert 'R$' not in ''.join(S[:N0 - 1]), '⛔⛔ PREÇO ANTES DA FOLHA DE VALOR'
_texto = re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S))
_texto = re.sub(r'<[^>]+>', ' ', _texto)
for _c in ('Michell', 'Michelle', 'Jéssica', 'Jessica', 'Arlei', 'Iara Cezar',
           'Lagoa Santa', 'Gustavo', 'Luiza Pacheco', 'Vale dos Pinhais'):
    assert _c not in _texto, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE: {_c}'
assert not [c for c in '⭐⛔⚠' if c in ''.join(S)], '⛔ marcação interna'
# ⛔ sem metragem nem contagem de peça nas folhas de ambiente
_amb = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(S[6:9])))
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco|seis)\s+(portas?|gavet\w+|prateleiras?)',
                     _amb, re.I), '⛔ contagem na descrição'

OUT = R / 'proposta-rafael-cozinha.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-rafael-cozinha.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {NF} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
for n in LIN:
    print(f'  {n:12s} cheio {br(CEN[n]["cheio"])} · ambientes {CEN[n]["amb"]}')
