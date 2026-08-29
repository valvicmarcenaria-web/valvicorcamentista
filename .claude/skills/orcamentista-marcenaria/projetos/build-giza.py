# -*- coding: utf-8 -*-
"""GIZA E RENATO — PROPOSTA ILUSTRADA, 4 páginas A4.

Valores lidos de `corte-giza.py`. [Jonathan 25/08] MC 40% COM RT.

  Investimento .................... R$ 20.500
  Banheiro da suíte ............... R$ 12.600
  Banheiro social .................  R$ 7.900

IMAGENS [Jonathan 25/08] "me de as propostas usando as imagens dos projetos
para compor". São as vistas do PRÓPRIO projeto executivo da arq. Dani Rosaria,
extraídas do caderno — modelo 3D, elevações e vistas internas.
  ⛔ Os dois renders fotorrealistas do caderno FICARAM DE FORA: a capa do
     próprio caderno os declara "imagens meramente ilustrativas", ou seja,
     referência de terceiros. A casa não usa imagem de terceiro em proposta.

REGRAS DA CASA (`referencias/proposta-comercial.md`):
  1. ⛔ nenhuma cota de móvel no texto — a dimensão é dita em palavras
  2. ⛔ nenhuma explicação de formação de preço
  3. ✅ compor com as imagens do projeto

REGISTRO TÉCNICO, não narrativo [Jonathan 25/08]: o que a peça é e o que ela
leva. Sem narrativa de benefício.

⛔ MONTAGEM fora do custo (equipe é salário fixo), dentro do escopo entregue.

⚠ PENDENTE DE DEFINIÇÃO — PRAZO e PAGAMENTO não foram fechados pelo Jonathan
   neste job. Estão na linha de base da casa (`proposta-comercial.md`:
   entrada de 30%, entrega 45 a 60 dias úteis). Trocar as três constantes
   abaixo quando ele definir.
"""
import os, re, subprocess

CLIENTE  = 'Giza e Renato'
OBRA     = 'Marcenaria dos banheiros · suíte e social'
ARQ      = 'arq. Dani Rosaria'
DATA     = '25 de agosto de 2026'
VALIDADE = '7 dias corridos'          # ⚠ pendente
PRAZO    = '45 dias úteis'            # ⚠ pendente
ENT_PCT  = 30                         # ⚠ pendente

# ── valores lidos DO MOTOR, não transcritos à mão ─────────────────────────
_out = subprocess.run(['python3', 'projetos/corte-giza.py'],
                      capture_output=True, text=True, check=True).stdout
def _n(pat):
    m = re.search(pat, _out)
    assert m, f'não achei {pat!r} no relatório do motor'
    return int(m.group(1).replace('.', ''))
INV = _n(r'FECHADO · MC 40% COM RT \.+ R\$ ([\d.]+)')

def _v(nome):
    return _n(re.escape(nome) + r'\s+[\d.,]+ m²\s+R\$ ([\d.]+)')

SUITE  = _v('Banheiro suíte · armário aéreo')
SOCIAL = _v('Banheiro social · armário aéreo')
assert SUITE + SOCIAL == INV, (SUITE, SOCIAL, INV)

ENTRADA = round(INV*ENT_PCT/100/100)*100
SALDO   = INV - ENTRADA
assert ENTRADA + SALDO == INV

# ⛔ SEM UMA ÚNICA COTA. Onde a dimensão importa, ela é dita em palavras.
ITENS = [
 ('Banheiro da suíte', SUITE, 'suite-interna.jpeg', 'ct',
  'Vista interna · banheiro da suíte',
  'Armário de espelheira em três frentes, todas com espelho prata colado, '
  'sobre dobradiça com amortecimento. Interior dividido em três colunas, com '
  'prateleiras reguláveis sobre suportes niquelados e passagem fitada para o '
  'secador. LED COB em perfil de alumínio no arremate superior; o driver fica '
  'alojado dentro do próprio armário.'),
 ('Banheiro social', SOCIAL, 'social-interna.jpeg', 'ct',
  'Vista interna · banheiro social',
  'Mesma construção e mesmo acabamento da suíte, em duas colunas. Frentes '
  'espelhadas sobre dobradiça com amortecimento, prateleiras reguláveis e '
  'LED COB em perfil no arremate superior, com driver alojado no armário.'),
]

ESPEC = [
 ('Chapa',       'MDF BP branco, com o interior e o fundo no mesmo padrão'),
 ('Borda',       'Fita ABS aplicada em coladeira automática'),
 ('Espelho',     'Prata lapidado colado nas frentes, com película de segurança'),
 ('Iluminação',  'Fita LED COB 24 V · 3000 K em perfil de alumínio com difusor, '
                 'IRC acima de 90 — driver slim alojado no armário'),
 ('Ferragem',    'Dobradiça Häfele com amortecimento'),
 ('Puxador',     'Cava usinada na própria frente, em meia esquadria — sem peça '
                 'aplicada'),
 ('Prateleiras', 'Reguláveis, sobre suportes niquelados à vista'),
 ('Fixação',     'Ancoragem na alvenaria, com arremate superior no forro'),
 ('Produção',    'Corte e usinagem em CNC própria, laminação de borda em '
                 'coladeira automática, instalação e montagem por equipe '
                 'própria da Valvic'),
]

