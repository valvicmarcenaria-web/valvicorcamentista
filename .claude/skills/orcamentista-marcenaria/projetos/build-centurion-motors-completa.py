# -*- coding: utf-8 -*-
"""CENTURION MOTORS — Showroom Vila da Serra · proposta COMPLETA em OITO páginas  [26/11/2026]

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
    f = (f'<div class="foot"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span><span>{N[0]:02d} / 08</span></div>'
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

# ── 03 · como trabalhamos ──────────────────────────────────────────────
PROC = [('01', 'Medição técnica', 'Conferimos no local prumo, nível e esquadro de paredes e laje — é daqui que sai o executivo, não da planta.'),
        ('02', 'Executivo e engenharia de produto', 'Cada pórtico, costela, painel e módulo de forro é desenhado peça por peça, com o plano de corte e a lista de compra.'),
        ('03', 'Aprovação', 'O executivo passa pelas arquitetas e por vocês antes de qualquer corte: nada é fabricado sem aprovação.'),
        ('04', 'Compra e corte', 'Chapas, compensado flexível, fórmica e espelho comprados para este projeto; corte e usinagem em máquina.'),
        ('05', 'Fabricação', 'Esqueletos, curvas e painéis montados na fábrica, com o arco conferido no gabarito antes de seguir.'),
        ('06', 'Acabamento', 'Laca aplicada em cabine, em camadas, com o nosso controle em cada demão e o tempo de cura respeitado.'),
        ('07', 'Transporte e instalação', 'Peças embaladas e protegidas; equipe própria na obra, fixação na estrutura e arremates finais.'),
        ('08', 'Entrega', 'Vistoria conjunta, regulagem final e termo de garantia assinado na entrega.')]
folha(f"""<div class="pad p3x">
 <div class="eyebrow">Como trabalhamos</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">Do primeiro traço à última regulagem, um só responsável.</h1>
 <p class="lead" style="max-width:200mm;margin:0 0 6mm">A Valvic não revende móvel: projeta o executivo, fabrica e instala. Em uma obra
  comercial isso significa um único interlocutor para prazo, qualidade e garantia — e nenhum vazio entre quem
  desenha, quem fabrica e quem monta.</p>
 <div class="pr">{''.join(f'<div class="pr-c"><div class="pr-n">{n}</div><b>{E(t)}</b><p>{E(d)}</p></div>' for n, t, d in PROC)}</div>
