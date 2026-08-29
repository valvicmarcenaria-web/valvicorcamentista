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

GARANTIA — números do Jonathan [07/08]: telescópica 2 anos, oculta 5 anos.
Este job tem as duas. Vai UM número com UMA ressalva ("10 anos · 2 anos nas
corrediças"), que é o piso honesto — sem abrir por componente.

⛔ MONTAGEM fora do custo (equipe é salário fixo), dentro do escopo entregue.

⚠ PENDENTE DE DEFINIÇÃO — PRAZO e PAGAMENTO não foram fechados pelo Jonathan
   neste job. Estão na linha de base da casa. Trocar as três constantes abaixo.
"""
import os, re, subprocess

CLIENTE  = 'Flaviana e Igor'
OBRA     = 'Marcenaria do banheiro da suíte'
ARQ      = 'arq. Dani Rosaria'
DATA     = '25 de agosto de 2026'
VALIDADE = '7 dias corridos'          # ⚠ pendente
PRAZO    = '45 dias úteis'            # ⚠ pendente
ENT_PCT  = 30                         # ⚠ pendente
GARANTIA = '10 anos'

# ── valores lidos DO MOTOR, não transcritos à mão ─────────────────────────
_out = subprocess.run(['python3', 'projetos/corte-flaviana.py'],
                      capture_output=True, text=True, check=True).stdout
def _n(pat):
    m = re.search(pat, _out)
    assert m, f'não achei {pat!r} no relatório do motor'
    return int(m.group(1).replace('.', ''))
INV = _n(r'FECHADO · MC 40% COM RT \.+ R\$ ([\d.]+)')
def _v(nome):
    return _n(re.escape(nome) + r'\s+[\d.,]+ m²\s+R\$ ([\d.]+)')

# ⛔ SEM UMA ÚNICA COTA. Onde a dimensão importa, ela é dita em palavras.
ITENS = [
 ('Armário aéreo sobre a bancada', _v('Armário aéreo sobre a bancada'),
  'Três frentes com espelho prata colado, sobre dobradiça com amortecimento. '
  'Corpo em amadeirado por fora e branco por dentro, com prateleiras '
  'reguláveis e passagem fitada para o secador. Dois rasgos verticais de LED '
  'entre as frentes, em perfil de alumínio — e é dentro deste armário que '
  'ficam alojados os drivers de toda a iluminação do banheiro.'),
 ('Armário inferior sob a bancada', _v('Armário inferior sob a bancada'),
  'Gabinete em amadeirado sob a bancada de mármore: nichos abertos na ponta, '
  'portas em dobradiça com amortecimento, um gavetão em corrediça oculta e '
  'uma coluna de gavetas em corrediça telescópica com amortecimento. Puxador '
  'em cava usinada com pega, na própria frente.'),
 ('Porta de correr em MDF', _v('Porta de correr em MDF'),
  'Folha de passagem em MDF laminado, montada em kit de correr embutido — '
  'trilho, roldanas e guia de piso. Puxador tipo concha embutido na folha.'),
]
assert sum(v for _, v, _d in ITENS) == INV, (ITENS, INV)

ENTRADA = round(INV*ENT_PCT/100/100)*100
SALDO   = INV - ENTRADA
assert ENTRADA + SALDO == INV

ESPEC = [
 ('Chapa',       'MDF BP amadeirado nas faces externas e branco no interior'),
 ('Borda',       'Fita ABS aplicada em coladeira automática'),
 ('Espelho',     'Prata lapidado colado nas frentes do aéreo, com película de '
                 'segurança'),
 ('Iluminação',  'Fita LED IP65 24 V · 3000 K em perfil de alumínio Usina '
                 'Design com difusor — drivers slim alojados no armário aéreo'),
 ('Ferragem',    'Dobradiça com amortecimento; corrediça oculta no gavetão e '
                 'corrediças telescópicas com amortecimento nas gavetas'),
 ('Puxador',     'Cava usinada com pega, na própria frente — sem peça aplicada'),
 ('Porta',       'Kit de correr embutido, com trilho, roldanas e guia de piso'),
 ('Prateleiras', 'Reguláveis, sobre suportes'),
 ('Produção',    'Corte e usinagem em CNC própria, laminação de borda em '
                 'coladeira automática, instalação e montagem por equipe '
                 'própria da Valvic'),
]

FORA = [
 ('Bancada esculpida em mármore', 'é serviço de marmoraria.'),
 ('Dente na parede para embutir o trilho',
  'a prancha manda fazer o dente — é serviço da obra. O kit de correr é nosso.'),
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

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 4
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
  <h2 class="h-sec">Investimento e condições.</h2>
  <table class="inv" style="margin-top:6mm">
    <tr><th class="l">Item</th><th class="hi">Investimento</th></tr>
    {linhas}
    <tr class="tot"><td class="l">Total</td>
      <td class="hi">R$ {brl(INV)}</td></tr>
  </table>
  <div class="box"><div class="t">O que está dentro do valor</div>
  <p>Fornecimento de material, produção em CNC e coladeira automática próprias,
  espelho, iluminação em LED com perfil e drivers, ferragem, kit de correr,
  transporte, entrega na obra e <strong>instalação e montagem por equipe
  própria da Valvic</strong>.</p></div>
  <div class="two" style="margin-top:7mm">
    <div>
      <div class="term" style="margin-top:0"><div class="k">Pagamento</div>
        <div class="v">Entrada de {ENT_PCT}% + saldo na entrega</div>
        <div class="s">Entrada de <strong>R$ {brl(ENTRADA)}</strong> na
        assinatura e <strong>R$ {brl(SALDO)}</strong> na entrega.</div></div>
      <div class="term"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da aprovação e da medição em obra.</div></div>
      <div class="term"><div class="k">Garantia Valvic</div>
        <div class="v">{GARANTIA}</div>
        <div class="s">2 anos nas corrediças.</div></div>
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
  <div class="sig">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">{CLIENTE}</div>
  </div>
  {foot(4)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head>'
        f'<body>{p1}{p2}{p3}{p4}</body></html>')

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
      f'· {PRAZO}   ⚠ prazo e pagamento ainda não fechados')
