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
# CENÁRIO 1 — entrada de 20% + 10× no cartão, A VALOR CHEIO  [Jonathan 07/10]
# "refaça os valores considerando o valor cheio do orçamento, sem considerar
#  acréscimo"
# ⭐ O cliente paga exatamente os R$ 67.850 — o MESMO do cenário 2. A escolha
#   dele deixa de ser de preço e passa a ser só de ritmo.
# ⚠ Mas a taxa não desaparece por não ser cobrada: 1,2% × 10 = 12% sobre a
#   parte parcelada, R$ 6.513,60, agora por conta da casa. É um desconto sem
#   nome, de 9,6% do total — MAIOR que os 7% que a opção "70% + transferência"
#   da v1 custaria. (modelo-de-custo.md §3.1, o mesmo princípio ao contrário:
#   separar uma linha não é descontá-la; não cobrar a taxa não a apaga.)
# ══════════════════════════════════════════════════════════════════════════
TX_CARTAO = 0.012          # modelo-de-custo.md: 1,2% por parcela
C1_N      = 10
C1_ACRES  = 0.00           # ⭐ valor cheio, sem acréscimo [Jonathan 07/10]
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
# o que a casa deixa na mesa por não repassar a taxa, em % do total
C1_CUSTO_PCT = C1_TAXA/TOTAL
# se um dia se quiser repassar: o acréscimo NEUTRO é ÷ 0,88 (+13,64%),
# nunca +12% — a taxa incide sobre o valor já acrescido
C1_NEUTRO  = A_PARC/(1 - TX_CARTAO*C1_N)/C1_N

# ⭐ O LADO DO CLIENTE. Nominalmente os dois cenários custam o mesmo, mas o
#   cartão espalha o desembolso por 10 meses e o boleto o concentra em 5 —
#   em valor presente o cenário 1 é MAIS BARATO PARA ELE. Ou seja: a valor
#   cheio, o cliente tem razão econômica para escolher justamente o cenário
#   que custa R$ 6.513,60 de taxa à casa. O cartão vira a escolha padrão.
C1_FLUXO_CLI = [(0, VAL_ENT)] + [(30*k, C1_PARCELA) for k in range(1, C1_N+1)]

# cenário 2 · boletos
VAL_BOL = A_PARC/N_BOL
FLUXO   = [(0, VAL_ENT)] + [(DIA_1 + PASSO*k, VAL_BOL) for k in range(N_BOL)]

# ══════════════════════════════════════════════════════════════════════════
# CENÁRIO 3 — entrada de 20% + 6 boletos a partir do dia 60  [Jonathan 07/10]
# "entrada de 20% + restante em 6 boletos com o primeiro a partir de 60 dias"
# É o cenário 2 esticado de 4 para 6 boletos: mesma lógica, parcela menor,
# último recebimento no dia 210 em vez de 150.
# ⚠ 54.280 ÷ 6 = 9.046,6667 — não fecha em centavos. A proposta mostra
#   R$ 9.046,67 e o ÚLTIMO boleto fecha a diferença de R$ 0,02.
# ══════════════════════════════════════════════════════════════════════════
N_BOL6   = 6
VAL_BOL6 = round(A_PARC/N_BOL6, 2)                       # 9.046,67
RESID6   = round(A_PARC - VAL_BOL6*N_BOL6, 2)            # −0,02, no último
FLUXO6   = ([(0, VAL_ENT)]
            + [(DIA_1 + PASSO*k, VAL_BOL6) for k in range(N_BOL6 - 1)]
            + [(DIA_1 + PASSO*(N_BOL6 - 1), VAL_BOL6 + RESID6)])
assert abs(sum(v for _, v in FLUXO6) - TOTAL) < 0.005, 'a escada não fecha'

# ── valor presente ────────────────────────────────────────────────────────
# ⭐ taxa = 1,2% a.m., que é a MESMA que `modelo-de-custo.md` já cobra por
#   parcela de cartão. Usar a taxa da própria casa evita escolher um número
#   conveniente: se o cartão vale 1,2% ao mês para ela, o tempo também vale.
I = 0.012
def vp(fluxos): return sum(v/(1 + I)**(d/30) for d, v in fluxos)

