# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — A VERSÃO FECHADA NA HETTICH  [06/11/2026]

⭐⭐ [Jonathan, 06/11/2026] "O cliente optou pela linha hettich."
   E com ela:
   · "retire os seguintes itens da proposta: Gourmet, na suíte o painel de
     cabeceira liso e estofado e as duas mesas de cabeceira";
   · "Adicione um painel liso de brinde no quarto de hospede";
   · "adicione um novo painel com portas de substituição para a rouparia em
     mdf melaminico amadeirado", "com abertura por toque com pulsadores Blum
     e um valor de 9.700";
   · "tire os valores de centavos dos itens tbm, vamos trabalhar com valores
     mais redondos".

⛔ A proposta LÊ o motor (`linhas.monta()`): os itens que ficam saem de lá,
   na coluna Hettich, com o preço que o cliente já viu no caderno de três
   linhas. Nenhum preço foi recalculado — só retirado, acrescido ou
   arredondado ao real.
⚠ O que NÃO tem custo levantado, e por isso não tem MC calculada:
   · a ROUPARIA — preço cravado pelo dono (R$ 9.700), sem prancha;
   · o PAINEL DE CORTESIA do quarto de hóspedes — sai a R$ 0 para o
     cliente, mas tem custo, e a medida dele fecha na medição.
"""
import importlib.util, sys, contextlib, io, pathlib

P = pathlib.Path(__file__).resolve().parent


def _mod(nome, arq):
    s = importlib.util.spec_from_file_location(nome, P / arq)
    m = importlib.util.module_from_spec(s); sys.modules[nome] = m
    with contextlib.redirect_stdout(io.StringIO()): s.loader.exec_module(m)
    return m


ln = _mod('ln', 'linhas.py')
LINHA = 'Hettich'
RETIRADOS = {('Gourmet', 'Armário complementar com portas de vidro'),
             ('Suíte', 'Painel liso da cabeceira'),
             ('Suíte', 'Cabeceira estofada'),
             ('Suíte', 'Mesas de cabeceira')}
NOVOS = [
    dict(amb='Rouparia', nome='Painel com portas de substituição, abertura por toque',
         pv=9700.0, por='[Jonathan, 06/11/2026] MDF melamínico amadeirado, pulsadores Blum, R$ 9.700'),
    dict(amb='Quarto de hóspedes', nome='Painel liso · cortesia',
         pv=0.0, por='[Jonathan, 06/11/2026] "painel liso de brinde no quarto de hospede"'),
]
ORDEM_AMB = ['Cozinha', 'Escritório', 'Sala de TV', 'Suíte', 'Suíte 01', 'Hall', 'Jantar',
             'Rouparia', 'Quarto de hóspedes']

_todos = ln.monta()
assert round(sum(d[f'{LINHA}_pv'] for d in _todos), 2) == 184184.35, '⛔ o motor saiu do caderno de três linhas'
_fora = [(d['amb'], d['nome']) for d in _todos if (d['amb'], d['nome']) in RETIRADOS]
assert set(_fora) == RETIRADOS, ('⛔ item a retirar não achado', RETIRADOS - set(_fora))

ITENS = [dict(amb=d['amb'], nome=d['nome'], pv_motor=d[f'{LINHA}_pv'], custo=d[LINHA],
              mc=d[f'{LINHA}_mc'])
         for d in _todos if (d['amb'], d['nome']) not in RETIRADOS]
ITENS += [dict(amb=n['amb'], nome=n['nome'], pv_motor=n['pv'], custo=None, mc=None) for n in NOVOS]
for it in ITENS:
    it['pv'] = int(it['pv_motor'] + 0.5)          # ⭐ ao real, sem centavo
ITENS.sort(key=lambda it: ORDEM_AMB.index(it['amb']))
TOTAL = sum(it['pv'] for it in ITENS)
PAGTO = [('Entrada, na assinatura do contrato', 0.30), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.30)]
GARANTIA = '10'

if __name__ == '__main__':
    amb = None
    for it in ITENS:
        if it['amb'] != amb:
            amb = it['amb']; print(amb)
        mc = f"MC {it['mc']*100:4.1f}%" if it['mc'] is not None else 'sem custo levantado'
        print(f"   {it['nome'][:58]:58s} {it['pv']:>8,} · motor {it['pv_motor']:>10,.2f} · {mc}")
    ret = sum(d[f'{LINHA}_pv'] for d in _todos if (d['amb'], d['nome']) in RETIRADOS)
    print(f'TOTAL {TOTAL:,} · retirado {ret:,.2f} · entrada {TOTAL * PAGTO[0][1]:,.2f}')
