# -*- coding: utf-8 -*-
"""ELIUTON · BRISAS DA PAMPULHA — 2ª FASE · proposta comercial.

[Jonathan 07/09/2026] Preço cravado item a item, cenário 2 (Hardt · 5 anos),
com RT. Total R$ 141.800. Prazo 70 dias corridos. Condição especial de
pagamento — entrada de 30% na assinatura e saldo à vista na entrega, o mesmo
desenho com que a 1ª fase fechou em 20/08 (R$ 73.000).

⛔ O PAINEL DO ESPELHO ORGÂNICO SAIU DO ESCOPO. Ele aparece nos renders do
   quarto master — por isso a proposta DIZ que ele não está incluído. Render
   que mostra o que não vendemos vira expectativa de graça.

⚠ As portas do roupeiro da filha viraram DESLIZANTES em sistema Dominus. O
  render mostra portas de abrir; a proposta descreve o que foi contratado.

Motor: `corte-eliuton2.py` · dossiê: `2026-eliuton-2a-fase.md`.
Imagens: deck de renders da Valvic, recortadas em `img-eliuton2/`.
"""
import subprocess, pathlib

P = pathlib.Path(__file__).resolve().parent
CLIENTE   = 'Eliuton Ribeiro'
OBRA      = 'Residência Brisas da Pampulha'
ARQUITETA = 'Arq. Luciana Beatriz Simplício · Núcleo SC Arquitetura'
DATA      = '07 de setembro de 2026'
VALIDADE  = '7 dias corridos a partir desta data'
PRAZO     = '70 dias corridos'
GARANTIA  = '5 anos'

# ── preço cravado item a item · espelha PRECO_ITEM de corte-eliuton2.py ───
ITENS = [
 ('Quarto master', 'Painel de cabeceira com cabeceira estofada', 'master',
  'Painel amadeirado de <b>3,60 m</b> na parede da cabeceira mais <b>1,50 m</b> '
  'de retorno na lateral, com <b>topo curvo</b> contínuo e rasgo de LED sob o '
  'forro. <b>Cabeceira estofada de 2,00 × 1,00 m</b> integrada ao painel.', 11400),
 ('Quarto master', 'Criados-mudos (2)', None,
  'Dois criados suspensos de <b>85</b> e <b>80 cm</b>, três gavetas cada, com '
  '<b>cantos arredondados</b> e frente em cava usinada. Corrediça oculta com '
  'amortecimento.', 3700),
 ('Quarto master', 'Rack suspenso de TV', 'rack',
  'Rack de <b>1,80 m</b> suspenso, quatro portas, cantos curvos e passa-cabo. '
  'Sem apoio no piso — a limpeza passa por baixo.', 2400),
 ('Closet master', 'Closet aberto · dois lados de 2,94 m', 'closet',
  'Os <b>dois lados</b> do closet, sem portas: cabideiro duplo em quatro vãos, '
  '<b>seis prateleiras superiores</b> e <b>cinco sapateiras</b>, todas com '
  '<b>LED embutido</b>, e <b>dois gaveteiros de quatro gavetas</b>. É o móvel '
  'em que o interno é a fachada — não há porta para escondê-lo.', 24000),
 ('Quarto dos pais', 'Roupeiro em L com nicho de TV', 'pais',
  'Roupeiro em L de <b>3,42 m + 2,30 m</b> do piso ao forro, <b>dez portas</b>, '
  'dez prateleiras, quatro cabideiros e <b>gaveteiro de cinco gavetas</b>. '
  '<b>Nicho de TV amadeirado embutido no corpo</b>, com reforço, passa-cabo e '
  'LED. A TV e o ponto elétrico são da obra.', 26500),
 ('Quarto da filha', 'Roupeiro com portas deslizantes Dominus', 'filha',
  'Roupeiro de <b>3,81 m</b> com <b>quatro folhas deslizantes</b> em sistema '
  '<b>Dominus (Rometal)</b> — trilhos ocultos, duplo amortecimento e '
  'desempenadores anti-empeno em todas as folhas. Dez prateleiras, quatro '
  'cabideiros e gaveteiro de quatro gavetas.', 16500),
 ('Quarto da filha', 'Bancada / penteadeira', None,
  'Bancada de <b>1,66 m</b> sob a janela, tampo em <b>25 mm</b>, duas gavetas '
  'e <b>LED sob o tampo</b>.', 2700),
 ('Quarto de visitas', 'Roupeiro de correr · 2,45 m', 'visitas',
  'Roupeiro de <b>2,45 m</b> com <b>três folhas deslizantes</b> em sistema '
  'Dominus, portas lisas sem puxador aparente. Oito prateleiras, três '
  'cabideiros e gaveteiro de quatro gavetas.', 14200),
 ('Escritório', 'Roupeiro · 2,50 m', 'escritorio',
  'Roupeiro de <b>2,50 m</b> do piso ao forro, quatro portas, oito prateleiras, '
  'três cabideiros e gaveteiro de três gavetas.', 9400),
 ('Escritório', 'Painel de TV com nichos', 'escritorio2',
  'Painel amadeirado de <b>3,00 m</b> com <b>seis nichos suspensos</b> '
  'iluminados em LED.', 5600),
 ('Escritório', 'Bancada de trabalho curva', None,
  'Bancada de <b>2,00 m</b> com <b>ponta curva</b>, tampo em <b>25 mm</b> para '
  'não fletir no vão, montante lateral e duas gavetas.', 5500),
 ('Sala de TV', 'Painel de TV com ripado', 'sala',
  'Painel de <b>4,00 × 2,60 m</b> ocupando a parede inteira, <b>doze nichos '
  'iluminados</b>, rasgo de LED e <b>faixa ripada</b> de 55 réguas a passo '
  'constante. <b>A faixa de mármore atrás da TV é da marmoraria e não está '
  'nesta proposta</b> — executamos o recorte e o encosto da marcenaria nela.', 16000),
 ('Sala de TV', 'Bancada suspensa · 3,20 m', None,
  'Bancada suspensa de <b>3,20 m</b>, quatro portas com cava usinada, sem apoio '
  'no piso.', 3900),
]
TOTAL = sum(i[4] for i in ITENS)
assert TOTAL == 141800, TOTAL

