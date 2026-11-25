# -*- coding: utf-8 -*-
import sys, os
_d=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _d)
sys.path.insert(0, os.path.join(_d, '..'))
import motor_mc as M
from estimativa import A, custo, MDF

def brl(v, n=0):
    return f'{v:,.{n}f}'.replace(',', '§').replace('.', ',').replace('§', '.')

MC = 0.40                      # alvo: topo da faixa ideal da casa (35-40%)
CEN = [('à vista · com RT e vendedor', dict()),
       ('à vista · com RT, sem vendedor', dict(vendedor=False)),
       ('à vista · sem RT e sem vendedor', dict(rt=False, vendedor=False))]

print('═'*104)
print('ESTIMATIVA POR AMBIENTE — RESIDÊNCIA HENRIQUE E KARELEN   ·   ferragem Blum   ·   MC alvo %.0f%%' % (MC*100))
print('⚠ ORDEM DE GRANDEZA: 10 dos 15 ambientes, com profundidades assumidas e MDF no piso do Fosco')
print('═'*104)
hdr = f'{"AMBIENTE":<26}{"chapas":>18}{"material":>11}{"ferragem":>11}{"terceiro":>11}{"CUSTO":>12}{"PREÇO":>13}'
print(hdr); print('─'*104)
tot_cd = 0.0; tot = {}
for k in sorted(A):
    c = custo(A[k]); tot[k] = c; tot_cd += c['cd']
    ch = ' '.join('%d×%dmm' % (n, e) for e, n in sorted(c['chapas'].items()))
    mat = c['ch'] + c['fita'] + c['cons'] + c['corte']
    print(f'{k:<26}{ch:>18}{brl(mat):>11}{brl(c["fer"]):>11}{brl(c["ter"]):>11}'
          f'{brl(c["cd"]):>12}{brl(M.preco(c["cd"], MC)):>13}')
print('─'*104)
pv = M.preco(tot_cd, MC)
print(f'{"TOTAL (10 ambientes)":<26}{"":>18}{"":>11}{"":>11}{"":>11}{brl(tot_cd):>12}{brl(pv):>13}')
print('═'*104)
print()
print('COMPOSIÇÃO DO CUSTO DIRETO')
agg = {k: sum(tot[a][k] for a in tot) for k in ('ch','fita','cons','corte','fer','ter')}
nome = dict(ch='chapa (MDF)', fita='fita + filetagem', cons='consumíveis 6%',
            corte='corte', fer='ferragem Blum + suportes', ter='terceirizados')
soma = sum(agg.values())
for k, v in sorted(agg.items(), key=lambda x: -x[1]):
    print(f'   {nome[k]:<30}{brl(v):>12}   {v/soma*100:>5.1f}%')
print(f'   {"embalagem 3%":<30}{brl(tot_cd-soma):>12}   {(tot_cd-soma)/tot_cd*100:>5.1f}%')
print(f'   {"CUSTO DIRETO":<30}{brl(tot_cd):>12}')
print()
print('PREÇO CONFORME A CONDIÇÃO (MC %.0f%%)' % (MC*100))
for nm, kw in CEN:
    b = M.base(**kw); p = M.preco(tot_cd, MC, **kw)
    print(f'   {nm:<34} base {b*100:5.2f}%   →  R$ {brl(p):>10}')
print()
print('SENSIBILIDADE — o que ainda pode mexer este número')
import estimativa as E
n_corr = sum(1 for a in A.values() for _ in [0]) # recontagem abaixo
nc = sum(getattr(a,'n_corr',0) for a in A.values())
nb = sum(getattr(a,'n_basc',0) for a in A.values())
nd = sum(getattr(a,'n_dobr',0) for a in A.values())
print(f'   contagem nestes 10 ambientes: {nc} corrediças · {nb} básculas · {nd} dobradiças')
d_corr = nc*(570-400)*1.03
print(f'   corrediça Movento a 570 em vez de 400 .... +{brl(d_corr):>9} de custo  →  preço +{brl(M.preco(tot_cd+d_corr,MC)-pv):>9}')
d_mdf = sum(tot[a]["ch"] for a in tot)*0.25*1.03
print(f'   MDF dos 12 padrões 25% acima do Fosco ..... +{brl(d_mdf):>9} de custo  →  preço +{brl(M.preco(tot_cd+d_mdf,MC)-pv):>9}')
falta = pv*(5/10)*0.55
print(f'   os 5 ambientes que faltam (estimativa) .... ~{brl(falta):>9} de PREÇO a somar')
print()
print()
print('PROJEÇÃO PARA OS 15 AMBIENTES (os 5 que faltam somam ~55% de um ambiente médio cada)')
for nm, kw in CEN:
    p10 = M.preco(tot_cd, MC, **kw)
    print(f'   {nm:<34} 10 amb. R$ {brl(p10):>9}   →   15 amb. ~R$ {brl(round(p10*1.55/1000)*1000):>9}')
