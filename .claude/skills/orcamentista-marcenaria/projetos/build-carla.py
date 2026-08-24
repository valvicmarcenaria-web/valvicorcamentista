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

# ⛔ SEM UMA ÚNICA COTA. Regra da casa, em `referencias/proposta-comercial.md`:
#    medida de móvel NÃO vai na proposta. Onde a dimensão é o argumento, ela é
#    dita EM PALAVRAS — "do piso ao forro", "parede inteira", "sem divisória".
ITENS = [
 ('01', 'Cozinha linear com torre de geladeira',
  'Bancada linear com a torre da geladeira integrada, do piso ao forro.',
  ['<strong>Armários inferiores</strong> em quatro módulos, com nicho para '
   'lava-louças de embutir e gaveteiro no módulo do cooktop.',
   '<strong>Aéreos com três portas</strong>, alinhados à porta superior da '
   'torre: a linha de cima corre sem degrau de uma ponta à outra.',
   '<strong>Nicho contínuo sem divisória</strong>, em MDF encorpado, encostado '
   'na base dos aéreos — forno e micro-ondas ficam lado a lado, sem moldura '
   'entre eles, com ventilação e passa-cabo previstos.',
   '<strong>Torre da geladeira</strong> com o fundo alinhado ao fundo da '
   'bancada: de frente ela avança e cria profundidade, de lado tudo termina no '
   'mesmo plano.',
   'Puxador em <strong>cava usinada</strong> no próprio material e iluminação '
   'em LED 3000 K sob o aéreo e dentro do nicho.'],
  22200),
 ('02', 'Painel amadeirado até o forro',
  'Parede inteira revestida, do rodapé ao forro, com porta integrada.',
  ['Painel sobre <strong>estrutura niveladora ancorada à parede</strong> — não é '
   'chapa colada em reboco, e por isso não estufa nem descola com o tempo.',
   '<strong>Porta integrada ao painel</strong>, com batente oculto e dobradiça '
   'invisível. De fora, a parede é contínua: a porta desaparece nela.',
   '<strong>Espelho lapidado com película de segurança</strong>, instalado entre '
   'os frisos, sem sobreposição.',
   '<strong>Frisos verticais usinados no próprio MDF</strong>, em três faixas, '
   'com o mesmo veio do painel.',
   'Reforço estrutural previsto para TV e rack: a carga não fica na chapa.'],
  15500),
 ('03', 'Rack suspenso',
  'Quatro frentes basculantes, solto do chão, com luz por baixo.',
  ['<strong>Quatro portas basculantes</strong> com articulador dimensionado pela '
   'massa real de cada frente — abrem leves e param onde você soltar.',
   '<strong>Tampo e base encorpados.</strong> Num móvel suspenso e longo, é a '
   'rigidez que impede a barriga no meio com o passar dos anos.',
   '<strong>Barra metálica contínua ancorada na alvenaria.</strong> O painel '
   'decorativo não recebe sozinho a carga do rack.',
   '<strong>LED 3000 K em perfil recuado com difusor leitoso</strong>: a luz '
   'aparece, a fita não.'],
  5200),
 ('04', 'Cristaleira até o forro',
  'Portas de vidro, prateleiras iluminadas e arremate no forro.',
  ['<strong>Duas portas de giro</strong> em perfil de alumínio preto e vidro '
   'temperado, com puxador vertical metálico.',
   '<strong>Prateleiras de vidro temperado lapidado</strong>, cada uma com a sua '
   'própria linha de luz — o que se vê é a peça exposta, não a fonte.',
   '<strong>Lateral esquerda com acabamento estendido até a parede</strong>, '
   'para absorver o desaprumo sem deixar fresta.',
   'Base niveladora e <strong>arremate superior recortado em obra</strong>, '
   'depois do nivelamento: o móvel encosta no forro sem vão.'],
  4900),
 ('05', 'Guarda-roupa de três portas de correr',
  'Três folhas deslizantes, com a central em espelho.',
  ['<strong>Três folhas</strong> em perfil de alumínio escuro, com roldana '
   'regulável e sistema antidescarrilamento.',
   '<strong>Porta central integral em espelho</strong> com película de '
   'segurança.',
   '<strong>Oito gavetas em corrediça oculta</strong>, prateleiras e maleiro '
   'superior com prateleira encorpada.',
   'Cabideiros ovais metálicos com suporte reforçado, com a profundidade útil '
   'preservada para os cabides.'],
  27500),
 ('06', 'Guarda-roupa em L com cabeceira',
  'Roupeiro e cabeceira no mesmo desenho, virando a esquina.',
  ['<strong>Roupeiro com quatro portas de giro</strong> do piso ao forro e '
   'cabideiro contínuo.',
   '<strong>Mesa de cabeceira com duas gavetas</strong>, alinhada ao último '
   'módulo do roupeiro — a esquina fecha sem sobra nem emenda aparente.',
   '<strong>Módulo vertical com prateleiras</strong>, resolvendo o encontro '
   'entre o roupeiro e a cama.',
   '<strong>Nicho iluminado sobre a cabeceira</strong>, em MDF encorpado, com '
   'passa-fio previsto.',
   '<strong>Armário aéreo com duas portas de giro</strong> sobre a cama.'],
  25900),
 ('07', 'Marcenaria sob a escada',
  'O vão da escada vira armário e vitrine.',
  ['<strong>Porta em vidro Reflecta temperado</strong> em perfil de alumínio '
   'preto, com dobradiça reforçada e puxador vertical.',
   '<strong>Nichos que acompanham a diagonal da escada</strong> e terminam '
   'zerados sobre a base: o desenho segue a escada em vez de brigar com ela.',
   '<strong>LED 3000 K inclusive nos nichos diagonais</strong>, em perfil '
   'recuado, sem ponto de luz aparente.',
   'Prateleiras encorpadas e rodapé recuado, para o vão respirar por baixo.'],
  8100),
]
assert sum(i[4] for i in ITENS) == INV

