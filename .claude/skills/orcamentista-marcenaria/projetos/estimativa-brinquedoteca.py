# -*- coding: utf-8 -*-
"""BRINQUEDOTECA — Eliza e Luiz Gustavo · arq. Helena Antunes  [30/09/2026]

⚠⚠ ISTO NÃO É UM ORÇAMENTO. É UMA ESTIMATIVA DE ORDEM DE GRANDEZA.

  A base de custos da Valvic (dados/materiais.json) é de MARCENARIA. Este job
  é ~60% serralheria estrutural, estofaria técnica e pintura automotiva —
  três ofícios sem uma única linha na nossa base. Todo custo marcado ★ é
  ADOÇÃO MINHA, sem cotação. São 11 dos 16 grupos.

  Ver `2026-brinquedoteca-eliza-luiz-gustavo.md` para a análise de risco.

ESCOPO [Jonathan 30/09, por mensagem — AINDA SEM MEMORIAL ESCRITO]
  · paredes coloridas e de tijolinho em MDF ultra premium, cruas, para o
    cliente pintar depois, TODAS estruturadas em serralheria
  · toda a serralheria é nossa: passarela, gradil com corda, plataformas
    acolchoadas, escadas com forração de espuma, piscina de espuma
  · passarela e gradil com PINTURA AUTOMOTIVA
  · banco extenso · janelas com frisos decorativos
  · cozinha de brinquedo — custo SEPARADO
"""
from collections import defaultdict
import motor_mc as M

# ── geometria lida das pranchas (PR01 a PR08) ────────────────────────────
AREA_PISO   = 33.68          # m², declarado na PR01
VAO         = (8.165, 4.125) # m — PR01
PD          = (2.15, 2.55, 3.66)
REDE_M2     = 3.97           # declarado na PR04
POCO_M2     = 2.535*2.425    # PR03 — 6,15 m²
BANCO_M     = 5.53           # PR03 — extensão do banco
PASSAR_M    = 5.53           # passarela ao longo da mesma parede
PLATAF      = 5              # PR08: +0,57 · +1,14 · +1,71 · +2,28 · +2,85
CASINHA     = (2.85, 1.70)   # PR03 — frente × prof
TUNEL_M     = 3.60           # PR03/PR05 — vão de 360 com cobertura em arco
ESCALADA_M2 = 2.425*2.45     # parede de escalada

# ── PAREDES: área revestida em MDF ultra sobre estrutura metálica ────────
# ★ estimativa por perímetro × altura média, descontando aberturas e o que
#   é alvenaria aparente. As pranchas não trazem quadro de áreas de parede.
PERIM   = 2*(VAO[0] + VAO[1])            # 24,58 m
H_MEDIA = 2.80                            # ★ média entre 2,15 / 2,55 / 3,66
PAREDE_M2 = PERIM*H_MEDIA*0.72            # ★ 72% — desconta vãos e aberturas
CASINHA_M2 = (CASINHA[0]*2.85)*2 + CASINHA[1]*2.85*2   # ★ fachada dupla face

# ══ CUSTOS UNITÁRIOS ═════════════════════════════════════════════════════
# ✓ = existe na base da casa · ★ = ADOÇÃO MINHA, sem cotação
CH_AREA = 2.75*1.85
MDF_ULTRA_18 = 320.0   # ★ MDF Ultra cru p/ pintura — a base só tem melamínico
MDF_ULTRA_15 = 260.0   # ★
COMPENSADO_18 = 200.0  # ✓ base (compensado 18)
FITA         = 2.0     # ✓

SERR_PAREDE_M2  = 190.0   # ★ montante metalon 40×40 a cada 60 cm + travessas
SERR_PASSAR_M2  = 780.0   # ★ estrutura que RECEBE PESSOAS: perfil 60×40 ch.2
SERR_PLAT_UN    = 950.0   # ★ plataforma estruturada, por unidade
SERR_ESCADA_M   = 620.0   # ★ escada metálica com forração, por metro
SERR_GRADIL_M   = 480.0   # ★ gradil com corda
PINT_AUTO_M2    = 220.0   # ★ cabine, primer, base, verniz
ESPUMA_PISC_M2  = 2100.0  # ★ blocos + fundo acolchoado, piscina completa
ACOLCH_M2       = 300.0   # ★ espuma D23 + courvin costurado
CORDA_M         = 45.0    # ★ corda náutica 16 mm com alma + conectores
REDE_M2_C       = 700.0   # ★ rede de poliamida para mezanino, instalada
TELA_M2         = 250.0   # ★ tela de proteção
AGARRA_UN       = 38.0    # ★ agarra de escalada
VINILICO_M2     = 120.0   # ★ piso vinílico
TAPETE_M2       = 180.0   # ★ tapete emborrachado
ACRILICO_M2     = 480.0   # ★ fechamento em acrílico
LED_M           = 150.0   # ✓ base

