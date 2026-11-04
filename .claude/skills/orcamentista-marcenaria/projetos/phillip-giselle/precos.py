# -*- coding: utf-8 -*-
"""Phillip e Giselle · CUSTO × VENDA por ambiente, nas três linhas.

Decisões [Jonathan, 04/11/2026]:
  · SEM RT e SEM VENDEDOR [Jonathan, 04/11/2026: "tire o percentual de vendedor"]
  · MC Telescópica 35% · Hettich 38% · Blum 42%
  · ⛔ SEM CARTÃO e SEM ESCALA DE DESCONTO: "não considere o cartão de crédito
    nesse cliente · parcelamentos igual à proposta do Michel e do Gustavo" →
    30% na assinatura, 20% em 30 dias, 20% em 60, 30% em 90, transferência.
    Um valor só por linha.
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
PAGTO = [('Entrada, na assinatura do contrato', 0.30),
         ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20),
         ('90 dias após a assinatura', 0.30)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9
ESCALA = [('Transferência, 30/20/20/30', 0.0, 0, 0.00)]   # sem cartão

def base(entrada, parc):
    """Cascata da casa com cartão só sobre o saldo, sem RT e sem vendedor."""
    cartao = MC.CARTAO_PP * parc * (1 - entrada)
    bruto = MC.NF + cartao + MC.ERRO + MC.SERRA + MC.MANUT
    liq = 1 - MC.NF - cartao
    vend = 0.0                                       # ⛔ sem vendedor
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
            print(f"   {lab}: {M.brl(p)} · MC {mc*100:.1f}% · base {base(0,0)*100:.2f}%")
        for lab, f in PAGTO:
            print(f"      {lab:36s} {f*100:3.0f}%  {M.brl(t['cheio']*f)}")
    for dsc, v, obs in AVULSO: print(f'\nAVULSO {M.brl(v)} (venda) · {obs}')
