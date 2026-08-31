# -*- coding: utf-8 -*-
"""CLÁUDIA — QUARTO DO MATHEUS E PAINEL LIVREIRO · PROPOSTA, 4 páginas A4.

REFAZIMENTO DE LAYOUT [Jonathan 31/08]. A proposta original é uma tabela de
três linhas com quatro renders embaixo (`proposta_claudia.pdf`). Os VALORES são
dela; o que muda é a forma e as condições:

  · duas formas de pagamento, lado a lado
      à vista  — entrada de 70% + restante na entrega, nos valores atuais
      cartão   — até 5× sem juros, com 10% a mais em cada valor
  · prazo de entrega ....... 60 dias corridos   (era 30 a 45 dias úteis)
  · garantia ............... 5 anos             (não constava)
  · validade ............... 5 dias úteis       (eram 2)

★ LEITURA DE ESCOPO — as opções 1 e 2 do quarto do Matheus são ALTERNATIVAS,
  não itens somáveis: a opção 1 tem armário aéreo com báscula mais prateleira;
  a 2 tem só duas prateleiras, sem armário. Os renders confirmam — o par de
  imagens do quarto é a mesma parede COM e SEM o aéreo. Por isso a proposta
  fecha por CONJUNTO (opção + painel), e não numa soma dos três. A tabela
  original deixava o cliente montar essa conta sozinho.

IMAGENS: as quatro do PDF original, recortadas dos dois pares. Trazem a marca
d'água "IMAGEM ILUSTRATIVA" do próprio fornecedor — fica como está, que é o
mais honesto: a imagem se identifica sozinha.

REGRAS DA CASA (`referencias/proposta-comercial.md`):
  1. ⛔ nenhuma cota de móvel no texto
  2. ⛔ nenhuma explicação de formação de preço
  3. ✅ compor com as imagens do projeto
"""
import os, subprocess

CLIENTE  = 'Cláudia'
OBRA     = 'Quarto do Matheus · painel livreiro'
DATA     = '31 de agosto de 2026'
PRAZO    = '60 dias corridos'      # [Jonathan 31/08]
VALIDADE = '5 dias úteis'          # [Jonathan 31/08]
GAR_ANOS = 5                       # [Jonathan 31/08]
ENT_PCT  = 70                      # à vista: entrada + restante na entrega
CARTAO_X = 5                       # parcelas sem juros
ACRESC   = 0.10                    # 10% a mais no cartão

# ── itens · valores da proposta original ──────────────────────────────────
# (chave, título, subtítulo, imagem, descrição, valor à vista)
ITENS = [
 ('op1', 'Quarto do Matheus', 'Opção 1 · com armário aéreo',
  'matheus-opcao1.png',
  'Armário aéreo em MDF melamínico fosco, na cor a definir. Báscula com '
  'articulador Blum HK-xs com amortecimento. Prateleira sobre suporte oculto e '
  'ganchos pintados no tom do MDF escolhido.', 3500),
 ('op2', 'Quarto do Matheus', 'Opção 2 · só as prateleiras',
  'matheus-opcao2.png',
  'Duas prateleiras sobre suporte oculto e ganchos pintados no tom do MDF '
  'escolhido. Mesma parede, sem o armário aéreo.', 1450),
 ('pnl', 'Painel livreiro', 'Item independente das opções acima',
  'livreiro-com.png',
  'Painel amadeirado fosco em MDF melamínico, com nicho para livreiro.', 4650),
]
VAL = {k: v for k, _t, _s, _i, _d, v in ITENS}

# o cartão é DERIVADO, não transcrito — e tem de fechar na parcela
def cartao(v):
    c = round(v*(1 + ACRESC))
    assert abs(c - v*1.10) < 1, (v, c)
    return c
for k, v in VAL.items():
    assert cartao(v) % CARTAO_X == 0, (k, v, cartao(v))   # parcela redonda