FORA = [
 ('Armários inferiores e espelhos existentes',
  'permanecem como estão; esta proposta é dos dois armários aéreos.'),
 ('Pontos de elétrica',
  'a iluminação embutida NA marcenaria é nossa; os pontos de energia são da obra.'),
 ('Forro de gesso, alvenaria, revestimento e pintura', ''),
 ('Louças, metais, cubas e acessórios', ''),
]

CSS = (open('projetos/css-proposta.css', encoding='utf-8').read()
       + open('projetos/css-proposta-img.css', encoding='utf-8').read() + """
.esp{padding:2.6mm 0;border-bottom:1px solid var(--hair);display:grid;
  grid-template-columns:26mm 1fr;gap:4mm;}
.esp:last-child{border-bottom:none;}
.esp .k{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--gold);font-weight:700;padding-top:.7mm;}
.esp .v{color:var(--soft);font-size:8.6pt;line-height:1.5;}
""")

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 4
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>{OBRA}</span><span>{n} / {NP}</span></div>')

dupla = ''.join(
    f'<div><div class="ph {cl}"><img src="{{IMG}}/{img}" alt=""></div>'
    f'<div class="t">{nome}</div><div class="d">{d}</div></div>'
    for nome, _v_, img, cl, cap, d in ITENS)

esp = ''.join(f'<div class="esp"><div class="k">{k}</div><div class="v">{v}</div>'
              f'</div>' for k, v in ESPEC)
fora = ''.join(f'<li><div class="k">{k}</div>'
               + (f'<div class="v">{v}</div>' if v else '') + '</li>'
               for k, v in FORA)
linhas = ''.join(f'<tr><td class="l">{nome}</td>'
                 f'<td class="hi">R$ {brl(v)}</td></tr>'
                 for nome, v, *_ in ITENS)

p1 = f"""<div class="page cover"><div class="cv2">
  <div class="txt">
    <div class="cv-brand">Valvic Marcenaria</div>
    <div style="margin-top:auto">
      <div class="eyebrow">Proposta de marcenaria planejada</div>
      <div class="rule"></div>
      <div class="cv-t">{CLIENTE}</div>
      <div class="cv-s">{OBRA}<br>
      Sobre o projeto executivo de {ARQ}</div>
    </div>
    <div class="cv-meta">
      <div><div class="k">Escopo</div><div class="v">2 armários de espelheira</div></div>
      <div><div class="k">Garantia Valvic</div><div class="v">10 anos</div></div>
      <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
      <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
    </div>
  </div>
  <div class="ph ct"><img src="{{IMG}}/suite-perspectiva.jpeg" alt="">
    <div class="cap">Banheiro da suíte · projeto executivo</div></div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Escopo</div>
  <div class="rule"></div>
  <h2 class="h-sec">Dois armários de espelheira.</h2>
  <p class="lead" style="margin-top:4mm">O levantamento foi feito sobre as
  cinco pranchas executivas — planta, elevações e vistas internas de cada
  banheiro. O que está descrito abaixo é o que será executado.</p>
  <div class="dupla" style="margin-top:6mm">{dupla}</div>
  <div class="eyebrow" style="margin-top:8mm">Especificação técnica</div>
  <div class="rule"></div>
  <div>{esp}</div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O projeto</div>
  <div class="rule"></div>
  <h2 class="h-sec">As vistas do executivo.</h2>
  <p class="lead" style="margin-top:4mm">Perspectiva e elevação do banheiro
  social, como saíram do projeto. O armário é o volume espelhado sobre a
  bancada — as frentes fecham no prumo, e o rasgo de luz corre no arremate
  superior.</p>
  <div class="dupla sangra" style="margin-top:8mm">
    <div class="ph ct"><img src="{{IMG}}/social-perspectiva.jpeg" alt="">
      <div class="cap">Perspectiva · banheiro social</div></div>
    <div class="ph ct"><img src="{{IMG}}/social-frontal.jpeg" alt="">
      <div class="cap">Elevação · banheiro social</div></div>
  </div>
  {foot(3)}
</div></div>"""

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Investimento e condições.</h2>
  <table class="inv" style="margin-top:6mm">
    <tr><th class="l">Ambiente</th><th class="hi">Investimento</th></tr>
    {linhas}
    <tr class="tot"><td class="l">Total</td>
      <td class="hi">R$ {brl(INV)}</td></tr>
  </table>
  <div class="box"><div class="t">O que está dentro do valor</div>
  <p>Fornecimento de material, produção em CNC e coladeira automática próprias,
  espelhos, iluminação em LED com perfil e driver, ferragem, transporte,
  entrega na obra e <strong>instalação e montagem por equipe própria da
  Valvic</strong>.</p></div>
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

OUT_H, OUT_P = 'projetos/proposta-giza.html', 'projetos/proposta-giza.pdf'
# o HTML do repositório aponta para a pasta ao lado; o do render usa file://
open(OUT_H, 'w', encoding='utf-8').write(HTML.replace('{IMG}', 'img-giza'))
_abs = 'file://' + os.path.abspath('projetos/img-giza')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML.replace('{IMG}', _abs))
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}')
print(f'  suíte R$ {brl(SUITE)} + social R$ {brl(SOCIAL)} = R$ {brl(INV)}')
print(f'  entrada {ENT_PCT}% R$ {brl(ENTRADA)} + R$ {brl(SALDO)} na entrega '
      f'· {PRAZO}   ⚠ prazo e pagamento ainda não fechados')
