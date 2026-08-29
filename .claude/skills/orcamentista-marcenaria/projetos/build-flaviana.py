# -*- coding: utf-8 -*-
"""FLAVIANA E IGOR — PROPOSTA ILUSTRADA, 4 páginas A4.

Valores lidos de `corte-flaviana.py`. [Jonathan 25/08] MC 40% COM RT.

  Investimento .................... R$ 21.000
  Armário aéreo ...................  R$ 7.100
  Armário inferior ................ R$ 10.200
  Porta de correr .................  R$ 3.700

IMAGENS [Jonathan 25/08] "me de as propostas usando as imagens dos projetos
para compor". Aqui os renders fotorrealistas SÃO do projeto: a prancha 02 do
caderno os identifica como "IMAGENS 3D RENDERIZADAS" do próprio executivo da
arq. Dani Rosaria — diferente do caderno da Giza, cuja capa declara os renders
"meramente ilustrativos" (lá eles ficaram de fora).

REGRAS DA CASA (`referencias/proposta-comercial.md`):
  1. ⛔ nenhuma cota de móvel no texto — a dimensão é dita em palavras
  2. ⛔ nenhuma explicação de formação de preço
  3. ✅ compor com as imagens do projeto

FERRAGEM [Jonathan 29/08]: "a gente não utiliza essas ferragens (telescópica),
substitui pela Hardt." As 4 gavetas saíram da telescópica e foram para a
Corrediça Oculta Hardt Invisível, junto com o gavetão. Com isso a garantia da
corrediça sobe de 2 para 5 anos (números do Jonathan, 07/08) — e a garantia
passou a ter bloco próprio na proposta, técnico e por componente, também a
pedido dele: "fale um pouco mais da garantia, sem ser muito conceitual".

RATEIO [Jonathan 29/08]: "a precificação do gabinete inferior ficou
superfaturada." Estava. O rateio era por ÁREA DE CHAPA, e o inferior é o item
de mais chapa e quase nenhum acessório. Agora é por CUSTO DIRETO de cada item.
O inferior caiu de R$ 10.200 para R$ 5.700 e o aéreo — que carrega espelho,
LED, drivers e 56 suportes — subiu para o que ele realmente é.

⛔ MONTAGEM fora do custo (equipe é salário fixo), dentro do escopo entregue.

⚠ PENDENTE — o PAGAMENTO não foi fechado. Está na linha de base da casa
   (entrada de 30%). O prazo o Jonathan fechou em 29/08: 60 dias corridos.
"""
import os, re, subprocess

CLIENTE  = 'Flaviana e Igor'
OBRA     = 'Marcenaria do banheiro da suíte'
ARQ      = 'arq. Dani Rosaria'
DATA     = '25 de agosto de 2026'
VALIDADE = '7 dias corridos'          # ⚠ pendente
PRAZO    = '60 dias corridos'         # [Jonathan 29/08]
ENT_PCT  = 30                         # ⚠ pendente

# ── valores lidos DO MOTOR, não transcritos à mão ─────────────────────────
_out = subprocess.run(['python3', 'projetos/corte-flaviana.py'],
                      capture_output=True, text=True, check=True).stdout
def _n(pat):
    m = re.search(pat, _out)
    assert m, f'não achei {pat!r} no relatório do motor'
    return int(m.group(1).replace('.', ''))
INV = _n(r'FECHADO · MC 40% COM RT \.+ R\$ ([\d.]+)')
def _v(nome):
    # a linha do motor agora traz DUAS colunas em R$ — custo direto e
    # investimento. O que vai para a proposta é a SEGUNDA.
    return _n(re.escape(nome) + r'\s+[\d.,]+ m²\s+R\$ [\d.]+\s+R\$ ([\d.]+)')

# ⛔ SEM UMA ÚNICA COTA. Onde a dimensão importa, ela é dita em palavras.
ITENS = [
 ('Armário aéreo sobre a bancada', _v('Armário aéreo sobre a bancada'),
  'Três folhas de abrir, cada uma em perfil de alumínio com espelho prata e '
  'película de segurança, sobre dobradiça com amortecimento; uma frente fixa '
  'fecha o vão. Corpo em amadeirado por fora e branco por dentro, com '
  'prateleiras fixas e passagem fitada para o secador. Dois rasgos verticais '
  'de LED entre as folhas, em perfil de alumínio — e é dentro deste armário '
  'que ficam alojados os drivers de toda a iluminação do banheiro.'),
 ('Armário inferior sob a bancada', _v('Armário inferior sob a bancada'),
  'Gabinete em amadeirado sob a bancada de mármore: nichos abertos na ponta, '
  'portas em dobradiça com amortecimento, um gavetão de roupa suja e uma '
  'coluna de quatro gavetas — todas as cinco em corrediça oculta Hardt '
  'Invisível com amortecimento, nenhuma telescópica. Puxador em cava usinada '
  'com pega, na própria frente.'),
 ('Porta de correr em MDF', _v('Porta de correr em MDF'),
  'Folha de passagem em MDF branco da linha ultra premium, montada em sistema '
  'deslizante Rometal RO82 Top, com amortecimento no fim de curso. Puxador '
  'tipo concha embutido.'),
]
assert sum(v for _, v, _d in ITENS) == INV, (ITENS, INV)