# ⭐ (rótulo, desconto, [(dia, fração, nº de parcelas no cartão)])
#   n = 0 → transferência ou boleto, sem taxa. n > 0 → taxa de 1,2% × n.
#   A v1 comparava opções de cartão SEM descontar a taxa, o que favorecia o
#   cartão de graça. Aqui toda opção paga o que custa.
OPCOES = [
  ('⭐ CENÁRIO 1 · 20% + 10× cartão', 0.00, [(0,0.20,0)]+[(30*k,0.80/C1_N,C1_N) for k in range(1,C1_N+1)]),
  ('⭐ CENÁRIO 3 · 20% + 6 boletos',  0.00, [(0,0.20,0)]+[(DIA_1+PASSO*k,0.80/N_BOL6,0) for k in range(N_BOL6)]),
  ('   CENÁRIO 2 · 20% + 4 boletos',  0.00, [(0,0.20,0)]+[(DIA_1+PASSO*k,0.20,0) for k in range(N_BOL)]),
  ('v1 · 30% entrada + 10× cartão',  0.00, [(0,0.30,0)]+[(30*k,0.70/10,10) for k in range(1,11)]),
  ('v1 · 50% entrada + 8× cartão',   0.03, [(0,0.50,0)]+[(30*k,0.50/8,8)   for k in range(1,9)]),
  ('v1 · 70% entrada + 6× cartão',   0.05, [(0,0.70,0)]+[(30*k,0.30/6,6)   for k in range(1,7)]),
  ('v1 · 70% entrada + transferência',0.07,[(0,0.70,0),(60,0.30,0)]),
]
def _cli(d, f): return sum(TOTAL*(1-d)*p for _,p,_ in f)
def _liq(d, f): return sum(TOTAL*(1-d)*p*(1-TX_CARTAO*n) for _,p,n in f)
def _vpl(d, f): return sum(TOTAL*(1-d)*p*(1-TX_CARTAO*n)/(1+I)**(dd/30) for dd,p,n in f)

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
          f'— A VALOR CHEIO, sem acréscimo')
    print(f'{"═"*W}')
    print(f'  entrada .......................... R$ {br2(VAL_ENT)}')
    print(f'  ⭐ {C1_N} parcelas de ................ R$ {br2(C1_PARCELA)}')
    print(f'  o cliente paga, no total ......... R$ {br2(C1_CLIENTE)}'
          f'   ← o valor cheio')
    print(f'  taxa de cartão ({TX_CARTAO*C1_N*100:.0f}%), por conta da casa  R$ {br2(C1_TAXA)}')
    print(f'  a casa recebe, líquido ........... R$ {br2(C1_LIQUIDO)}')
    print(f'  ⚠ a taxa virou desconto, só que sem nome: {C1_CUSTO_PCT*100:.1f}% do total,')
    print(f'    mais que os 7% da melhor oferta de desconto da v1')
    print(f'    se um dia se quiser repassar, o neutro é ÷ 0,88 '
          f'(+{(1/(1-TX_CARTAO*C1_N)-1)*100:.2f}%), não +12%:')
    print(f'    parcela de R$ {br2(C1_NEUTRO)} — R$ {br2(C1_NEUTRO-C1_PARCELA)} a mais por mês')

    print(f'\n{"═"*W}')
    print(f'CENÁRIO 2 · entrada de {ENTRADA*100:.0f}% + {N_BOL} boletos a partir do dia {DIA_1}')
    print(f'{"═"*W}')
    print(f'  entrada, reserva de agenda ....... R$ {br(VAL_ENT)}')
    print(f'  cada boleto ...................... R$ {br(VAL_BOL)}')
    print(f'  ⭐ os cinco pagamentos são IGUAIS — 20% cada')

    print(f'\n{"═"*W}')
    print(f'CENÁRIO 3 · entrada de {ENTRADA*100:.0f}% + {N_BOL6} boletos '
          f'a partir do dia {DIA_1}   ⭐ O ENTREGUE')
    print(f'{"═"*W}')
    print(f'  entrada, reserva de agenda ....... R$ {br2(VAL_ENT)}')
    print(f'  ⭐ cada boleto ................... R$ {br2(VAL_BOL6)}')
    print(f'  o último fecha os centavos ....... R$ {br2(VAL_BOL6+RESID6)}'
          f'   (resíduo {br2(RESID6)})')
    print(f'  último recebimento ............... dia {DIA_1+PASSO*(N_BOL6-1)}')
    print(f'  soma ............................. R$ {br2(sum(v for _,v in FLUXO6))}')

    print('\nPERFIL DE CAIXA · cenário 2 (4 boletos)')
    print(f'  {"dia":>5}{"recebe":>11}{"acumulado":>12}{"% do total":>12}')
    ac = 0
    for d, v in FLUXO:
        ac += v
        print(f'  {d:>5}{br(v):>11}{br(ac):>12}{ac/TOTAL*100:>11.0f}%')
    print(f'  prazo médio ponderado de recebimento: '
          f'{sum(d*v for d,v in FLUXO)/TOTAL:.0f} dias')

    print(f'\nVALOR PRESENTE a {I*100:.1f}% a.m. — a taxa que a casa já cobra por parcela de cartão')
    print('  ⭐ com a TAXA DE CARTÃO DESCONTADA em toda opção que usa cartão')
    print(f'  {"":<36}{"cliente":>9}{"líquido":>9}{"VP":>9}{"vs melhor":>11}')
    res = [(r, _cli(d,f), _liq(d,f), _vpl(d,f)) for r, d, f in OPCOES]
    best = max(x[3] for x in res)
    for rot, cli, lq, v in res:
        print(f'  {rot:<36}{br(cli):>9}{br(lq):>9}{br(v):>9}{v-best:>+11.0f}')
    print(f'\n{"═"*W}')
    print('OS DOIS CENÁRIOS, LADO A LADO')
    print(f'{"═"*W}')
    print(f'  {"":<30}{"cenário 1":>14}{"cenário 2":>14}')
    print(f'  {"":<30}{"cartão 10×":>14}{"4 boletos":>14}')
    print(f'  {"o cliente paga":<30}{br2(C1_CLIENTE):>14}{br2(TOTAL):>14}   ← IGUAL')
    print(f'  {"entrada":<30}{br2(VAL_ENT):>14}{br2(VAL_ENT):>14}')
    print(f'  {"e depois":<30}{"10 × "+br2(C1_PARCELA):>14}{"4 × "+br2(VAL_BOL):>14}')
    print(f'  {"taxa que a casa paga":<30}{br2(C1_TAXA):>14}{"—":>14}')
    print(f'  {"a casa recebe, líquido":<30}{br2(C1_LIQUIDO):>14}{br2(TOTAL):>14}')
    print(f'  {"último recebimento":<30}{"dia 300":>14}{"dia 150":>14}')
    print(f'  {"VP · o que a casa recebe":<30}{br2(vp(C1_FLUXO)):>14}{br2(vp(FLUXO)):>14}')
    print(f'  {"VP · o que o cliente paga":<30}{br2(vp(C1_FLUXO_CLI)):>14}{br2(vp(FLUXO)):>14}')
    print(f'\n  ⭐ A VALOR CHEIO, o cliente paga o MESMO nos dois cenários.')
    print('    A escolha dele deixa de ser de preço e passa a ser só de ritmo:')
    print(f'    parcela de R$ {br2(C1_PARCELA)} por 10 meses, começando no mês que vem,')
    print(f'    ou R$ {br(VAL_BOL)} a cada 30 dias, começando só no dia 60.')
    print(f'\n  ⚠ Para a CASA os dois são muito diferentes. O cenário 1 custa')
    print(f'    R$ {br2(C1_TAXA)} de taxa ({C1_CUSTO_PCT*100:.1f}% do total) e estende o recebimento')
    print(f'    até o dia 300 — R$ {br2(vp(FLUXO)-vp(C1_FLUXO))} a menos de valor presente.')
    print('    É mais caro que qualquer desconto que a v1 oferecia, inclusive os 7%.')

    print(f'\n  ⛔ E O CLIENTE TEM RAZÃO ECONÔMICA PARA ESCOLHER O CENÁRIO 1.')
    print(f'    Em valor presente ele paga R$ {br2(vp(FLUXO)-vp(C1_FLUXO_CLI))} a MENOS no cartão,')
    print('    porque o mesmo nominal espalhado em 10 meses vale menos hoje.')
    print('    A valor cheio o cartão vira a escolha padrão — e é a cara para a casa.')
    print('    Se os dois forem oferecidos lado a lado, contar com o cenário 2 é')
    print('    torcer, não precificar. Formas de corrigir sem mexer no preço:')
    print('     · menos parcelas no cartão (6× custa 7,2% em vez de 12%)')
    print('     · o cenário 2 ganhar algo que custe menos que R$ 6.513,60')
    print('     · ou repassar a taxa, com o acréscimo NEUTRO de +13,64%')

    print('\n  ⭐ O cenário 2 segue o MELHOR em valor presente de todos — e agora')
    print('     com folga maior, porque a tabela acima parou de dar cartão de graça')
    print('     às opções da v1. Os 150 dias de espera a 1,2% ao mês custam menos')
    print('     à casa do que o desconto OU a taxa de cartão de qualquer alternativa.')
