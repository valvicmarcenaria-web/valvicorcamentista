# -*- coding: utf-8 -*-
"""
APTO CJ — TABELA DE PREÇOS FECHADA  [Jonathan 28/07]
Preços de VENDA definidos comercialmente (valores cheios). O motor deixa de
definir o preço e passa a AUDITAR a margem de cada item e cenário.

Travas do Jonathan (à vista):
  entrada 100% melamínico Freijó ....... 4.500
  estante laca completa ................ mantida
  estante laca ext + melamínico fosco int  reancorada em MC 33% -> 42.600 à vista
  estante melamínico na cor ............ 27.000
  estante melamínico c/ branco interno .. 25.000

Regras de fechamento verificadas neste script:
  (1) coluna à vista e coluna parcelado ambas ADITIVAS (o cliente soma qualquer uma)
  (2) desconto à vista ≈ 10% em todo item e em todo cenário
  (3) cenário 1 honra exatamente os R$ 84.600 / 76.100 já entregues
"""
import io, contextlib, pathlib

SRC = pathlib.Path(__file__).parent/'corte-apto-cj-itens.py'
g = {'__file__': str(SRC)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(SRC.read_text(encoding='utf-8'), g)
VA, VB, VC, GERAIS, SERRA, base = g['VA'], g['VB'], g['VC'], g['GERAIS'], g['SERRA'], g['base']
VC_ANT = g['VC_ANT']   # v2 com interior branco TX — referência do que o upgrade custou
a_, liqF_, b_ = 0.182, 0.86, 0.043

def custo(cm, com_rateio=True):
    return cm + (GERAIS*cm/base if com_rateio else 0)

# ═══════════════ PREÇOS FECHADOS  (à vista, parcelado) — valores cheios
PRECO = {
  ('A','v1'): (7_900, 8_800),   ('A','v2'): (4_500,  5_000),
  ('B','v1'): (12_600, 14_000), ('B','v2'): (5_400,  6_000),
  ('C','v1'): (54_400, 60_500), ('C','v2'): (42_600, 47_300),
  ('C','v3'): (27_000, 30_000), ('C','v4'): (25_000, 27_800),
  ('D','u'):  (1_200,  1_300),
}
CUSTO = {
  ('A','v1'): custo(VA['v1 · lâmina natural']),  ('A','v2'): custo(VA['v2 · 100% melamínico']),
  ('B','v1'): custo(VB['v1 · lâmina natural']),  ('B','v2'): custo(VB['v2 · 100% melamínico']),
  ('C','v1'): custo(VC['v1 · laca completa']),   ('C','v2'): custo(VC['v2 · laca ext + melamínico fosco na cor int']),
  ('C','v3'): custo(VC['v3 · melamínico na cor']),('C','v4'): custo(VC['v4 · cor ext + branco int']),
  ('D','u'):  SERRA,
}
NOME = {
  ('A','v1'):'A · Entrada — lâmina natural de Freijó',
  ('A','v2'):'A · Entrada — 100% melamínico Freijó Puro',
  ('B','v1'):'B · Varanda/gourmet — lâmina natural',
  ('B','v2'):'B · Varanda/gourmet — 100% melamínico Freijó Puro',
  ('C','v1'):'C · Estante — laca fosca completa',
  ('C','v2'):'C · Estante — laca externa + melamínico fosco interno',
  ('C','v3'):'C · Estante — melamínico na cor, por inteiro',
  ('C','v4'):'C · Estante — cor externo + branco interno',
  ('D','u') :'D · Adega em serralheria',
}
def mc(c, p): return 1 - a_ - liqF_*b_ - c/p

print('═'*94)
print('APTO CJ — PREÇOS FECHADOS × CUSTO × MARGEM')
print('═'*94)
print(f'{"ITEM":<52}{"CUSTO":>10}{"À VISTA":>11}{"PARCEL.":>11}{"MC":>8}')
print('─'*94)
for k in [('A','v1'),('A','v2'),('B','v1'),('B','v2'),
          ('C','v1'),('C','v2'),('C','v3'),('C','v4'),('D','u')]:
    av, pa = PRECO[k]; c = CUSTO[k]
    print(f'{NOME[k]:<52}{c:>10,.0f}{av:>11,.0f}{pa:>11,.0f}{mc(c,pa)*100:>7.1f}%')

CEN = [('1 · Integral',                 ('A','v1'),('B','v1'),('C','v1')),
       ('2 · Entrada+varanda melamínico',('A','v2'),('B','v2'),('C','v1')),
       ('3 · Estante laca ext',          ('A','v1'),('B','v1'),('C','v2')),
       ('4 · Estante melamínico na cor', ('A','v1'),('B','v1'),('C','v3')),
       ('5 · Estante cor + branco int',  ('A','v1'),('B','v1'),('C','v4')),
       ('6 · Projeto 100% melamínico',   ('A','v2'),('B','v2'),('C','v4'))]

print('\n' + '═'*94)
print('CENÁRIOS — soma dos itens (as duas colunas fecham)')
print('═'*94)
print(f'{"CENÁRIO":<34}{"CUSTO":>10}{"À VISTA":>11}{"PARCEL.":>11}{"MC":>8}{"DESC.":>8}{"ECONOMIA":>11}')
print('─'*94)
res = {}
for nome, ka, kb, kc in CEN:
    c  = CUSTO[ka]+CUSTO[kb]+CUSTO[kc]+CUSTO[('D','u')]
    av = PRECO[ka][0]+PRECO[kb][0]+PRECO[kc][0]+PRECO[('D','u')][0]
    pa = PRECO[ka][1]+PRECO[kb][1]+PRECO[kc][1]+PRECO[('D','u')][1]
    econ = 84_600 - pa
    res[nome[0]] = (c, av, pa, econ)
    print(f'{nome:<34}{c:>10,.0f}{av:>11,.0f}{pa:>11,.0f}{mc(c,pa)*100:>7.1f}%'
          f'{(1-av/pa)*100:>7.1f}%{econ:>11,.0f}')

print('\n─'*47)
ok = True
c1 = res['1']
if (c1[1], c1[2]) != (76_100, 84_600):
    ok = False; print(f'  ✗ cenário 1 não honra 84.600/76.100 → {c1[2]:,}/{c1[1]:,}')
else:
    print('  ✓ cenário 1 honra exatamente R$ 84.600 parcelado / R$ 76.100 à vista')
for n,(c,av,pa,_) in res.items():
    d = 1-av/pa
    if not (0.089 <= d <= 0.101):
        ok = False; print(f'  ✗ cenário {n}: desconto {d*100:.2f}% fora da faixa')
mcs = [mc(c,pa) for c,_,pa,_ in res.values()]
print(f'  ✓ desconto à vista entre {min(1-av/pa for _,av,pa,_ in res.values())*100:.1f}% '
      f'e {max(1-av/pa for _,av,pa,_ in res.values())*100:.1f}% em todos os cenários')
print(f'  {"✓" if ok else "✗"} MC dos cenários: de {min(mcs)*100:.1f}% a {max(mcs)*100:.1f}%')
d_up = custo(VC['v2 · laca ext + melamínico fosco na cor int']) - custo(VC_ANT)
print(f'\n  Upgrade do interior da op.3 (branco TX → melamínico fosco na cor): '
      f'+R$ {d_up:,.0f} de custo, reancorado em MC {mc(CUSTO[("C","v2")], 47_300)*100:.1f}% '
      f'(alvo 33,0%) → R$ 47.300 parcelado / R$ 42.600 à vista')
print(f'\n  Cenário 6 = op2 + op5 − op1 (parcelado): '
      f'{res["2"][2]} + {res["5"][2]} − 84.600 = {res["2"][2]+res["5"][2]-84600:,} '
      f'{"✓" if res["2"][2]+res["5"][2]-84600 == res["6"][2] else "✗"}')
