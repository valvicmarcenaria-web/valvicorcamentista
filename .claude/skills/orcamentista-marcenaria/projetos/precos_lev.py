# -*- coding: utf-8 -*-
"""Preço por item nas três linhas, para projeto lançado no motor_lev.
uso: python3 precos_lev.py <pasta> [frete] [rt] [vendedor]

Regra da casa [Jonathan, 04/11/2026, Phillip e Giselle]:
  · item SEM ferragem de linha → parte comum a MC 42%, igual nas três linhas
  · item COM ferragem de linha → parte comum a 42 / 47 / 52 (Tel / Het / Blum)
  · corrediça e dobradiça → 35 / 43 / 55
  · sem cartão (30/20/20/30 por transferência)
"""
import sys, os, json, subprocess, pathlib
import motor_mc as MC
from motor_lev import brl

LIN = {'telescopica': ('Telescópica', 0.35, 0.42), 'hettich': ('Hettich', 0.43, 0.47),
       'blum': ('Blum', 0.55, 0.52)}
MC_COMUM = 0.42
# ⭐ Linhas apresentadas: LINHAS=hettich só a Hettich [Jonathan, 05/11/2026,
#   Tereza Sá e Júnia Portugal: "vamos trabalhar apenas com a linha Hettich"]
if os.environ.get('LINHAS'):
    LIN = {k: v for k, v in LIN.items() if k in os.environ['LINHAS'].split(',')}

def base(rt, vend):
    """Cascata sem cartão: NF, erro, serra, manutenção sobre o bruto; RT e
    vendedor sobre o líquido; comissões internas sobre o líquido 2."""
    bruto = MC.NF + MC.ERRO + MC.SERRA + MC.MANUT
    liq = 1 - MC.NF
    liq2 = liq - rt * liq - vend * liq
    return 1 - bruto - rt * liq - vend * liq - MC.PROD * liq2

def custos(pasta, linha, frete):
    code = ("import json, levantamento, motor_lev as M\n"
            f"R = M.calcula({frete})\n"
            "c, f = M.custo_por_movel(R)\n"
            "print(json.dumps({'c': {a + '||' + m: v for (a, m), v in c.items()},"
            " 'f': {a + '||' + m: v for (a, m), v in f.items()}, 'CD': R['CD'],"
            " 'chapas': R['chapas']}))")
    r = subprocess.run([sys.executable, '-c', code], cwd=pasta, capture_output=True,
                       text=True, check=True, env=dict(os.environ, LINHA=linha,
                       PYTHONPATH=str(pathlib.Path(__file__).parent)))
    d = json.loads(r.stdout)
    return ({tuple(k.split('||')): v for k, v in d['c'].items()},
            {tuple(k.split('||')): v for k, v in d['f'].items()}, d['chapas'])

def tabela(pasta, frete=400.0, rt=0.10, vend=0.03):
    B = base(rt, vend); T = {}
    for k, (nome, mcf, mci) in LIN.items():
        cus, mov, ch = custos(pasta, k, frete)
        pv = {x: round((cus[x] - mov[x]) / (B - (mci if mov[x] > 0 else MC_COMUM)), -1)
                 + round(mov[x] / (B - mcf), -1) for x in cus}
        # ⭐ PREÇO FIXO por ambiente, decisão do dono: <pasta>/fixos.json
        #   {"Ambiente": {"preco": 15600, "item": "nome do item único"}}
        fx = pathlib.Path(pasta) / 'fixos.json'
        for a, d in (json.loads(fx.read_text(encoding='utf-8')).items() if fx.exists() else []):
            it = [x for x in pv if x[0] == a]
            c, f = sum(cus[x] for x in it), sum(mov[x] for x in it)
            for x in it: del pv[x], cus[x], mov[x]
            pv[(a, d['item'])], cus[(a, d['item'])], mov[(a, d['item'])] = d['preco'], c, f
        T[k] = dict(nome=nome, cus=cus, mov=mov, pv=pv, CD=sum(cus.values()),
                    venda=sum(pv.values()), chapas=ch)
    return B, T

if __name__ == '__main__':
    pasta = pathlib.Path(sys.argv[1]).resolve()
    frete = float(sys.argv[2]) if len(sys.argv) > 2 else 400.0
    rt = float(sys.argv[3]) if len(sys.argv) > 3 else 0.10
    vend = float(sys.argv[4]) if len(sys.argv) > 4 else 0.03
    B, T = tabela(pasta, frete, rt, vend)
    print(f'{pasta.name} · base {B*100:.2f}% (RT {rt*100:.0f}%, vendedor {vend*100:.0f}%, sem cartão)')
    for x in T['hettich']['pv']:
        print(f'  {x[0]:12s} {x[1]:48s}' + ''.join(
            f"{brl(T[k]['cus'][x]):>13s}{brl(T[k]['pv'][x]):>14s}" for k in T))
    print(f"  {'TOTAL':61s}" + ''.join(f"{brl(T[k]['CD']):>13s}{brl(T[k]['venda']):>14s}" for k in T))
    for x in T['hettich']['pv']:
        mc_x = B - T['hettich']['cus'][x] / T['hettich']['pv'][x]
        if mc_x < 0.35: print(f'  ⚠ {x[0]} · {x[1]}: MC {mc_x*100:.1f}% (abaixo do piso de 35%)')
    print('  MC efetiva', ' / '.join(f"{(B - T[k]['CD'] / T[k]['venda'])*100:.1f}%" for k in T),
          '· chapas', T['hettich']['chapas'])
