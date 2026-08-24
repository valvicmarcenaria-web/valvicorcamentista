# -*- coding: utf-8 -*-
"""CARLA · BH 2026 — PROPOSTA, 7 páginas.

Valores de `corte-carla.py`. [Jonathan 24/08] COM RT · ferragem HETTICH ·
interno em Branco TX + UPGRADE de tudo na cor.

  Investimento .................... R$ 109.300
  + Upgrade · tudo na cor ......... R$  18.500
  Com o upgrade ................... R$ 127.800
  (sem RT, referência interna) ..... R$  86.400 · MC 38,0%)

Sete detalhamentos executivos com QUADRO DE PEÇAS — o levantamento é
transcrição, não interpretação. É o melhor insumo que a casa já recebeu, e a
proposta pode dizer isso com todas as letras.

⚠ PRAZO e VALIDADE são premissas minhas.
⛔ MONTAGEM fora do custo (equipe é salário fixo), dentro do escopo entregue.
"""
import subprocess

CLIENTE   = 'Carla'
OBRA      = 'Apartamento em Belo Horizonte'
DATA      = '24 de agosto de 2026'
VALIDADE  = '7 dias corridos'
PRAZO     = 'Até 75 dias corridos'

INV, UP = 109300, 18500
INV_UP = INV + UP
assert INV_UP == 127800

ITENS = [
 ('01', 'Cozinha linear com torre de geladeira',
  'Sequência de 3,89 m — 400 + 800 + 1170 + 600 + 920 mm — com 2,45 m de altura total.',
  ['<strong>Armários inferiores</strong> de 65 cm de profundidade em quatro '
   'módulos, com nicho para lava-louças de embutir e gaveteiro no módulo do '
   'cooktop.',
   '<strong>Aéreos</strong> com três portas (585 · 585 · 600) e 55 cm de altura, '
   'alinhados à porta superior da torre.',
   '<strong>Nicho contínuo de 1,77 m</strong> em MDF de 25 mm amadeirado, sem '
   'divisória, encostado na base dos aéreos — com ventilação e passa-cabo '
   'previstos para forno e micro-ondas.',
   '<strong>Torre da geladeira</strong> de 92 × 90 × 245, com o fundo alinhado '
   'ao fundo da bancada e avanço frontal de 25 cm.',
   'Puxador em <strong>cava usinada</strong> e iluminação em LED 3000 K sob o '
   'aéreo e dentro do nicho.'],
  22200),
 ('02', 'Painel amadeirado até o forro',
  '6,57 × 2,45 m, com porta integrada, espelho e frisos verticais.',
  ['<strong>Painel de 6,57 m</strong> sobre estrutura niveladora de sarrafo, '
   'ancorada à parede — não é chapa colada em reboco.',
   '<strong>Porta de 700 × 2100 integrada ao painel</strong>, com batente '
   'oculto, dobradiça invisível reforçada e folga perimetral de 3 mm. De fora, '
   'a parede é contínua e a porta some nela.',
   '<strong>Espelho de 2,50 × 1,10 m</strong> lapidado, com película de '
   'segurança, instalado entre os dois primeiros conjuntos de frisos.',
   '<strong>Três faixas de frisos verticais</strong>, cinco linhas cada, '
   'usinados no próprio MDF.',
   'Reforço estrutural previsto para TV e rack: a carga não fica na chapa.'],
  15500),
 ('03', 'Rack suspenso de 3,58 m',
  'Quatro frentes basculantes de 895 mm, 40 cm de profundidade.',
  ['<strong>Quatro portas basculantes</strong> com articulador dimensionado '
   'pela massa real de cada frente.',
   'Tampo e base <strong>engrossados para 25 mm</strong> — num móvel suspenso '
   'de 3,58 m, rigidez é estrutura, não estética.',
   '<strong>Barra metálica contínua de fixação</strong> ancorada na alvenaria. '
   'O painel decorativo não recebe sozinho a carga do rack.',
   '<strong>LED 3000 K</strong> em perfil de alumínio recuado 40 mm, com '
   'difusor leitoso, e ventilação técnica para os equipamentos.'],
  5200),
 ('04', 'Cristaleira até o forro',
  '920 × 400 × 2450, com duas portas de vidro e seis prateleiras iluminadas.',
  ['<strong>Duas portas de giro</strong> em perfil de alumínio preto e vidro '
   'temperado de 6 mm, com puxador vertical metálico.',
   '<strong>Seis prateleiras de vidro temperado de 8 mm</strong> lapidado, cada '
   'uma com seu perfil de LED 3000 K.',
   'Lateral esquerda de 550 mm — 400 do móvel e 150 de acabamento até a parede '
   '— para absorver o desaprumo sem deixar fresta.',
   'Base niveladora de 80 mm e arremate superior recortado em obra, depois do '
   'nivelamento.'],
  4900),
 ('05', 'Guarda-roupa de três portas de correr',
  '2,55 × 0,64 × 2,68 m, com porta central espelhada.',
  ['<strong>Três folhas deslizantes</strong> em perfil de alumínio escuro, com '
   'roldana regulável e sistema antidescarrilamento.',
   '<strong>Porta central integral em espelho</strong> prata com película de '
   'segurança.',
   '<strong>Oito gavetas</strong> em corrediça oculta, prateleiras e maleiro '
   'superior com prateleira engrossada.',
   'Dois cabideiros ovais metálicos com suporte reforçado, mantendo 550 mm '
   'úteis de profundidade para os cabides.'],
  27500),
 ('06', 'Guarda-roupa em L com cabeceira',
  '1,97 m de roupeiro mais o retorno com mesa, nicho e aéreo.',
  ['<strong>Roupeiro de 1,97 m</strong> modulado em 490 + 490 + 490 + 500, com '
   'quatro portas de giro de 2,68 m e cabideiro contínuo.',
   '<strong>Mesa de cabeceira</strong> de 500 × 500 × 700 com duas gavetas, '
   'alinhada ao último módulo do roupeiro.',
   '<strong>Módulo vertical</strong> de 500 × 500 × 1200 com prateleiras.',
   '<strong>Nicho de 1,42 m</strong> sobre a cabeceira, em MDF de 25 mm, com '
   'fita de LED e passa-fio previstos.',
   '<strong>Armário aéreo</strong> de 1,42 × 0,40 × 0,75 com duas portas de giro.'],
  25900),
 ('07', 'Marcenaria sob a escada',
  '2,39 m de largura, 40 cm de profundidade, acompanhando o intradorso.',
  ['<strong>Porta em vidro Reflecta temperado</strong> de 890 × 1760 em perfil '
   'de alumínio preto, com três dobradiças reforçadas e puxador vertical.',
   '<strong>Nichos com geometria diagonal</strong> — 1,50 m de largura, altura '
   'máxima de 1,06 m, terminando zerados sobre a base.',
   '<strong>LED 3000 K inclusive nos nichos diagonais</strong>, em perfil '
   'recuado, sem ponto aparente.',
   'Prateleiras engrossadas para 25 mm, rodapé recuado de 50 mm e folga técnica '
   'posterior de 20 mm.'],
  8100),
]
assert sum(i[4] for i in ITENS) == INV