ENTRADA = 42500                      # 30,0% de 141.800, redondo
SALDO   = TOTAL - ENTRADA
assert SALDO == 99300 and abs(ENTRADA/TOTAL - 0.30) < 0.002

UP_CLOSET = 10000                    # Gianduia só no closet aberto
UP_TUDO   = 31600                    # Gianduia em todos os internos

def brl(v): return f'{v:,.0f}'.replace(',', '.')
def img(n): return f'img-eliuton2/{n}.jpg'

CSS = (open(P/'css-proposta.css', encoding='utf-8').read()
       + open(P/'css-proposta-img.css', encoding='utf-8').read() + """
.itg{display:grid;grid-template-columns:1fr 1fr;gap:7mm 8mm;margin-top:5mm;}
.itg .ph{height:46mm;border-radius:2px;}
.itg .t{font-size:10.4pt;font-weight:700;margin-top:3.4mm;line-height:1.25;}
.itg .a{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.itg .d{color:var(--soft);font-size:8.3pt;margin-top:1.8mm;line-height:1.5;}
.itg .v{font-weight:700;font-size:9.6pt;margin-top:2.2mm;}
.itg .full{grid-column:1 / -1;}
.itg .full .ph{height:52mm;}
.ph img.baixo{object-position:center 66%;}
.itg.duo .ph{height:80mm;}
.banda2{margin:0 -19mm;height:68mm;}
.comp{display:grid;grid-template-columns:1fr 1fr;gap:5mm 9mm;margin-top:6mm;
  border-top:1px solid var(--line);padding-top:4.5mm;}
.comp .t{font-size:8.8pt;font-weight:700;line-height:1.25;}
.comp .a{font-size:6.4pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;margin-bottom:1mm;}
.comp .d{color:var(--soft);font-size:7.6pt;margin-top:1.4mm;line-height:1.45;}
.comp .v{font-weight:700;font-size:8.6pt;margin-top:1.8mm;}
.inv2{width:100%;border-collapse:collapse;font-size:8.8pt;margin-top:4mm;}
.inv2 th{font-size:6.6pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;border-bottom:1.5px solid var(--ink);
  padding:0 0 2mm;text-align:left;}
.inv2 th.r{text-align:right;}
.inv2 td{padding:1.9mm 0;border-bottom:1px solid var(--hair);vertical-align:top;}
.inv2 td.a{width:34mm;color:var(--gold);font-size:7.2pt;letter-spacing:.14em;
  text-transform:uppercase;font-weight:700;padding-top:2.5mm;}
.inv2 td.i{font-weight:600;}
.inv2 td.r{text-align:right;font-weight:700;white-space:nowrap;padding-left:6mm;}
.inv2 tr.tot td{border-bottom:0;border-top:2px solid var(--ink);
  padding-top:3.4mm;font-size:13pt;font-weight:700;}
.inv2 tr.tot td.r{font-family:'Cormorant Garamond',Georgia,serif;font-size:25pt;}
.up{margin-top:5mm;border:1px solid var(--gold-lt);border-radius:2px;
  background:var(--gold-pale);padding:5mm 6mm;}
.up .k{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.up .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:600;margin-top:1.5mm;line-height:1.1;}
.up .d{color:var(--soft);font-size:8.4pt;margin-top:2.4mm;}
.up .l{display:grid;grid-template-columns:1fr auto;gap:4mm;
  border-top:1px solid rgba(156,122,60,.24);padding:2.4mm 0 0;margin-top:3mm;}
.up .l b{font-weight:700;white-space:nowrap;}
.pf{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:6mm;}
.pf .c{border:1px solid var(--line);border-radius:2px;padding:5.5mm 6mm;}
.pf .c.hi{background:var(--deep);border-color:var(--deep);color:#F6F1E7;}
.pf .k{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.pf .c.hi .k{color:var(--gold-lt);}
.pf .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:29pt;
  line-height:1.05;font-weight:600;margin-top:2mm;}
.pf .s{color:var(--soft);font-size:8.4pt;margin-top:2.4mm;line-height:1.5;}
.pf .c.hi .s{color:#CFC6B4;}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:4mm 8mm;margin-top:4mm;}
.fr .k{font-size:6.9pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.fr .d{color:var(--soft);font-size:8.6pt;margin-top:1.2mm;line-height:1.52;}
.fr .d b{color:var(--ink);}
.nota{margin-top:5mm;padding-left:4mm;border-left:2px solid var(--gold-lt);
  font-size:8.2pt;color:var(--soft);line-height:1.5;}
.nota b{color:var(--ink);}
""")

