# -*- coding: utf-8 -*-
"""Phillip e Giselle · VERSÃO 2, a reduzida  [Jonathan, 06/11/2026]

"uma segunda versão do orçamento contemplando os seguintes itens e mantendo o
valor da proposta: Quarto de casal: cabeceira e portas pivotantes · Painel
circulação · Quarto Ana e quarto Mateus. Me apresente os valores antes de
gerar a proposta."

⭐ O PREÇO DE CADA ITEM É O DA PROPOSTA ATUAL (precos.py), sem recálculo.
⭐ O CUSTO é refeito SÓ com os itens da versão 2. Com menos chapa, o
   arredondamento é outro e o frete cai: o custo rateado do projeto inteiro
   não serve para dizer a margem desta versão.
⚠ O frete segue a régua de cerca de 20 chapas por viagem, a mesma que deu as
  5 viagens do projeto inteiro.
"""
import sys, os, json, math, subprocess, pathlib, io, contextlib
AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parent))

V2 = [('Quarto casal', 'Portas ripadas pivotantes (closet e banho)'),
      ('Quarto casal', 'Cabeceira'),
      ('Suíte Ana', 'Móvel da janela (nichos, banco e gavetões)'),
      ('Suíte Ana', 'Painel com 3 portas mimetizadas'),
      ('Quarto Mateus', 'Painel com porta oculta'),
      ('Circulação', 'Painel com 4 portas mimetizadas')]
MODS = ['a01_quarto_casal', 'a05_quarto_mateus', 'a06_quarto_ana', 'a10_circulacao']
CHAPAS_POR_VIAGEM = 20

if os.environ.get('LINHA') and __name__ == '__main__':
    import importlib, motor as M
    for a in MODS: importlib.import_module(a)
    M.pecas[:] = [p for p in M.pecas if (p['amb'], p['movel']) in V2]
    M.outras[:] = [o for o in M.outras if (o['amb'], o['movel']) in V2]
    R0 = M.calcula(0.0)
    viagens = max(1, math.ceil(sum(R0['chapas'].values()) / CHAPAS_POR_VIAGEM))
    R = M.calcula(viagens * 200.0)
    cm, _ = M.custo_por_movel(R)
    print(json.dumps(dict(CD=R['CD'], viagens=viagens, chapas=sum(R['chapas'].values()),
                          cus={f'{a}||{m}': v for (a, m), v in cm.items()})))
    sys.exit()

with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
from motor import brl

T = {}
for k in PR.TAB:
    r = subprocess.run([sys.executable, __file__], env=dict(os.environ, LINHA=k),
                       capture_output=True, text=True, check=True, cwd=AQUI)
    d = json.loads(r.stdout)
    cus = {tuple(x.split('||')): v for x, v in d['cus'].items()}
    pv = {x: PR.TAB[k]['pv'][x] for x in V2}
    T[k] = dict(pv=pv, cus=cus, venda=sum(pv.values()), CD=d['CD'], viagens=d['viagens'],
                chapas=d['chapas'])
    assert abs(sum(cus.values()) - d['CD']) < 0.05

if __name__ == '__main__':
    B = PR.B
    for k, t in T.items():
        print(f"\n{PR.TAB[k]['nome'].upper()} · {t['chapas']} chapas · {t['viagens']} viagens de frete")
        for x in V2:
            print(f"  {x[0]:14s} {x[1][:44]:44s} {brl(t['pv'][x]):>14s} · custo {brl(t['cus'][x]):>13s}"
                  f" · MC {(B - t['cus'][x] / t['pv'][x]) * 100:5.1f}%")
        print(f"  {'TOTAL':59s} {brl(t['venda']):>14s} · custo {brl(t['CD']):>13s}"
              f" · MC {(B - t['CD'] / t['venda']) * 100:5.1f}%")
