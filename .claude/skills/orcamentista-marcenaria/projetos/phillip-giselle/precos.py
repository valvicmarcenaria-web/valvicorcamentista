# -*- coding: utf-8 -*-
"""Phillip e Giselle · CUSTO × VENDA por ambiente, nas três linhas.

Decisões [Jonathan, 04/11/2026]:
  · SEM RT, COM VENDEDOR (10% do líquido)
  · MC Telescópica 35% · Hettich 38% · Blum 42%, cravada no PIOR degrau da
    escala de desconto padrão (30% + 10× no cartão), como no Rafael
  · Closet Mateus com o MESMO custo do Closet Ana ("considere custo igual")
  · Projeto executivo: custo de R$ 2.000, precificado como os ambientes
  · Serviço avulso do rodapé: R$ 1.900 de VENDA, fora da MC
"""
import sys, os, json, subprocess, math, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import motor_mc as MC
from resumo import AVULSO
import motor as M

LIN = {'telescopica': ('Telescópica', 0.35), 'hettich': ('Hettich', 0.38),
       'blum': ('Blum', 0.42)}
PROJETO = 2000.0
ESCALA = [('Entrada 30% + saldo em até 10× no cartão', 0.30, 10, 0.00),
          ('Entrada 50% + saldo em até 8× no cartão',  0.50,  8, 0.03),
          ('Entrada 70% + saldo em até 6× no cartão',  0.70,  6, 0.05),
          ('Entrada 70% + saldo por transferência',    0.70,  0, 0.07)]

def base(entrada, parc):
    """Cascata da casa com cartão só sobre o saldo, sem RT, com vendedor."""
    cartao = MC.CARTAO_PP * parc * (1 - entrada)
    bruto = MC.NF + cartao + MC.ERRO + MC.SERRA + MC.MANUT
    liq = 1 - MC.NF - cartao
    vend = MC.VENDEDOR * liq
    liq2 = liq - vend
    return 1 - bruto - vend - MC.PROD * liq2

def custos(linha):
    r = subprocess.run([sys.executable, 'resumo.py'], env=dict(os.environ, LINHA=linha),
                       capture_output=True, text=True, check=True,
                       cwd=pathlib.Path(__file__).parent)
    amb = json.loads(r.stdout)['amb']
    amb['Closet Mateus'] = amb['Closet Ana']          # ⭐ custo igual
    amb['Projeto executivo de marcenaria'] = PROJETO
    return amb

TAB = {}
for k, (nome, mc) in LIN.items():
    amb = custos(k); CD = sum(amb.values())
    cheio = max(CD / ((base(e, n) - mc) * (1 - d)) for _, e, n, d in ESCALA)
    cheio = math.ceil(cheio / 100) * 100
    pv = {a: round(cheio * c / CD, -1) for a, c in amb.items()}
    maior = max(pv, key=pv.get); pv[maior] += cheio - sum(pv.values())
    esc = [(lab, d, cheio * (1 - d), base(e, n) - CD / (cheio * (1 - d)))
           for lab, e, n, d in ESCALA]
    TAB[k] = dict(nome=nome, mc=mc, amb=amb, CD=CD, cheio=cheio, pv=pv, esc=esc)

if __name__ == '__main__':
    t0 = TAB['hettich']
    print(f"{'Ambiente':33s}" + ''.join(f"{'custo ' + t['nome'][:5]:>13s}{'venda':>13s}" for t in TAB.values()))
    for a in t0['amb']:
        print(f"{a:33s}" + ''.join(f"{M.brl(t['amb'][a]):>13s}{M.brl(t['pv'][a]):>13s}" for t in TAB.values()))
    print(f"{'TOTAL':33s}" + ''.join(f"{M.brl(t['CD']):>13s}{M.brl(t['cheio']):>13s}" for t in TAB.values()))
    for t in TAB.values():
        print(f"\n{t['nome']} · MC {t['mc']*100:.0f}%")
        for lab, d, p, mc in t['esc']:
            print(f"   {lab:44s} {'—' if not d else f'−{d*100:.0f}%':>4s} {M.brl(p):>14s}  MC {mc*100:5.1f}%")
    for dsc, v, obs in AVULSO: print(f'\nAVULSO {M.brl(v)} (venda) · {obs}')