def foot(n):
    return (f'<div class="foot"><span>valvic marcenaria</span>'
            f'<span>{CLIENTE} · 2ª fase</span><span>{n} / 6</span></div>')

def bloco(it, full=False, cls=''):
    amb, nome, im, desc, v = it
    ph = (f'<div class="ph"><img class="{cls}" src="{img(im)}" alt=""></div>') if im else ''
    return (f'<div class="{"full" if full else ""}">{ph}'
            f'<div class="a">{amb}</div><div class="t">{nome}</div>'
            f'<div class="d">{desc}</div>'
            f'<div class="v">R$ {brl(v)}</div></div>')

def compacto(*its):
    """Itens sem render próprio — entram como cartão de texto, mas ENTRAM.
    Nenhum item da tabela de preço pode ficar de fora do memorial."""
    cs = ''.join(f'<div><div class="a">{a}</div><div class="t">{n}</div>'
                 f'<div class="d">{d}</div><div class="v">R$ {brl(v)}</div></div>'
                 for a, n, _i, d, v in its)
    return f'<div class="comp">{cs}</div>'

# ── 1 · capa ──────────────────────────────────────────────────────────────
p1 = f"""<div class="page cover"><div class="cvfoto">
  <div class="top"><div class="cv-brand">valvic marcenaria</div></div>
  <div class="ph"><img src="{img('capa')}" alt=""></div>
  <div class="txt">
    <div class="eyebrow">Proposta comercial · 2ª fase</div>
    <div class="cv-t serif">Os quartos,<br>os closets<br>e a sala.</div>
    <div class="cv-meta">
      <div><div class="k">Cliente</div><div class="v">{CLIENTE}</div></div>
      <div><div class="k">Obra</div><div class="v">{OBRA}</div></div>
      <div><div class="k">Data</div><div class="v">{DATA}</div></div>
    </div>
  </div>
</div></div>"""