</div>""")

# ── 04 · do esqueleto à laca (o corte) ─────────────────────────────────
SVG = '''<svg viewBox="4 0 462 250" xmlns="http://www.w3.org/2000/svg" font-family="DM Sans,Arial,sans-serif">
 <defs><pattern id="mdf" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#F2EFE8"/>
  <circle cx="1.5" cy="1.5" r=".55" fill="#CFC8BA"/><circle cx="4.5" cy="4.2" r=".45" fill="#CFC8BA"/></pattern>
  <pattern id="comp" width="8" height="4" patternUnits="userSpaceOnUse"><rect width="8" height="4" fill="#D9B98A"/>
  <line x1="0" y1="2" x2="8" y2="2" stroke="#B8915C" stroke-width=".5"/></pattern></defs>
 <text x="150" y="16" font-size="7.5" fill="#918A7C" text-anchor="middle" letter-spacing="1.5">EXTRADORSO · OCULTO ENTRE OS PÓRTICOS</text>
 <rect x="40" y="26" width="220" height="8" fill="url(#comp)" stroke="#8C6A3F" stroke-width=".6"/>
 <rect x="40" y="34" width="12" height="150" fill="url(#mdf)" stroke="#9A9284" stroke-width=".6"/>
 <rect x="248" y="34" width="12" height="150" fill="url(#mdf)" stroke="#9A9284" stroke-width=".6"/>
 <rect x="52" y="104" width="196" height="9" fill="url(#mdf)" stroke="#9A9284" stroke-width=".6"/>
 <rect x="40" y="184" width="220" height="8" fill="url(#comp)" stroke="#8C6A3F" stroke-width=".6"/>
 <rect x="40" y="192" width="220" height="5" fill="#C9CCCE" stroke="#8E9296" stroke-width=".5"/>
 <rect x="34" y="197" width="226" height="5" fill="#4B2F22"/>
 <rect x="26" y="22" width="14" height="175" fill="url(#mdf)" stroke="#9A9284" stroke-width=".6"/>
 <rect x="20" y="22" width="6" height="180" fill="#4B2F22"/>
 <text x="150" y="222" font-size="7.5" fill="#4B2F22" text-anchor="middle" letter-spacing="1.5" font-weight="700">INTRADORSO · O QUE SE VÊ NO VÃO</text>
 <text x="12" y="112" font-size="7" fill="#918A7C" transform="rotate(-90 12 112)" text-anchor="middle" letter-spacing="1.2">FRENTE · SALÃO</text>
 <text x="272" y="112" font-size="7" fill="#918A7C" transform="rotate(90 272 112)" text-anchor="middle" letter-spacing="1.2">FUNDO · PAREDE</text>
 <g stroke="#9C7A3C" stroke-width=".7" fill="#9C7A3C" font-size="9">
  <line x1="254" y1="60" x2="300" y2="40"/><circle cx="254" cy="60" r="1.6"/>
  <line x1="200" y1="108" x2="300" y2="74"/><circle cx="200" cy="108" r="1.6"/>
  <line x1="230" y1="30" x2="300" y2="108"/><circle cx="230" cy="30" r="1.6"/>
  <line x1="230" y1="188" x2="300" y2="142"/><circle cx="230" cy="188" r="1.6"/>
  <line x1="215" y1="194.5" x2="300" y2="176"/><circle cx="215" cy="194.5" r="1.6"/>
  <line x1="190" y1="199.5" x2="300" y2="210"/><circle cx="190" cy="199.5" r="1.6"/>
  <line x1="33" y1="180" x2="38" y2="234" /><circle cx="33" cy="180" r="1.6"/>
 </g>
 <g font-size="9.4" fill="#1A1714">
  <text x="306" y="43"><tspan font-weight="700">1 · Costelas</tspan><tspan x="306" dy="10" font-size="7.6" fill="#5C564C">o esqueleto, no desenho exato do arco</tspan></text>
  <text x="306" y="77"><tspan font-weight="700">2 · Travessas</tspan><tspan x="306" dy="10" font-size="7.6" fill="#5C564C">amarram as costelas e travam o prumo</tspan></text>
  <text x="306" y="111"><tspan font-weight="700">3 · Compensado flexível · fora</tspan><tspan x="306" dy="10" font-size="7.6" fill="#5C564C">a pele que fecha o arco por cima</tspan></text>
  <text x="306" y="145"><tspan font-weight="700">3 · Compensado flexível · dentro</tspan><tspan x="306" dy="10" font-size="7.6" fill="#5C564C">a curva do vão, colada às costelas</tspan></text>
  <text x="306" y="179"><tspan font-weight="700">4 · Fórmica</tspan><tspan x="306" dy="10" font-size="7.6" fill="#5C564C">a base lisa, dura e estável da laca</tspan></text>
  <text x="306" y="213"><tspan font-weight="700">5 · Laca PU fosca café</tspan><tspan x="306" dy="10" font-size="7.6" fill="#5C564C">aderência, fundo e acabamento</tspan></text>
  <text x="40" y="244"><tspan font-weight="700">6 · Alizar laqueado</tspan><tspan font-size="7.6" fill="#5C564C"> · a moldura vista de frente</tspan></text>
 </g>
</svg>'''
ARCO = '''<svg viewBox="0 0 120 150" xmlns="http://www.w3.org/2000/svg">
 <path d="M10 148 V60 A50 50 0 0 1 110 60 V148 H96 V60 A36 36 0 0 0 24 60 V148 Z" fill="#4B2F22"/>
 <path d="M24 148 V60 A36 36 0 0 1 96 60 V148 Z" fill="#E9DCC6"/>
 <line x1="60" y1="2" x2="60" y2="30" stroke="#9C7A3C" stroke-width="1.2" stroke-dasharray="3 2"/>
 <text x="66" y="12" font-size="9" fill="#9C7A3C" font-family="DM Sans,Arial" font-weight="700">corte</text>
</svg>'''
CAM = [('Esqueleto', 'Costelas recortadas no desenho exato do arco e amarradas por travessas em espaçamento regular. É a estrutura que dá a forma: '
        'conferida em nível e prumo no gabarito, porque uma costela fora de prumo vira uma onda visível na laca.'),
       ('Compensado flexível', 'Lâminas orientadas para curvar num só sentido — o sentido da curva é escolhido antes da compra. '
        'Ele não se sustenta sozinho: veste o esqueleto por dentro e por fora, colado com cola de contato.'),
       ('Fórmica', 'O compensado tem veio aberto e pequenas ondulações que apareceriam através da laca. A fórmica fecha a superfície: '
        'curva a frio no raio largo destes arcos, assentada com rolo do centro para as bordas, sem bolha. A emenda da folha é posicionada no corte e desaparece sob a laca.'),
       ('Laca', 'Por último, e só sobre a base perfeita: aderência, fundo e acabamento fosco café — detalhados na folha seguinte.')]
folha(f"""<div class="pad p4">
 <div class="eyebrow">O pórtico curvo · do esqueleto à laca</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">Uma curva perfeita é feita de quatro camadas.</h1>
 <div class="ct">
  <div class="ct-d"><div class="ct-a">{ARCO}</div><div class="ct-s">{SVG}</div>
   <div class="ct-l">Corte no alto do arco · ilustrativo, fora de escala</div></div>
  <div class="ct-t">{''.join(f'<div class="ct-p"><div class="n">{i}</div><div><b>{E(t)}</b><p>{E(d)}</p></div></div>' for i, (t, d) in enumerate(CAM, 1))}</div>
 </div>
