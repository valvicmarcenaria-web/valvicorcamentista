# -*- coding: utf-8 -*-
"""LUIZA E RAPHAEL — proposta comercial, duas linhas de ferragem.

Caderno de marcenaria 1/25 da decoradora Jéssica Sollero, 31/08/2026.
Motor: `corte-luiza-raphael.py` · dossiê: `2026-luiza-raphael.md`
Modelo de custo: `referencias/modelo-de-custo.md` via `motor_mc.py`.

[Jonathan 12/09] preços cravados: penteadeira completa R$ 8.500 · divisores de
acrílico R$ 1.200 · espaço gourmet R$ 30.000 na Hettich (teto). Sem comissão de
vendedor. Prazo 70 dias corridos.

⛔⛔ [Jonathan 12/09] SEM METRAGEM NENHUMA NA PROPOSTA. Regra da casa, não
   deste job — `referencias/proposta-comercial.md`. Nenhuma cota, m², contagem
   de porta, gaveta, prateleira, metro de fita ou de LED. Descreve-se o móvel e
   o benefício; material, ferragem, função, prazo, garantia e preço ficam.

⛔ [Jonathan 12/09] O ACRÉSCIMO DO CARTÃO SEGURA A MC EM REAIS, não em
   percentual — `motor_mc.preco_repasse()`. Segurar o percentual fazia a margem
   subir junto com o preço (+31% em 10×), o que marca up a taxa da operadora em
   vez de repassá-la. O certo é +8% em 6× e +15% em 10×.

Imagens: renders do próprio caderno, recortados em `img-luiza-raphael/`.
"""
import pathlib, subprocess
import motor_mc as M

P = pathlib.Path(__file__).resolve().parent
CLIENTE   = 'Luiza e Raphael'
DECORADORA= 'Jéssica Sollero · Design de Interiores'
DATA      = '12 de setembro de 2026'
VALIDADE  = '7 dias corridos'
PRAZO     = '70 dias corridos'
RT_ON, VEND_ON = True, False

# ── os cinco itens · (ambiente, nome, imagem, descritivo, preço T, preço H) ──
ITENS = [
 ('Quarto casal', 'Cabeceira estofada em tecido Bouclé', 'quarto',
  'Cabeceira em <b>tecido Bouclé</b> sobre estrutura de MDF, ocupando a parede '
  'inteira, com <b>cantos superiores arredondados</b> e acabamento em <b>meia '
  'esquadria</b>. Instalada acima do rodapé, sem apoio no piso.', 7100, 7100),
 ('Quarto casal', 'Penteadeira completa', 'penteadeira',
  'Bancada suspensa em <b>MDF Carvalho Arauco</b>, com quina arredondada e '
  '<b>tampo em vidro incolor temperado</b>. Gavetas rasas de organização e '
  '<b>gaveteiro auxiliar</b> ao lado. <b>Espelho prata colado</b> com canto em '
  'arco e <b>iluminação em LED contornando a borda</b>, acendendo por trás. '
  'Puxador em chanfro usinado; interno em MDF Branco TX.', 8500, 8500),
 ('Quarto casal', 'Divisórias internas em acrílico', None,
  'Divisores em <b>acrílico sob medida</b>, um por gaveta, com a malha de '
  'compartimentos do detalhe da prancha. Feitos para maquiagem e joias, '
  'removíveis para limpeza.', 1200, 1200),
 ('Espaço gourmet', 'Conjunto completo do espaço gourmet', 'gourmet',
  'A corrida inteira em <b>MDF Grafito Chess</b>, com as básculas em <b>MDF '
  'Jequitibá</b>: portas da lavanderia do piso ao teto em <b>dobradiça '
  'camarão</b> · armário superior e inferior da lavanderia · <b>vassoureiro do '
  'piso ao teto</b>, com vassoureiro deslizante, ganchos e prateleiras · '
  'armário superior do gourmet · <b>básculas em Jequitibá com pistão a gás</b>, '
  'uma em <b>vidro reflecta bronze com perfil e puxador sotille bronze</b> e '
  'outra com <b>escorredor metálico interno</b>, ambas com <b>LED 4000K</b> '
  'por baixo · armário inferior com básculas, gavetões, gavetas, nicho do forno '
  'e porta de temperos. Puxador em chanfro usinado; interno em MDF Branco TX.',
  26100, 30000),
 ('Sala da cobertura', 'Painel de TV e rack', 'sala',
  'Painel em <b>MDF Griss Chess</b> ocupando a parede inteira, construído em '
  'caixa para receber <b>LED 3000K nas bordas superior e inferior</b> sem perfil '
  'aparente, com acabamento em meia esquadria e <b>dobradiça de 90° para '
  'rotação da TV</b>. <b>Rack suspenso</b> com gavetões, <b>cantos '
  'arredondados</b> e puxador em chanfro usinado.', 9100, 10400),
]