# ── 2 · os roupeiros, primeira parte ──────────────────────────────────────
p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O que entra</div>
  <div class="h-sec serif">Os roupeiros primeiro.</div>
  <div class="rule"></div>
  <p class="lead">São <b>cinco roupeiros e um closet</b> — o coração desta fase.
  Todos do piso ao forro, com cabideiro, prateleira, gaveteiro interno e a mesma
  ferragem <b>Hardt</b> da 1ª fase: corrediça oculta com amortecimento e
  dobradiça com regulagem em três dimensões.</p>
  <div class="itg duo">
    {bloco(ITENS[3])}
    {bloco(ITENS[4])}
  </div>
  <div class="nota">Os dois maiores móveis desta fase. Juntos somam
  <b>R$ {brl(ITENS[3][4] + ITENS[4][4])}</b> dos R$ {brl(TOTAL)} da proposta —
  e são os dois que o cliente abre todos os dias.</div>
  <div class="ph banda2" style="margin-top:auto;"><img src="{img('pais2')}" alt="">
    <div class="cap">Quarto dos pais · o nicho de TV sai do próprio corpo do
    roupeiro, com reforço e passa-cabo.</div>
  </div>
  {foot(2)}
</div></div>"""

# ── 3 · os roupeiros, segunda parte ───────────────────────────────────────
p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O que entra</div>
  <div class="h-sec serif">Três roupeiros,<br>três soluções de porta.</div>
  <div class="rule"></div>
  <p class="lead">Porta de abrir onde há espaço para ela girar; porta
  deslizante onde não há. É decisão de circulação, não de preço.</p>
  <div class="itg">
    {bloco(ITENS[5])}
    {bloco(ITENS[7])}
    {bloco(ITENS[8])}
    {bloco(ITENS[9])}
  </div>
  {compacto(ITENS[6], ITENS[10])}
  {foot(3)}
</div></div>"""

# ── 4 · os demais ambientes ───────────────────────────────────────────────
p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O que entra</div>
  <div class="h-sec serif">O quarto master<br>e a sala.</div>
  <div class="rule"></div>
  <div class="itg">
    {bloco(ITENS[0])}
    {bloco(ITENS[2])}
    {bloco(ITENS[11], full=True, cls='baixo')}
  </div>
  {compacto(ITENS[1], ITENS[12])}
  <div class="nota"><b>O painel do espelho orgânico não está nesta proposta.</b>
  Ele aparece nos renders do quarto master — o painel amadeirado de 1,20 m com o
  espelho de corte orgânico na parede lateral. Ficou fora do escopo a seu pedido.
  Se voltar, orçamos à parte.</div>
  {foot(4)}
</div></div>"""

# ── 5 · investimento ──────────────────────────────────────────────────────
linhas = ''
_amb = None
for amb, nome, im, desc, v in ITENS:
    a = amb if amb != _amb else ''
    _amb = amb
    linhas += (f'<tr><td class="a">{a}</td><td class="i">{nome}</td>'
               f'<td class="r">R$ {brl(v)}</td></tr>')

p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif">Item a item.</div>
  <div class="rule"></div>
  <table class="inv2">
    <thead><tr><th>Ambiente</th><th>Item</th><th class="r">Investimento</th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td></td><td>Total</td><td class="r">R$ {brl(TOTAL)}</td></tr>
    </tbody>
  </table>

  <div class="up">
    <div class="k">Opcional</div>
    <div class="t serif">Interno em MDF Gianduia Trama.</div>
    <div class="d">Hoje o interno de todos os roupeiros é <b>MDF branco</b> —
    caixaria, fundos, prateleiras e frentes de gaveteiro. O upgrade troca esse
    interno pelo <b>Gianduia Trama</b>, amadeirado com textura. <b>As portas não
    mudam.</b></div>
    <div class="l"><span><b>Só o closet master</b> — é o único móvel aberto:
      nele o interno é a fachada</span><b>+ R$ {brl(UP_CLOSET)}</b></div>
    <div class="l"><span><b>Todos os roupeiros e o closet</b></span>
      <b>+ R$ {brl(UP_TUDO)}</b></div>
    <div class="d" style="margin-top:3mm;">Valores sujeitos a confirmação da
    tabela do fornecedor da chapa Gianduia Trama.</div>
  </div>
  {foot(5)}
</div></div>"""

