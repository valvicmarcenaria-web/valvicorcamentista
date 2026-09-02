# -*- coding: utf-8 -*-
"""LÍDIA DE SOUZA — PROPOSTA ILUSTRADA, 4 páginas A4.

Valores lidos de `corte-lidia.py`. [Jonathan 02/09] COM RT, MC POR ITEM:

  Investimento .................... R$ 30.300
  Cristaleira ..................... R$ 10.700   MC 30%
  Painel do jantar ................  R$ 8.100   MC 40%
  Painel e rack da TV ............. R$ 11.500   ◄ preço fechado (implica 49,1%)

O preço não sai de uma MC única do job: cada item é precificado pela SUA margem
sobre o SEU custo direto, e o total é a soma. O rack e o painel da TV são a
mesma parede e viraram UM item, e depois o Jonathan fechou o preço desse item
a dedo. A MC misturada do job dá 39,9% com RT.

FERRAGEM [Jonathan 02/09, 2ª rodada] "troque corrediças telescópicas para
oculta da Hettich, os pistões para articuladores (não precisa falar marca)".
A troca é de FERRAGEM, não de texto: a oculta custa o triplo da telescópica e o
articulador oito vezes o pistão. Com ela a garantia da corrediça sobe de 2 para
5 anos. ⛔ A MARCA DO ARTICULADOR NÃO VAI PARA A PROPOSTA, a pedido dele.

PAGAMENTO [Jonathan 02/09] duas formas, com o benefício do à vista em destaque:
  à vista  — entrada de 30% + saldo na entrega, nos valores da tabela
  cartão   — até 6× sem juros, com 10% a mais em cada valor

IMAGENS: os três renders do próprio caderno da decoradora Jéssica Sollero,
recortados das pranchas 4 e 7 e girados (o desenho está deitado na folha A4).

REGRAS DA CASA (`referencias/proposta-comercial.md`):
  1. ⛔ nenhuma cota de móvel no texto — a dimensão é dita em palavras
  2. ⛔ nenhuma explicação de formação de preço
  3. ✅ compor com as imagens do projeto

⛔ MONTAGEM fora do custo (equipe é salário fixo), dentro do escopo entregue.

Prazo e pagamento fechados pelo Jonathan: 60 dias corridos; à vista com entrada
de 30% e saldo na entrega, ou até 6× sem juros no cartão com 10% a mais.
"""
import os, re, subprocess

CLIENTE  = 'Lídia de Souza'
OBRA     = 'Sala de estar e jantar'
ARQ      = 'decoradora Jéssica Sollero'
VALIDADE = '7 dias corridos'
CARTAO_X = 6
ACRESC   = 0.10
PRAZO    = '60 dias corridos'         # [Jonathan 02/09]
ENT_PCT  = 30                         # ⚠ pendente
GAR_ANOS = 10

# ── valores lidos DO MOTOR, não transcritos à mão ─────────────────────────
_out = subprocess.run(['python3', 'projetos/corte-lidia.py'],
                      capture_output=True, text=True, check=True).stdout
def _n(pat):
    m = re.search(pat, _out)
    assert m, f'não achei {pat!r} no relatório do motor'
    return int(m.group(1).replace('.', ''))
INV = _n(r'INVESTIMENTO FECHADO \.+ R\$ ([\d.]+)')
def _v(nome):
    # a linha do motor traz m², custo direto, MC do item e investimento.
    # O que vai para a proposta é o ÚLTIMO campo.
    return _n(re.escape(nome) + r'\s+[\d.,]+ m²\s+R\$ [\d.]+\s+\d+%\s+R\$ ([\d.]+)')

# ⛔ SEM UMA ÚNICA COTA. Onde a dimensão importa, ela é dita em palavras.
ITENS = [
 ('Cristaleira', _v('Cristaleira'),
  'Embutida no painel do jantar, em duas colunas. A da direita fecha com duas '
  'folhas em vidro reflecta bronze, com perfil bronze e puxador sotille; a da '
  'esquerda fica aberta, com nicho alto e um gavetão em corrediça oculta '
  'embaixo. Dez prateleiras, '
  'todas com fita de LED 3000 K, e adega em tubinho preto no rodapé.'),
 ('Painel do jantar', _v('Painel do jantar'),
  'Tamponamento em MDF amadeirado de parede a parede, com o vão da cristaleira '
  'recortado nele. Bordas em meia esquadria e perfil de alumínio correndo na '
  'base.'),
 ('Painel e rack da TV', _v('Painel e rack da TV'),
  'A parede inteira, num item só. Tamponamento em MDF claro acima do rodapé, '
  'com recorte e passa-cabo previstos para a televisão, e sobre ele o rack '
  'suspenso em amadeirado, de frentes ripadas: uma báscula com frente vazada '
  'sobre articulador com amortecimento e dois gavetões em corrediça oculta. O '
  'puxador é o próprio ripado. Nichos abertos nas duas pontas e bordas '
  'arredondadas. Bordas dos dois em meia esquadria.'),
]
assert sum(v for _, v, _d in ITENS) == INV, (ITENS, INV)

