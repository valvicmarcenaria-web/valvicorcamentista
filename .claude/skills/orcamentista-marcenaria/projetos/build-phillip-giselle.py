# -*- coding: utf-8 -*-
"""PHILLIP E GISELLE — caderno de proposta  [04/11/2026]

⭐ Layout do caderno do MICHELL (ICA) na versão revisada do GUSTAVO RAPOSO:
  A4 paisagem · capa · abertura · a empresa · as doze etapas · a arquiteta ·
  índice · folhas de ambiente SEM preço · as três linhas · garantia ·
  investimento · decisão · condições · encerramento.
⛔ Só a estrutura vem de lá: nenhum nome, número ou imagem de outro cliente.
⛔ Nenhum número digitado: tudo sai de `phillip-giselle/precos.py`.
⛔ Sem metragem e sem contagem nas descrições.
⭐ Pagamento como no Michell e no Gustavo: 30/20/20/30 por transferência,
  sem cartão e sem escala de desconto [Jonathan, 04/11/2026].
⭐ Imagens: os renders do executivo da Janaina Pacheco. Closets da Ana e do
  Mateus e rouparia não têm render, e os desenhos trazem cota: folha só texto.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'phillip-giselle'
sys.path.insert(0, str(R))
os.chdir(R)
with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')

CLIENTE = 'Phillip e Giselle'
ARQ, ARQ_CURTO = 'Janaina Pacheco Arquitetura & Interiores', 'Janaina Pacheco'
OBRA, DATA = 'Residência unifamiliar · pavimento íntimo', 'Novembro de 2026'
PRAZO, VALIDADE = '45 a 60 dias úteis', '7 dias úteis'
LIN = ('telescopica', 'hettich', 'blum')
NOME = {'telescopica': 'Telescópica', 'hettich': 'Hettich', 'blum': 'Blum'}
GAR = {'telescopica': '2', 'hettich': '10', 'blum': '30'}
CHAMADA = {'telescopica': 'Linha Telescópica', 'hettich': 'Linha Hettich · oculta alemã',
           'blum': 'Linha Blum'}
DESTAQUE = 'hettich'

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
IMG = {p.stem: 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
       for p in (P / 'img-phillip-giselle').glob('*.jpg') if not p.stem.startswith('des-')}

TAB = PR.TAB
def amb_total(k, a): return sum(v for x, v in TAB[k]['pv'].items() if x[0] == a)

S, N = [], [0]
def folha(corpo, dark=False, rodape=True, foot_r=False):
    N[0] += 1
    f = (f'<div class="foot{" r" if foot_r else ""}"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span>'
         f'<span>{N[0]:02d}</span></div>') if rodape else ''
    S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')

def mv(itens):
    return ''.join(f'''<div class="mv"><span class="b"></span><span>
      <span class="t">{E(t)}</span> <span class="d">{E(d)}</span></span></div>''' for t, d in itens)

# ── 01 · capa ───────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">Phillip<br>e Giselle</div>
  <div class="cv-s">Os quartos, os closets e a circulação<br>
     do pavimento íntimo, do desenho à instalação.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">{E(ARQ_CURTO)}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Linhas</div><div class="v">Telescópica · Hettich · Blum</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['casal-01']}" alt=""></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''', dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
folha(f'''<div class="ambw">
 <div class="band" style="height:104mm"><img src="{IMG['fachada']}" alt="" style="object-position:50% 40%">
   <div class="tag">A casa</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">O que esta casa pede</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">Um pavimento inteiro. Uma empresa só.</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">A suíte do casal, os quartos da
    Ana e do Mateus, os closets, a rouparia e a circulação que os une — um só projeto da
    <b>{E(ARQ)}</b>, com painéis que escondem as portas, ripado de madeira, espelho com luz
    embutida e armários do piso ao forro. <b>Uma só empresa responde por tudo o que está
    nestas folhas</b>, da medição à instalação. <em>Um contrato, uma data, um nome para
    chamar.</em></p></div>
 </div></div>''')

# ── 03 · a empresa e a infraestrutura ───────────────────────────────────
PIL = [
 ('01', 'O projeto pede mais que marcenaria.',
  'Painel que esconde porta, ripado com metalon contra empeno, espelho com luz embutida, '
  'sistema de correr com amortecimento. Tudo isso entra no nosso escopo, no mesmo contrato '
  'e na mesma data. <b>Vocês não contratam mais ninguém</b> para a marcenaria e para o que '
  'faz parte dela. O que fica fora vem nomeado — a pedra, por exemplo, é marmoraria.'),
 ('02', 'A peça sai daqui conferida.',
  'Detalhamento, programação, usinagem, montagem e conferência acontecem dentro da nossa '
  'fábrica. Cada módulo é montado aqui antes de ser embalado: porta regulada, gaveta corrida, '
  'LED ligado para ver a luz. A conferência é <b>etapa do processo</b>, não boa vontade no fim.'),
 ('03', 'Uma arquiteta responsável pelo projeto.',
  'Do orçamento aprovado à entrega, o projeto tem uma arquiteta nossa como responsável. É ela '
  f'quem lê o executivo prancha por prancha, está na medição e segue as peças pela fábrica. Ela '
  f'conversa com a {E(ARQ_CURTO)} na mesma linguagem técnica. <b>Vocês explicam o projeto uma '
  'vez, a uma pessoa.</b>'),
 ('04', 'O executivo de marcenaria é nosso.',
  'Antes de cortar, a Valvic desenha. O projeto de interiores diz o que o ambiente precisa ser; '
  'o nosso executivo diz como cada móvel se constrói — estrutura, ferragem, sentido de abertura, '
  'folga das portas no painel. É nele que a divergência aparece <em>no papel, antes de virar '
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
  <p class="lead" style="margin:0;max-width:112mm">Da decisão de vocês até a casa pronta são
    doze etapas — e nenhuma delas muda de dono.</p></div>
 <div class="rail"></div><div class="proc">{cols}</div>
</div>''')

# ── 05 · a arquiteta responsável ────────────────────────────────────────
folha(f'''<div class="amb">
 <div class="amb-img"><img src="{IMG['fachada-02']}" alt=""><div class="tag">A casa</div></div>
 <div class="amb-txt" style="padding:15mm 15mm 21mm 12mm">
  <div class="eyebrow">Quem responde</div><div class="rule"></div>
  <h2 class="h2" style="margin:1mm 0 5mm">Uma arquiteta responsável, do começo ao fim</h2>
  <div style="color:var(--soft);font-size:9pt">
   <p style="margin:0 0 3mm">Do orçamento aprovado à entrega, o seu projeto tem uma
    <b>arquiteta responsável</b>. É ela que está na obra no dia da medição, detalha a execução
    junto com a {E(ARQ_CURTO)}, confere o móvel montado na fábrica e está na sua casa no dia
    da instalação.</p>
   <p style="margin:0 0 3mm">Vocês não explicam o projeto duas vezes. Falam sempre com a
    mesma pessoa — e essa pessoa conhece o pavimento inteiro, não um pedaço dele.</p>
   <p style="margin:0 0 3mm">Quando o móvel junta mais de um ofício — o painel que esconde a
    porta, o ripado com estrutura metálica, o espelho com luz — é com ela que vocês tratam, e
    só com ela.</p></div>
  <div class="amb-nota" style="margin-top:auto"><div class="t">A fábrica</div>
   <p>Cinco das doze etapas acontecem dentro da nossa fábrica: detalhamento, programação,
    usinagem, montagem e conferência. O que chega na sua obra já funcionou uma vez — aqui.</p></div>
 </div></div>''', foot_r=True)

# ── 06 · índice ─────────────────────────────────────────────────────────
MAT = {'Quarto casal': 'Ripado amadeirado, MDF Areia, espelho',
       'Closet casal': 'MDF Areia, espelho prata',
       'Suíte Ana': 'MDF branco liso, painel em cor',
       'Closet Ana': 'MDF Tartufo',
       'Quarto Mateus': 'MDF Grafite',
       'Closet Mateus': 'MDF Grafite',
       'Rouparia': 'MDF branco liso',
       'Circulação': 'Painel em cor, portas mimetizadas'}
assert list(MAT) == PR.ORDEM
ix = ''.join(f'<div class="ix"><span class="ix-n">{i:02d}</span><span class="ix-t">{E(a)}</span>'
             f'<span class="ix-d">{E(MAT[a])}</span></div>' for i, a in enumerate(PR.ORDEM, 1))
folha(f'''<div class="pad">
 <div class="eyebrow">Os ambientes</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">Oito ambientes,<br>um pavimento inteiro.</h1>
 <p class="lead" style="margin-bottom:5mm">Uma folha para cada conjunto, com o que a Valvic
    executa ali e em que material cada peça sai.</p>
 <div style="display:grid;grid-template-columns:1.1fr 1fr;gap:0 12mm;flex:1;min-height:0">
  <div>{ix}</div>
  <div class="amb-img"><img src="{IMG['mateus-02']}" alt=""><div class="tag">Quarto Mateus</div></div>
 </div></div>''')

# ── 07… · as folhas de ambiente, SEM preço ──────────────────────────────
PG = [
 ('A suíte<br>do casal.', ['casal-01', 'casal-02'], 'Quarto casal',
  'Ripado amadeirado · MDF Areia · espelho prata · LED 3000K',
  [('Portas ripadas de correr', 'As portas do closet e do banho, em ripado amadeirado do lado do quarto e Areia do lado de dentro, correm com amortecimento rente ao painel ripado.'),
   ('Mesa rack suspensa', 'Em Areia, atravessa a parede do espelho até os nichos, com gavetas sob o tampo.'),
   ('Torre de nichos', 'Em amadeirado, do piso ao forro no canto da parede, para livros e objetos.'),
   ('Espelho com luz', 'Espelho prata do piso ao forro, com luz quente embutida nas laterais.'),
   ('Cabeceira', 'Em Areia, de parede a parede, com luz quente no topo que lava a parede.'),
   ('Mesinhas de cabeceira', 'Em Areia, com gaveta, sobre base marmorizada.')]),
 ('O closet<br>do casal.', ['closet-casal'], 'Closet casal',
  'MDF Areia por dentro e por fora · espelho prata',
  [('Armários do piso ao forro', 'Em Areia, com portas de correr e puxador cava usinado na própria frente: maleiros, cabideiros, prateleiras e gavetas internas.'),
   ('Sapateira com espelho', 'Portas de correr inteiras em espelho prata, que ampliam o closet e servem de espelho de corpo.'),
   ('Fechamento superior', 'Faixa em Areia no encontro com o forro, em todo o perímetro, que fecha o closet como uma peça só.')]),
 ('A suíte<br>da Ana.', ['ana-janela'], 'Suíte Ana',
  'MDF branco liso · painel em material de cor',
  [('Móvel da janela', 'Nichos com prateleiras dos dois lados da janela e um banco sob ela, com gavetões que guardam o que o quarto precisa esconder.'),
   ('Painel com portas mimetizadas', 'Painel de parede inteira em que as portas pivotantes desaparecem: fechadas, a parede fica lisa.')]),
 ('O quarto<br>do Mateus.', ['mateus-01', 'mateus-02'], 'Quarto Mateus',
  'MDF Grafite · LED 3000K',
  [('Mesa do computador', 'Em Grafite, com gaveteiro sob o tampo.'),
   ('Prateleiras suspensas', 'Sobre a mesa, com alma de aço por dentro contra a flecha das prateleiras longas.'),
   ('Cabeceira', 'Em Grafite, de parede a parede, com luz quente no topo.'),
   ('Mesas de cabeceira', 'Em Grafite, nos dois lados da cama.'),
   ('Painel com porta oculta', 'Painel em Grafite na parede da TV, com a porta do closet escondida no mesmo material.')]),
]
for titulo, imgs, tag, acab, itens in PG:
    if len(imgs) == 1:
        folha(f'''<div class="amb">
         <div class="amb-img"><img src="{IMG[imgs[0]]}" alt=""><div class="tag">{E(tag)}</div></div>
         <div class="amb-txt{" curto" if len(itens) <= 3 else ""}">
          <div class="eyebrow">Ambiente</div><div class="rule"></div>
          <div class="fit"><h2 class="h2" style="margin:1mm 0 4mm">{titulo}</h2>{mv(itens)}
           <div class="amb-nota" style="background:none;border-left-color:var(--line)">
             <div class="t">Acabamentos</div><p>{E(acab)}</p></div></div>
         </div></div>''', foot_r=True)
    else:
        band = ''.join(f'<img src="{IMG[i]}" alt="" style="flex:1;min-width:0">' for i in imgs)
        meio = (len(itens) + 1) // 2
        folha(f'''<div class="ambw">
         <div class="band" style="height:{88 if len(itens) <= 4 else 76}mm;display:flex;gap:2mm">{band}
           <div class="tag">{E(tag)}</div></div>
         <div class="low" style="display:block;padding:7mm 18mm 17mm"><div class="fitw">
           <div class="eyebrow">Ambiente</div><div class="rule"></div>
           <h2 class="h2" style="margin:1mm 0 3mm">{titulo}</h2>
           <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 11mm">
            <div>{mv(itens[:meio])}</div><div>{mv(itens[meio:])}</div></div>
           <div class="amb-nota" style="background:none;border-left-color:var(--line)">
             <div class="t">Acabamentos</div><p>{E(acab)}</p></div></div>
         </div></div>''')

# ── closets da Ana e do Mateus · rouparia e circulação ──────────────────
folha(f'''<div class="pad">
 <div class="eyebrow">Ambiente</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Os closets da Ana e do Mateus.</h1>
 <p class="lead" style="max-width:215mm">Dois closets irmãos, com o mesmo desenho e a mesma
  construção — cada um na cor do seu quarto. Armário em L do piso ao forro, que aproveita as
  duas paredes e deixa o centro livre.</p>
 <div class="three" style="grid-template-columns:1fr 1fr;margin-top:7mm">
  <div><div class="eyebrow" style="margin-bottom:3mm">Closet Ana · MDF Tartufo</div>
   {mv([('Armário em L', 'Portas de correr com puxador perfil, maleiros no alto, cabideiros, prateleiras e gavetas internas.'),
        ('Por dentro e por fora', 'O mesmo Tartufo nas frentes, na caixa e no interno: abrir a porta é ver o mesmo móvel.')])}</div>
  <div><div class="eyebrow" style="margin-bottom:3mm">Closet Mateus · MDF Grafite</div>
   {mv([('Armário em L', 'A mesma composição do closet da Ana, no Grafite do quarto do Mateus.'),
        ('Por dentro e por fora', 'Grafite nas frentes, na caixa e no interno.')])}</div>
 </div>
 <div class="box" style="margin-top:auto"><div class="t">O canto do L</div>
  <p>O encontro das duas alas é resolvido no nosso executivo, na medição: é ali que se decide
   o acesso ao canto, antes de qualquer corte.</p></div>
</div>''')

folha(f'''<div class="amb">
 <div class="amb-img"><img src="{IMG['circulacao']}" alt="" style="object-position:30% 50%">
   <div class="tag">Circulação</div></div>
 <div class="amb-txt">
  <div class="eyebrow">Ambiente</div><div class="rule"></div>
  <div class="fit"><h2 class="h2" style="margin:1mm 0 4mm">A circulação<br>e a rouparia.</h2>
   {mv([('Painel da circulação', 'Em toda a extensão do corredor, em material de cor, com as portas pivotantes dos quartos mimetizadas no painel: o corredor vira uma parede só.'),
        ('Rouparia', 'Armários em L do piso ao forro em branco liso, com portas de correr e prateleiras corridas reforçadas com alma de aço.')])}
   <div class="amb-nota" style="background:none;border-left-color:var(--line)">
     <div class="t">Acabamentos</div><p>Painel em material de cor · rouparia em MDF branco liso</p></div></div>
 </div></div>''', foot_r=True)

# ── a escolha: três linhas, a diferença está na ferragem ────────────────
DIF = [
 ('Corrediça', 'Telescópica, com o trilho aparente na lateral da gaveta e sem amortecedor.',
  'Oculta alemã: o trilho some por baixo, a gaveta abre inteira e fecha amortecida.',
  'Oculta Blum: a mesma discrição, com o curso mais macio e a maior capacidade de carga das três.'),
 ('Dobradiça', 'Nacional, com amortecimento.', 'Alemã, com amortecedor e regulagem nos três sentidos.',
  'Blum, com amortecedor e regulagem nos três sentidos.'),
 ('Portas de correr e pivotantes', 'Os mesmos sistemas nas três linhas.', 'Os mesmos sistemas.', 'Os mesmos sistemas.'),
 ('Iluminação', 'LED quente embutido na peça, entregue instalado. O mesmo nas três.', 'O mesmo LED.', 'O mesmo LED.'),
 ('Garantia', f"{GAR['telescopica']} anos", f"{GAR['hettich']} anos", f"{GAR['blum']} anos"),
]
linhas = ''.join(f'<tr><td class="l">{E(k)}</td>' + ''.join(
    f'<td{" class=hi" if L == DESTAQUE else ""} style="text-align:left;font-size:8.3pt">{E(v)}</td>'
    for L, v in zip(LIN, vs)) + '</tr>' for k, *vs in DIF)
folha(f'''<div class="pad">
 <div class="eyebrow">Uma escolha</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Três linhas. A diferença está na ferragem.</h1>
 <p class="lead" style="max-width:215mm">O desenho, os padrões de MDF, os painéis, as portas e
   a luz são <b>os mesmos nas três</b>. O que muda é a peça que vocês tocam todo dia — a
   corrediça e a dobradiça — e é ela que decide quanto tempo o móvel continua fechando bem.</p>
 <table class="cmp" style="margin-top:6mm">
  <tr><th class="l" style="text-align:left"></th>
   {''.join(f'<th{" class=hi" if L == DESTAQUE else ""}>{E(NOME[L])}</th>' for L in LIN)}</tr>
  {linhas}</table>
 <div class="box" style="margin-top:auto"><div class="t">O que não muda</div>
  <p>Os padrões especificados pela arquiteta, os painéis com portas mimetizadas, o ripado, os
   sistemas de correr, o espelho, a iluminação entregue instalada e a equipe própria do corte
   à montagem. <b>Os ambientes sem gaveta nem dobradiça têm o mesmo valor nas três linhas.</b></p></div>
</div>''')

# ── a garantia ──────────────────────────────────────────────────────────
PASSOS = [('Vocês nos chamam', 'Por telefone, WhatsApp ou e-mail, direto com a fábrica. Sem central e sem intermediário.'),
          ('Respondemos em 24 horas', 'Esse é o nosso compromisso de retorno, contado a partir do chamado.'),
          ('Visita em até três dias úteis', 'Se não resolvermos pelo telefone, a equipe vai ao local. Dentro do prazo de garantia, visita e reparo não têm custo.')]
passos = ''.join(f'''<div class="pe"><div class="pe-n">{i:02d}</div><div class="pe-t">{E(t)}</div>
  <div class="pe-l">{E(d)}</div></div>''' for i, (t, d) in enumerate(PASSOS, 1))
cards = ''.join(f'''<div class="c{" hi" if L == DESTAQUE else ""}"><div class="anos">{GAR[L]}</div>
  <div class="unid">anos de garantia</div><div class="nm">{E(CHAMADA[L])}</div></div>''' for L in LIN)
folha(f'''<div class="pad">
 <div class="eyebrow">Garantia</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O termo é assinado na entrega.</h1>
 <p class="lead" style="max-width:215mm">A garantia da Valvic <b>é escalonada pela ferragem</b>
  e vale para o projeto inteiro pelo prazo da linha escolhida. Não é promessa de proposta: é
  <b>termo assinado no dia da entrega</b>, junto com o guia de conservação do móvel.</p>
 <div class="gar justo" style="margin-top:5mm">{cards}</div>
 <div class="three" style="margin-top:6mm">
  <div><div class="eyebrow" style="margin-bottom:3mm">Como se aciona</div>{passos}</div>
  <div><div class="eyebrow" style="margin-bottom:3mm">O que o termo cobre</div>
   <div class="term"><div class="k">Marcenaria e ferragem de movimento</div>
    <div class="s">Estrutura, painéis, frentes, corrediças e dobradiças, pelo prazo da linha.</div></div>
   <div class="term"><div class="k">Montagem e instalação</div>
    <div class="s">Instalações e regulagens têm garantia de dois anos em qualquer linha.</div></div></div>
  <div><div class="eyebrow" style="margin-bottom:3mm">O que fica de fora</div>
   <div class="term"><div class="k">Iluminação em LED</div>
    <div class="s">Componente eletrônico, segue a garantia do fabricante.</div></div>
   <div class="term"><div class="k">Desgaste, umidade e alteração por terceiro</div>
    <div class="s">Dano vindo da obra ou mudança feita no móvel depois da entrega.</div></div></div>
 </div></div>''')
N0 = N[0] + 1   # ⛔ a primeira folha com preço

# ── a decisão: as três linhas ───────────────────────────────────────────
RESUMO = {'telescopica': 'Trilho aparente na gaveta e fechamento sem amortecedor. A versão econômica do projeto.',
          'hettich': 'Trilho oculto, gaveta que sai inteira e fechamento amortecido. <em>A recomendação da casa.</em>',
          'blum': 'O curso mais macio e a maior capacidade de carga — o topo da ferragem, com trinta anos de garantia.'}
cards = ''.join(f'''<div class="c{" hi" if L == DESTAQUE else ""}"><div class="anos">{GAR[L]}</div>
  <div class="unid">anos de garantia</div><div class="nm">{E(CHAMADA[L])}</div>
  <div class="x">{RESUMO[L]}</div>
  <div class="l"><div class="k">O projeto completo</div>
   <div class="v" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:20pt">{br(TAB[L]['venda'])}</div>
   <div class="k" style="margin-top:2mm">Entrada, na assinatura</div>
   <div class="v">{br(TAB[L]['venda'] * PR.PAGTO[0][1])}</div></div></div>''' for L in LIN)
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · as três linhas</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Dois anos, dez, ou trinta.</h1>
 <p class="lead" style="max-width:215mm">O mesmo projeto, o mesmo desenho e os mesmos padrões.
  A diferença é a <b>ferragem</b> — e o tempo pelo qual respondemos por ela.</p>
 <div class="gar justo">{cards}</div>
 <div class="box" style="margin-top:5mm"><div class="t">O que está incluso</div>
  <p>Projeto executivo de marcenaria, material, usinagem, ferragem, a estrutura metálica do
   ripado, o espelho, a iluminação em LED embutida, transporte, montagem e instalação — num só
   contrato, com uma só data e uma só arquiteta responsável.</p></div>
</div>''')

# ── investimento, ambiente a ambiente, nas três linhas ──────────────────
rows = ''.join(f'<tr><td class="l">{E(a)}</td>' + ''.join(
    f'<td{" class=hi" if L == DESTAQUE else ""}>{brs(amb_total(L, a))}</td>' for L in LIN) + '</tr>'
    for a in PR.ORDEM)
IGUAIS = [a for a in PR.ORDEM if len({amb_total(L, a) for L in LIN}) == 1]
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · ambiente a ambiente</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O pavimento, nas três linhas.</h1>
 <p class="lead" style="max-width:215mm">Cada móvel foi levantado <b>peça por peça do projeto
  executivo</b> — nada é rateio nem estimativa por metro quadrado. Valores em reais.</p>
 <table class="inv" style="margin-top:5mm">
  <tr><th class="l">Ambiente</th>
   {''.join(f'<th{" class=hi" if L == DESTAQUE else ""}>{E(NOME[L])}</th>' for L in LIN)}</tr>
  {rows}
  <tr class="tot"><td class="l">O projeto completo</td>
   {''.join(f'<td{" class=hi" if L == DESTAQUE else ""}>{brs(TAB[L]["venda"])}</td>' for L in LIN)}</tr>
 </table>
 <div class="box" style="margin-top:auto"><p style="font-size:8.4pt"><b>{E(', '.join(IGUAIS[:-1]))}
  e {E(IGUAIS[-1])}</b> têm o mesmo valor nas três linhas: neles não há corrediça nem dobradiça
  que mude de linha.</p></div>
</div>''')

# ── condições ───────────────────────────────────────────────────────────
pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{p*100:.0f}%</td></tr>' for r, p in PR.PAGTO)
avd, avv, avo = PR.AVULSO[0]
folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Prazo, pagamento e fronteiras.</h1>
 <div class="three">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div><div class="v">{E(VALIDADE)}</div>
     <div class="s">A partir desta data.</div></div>
   <div class="term"><div class="k">Prazo de execução</div><div class="v">{E(PRAZO)}</div>
     <div class="s">Contados da aprovação do detalhamento de execução, não da assinatura. A
       medição técnica entra antes e tem data própria no cronograma.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">Conforme a linha</div>
     <div class="s">Trinta anos na Blum, dez na Hettich e dois na Telescópica. Instalação e
       regulagem, dois anos. Termo assinado na entrega.</div></div>
   <div class="term"><div class="k">Projeto executivo de marcenaria</div><div class="v">Incluso</div>
     <div class="s">Aprovado por vocês e pela {E(ARQ_CURTO)} antes de qualquer corte.</div></div>
  </div>
  <div>
   <table class="pay" style="width:100%">
    <tr><td colspan="2" style="border:none;padding-bottom:2mm"><span class="eyebrow">Formas de pagamento</span></td></tr>
    {pay}</table>
   <div style="font-size:7.4pt;color:var(--mut);margin-top:2.5mm;letter-spacing:.06em">
     Todas as parcelas por transferência bancária.</div>
   <div class="box" style="margin-top:5mm"><div class="t">Serviço avulso · {br(avv)}</div>
    <p>{E(avd)}. <b>{E(avo.capitalize())}</b>: a recuperação depende do estado do painel
     existente.</p></div>
  </div>
  <div class="fora">
   <div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>
    <li><div class="k">Banheiros</div><div class="v">Gabinetes, armários de espelho e
      cristaleiras dos banhos não entram nesta proposta.</div></li>
    <li><div class="k">Pedra e vidro avulso</div><div class="v">Bancadas, revestimentos em
      mármore, as cristaleiras de vidro e a estante de metal do quarto do Mateus.</div></li>
    <li><div class="k">Outros pavimentos</div><div class="v">Academia, rooftop e fachada, e o
      bar da circulação.</div></li>
    <li><div class="k">Obra, luminárias e eletros</div><div class="v">Alvenaria, elétrica,
      spots e perfis de forro, metais, eletrodomésticos e as portas de passagem que não estão
      nos painéis desta proposta.</div></li>
    <li><div class="k">Decoração</div><div class="v">Camas, recamier, tapetes, cadeiras,
      TVs e objetos.</div></li>
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
   {E(ARQ_CURTO)} sai da nossa fábrica e chega instalado.</div>
  <div class="cv-meta">
   <div><div class="k">Proposta</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['ana-janela']}" alt=""></div>
</div>''', dark=True, rodape=False)

# ── estilo e montagem ───────────────────────────────────────────────────
EXTRA = re.search(r"EXTRA = '''(.*?)'''", src, re.S).group(1)
AJUSTE = re.search(r"AJUSTE = '''(.*?)'''", src, re.S).group(1)
EXTRA += '''
.gar .c .selo{margin-bottom:2mm}
.cmp td.l{width:30mm}
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
for _c in ('Michell', 'Michelle', 'Jéssica', 'Jessica', 'Arlei', 'Iara Cezar', 'Gustavo',
           'Luiza Pacheco', 'Rafael', 'Clara Dobscha', 'Lagoa Santa', 'Vale dos Pinhais'):
    assert _c not in _t, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE: {_c}'
assert not [c for c in '⭐⛔⚠' if c in ''.join(S)], '⛔ marcação interna'
for _p in ('cartão', 'cartao', 'desconto', 'valor cheio'):
    assert _p not in _t.lower(), f'⛔ a peça fala em "{_p}"'
_amb = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(S[6:N0 - 3])))
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco|seis)\s+(portas?|gavet\w+|prateleiras?)', _amb, re.I), '⛔ contagem'
assert sum(amb_total('hettich', a) for a in PR.ORDEM) == TAB['hettich']['venda']

OUT = R / 'proposta-phillip-giselle.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-phillip-giselle.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {NF} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
for L in LIN: print(f'  {NOME[L]:12s} {br(TAB[L]["venda"])}')
