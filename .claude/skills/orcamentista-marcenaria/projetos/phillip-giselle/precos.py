# -*- coding: utf-8 -*-
"""Phillip e Giselle · CUSTO × VENDA por ambiente e por ITEM, nas três linhas.

Decisões [Jonathan, 04/11/2026]:
  · SEM RT, SEM VENDEDOR, SEM CARTÃO: 30/20/20/30 por transferência, como nas
    propostas do Michell e do Gustavo · base 84,88%
  · ⛔⛔ O QUE NÃO MUDA DE FERRAGEM NÃO MUDA DE PREÇO: cada item = PARTE
    COMUM a MC 42% (igual nas três linhas) + FERRAGEM DE MOVIMENTO (corrediça
    e dobradiça da linha) na MC da linha: Telescópica 35 · Hettich 38 · Blum 45
  · Projeto executivo R$ 2.000 DILUÍDO nos closets e no painel da Suíte Ana
    (não aparece como item)
  · Preços FIXOS, iguais nas três linhas: Suíte Ana · móvel da janela 9.800 ·
    painel com 3 portas 15.600 · Circulação (bar + painel) 30.420
  · Closet Mateus com o MESMO custo do Closet Ana
  · Serviço avulso do rodapé: R$ 1.900 de VENDA, fora da MC
"""
import sys, os, json, subprocess, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import motor_mc as MC
from resumo import AVULSO
from motor import brl

AQUI = pathlib.Path(__file__).parent
LIN = {'telescopica': ('Telescópica', 0.35), 'hettich': ('Hettich', 0.38),
       'blum': ('Blum', 0.45)}
MC_COMUM = 0.42
PROJETO = 2000.0
B = MC.base(0, rt=False, vendedor=False)                      # 84,875%
PAGTO = [('Entrada, na assinatura do contrato', 0.30), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.30)]
ORDEM = ['Quarto casal', 'Closet casal', 'Suíte Ana', 'Closet Ana', 'Quarto Mateus',
         'Closet Mateus', 'Rouparia', 'Circulação']
FIXO_ITEM = {('Suíte Ana', 'Móvel da janela (nichos, banco e gavetões)'): 9800.0,
             ('Suíte Ana', 'Painel com 3 portas mimetizadas'): 15600.0}
FIXO_AMB = {'Circulação': 30420.0}
DILUI = lambda a, m: a.startswith('Closet') or m == 'Painel com 3 portas mimetizadas'

def linha(k):
    r = subprocess.run([sys.executable, 'resumo.py'], env=dict(os.environ, LINHA=k),
                       capture_output=True, text=True, check=True, cwd=AQUI)
    d = json.loads(r.stdout)
    cus = {tuple(x.split('||')): v for x, v in d['movel'].items()}
    mov = {tuple(x.split('||')): v for x, v in d['mov'].items()}
    # ⭐ Closet Mateus = Closet Ana, item por item
    for (a, m) in list(cus):
        if a == 'Closet Mateus':
            cus[(a, m)] = cus[('Closet Ana', m)]; mov[(a, m)] = mov[('Closet Ana', m)]
    return cus, mov

TAB = {}
for k, (nome, mc) in LIN.items():
    cus, mov = linha(k)
    com = {x: cus[x] - mov[x] for x in cus}
    # projeto diluído na parte comum (que não muda de linha → mesmo rateio)
    alvo = {x: com[x] for x in com if DILUI(*x)}
    for x, v in alvo.items():
        com[x] += PROJETO * v / sum(alvo.values()); cus[x] += PROJETO * v / sum(alvo.values())
    pv = {x: round(com[x] / (B - MC_COMUM), -1) + round(mov[x] / (B - mc), -1) for x in cus}
    for x, v in FIXO_ITEM.items(): pv[x] = v
    for a, v in FIXO_AMB.items():
        it = [x for x in pv if x[0] == a]; tot = sum(pv[x] for x in it)
        for x in it: pv[x] = round(v * pv[x] / tot, -1)
        pv[max(it, key=pv.get)] += v - sum(pv[x] for x in it)
    TAB[k] = dict(nome=nome, mc=mc, cus=cus, pv=pv, CD=sum(cus.values()),
                  venda=sum(pv.values()))

# ⛔ as travas
for x in TAB['hettich']['pv']:
    if not TAB['hettich']['cus'][x] - TAB['telescopica']['cus'][x]:   # sem ferragem de linha
        v = {TAB[k]['pv'][x] for k in TAB}
        assert len(v) == 1, ('⛔ item sem ferragem de linha com preços diferentes', x, v)
for a, v in FIXO_AMB.items():
    for k in TAB: assert sum(p for x, p in TAB[k]['pv'].items() if x[0] == a) == v
assert set(a for a, _ in TAB['hettich']['pv']) == set(ORDEM), set(a for a, _ in TAB['hettich']['pv'])

if __name__ == '__main__':
    T = TAB
    for a in ORDEM:
        it = [x for x in T['hettich']['pv'] if x[0] == a]
        print(f'\n{a.upper()}')
        for x in it:
            print(f"  {x[1]:48s}" + ''.join(f"{brl(T[k]['pv'][x]):>15s}" for k in T))
        print(f"  {'subtotal':48s}" + ''.join(f"{brl(sum(T[k]['pv'][y] for y in it)):>15s}" for k in T))
        print(f"  {'custo':48s}" + ''.join(f"{brl(sum(T[k]['cus'][y] for y in it)):>15s}" for k in T))
    print(f"\n{'TOTAL':50s}" + ''.join(f"{brl(T[k]['venda']):>15s}" for k in T))
    print(f"{'CUSTO DIRETO':50s}" + ''.join(f"{brl(T[k]['CD']):>15s}" for k in T))
    print(f"{'MC efetiva':50s}" + ''.join(f"{(B - T[k]['CD'] / T[k]['venda'])*100:14.1f}%" for k in T))
    for lab, f in PAGTO:
        print(f"{lab:50s}" + ''.join(f"{brl(T[k]['venda'] * f):>15s}" for k in T))
    for x, v in FIXO_ITEM.items():
        print('MC do fixo', x[1], ' / '.join(f"{(B - T[k]['cus'][x] / v)*100:.1f}%" for k in T))
    for d, v, obs in AVULSO: print(f'AVULSO {brl(v)} · {obs}')