ENTRADA = round(INV*ENT_PCT/100/100)*100
SALDO   = INV - ENTRADA
assert ENTRADA + SALDO == INV
# o cartão é DERIVADO item a item e tem de fechar com o total
def cartao(v):
    c = round(v*(1 + ACRESC))
    assert abs(c - v*(1 + ACRESC)) < 1, (v, c)
    return c
INV_CARTAO = sum(cartao(v) for _, v, _d in ITENS)
assert INV_CARTAO == cartao(INV), (INV_CARTAO, cartao(INV))
ECONOMIA = INV_CARTAO - INV

ESPEC = [
 ('Chapa',       'MDF melamínico ARAUCO nas três cores do projeto — Frapê na '
                 'cristaleira, Cumaru no painel do jantar e no rack, Atenna no '
                 'painel da TV. Interno dos gavetões em branco'),
 ('Borda',       'Fita de borda extra fina de 0,4 mm, aplicada em coladeira '
                 'automática'),
 ('Arremate',    'Meia esquadria em todo o perímetro aparente dos painéis e do '
                 'rack — o canto fecha em 45°, sem topo de chapa à vista'),
 ('Vidro',       'Reflecta bronze com perfil bronze e puxador sotille, com '
                 'furação de dobradiça de fábrica'),
 ('Ferragem',    'Dobradiça Hettich Sensys e corrediça oculta Hettich, as '
                 'duas com amortecimento — a corrediça não aparece na lateral '
                 'e a gaveta sai inteira. A báscula do rack sobe em '
                 'articulador com amortecimento: para onde você soltar'),
 ('Ripado',      'Ripas aplicadas com espaçamento regular; na báscula a frente '
                 'é vazada, e é o próprio ripado que serve de puxador'),
 ('Iluminação',  'Fita LED 24 V · 3000 K em perfil de alumínio, sob cada '
                 'prateleira da cristaleira e sob o móvel'),
 ('Fixação',     'Ancoragem na alvenaria; o rack é suspenso, sem apoio no piso'),
 ('Produção',    'Corte e usinagem em CNC própria, laminação de borda em '
                 'coladeira automática, instalação e montagem por equipe '
                 'própria da Valvic'),
]

# [Jonathan 02/09] com a oculta no lugar da telescópica, a garantia da
# corrediça sobe de 2 para 5 anos (números do Jonathan, 07/08).
GARANTIA = dict(anos=GAR_ANOS, nota=(
 'Garantia da <strong>Valvic</strong>, não do fabricante: quem projeta, corta, '
 'monta e atende é a mesma equipe, sem triangulação. Cobertura por componente, '
 'documentada e assinada na entrega.'), linhas=[
 ('Estrutura, corpo, fundos e prateleiras', f'{GAR_ANOS} anos'),
 ('Dobradiça Hettich Sensys com amortecimento', f'{GAR_ANOS} anos'),
 ('Articulador da báscula, com amortecimento', f'{GAR_ANOS} anos'),
 ('Corrediça oculta Hettich com amortecimento', '5 anos'),
 ('Regulagem de porta, de báscula e de gaveta', '2 anos'),
 ('Retorno do chamado', '24 horas'),
 ('Visita técnica, sem custo dentro do prazo', 'até 3 dias úteis'),
])

FORA = [
 ('Sofá, mesa, cadeiras, poltrona, tapete e pendente', ''),
 ('Televisão, ar-condicionado e cortina',
  'no painel da TV prevemos o recorte, o reforço e o passa-cabo.'),
 ('Gesso, sanca e rodapé de obra', ''),
 ('Preparo e sarrafeamento das paredes',
  'o painel é um tamponamento fino: ele acompanha a parede que encontra.'),
 ('Revestimento, pintura e pontos de elétrica',
  'a iluminação embutida NA marcenaria é nossa; os pontos são da obra.'),
]