VERSOES = [
 dict(cod='01', nome='Telescópica', mc=0.32, gar='2 anos',
      dobr='Hardt', corr='telescópica', pist='pistão a gás simples'),
 dict(cod='02', nome='Hettich',     mc=0.40, gar='10 anos',
      dobr='Hettich Sensys', corr='oculta Quadro (Hettich)',
      pist='pistão com amortecimento'),
]
TOT = [sum(i[4] for i in ITENS), sum(i[5] for i in ITENS)]
CD  = [22033.0, 24737.0]                     # de corte-luiza-raphael.py
assert TOT == [52000, 57200], TOT
MC  = [M.mc(TOT[i], CD[i], rt=RT_ON, vendedor=VEND_ON) for i in range(2)]

# ── escada: o acréscimo SEGURA a MC do pagamento à vista ─────────────────
ESCADA = [('Entrada 30% + saldo via transferência', 0),
          ('Entrada 30% + saldo em até 6× no cartão', 6),
          ('Entrada 30% + saldo em até 10× no cartão', 10)]
PAG = []
for rot, parc in ESCADA:
    vs = [TOT[i] if not parc else
          M.preco_repasse(CD[i], TOT[i], parc, rt=RT_ON, vendedor=VEND_ON)
          for i in range(2)]
    PAG.append((rot, parc, vs, [v/TOT[i]-1 for i, v in enumerate(vs)]))

def br(v): return f'{v:,.0f}'.replace(',', '.')
def img(n): return f'img-luiza-raphael/{n}.jpg'

