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
⭐⭐ [Jonathan, 06/11/2026] DUAS CORREÇÕES, as duas no motor:
   · "as portas do corredor mudam de deslizantes para pivotantes": sai o
     sistema de correr com os desempenadores, entra o pivô. O preço segue
     CRAVADO em R$ 39.700 — não foi pedido mudar —, e a MC realizada sobe
     porque o custo caiu;
   · "o painel ripado da sala de tv ganha duas portas compridas para acesso
     de manutenções a quadro de energia e rede hidraulica": duas folhas
     ripadas de 45 × 272, em giro, por toque. Este item SOBE.
   ⛔ E O QUE NÃO FOI MEXIDO NÃO MUDA DE PREÇO. O motor rateia a sobra de
     chapa pelo AMBIENTE, e as peles de 6 das portas mexeram no rateio do
     painel liso e do rack (+R$ 295 num, −R$ 224 no outro). Eles ficam no
     preço que o cliente viu, e a diferença vai para o ripado — o total da
     Sala de TV continua sendo o do motor, ao centavo.
⭐⭐ [Jonathan, 06/11/2026] "reformule a proposta tirando o painel da
   rouparia, mantendo o painel de cortesia e valor de venda final de
   164.000 na linha hettich".
   ⭐ O ALVO SE FAZ COMO NA BLUM: os preços CRAVADOS pelo dono (corredor
     39.700, parede da TV 15.500) e a cortesia ficam fora da diluição, e o
     resto cai na MESMA PROPORÇÃO sobre o valor que o cliente já viu. A
     sobra do arredondamento ao real vai para o maior item diluído, e o
     total fecha em 164.000 exato.
⚠ O que NÃO tem custo levantado, e por isso não tem MC calculada:
   · ⛔ a ROUPARIA saiu em 06/11/2026 (era R$ 9.700 cravado, sem prancha);
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
    #   ⛔ [Jonathan, 06/11/2026] "tirando o painel da rouparia": era R$ 9.700,
    #     MDF melamínico amadeirado com pulsadores Blum, sem prancha.
    dict(amb='Quarto de hóspedes', nome='Painel liso · cortesia',
         pv=0.0, por='[Jonathan, 06/11/2026] "painel liso de brinde no quarto de hospede"'),
]
ORDEM_AMB = ['Cozinha', 'Escritório', 'Sala de TV', 'Suíte', 'Suíte 01', 'Hall', 'Jantar',
             'Quarto de hóspedes']
ALVO = 164000          # ⭐ [Jonathan, 06/11/2026] o valor de venda final, na Hettich

_todos = ln.monta()
#   ⭐ 184.184,35 no caderno de três linhas · 188.973,24 depois das duas
#     correções de 06/11 (pivô no corredor, portas de manutenção na TV)
assert round(sum(d[f'{LINHA}_pv'] for d in _todos), 2) == 188973.24, '⛔ o motor mudou e ninguém pediu'
#   ⭐ os que ficam no preço que o cliente já viu, e quem absorve o rateio
INTOCADOS = {('Sala de TV', 'Painel liso'): 3227.55, ('Sala de TV', 'Rack de TV'): 7734.11}
ABSORVE = {'Sala de TV': 'Painel ripado com duas portas de manutenção'}
for d in _todos:
    k = (d['amb'], d['nome'])
    if k in INTOCADOS:
        dif = d[f'{LINHA}_pv'] - INTOCADOS[k]
        alvo = next(x for x in _todos if (x['amb'], x['nome']) == (d['amb'], ABSORVE[d['amb']]))
        amb_antes = sum(x[f'{LINHA}_pv'] for x in _todos if x['amb'] == d['amb'])
        d[f'{LINHA}_pv'] = INTOCADOS[k]
        alvo[f'{LINHA}_pv'] += dif
        for x in (d, alvo):
            x[f'{LINHA}_mc'] = ln.b.BASE - x[LINHA] / x[f'{LINHA}_pv']
        assert abs(sum(x[f'{LINHA}_pv'] for x in _todos if x['amb'] == d['amb']) - amb_antes) < 0.005
_fora = [(d['amb'], d['nome']) for d in _todos if (d['amb'], d['nome']) in RETIRADOS]
assert set(_fora) == RETIRADOS, ('⛔ item a retirar não achado', RETIRADOS - set(_fora))

ITENS = [dict(amb=d['amb'], nome=d['nome'], pv_motor=d[f'{LINHA}_pv'], custo=d[LINHA],
              mc=d[f'{LINHA}_mc'], cravado=bool(d.get('grupo', {}).get('cravado')))
         for d in _todos if (d['amb'], d['nome']) not in RETIRADOS]
ITENS += [dict(amb=n['amb'], nome=n['nome'], pv_motor=n['pv'], custo=None, mc=None, cravado=True)
          for n in NOVOS]
for it in ITENS:
    it['pv_antes'] = int(it['pv_motor'] + 0.5)    # ⭐ ao real: o que o cliente já viu
#   ── o alvo de 164.000: cravado e cortesia parados, o resto na mesma proporção
_fixos = [it for it in ITENS if it['cravado']]
_resto = [it for it in ITENS if not it['cravado']]
FATOR = (ALVO - sum(it['pv_antes'] for it in _fixos)) / sum(it['pv_antes'] for it in _resto)
for it in ITENS:
    it['pv'] = it['pv_antes'] if it['cravado'] else int(it['pv_antes'] * FATOR + 0.5)
max(_resto, key=lambda it: it['pv'])['pv'] += ALVO - sum(it['pv'] for it in ITENS)
for it in _resto:
    it['mc'] = ln.b.BASE - it['custo'] / it['pv']
ITENS.sort(key=lambda it: ORDEM_AMB.index(it['amb']))
TOTAL = sum(it['pv'] for it in ITENS)
assert TOTAL == ALVO, TOTAL
#   ⭐ a MC do projeto, sobre o que tem custo levantado (a cortesia não tem)
MC_PROJETO = ln.b.BASE - sum(it['custo'] for it in ITENS if it['custo']) / TOTAL
PAGTO = [('Entrada, na assinatura do contrato', 0.30), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.30)]
#   ⭐ [Jonathan, 06/11/2026] "vamos colocar o valor de R$ ao lado das
#     porcentagens tbm". Em real cheio, como os itens: a última parcela
#     absorve o arredondamento, e a soma fecha no total ao real.
PARCELAS = [int(TOTAL * p + 0.5) for _r, p in PAGTO[:-1]]
PARCELAS.append(TOTAL - sum(PARCELAS))
assert sum(PARCELAS) == TOTAL and all(abs(v - TOTAL * p) <= 1 for v, (_r, p) in zip(PARCELAS, PAGTO))
GARANTIA = '10'

if __name__ == '__main__':
    amb = None
    for it in ITENS:
        if it['amb'] != amb:
            amb = it['amb']; print(amb)
        mc = f"MC {it['mc']*100:4.1f}%" if it['mc'] is not None else 'sem custo levantado'
        print(f"   {it['nome'][:58]:58s} {it['pv']:>8,} · antes {it['pv_antes']:>8,} · {mc}")
    ret = sum(d[f'{LINHA}_pv'] for d in _todos if (d['amb'], d['nome']) in RETIRADOS)
    print(f'TOTAL {TOTAL:,} · fator {FATOR:.4f} ({(1 - FATOR) * 100:.2f}% nos itens diluídos) · '
          f'MC do projeto {MC_PROJETO * 100:.1f}% · retirado {ret:,.2f}')
    for (r, p), v in zip(PAGTO, PARCELAS):
        print(f'   {p*100:3.0f}%  R$ {v:>8,}  {r}')
