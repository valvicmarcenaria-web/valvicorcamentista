# -*- coding: utf-8 -*-
"""Phillip e Giselle · resumo: custo direto por ambiente nas linhas de ferragem.
Uso: LINHA=silver|padrao|gold python3 resumo.py"""
import importlib, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import motor as M, motor_mc as MC
AMBS = ['a01_quarto_casal', 'a02_closet_casal', 'a03_banho_casal', 'a04_rouparia',
        'a05_quarto_mateus', 'a06_quarto_ana', 'a07_banho_ana',
        'a08_closet_banho_mateus', 'a09_closet_ana', 'a10_circulacao']
FRETE = 3 * 200.0     # compra + 2 entregas
for a in AMBS: importlib.import_module(a)
R = M.calcula(FRETE)
if __name__ == '__main__':
    print(f'LINHA {M.LINHA} · custo direto {M.brl(R["CD"])} · {sum(R["chapas"].values())} chapas · {R["npecas"]} peças')
    for k, v in M.custo_por_ambiente(R).items(): print(f'  {k:24s} {M.brl(v)}')
    for rt in (False, True):
        print(' ', 'com RT' if rt else 'sem RT', ' · '.join(
            f'MC {mc*100:.0f}% {M.brl(MC.preco(R["CD"], mc, 0, rt, False))}' for mc in (.35, .38, .40)))