CSS = (open(P/'css-proposta.css', encoding='utf-8').read()
       + open(P/'css-proposta-img.css', encoding='utf-8').read() + """
/* ── proposta Luiza e Raphael ─────────────────────────────────────────── */
.amb{margin-top:6mm;}
.amb .num{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;
  color:var(--gold-lt);font-weight:600;line-height:1;}
.amb .t{font-size:12.4pt;font-weight:700;letter-spacing:-.01em;margin-top:1mm;}
.amb .d{color:var(--soft);font-size:8.9pt;line-height:1.6;margin-top:2.2mm;}
.amb .d b{color:var(--ink);}
.par{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin:0 -19mm;}
.par .ph{height:82mm;}
.par .ph:first-child{border-radius:0 2px 2px 0;}
.solo{margin:0 -19mm;height:76mm;}
.lin2{display:grid;grid-template-columns:1fr 1fr;gap:7mm;margin-top:8mm;}
.lin2 > div{border:1.5px solid var(--line);border-radius:6px;padding:11mm 9mm;}
.lin2 > div.g{border-color:var(--gold);background:rgba(201,169,106,.07);}
.lin2 .cod{font-family:'Cormorant Garamond',Georgia,serif;font-size:28pt;
  color:var(--gold-lt);font-weight:600;line-height:1;}
.lin2 .nm{font-family:'Cormorant Garamond',Georgia,serif;font-size:25pt;
  font-weight:700;color:var(--ink);line-height:1.05;margin-top:1mm;}
.lin2 ul{margin:3.4mm 0 0;padding-left:4.4mm;font-size:9pt;color:var(--soft);
  line-height:1.78;}
.lin2 ul b{color:var(--ink);}
.lin2 .gar{margin-top:4mm;padding-top:3mm;border-top:1px solid var(--hair);
  font-size:8.4pt;color:var(--soft);}
.lin2 .gar b{font-size:11pt;color:var(--ink);}
.mesmo{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6mm;margin-top:7mm;
  padding-top:5mm;border-top:1px solid var(--line);}
.mesmo .k{font-size:6.6pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.mesmo .d{color:var(--soft);font-size:8.4pt;line-height:1.5;margin-top:1.4mm;}
.mesmo .d b{color:var(--ink);}
.invA{width:100%;border-collapse:collapse;font-size:8.8pt;margin-top:4mm;}
.invA th{font-size:6.5pt;letter-spacing:.15em;text-transform:uppercase;
  color:var(--mut);font-weight:700;border-bottom:1.5px solid var(--ink);
  padding:0 0 2.2mm;text-align:left;vertical-align:bottom;}
.invA th.r{text-align:right;width:27mm;padding-left:4mm;}
.invA th.r.alt{color:var(--gold);}
.invA td{padding:2.6mm 0;border-bottom:1px solid var(--hair);vertical-align:top;
  text-align:left;}
.invA td.a{width:31mm;color:var(--gold);font-size:7pt;letter-spacing:.13em;
  text-transform:uppercase;font-weight:700;padding-top:3.2mm;}
.invA td.i{font-weight:700;font-size:9.4pt;padding-right:5mm;}
.invA td.i small{display:block;font-weight:400;color:var(--soft);font-size:8pt;
  margin-top:.8mm;}
.invA td.r{text-align:right;font-weight:700;white-space:nowrap;padding-left:4mm;}
.invA td.r.alt{color:var(--gold);background:rgba(201,169,106,.07);}
.invA tr.tot td{border-bottom:0;border-top:2px solid var(--ink);padding-top:3.6mm;
  font-size:12pt;font-weight:700;}
.invA tr.tot td.r{font-family:'Cormorant Garamond',Georgia,serif;font-size:24pt;}
.payA{width:100%;border-collapse:collapse;font-size:9pt;margin-top:4mm;}
.payA th{font-size:6.5pt;letter-spacing:.15em;text-transform:uppercase;
  color:var(--mut);font-weight:700;border-bottom:1.5px solid var(--ink);
  padding:0 0 2mm;text-align:left;}
.payA th.r{text-align:right;}
.payA td{padding:2.4mm 0;border-bottom:1px solid var(--hair);}
.payA td.r{text-align:right;font-weight:700;white-space:nowrap;padding-left:5mm;}
.payA td.r.alt{color:var(--gold);}
.payA tr.best td{background:rgba(201,169,106,.12);border-bottom:0;}
.payA tr.best td:first-child{border-radius:3px 0 0 3px;font-weight:700;}
.payA tr.best td:last-child{border-radius:0 3px 3px 0;}
.cnd{display:grid;grid-template-columns:1fr 1fr;gap:4.5mm 8mm;margin-top:6mm;}
.cnd .k{font-size:6.6pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cnd .d{color:var(--soft);font-size:8.7pt;margin-top:1.2mm;line-height:1.52;}
.cnd .d b{color:var(--ink);}
.nota{margin-top:5mm;padding-left:4mm;border-left:2px solid var(--gold-lt);
  font-size:8.2pt;color:var(--soft);line-height:1.5;}
.nota b{color:var(--ink);}
""")

NP = 7
def foot(n):
    return (f'<div class="foot"><span>valvic marcenaria</span>'
            f'<span>{CLIENTE}</span><span>{n} / {NP}</span></div>')

def bloco(idx, it, n):
    amb, nome, im, desc, t, h = it
    return (f'<div class="amb"><div class="num serif">{n:02d}</div>'
            f'<div class="t">{nome}</div><div class="d">{desc}</div></div>')

# ── 1 · capa ─────────────────────────────────────────────────────────────
p1 = f"""<div class="page cover"><div class="cvfoto">
  <div class="top"><div class="cv-brand">valvic marcenaria</div></div>
  <div class="ph"><img src="{img('sala')}" alt=""></div>
  <div class="txt">
    <div class="eyebrow">Proposta comercial</div>
    <div class="cv-t serif">O quarto, o gourmet<br>e a sala da cobertura.</div>
    <div class="cv-meta">
      <div><div class="k">Cliente</div><div class="v">{CLIENTE}</div></div>
      <div><div class="k">Projeto</div><div class="v">{DECORADORA}</div></div>
      <div><div class="k">Data</div><div class="v">{DATA}</div></div>
    </div>
  </div>
</div></div>"""