# ── conjuntos · opção + painel. As opções são ALTERNATIVAS entre si ───────
CONJ = [
 ('Opção 1 + painel livreiro', 'op1', 'Armário aéreo com báscula, prateleira, '
  'ganchos e o painel livreiro.'),
 ('Opção 2 + painel livreiro', 'op2', 'Duas prateleiras, ganchos e o painel '
  'livreiro, sem o armário aéreo.'),
]
def conjunto(k):
    a = VAL[k] + VAL['pnl']
    c = cartao(VAL[k]) + cartao(VAL['pnl'])
    assert c == cartao(a), (a, c, cartao(a))     # 10% no item = 10% no conjunto
    ent = round(a*ENT_PCT/100/100)*100
    return dict(vista=a, entrada=ent, saldo=a-ent, cartao=c, parcela=c//CARTAO_X)

GARANTIA = dict(anos=GAR_ANOS, nota=(
 'Garantia da <strong>Valvic</strong>, não do fabricante: quem projeta, corta, '
 'monta e atende é a mesma equipe, sem triangulação. Cobertura por componente, '
 'documentada e assinada na entrega.'), linhas=[
 ('Estrutura, corpo e prateleiras', f'{GAR_ANOS} anos'),
 ('Articulador da báscula, com amortecimento', f'{GAR_ANOS} anos'),
 ('Suporte oculto da prateleira', f'{GAR_ANOS} anos'),
 ('Regulagem da báscula', '2 anos'),
 ('Retorno do chamado', '24 horas'),
 ('Visita técnica, sem custo dentro do prazo', 'até 3 dias úteis'),
])

ESPEC = [
 ('Chapa',       'MDF melamínico fosco, cor a definir — exceto a linha '
                 'acetinada'),
 ('Borda',       'Fita de borda extra fina de 0,4 mm, aplicada em coladeira '
                 'automática'),
 ('Báscula',     'Articulador Blum HK-xs com amortecimento: a frente sobe e '
                 'para sozinha, sem bater ao fechar'),
 ('Prateleiras', 'Sobre suporte oculto — sem mão-francesa e sem ferragem à '
                 'vista por baixo'),
 ('Ganchos',     'Pintados no tom do MDF escolhido'),
 ('Fixação',     'Ancoragem na alvenaria'),
 ('Produção',    'Corte e usinagem em CNC própria, laminação de borda em '
                 'coladeira automática, instalação e montagem por equipe '
                 'própria da Valvic'),
]

FORA = [
 ('Cama, mesa, cadeira, criado-mudo e os demais móveis das imagens', ''),
 ('Pintura, papel de parede, cortina e persiana', ''),
 ('Pontos de elétrica', 'a marcenaria é nossa; os pontos de energia são da obra.'),
 ('Objetos, brinquedos e decoração', ''),
]

CSS = (open('projetos/css-proposta.css', encoding='utf-8').read()
       + open('projetos/css-proposta-img.css', encoding='utf-8').read() + """
.esp{padding:2.4mm 0;border-bottom:1px solid var(--hair);display:grid;
  grid-template-columns:26mm 1fr;gap:4mm;}
.esp:last-child{border-bottom:none;}
.esp .k{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--gold);font-weight:700;padding-top:.7mm;}
.esp .v{color:var(--soft);font-size:8.5pt;line-height:1.48;}
.op{display:grid;grid-template-columns:1fr 1fr;gap:7mm;}
.op .c{display:flex;flex-direction:column;}
.op .ph{height:66mm;background:#F2EEE6;}
.op .ph img{object-fit:cover;}
.op .t{font-size:11pt;font-weight:700;margin-top:3.6mm;}
.op .s{font-size:7pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;margin-top:1.4mm;}
.op .d{color:var(--soft);font-size:8.5pt;margin-top:2.4mm;line-height:1.52;}
.op .v{margin-top:auto;padding-top:3.4mm;font-family:'Cormorant Garamond',Georgia,serif;
  font-size:19pt;font-weight:600;}
.uni{display:grid;grid-template-columns:1fr 1.15fr;gap:7mm;align-items:center;
  border-top:1px solid var(--line);padding-top:6mm;margin-top:7mm;}
.uni .ph{height:64mm;background:#F2EEE6;}
.uni .ph img{object-fit:cover;}
.pg{display:grid;grid-template-columns:1fr 1fr;gap:7mm;}
.pg .c{border:1px solid var(--line);border-radius:2px;padding:5.5mm 6mm;
  display:flex;flex-direction:column;}
.pg .c.hi{background:var(--deep);border-color:var(--deep);color:#F6F1E7;}
.pg .k{font-size:7pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.pg .c.hi .k{color:var(--gold-lt);}
.pg .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt;
  font-weight:600;line-height:1.1;margin-top:2mm;}
.pg .x{color:var(--soft);font-size:8.6pt;margin-top:2.4mm;line-height:1.5;}
.pg .c.hi .x{color:#CFC6B4;}
/* a coluna do meio (à vista) encostava no bloco bege da coluna do cartão —
   no total, em serifa de 13,5pt, o número chegava a invadir o fundo. */
.inv td:nth-child(2), .inv th:nth-child(2){padding-right:7mm;}
""")

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 5
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>{OBRA}</span><span>{n} / {NP}</span></div>')

op = ''.join(
 f'<div class="c"><div class="ph"><img src="{{IMG}}/{img}" alt=""></div>'
 f'<div class="s">{sub}</div><div class="t">{tit}</div>'
 f'<div class="d">{d}</div>'
 f'<div class="v">R$ {brl(v)}</div></div>'
 for k, tit, sub, img, d, v in ITENS if k != 'pnl')
_p = [i for i in ITENS if i[0] == 'pnl'][0]
esp = ''.join(f'<div class="esp"><div class="k">{k}</div><div class="v">{v}</div>'
              f'</div>' for k, v in ESPEC)
fora = ''.join(f'<li><div class="k">{k}</div>'
               + (f'<div class="v">{v}</div>' if v else '') + '</li>'
               for k, v in FORA)
gar = ('<div class="gar"><div class="gar-h">'
       f'<div><div class="gar-n">{GARANTIA["anos"]}</div>'
       f'<div class="gar-u">anos de garantia</div></div>'
       f'<div class="gar-x">{GARANTIA["nota"]}</div></div>'
       + ''.join(f'<div class="gar-l"><div class="k">{k}</div>'
                 f'<div class="v">{v}</div></div>'
                 for k, v in GARANTIA['linhas']) + '</div>')

itens_tab = ''.join(
 f'<tr><td class="l">{tit}<br><span style="color:var(--mut);font-size:8pt">'
 f'{sub}</span></td><td>R$ {brl(v)}</td>'
 f'<td class="hi">R$ {brl(cartao(v))}</td></tr>'
 for k, tit, sub, img, d, v in ITENS)
conj_tab = ''.join(
 (lambda c: f'<tr class="tot"><td class="l">{nome}</td>'
            f'<td>R$ {brl(c["vista"])}</td>'
            f'<td class="hi">R$ {brl(c["cartao"])}</td></tr>')(conjunto(k))
 for nome, k, _d in CONJ)
conj_det = ''.join(
 (lambda c: f'<div class="term"><div class="k">{nome}</div>'
            f'<div class="v">À vista: entrada de R$ {brl(c["entrada"])} + '
            f'R$ {brl(c["saldo"])} na entrega</div>'
            f'<div class="s">No cartão: {CARTAO_X} × R$ {brl(c["parcela"])} '
            f'sem juros, total de R$ {brl(c["cartao"])}.</div></div>')(conjunto(k))
 for nome, k, _d in CONJ)

p1 = f"""<div class="page cover"><div class="cvfoto"
  style="grid-template-rows:auto 78mm 1fr">
  <div class="top"><div class="cv-brand">Valvic Marcenaria</div></div>
  <div class="ph"><img src="{{IMG}}/matheus-par.png"
    style="object-fit:cover" alt=""></div>
  <div class="txt">
    <div class="eyebrow">Proposta de marcenaria planejada</div>
    <div class="rule"></div>
    <div class="cv-t">{CLIENTE}</div>
    <div class="cv-s">{OBRA}<br>
    Duas opções para a parede do quarto, mais o painel livreiro</div>
    <div class="cv-meta" style="margin-top:auto">
      <div><div class="k">Garantia Valvic</div><div class="v">{GAR_ANOS} anos</div></div>
      <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
      <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
    </div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Escopo</div>
  <div class="rule"></div>
  <h2 class="h-sec">Duas opções para a mesma parede.</h2>
  <p class="lead" style="margin-top:3.5mm">As opções 1 e 2 são alternativas
  entre si — a mesma parede, com e sem o armário aéreo. O painel livreiro é
  independente das duas.</p>
  <div class="op" style="margin-top:6mm">{op}</div>
  <div class="uni">
    <div class="ph"><img src="{{IMG}}/{_p[3]}" alt=""></div>
    <div>
      <div class="s" style="font-size:7pt;letter-spacing:.18em;
        text-transform:uppercase;color:var(--gold);font-weight:700">{_p[2]}</div>
      <div style="font-size:11pt;font-weight:700;margin-top:1.4mm">{_p[1]}</div>
      <div style="color:var(--soft);font-size:8.5pt;margin-top:2.4mm">{_p[4]}</div>
      <div style="font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
        font-weight:600;margin-top:3.4mm">R$ {brl(_p[5])}</div>
    </div>
  </div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Duas formas de pagar.</h2>
  <div class="pg" style="margin-top:6mm">
    <div class="c"><div class="k">À vista</div>
      <div class="t">Entrada de {ENT_PCT}%</div>
      <div class="x">Entrada de {ENT_PCT}% na assinatura e o restante na
      entrega, por transferência. <strong>Nos valores da tabela.</strong></div></div>
    <div class="c hi"><div class="k">No cartão</div>
      <div class="t">{CARTAO_X} × sem juros</div>
      <div class="x">Até {CARTAO_X} parcelas sem juros no cartão. Os valores
      da coluna à direita são <strong>{ACRESC*100:.0f}% acima</strong> dos
      valores à vista.</div></div>
  </div>
  <table class="inv" style="margin-top:8mm">
    <tr><th class="l">Item</th><th>À vista</th>
      <th class="hi">{CARTAO_X} × sem juros</th></tr>
    {itens_tab}
  </table>
  <div class="eyebrow" style="margin-top:8mm">Fechando por conjunto</div>
  <div class="rule"></div>
  <p class="lead" style="font-size:9.3pt">Uma das opções do quarto mais o
  painel livreiro:</p>
  <table class="inv" style="margin-top:4mm">
    <tr><th class="l">Conjunto</th><th>À vista</th>
      <th class="hi">{CARTAO_X} × sem juros</th></tr>
    {conj_tab}
  </table>
  {foot(3)}
</div></div>"""

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Garantia</div>
  <div class="rule"></div>
  <h2 class="h-sec">O que a garantia cobre.</h2>
  <div style="margin-top:5mm">{gar}</div>
  <div class="eyebrow" style="margin-top:8mm">Especificação técnica</div>
  <div class="rule"></div>
  <div>{esp}</div>
  {foot(4)}
</div></div>"""

p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h-sec">Prazo, pagamento e limites.</h2>
  <div class="two" style="margin-top:7mm">
    <div>{conj_det}
      <div class="term"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da aprovação e da medição em obra.</div></div>
      <div class="term"><div class="k">Conferência de medidas</div>
        <div class="v">Visita técnica antes do corte</div>
        <div class="s">Nada vai para a CNC antes da nossa medição no local.</div></div>
      <div class="term"><div class="k">Validade da proposta</div>
        <div class="v">{VALIDADE}</div></div>
    </div>
    <div class="fora">
      <div class="eyebrow">Não incluso nesta proposta</div>
      <div class="rule"></div>
      <ul>{fora}</ul>
    </div>
  </div>
  <div class="ph banda" style="margin-top:auto;height:62mm">
    <img src="{{IMG}}/livreiro-com.png"
      style="object-fit:cover;object-position:center 38%" alt="">
    <div class="cap">Painel livreiro · referência de acabamento</div></div>
  <div class="sig" style="margin-top:9mm">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">{CLIENTE}</div>
  </div>
  {foot(5)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head>'
        f'<body>{p1}{p2}{p3}{p4}{p5}</body></html>')

OUT_H, OUT_P = 'projetos/proposta-claudia.html', 'projetos/proposta-claudia.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML.replace('{IMG}', 'img-claudia'))
_abs = 'file://' + os.path.abspath('projetos/img-claudia')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML.replace('{IMG}', _abs))
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}')
for k, tit, sub, img, d, v in ITENS:
    print(f'  {tit+" · "+sub:<48} R$ {brl(v):>6}   cartão R$ {brl(cartao(v)):>6}'
          f'   ({CARTAO_X}× R$ {brl(cartao(v)//CARTAO_X)})')
for nome, k, _d in CONJ:
    c = conjunto(k)
    print(f'  {nome:<48} R$ {brl(c["vista"]):>6}   cartão R$ {brl(c["cartao"]):>6}'
          f'   ({CARTAO_X}× R$ {brl(c["parcela"])})')
    print(f'  {"":48} à vista: {brl(c["entrada"])} + {brl(c["saldo"])} na entrega')