ESPEC = [
 ('Chapa', 'MDF BP <strong>18 mm</strong> na caixaria e nas frentes, '
  '<strong>25 mm</strong> nos nichos e nas prateleiras longas, e '
  '<strong>6 mm</strong> nos fundos encaixados — exatamente as espessuras que '
  'os quadros de peças das pranchas especificam.'),
 ('Borda', 'Fita <strong>ABS de 1 mm</strong> nas faces aparentes e 0,45 mm nas '
  'não aparentes, aplicada em coladeira automática.'),
 ('Puxador', '<strong>Cava usinada</strong> no próprio material, e perfil '
  'vertical preto onde a prancha pede.'),
 ('Ferragem', 'Linha <strong>Hettich</strong> em todo o projeto: dobradiça '
  '<strong>Novisys</strong> com amortecimento, corrediça oculta '
  '<strong>Quadro</strong> e articulador <strong>Blum HK-xs</strong> nas '
  'básculas do rack.'),
 ('Iluminação', 'Fita de LED <strong>24 V · 3000 K · IRC ≥ 90</strong> em perfil '
  'de alumínio com difusor leitoso, com driver bivolt dimensionado com 20% de '
  'reserva e acessível para manutenção.'),
 ('Vidro e espelho', 'Espelho lapidado com <strong>película de segurança</strong> '
  'no painel e na porta central do roupeiro; vidro temperado nas portas da '
  'cristaleira, nas prateleiras e na porta Reflecta sob a escada.'),
 ('Fixação', 'Niveladores, cantoneiras ocultas e ancoragem <strong>na alvenaria '
  'ou na estrutura</strong> — nunca só no painel decorativo.'),
 ('Produção e montagem', 'Corte e usinagem em <strong>CNC própria</strong>, '
  'laminação de borda em coladeira automática própria, e <strong>instalação e '
  'montagem por equipe própria da Valvic</strong>.'),
]

