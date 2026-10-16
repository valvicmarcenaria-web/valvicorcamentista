# -*- coding: utf-8 -*-
"""SANDRA DUARTE — rack da sala  [14/10/2026]

Prancha única A1, **arquiteta JUNIA ORDONES**, outubro/26, escala 1/25.
Residencial. ⛔ "AS MEDIDAS DEVERÃO SER CONFERIDAS NO LOCAL" e "CONFERIR
MEDIDAS E PONTO DE ENERGIA NO LOCAL PARA CONFIRMAR CORTES ANTES DA
PRODUÇÃO".

O MÓVEL — um rack, SOLTO do painel existente, sobre rodízios ocultos, e
  ⭐ [Jonathan 16/10] um PAINEL DE TV LISO de 142 de largura, apoiado no
  rodapé, cobrado À PARTE por R$ 2.300 — preço dele, conferido por mim.
  138 de largura × 35 de profundidade × 80 de altura (corpo de 70 sobre
  base de 10), e uma prateleira superior que chega a 83.

  A frente, da planta BB:  3 + 17 + 3 + 112 + 3 = 138
    · nicho de 17 em MDF, ABERTO À FRENTE
    · vão de 112 fechado por DUAS PORTAS DE GIRO EM VIDRO de 6 mm
    · prateleira interna em vidro de 6 ou 8 mm sobre pinos de metal
  Em cima: TAMPO EM VIDRO de 10 mm (135 × 35) com bisotê de 1,5 na frente
    e na lateral esquerda, lapidado reto no fundo.
  Acima dele, PRATELEIRA EM MDF (59 × 35) apoiada na lateral que sobe e
    num suporte de metal tubular champagne fixado no fundo.
  Fita de LED 4,8 W/m 2700 K em perfil de alumínio com difusor leitoso,
    em CAVA no tampo inferior, aos fundos, voltada para o fundo.

AS CHAPAS
  **MDF GUARARAPES LINHA METALIC, cor CHAMPAGNE** — ⭐ [Jonathan 14/10]
  **R$ 600 a chapa**, o MESMO preço do MDF de cor comum da base. O maior ★
  do orçamento caiu: o padrão champagne não cobra prêmio de chapa.
  **VIDRO TEMPERADO REFLECTA CHAMPAGNE** — 6, 8 e 10 mm.

⛔⛔ TUDO EM 30 mm — laterais, fundos, base, tampo inferior, nicho e
   prateleira. **MDF não existe em 30 mm**: é chapa dupla colada. Dobra a
   área de chapa de TODO o corpo, e em chapa cara.

⭐ [Jonathan 14/10] **MC 30% e COM RT.** ⚠ 30% está ABAIXO do piso da
casa (35%) — é instrução dele, fica registrado.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')
vg  = lambda v, n=2: f'{v:.{n}f}'.replace('.', ',')

CH_M2, APROV = 2.75*1.85, 0.80
MC_ALVO = 0.30                        # ⭐ [Jonathan 14/10] ⚠ abaixo do piso (35%)
RT_ON   = True                        # ⭐ [Jonathan 14/10] "adicione a RT"
BASE = M.base(parcelas=0, rt=RT_ON, vendedor=False)

# ── insumos ──────────────────────────────────────────────────────────────
# ⭐ [Jonathan 14/10] "A CHAPA CUSTA 600,00". Eu havia estimado R$ 1.150
#   — quase o dobro. A Metalic Champagne custa o MESMO que o MDF de cor
#   comum de 18 mm da base da casa: o acabamento premium não cobra prêmio
#   de chapa. Some o maior ★ do orçamento.
METALIC_15 = 600.0     # ⭐ chapa Guararapes Metalic Champagne [Jonathan 14/10]
BR_15      = 260.0     # Branco TX 15 — a camada interna da chapa dupla
FITA_M     = 3.0 + 2.5 # fita de cor + filetagem

VIDRO = {6: 320.0, 8: 390.0, 10: 480.0}   # ★ temperado reflecta, R$/m²
BISOTE_M   = 90.0      # ★ bisotê de 1,5 cm, por metro
LAPID_M    = 25.0      # ★ lapidação reta, por metro
PERFIL_SLIM= 120.0     # ★ perfil de alumínio slim champagne, por m
LED_M      = 95.0      # ★ fita 4,8 W/m + perfil com difusor leitoso + cava
LED_FONTE  = 120.0     # ★ fonte, embutida na base
RODIZIO    = 45.0      # ★ rodízio giratório oculto
SUP_TUBO   = 180.0     # ★ suporte em metal tubular champagne
PINO       = 12.0      # ★ pino de metal champagne
DOBR_VIDRO = 85.0      # ★ dobradiça de porta de vidro em perfil
SILICONE   = 60.0      # ★ silicone estrutural entre vidro, metal e MDF

# ── as peças ─────────────────────────────────────────────────────────────
# ⛔ toda peça de 30 mm entra DUAS VEZES: a chapa dupla é a construção real.
# ⭐ A SEGUNDA CAMADA SÓ É METALIC ONDE AS DUAS FACES APARECEM. Onde uma
#   face não se vê — fundo, tampo inferior e base — o miolo vai em Branco
#   TX. É a mesma lógica que a arquiteta abre na nota do tampo posterior.
PCS = [  # (desc, c, l, q, faces_metalic de 2, fc)
 ('Lateral',                      70, 35, 2, 2, 2),
 ('Divisória do nicho',           70, 35, 1, 2, 2),
 ('Fundo',                       138, 70, 1, 1, 1),
 ('Tampo inferior · com a cava do LED', 138, 35, 1, 1, 2),
 ('Base de apoio · recuada, sobre rodízios', 118, 28, 1, 1, 1),
 ('Prateleira do nicho',          17, 32, 1, 2, 2),
 ('Prateleira superior',          59, 35, 1, 2, 2),
]
area_met = sum(c*l*q*fm/1e4 for _d, c, l, q, fm, _f in PCS)
area_br  = sum(c*l*q*(2-fm)/1e4 for _d, c, l, q, fm, _f in PCS)
fita_m   = sum(2*(c+l)*q/100*(0.75 if fc == 2 else 0.4)
               for _d, c, l, q, _fm, fc in PCS)
chapas    = -(-area_met/(CH_M2*APROV)//1)
chapas_br = -(-area_br/(CH_M2*APROV)//1) if area_br else 0

# ── o vidro ──────────────────────────────────────────────────────────────
TAMPO_L, TAMPO_P = 1.35, 0.35
PORTA_L, PORTA_A, N_PORTA = 0.56, 0.64, 2
PRAT_L, PRAT_P = 1.12, 0.32
a_tampo = TAMPO_L*TAMPO_P
a_porta = N_PORTA*PORTA_L*PORTA_A
a_prat  = PRAT_L*PRAT_P
m_bisote = TAMPO_L + TAMPO_P              # frente e lateral esquerda
m_lapid  = TAMPO_L                        # face posterior, reta
m_perfil = N_PORTA*2*(PORTA_L + PORTA_A)  # ★ enquadramento slim das portas

VID = {
 'Tampo em vidro de 10 mm':          a_tampo*VIDRO[10],
 'Portas de giro em vidro de 6 mm':  a_porta*VIDRO[6],
 'Prateleira interna em vidro de 8 mm': a_prat*VIDRO[8],
 'Bisotê de 1,5 cm · frente e lateral': m_bisote*BISOTE_M,
 'Lapidação reta · face posterior':  m_lapid*LAPID_M,
 '⭐ Perfil slim de enquadramento das portas': m_perfil*PERFIL_SLIM,
}
FER = {
 'Dobradiça de porta de vidro':      N_PORTA*2*DOBR_VIDRO,
 'Rodízio giratório oculto':         4*RODIZIO,
 'Suporte em metal tubular champagne': SUP_TUBO,
 'Pino de metal champagne':          8*PINO,
 'Silicone estrutural':              SILICONE,
}
LED = {
 'Fita 4,8 W/m 2700 K em perfil com difusor': 1.35*LED_M,
 'Fonte embutida na base':                    LED_FONTE,
}

CH_CUSTO   = chapas*METALIC_15 + chapas_br*BR_15
FITA_CUSTO = fita_m*FITA_M
CD_VID = sum(VID.values()); CD_FER = sum(FER.values()); CD_LED = sum(LED.values())
CD = ((CH_CUSTO + FITA_CUSTO)*1.06 + CD_VID + CD_FER + CD_LED)*(1 + M.EMBALAGEM)
PV = round(CD/(BASE - MC_ALVO)/10)*10

# ── e se a chapa não fosse Metalic ───────────────────────────────────────
# ⛔ O CONTRAFACTUAL VIROU DE LADO. Enquanto a Metalic era ★ R$ 1.150, a
#   pergunta era "quanto custa o padrão champagne". A R$ 600 ela EMPATA com
#   o MDF de cor comum da base — trocar por cor não economiza um centavo.
#   O único piso abaixo dela é o Branco TX, que é outro móvel.
PV_COR = round((((chapas*600.0 + chapas_br*BR_15) + FITA_CUSTO)*1.06
                + CD_VID + CD_FER + CD_LED)
               *(1 + M.EMBALAGEM)/(BASE - MC_ALVO)/10)*10
PV_BR  = round((((chapas+chapas_br)*BR_15 + FITA_CUSTO)*1.06
                + CD_VID + CD_FER + CD_LED)
               *(1 + M.EMBALAGEM)/(BASE - MC_ALVO)/10)*10

# ── ⭐ PAINEL DE TV  [Jonathan 16/10] ─────────────────────────────────────
# "painel de tv liso de 142 cm de largura, apoiado no rodapé (a se validar
#  a possibilidade de ser inteiro) — investimento 2.300"
#
# ⛔ O PREÇO É DELE, NÃO MEU. R$ 2.300 veio fechado. O que eu faço aqui é
#   conferir se ele cobre o custo e em que MC cai — e achar o degrau onde
#   deixa de cobrir.
# ⚠ A ALTURA NÃO VEIO. Mas, para a CHAPA, ela quase não importa: a peça
#   inteira toma uma chapa de pé e a sobra é um filete que não vira outro
#   painel. De 2,00 a 2,75 de altura é SEMPRE UMA CHAPA — e o preço anda só
#   o que anda a fita de borda. O degrau está em 2,75.
PAINEL_L   = 1.42       # ⭐ [Jonathan] 142 cm de largura
PAINEL_H   = 2.20       # ★ estimativa minha — a altura não veio
PAINEL_PV  = 2300.0     # ⭐ [Jonathan] investimento fechado por ele
CH_L, CH_C = 1.85, 2.75 # a chapa DE PÉ: 1,42 de largura cabe folgado no 1,85
FIXA_PAINEL = 180.0     # ★ estrutura de fixação, buchas e parafusos

# ⭐ A RESPOSTA DO "SE DÁ PARA SER INTEIRO": DÁ.
#   1,42 cabe no 1,85 da chapa, e sobra altura até 2,75. O painel sai de
#   UMA PEÇA SÓ, sem emenda, desde que não passe de 2,75 de altura.
INTEIRO = PAINEL_L <= CH_L and PAINEL_H <= CH_C

def painel_cd(h, dupla=False, chapa=METALIC_15):
    """Custo direto do painel. `dupla` = 30 mm, chapa colada como o rack."""
    ch = chapa + (BR_15 if dupla else 0)     # ⛔ uma chapa de pé por camada
    if h > CH_C:                             # não cabe inteiro: 2ª chapa
        ch += chapa + (BR_15 if dupla else 0)
    fita = 2*(PAINEL_L + h)*FITA_M*(2 if dupla else 1)
    return ((ch + fita)*1.06 + FIXA_PAINEL)*(1 + M.EMBALAGEM)

CD_PAINEL = painel_cd(PAINEL_H)
MC_PAINEL = BASE - CD_PAINEL/PAINEL_PV       # a MC que o preço dele entrega
TOTAL = PV + PAINEL_PV

if __name__ == '__main__':
    W = 88
    print('═'*W)
    print('SANDRA DUARTE — RACK  ·  arquiteta Junia Ordones  ·  outubro/26')
    print(f'MC {MC_ALVO*100:.0f}% ⭐ · COM RT ⭐ · base {BASE*100:.2f}%'
          f'   ⚠ a MC está abaixo do piso da casa ({M.MC_PISO:.0%})')
    print('═'*W)
    print(f'\n{"PEÇA · chapa dupla de 15 + 15":<42}{"medida":>12}'
          f'{"Metalic":>10}{"Branco":>9}')
    print('─'*W)
    for d, c, l, q, fm, _f in PCS:
        print(f'{d:<42}{f"{c} × {l}":>12}{c*l*q*fm/1e4:>10.2f}'
              f'{c*l*q*(2-fm)/1e4:>9.2f}')
    print('─'*W)
    print(f'{"ÁREA, em m²":<42}{"":>12}{area_met:>10.2f}{area_br:>9.2f}')
    print(f'{"CHAPAS":<42}{"":>12}{chapas:>10.0f}{chapas_br:>9.0f}')
    print(f'  ⭐ {chapas:.0f} de Metalic a R$ {br(METALIC_15)} + {chapas_br:.0f} de Branco TX '
          f'a R$ {br(BR_15)} = R$ {br(CH_CUSTO)}')
    print('  ⛔⛔ O PROJETO PEDE 30 mm EM TODO O CORPO, e MDF não existe em')
    print('    30 mm: é chapa dupla colada. Dobra a área de chapa do móvel.')
    print('    ⭐ Mas só metade precisa ser Metalic: onde uma face não')
    print('      aparece — fundo, tampo inferior e base — o miolo vai em')
    print('      Branco TX, e ninguém vê a diferença.')
    _tudo = -(-(area_met+area_br)/(CH_M2*APROV)//1)*METALIC_15
    print(f'    Em Metalic nas duas camadas seriam R$ {br(_tudo)} — '
          f'R$ {br(_tudo-CH_CUSTO)} a mais.')

    print(f'\n{"═"*W}')
    print('O VIDRO TEMPERADO REFLECTA CHAMPAGNE')
    print(f'{"═"*W}')
    for k, v in VID.items(): print(f'  {k:<48}R$ {br(v):>8}')
    print(f'  {"":<48}{"─"*11}')
    print(f'  {"":<48}R$ {br(CD_VID):>8}')
    print(f'\n  ⚠ A prancha deixa EM ABERTO: "verificar a necessidade de')
    print('    enquadrar as portas em perfis de alumínio slim". Orçei COM o')
    print(f'    perfil — R$ {br(m_perfil*PERFIL_SLIM)}. Sem ele a porta é vidro puro com')
    print('    dobradiça de pinça, e aí o puxador tem de ser FURO NO VIDRO.')

    print(f'\n{"═"*W}')
    print('FERRAGEM E ILUMINAÇÃO')
    print(f'{"═"*W}')
    for k, v in list(FER.items()) + list(LED.items()):
        print(f'  {k:<48}R$ {br(v):>8}')

    print(f'\n{"═"*W}')
    print('O INVESTIMENTO')
    print(f'{"═"*W}')
    print(f'  {"chapa Metalic":<34}R$ {br(CH_CUSTO):>9}')
    print(f'  {"fita de borda e filetagem":<34}R$ {br(FITA_CUSTO):>9}')
    print(f'  {"consumíveis · 6%":<34}R$ {br((CH_CUSTO+FITA_CUSTO)*0.06):>9}')
    print(f'  {"vidro, bisotê e perfil":<34}R$ {br(CD_VID):>9}')
    print(f'  {"ferragem":<34}R$ {br(CD_FER):>9}')
    print(f'  {"iluminação":<34}R$ {br(CD_LED):>9}')
    print(f'  {"embalagem · 2%":<34}R$ {br(CD/(1+M.EMBALAGEM)*M.EMBALAGEM):>9}')
    print('  ' + '─'*46)
    print(f'  {"CUSTO DIRETO":<34}R$ {br(CD):>9}')
    print(f'  {"PREÇO":<34}R$ {br(PV):>9}')
    print(f'\n  ⭐ Agora o VIDRO é o maior insumo: {CD_VID/CD*100:.0f}% do custo direto,')
    print(f'    contra {CH_CUSTO/CD*100:.0f}% de chapa. Com a Metalic a R$ {br(METALIC_15)}, a maior')
    print('    incerteza do orçamento passou a ser a VIDRAÇARIA — é lá que')
    print('    a cotação tem de bater agora.')
    print(f'\n  ⭐ E A METALIC CHAMPAGNE NÃO COBRA PRÊMIO NENHUM. A R$ {br(METALIC_15)} ela')
    print(f'    EMPATA com o MDF de cor comum da base: o mesmo rack em cor')
    print(f'    comum daria os mesmos R$ {br(PV_COR)}. Trocar o padrão que a arquiteta')
    print('    especificou não economiza um centavo — não há o que negociar aí.')
    print(f'    Só o corpo todo em Branco TX desceria, para R$ {br(PV_BR)}, e aí é')
    print(f'    outro móvel: {br(PV-PV_BR)} de diferença para perder o champagne inteiro.')

    print(f'\n{"═"*W}')
    print('⭐ PAINEL DE TV — ITEM À PARTE  [Jonathan 16/10]')
    print(f'{"═"*W}')
    print(f'  Liso, 142 de largura, apoiado no rodapé, no mesmo padrão '
          f'champagne.')
    print(f'  ⛔ O investimento é DELE: R$ {br(PAINEL_PV)}. Abaixo eu só confiro.')
    print(f'\n  {"chapa · 1 Metalic de pé":<34}R$ {br(METALIC_15):>9}')
    print(f'  {"fita de borda e filetagem":<34}'
          f'R$ {br(2*(PAINEL_L+PAINEL_H)*FITA_M):>9}')
    print(f'  {"estrutura de fixação":<34}R$ {br(FIXA_PAINEL):>9}')
    print(f'  {"consumíveis e embalagem":<34}'
          f'R$ {br(CD_PAINEL - METALIC_15 - 2*(PAINEL_L+PAINEL_H)*FITA_M - FIXA_PAINEL):>9}')
    print('  ' + '─'*46)
    print(f'  {"CUSTO DIRETO":<34}R$ {br(CD_PAINEL):>9}')
    print(f'  {"PREÇO ⭐ dele":<34}R$ {br(PAINEL_PV):>9}')
    print(f'  {"MC que esse preço entrega":<34}{MC_PAINEL*100:>10.1f}%')
    print(f'\n  ⭐ R$ {br(PAINEL_PV)} ESTÁ BOM: entrega MC de {MC_PAINEL:.1%}, DENTRO da faixa')
    print(f'    ideal da casa ({M.MC_IDEAL[0]:.0%}–{M.MC_IDEAL[1]:.0%}) — e acima dos {MC_ALVO:.0%} do rack.')

    print(f'\n  ⭐ "A SE VALIDAR A POSSIBILIDADE DE SER INTEIRO" — DÁ.')
    print(f'    A chapa é 2,75 × 1,85. De pé, os 1,42 de largura cabem')
    print(f'    folgados no 1,85, e sobra altura até 2,75. O painel sai de')
    print(f'    UMA PEÇA SÓ, sem emenda — {"confirmado" if INTEIRO else "⛔ NÃO CABE"} na altura de '
          f'{vg(PAINEL_H)} que estimei.')
    print(f'    ⭐ E a altura quase não mexe no preço: de 2,00 a 2,75 é')
    print(f'      SEMPRE UMA CHAPA, e só a fita de borda anda.')

    print(f'\n  ⚠ ONDE R$ {br(PAINEL_PV)} DEIXA DE COBRIR — os dois degraus:')
    _alto = painel_cd(2.95)
    _dupla = painel_cd(PAINEL_H, dupla=True)
    print(f'    · ALTURA ACIMA DE 2,75 — entra uma 2ª chapa e uma emenda.')
    print(f'      Custo direto vai a R$ {br(_alto)} e a MC cai para '
          f'{(BASE-_alto/PAINEL_PV)*100:.1f}%.')
    print(f'    · PAINEL EM 30 mm, chapa dupla como o resto do móvel.')
    print(f'      Custo direto vai a R$ {br(_dupla)} e a MC cai para '
          f'{(BASE-_dupla/PAINEL_PV)*100:.1f}%.')
    print(f'    Orçei LISO, em chapa simples, apoiado no rodapé — que é o')
    print(f'    que ele pediu. Os dois degraus são aviso, não orçamento.')

    print(f'\n{"═"*W}')
    print(f'  {"RACK":<34}R$ {br(PV):>9}')
    print(f'  {"PAINEL DE TV":<34}R$ {br(PAINEL_PV):>9}')
    print(f'  {"INVESTIMENTO TOTAL":<34}R$ {br(TOTAL):>9}')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print(f'  · ⭐ O PREÇO DA CHAPA METALIC FECHOU: R$ {br(METALIC_15)} [Jonathan 14/10].')
    print('    Eu havia estimado R$ 1.150 — quase o dobro. Saiu o maior ★ do')
    print('    orçamento, e com ele R$ 550 de chapa. ⭐ Vale atualizar a base')
    print('    da casa: a Metalic Champagne empata com o MDF de cor comum.')
    print('  · ⛔⛔ FURO DE 3 cm EM VIDRO TEMPERADO. A prancha oferece')
    print('    "puxador tipo furo de 3 cm OU alumínio slim colado". ⚠ Furo em')
    print('    temperado tem de ser feito ANTES da têmpera — depois não se')
    print('    fura, e a peça não se reaproveita. E a mesma prancha manda')
    print('    CONFERIR AS MEDIDAS NO LOCAL antes de cortar. As duas coisas')
    print('    não cabem juntas: ou a medida está fechada antes do vidro, ou')
    print('    o puxador é o slim colado. ⭐ Recomendo o SLIM COLADO.')
    print('  · ⚠ O ENQUADRAMENTO DAS PORTAS. A prancha pergunta e não responde.')
    print('    Orçei COM perfil slim. Decide construção, puxador e preço.')
    print('  · ★ O vidro reflecta champagne também é estimado. Cotar junto')
    print('    com o bisotê, que é serviço de vidraceiro, não nosso.')
    print('  · ⭐ "O tampo posterior em MDF não é necessariamente no padrão')
    print('    Metalic Champagne" — a própria arquiteta abre essa porta. Em')
    print('    chapa comum ali, economiza-se sem aparecer.')
    _srt = M.base(parcelas=0, rt=False, vendedor=False)
    print(f'  · ⭐ RT DE 10% INCLUÍDO [Jonathan 14/10], para a arquiteta Junia')
    print(f'    Ordones. Sem ela o rack sairia a '
          f'R$ {br(round(CD/(_srt-MC_ALVO)/10)*10)} — o RT vale')
    print(f'    R$ {br(PV - round(CD/(_srt-MC_ALVO)/10)*10)}.')
    print(f'  · ⚠ A MC DE {MC_ALVO:.0%} ESTÁ ABAIXO DO PISO DA CASA ({M.MC_PISO:.0%}) '
          f'[Jonathan 14/10].')
    _p35 = round(CD/(BASE-0.35)/10)*10
    print(f'    A 35% o rack sairia a R$ {br(_p35)} — a queda de margem devolve')
    print(f'    R$ {br(_p35-PV)} ao cliente e tira o mesmo da casa. Fica registrado.')
    print('  · ⚠ A ALTURA DO PAINEL NÃO VEIO. Não mexe no preço enquanto')
    print('    ficar abaixo de 2,75 — mas decide se ele sai inteiro. Medir.')
    print('  · ⚠ O PAINEL EXISTENTE. O projeto trazia o rack SOLTO dele; agora')
    print('    vendemos um painel novo. Se o novo SUBSTITUI o atual, a')
    print('    RETIRADA do atual não está no preço. Confirmar com a Sandra.')
    print('  · "CONFERIR MEDIDAS E PONTO DE ENERGIA NO LOCAL": o ponto de')
    print('    energia é da elétrica, mas a fonte do LED fica embutida na')
    print('    nossa base — ela precisa de tomada alcançável e de manutenção.')
