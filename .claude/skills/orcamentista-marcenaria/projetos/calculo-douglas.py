# -*- coding: utf-8 -*-
"""DOUGLAS — estrutura de cálculo do cenário de fechamento  [07/10/2026]

⛔ NÃO é motor de custo. A proposta do Douglas não saiu de um motor da casa —
   só temos os PREÇOS DE VENDA por item. Aqui se calcula o que dá para
   calcular com isso: o total, a escada de pagamento e o perfil de caixa.

CONTEXTO [Jonathan 07/10]
  O cliente está abrindo o empreendimento e decidiu esperar para investir na
  marcenaria. O cenário existe para SEGURAR O SERVIÇO: entrada de 20% para
  reserva de agenda e o restante em 4 boletos sem juros, a valor cheio, a
  partir de 60 dias.
  ⭐ M07 "Painel e móvel" passa a contar como 3 unidades.
"""
br  = lambda v: f'{v:,.0f}'.replace(',', '.')

# ── itens da proposta v1 ──────────────────────────────────────────────────
ITENS = [('M01','Balcão recepção',           7500, 1, 'até dia 20'),
         ('M02','Painel',                    6800, 1, 'até dia 20'),
         ('M03','Prateleiras e rack',        5600, 1, ''),
         ('M04','Carrinho',                  3200, 1, ''),
         ('M05','Banco',                     1300, 1, 'até dia 20'),
         ('M06','Escaninho',                12500, 1, 'até dia 20'),
         ('M07','Painel e móvel',            4900, 3, '⭐ 3 unidades [Jonathan]'),
         ('M08','Mesa',                       950, 1, ''),
         ('M09','Armário e prateleiras',     6500, 1, ''),
         ('M10/11/13','Armários copa',       4900, 1, 'até dia 20 · ★ lote ou cada?'),
         ('M14','Painel curvo',              3900, 1, '')]
TOTAL = sum(v*q for _,_,v,q,_ in ITENS)

# ── escada proposta ───────────────────────────────────────────────────────
ENTRADA, N_BOL, DIA_1, PASSO = 0.20, 4, 60, 30
VAL_ENT = TOTAL*ENTRADA
VAL_BOL = TOTAL*(1-ENTRADA)/N_BOL
FLUXO   = [(0, VAL_ENT)] + [(DIA_1 + PASSO*k, VAL_BOL) for k in range(N_BOL)]

# ── valor presente ────────────────────────────────────────────────────────
# ⭐ taxa = 1,2% a.m., que é a MESMA que `modelo-de-custo.md` já cobra por
#   parcela de cartão. Usar a taxa da própria casa evita escolher um número
#   conveniente: se o cartão vale 1,2% ao mês para ela, o tempo também vale.
I = 0.012
def vp(fluxos): return sum(v/(1 + I)**(d/30) for d, v in fluxos)

OPCOES = [
  ('30% entrada + 10× cartão',      [(0,0.30)]+[(30*k,0.70/10) for k in range(1,11)], 0.00),
  ('50% entrada + 8× cartão',       [(0,0.50)]+[(30*k,0.50/8)  for k in range(1,9)],  0.03),
  ('70% entrada + 6× cartão',       [(0,0.70)]+[(30*k,0.30/6)  for k in range(1,7)],  0.05),
  ('70% entrada + transferência',   [(0,0.70),(60,0.30)],                             0.07),
  ('PROPOSTO · 20% + 4 boletos',    [(0,0.20)]+[(DIA_1+PASSO*k,0.20) for k in range(4)], 0.00),
]

if __name__ == '__main__':
    W = 80
    print('═'*W); print('DOUGLAS — estrutura de cálculo do cenário de fechamento'); print('═'*W)
    print(f'\n{"":<11}{"item":<24}{"unit":>8}{"qt":>4}{"total":>10}   obs')
    print('─'*W)
    for c,n,v,q,o in ITENS:
        print(f'{c:<11}{n:<24}{br(v):>8}{q:>4}{br(v*q):>10}   {o}')
    print('─'*W)
    print(f'{"":<11}{"INVESTIMENTO TOTAL":<24}{"":>12}{br(TOTAL):>10}')
    _v1 = sum(v for _,_,v,_,_ in ITENS)
    print(f'{"":<11}{"(v1, com M07 × 1)":<24}{"":>12}{br(_v1):>10}'
          f'   +{br(TOTAL-_v1)} com M07 × 3')

    print(f'\nESCADA · entrada de {ENTRADA*100:.0f}% + {N_BOL} boletos a partir do dia {DIA_1}')
    print(f'  entrada, reserva de agenda ....... R$ {br(VAL_ENT)}')
    print(f'  cada boleto ...................... R$ {br(VAL_BOL)}')
    print(f'  ⭐ os cinco pagamentos são IGUAIS — 20% cada')

    print('\nPERFIL DE CAIXA')
    print(f'  {"dia":>5}{"recebe":>11}{"acumulado":>12}{"% do total":>12}')
    ac = 0
    for d, v in FLUXO:
        ac += v
        print(f'  {d:>5}{br(v):>11}{br(ac):>12}{ac/TOTAL*100:>11.0f}%')
    print(f'  prazo médio ponderado de recebimento: '
          f'{sum(d*v for d,v in FLUXO)/TOTAL:.0f} dias')

    print(f'\nVALOR PRESENTE a {I*100:.1f}% a.m. — a taxa que a casa já cobra por parcela de cartão')
    print(f'  {"":<34}{"nominal":>10}{"VP":>10}{"vs melhor":>11}')
    res = [(r, TOTAL*(1-d), vp([(dd, TOTAL*p*(1-d)) for dd, p in f])) for r, f, d in OPCOES]
    best = max(x[2] for x in res)
    for rot, nom, v in res:
        print(f'  {rot:<34}{br(nom):>10}{br(v):>10}{v-best:>+11.0f}')
    print('\n  ⭐ O cenário proposto é o MELHOR em valor presente de todos — o')
    print('     desconto de 3 a 7% das outras opções custa mais à casa do que')
    print('     os 150 dias de espera custam a 1,2% ao mês.')
