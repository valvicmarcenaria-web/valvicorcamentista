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
br2 = lambda v: f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')

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

# ══════════════════════════════════════════════════════════════════════════
# CENÁRIO 1 — entrada de 20% + 10× no cartão  [Jonathan 07/10]
# "acrescentar 12% no percentual a ser dividido no cartão, evidenciando a
#  parcela ao invés do valor total"
# ⚠ 12% POR CIMA NÃO REPÕE 12% DE TAXA. A taxa incide sobre o valor já
#   acrescido: 54.280 × 1,12 = 60.793,60, taxa de 12% = 7.295,23, líquido
#   53.498,37 — faltam R$ 781,63. O acréscimo neutro seria ÷ 0,88 (+13,64%),
#   com parcela de R$ 6.168,18. Entregue como pedido; ver o quadro no fim.
# ══════════════════════════════════════════════════════════════════════════
TX_CARTAO = 0.012          # modelo-de-custo.md: 1,2% por parcela
C1_N      = 10
C1_ACRES  = 0.12
# ── escada proposta ───────────────────────────────────────────────────────
ENTRADA, N_BOL, DIA_1, PASSO = 0.20, 4, 60, 30
VAL_ENT = TOTAL*ENTRADA
A_PARC  = TOTAL*(1 - ENTRADA)          # a parte que não é entrada

# cenário 1 · cartão
C1_TOTPARC = A_PARC*(1 + C1_ACRES)
C1_PARCELA = C1_TOTPARC/C1_N
C1_TAXA    = C1_TOTPARC*TX_CARTAO*C1_N
C1_CLIENTE = VAL_ENT + C1_TOTPARC
C1_LIQUIDO = C1_CLIENTE - C1_TAXA
C1_FLUXO   = [(0, VAL_ENT)] + [(30*k, C1_PARCELA*(1 - TX_CARTAO*C1_N))
                               for k in range(1, C1_N + 1)]
# o acréscimo que deixaria a casa inteira
C1_NEUTRO  = A_PARC/(1 - TX_CARTAO*C1_N)/C1_N

# cenário 2 · boletos
VAL_BOL = A_PARC/N_BOL
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

    print(f'\n{"═"*W}')
    print(f'CENÁRIO 1 · entrada de {ENTRADA*100:.0f}% + {C1_N}× no cartão '
          f'(+{C1_ACRES*100:.0f}% sobre a parte parcelada)')
    print(f'{"═"*W}')
    print(f'  entrada .......................... R$ {br2(VAL_ENT)}')
    print(f'  ⭐ {C1_N} parcelas de ................ R$ {br2(C1_PARCELA)}')
    print(f'  o cliente paga, no total ......... R$ {br2(C1_CLIENTE)}')
    print(f'  taxa de cartão ({TX_CARTAO*C1_N*100:.0f}%) ............ R$ {br2(C1_TAXA)}')
    print(f'  a casa recebe, líquido ........... R$ {br2(C1_LIQUIDO)}')
    print(f'  ⚠ contra os R$ {br(TOTAL)} de investimento, faltam R$ {br2(TOTAL-C1_LIQUIDO)}')
    print(f'    o acréscimo neutro seria ÷ 0,88 '
          f'(+{(1/(1-TX_CARTAO*C1_N)-1)*100:.2f}%), parcela de R$ {br2(C1_NEUTRO)}')

    print(f'\n{"═"*W}')
    print(f'CENÁRIO 2 · entrada de {ENTRADA*100:.0f}% + {N_BOL} boletos a partir do dia {DIA_1}')
    print(f'{"═"*W}')
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
    print(f'\n{"═"*W}')
    print('OS DOIS CENÁRIOS, LADO A LADO')
    print(f'{"═"*W}')
    print(f'  {"":<30}{"cenário 1":>14}{"cenário 2":>14}')
    print(f'  {"":<30}{"cartão 10×":>14}{"4 boletos":>14}')
    print(f'  {"o cliente paga":<30}{br2(C1_CLIENTE):>14}{br2(TOTAL):>14}')
    print(f'  {"entrada":<30}{br2(VAL_ENT):>14}{br2(VAL_ENT):>14}')
    print(f'  {"e depois":<30}{"10 × "+br2(C1_PARCELA):>14}{"4 × "+br2(VAL_BOL):>14}')
    print(f'  {"taxa que a casa paga":<30}{br2(C1_TAXA):>14}{"—":>14}')
    print(f'  {"a casa recebe, líquido":<30}{br2(C1_LIQUIDO):>14}{br2(TOTAL):>14}')
    print(f'  {"último recebimento":<30}{"dia 300":>14}{"dia 150":>14}')
    print(f'  {"valor presente":<30}{br2(vp(C1_FLUXO)):>14}{br2(vp(FLUXO)):>14}')
    print(f'\n  ⚠ O cenário 1 custa mais ao cliente (R$ {br2(C1_CLIENTE-TOTAL)} a mais) e ainda')
    print(f'    entrega R$ {br2(vp(FLUXO)-vp(C1_FLUXO))} a MENOS de valor presente para a casa.')
    print('    O cartão parcela em 10 meses e cobra 12% por isso; o boleto fecha')
    print('    em 5 meses e não cobra nada. Os dois servem — mas não pelo mesmo motivo:')
    print('    o cenário 1 é para quem precisa de parcela baixa, o 2 é o melhor negócio.')

    print('\n  ⭐ O cenário 2 é o MELHOR em valor presente de todos — o')
    print('     desconto de 3 a 7% das outras opções custa mais à casa do que')
    print('     os 150 dias de espera custam a 1,2% ao mês.')