ESPEC = [
 ('Chapa', 'MDF BP <strong>18 mm</strong> na caixaria e nas frentes, '
  '<strong>25 mm</strong> nos nichos e nas prateleiras longas, e '
  '<strong>6 mm</strong> nos fundos encaixados.'),
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
 ('Tampo e rodabanca da cozinha', 'O projeto especifica <strong>pedra</strong> '
  'sobre toda a bancada. É fornecimento de marmoraria.'),
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
  <p class="lead" style="margin-top:4mm">Seu projeto chegou detalhado peça a
  peça — cada prancha com memorial de materiais, ferragens e acabamentos. Isso
  permitiu que este orçamento fosse feito <strong>sobre o projeto real</strong>,
  e não sobre uma estimativa: o que está descrito abaixo é o que será
  executado.</p>
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
  prateleiras, fundos e a caixa de cada gaveta. <strong>Nenhuma peça branca fica
  no projeto.</strong></p>
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
  <div class="box" style="margin-top:6mm"><div class="t">O que muda no dia a dia</div>
  <p><strong>Abrir a porta deixa de mostrar branco.</strong> O móvel fica inteiro
  na mesma cor, e o interior passa a fazer parte do desenho em vez de contrastar
  com ele. Onde há porta de vidro, gaveta aberta, nicho ou prateleira à vista —
  a cristaleira, o rack, o nicho da cabeceira, os nichos sob a escada — é o que
  separa um móvel bem-feito de um móvel bem-resolvido.</p></div>
  <div class="box"><div class="t">E envelhece melhor</div>
  <p>Marca de uso, poeira e risco de manuseio aparecem muito menos em superfície
  colorida do que em branca. Num armário que abre e fecha todo dia por dez anos,
  o interior na cor é também uma decisão de manutenção.</p></div>
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