PAGTO = [
    ('Entrada de 30% + saldo em até 10× no cartão', '—'),
    ('Entrada de 50% + saldo em até 8× no cartão',  '3%'),
    ('Entrada de 70% + saldo em até 6× no cartão',  '5%'),
    ('Entrada de 70% + saldo por transferência',    '7%'),
]

FORA = [
 ('Tampo e rodabanca da cozinha', 'A prancha especifica <strong>pedra de 20 mm</strong> '
  'sobre 2,97 × 0,65 m. É fornecimento de marmoraria.'),
 ('Eletrodomésticos, louças e metais', 'Cooktop, forno, micro-ondas, lava-louças, '
  'geladeira, coifa, cuba e torneira. Prevemos o vão e a usinagem — precisamos '
  'das medidas de fábrica antes do corte.'),
 ('Elétrica e hidráulica', 'A iluminação embutida NA marcenaria é nossa; os '
  'pontos de energia, água e esgoto e os circuitos exclusivos dos '
  'eletrodomésticos são da obra.'),
 ('Alvenaria, gesso, revestimento e pintura', 'Inclusive o forro sobre o qual o '
  'painel, a cristaleira e os roupeiros são arrematados.'),
 ('Móveis soltos, cortinas e decoração', 'Cama, mesa de jantar, cadeiras, '
  'poltronas, tapetes e TV.'),
]

CSS = open('projetos/css-proposta.css', encoding='utf-8').read() + """
.mem{padding:3.4mm 0;border-bottom:1px solid var(--hair);}
.mem:last-child{border-bottom:none;}
.mem-h{display:flex;align-items:baseline;gap:4mm;}
.mem-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:16pt;
  color:var(--gold-lt);font-weight:600;line-height:1;min-width:9mm;}
.mem-t{font-size:10.6pt;font-weight:700;letter-spacing:-.005em;}
.mem-q{margin-left:auto;font-size:9.6pt;font-weight:700;white-space:nowrap;}
.mem-m{color:var(--soft);font-size:8.3pt;margin:1.4mm 0 0 13mm;font-style:italic;}
.mem ul{margin:1.8mm 0 0 13mm;padding:0;}
.mem li{list-style:none;color:var(--soft);font-size:8.3pt;line-height:1.5;
  margin-bottom:1.3mm;padding-left:4.5mm;position:relative;}
.mem li::before{content:'';position:absolute;left:0;top:1.8mm;width:3.5px;
  height:3.5px;border-radius:50%;background:var(--gold-lt);}
.esp{padding:2.6mm 0;border-bottom:1px solid var(--hair);display:grid;
  grid-template-columns:32mm 1fr;gap:5mm;}
.esp:last-child{border-bottom:none;}
.esp .k{font-size:7.2pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;padding-top:.5mm;}
.esp .v{color:var(--soft);font-size:8.6pt;}
.up{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:6mm;}
.up .c{border:1px solid var(--line);border-radius:2px;padding:5.5mm 6mm;}
.up .c.hi{background:var(--deep);border-color:var(--deep);color:#F6F1E7;}
.up .k{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.up .c.hi .k{color:var(--gold-lt);}
.up .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;
  line-height:1.05;font-weight:600;margin-top:2mm;}
.up .s{color:var(--soft);font-size:8.4pt;margin-top:2mm;}
.up .c.hi .s{color:#CFC6B4;}
"""

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 9
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>{OBRA}</span><span>{n} / {NP}</span></div>')
def mem(i):
    n, t, sub, bul, v = i
    li = ''.join(f'<li>{b}</li>' for b in bul)
    return (f'<div class="mem"><div class="mem-h"><div class="mem-n">{n}</div>'
            f'<div class="mem-t">{t}</div><div class="mem-q">R$ {brl(v)}</div></div>'
            f'<div class="mem-m">{sub}</div><ul>{li}</ul></div>')

p1 = f"""<div class="page cover"><div class="pad">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div style="margin-top:auto">
    <div class="eyebrow">Proposta de marcenaria planejada para</div>
    <div class="rule"></div>
    <div class="cv-t">{CLIENTE}</div>
    <div class="cv-s">{OBRA}<br>Sete conjuntos, sobre projeto executivo detalhado</div>
  </div>
  <div class="cv-meta">
    <div><div class="k">Garantia Valvic</div><div class="v">10 anos</div></div>
    <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O que está sendo proposto</div>
  <div class="rule"></div>
  <h2 class="h-sec">Sete conjuntos, sobre<br>projeto executivo detalhado.</h2>
  <p class="lead" style="margin-top:4mm">Seu projeto chegou com uma coisa rara:
  <strong>quadro de peças</strong>. Cada prancha lista código, quantidade,
  espessura e dimensão de cada peça. Isso significa que este orçamento é
  <strong>transcrição, não estimativa</strong> — não houve arredondamento por
  metro quadrado nem chute de modulação. São <strong>133 m² de chapa</strong>,
  contados peça a peça.</p>
  {mem(ITENS[0])}
  {mem(ITENS[1])}
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  {mem(ITENS[2])}
  {mem(ITENS[3])}
  {mem(ITENS[4])}
  {foot(3)}
</div></div>"""

