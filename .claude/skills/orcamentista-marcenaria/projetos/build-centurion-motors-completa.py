# -*- coding: utf-8 -*-
"""CENTURION MOTORS — Showroom Vila da Serra · proposta COMPLETA em NOVE páginas  [26/11/2026]

⭐ [Jonathan, 26/11/2026] "vamos montar a versão mais completa, apresentando os processos da empresa,
  falando mais sobre o processo da laca, incluindo os materiais da curva: esqueleto, compensado flexível,
  fórmica e laca" — pesquisa apresentada e aprovada ("pode seguir") · ⛔ "não coloque nada em inglês".
⚠ A laca está no levantamento como serviço de terceiro: o texto diz "em cabine, com o nosso controle",
  sem afirmar cabine própria.

⭐ [Jonathan, 26/11/2026] "vamos montar com esse cenario": cinco itens com preço fechado, R$ 295.500
  (valores em `centurion-motors/valores.py`, onde também ficam custo e MC — nunca na proposta).
⚠ Condições NÃO informadas para este projeto: repetidas as últimas (40% + 20% a 30/60/90, 90 dias,
  validade 5 dias) e garantia de 5 anos (padrão comercial, Honda Minas Motos) — confirmar com o Jonathan.
⛔ Sem medida e sem contagem nas descrições · sem preço antes da folha 3 · espelho É nosso (23/11/2026),
  tinta e pedra não.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'centurion-motors'
sys.path.insert(0, str(R))
with contextlib.redirect_stdout(io.StringIO()):
    import valores as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')

CLIENTE, DESIGNER, OBRA, DATA = 'Centurion Motors', 'CLS Arquitetas Associadas', 'Showroom · Vila da Serra, Nova Lima', 'Novembro de 2026'
PRAZO, VALIDADE = '90 dias corridos', '5 dias'
PAGTO = [('Entrada, na assinatura do contrato', 0.40), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.20)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
IMG = {p.stem: 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
       for p in (P / 'img-centurion-motors').glob('*.jpg')}
TOTAL = PR.TOTAL
assert TOTAL == sum(v for _, _, v, _ in PR.VALORES) == 295500

S, N = [], [0]
def folha(corpo, dark=False, rodape=True):
    N[0] += 1
    f = (f'<div class="foot"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span><span>{N[0]:02d} / 09</span></div>'
         if rodape else '')
    S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')

# ── 01 · capa ─────────────────────────────────────────────────────────
PIL = [('Do corte à instalação', 'Fábrica e equipe próprias: uma só empresa responde pela madeira, pela curva, pela luz e pelo espelho.'),
       ('Executivo nosso', 'Cada pórtico, painel e módulo de forro é detalhado por nós e aprovado pelas arquitetas antes do corte.'),
       ('Obra comercial, prazo de loja', 'Montagem planejada para que o showroom volte a receber clientes o quanto antes.')]
folha(f"""<div class="p1">
 <div class="p1-l">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="p1-nome">Centurion<br>Motors</div>
  <div class="p1-s">A marcenaria do showroom.</div>
  <p class="p1-t">No projeto da <b>{E(DESIGNER)}</b>, a madeira envolve o salão do forro às paredes e
   emoldura os carros; na área de convivência, os pórticos em arco laqueados café abrigam nichos
   iluminados, e os espelhos ampliam o espaço e multiplicam a vitrine.</p>
  <div class="p1-pil">{''.join(f'<div><b>{E(t)}</b><span>{E(d)}</span></div>' for t, d in PIL)}</div>
  <div class="p1-meta">
   <div><div class="k">Projeto</div><div class="v">{E(DESIGNER)}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Escopo</div><div class="v">Forro, pórticos, painéis e espelhos</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="p1-r"><img class="g1" src="{IMG['nichos']}" alt=""><img class="g2" src="{IMG['frontal']}" alt="">
  <img class="g3" src="{IMG['corredor']}" alt=""></div>
</div>""", dark=True, rodape=False)

# ── 02 · a leitura do projeto ──────────────────────────────────────────
LEI = [('A madeira como moldura', 'Forro e paredes no mesmo amadeirado fecham o salão num tom quente e contínuo — os carros ficam em primeiro plano, emoldurados.'),
       ('O arco como assinatura', 'Os pórticos curvos laqueados café repetem-se ao longo da convivência e marcam as passagens: é o desenho que dá identidade à loja.'),
       ('A luz que expõe', 'Os nichos acendem as peças expostas por dentro, com a luz embutida nas prateleiras.'),
       ('O espelho que multiplica', 'Os grandes panos de espelho ampliam o salão e repetem a vitrine, sem uma emenda de suporte aparente.')]
folha(f"""<div class="pad p2">
 <div class="eyebrow">A leitura do projeto</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 5mm">O que a marcenaria faz por este showroom.</h1>
 <div class="lg">
  <div class="lg-i"><img src="{IMG['moodboard']}" alt=""><div class="cap">Painel de referências · {E(DESIGNER)}</div></div>
  <div class="lg-t">
   {''.join(f'<div class="lg-p"><b>{E(t)}</b><p>{E(d)}</p></div>' for t, d in LEI)}
   <div class="lg-m"><img src="{IMG['convivencia']}" alt=""><img src="{IMG['lateral']}" alt=""></div>
  </div>
 </div>
