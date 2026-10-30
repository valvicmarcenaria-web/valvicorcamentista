# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO — os três cenários de ferragem e as duas trocas.

⭐ ESTE MÓDULO É A ÚNICA FONTE DE NÚMERO DA PROPOSTA. O build importa daqui;
  nada é digitado na peça. É a mesma regra do `corte-michelle-arlei.py`.

⛔⛔ E A CONTA É A DA PLANILHA, NÃO UMA PARALELA: preço = custo ÷ (BASE − MC),
  BASE = 1 − encargos. Qualquer fórmula escrita aqui que divirja da aba
  "Preço e Comissões" é um preço que só existe de um lado da conta — foi
  exatamente assim que a corrediça Hettich passou meses errada.
"""
# ── os encargos, na ordem da aba Preço e Comissões ──────────────────────
ENCARGOS = (0.05        # nota fiscal, sobre o bruto
            + 0.00      # cartão · 1,2% × 0 parcelas
            + 0.02      # margem de erro
            + 0.005     # desgaste de serra e fresa
            + 0.005     # manutenção de máquinas
            + 0.00      # RT de arquiteto
            + 0.00      # comissão de vendedor
            + 0.025*0.95 + 0.025*0.95      # produção, montagem
            + 0.01*0.95 + 0.01*0.95        # projeto, coordenação
            + 0.005*0.95)                  # gestão de projetos
BASE = 1 - ENCARGOS
assert abs(ENCARGOS - 0.15125) < 1e-9, ENCARGOS

# ── os dezenove ambientes, como a planilha os tem hoje ──────────────────
#    custo direto · pares de corrediça · dobradiças
AMB = [
 ('01 Varanda',           10568.90,  8, 20), ('02 Lavabo',          1082.32,  0,  0),
 ('03 Cozinha',           24619.43,  7, 10), ('04 Despensa',        3939.78,  0,  0),
 ('05 Lavanderia',         7387.44,  5,  3), ('06 Rouparia',        5619.80,  0, 20),
 ('07 Office',             9328.00,  0,  0), ('08 Suíte Master',   10706.53,  4,  8),
 ('09 Closet Master',     11651.11, 12,  0), ('10 Banho Master',    5627.02,  2,  4),
 ('11 Suíte 01 Filhos',   20883.37, 13,  0), ('12 Banho Suíte 01',  2367.60,  2,  4),
 ('13 Suíte 02 Filhas',   17534.94, 14,  0), ('14 Closet Suíte 02', 8248.74,  4,  0),
 ('15 Banho Suíte 02',     2374.36,  2,  4), ('16 Suíte Hóspedes',  7489.49,  8,  0),
 ('17 Banho Hóspedes',     1571.69,  0,  4), ('18 Banho Social',    1603.93,  0,  4),
 ('19 Homeschooling',      9203.79,  6, 16),
]
assert abs(sum(a[1] for a in AMB) - 161808.24) < 0.01   # ⛔ é o custo de hoje
assert sum(a[2] for a in AMB) == 87 and sum(a[3] for a in AMB) == 97

# ⭐ A FERRAGEM SÓ ARRASTA A EMBALAGEM. Os consumíveis são 6% sobre chapa,
#   fita e filetagem — onde ferragem não entra. A embalagem é 2% sobre um
#   subtotal que a inclui. Conferido contra a Varanda: R$ 207,23 de
#   embalagem sobre R$ 10.361,67 de subtotal.
EMB = 1.02
CORR_BASE, DOBR_BASE = 150.0, 50.0          # a casa está em Hettich

# ── as três linhas ──────────────────────────────────────────────────────
#    (nome, corrediça, dobradiça, MC, garantia, chamada)
LINHAS = [
 ('Blum',         300.0, 50.0, 0.42, '30 anos', 'Corrediça e dobradiça Blum'),
 ('Hettich',      150.0, 50.0, 0.42, '10 anos', 'Corrediça oculta Hettich'),
 ('Telescópica',   40.0, 10.0, 0.35,  '2 anos', 'Corrediça telescópica'),
]
def custos(corr, dobr):
    return [c + (p*(corr-CORR_BASE) + d*(dobr-DOBR_BASE))*EMB
            for _, c, p, d in AMB]

CEN = {}
for nome, corr, dobr, mc, gar, cham in LINHAS:
    lin = custos(corr, dobr)
    CEN[nome] = dict(custo=sum(lin), mc=mc, gar=gar, chamada=cham, div=BASE-mc,
                     pv=[v/(BASE-mc) for v in lin], preco=sum(lin)/(BASE-mc))
assert abs(CEN['Hettich']['custo'] - 161808.24) < 0.01   # ⭐ a planilha de hoje
for n in CEN:                                            # ⛔ piso da casa
    assert CEN[n]['mc'] >= 0.35, n

# ── as duas trocas ──────────────────────────────────────────────────────
# ⭐ [Jonathan 30/10] "Retire do preço cheio um valor unico, considere esse
#   para os tres cenarios" — os descontos da coluna da telescópica, que são
#   os MENORES. Aplicados sobre as linhas de MC 42% eles devolvem ao cliente
#   MENOS do que a economia justificaria ali, e a margem sobe.
TROCA = [
 ('Cozinha em melamínico', 28343.92, 14136.53,
  'A cozinha sai da laca e vai para o melamínico, em frente lisa'),
 ('Painel do office usinado', 12177.30, 6073.43,
  'A grade de réguas vira painel plano usinado na CNC'),
]
def mc_apos(linha, descontos):
    """MC realizada depois de aplicar os descontos — é ela que não pode
       furar o piso de 35%."""
    dp = sum(TROCA[i][1] for i in descontos)
    dc = sum(TROCA[i][2] for i in descontos)
    pr = CEN[linha]['preco'] - dp
    return BASE - (CEN[linha]['custo'] - dc)/pr, pr
for n in CEN:                              # ⛔ nenhuma das doze combinações
    for comb in ([], [0], [1], [0, 1]):    #   pode furar o piso
        assert mc_apos(n, comb)[0] >= 0.35 - 1e-9, (n, comb)

if __name__ == '__main__':
    print(f'BASE {BASE*100:.3f}%')
    for n in CEN:
        c = CEN[n]
        print(f'  {n:14s} MC {c["mc"]*100:.0f}% · custo {c["custo"]:>12,.2f} · '
              f'PREÇO {c["preco"]:>12,.2f} · {c["gar"]}')
    for n in CEN:
        mc, pr = mc_apos(n, [0, 1])
        print(f'  {n:14s} com as duas trocas: {pr:>12,.2f} · MC {mc*100:.2f}%')
