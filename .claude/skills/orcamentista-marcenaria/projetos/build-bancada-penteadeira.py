# -*- coding: utf-8 -*-
"""BANCADA COM PENTEADEIRA — PROPOSTA, 3 páginas A4.

Valores de `corte-bancada-penteadeira.py`. Corte racionalizado, MC 40%, sem RT.

  Hettich · garantia 10 anos ....... R$ 16.700
  Blum    · garantia 20 anos ....... R$ 18.800
  Entrada de 40% + 60% na entrega · 90 dias corridos

DIREÇÃO DE REDAÇÃO [Jonathan 25/08]: "menos texto e menos conceitual, torne-a
um pouco mais técnica". Uma linha por móvel, com o que ele é e a ferragem que
leva. Sai a narrativa de benefício, fica a especificação.

FRASES QUE O JONATHAN CORTOU — não voltar:
  · "A tampa levanta e para onde você soltar"
  · "fundos encaixados em ranhura"
  · "driver bivolt acessível para manutenção"
  · "arremate superior recortado em obra após o nivelamento"

REGRAS DA CASA (`referencias/proposta-comercial.md`) — seguem valendo:
  1. ⛔ nenhuma cota de móvel no texto
  2. ⛔ nenhuma explicação de formação de preço. Ser técnico é falar de
        ferragem, fita e temperatura de LED — NÃO de chapa e aproveitamento.
"""
import subprocess

CLIENTE  = 'Proposta'
OBRA     = 'Bancada com penteadeira · quarto'
DATA     = '25 de agosto de 2026'
VALIDADE = '7 dias corridos'
PRAZO    = '90 dias corridos'
ENT_PCT  = 40

# ── valores · corte-bancada-penteadeira.py, MC 40% sem RT ─────────────────
LINHAS = [
 dict(k='HETTICH', nome='Hettich', gar=10, inv=16700, rec=False,
      esp='Dobradiça Novisys e corrediça oculta Quadro, as duas com '
          'amortecimento. Tampa da penteadeira em dois pistões a gás.'),
 dict(k='BLUM', nome='Blum', gar=20, inv=18800, rec=True,
      esp='Dobradiça Clip Top Blumotion e corrediça oculta Blum. Tampa da '
          'penteadeira em articulador HK-xs.'),
]
for L in LINHAS:
    L['ent'] = round(L['inv']*ENT_PCT/100/100)*100
    L['sal'] = L['inv'] - L['ent']
    assert L['ent'] + L['sal'] == L['inv']

# ⛔ SEM UMA ÚNICA COTA. Onde a dimensão é o argumento, ela é dita em palavras.
ITENS = [
 ('Bancada',
  'Tampo em MDF encorpado sobre lateral cega e montante intermediário, com '
  'borda laminada.'),
 ('Penteadeira basculante',
  'Trecho do tampo em tampa articulada sobre dobradiça, com espelho colado na '
  'face interna e caixa com divisórias.'),
 ('Gaveteiro',
  'Três gavetas em corrediça oculta com amortecimento. Puxador em perfil '
  'Arezzo.'),
 ('Nicho superior aberto',
  'Sem portas: fundo no mesmo amadeirado das frentes, todas as bordas '
  'laminadas, LED em perfil.'),
 ('Duas prateleiras',
  'Fixadas em sarrafo contínuo ancorado no painel, com LED em perfil sob '
  'cada uma.'),
 ('Torre de nichos',
  'Do piso ao forro, com LED em perfil por nicho.'),
 ('Painel de fundo',
  'Em toda a extensão, com passa-fio previsto.'),
]

ESPEC = [
 ('Chapa',       'MDF BP'),
 ('Borda',       'Fita ABS aplicada em coladeira automática'),
 ('Puxador',     'Perfil Arezzo'),
 ('Iluminação',  'Fita LED 24 V · 3000 K em perfil de alumínio com difusor'),
 ('Espelho',     'Prata lapidado, com película de segurança'),
 ('Fixação',     'Niveladores e ancoragem na alvenaria, rodapé recuado'),
 ('Produção',    'Corte e usinagem em CNC própria, laminação de borda em '
                 'coladeira automática, instalação e montagem por equipe '
                 'própria da Valvic'),
]

FORA = [
 ('Painel de cabeceira e mesa de cabeceira', 'já instalados.'),
 ('Pontos de elétrica', 'a iluminação embutida NA marcenaria é nossa; os pontos '
  'de energia são da obra.'),
 ('Alvenaria, gesso, revestimento e pintura', ''),
 ('Cadeira, objetos e decoração', ''),
]