</div>""")

# ── 03 · a empresa e a infraestrutura (o padrão das outras propostas) ───
PILX = [
 ('01', 'O projeto pede mais que marcenaria.',
  'Forro, painéis, pórticos curvos laqueados, luz embutida nos nichos e espelhos. Tudo isso entra no nosso '
  'escopo, no mesmo contrato e na mesma data. <b>A loja não contrata mais ninguém</b> para a marcenaria e '
  'para o que faz parte dela. O que fica fora vem nomeado.'),
 ('02', 'A peça sai daqui conferida.',
  'Detalhamento, programação, usinagem, montagem e conferência acontecem dentro da nossa fábrica. Cada '
  'pórtico é montado e conferido no gabarito antes de seguir para o acabamento. A conferência é '
  '<b>etapa do processo</b>, não boa vontade no fim.'),
 ('03', 'Uma arquiteta responsável pelo projeto.',
  'Do orçamento aprovado à entrega, o projeto tem uma arquiteta nossa como responsável. É ela quem lê o '
  'executivo prancha por prancha, está na medição e segue as peças pela fábrica, conversando com a '
  f'{E(DESIGNER)} na mesma linguagem técnica. <b>Vocês explicam o projeto uma vez, a uma pessoa.</b>'),
 ('04', 'O executivo de marcenaria é nosso.',
  'Antes de cortar, a Valvic desenha. O projeto de interiores diz o que o ambiente precisa ser; o nosso '
  'executivo diz como cada peça se constrói — a costela de cada arco, a fixação do forro, o prumo da base '
  'do espelho. É nele que a divergência aparece <em>no papel, antes de virar retrabalho</em>.'),
]
pilx = '\n'.join(f'''<div class="c"><div class="n">{n}</div><div class="t">{E(t)}</div>
  <div class="d">{d}</div></div>''' for n, t, d in PILX)
folha(f"""<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">A empresa e a infraestrutura</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">A Valvic articula todas as soluções do projeto.</h1>
 <p class="lead" style="max-width:215mm">Um projeto raramente se perde na marcenaria. Ele se perde na costura
  entre os ofícios, quando cada um chega com contrato, prazo e medida próprios. Aqui não há essa costura para
  fazer: tudo o que esta proposta reúne entra no mesmo escopo, no mesmo contrato e na mesma data.</p>
 <div class="fr" style="margin-top:6mm;flex:1;min-height:0">{pilx}</div>
 <div class="box" style="margin-top:5mm"><p style="font-size:9.4pt;color:var(--ink)">
   Na próxima folha, o caminho que o projeto percorre — etapa por etapa, até o dia em que a loja abre as
   portas com a marcenaria pronta.</p></div>
</div>""")

# ── 04 · as doze etapas (as mesmas do caderno de referência) ────────────
_src = (P / 'build-gustavo-caderno.py').read_text(encoding='utf-8')
BLOCOS = eval(re.search(r'^BLOCOS = (\[.*?\n\])', _src, re.S | re.M).group(1))
assert sum(len(b[2]) for b in BLOCOS) == 12
_LOJA = [('da nossa fábrica à sua casa', 'da nossa fábrica à sua loja'), ('até a porta da sua casa', 'até a porta da loja'),
         ('O projeto virou casa.', 'O projeto virou loja.'), ('Casa', 'Loja')]
def _loja(t):
    for a, b in _LOJA:
        t = t.replace(a, b)
    return t
BLOCOS = [(_loja(nm), _loja(sub), [tuple(_loja(x) for x in e) for e in ets]) for nm, sub, ets in BLOCOS]
_n = [0]
def etapa(k, t, l, e):
    _n[0] += 1
    return f'''<div class="pe"><div class="pe-n">{_n[0]:02d}</div><div class="pe-k">{E(k)}</div>
      <div class="pe-t">{E(t)}</div><div class="pe-l">{E(l)}</div><div class="pe-e">{E(e)}</div></div>'''
cols = '\n'.join(f'''<div class="pb"><div class="pb-h">{E(nm)}</div><div class="pb-s">{E(sub)}</div>
  {''.join(etapa(*e) for e in ets)}</div>''' for nm, sub, ets in BLOCOS)
folha(f"""<div class="pad" style="padding:13mm 15mm 20mm">
 <div class="eyebrow">O caminho do seu projeto</div><div class="rule"></div>
 <div style="display:flex;align-items:baseline;gap:9mm;margin-bottom:5mm">
  <h1 class="h1" style="margin:0">Doze etapas,<br>um só responsável</h1>
  <p class="lead" style="margin:0;max-width:112mm">Da sua decisão até a loja pronta são doze
    etapas — e nenhuma delas muda de dono.</p></div>
 <div class="rail"></div><div class="proc">{cols}</div>
