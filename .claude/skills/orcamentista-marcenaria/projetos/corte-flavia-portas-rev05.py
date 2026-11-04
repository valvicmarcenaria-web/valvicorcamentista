# -*- coding: utf-8 -*-
"""FLÁVIA — portas e painéis do vão da escada · REV.05  [Jonathan 04/08/2026]

RETIFICAÇÃO DE ESCOPO. A REV.04 (entregue, R$ 14.500) tinha DUAS portas de giro
e UM painel de complemento. Agora:

  · 2 PAINÉIS FIXOS
  · 1 PORTA PIVOTANTE — dobradiça invisível, puxador em cava, COM fechadura
  · 1 PORTA DE CORRER — sistema RO82 com duplo amortecimento, cava, SEM fechadura
  · rodapé de alumínio fosco de 30 mm em portas E painéis
  · MDF Itapuã Ultra

Comercial: desconto especial de 10% · 50% + 50% · até 45 dias corridos.
"""
CHAPA_A, CHAPA_L = 2.75, 1.85
CHAPA_AREA = CHAPA_A * CHAPA_L
DENS_MDF, ESP_FACE = 750, 0.015

# ── preços ───────────────────────────────────────────────────────────────────
P_CHAPA      = 580.0   # MDF Itapuã Ultra 15mm — mesmo patamar da linha Ultra da REV.04
P_FITA_M     = 4.0
P_SARRAFO_M  = 8.0
P_DOBR_IN600 = 250.0   # Häfele IN600 — dobradiça INVISÍVEL, valor confirmado pelo cliente
P_RO82_TOP   = 400.0   # Rometal RO82 "top" = versão com amortecimento nos dois sentidos
P_TRILHO_2M  = 200.0   # trilho RO82 2 m (porta de 88 → curso ~176)
P_FECHADURA  = 250.0   # ⚠ ESTIMATIVA — fechaduras não estão catalogadas na base
P_RODAPE_M   = 38.0    # perfil de alumínio, referência da base (preto/bronze 38)
P_CAVA_M     = 50.0    # cava usinada, por metro

VAO_TOTAL, ALTURA = 4.45, 2.20

# ── peças ────────────────────────────────────────────────────────────────────
# (nome, largura, nº faces, tipo)
PORTA_PIV  = ('Porta pivotante',    1.16, 2, 'piv')
PORTA_COR  = ('Porta de correr',    0.88, 2, 'cor')
LARG_PAINEIS = VAO_TOTAL - PORTA_PIV[1] - PORTA_COR[1]           # 2,41 m
PAINEL_L = LARG_PAINEIS / 2                                       # 2 painéis fixos iguais
PAINEIS = [('Painel fixo 1', PAINEL_L, 1, 'pai'), ('Painel fixo 2', PAINEL_L, 1, 'pai')]
PECAS = [PORTA_PIV, PORTA_COR] + PAINEIS

print('═'*84)
print('FLÁVIA — VÃO DA ESCADA · REV.05 · 2 painéis fixos + pivotante + correr')
print('MDF Itapuã Ultra · rodapé de alumínio fosco 30 mm')
print('═'*84)
print(f'\nVão de passagem: {VAO_TOTAL*100:.0f} × {ALTURA*100:.0f} cm')
print(f'  pivotante {PORTA_PIV[1]*100:.0f} + correr {PORTA_COR[1]*100:.0f} + '
      f'2 painéis de {PAINEL_L*100:.1f} = {VAO_TOTAL*100:.0f} cm  ✓')

area = perim = 0.0
print('\nPEÇAS')
for nome, larg, faces, tipo in PECAS:
    a = ALTURA*larg*faces
    p = 2*(ALTURA+larg)
    area += a; perim += p
    peso = (a*ESP_FACE*DENS_MDF)*1.15 if faces == 2 else 0
    ex = f' · peso {peso:.1f} kg' if peso else ''
    print(f'  {nome:<20} {ALTURA*100:.0f}×{larg*100:>5.1f} cm · {faces} face(s) · '
          f'{a:>5.2f} m² · fita {p:>5.2f} m{ex}')
    if tipo == 'piv': peso_piv = peso

# ── plano de corte ───────────────────────────────────────────────────────────
# Nenhuma peça de 220 cm cabe no lado de 185; todas correm no eixo de 275.
# Larguras: 116 · 88 · 120,5 · 120,5 — duas de 88+... não somam <185 com as demais.
print('\nPLANO DE CORTE (peça de 220 corre no eixo de 275)')
print('  Chapa 1  pivotante face 1   116 cm   sobra 69')
print('  Chapa 2  pivotante face 2   116 cm   sobra 69')
print('  Chapa 3  correr face 1       88 cm   sobra 97')
print('  Chapa 4  correr face 2       88 cm   sobra 97')
print('  Chapa 5  painel fixo 1    120,5 cm   sobra 64,5')
print('  Chapa 6  painel fixo 2    120,5 cm   sobra 64,5')
N_CHAPAS = 6
print(f'  → {N_CHAPAS} chapas · área útil {area:.2f} m² em {N_CHAPAS*CHAPA_AREA:.2f} m² '
      f'({area/(N_CHAPAS*CHAPA_AREA)*100:.0f}%)')