CSS = open('projetos/css-proposta.css', encoding='utf-8').read() + """
.mv{padding:3.2mm 0;border-bottom:1px solid var(--hair);}
.mv:last-child{border-bottom:none;}
.mv .t{font-size:11pt;font-weight:700;letter-spacing:-.005em;}
.mv .d{color:var(--soft);font-size:9.4pt;margin-top:1.2mm;}
.esp{padding:2.8mm 0;border-bottom:1px solid var(--hair);display:grid;
  grid-template-columns:30mm 1fr;gap:5mm;}
.esp:last-child{border-bottom:none;}
.esp .k{font-size:7.2pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;padding-top:.6mm;}
.esp .v{color:var(--soft);font-size:9pt;}
.ln{display:grid;grid-template-columns:1fr 1fr;gap:7mm;margin-top:6mm;}
.ln .c{border:1px solid var(--line);border-radius:2px;padding:6mm 6.5mm;
  display:flex;flex-direction:column;position:relative;}
.ln .c.hi{background:var(--deep);border-color:var(--deep);color:#F6F1E7;}
.ln .anos{font-family:'Cormorant Garamond',Georgia,serif;font-size:44pt;
  line-height:.86;color:var(--gold);font-weight:500;}
.ln .c.hi .anos{color:var(--gold-lt);}
.ln .unid{font-size:7pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--mut);font-weight:700;margin-top:2mm;}
.ln .c.hi .unid{color:var(--gold-lt);}
.ln .marca{font-size:13pt;font-weight:700;margin-top:4mm;}
.ln .x{color:var(--soft);font-size:8.8pt;margin-top:2mm;}
.ln .c.hi .x{color:#CFC6B4;}
.ln .val{margin-top:auto;padding-top:5mm;border-top:1px solid var(--hair);}
.ln .c.hi .val{border-top-color:rgba(255,255,255,.16);}
.ln .val .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:24pt;
  font-weight:600;line-height:1.1;}
.ln .val .p{font-size:8.6pt;color:var(--soft);margin-top:1.6mm;}
.ln .c.hi .val .p{color:#CFC6B4;}
"""

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 3
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{OBRA}</span><span>{n} / {NP}</span></div>')

mv = ''.join(f'<div class="mv"><div class="t">{t}</div>'
             f'<div class="d">{d}</div></div>' for t, d in ITENS)
esp = ''.join(f'<div class="esp"><div class="k">{k}</div><div class="v">{v}</div>'
              f'</div>' for k, v in ESPEC)
fora = ''.join(f'<li><div class="k">{k}</div>'
               + (f'<div class="v">{v}</div>' if v else '') + '</li>'
               for k, v in FORA)
cards = ''.join(
    f'<div class="c{" hi" if L["rec"] else ""}">'
    f'<div class="anos">{L["gar"]}</div>'
    f'<div class="unid">anos de garantia</div>'
    f'<div class="marca">{L["nome"]}</div>'
    f'<div class="x">{L["esp"]}</div>'
    f'<div class="val"><div class="big">R$ {brl(L["inv"])}</div>'
    f'<div class="p">Entrada de {ENT_PCT}% — R$ {brl(L["ent"])}<br>'
    f'R$ {brl(L["sal"])} na entrega</div></div></div>' for L in LINHAS)

p1 = f"""<div class="page cover"><div class="pad">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div style="margin-top:auto">
    <div class="eyebrow">Proposta de marcenaria planejada</div>
    <div class="rule"></div>
    <div class="cv-t">Bancada com<br>penteadeira integrada</div>
    <div class="cv-s">Parede inteira, do rodapé ao forro<br>
    Sete conjuntos numa peça só</div>
  </div>
  <div class="cv-meta">
    <div><div class="k">Garantia Valvic</div><div class="v">10 ou 20 anos</div></div>
    <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Escopo</div>
  <div class="rule"></div>
  <h2 class="h-sec">O que está sendo proposto.</h2>
  <div style="margin-top:6mm">{mv}</div>
  <div class="eyebrow" style="margin-top:9mm">Especificação técnica</div>
  <div class="rule"></div>
  <div style="margin-top:4mm">{esp}</div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Duas linhas de ferragem.</h2>
  <p class="lead" style="margin-top:3.5mm">O móvel é o mesmo nas duas: mesmo
  desenho, mesmos materiais, mesmo acabamento. O que muda é a ferragem — e com
  ela a garantia.</p>
  <div class="ln">{cards}</div>
  <div class="two" style="margin-top:9mm">
    <div>
      <div class="term"><div class="k">Pagamento</div>
        <div class="v">Entrada de {ENT_PCT}% + {100-ENT_PCT}% na entrega</div></div>
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
      <div class="eyebrow">Não incluso</div>
      <div class="rule"></div>
      <ul>{fora}</ul>
    </div>
  </div>
  <div class="sig">
    <div class="ln" style="display:block">Valvic Marcenaria</div>
    <div class="ln" style="display:block">Cliente</div>
  </div>
  {foot(3)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>{p1}{p2}{p3}</body></html>')

OUT_H = 'projetos/proposta-bancada-penteadeira.html'
OUT_P = 'projetos/proposta-bancada-penteadeira.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML)
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}')
for L in LINHAS:
    print(f"  {L['nome']:<8} {L['gar']:>2} anos   R$ {brl(L['inv']):>7}   "
          f"entrada R$ {brl(L['ent'])} + R$ {brl(L['sal'])} na entrega")