CSS = (open('projetos/css-proposta.css', encoding='utf-8').read()
       + open('projetos/css-proposta-img.css', encoding='utf-8').read() + """
.esp{padding:2.3mm 0;border-bottom:1px solid var(--hair);display:grid;
  grid-template-columns:24mm 1fr;gap:4mm;}
.esp:last-child{border-bottom:none;}
.esp .k{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--gold);font-weight:700;padding-top:.7mm;}
.esp .v{color:var(--soft);font-size:8.4pt;line-height:1.46;}
.cj{padding:3.4mm 0;border-bottom:1px solid var(--hair);}
.cj:last-child{border-bottom:none;}
.cj-h{display:flex;align-items:baseline;gap:4mm;}
.cj-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;
  color:var(--gold-lt);font-weight:600;line-height:1;min-width:8mm;}
.cj-t{font-size:10.8pt;font-weight:700;letter-spacing:-.005em;}
.cj-q{margin-left:auto;font-size:9.8pt;font-weight:700;white-space:nowrap;}
.cj-d{color:var(--soft);font-size:8.6pt;margin:1.4mm 0 0 12mm;line-height:1.52;}
.pg{display:grid;grid-template-columns:1fr 1fr;gap:7mm;}
.pg .c{border:1px solid var(--line);border-radius:2px;padding:5.5mm 6mm;
  display:flex;flex-direction:column;}
.pg .c.hi{background:var(--deep);border-color:var(--deep);color:#F6F1E7;}
.pg .k{font-size:7pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.pg .c.hi .k{color:var(--gold-lt);}
.pg .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;
  font-weight:600;line-height:1.1;margin-top:2mm;}
.pg .x{color:var(--soft);font-size:8.6pt;margin-top:2.4mm;line-height:1.5;}
.pg .c.hi .x{color:#CFC6B4;}
.pg .v{margin-top:auto;padding-top:4mm;border-top:1px solid var(--hair);
  font-size:9pt;}
.pg .c.hi .v{border-top-color:rgba(255,255,255,.16);}
.eco{background:var(--gold-pale);border-left:2.5px solid var(--gold);
  padding:4mm 5.2mm;margin-top:6mm;display:flex;align-items:baseline;gap:5mm;}
.eco .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;
  font-weight:600;color:var(--gold);line-height:1;white-space:nowrap;}
.eco .t{font-size:9.2pt;color:var(--ink);}
.inv td:nth-child(2), .inv th:nth-child(2){padding-right:7mm;}
""")

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 5
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>{OBRA}</span><span>{n} / {NP}</span></div>')

cj = ''.join(f'<div class="cj"><div class="cj-h"><div class="cj-n">{i:02d}</div>'
             f'<div class="cj-t">{nome}</div>'
             f'<div class="cj-q">R$ {brl(v)}</div></div>'
             f'<div class="cj-d">{d}</div></div>'
             for i, (nome, v, d) in enumerate(ITENS, 1))
esp = ''.join(f'<div class="esp"><div class="k">{k}</div><div class="v">{v}</div>'
              f'</div>' for k, v in ESPEC)
fora = ''.join(f'<li><div class="k">{k}</div>'
               + (f'<div class="v">{v}</div>' if v else '') + '</li>'
               for k, v in FORA)
linhas = ''.join(f'<tr><td class="l">{nome}</td><td>R$ {brl(v)}</td>'
                 f'<td class="hi">R$ {brl(cartao(v))}</td></tr>'
                 for nome, v, _d in ITENS)
gar = ('<div class="gar"><div class="gar-h">'
       f'<div><div class="gar-n">{GARANTIA["anos"]}</div>'
       f'<div class="gar-u">anos de garantia</div></div>'
       f'<div class="gar-x">{GARANTIA["nota"]}</div></div>'
       + ''.join(f'<div class="gar-l"><div class="k">{k}</div>'
                 f'<div class="v">{v}</div></div>'
                 for k, v in GARANTIA['linhas']) + '</div>')