# ── 2 · quarto casal ─────────────────────────────────────────────────────
p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Ambiente 01</div>
  <div class="h-sec serif">Quarto casal</div>
  <div class="rule"></div>
  <p class="lead">Leitura fiel do seu caderno de marcenaria — planta, elevações
  e cortes. Cada peça saiu da prancha cotada, não de estimativa por área.</p>
  <div class="par" style="margin-top:6mm;">
    <div class="ph"><img src="{img('quarto')}" alt=""></div>
    <div class="ph"><img src="{img('penteadeira')}" alt=""></div>
  </div>
  {bloco(0, ITENS[0], 1)}
  {bloco(1, ITENS[1], 2)}
  {bloco(2, ITENS[2], 3)}
  {foot(2)}
</div></div>"""

# ── 3 · espaço gourmet ──────────────────────────────────────────────────
p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Ambiente 02</div>
  <div class="h-sec serif">Espaço gourmet</div>
  <div class="rule"></div>
  <p class="lead">Uma corrida única, da lavanderia ao forno: planta, elevação
  externa, elevação interna e os três cortes do caderno. Lavanderia fechada por
  portas do piso ao teto, vassoureiro inteiro e a bancada completa.</p>
  <div class="ph solo" style="margin-top:6mm;"><img src="{img('gourmet')}" alt="">
    <div class="cap">Espaço gourmet · render do caderno de marcenaria.</div>
  </div>
  {bloco(3, ITENS[3], 4)}
  <div class="nota"><b>Bancada e rodabanca são de pedra</b> e não estão neste
  valor — a marcenaria entrega o corpo, o recorte da cuba e o encosto na pedra.
  Eletrodomésticos, cuba e torneira também são de fornecimento do cliente.</div>
  <div class="ph banda" style="margin-top:auto;height:52mm;"><img src="{img('lavanderia')}" alt="">
    <div class="cap">Lavanderia integrada · portas do piso ao teto.</div>
  </div>
  {foot(3)}
</div></div>"""

# ── 4 · sala da cobertura ───────────────────────────────────────────────
p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Ambiente 03</div>
  <div class="h-sec serif">Sala da cobertura</div>
  <div class="rule"></div>
  <p class="lead">Planta, elevações e corte da sala. O painel é construído em
  caixa para que a luz nasça da própria borda, sem perfil aparente.</p>
  <div class="ph solo" style="margin-top:6mm;"><img src="{img('sala')}" alt="">
    <div class="cap">Painel de TV e rack · render do caderno de marcenaria.</div>
  </div>
  {bloco(4, ITENS[4], 5)}
  <div class="nota"><b>O revestimento de madeira da parede</b> que aparece no
  render atrás do painel <b>não está descrito no caderno</b> e não está neste
  valor. Se ele fizer parte do escopo, orçamos à parte. A TV e o ponto elétrico
  são da obra.</div>
  <div class="ph banda" style="margin-top:auto;height:60mm;"><img src="{img('estar-jantar')}" alt="">
    <div class="cap">O painel visto do estar e jantar.</div>
  </div>
  {foot(4)}