print('  Os 2 painéis fixos já saíam em 2 tiras na REV.04 porque 241 cm não cabe na chapa.')
print('  Agora a emenda deixou de ser emenda: virou a junta entre duas peças do projeto.')

fita = perim*1.10
cava = ALTURA*2                                   # cava vertical nas 2 portas
rodape_m = 6.0                                    # 4,45 m de vão → 2 barras de 3 m
sarrafo = sum(2*(ALTURA+l)*(1.3 if f == 2 else 1.2) for _, l, f, _ in PECAS)

print(f'\nFita {fita:.1f} m · cava usinada {cava:.1f} m · rodapé {rodape_m:.0f} m '
      f'(2 barras de 3 m p/ {VAO_TOTAL:.2f} m) · sarrafo {sarrafo:.1f} m')

# ── ferragens ────────────────────────────────────────────────────────────────
N_DOBR = 4                                        # pivotante 116 → 66 kg, reforçada
print('\nFERRAGENS')
print(f'  Pivotante   {N_DOBR} × Häfele IN600 (invisível) ..... R$ {N_DOBR*P_DOBR_IN600:>8,.2f}')
print(f'              1 × fechadura ⚠ estimativa ........... R$ {P_FECHADURA:>8,.2f}')
print(f'  Correr      1 × RO82 top (duplo amortecimento) ... R$ {P_RO82_TOP:>8,.2f}')
print(f'              1 × trilho RO82 2 m ................. R$ {P_TRILHO_2M:>8,.2f}')
print('              sem fechadura, conforme definido')

c_chapa   = N_CHAPAS*P_CHAPA
c_fita    = fita*P_FITA_M
c_cava    = cava*P_CAVA_M
c_rodape  = rodape_m*P_RODAPE_M
c_sarrafo = sarrafo*P_SARRAFO_M
c_ferr    = N_DOBR*P_DOBR_IN600 + P_FECHADURA + P_RO82_TOP + P_TRILHO_2M

print('\n' + '─'*84)
LIN = [('MDF Itapuã Ultra 15 mm', f'{N_CHAPAS} chapas × R$ {P_CHAPA:.0f}', c_chapa),
       ('Fita de borda',          f'{fita:.1f} m × R$ {P_FITA_M:.2f}',      c_fita),
       ('Cava usinada',           f'{cava:.1f} m × R$ {P_CAVA_M:.2f}',      c_cava),
       ('Rodapé alumínio fosco 30 mm', f'{rodape_m:.0f} m × R$ {P_RODAPE_M:.2f}', c_rodape),
       ('Estrutura interna (sarrafo)', f'{sarrafo:.1f} m × R$ {P_SARRAFO_M:.2f}', c_sarrafo),
       ('Ferragens',              'IN600 · fechadura · RO82 top · trilho',  c_ferr)]
for d, q, v in LIN: print(f'  {d:<32}{q:<34}R$ {v:>9,.2f}')
MAT = sum(v for _, _, v in LIN)
LOG, VIS = 300.0, 200.0
fixedR = MAT + LOG + VIS
print(f'  {"Subtotal material":<66}R$ {MAT:>9,.2f}')
print(f'  {"Logística · visita técnica":<66}R$ {LOG+VIS:>9,.2f}')
print(f'  {"CUSTO DIRETO":<66}R$ {fixedR:>9,.2f}')

# ── preço ────────────────────────────────────────────────────────────────────
a_, liqF_, b_, MC = 0.162, 0.88, 0.043, 0.37
div = 1 - a_ - liqF_*b_ - MC
inv = fixedR/div
print('\n' + '═'*84)
print(f'PREÇO — MC {MC*100:.0f}%, sem RT · divisor {div:.5f}')
print('═'*84)
print(f'  Motor:  R$ {fixedR:,.2f} ÷ {div:.5f} = R$ {inv:,.2f}   →  R$ {round(inv/100)*100:,.0f}')
print(f'  REV.04 entregue (escopo antigo)                        R$ {14500:>9,.0f}')
print()
for base, rot in ((14500, 'mantendo o valor entregue'), (round(inv/100)*100, 'pelo motor, escopo novo')):
    print(f'  {rot:<40} tabela R$ {base:>8,.0f}   −10% → R$ {round(base*0.9/100)*100:>8,.0f}')
print()
mc_14500 = 1 - a_ - liqF_*b_ - fixedR/(14500*0.9)
print(f'  A R$ 13.050 (14.500 −10%) a MC real vira {mc_14500*100:.1f}%.')
print('  Pagamento 50% + 50% · entrega até 45 dias corridos.')
