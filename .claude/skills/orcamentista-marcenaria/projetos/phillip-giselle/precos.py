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

Revisão de escopo [Jonathan, 06/11/2026] — seis mudanças:
  ① só DUAS linhas: Hettich e Blum (a Telescópica sai da proposta)
  ② o QUARTO DO MATEUS sai inteiro (o closet dele fica)
  ③ as portas ripadas viram PIVOTANTES (preço fixo de 8.500 mantido)
  ④ o CLOSET DE CASAL perde todas as portas
  ⑤ as portas de ESPELHO do closet de casal em LINHA PRÓPRIA
  ⑥ os CLOSETS ANA E MATEUS perdem as portas
  ⛔ VALOR SÓ MUDA SE PEDIDO: o que não foi tocado fica no preço que o
    cliente viu em 04/11, na tabela VISTO abaixo. Só os três closets e a
    linha nova saem do motor.
"""
import sys, os, json, subprocess, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import motor_mc as MC
from resumo import AVULSO
from motor import brl

AQUI = pathlib.Path(__file__).parent
# (nome, MC da ferragem de movimento, MC da parte comum dos ITENS QUE TÊM
#  ferragem da linha). ⭐ [Jonathan, 04/11/2026] "vamos puxar a Hettich em 5%
#  de MC acima e a Blum em 10" → os itens com gaveta/dobradiça da linha sobem
#  INTEIROS; os sem ferragem de linha continuam a 42%, iguais nas três.
#   ⛔ [Jonathan, 06/11/2026] "duas linhas de ferragem: HETTICH e BLUM"
LIN = {'hettich': ('Hettich', 0.43, 0.47), 'blum': ('Blum', 0.55, 0.52)}
MC_COMUM = 0.42
PROJETO = 2000.0
B = MC.base(0, rt=False, vendedor=False)                      # 84,875%
PAGTO = [('Entrada, na assinatura do contrato', 0.30), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.30)]
ORDEM = ['Quarto casal', 'Closet casal', 'Closet casal · portas de espelho', 'Suíte Ana',
         'Closet Ana', 'Closet Mateus', 'Rouparia', 'Circulação']
FIXO_ITEM = {('Suíte Ana', 'Móvel da janela (nichos, banco e gavetões)'): 9800.0,
             ('Suíte Ana', 'Painel com 3 portas mimetizadas'): 15600.0,
             # ⭐ "ambas as portas ripadas são de correr, preço final de ambas 8.500"
             ('Quarto casal', 'Portas ripadas pivotantes (closet e banho)'): 8500.0,
             # ⭐ [Jonathan, 06/11/2026] "as portas de espelho do closet vamos
             #   vender por 4.500" · ⛔ ABAIXO DO CUSTO: decisão de preço
             #   declarada, e a MC negativa sai impressa na tabela
             ('Closet casal · portas de espelho', 'Portas de correr com espelho na sapateira'): 4500.0}
# ⭐ "Rouparia, valor total de venda 9.300" (os dois armários na proporção)
FIXO_AMB = {'Rouparia': 9300.0}
# ⭐ MESCLA num item só [Jonathan, 04/11/2026]: o fator é o desconto do total
#   "Closet casal pode diminuir 10% do valor total e apresente um item único"
#   "Closet Ana, mescle o valor de cada item · idem Closet Mateus"
MESCLA = {'Closet casal': ('Closet completo, sem portas: armários, sapateira e fechamento', 0.90),
          'Closet Ana': ('Armário em L do piso ao forro', 1.00),
          'Closet Mateus': ('Armário em L do piso ao forro', 1.00)}
DILUI = lambda a, m: ((a.startswith('Closet') and 'espelho' not in a)
                      or m == 'Painel com 3 portas mimetizadas')
# ⛔⛔ A TABELA DECLARADA: o preço que o cliente viu em 04/11/2026, nos itens
#   que a revisão de 06/11 NÃO tocou (Hettich, Blum). Sem isto, tirar o
#   quarto do Mateus e as portas mexeria no rateio da chapa e do frete e
#   andaria com o preço de quem ninguém pediu para mudar.
VISTO = {('Quarto casal', 'Mesa rack suspensa'): (4250, 7310),
         ('Quarto casal', 'Torre de nichos'): (2490, 2490),
         ('Quarto casal', 'Espelho com LED'): (5000, 5000),
         ('Quarto casal', 'Cabeceira'): (4290, 4290),
         ('Quarto casal', 'Mesinhas de cabeceira (2)'): (2820, 4460),
         ('Rouparia', 'Armário parede A (174 × 270 × 45)'): (5030, 5030),
         ('Rouparia', 'Armário parede B (121 × 270 × 70)'): (4270, 4270),
         ('Circulação', 'Painel com 4 portas mimetizadas'): (22430, 22430)}
# ⭐ o que o cliente viu nos três closets em 04/11, para a tabela comparar
ANTES = {('Closet casal', 'Closet completo: armários, sapateira com espelho e fechamento'): (45030, 55720),
         ('Closet Ana', 'Armário em L do piso ao forro'): (28460, 33880),
         ('Closet Mateus', 'Armário em L do piso ao forro'): (28460, 33880),
         ('Quarto Mateus', '(cinco itens)'): (17550, 19850)}
TOTAL_ANTES = {'hettich': 203980, 'blum': 232510}
# ⭐ [Jonathan, 06/11/2026] "linha própria, não embutida no conjunto": o
#   opcional NÃO soma no total do projeto, aparece ao lado dele.
OPCIONAL = {'Closet casal · portas de espelho'}

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
for k, (nome, mc, mc_item) in LIN.items():
    cus, mov = linha(k)
    com = {x: cus[x] - mov[x] for x in cus}
    # projeto diluído na parte comum (que não muda de linha → mesmo rateio)
    alvo = {x: com[x] for x in com if DILUI(*x)}
    for x, v in alvo.items():
        com[x] += PROJETO * v / sum(alvo.values()); cus[x] += PROJETO * v / sum(alvo.values())
    pv = {x: round(com[x] / (B - (mc_item if mov[x] > 0 else MC_COMUM)), -1)
             + round(mov[x] / (B - mc), -1) for x in cus}
    for x, v in FIXO_ITEM.items(): pv[x] = v
    for a, v in FIXO_AMB.items():
        it = [x for x in pv if x[0] == a]; tot = sum(pv[x] for x in it)
        for x in it: pv[x] = round(v * pv[x] / tot, -1)
        pv[max(it, key=pv.get)] += v - sum(pv[x] for x in it)
    for a, (nm, fat) in MESCLA.items():
        it = [x for x in pv if x[0] == a]
        v = round(sum(pv[x] for x in it) * fat, -1); c = sum(cus[x] for x in it)
        for x in it: del pv[x]; del cus[x]
        pv[(a, nm)] = v; cus[(a, nm)] = c
    for x, vs in VISTO.items():
        pv[x] = float(vs[list(LIN).index(k)])
    conj = [x for x in pv if x[0] not in OPCIONAL]
    TAB[k] = dict(nome=nome, mc=mc, cus=cus, pv=pv,
                  CD=sum(cus[x] for x in conj), venda=sum(pv[x] for x in conj),
                  opc={x: pv[x] for x in pv if x[0] in OPCIONAL},
                  opc_cus={x: cus[x] for x in pv if x[0] in OPCIONAL})

# ⛔ as travas
for x in TAB['hettich']['pv']:
    if not TAB['blum']['cus'][x] - TAB['hettich']['cus'][x]:   # sem ferragem de linha
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
    print(f"\n{'TOTAL DO CONJUNTO (sem o opcional)':50s}" + ''.join(f"{brl(T[k]['venda']):>15s}" for k in T))
    print(f"{'OPCIONAL · portas de espelho':50s}" + ''.join(f"{brl(sum(T[k]['opc'].values())):>15s}" for k in T))
    print(f"{'CUSTO DIRETO':50s}" + ''.join(f"{brl(T[k]['CD']):>15s}" for k in T))
    print(f"{'MC efetiva':50s}" + ''.join(f"{(B - T[k]['CD'] / T[k]['venda'])*100:14.1f}%" for k in T))
    for lab, f in PAGTO:
        print(f"{lab:50s}" + ''.join(f"{brl(T[k]['venda'] * f):>15s}" for k in T))
    for x, v in FIXO_ITEM.items():
        print('MC do fixo', x[1], ' / '.join(f"{(B - T[k]['cus'][x] / v)*100:.1f}%" for k in T))
    for a in list(FIXO_AMB) + list(MESCLA):
        it = [x for x in T['hettich']['pv'] if x[0] == a]
        print('MC', a, ' / '.join(f"{(B - sum(T[k]['cus'][y] for y in it) / sum(T[k]['pv'][y] for y in it))*100:.1f}%" for k in T))
    for d, v, obs in AVULSO: print(f'AVULSO {brl(v)} · {obs}')