</div></div>"""

# ── 5 · as duas linhas ──────────────────────────────────────────────────
def card(v, g=False):
    return f"""<div class="{'g' if g else ''}">
      <div class="cod serif">{v['cod']}</div>
      <div class="nm serif">Linha<br>{v['nome']}</div>
      <ul>
        <li>Dobradiça <b>{v['dobr']}</b> em todas as portas e básculas</li>
        <li>Corrediça <b>{v['corr']}</b> em todas as gavetas e gavetões</li>
        <li>Báscula com <b>{v['pist']}</b></li>
      </ul>
      <div class="gar">Garantia de <b>{v['gar']}</b> sobre estrutura e ferragens</div>
    </div>"""

p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">As duas linhas</div>
  <div class="h-sec serif">A mesma marcenaria.<br><em>A ferragem decide.</em></div>
  <div class="rule"></div>
  <p class="lead">O desenho, as medidas, as chapas, os espelhos, o vidro, o
  estofado e o LED são <b>idênticos</b> nas duas linhas. O que muda é a ferragem
  — e, com ela, o tempo de garantia.</p>

  <div class="lin2">{card(VERSOES[0])}{card(VERSOES[1], g=True)}</div>

  <div class="mesmo" style="margin-top:auto;">
    <div><div class="k">O que não muda</div><div class="d"><b>O desenho e as
      medidas.</b> Mesmos móveis, mesma modulação, mesma distribuição interna
      nos dois casos.</div></div>
    <div><div class="k">Também não muda</div><div class="d"><b>Chapa e
      acabamento.</b> Carvalho, Grafito Chess, Jequitibá e Griss Chess, interno
      em Branco TX, e o mesmo LED instalado.</div></div>
    <div><div class="k">Nem muda</div><div class="d"><b>Quem faz.</b> Equipe
      própria do corte à instalação, com a medida conferida no local antes do
      corte.</div></div>
  </div>

  <div class="nota" style="margin-top:8mm;margin-bottom:2mm;">Três itens <b>não levam ferragem
  nenhuma</b> — a cabeceira estofada, os divisores de acrílico e o painel da
  sala. Eles são o mesmo móvel nas duas linhas e por isso têm <b>o mesmo preço
  nas duas</b>, sem diferença de um real.</div>
  {foot(5)}
</div></div>"""

# ── 6 · investimento ────────────────────────────────────────────────────
linhas = ''
_amb = None
for amb, nome, im, desc, t, h in ITENS:
    a = amb if amb != _amb else ''
    _amb = amb
    mesmo = ' <small>mesmo preço nas duas linhas</small>' if t == h else ''
    linhas += (f'<tr><td class="a">{a}</td><td class="i">{nome}{mesmo}</td>'
               f'<td class="r">R$ {br(t)}</td>'
               f'<td class="r alt">R$ {br(h)}</td></tr>')

p6 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif">Cinco itens, duas linhas.</div>
  <div class="rule"></div>
  <table class="invA">
    <thead><tr><th>Ambiente</th><th>Item</th>
      <th class="r">Telescópica<br><span style="font-weight:400;text-transform:none;letter-spacing:0;">2 anos</span></th>
      <th class="r alt">Hettich<br><span style="font-weight:400;text-transform:none;letter-spacing:0;">10 anos</span></th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td></td><td>Total</td>
        <td class="r">R$ {br(TOT[0])}</td>
        <td class="r alt">R$ {br(TOT[1])}</td></tr>
    </tbody>
  </table>

  <div class="cnd">
    <div><div class="k">O que está incluído</div><div class="d">Projeto
      executivo de marcenaria, chapas, ferragens, <b>espelho, vidro temperado,
      estofamento e acrílico</b>, iluminação em LED com driver, transporte e
      <b>montagem por equipe própria</b>.</div></div>
    <div><div class="k">A diferença entre as linhas</div><div class="d">
      <b>R$ {br(TOT[1]-TOT[0])}</b> separam as duas, e <b>oito anos de
      garantia</b>. Num gourmet com dezenas de portas, gavetas e básculas, a
      ferragem é o que se aciona todos os dias.</div></div>
  </div>

  <div class="nota">Valores do anteprojeto, com as medidas conferidas no local
  antes do corte. Se alguma diferir do caderno, avisamos antes de produzir.</div>

  <div class="mesmo" style="margin-top:8mm;">
    <div><div class="k">Na borda</div><div class="d"><b>Fita de borda extra fina</b>,
      colada em máquina, e <b>meia esquadria</b> nos encontros aparentes:
      o canto fecha sem topo de chapa à vista.</div></div>
    <div><div class="k">Nos terceiros</div><div class="d"><b>Espelho, vidro
      temperado, estofamento e acrílico</b> entram coordenados pela Valvic e
      <b>entregues instalados</b> — não sobra ponta para você resolver.</div></div>
    <div><div class="k">Na luz</div><div class="d"><b>Fita de LED em perfil de
      alumínio</b> embutida na própria peça, com <b>driver dimensionado por
      circuito</b>: no espelho, sob as básculas e nas bordas do painel.</div></div>
  </div>

  {foot(6)}