</div>""")

# ── 05 · o pórtico curvo: vista frontal e as camadas ────────────────────
import math
CX, CY, BASE = 190, 168, 318
def _banda(r1, r2, lado):
    s = 1 if lado == 'd' else -1
    sw_o, sw_i = (1, 0) if lado == 'd' else (0, 1)
    return (f'M {CX},{CY - r2} A {r2} {r2} 0 0 {sw_o} {CX + s * r2},{CY} L {CX + s * r2},{BASE} '
            f'L {CX + s * r1},{BASE} L {CX + s * r1},{CY} A {r1} {r1} 0 0 {sw_i} {CX},{CY - r1} Z')
CAMADAS = [  # (r1, r2, preenchimento, rótulo, explicação)
    (96, 116, 'url(#mdf)', 'Esqueleto', 'costelas recortadas no desenho exato do arco'),
    (88, 96, 'url(#comp)', 'Compensado flexível', 'a pele que acompanha a curva'),
    (83, 88, '#C3C7CA', 'Fórmica', 'a base lisa e estável da laca'),
    (78, 83, '#4B2F22', 'Laca PU fosca café', 'aderência, fundo e acabamento'),
]
_rot, _ld = [], ''
for i, (r1, r2, cor, t, d) in enumerate(CAMADAS):
    a = math.radians(62 - i * 15)
    rm = (r1 + r2) / 2
    px, py = CX + rm * math.cos(a), CY - rm * math.sin(a)
    ly = 60 + i * 52
    _ld += (f'<line x1="{px:.1f}" y1="{py:.1f}" x2="352" y2="{ly - 4}" stroke="#9C7A3C" stroke-width=".8"/>'
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2.2" fill="#9C7A3C"/>')
    _rot.append(f'<text x="358" y="{ly}" font-size="12" font-weight="700" fill="#1A1714">{i + 1} · {E(t)}</text>'
                f'<text x="358" y="{ly + 14}" font-size="9.6" fill="#5C564C">{E(d)}</text>')
ABERTO = ''.join(f'<path d="{_banda(r1, r2, "d")}" fill="{cor}" stroke="#7d746a" stroke-width=".5"/>'
                 for r1, r2, cor, *_ in CAMADAS)
VAO = f'M {CX - 78},{BASE} L {CX - 78},{CY} A 78 78 0 0 1 {CX + 78},{CY} L {CX + 78},{BASE} Z'
PRAT = ''.join(f'<rect x="{CX - 78}" y="{y}" width="156" height="5" fill="#B88A5A"/>'
               f'<rect x="{CX - 74}" y="{y + 5}" width="148" height="2" fill="#F6D9A0" opacity=".9"/>'
               for y in (190, 232, 274))
SVG = f'''<svg viewBox="66 40 500 300" xmlns="http://www.w3.org/2000/svg" font-family="DM Sans,Arial,sans-serif">
 <defs><pattern id="mdf" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="#F2EFE8"/>
  <circle cx="2" cy="2" r=".7" fill="#C9C1B2"/><circle cx="5.2" cy="5" r=".55" fill="#C9C1B2"/></pattern>
  <pattern id="comp" width="9" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><rect width="9" height="4" fill="#DDBD8C"/>
  <line x1="0" y1="2" x2="9" y2="2" stroke="#B8915C" stroke-width=".6"/></pattern>
  <linearGradient id="fundo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8A5E38"/><stop offset="1" stop-color="#A97A4E"/></linearGradient></defs>
 <path d="{VAO}" fill="url(#fundo)"/>{PRAT}
 <path d="{_banda(78, 116, 'e')}" fill="#4B2F22"/>
 {ABERTO}
 <line x1="{CX}" y1="{CY - 122}" x2="{CX}" y2="{BASE + 4}" stroke="#1A1714" stroke-width=".7" stroke-dasharray="4 3"/>
 <text x="{CX - 58}" y="{BASE + 22}" font-size="9.6" text-anchor="middle" fill="#4B2F22" letter-spacing="1.6" font-weight="700">ACABADO</text>
 <text x="{CX + 58}" y="{BASE + 22}" font-size="9.6" text-anchor="middle" fill="#9C7A3C" letter-spacing="1.6" font-weight="700">ABERTO · AS CAMADAS</text>
 {_ld}{''.join(_rot)}
</svg>'''
FOTOS = [('pt-esqueleto', 'Esqueleto', 'Costelas e travessas dão a forma: é a estrutura, conferida em nível e prumo, que mantém a curva.'),
         ('pt-desenho', 'O desenho da curva', 'Raio, espessura e encaixe definidos no executivo, antes de qualquer corte.'),
         ('pt-flexivel', 'Compensado flexível', 'Lâminas que curvam num só sentido. Não se sustenta sozinho: veste o esqueleto.'),
         ('pt-colagem', 'Colagem', 'A pele é colada às costelas, por dentro e por fora, até a curva correr contínua.')]
fotos = ''.join(f'''<div class="pf"><div class="pf-i"><img src="{IMG[k]}" alt=""><span>{i}</span></div>
  <b>{E(t)}</b><p>{E(d)}</p></div>''' for i, (k, t, d) in enumerate(FOTOS, 1))
folha(f"""<div class="pad p4">
 <div class="eyebrow">O pórtico curvo · do esqueleto à laca</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">Uma curva perfeita é feita de quatro camadas.</h1>
 <div class="pv">
  <div class="pv-d"><div class="pv-s">{SVG}</div>
   <p class="pv-x">Vista frontal de um pórtico · ilustrativa, fora de escala. À esquerda, como ele fica; à direita, as
    camadas que estão por baixo da laca. A <b>fórmica</b> fecha o veio do compensado com uma superfície lisa e estável — é por
    isso que a laca corre limpa na curva, sem onda e sem marca de emenda.</p></div>
  <div class="pfs">{fotos}</div>
 </div>