</div>""")

# ── 05 · a laca, demão por demão ───────────────────────────────────────
LACA = [('Preparo', 'A fórmica é desengordurada e recebe uma lixa leve — só o suficiente para criar a ancoragem, sem atravessar o laminado.'),
        ('Primer de aderência', 'A etapa decisiva: a fórmica não absorve nada, e é o primer próprio para superfície lisa que prende a laca a ela. A face e o alizar, em MDF, recebem o fundo direto.'),
        ('Fundo PU', 'Aplicado em camadas e lixado com lixa fina. É depois do fundo que aparecem imperfeições antes invisíveis — e é aqui que elas são corrigidas.'),
        ('Laca PU fosca café', 'Catalisada e aplicada com pistola, em cabine, em camadas finas e contínuas, com o lixamento separado da pintura: pó em suspensão é o maior inimigo do acabamento liso.'),
        ('Cura', 'A laca PU endurece por reação química, e reação precisa de tempo. A peça só é embalada depois da cura completa.'),
        ('Inspeção', 'Cada pórtico é conferido sob luz rasante antes de sair: a curva tem de correr limpa, sem onda, sem marca de emenda.')]
folha(f"""<div class="pad p5">
 <div class="eyebrow">A laca · demão por demão</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 5mm">O café do projeto, com acabamento de peça única.</h1>
 <div class="lc">{''.join(f'<div class="lc-c"><div class="lc-n">{i:02d}</div><b>{E(t)}</b><p>{E(d)}</p></div>' for i, (t, d) in enumerate(LACA, 1))}</div>
 <div class="lc-b">
  <div class="lc-k"><div class="big">5 a 7</div><div class="u">dias de cura</div><p>antes de embalar a peça. Pressa aqui é a laca marcada na obra.</p></div>
  <div class="lc-x"><b>Por que fórmica por baixo da laca?</b><p>Laca é rígida: se o que está por baixo trabalha, ela trinca na emenda ou no
   encontro do arco com o pilar. O esqueleto firme, o compensado bem colado e a fórmica estável são o que mantém a curva lisa por anos —
   a laca é a última camada, nunca a que corrige.</p></div>
  <div class="lc-x"><b>Clima de pintura</b><p>Frio intenso ou umidade alta pedem adiar a demão: a laca não cura direito e perde o acabamento.
   A cabine controla isso — a obra, não. Por isso nenhum pórtico é laqueado no local.</p></div>
 </div>
</div>""")

# ── 06 · os itens ──────────────────────────────────────────────────────
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

# ── 07 · o que está e o que não está ───────────────────────────────────
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

# ── 08 · investimento e condições ───────────────────────────────────────
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
assert npg == 8, f'⛔ a proposta tem de ter 8 páginas: saiu com {npg}'
print(f'{PDF.name} · {npg} folhas · {br(TOTAL)} · entrada {br(TOTAL * PAGTO[0][1])}')