ENTRADA = round(INV*ENT_PCT/100/100)*100
SALDO   = INV - ENTRADA
assert ENTRADA + SALDO == INV

ESPEC = [
 ('Chapa',       'MDF amadeirado nas faces externas; todo o branco — '
                 'interior, fundos e a folha da porta de correr — na linha '
                 '<strong>ultra premium</strong>, chapa de área úmida, mais '
                 'resistente à umidade que o MDF branco comum'),
 ('Borda',       'Fita de borda extra fina de 0,4 mm, aplicada em coladeira '
                 'automática'),
 ('Portas',      'As folhas que abrem são <strong>portas de espelho com '
                 'estrutura de perfil de alumínio</strong>. O espelho é '
                 'pesado, e o perfil é o que sustenta a folha, mantém o '
                 'esquadro e evita que a frente empene ou descaia com o uso'),
 ('Espelho',     'Prata com película de segurança nas folhas de abrir; colado '
                 'na frente fixa'),
 ('Iluminação',  'Fita LED IP65 24 V · 3000 K em perfil de alumínio Usina '
                 'Design com difusor — drivers slim alojados no armário aéreo'),
 ('Ferragem',    'Dobradiça com amortecimento e corrediça oculta Hardt '
                 'Invisível P-10 com amortecimento nas cinco gavetas — a '
                 'corrediça não aparece na lateral e a gaveta sai inteira'),
 ('Puxador',     'Cava usinada com pega, na própria frente — sem peça aplicada'),
 ('Porta',       'Sistema deslizante Rometal RO82 Top com amortecimento, '
                 'trilho embutido no dente da parede e guia de piso'),
 ('Prateleiras', 'Fixas, sobre suportes'),
 ('Produção',    'Corte e usinagem em CNC própria, laminação de borda em '
                 'coladeira automática, instalação e montagem por equipe '
                 'própria da Valvic'),
]

FORA = [
 ('Bancada esculpida em mármore', 'é serviço de marmoraria.'),
 ('Dente na parede para embutir o trilho',
  'a prancha manda fazer o dente — é serviço da obra. O sistema deslizante é '
  'nosso.'),
 ('Box de vidro, nicho em porcelanato, porcelanato e paginação', ''),
 ('Forro de gesso e sanca', ''),
 ('Louças, metais, cubas e aquecimento', ''),
 ('Pontos elétricos e hidráulicos',
  'a iluminação embutida NA marcenaria é nossa; os pontos são da obra.'),
]

CSS = (open('projetos/css-proposta.css', encoding='utf-8').read()
       + open('projetos/css-proposta-img.css', encoding='utf-8').read() + """
.esp{padding:2.6mm 0;border-bottom:1px solid var(--hair);display:grid;
  grid-template-columns:26mm 1fr;gap:4mm;}
.esp:last-child{border-bottom:none;}
.esp .k{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--gold);font-weight:700;padding-top:.7mm;}
.esp .v{color:var(--soft);font-size:8.6pt;line-height:1.5;}
.cj{padding:3.6mm 0;border-bottom:1px solid var(--hair);}
.cj:last-child{border-bottom:none;}
.cj-h{display:flex;align-items:baseline;gap:4mm;}
.cj-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;
  color:var(--gold-lt);font-weight:600;line-height:1;min-width:8mm;}
.cj-t{font-size:10.8pt;font-weight:700;letter-spacing:-.005em;}
.cj-q{margin-left:auto;font-size:9.8pt;font-weight:700;white-space:nowrap;}
.cj-d{color:var(--soft);font-size:8.7pt;margin:1.4mm 0 0 12mm;line-height:1.55;}
""")


# ── GARANTIA ──────────────────────────────────────────────────────────────
# [Jonathan 29/08] "expresse um pouco melhor a garantia, fale um pouco mais.
# Sem ser muito conceitual, sendo um pouco mais técnico."
#   Números de `referencias/proposta-comercial.md` + a correção do Jonathan de
#   07/08 (telescópica 2 anos · oculta Hardt 5 anos). NADA aqui é inventado:
#   espelho e LED NÃO entram na cobertura da casa e por isso não aparecem
#   como cobertos — a linha diz o que a garantia é, e o que ela não é.
GARANTIA = dict(anos=10, unid='anos de garantia', nota=(
 'Garantia da <strong>Valvic</strong>, não do fabricante: quem projeta, corta, '
 'monta e atende é a mesma equipe, sem triangulação. Cobertura por componente, '
 'documentada e assinada na entrega.'), linhas=[
 ('Estrutura, corpo, fundo e prateleiras', '10 anos'),
 ('Dobradiça com amortecimento', '10 anos'),
 ('Corrediça oculta Hardt Invisível, em <strong>todas</strong> as gavetas — '
  'a Valvic não trabalha com telescópica', '5 anos'),
 ('Sistema deslizante da porta de correr', '10 anos'),
 ('Regulagem de porta e de gaveta', '2 anos'),
 ('Retorno do chamado', '24 horas'),
 ('Visita técnica, sem custo dentro do prazo', 'até 3 dias úteis'),
])

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
gar = ('<div class="gar"><div class="gar-h">'
       f'<div><div class="gar-n">{GARANTIA["anos"]}</div>'
       f'<div class="gar-u">{GARANTIA["unid"]}</div></div>'
       f'<div class="gar-x">{GARANTIA["nota"]}</div></div>'
       + ''.join(f'<div class="gar-l"><div class="k">{k}</div>'
                 f'<div class="v">{v}</div></div>'
                 for k, v in GARANTIA['linhas']) + '</div>')