G = []   # (grupo, item, detalhe, custo, base?)
def a(g, item, det, v, base=False): G.append((g, item, det, v, base))

# ══ 1 · PAREDES CENOGRÁFICAS ═════════════════════════════════════════════
ch_par = -(-int((PAREDE_M2 + CASINHA_M2)/(CH_AREA*0.80)*100)//100)
a('Paredes', 'MDF ultra premium (cru, p/ pintura do cliente)',
  f'{PAREDE_M2+CASINHA_M2:.1f} m² → {ch_par} chapas', ch_par*MDF_ULTRA_18)
a('Paredes', 'Estrutura de serralheria das paredes',
  f'{PAREDE_M2+CASINHA_M2:.1f} m²', (PAREDE_M2+CASINHA_M2)*SERR_PAREDE_M2)
a('Paredes', 'Fita de borda e acabamento de junta',
  f'{(PAREDE_M2+CASINHA_M2)*2.2:.0f} m', (PAREDE_M2+CASINHA_M2)*2.2*FITA)

# ══ 2 · CASINHA — esquadria cenográfica ══════════════════════════════════
# PR03/05/07: vão porta 60×140 · vão janelinha 60×80/60 · janelinha fechada
# 60×80/60 · porta/janelinha 45×140/60 · porta fake · molduras · floreira
a('Casinha', 'Janelas com frisos decorativos e portinhas fixas',
  '4 conjuntos de esquadria cenográfica', 4*1450.0)
a('Casinha', 'Porta fake com peitoril fixo e molduras de janela',
  'PR07/PR08', 2200.0)
a('Casinha', 'Floreira, letreiro e toldo da fachada', 'PR05 vista B', 1800.0)
a('Casinha', 'Nicho profundo e nicho raso, portas de giro',
  'PR07/PR08 · 2 un', 1600.0)

# ══ 3 · PASSARELA E ESTRUTURA DE CIRCULAÇÃO ══════════════════════════════
a('Circulação', 'Passarela em serralheria estruturada',
  f'{PASSAR_M:.1f} m × 0,60', PASSAR_M*0.60*SERR_PASSAR_M2)
a('Circulação', 'Laje do mezanino — estrado metalon + chapa MDF',
  f'{REDE_M2+4.5:.1f} m²', (REDE_M2+4.5)*SERR_PASSAR_M2*0.75)
a('Circulação', 'Piso vinílico sobre a laje',
  f'{REDE_M2+4.5:.1f} m²', (REDE_M2+4.5)*VINILICO_M2)
a('Circulação', 'Gradil com corda, estrutura metálica',
  f'{PASSAR_M+3.6:.1f} m', (PASSAR_M+3.6)*SERR_GRADIL_M)
a('Circulação', 'Corda náutica do gradil',
  f'{(PASSAR_M+3.6)*6:.0f} m', (PASSAR_M+3.6)*6*CORDA_M)
a('Circulação', 'Plataformas acolchoadas estruturadas',
  f'{PLATAF} un (+0,57 a +2,85)', PLATAF*SERR_PLAT_UN)
a('Circulação', 'Escada/rampa com forração de espuma',
  '2 lances · PR03 e PR04', 2*2.6*SERR_ESCADA_M)

# ══ 4 · PINTURA AUTOMOTIVA ═══════════════════════════════════════════════
M2_PINT = PASSAR_M*0.60*2.4 + (PASSAR_M+3.6)*1.1 + PLATAF*0.9 + 2*2.6*1.4
a('Pintura', 'Pintura automotiva da serralheria aparente',
  f'★ {M2_PINT:.1f} m² de superfície desenvolvida', M2_PINT*PINT_AUTO_M2)

# ══ 5 · ESPUMA E ACOLCHOAMENTO ═══════════════════════════════════════════
a('Espuma', 'Piscina de espuma acolchoada',
  f'{POCO_M2:.2f} m² · blocos + fundo', POCO_M2*ESPUMA_PISC_M2)
a('Espuma', 'Acolchoamento das plataformas',
  f'{PLATAF*0.9:.1f} m²', PLATAF*0.9*ACOLCH_M2)
a('Espuma', 'Forração de espuma das escadas e rampa',
  f'{2*2.6*1.4:.1f} m²', 2*2.6*1.4*ACOLCH_M2)
a('Espuma', 'Acolchoamento de paredes em zona de queda',
  f'★ {12.0:.1f} m² — NÃO está na prancha, ver RISCO 2', 12.0*ACOLCH_M2)

# ══ 6 · BRINQUEDOS INTEGRADOS ════════════════════════════════════════════
a('Brinquedos', 'Túnel escorregador com cobertura em arco',
  f'{TUNEL_M:.1f} m · MDF curvado sobre gabarito + estrutura', 8900.0)
a('Brinquedos', 'Parede de escalada — painel e agarras',
  f'{ESCALADA_M2:.1f} m² · ~40 agarras',
  ESCALADA_M2*SERR_PAREDE_M2 + 40*AGARRA_UN + 1200.0)
a('Brinquedos', 'Escada horizontal (monkey bars)', 'PR05/PR06', 2400.0)
a('Brinquedos', 'Balanço sob viga, com fixação', 'PR03', 1300.0)
a('Brinquedos', 'Rede flexível do mezanino, instalada',
  f'{REDE_M2:.2f} m²', REDE_M2*REDE_M2_C)
a('Brinquedos', 'Telas de proteção',
  '★ ~14 m² · perímetro do mezanino e do túnel', 14.0*TELA_M2)
a('Brinquedos', 'Fechamento em acrílico', '★ ~2,2 m²', 2.2*ACRILICO_M2)

# ══ 7 · MOBILIÁRIO ═══════════════════════════════════════════════════════
a('Mobiliário', 'Banco extenso',
  f'{BANCO_M:.2f} m × 0,50 · estrutura + assento acolchoado',
  BANCO_M*0.50*SERR_PASSAR_M2*0.55 + BANCO_M*0.50*ACOLCH_M2)
a('Mobiliário', 'Mesinha e 4 banquinhos infantis', 'PR03', 2600.0)
a('Mobiliário', 'Painel imantado', f'{1.925*1.2:.1f} m²', 1.925*1.2*620.0)
a('Mobiliário', 'Painel com bobina de papel e organizadores',
  'PR03 · 0,60 de profundidade', 2900.0)
a('Mobiliário', 'Prateleiras/degraus e nichos em MDF', 'PR05 vista A', 3400.0)

# ══ 8 · PISOS E ARREMATES ════════════════════════════════════════════════
a('Arremates', 'Tapete emborrachado', f'★ ~{12.0:.0f} m²', 12.0*TAPETE_M2)
a('Arremates', 'LED e instalação', '★ ~14 m', 14.0*LED_M)

# ══ 9 · COZINHA DE BRINQUEDO — CUSTO SEPARADO ════════════════════════════
COZINHA = [
  ('Corpo, bancada e frentes em MDF ultra premium', 3*MDF_ULTRA_18 + 260.0),
  ('Ferragem, puxadores e acessórios lúdicos',       900.0),
  ('Pintura e acabamento',                           850.0),
  ('Mão de obra de marcenaria e montagem',          1400.0),
]

# ══ CONSOLIDAÇÃO ═════════════════════════════════════════════════════════
CD_DIRETO = sum(v for _, _, _, v, _ in G)

# logística e instalação — job de 2 pavimentos, obra longa
CARRETO, DIARIA, VISITA = 150.0, 260.0, 275.0
LOG = 6*CARRETO + 18*DIARIA + 4*VISITA      # ★ 18 dias de equipe no local
CONSUM = CD_DIRETO*0.04                      # consumível sobre um job misto
ART = 3800.0                                 # ★ projeto estrutural + ART

CD_SEM_EMB = CD_DIRETO + LOG + CONSUM + ART
CD = CD_SEM_EMB*(1 + M.EMBALAGEM)
CD_COZ = sum(v for _, v in COZINHA)*(1 + M.EMBALAGEM)

# ── margem ───────────────────────────────────────────────────────────────
BASE = M.base(parcelas=0, rt=False, vendedor=False)     # sem RT, sem comissão
MC_MARCENARIA = 0.38          # o que a casa pratica num job que conhece
MC_ESTE       = 0.48          # ★ ver "margem de segurança" no dossiê
CONTING       = 0.15          # ★ contingência sobre o custo

if __name__ == '__main__':
    br = lambda v: f'{v:,.0f}'.replace(',', '.')
    W = 94
    print('═'*W)
    print('BRINQUEDOTECA · Eliza e Luiz Gustavo — ESTIMATIVA DE ORDEM DE GRANDEZA')
    print('═'*W)
    print(f'\n⚠ NÃO É ORÇAMENTO. {sum(1 for g in G if not g[4])} de {len(G)} linhas '
          f'são adoção sem cotação (★).')
    print(f'\nEspaço: {AREA_PISO} m² de piso · pé-direito {PD[0]}–{PD[2]} m · dois níveis')
    print(f'Parede cenográfica estimada: {PAREDE_M2+CASINHA_M2:.1f} m²'
          f'   (perímetro {PERIM:.1f} m × {H_MEDIA} m × 72%, + casinha)')

    por = defaultdict(float)
    for g, *_r in G: por[g] += _r[2]
    print('\n' + '─'*W)
    for grupo in dict.fromkeys(g for g, *_ in G):
        print(f'\n  {grupo.upper():<44}{br(por[grupo]):>12}'
              f'{por[grupo]/CD_DIRETO*100:>7.1f}%')
        for g, item, det, v, base in G:
            if g != grupo: continue
            print(f'    {"✓" if base else "★"} {item:<52}{br(v):>10}')
            print(f'      {det}')
    print('─'*W)
    print(f'  {"CUSTO DOS SISTEMAS":<44}{br(CD_DIRETO):>12}')
    print(f'  {"+ logística e 18 dias de equipe":<44}{br(LOG):>12}')
    print(f'  {"+ consumíveis (4%)":<44}{br(CONSUM):>12}')
    print(f'  {"+ projeto estrutural e ART":<44}{br(ART):>12}')
    print(f'  {"+ embalagem (2%)":<44}{br(CD-CD_SEM_EMB):>12}')
    print(f'  {"= CUSTO DIRETO":<44}{br(CD):>12}')

    print(f'\n{"─"*W}\nPREÇO — BASE {BASE*100:.2f}% (à vista, sem RT, sem comissão)')
    print(f'{"":<46}{"preço":>12}{"MC R$":>12}')
    for rot, mc, cd in (
        (f'MC {MC_MARCENARIA:.0%} — o que a casa pratica', MC_MARCENARIA, CD),
        (f'MC {MC_ESTE:.0%} — margem de segurança deste job', MC_ESTE, CD),
        (f'MC {MC_ESTE:.0%} + contingência de {CONTING:.0%} no custo',
         MC_ESTE, CD*(1+CONTING))):
        p = round(cd/(BASE-mc)/100)*100
        print(f'  {rot:<44}{br(p):>12}{br(p*BASE-cd):>12}')

    p_rec = round(CD*(1+CONTING)/(BASE-MC_ESTE)/100)*100
    p_coz = round(CD_COZ/(BASE-MC_ESTE)/100)*100
    print(f'\n{"─"*W}')
    print(f'  BRINQUEDOTECA (recomendado)  custo {br(CD*(1+CONTING)):>9}   '
          f'venda {br(p_rec):>9}')
    print(f'  COZINHA DE BRINQUEDO         custo {br(CD_COZ):>9}   '
          f'venda {br(p_coz):>9}   ← separado')
    print(f'  {"":<29}{"":>9}   {"TOTAL":>5} {br(p_rec+p_coz):>9}')
    print(f'\n  R$/m² de piso: {(p_rec+p_coz)/AREA_PISO:,.0f}'.replace(',', '.'))