p4 = f"""<div class="page"><div class="pad">
  {mem(ITENS[5])}
  {mem(ITENS[6])}
  <div class="box" style="margin-top:6mm"><div class="t">Onde a prancha pede conferência</div>
  <p>Os detalhamentos marcam alguns pontos como "conferir em obra": a cota
  vertical do rack, a inclinação real da escada e os modelos definitivos dos
  eletrodomésticos. <strong>Nada vai para a CNC antes da nossa medição no
  local</strong> — é assim que a prancha pede e é assim que trabalhamos.</p></div>
  {foot(4)}
</div></div>"""

p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Ferragem e garantia</div>
  <div class="rule"></div>
  <h2 class="h-sec">Hettich em todo o projeto.<br>Dez anos de garantia Valvic.</h2>
  <p class="lead" style="margin-top:4mm">Ferragem se mede em ciclo de abertura,
  amortecimento e regulagem. Neste projeto são <strong>46 dobradiças, 13
  corrediças e 4 articuladores</strong> — e todos na linha superior, sem degrau
  intermediário.</p>
  <div class="cen hi" style="margin-top:6mm">
    <div class="cen-h"><div class="cen-n">★</div>
      <div class="cen-t">Linha Hettich</div>
      <div class="cen-g">Garantia 10 anos</div></div>
    <div class="cen-x">A corrediça Quadro tem curso mais longo, carga maior,
    retorno mais macio e ciclo de teste muito acima do uso doméstico. Nas oito
    gavetas do roupeiro de correr e nas quatro básculas do rack, é o que separa
    um móvel que abre bem no primeiro ano de um que abre bem no décimo.</div>
    <div class="cen-l">
      <div><div class="k">Dobradiça</div><div class="v">Hettich Novisys</div></div>
      <div><div class="k">Corrediça</div><div class="v">Oculta Hettich Quadro</div></div>
      <div><div class="k">Báscula</div><div class="v">Articulador Blum HK-xs</div></div>
    </div>
  </div>
  <div class="box"><div class="t">Sobre a garantia</div>
  <p>Os dez anos são <strong>garantia Valvic</strong> — nossa, escrita e
  assinada na entrega, cobrindo estrutura, ferragem e acabamento. Não é a
  garantia do fabricante da ferragem, que não faz parte do que vendemos.</p></div>
  <div class="box"><div class="t">Sobre a montagem</div>
  <p>A <strong>instalação e a montagem são feitas por equipe própria da
  Valvic</strong> e estão dentro deste valor. Quem produz é quem monta, e é a
  mesma empresa que responde pela garantia.</p></div>
  {foot(5)}
</div></div>"""

p6 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Upgrade de projeto</div>
  <div class="rule"></div>
  <h2 class="h-sec">O interior na mesma cor<br>da estrutura externa.</h2>
  <p class="lead" style="margin-top:4mm">O projeto especifica o interior dos
  armários em <strong>MDF Branco TX</strong> — fora na cor, dentro em branco. É
  o padrão do mercado e é o que está no valor abaixo.</p>
  <p class="lead" style="margin-top:3mm">O upgrade troca esse interior pela
  <strong>mesma cor da frente</strong>, e é <strong>integral</strong>: caixaria,
  prateleiras, fundos, caixa de gaveta e todo o miolo dos sete conjuntos. São
  <strong>85 m²</strong> que deixam de ser brancos. <strong>Nenhuma peça branca
  fica no projeto.</strong></p>
  <div class="up">
    <div class="c"><div class="k">Como o projeto especifica</div>
      <div class="v" style="color:var(--mut)">R$ {brl(INV)}</div>
      <div class="s">Interior em MDF Branco TX, ferragem Hettich, garantia de
      10 anos.</div></div>
    <div class="c hi"><div class="k">Com o upgrade · tudo na cor</div>
      <div class="v">R$ {brl(INV_UP)}</div>
      <div class="s">Upgrade de <strong>R$ {brl(UP)}</strong>. Mesmo escopo,
      mesma ferragem, mesma garantia.</div></div>
  </div>
  <div class="box" style="margin-top:6mm"><div class="t">Por que ele custa isso</div>
  <p>Não é só a diferença de preço entre a chapa branca e a colorida. Quando o
  interior muda de cor, ele <strong>deixa de dividir chapa branca com todos os
  módulos</strong> e passa a dividir chapa colorida com a frente do seu próprio
  móvel — e cor nenhuma divide chapa com outra. São duas chapas a mais no plano
  de corte, além do preço maior por chapa.</p></div>
  {foot(6)}
</div></div>"""

