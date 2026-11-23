# -*- coding: utf-8 -*-
"""APARTAMENTO MR · MARIANA DINIZ BRAZ — caderno de proposta, Telescópica e Hettich  [23/11/2026]

⭐ [Jonathan, 23/11/2026] RT 10% · nota 9% · "vamos propor os 2 cenários (telescópica, hettich)" ·
  Belo Horizonte · 90 dias corridos · 40% de entrada + 20% a 30, 60 e 90 dias · validade 5 dias.
⭐ Caderno do Gran Royalle (duas linhas), com os renders da arquiteta Bruna Teixeira.
⛔ Nenhum número digitado: valores de `apto-mr/precos.py` · sem metragem e sem contagem.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'apto-mr'
sys.path.insert(0, str(R)); sys.path.insert(0, str(P))
with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')
src = (P / 'build-gustavo-caderno.py').read_text(encoding='utf-8')

CLIENTE = 'Mariana Diniz Braz'
ARQ = 'Bruna Teixeira'
OBRA = 'Apartamento MR · Belo Horizonte'
DATA = 'Novembro de 2026'
PRAZO, VALIDADE = '90 dias corridos', '5 dias'
LIN = ('Telescópica', 'Hettich')
GAR = {'Telescópica': '2', 'Hettich': '10'}
CHAMADA = {'Telescópica': 'Corrediça telescópica', 'Hettich': 'Ferragem Hettich'}
PAGTO = [('Entrada, na assinatura do contrato', 0.40), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.20)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
def b64(p): return 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
IMG = {p.stem: b64(p) for p in (P / 'img-apto-mr').glob('*.jpg')}

# ── os valores: por ambiente, em real cheio; o total é a soma do que se lê ──
DESC = {
 'Lavanderia': ('Lavanderia', 'Armário sob o tanque e armário com cesto de roupa e gaveta'),
 'Despensa': ('Despensa', 'Armários de piso a teto, nicho do micro-ondas e prateleira dobrável'),
 'Sala de jantar': ('Sala de jantar', 'Armário sob a bancada e cristaleira com portas de vidro'),
 'Hall de entrada': ('Hall de entrada', 'Banco sapateira com palhinha e almofada, e armário com palhinha e nicho'),
 'Sala de TV': ('Sala de TV', 'Estante de piso a teto com o nicho da TV'),
 'Brinquedoteca': ('Brinquedoteca', 'Bancada solta, caixas com rodízios, prateleiras de livros e suportes de bola'),
 'Quarto Diego': ('Quarto do Diego', 'Guarda-roupa com maleiro, armário raso, mesa de estudo regulável e nichos redondos'),
 'Quarto casal': ('Quarto do casal', 'Guarda-roupas de correr, armário de giro, cabeceira e prateleira'),
 'Escritório': ('Escritório', 'Armário com prateleira da impressora, bancada em L, aéreo e gaveteiro móvel'),
}
assert list(DESC) == PR.L.AMBIENTES
LINHAS_INV = [(DESC[a][0], DESC[a][1], {l: PR.total(l, a) for l in LIN}) for a in PR.L.AMBIENTES]
VAL = {l: [round(v[l]) for *_, v in LINHAS_INV] for l in LIN}
TOT = {l: sum(VAL[l]) for l in LIN}
for l in LIN: assert abs(TOT[l] - PR.total(l)) <= 7, (l, TOT[l], PR.total(l))
assert TOT['Telescópica'] < TOT['Hettich']

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
  <div class="cv-nome">Mariana<br>Diniz Braz</div>
  <div class="cv-s">A marcenaria do apartamento,<br>da lavanderia ao escritório.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">Arq. {E(ARQ)}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Linhas</div><div class="v">Telescópica · Hettich</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['sala']}" alt="" style="object-position:50% 50%"></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''', dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
folha(f'''<div class="ambw">
 <div class="band duo3" style="height:96mm"><img src="{IMG['jantar']}" alt="">
   <img src="{IMG['hall']}" alt=""><img src="{IMG['diego']}" alt="">
   <div class="tag">A casa</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">O que este apartamento pede</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">Um apartamento inteiro. Uma só mão, do corte à montagem.</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">No projeto da arquiteta <b>{E(ARQ)}</b>:
    o Louro Freijó quente na sala, no hall e na cristaleira, o Frapê claro nos armários, a palhinha
    natural nas portas do hall, o Verde Jade nos detalhes das crianças. Da lavanderia ao
    escritório, <b>uma só empresa responde por tudo o que está nestas folhas</b>, da medição à
    instalação. <em>Um contrato, uma data, um nome para chamar.</em></p></div>
 </div></div>''')

# ── 03 · a empresa e a infraestrutura ───────────────────────────────────
PIL = [
 ('01', 'O projeto pede mais que marcenaria.',
  'Vidro das portas, palhinha natural, almofada estofada, rodízios e as peças soltas '
  'das crianças. Tudo isso entra no nosso escopo, no mesmo contrato e na mesma data. '
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
GAVETA = ('Gavetas', 'Sobre a corrediça da linha escolhida: a diferença entre as duas está explicada mais adiante.')
AMB = [
 ('A lavanderia<br>e a despensa.', ['lav', 'desp'], 'Serviço',
  'MDF Branco TX por fora e por dentro · puxador Beetle preto, Zen Design',
  [('Lavanderia', 'Armário sob o tanque e o armário do cesto de roupa, com gaveta.'),
   ('Despensa', 'Armários de piso a teto, com o nicho do micro-ondas, o espaço reforçado para guardar revestimentos e a prateleira dobrável.'),
   GAVETA]),
 ('A sala de jantar.', ['jantar', 'jantar-arm'], 'Sala de jantar',
  'MDF Louro Freijó Poro e Frapê, Arauco · vidro incolor · puxador redondo usinado',
  [('Cristaleira', 'Em Louro Freijó, do piso à viga, com portas de quadro e vidro incolor e o puxador redondo na própria madeira.'),
   ('Armário sob a bancada', 'Em Frapê, com portas de giro e puxador Beetle preto.')]),
 ('O hall de entrada.', ['hall', 'banco'], 'Hall',
  'MDF Frapê e Louro Freijó Poro · palhinha natural · almofada estofada',
  [('Armário', 'Em Frapê, com portas de palhinha natural e o nicho em Louro Freijó.'),
   ('Banco sapateira', 'Solto, em Louro Freijó, com portas de palhinha, puxador cava e a almofada do assento.')]),
 ('A sala de TV<br>e a brinquedoteca.', ['sala', 'brinq'], 'Sala',
  'MDF Louro Freijó Poro e Verde Jade, Arauco · puxador redondo usinado',
  [('Estante', 'De piso a teto, com o nicho da TV, as prateleiras de livros e portas de puxador redondo.'),
   ('Brinquedoteca', 'Bancada solta, caixas de brinquedo em Verde Jade sobre rodízios, prateleiras de livros e os suportes de bola.')]),
 ('O quarto do Diego.', ['diego', 'diego-roupeiro'], 'Quarto Diego',
  'MDF Frapê com interior em Branco TX · Louro Freijó e Verde Jade nos detalhes · puxador cava',
  [('Guarda-roupa', 'Com maleiro até o teto; por dentro, cabideiros, gavetas e sapateiras.'),
   ('Armário raso', 'Ao lado, de portas de giro e prateleiras.'),
   ('Mesa de estudo', 'Com o tampo em Verde Jade que sobe e desce, acompanhando o crescimento.'),
   ('Nichos redondos', 'Em Louro Freijó, sobre a mesa.')]),
 ('O quarto do casal.', ['casal', 'casal-b'], 'Quarto casal',
  'MDF Frapê com interior em Branco TX · Louro Freijó · puxador Bali Granado ponto dourado e perfil metálico',
  [('Guarda-roupas de correr', 'Portas de correr em Frapê com puxador em perfil; por dentro, maleiro, cabideiros, prateleiras e gavetas.'),
   ('Armário de giro', 'Do piso ao teto, com prateleiras.'),
   ('Cabeceira e prateleira', 'Cabeceira em painéis de Louro Freijó e a prateleira de bordas arredondadas.')]),
 ('O escritório.', ['escr'], 'Escritório',
  'MDF Frapê e Louro Freijó Poro · puxador Bali Granado ponto dourado',
  [('Bancada em L', 'Em Frapê, com o armário de portas, nichos e a prateleira deslizante da impressora.'),
   ('Armário aéreo', 'Em Louro Freijó, sobre a bancada.'),
   ('Gaveteiro móvel', 'Sobre rodízios, para acompanhar a cadeira.')]),
]
_a0 = N[0] + 1
# ⭐ [Jonathan, 23/11/2026] "coloque 2 ambientes por página"
def metade(titulo, imgs, tag, acab, itens):
    return f'''<div class="dp">
     <div class="dp-img"><img src="{IMG[imgs[0]]}" alt=""><div class="tag">{E(tag)}</div></div>
     <div class="dp-txt"><div class="eyebrow">Ambiente</div><div class="rule"></div>
      <h2 class="h2">{titulo.replace("<br>", " ")}</h2>{mv(itens)}
      <div class="amb-nota" style="background:none;border-left-color:var(--line)">
        <div class="t">Acabamentos</div><p>{E(acab)}</p></div></div></div>'''
for k in range(0, len(AMB), 2):
    folha(f'<div class="duplo">{"".join(metade(*a) for a in AMB[k:k + 2])}</div>')
N_AMB = (_a0, N[0])

# ── a escolha: duas linhas, a diferença está na ferragem ────────────────
# ⭐ [Jonathan, 23/11/2026] "unifique as páginas 12 e 13": a escolha e as duas opções numa folha só
DIF = [
 ('Corrediça', 'Telescópica, com o trilho aparente na lateral da gaveta.',
  'Oculta Hettich: o trilho some por baixo, a gaveta abre inteira e fecha amortecida.'),
 ('Dobradiça', 'Nacional, de caneco.', 'Hettich Novisys, com amortecedor e regulagem nos três sentidos.'),
 ('O que não muda', 'Desenho, padrões de MDF, vidro, palhinha, almofada e a equipe própria.', 'Os mesmos.'),
]
OPC = {
 'Telescópica': 'Corre sobre esferas e <b>mostra o trilho</b> quando a gaveta abre. É o padrão da maior parte do mercado — <em>o que muda é por quanto tempo</em>.',
 'Hettich': 'Corre <b>por baixo da gaveta</b>: você abre e não vê ferragem. Sai inteira, fecha amortecida, e a dobradiça Novisys fecha a porta sem bater.',
}
ops = ''.join(f'''<div class="c{" hi" if k == "Hettich" else ""}">
     <div class="anos">{GAR[k]}</div><div class="unid">anos de garantia</div>
     <div class="nm">{E(CHAMADA[k])}</div><div class="x">{OPC[k]}</div></div>''' for k in LIN)
linhas = ''.join(f'<tr><td class="l">{E(k)}</td><td style="text-align:left;font-size:8.3pt">{E(a)}</td>'
                 f'<td class="hi" style="text-align:left;font-size:8.3pt">{E(b)}</td></tr>' for k, a, b in DIF)
folha(f'''<div class="pad">
 <div class="eyebrow">Uma escolha · duas linhas</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">A diferença está na ferragem.</h1>
 <p class="lead" style="max-width:225mm">A ferragem é a única peça da marcenaria que <b>se usa todo dia e
  se desgasta</b>. O desenho e os materiais são os mesmos nas duas linhas; a garantia do conjunto
  segue a ferragem escolhida.</p>
 <div class="gar justo duas" style="margin-top:5mm">{ops}</div>
 <table class="cmp" style="margin-top:5mm">
  <tr><th class="l" style="text-align:left"></th>
   {''.join(f'<th{" class=hi" if n == "Hettich" else ""}>{E(n)}</th>' for n in LIN)}</tr>
  {linhas}
 </table>
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
  dois anos na telescópica e dez na Hettich, para o apartamento inteiro. Não é promessa
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

# ⭐ [Jonathan, 23/11/2026] "melhore o layout da pág 15 e mescle com a página 16"
rows = ''.join(
    f'<tr><td class="l">{E(n)}</td>'
    + ''.join(f'<td{" class=hi" if l == "Hettich" else ""}>{brs(VAL[l][i])}</td>' for l in LIN)
    + '</tr>' for i, (n, d, _v) in enumerate(LINHAS_INV))
def cartao(k):
    hi = k == 'Hettich'
    return f'''<div class="tc{" hi" if hi else ""}">
   <div class="hd"><b>{GAR[k]}</b><span>anos de garantia<br>{E(CHAMADA[k])}</span></div>
   <div class="k">O projeto completo</div><div class="v">{br(TOT[k])}</div>
   <div class="k" style="margin-top:2.6mm">Entrada · {PAGTO[0][1]*100:.0f}%</div><div class="e">{br(TOT[k] * PAGTO[0][1])}</div>
   <div class="k" style="margin-top:2mm">{len(PAGTO) - 1} parcelas de {PAGTO[1][1]*100:.0f}%</div><div class="e">{br(TOT[k] * PAGTO[1][1])}</div></div>'''
folha(f'''<div class="pad" style="padding-top:11mm">
 <div class="eyebrow">Investimento</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">O apartamento, nas duas linhas.</h1>
 <p class="lead" style="max-width:235mm;font-size:9pt">Cada móvel foi levantado <b>peça por peça do
  caderno de marcenaria</b>. A mesma casa, o mesmo desenho e os mesmos padrões: a diferença é a
  ferragem — e o tempo pelo qual respondemos por ela.</p>
 <div class="invx">
  <table class="inv inv13">
   <tr><th class="l">Ambiente</th>
    {''.join(f'<th{" class=hi" if l == "Hettich" else ""}>{E(l)}</th>' for l in LIN)}</tr>
   {rows}
   <tr class="tot"><td class="l">O projeto completo</td>
    {''.join(f'<td{" class=hi" if l == "Hettich" else ""}>{brs(TOT[l])}</td>' for l in LIN)}</tr>
  </table>
  <div class="tcs">{cartao('Telescópica')}{cartao('Hettich')}</div>
 </div>
 <div class="incl"><b>Incluso nas duas linhas:</b> projeto executivo de marcenaria, material, usinagem,
  ferragem da linha escolhida, o vidro da cristaleira, a palhinha natural, a almofada do banco, os
  rodízios, transporte, montagem e instalação — num só contrato, com uma só data.</div>
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
     <div class="s">Dez anos na Hettich e dois na telescópica. Instalação e regulagem, dois anos.
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
  </div>
  <div class="fora">
   <div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>
    <li><div class="k">Pedra e serralheria</div><div class="v">As bancadas em granito, o tanque e a
      porta camarão da lavanderia.</div></li>
    <li><div class="k">Móveis existentes e decoração</div><div class="v">Mesa, cadeiras, sofá, cama,
      estante existente, tapetes, luminárias e peças de decoração.</div></li>
    <li><div class="k">Espelho de parede</div><div class="v">O espelho colado na parede do quarto
      do casal.</div></li>
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
  <div class="cv-s">Obrigado pela confiança. O projeto da arquiteta {E(ARQ)} sai da nossa
   fábrica e chega instalado.</div>
  <div class="cv-meta">
   <div><div class="k">Proposta</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['casal']}" alt="" style="object-position:50% 50%"></div>
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
.duplo{display:grid;grid-template-columns:1fr 1fr;gap:9mm;height:100%;padding:10mm 14mm 16mm}
.dp{display:flex;flex-direction:column;min-height:0}
.dp-img{position:relative;height:84mm;flex:none;overflow:hidden;background:var(--sand)}
.dp-img img{width:100%;height:100%;object-fit:cover;display:block}
.dp-img .tag{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);
  font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;padding:3mm 6mm;font-weight:600}
.dp-txt{padding-top:5mm;min-height:0}
.dp-txt .h2{font-size:19pt;margin:1mm 0 2.5mm}
.dp-txt .mv .t{font-size:8.8pt}
.dp-txt .mv .d{font-size:8.1pt}
.dp-txt .amb-nota{margin-top:3mm}
.invx{display:grid;grid-template-columns:1.35fr 1fr;gap:8mm;margin-top:4mm;align-items:start}
.invx .inv13 td,.invx .inv13 th{padding-top:1.7mm !important;padding-bottom:1.7mm !important;font-size:9.2pt}
.tcs{display:flex;flex-direction:column;gap:4mm}
.tc{border:1.2px solid var(--line);border-radius:4px;padding:4.4mm 5mm;background:#fff}
.tc.hi{background:var(--deep);color:#F6F1E7;border-color:var(--deep)}
.tc .hd{display:flex;align-items:center;gap:3mm;margin-bottom:3mm}
.tc .hd b{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;line-height:.9;color:var(--gold);font-weight:600}
.tc.hi .hd b{color:var(--gold-lt)}
.tc .hd span{font-size:6.6pt;letter-spacing:.14em;text-transform:uppercase;line-height:1.4}
.tc .k{font-size:6.4pt;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:700}
.tc.hi .k{color:var(--gold-lt)}
.tc .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;line-height:1.05;margin-top:.6mm}
.tc .e{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;margin-top:.3mm}
.incl{margin-top:auto;padding-left:4mm;border-left:2.5px solid var(--gold-lt);font-size:8pt;color:var(--soft);line-height:1.5}
.incl b{color:var(--ink)}

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
for _p in ('cartão', 'cartao', 'desconto', 'margem', 'blum', 'sensys', 'nada corta', 'gran royalle', 'corsino', 'sollero', 'escarlate'):
    assert _p not in _t.lower(), f'⛔ a peça fala em "{_p}"'
_amb = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(S[N_AMB[0] - 1:N_AMB[1]])))
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco|seis|sete|oito|dez)\s+(portas?|folhas?|gavet\w+|básculas?|nichos?|prateleiras?)', _amb, re.I), '⛔ contagem'

OUT = R / 'proposta-apto-mr.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-apto-mr.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {NF} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
for l in LIN:
    print(f'  {l:8s} {br(TOT[l])} · entrada {br(TOT[l] * PAGTO[0][1])}')