# ── 6 · prazo, pagamento, garantia e fronteiras ───────────────────────────
p6 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="h-sec serif">Prazo, pagamento<br>e fronteiras.</div>
  <div class="rule"></div>

  <div class="pf">
    <div class="c hi"><div class="k">Condição especial</div>
      <div class="v">R$ {brl(ENTRADA)}</div>
      <div class="s">Entrada na assinatura — 30% do total. Libera a compra de
      material e a entrada do projeto na fila de produção.</div></div>
    <div class="c"><div class="k">Saldo à vista, na entrega</div>
      <div class="v">R$ {brl(SALDO)}</div>
      <div class="s">Pago após a instalação concluída e conferida na obra.
      <b>Não há parcela durante a produção.</b></div></div>
  </div>

  <div class="fr" style="margin-top:7mm;">
    <div><div class="k">Prazo de entrega</div><div class="d"><b>{PRAZO}</b>,
      contados da assinatura, do pagamento da entrada e da medição final no
      local.</div></div>
    <div><div class="k">Garantia</div><div class="d"><b>{GARANTIA}</b> sobre
      estrutura e ferragens — a mesma linha Hardt com que a 1ª fase foi
      contratada.</div></div>
    <div><div class="k">Validade da proposta</div><div class="d">{VALIDADE}.</div></div>
    <div><div class="k">Escopo Valvic</div><div class="d">Projeto executivo,
      chapas, ferragens, iluminação em LED com driver, sistemas deslizantes,
      transporte e <b>montagem por equipe própria</b>.</div></div>
  </div>

  <div class="nota" style="margin-top:7mm;">
  <b>Não estão nesta proposta:</b> tudo o que foi contratado na 1ª fase (cozinha,
  área gourmet, área de serviço e banheiros); o <b>painel do espelho orgânico</b>
  do quarto master; a <b>faixa de mármore</b> atrás da TV da sala, que é
  marmoraria; camas, colchões, sofás, poltronas, mesas, cadeiras, tapetes e
  cortinas; TVs e eletrodomésticos; ar-condicionado, gesso, sanca, elétrica e
  pintura.</div>

  <div class="nota"><b>Medidas.</b> Os valores acima partem da planta cotada da
  arquiteta e do projeto de renders. <b>As medidas são conferidas no local antes
  do corte</b> — se alguma diferir do projeto, avisamos antes de produzir.</div>

  <div class="ph banda" style="margin-top:auto;"><img src="{img('closet2')}" alt="">
    <div class="cap">Closet master · render do projeto desta 2ª fase.</div>
  </div>
  <div class="eyebrow" style="margin-top:6mm;">{ARQUITETA}</div>
  {foot(6)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>'
        f'{p1}{p2}{p3}{p4}{p5}{p6}</body></html>')

(P/'proposta-eliuton2.html').write_text(HTML, encoding='utf-8')
tmp = HTML.replace('src="img-eliuton2/', f'src="file://{P}/img-eliuton2/')
assert '{' not in ''.join(s.split('"')[1] for s in tmp.split('src=')[1:])
pathlib.Path('/tmp/in.html').write_text(tmp, encoding='utf-8')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-eliuton2.pdf')], check=True)
print(f'proposta-eliuton2.pdf · total R$ {brl(TOTAL)} · '
      f'entrada {brl(ENTRADA)} + saldo {brl(SALDO)} · prazo {PRAZO}')
print(f'upgrade Gianduia: closet +{brl(UP_CLOSET)} · tudo +{brl(UP_TUDO)}')