</div>""")

# ── 06 · a laca, demão por demão (com as fotos) ─────────────────────────
LACA = [('lc-lixa', 'Preparo', 'A superfície é desengordurada e recebe uma lixa leve: só a ancoragem, sem atravessar o laminado.'),
        ('lc-tinta', 'Primer e laca preparados', 'Primer de aderência próprio para superfície lisa e laca catalisada na proporção certa, demão por demão.'),
        ('lc-lixadeira', 'Fundo PU e lixamento', 'O fundo é lixado com lixa fina. É depois dele que aparecem imperfeições antes invisíveis — e é aqui que se corrigem.'),
        ('lc-pistola', 'Laca em cabine', 'Laca PU fosca café aplicada com pistola, em camadas finas e contínuas, longe do pó da lixa.'),
        ('lc-pistola-branca', 'Cura e inspeção', 'A laca endurece por reação química. A peça só é embalada depois da cura completa e conferida sob luz rasante.')]
lac = ''.join(f'''<div class="lf"><div class="lf-i"><img src="{IMG[k]}" alt=""><span>{i:02d}</span></div>
  <b>{E(t)}</b><p>{E(d)}</p></div>''' for i, (k, t, d) in enumerate(LACA, 1))
folha(f"""<div class="pad p5">
 <div class="eyebrow">A laca · demão por demão</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">A qualidade da laca se decide antes da primeira demão.</h1>
 <p class="lead" style="max-width:220mm;margin:0 0 4mm">O café do projeto pede acabamento de peça única: a laca é a última
  camada, nunca a que corrige. Tudo o que vem antes dela — esqueleto, pele, fórmica e preparo — é o que garante a curva lisa por anos.</p>
 <div class="lfs">{lac}</div>
 <div class="lc-b">
  <div class="lc-k"><div class="big">5 a 7</div><div class="u">dias de cura</div><p>antes de embalar a peça. Pressa aqui é laca marcada na obra.</p></div>
  <div class="lc-x"><b>Por que fórmica por baixo da laca?</b><p>Laca é rígida: se o que está por baixo trabalha, ela trinca na emenda ou no
   encontro do arco com o pilar. Esqueleto firme, compensado bem colado e fórmica estável mantêm a curva lisa por anos.</p></div>
  <div class="lc-x"><b>Clima de pintura</b><p>Frio intenso ou umidade alta pedem adiar a demão: a laca não cura direito. A cabine controla
   isso — a obra, não. Por isso nenhum pórtico é laqueado no local.</p></div>
 </div>
</div>""")

# ── 07 · os itens ──────────────────────────────────────────────────────
MOV = [('01', 'Forro amadeirado', 'convivencia',
        'Em MDF amadeirado, sobre o salão e a convivência, contínuo de ponta a ponta, fixado em estrutura própria contra a laje.'),
       ('02', 'Nichos e pórticos', 'nichos',
        'Pórticos curvos laqueados café, nichos com fundo amadeirado, prateleiras com alma de aço e luz embutida, e os arcos de acesso aos ambientes.'),
       ('03', 'Painéis de parede', 'corredor',
        'As paredes revestidas em MDF amadeirado, no mesmo padrão do forro, no lugar do adesivo indicado no projeto.'),
       ('04', 'Painéis para o espelho', 'frontal2',
        'A base em MDF que recebe os espelhos, aprumada e plana sobre estrutura — espelho colado não perdoa parede torta.'),
       ('05', 'Espelhos', 'destaque',
        'Espelho prata colado sobre os painéis, que amplia o salão e multiplica a vitrine, com transporte e instalação.')]
mov = ''.join(f"""<div class="it"><div class="mi"><img src="{IMG[img]}" alt=""><span>{n}</span></div>
  <b>{E(t)}</b><p>{E(d)}</p></div>""" for n, t, img, d in MOV)
folha(f"""<div class="pad p6">
 <div class="eyebrow">Os itens</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">Cinco itens, uma só linguagem.</h1>
 <div class="its">{mov}
  <div class="it-a"><div class="hk">Acabamentos</div>
   <p>MDF amadeirado no forro, nos painéis e no fundo dos nichos · MDF branco na estrutura e na base do espelho ·
    compensado flexível e fórmica nas curvas · laca PU fosca café nos pórticos · alma de aço nas prateleiras ·
    luz embutida nos nichos · espelho prata.</p></div>
 </div>