</div></div>"""

# ── 7 · condições ───────────────────────────────────────────────────────
pay = ''
for rot, parc, vs, acr in PAG:
    cls = ' class="best"' if parc == 0 else ''
    ac = 'valor de tabela' if parc == 0 else f'+{acr[0]*100:.0f}%'
    pay += (f'<tr{cls}><td>{rot}</td><td class="r">{ac}</td>'
            f'<td class="r">R$ {br(vs[0])}</td>'
            f'<td class="r alt">R$ {br(vs[1])}</td></tr>')

p7 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="h-sec serif">Pagamento, prazo<br>e fronteiras.</div>
  <div class="rule"></div>

  <table class="payA">
    <thead><tr><th>Forma de pagamento</th><th class="r">Acréscimo</th>
      <th class="r">Telescópica</th><th class="r alt">Hettich</th></tr></thead>
    <tbody>{pay}</tbody>
  </table>
  <div class="nota" style="margin-top:3mm;">A entrada libera a compra de
  material e a entrada do projeto na fila de produção; o saldo é pago na
  entrega. <b>O acréscimo do cartão é a taxa da operadora, repassada sem
  margem</b> — a Valvic recebe exatamente o mesmo nas três condições. Por isso o
  pagamento via transferência é sempre o melhor valor para você.</div>

  <div class="cnd">
    <div><div class="k">Prazo de entrega</div><div class="d"><b>{PRAZO}</b>,
      contados da assinatura, do pagamento da entrada e da medição final no
      local.</div></div>
    <div><div class="k">Garantia</div><div class="d"><b>Hettich: 10 anos</b>
      sobre estrutura e ferragens · <b>Telescópica: 2 anos</b>.</div></div>
    <div><div class="k">Validade da proposta</div><div class="d"><b>{VALIDADE}</b>
      a partir desta data.</div></div>
    <div><div class="k">Escopo Valvic</div><div class="d">Do corte à instalação,
      com <b>equipe própria</b> e os terceiros de espelho, vidro, estofado e
      acrílico <b>coordenados e entregues instalados</b>.</div></div>
  </div>

  <div class="nota"><b>Não inclusos:</b> bancada e rodabanca de pedra do
  gourmet, revestimento de madeira da parede da sala, eletrodomésticos, cuba,
  torneira, TV, cama, cadeiras, cortinas e tapetes, pontos elétricos e
  hidráulicos, gesso e pintura.</div>

  <div class="ph banda" style="margin-top:auto;"><img src="{img('estar-jantar')}" alt="">
    <div class="cap">Sala da cobertura · render do caderno de marcenaria.</div>
  </div>
  <div class="eyebrow" style="margin-top:5mm;">{DECORADORA}</div>
  {foot(7)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>'
        f'{p1}{p2}{p3}{p4}{p5}{p6}{p7}</body></html>')

(P/'proposta-luiza-raphael.html').write_text(HTML, encoding='utf-8')
tmp = HTML.replace('src="img-luiza-raphael/', f'src="file://{P}/img-luiza-raphael/')
assert '{' not in ''.join(x.split('"')[1] for x in tmp.split('src=')[1:])
pathlib.Path('/tmp/in.html').write_text(tmp, encoding='utf-8')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-luiza-raphael.pdf')], check=True)

print(f'proposta-luiza-raphael.pdf · {NP} páginas')
print(f'  Telescópica R$ {br(TOT[0])}  MC {MC[0]*100:.1f}%')
print(f'  Hettich     R$ {br(TOT[1])}  MC {MC[1]*100:.1f}%')
for rot, parc, vs, acr in PAG:
    print(f'  {rot:<42}{"R$ "+br(vs[0]):>11}{"R$ "+br(vs[1]):>11}'
          f'   {"tabela" if parc==0 else f"+{acr[0]*100:.0f}% / +{acr[1]*100:.0f}%"}')