p1 = f"""<div class="page cover"><div class="cvfoto">
  <div class="top"><div class="cv-brand">Valvic Marcenaria</div></div>
  <div class="ph"><img src="{{IMG}}/sala-cristaleira.png"
    style="object-position:center 45%" alt=""></div>
  <div class="txt">
    <div class="eyebrow">Proposta de marcenaria planejada</div>
    <div class="rule"></div>
    <div class="cv-t">{CLIENTE}</div>
    <div class="cv-s">{OBRA} · sobre o caderno de marcenaria da {ARQ}</div>
    <div class="cv-meta">
      <div><div class="k">Escopo</div><div class="v">Duas paredes inteiras</div></div>
      <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
      <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
    </div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Escopo</div>
  <div class="rule"></div>
  <h2 class="h-sec">Duas paredes inteiras.</h2>
  <p class="lead" style="margin-top:4mm">O levantamento foi feito sobre as oito
  pranchas do caderno — planta, elevações externas e internas, cortes e o
  detalhe da báscula. A parede do jantar vai em dois itens, porque a cristaleira
  é um móvel e o painel é outro; a da TV vai num só, porque o rack nasce do
  painel. O que está descrito abaixo é o que será executado.</p>
  <div style="margin-top:5mm">{cj}</div>
  <div class="ph banda" style="margin-top:7mm;height:76mm">
    <img src="{{IMG}}/sala-jantar.png" style="object-position:center 55%" alt="">
    <div class="cap">Parede do jantar · caderno da decoradora</div></div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="rule"></div>
  <h2 class="h-sec">Como cada peça é feita.</h2>
  <div style="margin-top:5mm">{esp}</div>
  <div class="ph banda" style="margin-top:7mm;height:82mm">
    <img src="{{IMG}}/sala-tv.png" style="object-position:center 50%" alt="">
    <div class="cap">Parede da TV · caderno da decoradora</div></div>
  {foot(3)}
</div></div>"""

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Investimento e garantia.</h2>
  <table class="inv" style="margin-top:6mm">
    <tr><th class="l">Conjunto</th><th>À vista</th>
      <th class="hi">{CARTAO_X} × sem juros</th></tr>
    {linhas}
    <tr class="tot"><td class="l">Total</td><td>R$ {brl(INV)}</td>
      <td class="hi">R$ {brl(INV_CARTAO)}</td></tr>
  </table>
  <div class="box"><div class="t">O que está dentro do valor</div>
  <p>Fornecimento de material, produção em CNC e coladeira automática próprias,
  portas em vidro reflecta bronze, iluminação em LED com perfil, ferragem,
  perfil de alumínio, adega, transporte, entrega na obra e <strong>instalação e
  montagem por equipe própria da Valvic</strong>.</p></div>
  <div class="eyebrow" style="margin-top:7mm">Garantia</div>
  <div class="rule"></div>
  {gar}
  {foot(4)}
</div></div>"""

p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h-sec">Duas formas de pagar.</h2>
  <div class="pg" style="margin-top:6mm">
    <div class="c hi"><div class="k">À vista</div>
      <div class="t">R$ {brl(INV)}</div>
      <div class="x">Entrada de {ENT_PCT}% na assinatura e o saldo na entrega,
      por transferência. <strong>É o valor cheio da tabela, sem acréscimo
      nenhum.</strong></div>
      <div class="v">R$ {brl(ENTRADA)} na assinatura<br>
      R$ {brl(SALDO)} na entrega</div></div>
    <div class="c"><div class="k">No cartão</div>
      <div class="t">R$ {brl(INV_CARTAO)}</div>
      <div class="x">Em até <strong>{CARTAO_X} parcelas sem juros</strong>. Os
      valores da coluna da direita são {ACRESC*100:.0f}% acima dos de
      tabela.</div>
      <div class="v">{CARTAO_X} × sem juros</div></div>
  </div>
  <div class="eco"><div class="n">R$ {brl(ECONOMIA)}</div>
    <div class="t">é o que o pagamento <strong>à vista</strong> economiza —
    quase o valor de um dos três itens desta proposta.</div></div>
  <div class="two" style="margin-top:7mm">
    <div>
      <div class="term" style="margin-top:0"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da aprovação e da medição em obra.</div></div>
      <div class="term"><div class="k">Conferência de medidas</div>
        <div class="v">Visita técnica antes do corte</div>
        <div class="s">O caderno carimba "conferir medidas no local" em todas
        as folhas — é exatamente o que fazemos antes de cortar.</div></div>
      <div class="term"><div class="k">Validade da proposta</div>
        <div class="v">{VALIDADE}</div></div>
    </div>
    <div class="fora">
      <div class="eyebrow">Não incluso nesta proposta</div>
      <div class="rule"></div>
      <ul>{fora}</ul>
    </div>
  </div>
  <div class="ph banda" style="margin-top:auto;height:66mm">
    <img src="{{IMG}}/sala-cristaleira.png"
      style="object-position:center 30%" alt="">
    <div class="cap">A sala · caderno da decoradora</div></div>
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

OUT_H, OUT_P = 'projetos/proposta-lidia.html', 'projetos/proposta-lidia.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML.replace('{IMG}', 'img-lidia'))
_abs = 'file://' + os.path.abspath('projetos/img-lidia')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML.replace('{IMG}', _abs))
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}')
for nome, v, _d in ITENS:
    print(f'  {nome:<22} R$ {brl(v):>7}')
print(f'  {"TOTAL":<22} R$ {brl(INV):>7}')
print(f'  entrada {ENT_PCT}% R$ {brl(ENTRADA)} + R$ {brl(SALDO)} na entrega '
      f'· {PRAZO}')
print(f'  no cartão {CARTAO_X}× sem juros: R$ {brl(INV_CARTAO)}   '
      f'(à vista economiza R$ {brl(ECONOMIA)})')