</div>""")

# ── 08 · o que está e o que não está ───────────────────────────────────
INC = ['Medição técnica no local', 'Projeto executivo e engenharia de produto', 'Todo o material de marcenaria, a fórmica e o compensado flexível',
       'Laca PU fosca café nos pórticos', 'Prateleiras com alma de aço e luz embutida nos nichos', 'Espelho prata, com transporte próprio',
       'Transporte, montagem, fixação e arremates', 'Limpeza fina da marcenaria e vistoria de entrega']
FORA = ['Pintura e tinta indicadas no projeto, e o preparo das paredes', 'Pedras e bancadas, como a do bar',
        'Forro de gesso, iluminação geral do salão e do forro, e pontos elétricos', 'Obra civil, piso e escada',
        'Mobiliário solto, quadros, arandelas, tapetes e objetos de decoração']
CUI = [('Limpeza', 'Pano macio levemente úmido e sabão neutro. Nada de álcool, solvente, esponja abrasiva ou produto com cera.'),
       ('Laca', 'Evite apoiar objetos quentes ou arrastar peças metálicas na curva: a laca é dura, mas não é pedra.'),
       ('Espelho', 'Limpe com produto próprio para vidro, aplicado no pano — nunca borrifado direto na junta.')]
folha(f"""<div class="pad p7">
 <div class="eyebrow">O escopo</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 5mm">O que está — e o que não está — nesta proposta.</h1>
 <div class="es">
  <div class="es-c in"><div class="hk">Está incluso</div><ul>{''.join(f'<li>{E(x)}</li>' for x in INC)}</ul></div>
  <div class="es-c out"><div class="hk">Não está nesta proposta</div><ul>{''.join(f'<li>{E(x)}</li>' for x in FORA)}</ul>
   <p class="es-n">A parede chega pronta e aprumada para receber a marcenaria; no forro, deixamos os rasgos e a passagem para a iluminação do projeto.</p></div>
  <div class="es-g">
   <div class="gs"><div class="sl"><b>5</b><span>anos</span></div><div><div class="hk">Garantia Valvic</div>
    <p>Cinco anos sobre a marcenaria. Termo assinado na entrega.</p></div></div>
   {''.join(f'<div class="cu"><b>{E(t)}</b><p>{E(d)}</p></div>' for t, d in CUI)}
  </div>
 </div>
