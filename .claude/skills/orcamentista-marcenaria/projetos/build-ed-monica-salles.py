# -*- coding: utf-8 -*-
"""ED. MÔNICA SALLES — caderno de proposta, academia e espaço gourmet  [12/11/2026]

⭐ [Jonathan, 12/11/2026] "pode fechar a proposta", depois de: só a linha HETTICH, RT 10%
  + comissão 4%, e todos os espelhos num item próprio (o do painel do banco e os três de
  parede). Números de `ed-monica-salles/precos.py`.
⭐ Mesmo caderno do Gran Royalle (A4 paisagem), com UMA linha: saem as folhas de escolha
  entre linhas. Fotos: renders da Apresentação R02 da OCAPI.
⚠ Prazo, pagamento e validade: padrão da casa, oferecido e não contestado — confirmar.
⛔ Nenhum número digitado · sem metragem e sem contagem nas descrições dos ambientes.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'ed-monica-salles'
sys.path.insert(0, str(R)); sys.path.insert(0, str(P))
with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')
src = (P / 'build-gustavo-caderno.py').read_text(encoding='utf-8')

CLIENTE = 'Ed. Mônica Salles'
ARQ = 'Dalila Souza'
OBRA = 'Academia e espaço gourmet'
DATA = 'Novembro de 2026'
PRAZO, VALIDADE = '90 dias corridos', '7 dias úteis'
LIN = ('Hettich',)
GAR = {'Hettich': '10'}
CHAMADA = {'Hettich': 'Ferragem Hettich'}
PAGTO = [('Entrada, na assinatura do contrato', 0.30), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.30)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
def b64(p): return 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
IMG = {p.stem: b64(p) for p in (P / 'img-ed-monica-salles').glob('*.jpg')}

# ── os valores: por ambiente, em real cheio; o total é a soma do que se lê ──
import levantamento as LV
DESC = {it['movel']: d for it, d in zip(LV.ITENS, [
 'Inferiores sob a pedra, com o nicho do forno',
 'A parede do bar revestida dos dois lados, com o portal sob o forro',
 'O painel da TV emoldurado pelo portal',
 'O abrigo ripado da máquina da sauna, com portas de abrir',
 'O painel da TV com perfil metálico de proteção',
 'O painel sobre o banco e o banco de lateral abaulada, com nicho para colchonetes',
 'Do piso ao teto, com prateleiras abertas',
 'A porta de correr com perfil metálico de proteção',
 'O espelho do painel do banco e os espelhos das paredes',
])}
assert len(DESC) == len(LV.ITENS)
LINHAS_INV = [(f"{a} · {m}", DESC[m], {l: v['pv'] for l in LIN}) for (a, m), v in PR.TAB['Hettich'].items()]
VAL = {l: [round(v[l]) for *_, v in LINHAS_INV] for l in LIN}
TOT = {l: sum(VAL[l]) for l in LIN}
for l in LIN: assert abs(TOT[l] - PR.total(l)) <= 7, (l, TOT[l], PR.total(l))

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
  <div class="cv-nome">Ed. Mônica<br>Salles</div>
  <div class="cv-s">A marcenaria da academia<br>e do espaço gourmet.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">OCAPI · arq. {E(ARQ)}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Ferragem</div><div class="v">Hettich</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['gour-2']}" alt="" style="object-position:55% 50%"></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''', dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
folha(f'''<div class="ambw">
 <div class="band duo3" style="height:96mm"><img src="{IMG['gour-3']}" alt="">
   <img src="{IMG['acad-3']}" alt=""><img src="{IMG['acad-1']}" alt="">
   <div class="tag">O projeto</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">O que este projeto pede</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">Duas áreas comuns. Uma só mão, do corte à montagem.</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">No projeto da arquiteta <b>{E(ARQ)}</b>,
    da OCAPI: a academia com painéis em madeira escura, espelhos e o banco com nicho para os
    colchonetes; o espaço gourmet com o bar revestido, o portal sob o forro e o abrigo ripado
    da sauna. <b>Uma só empresa responde por tudo o que está nestas folhas</b>, da medição à
    instalação. <em>Um contrato, uma data, um nome para chamar.</em></p></div>
 </div></div>''')

# ── 03 · a empresa e a infraestrutura ───────────────────────────────────
PIL = [
 ('01', 'O projeto pede mais que marcenaria.',
  'Espelhos, ripado, perfis metálicos de proteção, porta de correr e os painéis que '
  'revestem as paredes. Tudo isso entra no nosso escopo, no mesmo contrato e na mesma data. '
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
AMB = [
 ('O espaço gourmet.', ['gour-3', 'gour-2'], 'Gourmet',
  'MDF no acabamento definido pela arquiteta · interior em Branco TX · ferragem Hettich',
  [('A cozinha', 'Armários inferiores sob a bancada de pedra, com portas de puxador usinado e o nicho do forno embutido.'),
   ('O bar e o portal', 'A parede do bar revestida dos dois lados, do piso ao forro, com o portal que desenha o teto.'),
   ('O painel da TV', 'Emoldurado pelo mesmo portal, no acabamento do bar.')]),
 ('O gourmet,<br>a TV e a sauna.', ['gour-4', 'gour-6'], 'Gourmet',
  'MDF no acabamento definido pela arquiteta · ripado de desenho fino · perfil metálico de proteção',
  [('Abrigo da sauna', 'Ripado, com portas de abrir que escondem a máquina e garantem o acesso para manutenção.'),
   ('Proteção', 'Perfil metálico na base dos painéis, onde o uso de área comum mais pede.')]),
 ('A academia.', ['acad-3', 'acad-4'], 'Academia',
  'MDF no acabamento definido pela arquiteta · espelho prata · perfil metálico de proteção',
  [('O painel da TV', 'A parede inteira revestida, com perfil metálico na base.'),
   ('Os espelhos', 'Espelho prata nas paredes de treino e sobre o banco, instalados por nós.'),
   ('A porta de correr', 'No mesmo acabamento, com perfil metálico de proteção.')]),
 ('A academia,<br>o banco e a estante.', ['acad-6', 'acad-2'], 'Academia',
  'MDF no acabamento definido pela arquiteta · interior em Branco TX',
  [('O banco', 'De lateral abaulada, com o nicho para os colchonetes embaixo e o painel com espelho atrás.'),
   ('A estante', 'Do piso ao teto, com prateleiras abertas para toalhas, halteres e acessórios.')]),
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

# ── a garantia ──────────────────────────────────────────────────────────
PASSOS = [('Vocês nos chamam', 'Por telefone, WhatsApp ou e-mail, direto com a fábrica. Sem central e sem intermediário.'),
          ('Respondemos em 24 horas', 'Esse é o nosso compromisso de retorno, contado a partir do chamado.'),
          ('Visita em até três dias úteis', 'Se não resolvermos pelo telefone, a equipe vai ao local. Dentro do prazo de garantia, visita e reparo não têm custo.')]
passos = ''.join(f'''<div class="pe"><div class="pe-n">{i:02d}</div><div class="pe-t">{E(t)}</div>
  <div class="pe-l">{E(d)}</div></div>''' for i, (t, d) in enumerate(PASSOS, 1))
folha(f'''<div class="pad">
 <div class="eyebrow">Garantia</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O termo é assinado na entrega.</h1>
 <p class="lead" style="max-width:215mm">A garantia da Valvic <b>segue a ferragem</b>:
  dez anos na Hettich, para todo o projeto. Não é promessa
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
 <div class="eyebrow">Investimento · item a item</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">O projeto, item a item.</h1>
 <p class="lead" style="max-width:235mm;font-size:9pt">Cada móvel foi levantado <b>peça por peça
  do caderno de marcenaria</b> — nada é rateio nem estimativa por metro quadrado. Valores em reais.</p>
 <table class="inv inv13" style="margin-top:3mm">
  <tr><th class="l">Item</th>
   {''.join(f'<th{" class=hi" if l == "Hettich" else ""}>{E(l)}</th>' for l in LIN)}</tr>
  {rows}
  <tr class="tot"><td class="l">O projeto completo</td>
   {''.join(f'<td{" class=hi" if l == "Hettich" else ""}>{brs(TOT[l])}</td>' for l in LIN)}</tr>
 </table>
</div>''')

folha(f'''<div class="pad">
 <div class="eyebrow">Investimento</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O projeto completo.</h1>
 <p class="lead" style="max-width:215mm">A academia e o espaço gourmet, com ferragem
  <b>Hettich</b> e dez anos de garantia sobre a marcenaria e a ferragem.</p>
 <div class="gar justo duas"><div class="c hi">
     <div class="anos">{GAR['Hettich']}</div><div class="unid">anos de garantia</div>
     <div class="nm">Ferragem Hettich</div>
     <div class="x">Dobradiça com amortecedor e regulagem nos três sentidos.</div>
     <div class="l"><div class="k">O projeto completo</div>
      <div class="v" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt">{br(TOT['Hettich'])}</div></div>
     <div class="l" style="margin-top:2mm"><div class="k">Entrada, na assinatura</div>
      <div class="v">{br(TOT['Hettich'] * PAGTO[0][1])}</div></div></div>
  <div class="c"><div class="nm" style="margin-top:0">O que está incluso</div>
   <div class="x">Projeto executivo de marcenaria, material, usinagem, ferragem Hettich, os
    espelhos, o ripado, os perfis metálicos de proteção, a porta de correr, transporte,
    montagem e instalação — num só contrato, com uma só data e uma só arquiteta
    responsável.</div></div></div>
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
   <div class="term"><div class="k">Garantia</div><div class="v">Dez anos</div>
     <div class="s">Dez anos na marcenaria e na ferragem Hettich. Instalação e regulagem, dois anos.
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
    <li><div class="k">Pedra</div><div class="v">As bancadas, a rodabanca até o teto, a
      bancada com pés laterais e a mesa de jantar são marmoraria.</div></li>
    <li><div class="k">Equipamentos e eletros</div><div class="v">Aparelhos de academia,
      televisões, cooktop, coifa, forno, geladeira, cubas e torneiras.</div></li>
    <li><div class="k">Mobiliário solto</div><div class="v">Cadeiras, banquetas e
      luminárias.</div></li>
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
 <div class="cv-r"><img src="{IMG['acad-4']}" alt="" style="object-position:50% 50%"></div>
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
           'Orlando', 'Ivone', 'Corsino', 'Sollero', 'Tereza', 'Júnia', 'Rafael', 'Lagoa Santa', 'Costa Laguna', 'Residencial Árvores'):
    assert _c not in _t, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE: {_c}'
assert not [c for c in '⭐⛔⚠' if c in ''.join(S)], '⛔ marcação interna'
for _p in ('cartão', 'cartao', 'desconto', 'margem', 'comissão', 'telescópica', 'sensys', 'blum', 'nada corta', 'corsino', 'gran royalle', 'jéssica'):
    assert _p not in _t.lower(), f'⛔ a peça fala em "{_p}"'
_amb = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(S[N_AMB[0] - 1:N_AMB[1]])))
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco|seis|sete|oito|dez)\s+(portas?|folhas?|gavet\w+|básculas?|nichos?|prateleiras?)', _amb, re.I), '⛔ contagem'

OUT = R / 'proposta-ed-monica-salles.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-ed-monica-salles.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {NF} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
for l in LIN:
    print(f'  {l:8s} {br(TOT[l])} · entrada {br(TOT[l] * PAGTO[0][1])}'); [print(f'    {n[:60]:60s} {brs(v)}') for (n, _d, _v), v in zip(LINHAS_INV, VAL[l])]