linhas = ''.join(f'<tr><td class="l">{n} · {t}</td><td class="hi">{brl(v)}</td></tr>'
                 for n, t, _s, _b, v in ITENS)
esp = ''.join(f'<div class="esp"><div class="k">{k}</div><div class="v">{v}</div></div>'
              for k, v in ESPEC)
fora = ''.join(f'<li><div class="k">{k}</div><div class="v">{v}</div></li>'
               for k, v in FORA)

p7 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Conjunto a conjunto.</h2>
  <table class="inv" style="margin-top:6mm">
    <tr><th class="l">Conjunto</th><th class="hi">Investimento</th></tr>
    {linhas}
    <tr class="tot"><td class="l">Investimento total</td>
      <td class="hi">{brl(INV)}</td></tr>
    <tr><td class="l" style="padding-top:3mm;color:var(--gold);font-weight:600">
      + Upgrade · tudo na cor</td>
      <td class="hi" style="padding-top:3mm">{brl(UP)}</td></tr>
    <tr class="tot"><td class="l">Com o upgrade</td>
      <td class="hi">{brl(INV_UP)}</td></tr>
  </table>
  <div class="box" style="margin-top:6mm"><div class="t">O que está dentro do valor</div>
  <p>Projeto executivo de marcenaria, fornecimento de material, produção em CNC
  e coladeira automática próprias, espelhos com película de segurança, portas de
  vidro temperado, prateleiras de vidro, porta Reflecta, sistema de correr de
  três folhas, cabideiros, iluminação em LED com driver, transporte, entrega na
  obra e <strong>instalação e montagem por equipe própria da Valvic</strong>.</p></div>
  <div class="box"><div class="t">Coordenação de projeto</div>
  <p>O acompanhamento do projeto executivo está contemplado no valor, com e sem
  o upgrade.</p></div>
  {foot(7)}
</div></div>"""

p8 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h-sec">Prazo, pagamento<br>e fronteiras.</h2>
  <div class="two" style="margin-top:7mm">
    <div>
      <table class="pay">
        <tr><td colspan="2" style="border:none;padding-bottom:1.4mm">
          <span class="eyebrow">Formas de pagamento</span></td></tr>
        {''.join(f'<tr><td>{c}</td><td class="d">{d}</td></tr>' for c, d in PAGTO)}
      </table>
      <p style="color:var(--mut);font-size:7.9pt;margin-top:2.5mm">
      O desconto por transferência devolve ao cliente a taxa de máquina que
      deixamos de pagar.</p>
      <div class="term" style="margin-top:3mm"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da aprovação e da medição em obra.</div></div>
      <div class="term"><div class="k">Validade da proposta</div>
        <div class="v">{VALIDADE}</div></div>
      <div class="term"><div class="k">Garantia</div>
        <div class="v">10 anos, Valvic</div>
        <div class="s">Escrita e assinada na entrega, cobrindo estrutura,
        ferragem e acabamento.</div></div>
      <div class="term"><div class="k">Conferência de medidas</div>
        <div class="v">Visita técnica antes do corte</div>
        <div class="s">As próprias pranchas marcam "conferir em obra" na cota
        vertical do rack, na inclinação da escada e nos modelos dos
        eletrodomésticos. Nada vai para a CNC antes da nossa medição.</div></div>
    </div>
    <div class="fora">
      <div class="eyebrow">Não incluso nesta proposta</div>
      <div class="rule"></div>
      <ul>{fora}</ul>
    </div>
  </div>
  {foot(8)}
</div></div>"""

p9 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="rule"></div>
  <h2 class="h-sec">O que atravessa<br>o projeto inteiro.</h2>
  <p class="lead" style="margin-top:3.5mm">As oito linhas abaixo valem para os
  sete conjuntos, e são o que sustenta a garantia de dez anos.</p>
  <div style="margin-top:5mm">{esp}</div>
  <div class="sig">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">{CLIENTE}</div>
  </div>
  {foot(9)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>'
        f'{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}</body></html>')

OUT_H, OUT_P = 'projetos/proposta-carla.html', 'projetos/proposta-carla.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML)
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}   ·   R$ {brl(INV)}  ·  com upgrade R$ {brl(INV_UP)}')