</div>""")

# ── 09 · investimento e condições ───────────────────────────────────────
rows = ''.join(f'<tr><td class="l">{E(n)}<div class="sub">{E(d)}</div></td><td class="hi">{brs(v)}</td></tr>'
               for n, d, v, _ in PR.VALORES)
pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{p*100:.0f}%</td><td class="d">{br(TOTAL * p)}</td></tr>'
              for r, p in PAGTO)
folha(f"""<div class="pad p8">
 <div class="eyebrow">Investimento e condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">O showroom completo.</h1>
 <div class="p3g">
  <div>
   <table class="inv inv3"><tr><th class="l">Item</th><th class="hi">Valor</th></tr>{rows}</table>
  </div>
  <div class="cx">
   <div class="tot"><div class="k">O projeto completo</div><div class="v">{br(TOTAL)}</div>
    <div class="sp"></div>
    <table class="pg">{pay}</table>
    <div class="ob">Todas as parcelas por transferência bancária.</div></div>
   <div class="cd">
    <div><div class="k">Prazo</div><div class="v">{E(PRAZO)}</div><div class="s">Contados a partir da medição técnica no local.</div></div>
    <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div><div class="s">A partir desta data.</div></div>
    <div><div class="k">Garantia</div><div class="v">5 anos</div><div class="s">Sobre a marcenaria.</div></div>
    <div><div class="k">Incluso</div><div class="v">Do projeto à instalação</div><div class="s">Executivo, material, laca, luz dos nichos, espelho, transporte, montagem.</div></div>
   </div>
  </div>
 </div>
 <div class="sig"><div class="ln">{E(CLIENTE)}</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>""")

EXTRA = '''
:root{--paper:#FCFAF5}
.slide{background:var(--paper)}
.slide.dark{background:var(--deep)}
.p1{display:grid;grid-template-columns:118mm 1fr;height:100%}
.p1-l{padding:16mm 12mm 12mm 16mm;display:flex;flex-direction:column;color:#F6F1E7}
.p1-nome{font-family:'Cormorant Garamond',Georgia,serif;font-size:40pt;line-height:.98;margin-top:9mm}
.p1-s{color:var(--gold-lt);font-size:9pt;letter-spacing:.06em;margin-top:3mm}
.p1-t{font-size:9pt;line-height:1.6;color:#D9D2C4;margin-top:7mm}
.p1-t b{color:#F6F1E7}
.p1-pil{display:grid;gap:2.6mm;margin-top:6mm}
.p1-pil div{border-left:2px solid var(--gold);padding-left:3mm}
.p1-pil b{display:block;font-size:8.2pt;color:#F6F1E7;letter-spacing:.04em}
.p1-pil span{font-size:7.6pt;color:#BDB5A6;line-height:1.45}
.p1-meta{display:grid;grid-template-columns:1fr 1fr;gap:3mm 6mm;margin-top:auto;padding-top:4mm;border-top:1px solid rgba(255,255,255,.14)}
.p1-meta .k{font-size:6.2pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-lt)}
.p1-meta .v{font-size:8.4pt;margin-top:.6mm}
.p1-r{display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:1fr 1fr;gap:2mm;padding:2mm 2mm 2mm 0}
.p1-r img{width:100%;height:100%;object-fit:cover;display:block;min-height:0}
.p1-r .g1{grid-row:1 / span 2}
.p2g{display:grid;grid-template-columns:1.55fr 1fr;gap:8mm;flex:1;min-height:0}
.movs{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:5mm;min-height:0}
.mv2{display:flex;flex-direction:column;min-height:0}
.mv2 .mi{position:relative;flex:1;min-height:0;overflow:hidden}
.mv2 .mi img{width:100%;height:100%;object-fit:cover;display:block}
.mv2 .mi span{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);font-family:'Cormorant Garamond',Georgia,serif;
  font-size:13pt;padding:1mm 4mm}
.mv2 .mt{padding-top:2.4mm}
.mv2 .mt b{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;font-weight:600}
.mv2 .mt p{font-size:7.7pt;color:var(--soft);line-height:1.45;margin-top:.6mm}
.het{background:var(--deep);color:#F6F1E7;border-radius:4px;padding:5mm;display:flex;flex-direction:column}
.het .hf{display:grid;grid-template-columns:1fr 1fr;gap:2mm;height:44mm}
.het .hf img{width:100%;height:100%;object-fit:cover;border-radius:2px;background:#fff}
.het .hk{font-size:6.4pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-lt);font-weight:600;margin-top:4mm}
.het .ht{font-family:'Cormorant Garamond',Georgia,serif;font-size:16pt;line-height:1.15;margin-top:1mm}
.het p{font-size:8pt;line-height:1.5;color:#D9D2C4;margin-top:2mm}
.het p b{color:#F6F1E7}
.het .hs{display:flex;gap:4mm;align-items:center;margin-top:auto;padding-top:4mm;border-top:1px solid rgba(226,201,142,.3)}
.het .sl{width:22mm;height:22mm;border-radius:50%;border:1.4px solid var(--gold-lt);display:flex;flex-direction:column;
  align-items:center;justify-content:center;flex:none}
.het .sl b{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;line-height:.9;color:var(--gold-lt);font-weight:600}
.het .sl span{font-size:5.8pt;letter-spacing:.24em;text-transform:uppercase}
.het .hs .hk{margin-top:0}
.het .hx{font-size:7.6pt;color:#D9D2C4;line-height:1.45;margin-top:.8mm}
.acab{margin-top:4mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);font-size:7.8pt;color:var(--soft)}
.acab b{color:var(--ink)}
.p2,.p3{padding-bottom:18mm}
.movs{grid-template-rows:auto auto;align-content:start}
.movs .mv2 .mi{flex:none;height:46mm}
.p3g{display:grid;grid-template-columns:1.2fr 1fr;gap:9mm;flex:1;min-height:0}
.inv3 td,.inv3 th{padding-top:2mm !important;padding-bottom:2mm !important;font-size:9.6pt}
.inv3 td .sub{font-size:7.2pt;color:var(--mut);font-weight:400;margin-top:.6mm}
.fora{margin-top:6mm;font-size:7.8pt;color:var(--soft);line-height:1.5}
.cx{display:flex;flex-direction:column;gap:5mm}
.tot{background:var(--deep);color:#F6F1E7;border-radius:4px;padding:5mm 6mm}
.tot .k{font-size:6.4pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-lt);font-weight:600}
.tot .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;line-height:1.05;margin-top:1mm}
.tot .sp{height:1px;background:rgba(226,201,142,.35);margin:3.6mm 0}
.tot .pg{width:100%;border-collapse:collapse;font-size:8.2pt}
.tot .pg td{padding:1.4mm 0;border-bottom:1px solid rgba(255,255,255,.1)}
.tot .pg td.d{text-align:right;color:var(--gold-lt);white-space:nowrap;padding-left:3mm}
.tot .ob{font-size:6.8pt;color:#BDB5A6;margin-top:2mm}
.cd{display:grid;grid-template-columns:1fr 1fr;gap:3.6mm 6mm}
.cd .k{font-size:6.4pt;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:700}
.cd .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;margin-top:.6mm}
.cd .s{font-size:7.2pt;color:var(--soft);line-height:1.4;margin-top:.4mm}
.sig{display:grid;grid-template-columns:1fr 1fr;gap:14mm;margin-top:6mm}
.sig .ln{border-top:1px solid var(--ink);padding-top:1.6mm;font-size:7.4pt;color:var(--soft)}
.p3x,.p4,.p5,.p6,.p7,.p8{padding-bottom:18mm}
.hk{font-size:6.4pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700}
.lg{display:grid;grid-template-columns:1.15fr 1fr;gap:9mm;flex:1;min-height:0}
.lg-i{display:flex;flex-direction:column;min-height:0}
.lg-i img{width:100%;flex:1;min-height:0;object-fit:cover;border-radius:3px}
.lg-i .cap{font-size:6.8pt;color:var(--mut);margin-top:1.6mm;letter-spacing:.06em}
.lg-t{display:flex;flex-direction:column;gap:3.4mm;min-height:0}
.lg-p{border-left:2px solid var(--gold-lt);padding-left:3.4mm}
.lg-p b{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;font-weight:600}
.lg-p p{font-size:8pt;color:var(--soft);line-height:1.45;margin:.4mm 0 0}
.lg-m{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm;flex:1;min-height:0;margin-top:1mm}
.lg-m img{width:100%;height:100%;object-fit:cover;border-radius:3px;min-height:0}
.pr{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;gap:5mm 6mm;flex:1;min-height:0}
.pr-c{border-top:1.5px solid var(--ink);padding:4mm 4mm 0;background:#FFFDF8;border-left:1px solid var(--line);border-right:1px solid var(--line);border-bottom:1px solid var(--line)}
.pr-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:32pt;color:var(--gold);line-height:1}
.pr-c b{display:block;font-size:11pt;margin-top:3mm}
.pr-c p{font-size:8.8pt;color:var(--soft);line-height:1.55;margin:2mm 0 0}
.ct{display:grid;grid-template-columns:2fr 1fr;gap:8mm;flex:1;min-height:0}
.ct-d{position:relative;background:#FFFDF8;border:1px solid var(--line);border-radius:4px;padding:5mm 4mm 7mm;display:flex;align-items:center}
.ct-s{flex:1}.ct-s svg{width:100%;height:auto;display:block}
.ct-a{position:absolute;left:5mm;bottom:8mm;width:16mm}.ct-a svg{width:100%;display:block}
.ct-l{position:absolute;right:5mm;bottom:2.6mm;font-size:6.4pt;color:var(--mut);letter-spacing:.08em}
.ct-t{display:flex;flex-direction:column;gap:4mm;justify-content:center}
.ct-p{display:grid;grid-template-columns:9mm 1fr;gap:3mm}
.ct-p .n{width:8mm;height:8mm;border-radius:50%;background:var(--deep);color:var(--gold-lt);display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',Georgia,serif;font-size:12pt}
.ct-p b{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;font-weight:600}
.ct-p p{font-size:7.9pt;color:var(--soft);line-height:1.5;margin:.4mm 0 0}
.lc{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:5mm 6mm;flex:1;min-height:0;margin-bottom:5mm}
.lc-c{background:#FFFDF8;border:1px solid var(--line);border-radius:4px;padding:5mm 5mm}
.lc-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:26pt;color:#4B2F22;line-height:1}
.lc-c b{display:block;font-size:10.6pt;margin-top:2mm}
.lc-c p{font-size:8.6pt;color:var(--soft);line-height:1.55;margin:1.4mm 0 0}
.lc-b{display:grid;grid-template-columns:52mm 1fr 1fr;gap:6mm;background:var(--deep);color:#F6F1E7;border-radius:4px;padding:5mm 6mm}
.lc-k .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;color:var(--gold-lt);line-height:1}
.lc-k .u{font-size:6.6pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-lt);margin-top:1mm}
.lc-k p,.lc-x p{font-size:7.8pt;color:#D9D2C4;line-height:1.5;margin:1.6mm 0 0}
.lc-x b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;font-weight:600}
.its{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:auto auto;gap:5mm 6mm;align-content:start}
.it .mi{position:relative;height:48mm;overflow:hidden;border-radius:2px}
.it .mi img{width:100%;height:100%;object-fit:cover;display:block}
.it .mi span{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);font-family:'Cormorant Garamond',Georgia,serif;font-size:13pt;padding:1mm 4mm}
.it b{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;font-weight:600;margin-top:2mm}
.it p{font-size:7.7pt;color:var(--soft);line-height:1.45;margin:.6mm 0 0}
.it-a{background:var(--deep);border-radius:4px;padding:5mm;color:#F6F1E7;display:flex;flex-direction:column;justify-content:center}
.it-a .hk{color:var(--gold-lt)}
.it-a p{font-size:8.2pt;line-height:1.6;color:#D9D2C4;margin:2mm 0 0}
.es{display:grid;grid-template-columns:1fr 1fr 1fr;gap:7mm;flex:1;min-height:0}
.es-c ul{margin:3mm 0 0;padding:0;list-style:none}
.es-c li{font-size:9.2pt;padding:2.6mm 0 2.6mm 6mm;border-bottom:1px solid var(--hair);position:relative}
.es-c.in li:before{content:'';position:absolute;left:0;top:3.6mm;width:2.6mm;height:1.4mm;border-left:1.5px solid var(--gold);border-bottom:1.5px solid var(--gold);transform:rotate(-45deg)}
.es-c.out li:before{content:'—';position:absolute;left:0;color:var(--mut)}
.es-c.out li{color:var(--soft)}
.es-n{font-size:7.6pt;color:var(--mut);line-height:1.5;margin-top:4mm}
.es-g{align-self:start;background:var(--deep);color:#F6F1E7;border-radius:4px;padding:5mm;display:flex;flex-direction:column;gap:3.4mm}
.es-g .hk{color:var(--gold-lt)}
.gs{display:flex;gap:4mm;align-items:center;padding-bottom:3.4mm;border-bottom:1px solid rgba(226,201,142,.3)}
.gs .sl{width:20mm;height:20mm;border-radius:50%;border:1.4px solid var(--gold-lt);display:flex;flex-direction:column;align-items:center;justify-content:center;flex:none}
.gs .sl b{font-family:'Cormorant Garamond',Georgia,serif;font-size:25pt;line-height:.9;color:var(--gold-lt);font-weight:600}
.gs .sl span{font-size:5.6pt;letter-spacing:.24em;text-transform:uppercase}
.gs p{font-size:7.8pt;color:#D9D2C4;margin:.8mm 0 0;line-height:1.45}
.cu b{font-size:8.4pt;color:#F6F1E7}
.cu p{font-size:8.2pt;color:#BDB5A6;line-height:1.45;margin:.4mm 0 0}
.rail{height:1.5px;background:linear-gradient(90deg,var(--gold),var(--gold-lt) 70%,var(--hair));
      margin:0;flex:none}
.proc{display:grid;grid-template-columns:repeat(4,1fr);gap:0 7mm;flex:1;min-height:0;
      margin-top:-1px;overflow:hidden;align-content:start;align-items:start}
.proc .pb{transform-origin:top left}
.pb{border-left:1px solid var(--hair);padding:5mm 5mm 0 5mm}
.pb:first-child{border-left:none;padding-left:0}
.pb-h{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);
      font-weight:700}
.pb-s{font-size:7.6pt;color:var(--mut);margin:1mm 0 3.4mm;min-height:6mm;line-height:1.35}
.pe{position:relative;padding:0 0 3.2mm 0}
.pe-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;color:var(--gold-lt);
      line-height:1;float:right;margin-left:3mm}
.pe-k{font-size:6pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);
      font-weight:700}
.pe-t{font-size:9.6pt;font-weight:700;margin:.6mm 0 1mm;letter-spacing:-.006em}
.pe-l{font-size:7.8pt;color:var(--soft);line-height:1.46}
.pe-e{font-size:7.1pt;color:var(--mut);margin-top:1.4mm;padding-left:3mm;
      border-left:1.5px solid var(--gold-pale);line-height:1.38}


.pv{display:grid;grid-template-columns:1.25fr 1fr;gap:7mm;flex:1;min-height:0}
.pv-d{background:#FFFDF8;border:1px solid var(--line);border-radius:4px;padding:4mm 5mm;display:flex;flex-direction:column}
.pv-s{flex:1;min-height:0;display:flex;align-items:center}.pv-s svg{width:100%;height:100%;display:block}
.pv-x{font-size:7.8pt;color:var(--soft);line-height:1.5;margin:2mm 0 0;border-top:1px solid var(--hair);padding-top:2.4mm}
.pv-x b{color:var(--ink)}
.pfs{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:4mm 5mm;min-height:0}
.pf{display:flex;flex-direction:column;min-height:0}
.pf-i{position:relative;flex:1;min-height:0;overflow:hidden;border-radius:2px;background:#fff;border:1px solid var(--hair)}
.pf-i img{width:100%;height:100%;object-fit:cover;display:block}
.pf-i span,.lf-i span{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);font-family:'Cormorant Garamond',Georgia,serif;font-size:12pt;padding:.6mm 3.4mm}
.pf b,.lf b{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:12.5pt;font-weight:600;margin-top:1.4mm;line-height:1.1}
.pf p,.lf p{font-size:7.3pt;color:var(--soft);line-height:1.42;margin:.6mm 0 0}
.lfs{display:grid;grid-template-columns:repeat(5,1fr);gap:4.5mm;flex:1;min-height:0;margin-bottom:5mm}
.lf{display:flex;flex-direction:column;min-height:0}
.lf-i{position:relative;flex:1;min-height:0;overflow:hidden;border-radius:2px}
.lf-i img{width:100%;height:100%;object-fit:cover;display:block}
'''
HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {E(CLIENTE)}</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&'
        'family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S) + '</body></html>')

# ── as travas ───────────────────────────────────────────────────────────
_t = re.sub(r'<[^>]+>', ' ', re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S)))
assert 'R$' not in ''.join(S[:-1]), '⛔ preço antes da folha de valor'
assert not [c for c in '⭐⛔⚠' if c in _t]
for _p in ('cartão', 'desconto', 'margem', 'telescópica', 'blum', 'sensys', 'mariana', 'odiney', 'hettich', 'luiza', 'custo', 'mc ', 'nada corta'):
    assert _p not in _t.lower(), _p
assert not re.search(r'\d+\s*(cm|mm|m²)', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg.*?</svg>', '', ''.join(S[:-1]), flags=re.S))), '⛔ medida na descrição'
OUT = R / 'proposta-centurion-motors-completa.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-centurion-motors-completa.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
npg = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(PDF)], capture_output=True, text=True).stdout).group(1))
assert npg == 9, f'⛔ a proposta tem de ter 9 páginas: saiu com {npg}'
print(f'{PDF.name} · {npg} folhas · {br(TOTAL)} · entrada {br(TOTAL * PAGTO[0][1])}')