linhas = ''.join(f'<tr><td class="l">{nome}</td><td class="hi">R$ {brl(v)}</td></tr>'
                 for nome, v, _d in ITENS)

p1 = f"""<div class="page cover"><div class="cvfoto">
  <div class="top"><div class="cv-brand">Valvic Marcenaria</div></div>
  <div class="ph"><img src="{{IMG}}/render-bancada.jpeg"
    style="object-position:20% center" alt=""></div>
  <div class="txt">
    <div class="eyebrow">Proposta de marcenaria planejada</div>
    <div class="rule"></div>
    <div class="cv-t">{CLIENTE}</div>
    <div class="cv-s">{OBRA} · sobre o projeto executivo de {ARQ}</div>
    <div class="cv-meta">
      <div><div class="k">Escopo</div><div class="v">3 itens de marcenaria</div></div>
      <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
      <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
    </div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Escopo</div>
  <div class="rule"></div>
  <h2 class="h-sec">Três itens de marcenaria.</h2>
  <p class="lead" style="margin-top:4mm">O levantamento foi feito sobre as oito
  pranchas executivas — planta, elevações internas e externas, vistas e
  detalhes. O que está descrito abaixo é o que será executado.</p>
  <div style="margin-top:6mm">{cj}</div>
  <div class="dupla sangra baixa" style="margin-top:8mm">
    <div class="ph ct"><img src="{{IMG}}/armarios-externa.jpeg" alt="">
      <div class="cap">Elevação · tudo fechado</div></div>
    <div class="ph ct"><img src="{{IMG}}/armarios-interna.jpeg" alt="">
      <div class="cap">Elevação · tudo aberto</div></div>
  </div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="rule"></div>
  <h2 class="h-sec">Como cada peça é feita.</h2>
  <div style="margin-top:5mm">{esp}</div>
  <div class="ph banda" style="margin-top:9mm;height:110mm">
    <img src="{{IMG}}/render-porta.jpeg" alt="">
    <div class="cap">Porta de correr · projeto executivo</div></div>
  {foot(3)}
</div></div>"""

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Investimento e garantia.</h2>
  <table class="inv" style="margin-top:6mm">
    <tr><th class="l">Item</th><th class="hi">Investimento</th></tr>
    {linhas}
    <tr class="tot"><td class="l">Total</td>
      <td class="hi">R$ {brl(INV)}</td></tr>
  </table>
  <div class="box"><div class="t">O que está dentro do valor</div>
  <p>Fornecimento de material, produção em CNC e coladeira automática próprias, espelho, iluminação em LED com perfil e drivers, ferragem, sistema deslizante, transporte, entrega na obra e <strong>instalação e montagem por equipe própria da Valvic</strong>.</p></div>
  <div class="eyebrow" style="margin-top:7mm">Garantia</div>
  <div class="rule"></div>
  {gar}
  {foot(4)}
</div></div>"""

p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h-sec">Prazo, pagamento e limites.</h2>
  <div class="two" style="margin-top:7mm">
    <div>
      <div class="term" style="margin-top:0"><div class="k">Pagamento</div>
        <div class="v">Entrada de {ENT_PCT}% + saldo na entrega</div>
        <div class="s">Entrada de <strong>R$ {brl(ENTRADA)}</strong> na
        assinatura e <strong>R$ {brl(SALDO)}</strong> na entrega.</div></div>
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
  <div class="ph banda" style="margin-top:auto;height:68mm">
    <img class="ct" src="{{IMG}}/armarios-perspectiva.jpeg" alt="">
    <div class="cap">O banheiro inteiro · projeto executivo</div></div>
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

OUT_H, OUT_P = 'projetos/proposta-flaviana.html', 'projetos/proposta-flaviana.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML.replace('{IMG}', 'img-flaviana'))
_abs = 'file://' + os.path.abspath('projetos/img-flaviana')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML.replace('{IMG}', _abs))
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}')
for nome, v, _d in ITENS:
    print(f'  {nome:<34} R$ {brl(v):>7}')
print(f'  {"TOTAL":<34} R$ {brl(INV):>7}')
print(f'  entrada {ENT_PCT}% R$ {brl(ENTRADA)} + R$ {brl(SALDO)} na entrega '
      f'· {PRAZO}   ⚠ pagamento ainda não fechado')
