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
# ⭐⭐ [Jonathan 19/10] "adicione também a RT do projeto completo, mas a RT
#   precisa estar ALOCADA APENAS NO CUSTO DO PAINEL."
#   → O RACK sai da cascata SEM RT (base 85,35%), e a RT do projeto inteiro
#     — rack mais painel — é paga por dentro do preço do PAINEL.
#   ⛔ Isso NÃO muda o que a arquiteta recebe: a RT continua sendo 9,5% do
#     preço total. Muda de onde o dinheiro sai.
RT_ON   = False                       # ⭐ o rack, sem RT na cascata
RT_NO_PAINEL = True                   # ⭐ toda a RT do projeto, no painel
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

# ── ⭐ PAINEL DE TV  [Jonathan 16/10 · atualizado 19/10] ──────────────────
# 16/10: "painel de tv LISO de 142 cm de largura, apoiado no rodapé —
#         investimento 2.300"
# ⭐ 19/10: "vamos atualizar o painel para RIPADO com ripas de 2×2 e o valor
#           para R$ 7.500"
# ⭐ 19/10, depois: "vamos VOLTAR COM O PAINEL LISO, dessa vez acrescentando
#           DOIS FRISOS COM PERFIL LAQUEADO. A 3.100"
#
# ⛔ O PREÇO É DELE, NÃO MEU. O que eu faço aqui é conferir se cobre o custo
#   e em que MC cai.
# ⚠ A ALTURA CONTINUA SEM VIR. Para a chapa ela quase não importa: a peça
#   de pé toma uma chapa inteira e a sobra é um filete. O degrau está em
#   2,75 — acima disso entra uma segunda chapa e uma emenda.
PAINEL_L   = 1.42       # ⭐ [Jonathan] 142 cm de largura
PAINEL_H   = 2.20       # ★ estimativa minha — a altura não veio
PAINEL_PV  = 3900.0     # ⭐ [Jonathan 19/10] investimento fechado por ele
PERFIL_LAQ = 160.0      # ★ friso em perfil laqueado: perfil, rasgo e laca, por m
N_FRISO    = 2          # ⭐ [Jonathan 19/10] "dois frisos com perfil laqueado"
CH_L, CH_C = 1.85, 2.75 # a chapa DE PÉ: 1,42 de largura cabe folgado no 1,85
FIXA_PAINEL = 180.0     # ★ estrutura de fixação, buchas e parafusos
RIPA, VAO  = 2.0, 2.0   # ⭐ [Jonathan 19/10] ripas de 2×2
SERRA_RIPA = 1.10       # ★ perda de serra ao tirar ripa de 2 cm da chapa

# ⭐ O "SE DÁ PARA SER INTEIRO" CONTINUA VALENDO, e agora vale para a RIPA:
#   a chapa tem 2,75 de comprimento, então a ripa corre a altura toda sem
#   emenda enquanto o painel não passar de 2,75.
INTEIRO = PAINEL_L <= CH_L and PAINEL_H <= CH_C

def painel_parcelas(h, dupla=False, chapa=METALIC_15, ripado=False,
                    frisos=N_FRISO):
    """Custo direto do painel. `dupla` = 30 mm, chapa colada como o rack.

    ⛔⛔ O QUE ENCARECE O RIPADO NÃO É A CHAPA, É A FITA. A ripa de 2 cm sai
      da chapa com a face melamínica na frente e o MIOLO CRU nos dois lados
      — e os dois lados ficam à vista no vão entre as ripas. Cada ripa
      precisa de fita nas duas arestas longas, e são dezenas de ripas: dá
      MUITO mais metro de fita do que o painel liso inteiro tinha.
    """
    base = chapa + (BR_15 if dupla else 0)   # ⛔ uma chapa de pé por camada
    if h > CH_C:                             # não cabe inteiro: 2ª chapa
        base += chapa + (BR_15 if dupla else 0)
    fita_b = 2*(PAINEL_L + h)*FITA_M*(2 if dupla else 1)
    ch_ripa = fita_r = 0.0
    if ripado:
        # as ripas saem de chapa PRÓPRIA: a base já tomou a dela, de pé
        a_ripa = PAINEL_L*h*RIPA/(RIPA + VAO)*SERRA_RIPA
        ch_ripa = -(-a_ripa/(CH_M2*APROV)//1)*chapa
        fita_r = (PAINEL_L*100/(RIPA + VAO))*2*h*FITA_M
    friso = frisos*PAINEL_L*PERFIL_LAQ
    cons = (base + ch_ripa + fita_b + fita_r)*0.06
    sub  = base + ch_ripa + fita_b + fita_r + cons + friso + FIXA_PAINEL
    emb  = sub*M.EMBALAGEM
    return dict(chapa_base=base, chapa_ripa=ch_ripa, fita_base=fita_b,
                fita_ripa=fita_r, friso=friso, cons=cons, fixa=FIXA_PAINEL,
                emb=emb, total=sub + emb)

def painel_cd(h, **kw): return painel_parcelas(h, **kw)['total']

PP        = painel_parcelas(PAINEL_H)
CD_PAINEL = PP['total']
CD_SEM_FRISO = painel_cd(PAINEL_H, frisos=0)
TOTAL     = PV + PAINEL_PV

# ── ⭐ A RT DO PROJETO INTEIRO, PAGA DENTRO DO PAINEL ────────────────────
# A RT devida à arquiteta é 9,5% do preço de venda — 10% sobre o líquido,
# e o líquido é o bruto menos a nota. Sobre o TOTAL, não sobre o painel.
RT_RATE  = M.encargos(parcelas=0, rt=True, vendedor=False)['RT']
RT_TOTAL = RT_RATE*TOTAL if RT_NO_PAINEL else 0.0
# ⛔ A MC do painel é o que sobra DEPOIS de ele pagar a RT dos dois móveis.
MC_PAINEL = BASE - (CD_PAINEL + RT_TOTAL)/PAINEL_PV
# ⭐ e o preço que o painel precisaria ter para segurar a MC do rack
#   carregando a mesma RT:  PVp(B − mc) = CDp + rt·(PVr + PVp)
PV_PAINEL_30 = round((CD_PAINEL + RT_RATE*PV)/(BASE - MC_ALVO - RT_RATE)/10)*10
# ── a MC do conjunto ────────────────────────────────────────────────────
MC_CONJ = (TOTAL - (CD + CD_PAINEL) - RT_TOTAL - (1 - BASE)*TOTAL)/TOTAL

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
    print('⭐ PAINEL DE TV — ITEM À PARTE  [Jonathan 16/10 · liso com frisos 19/10]')
    print(f'{"═"*W}')
    print(f'  LISO, 142 de largura, apoiado no rodapé, no padrão champagne,')
    print(f'  com {N_FRISO} FRISOS EM PERFIL LAQUEADO.')
    print(f'  ⛔ O investimento é DELE: R$ {br(PAINEL_PV)}. Abaixo eu só confiro.')
    print(f'\n  {"chapa · uma Metalic de pé":<34}R$ {br(PP["chapa_base"]):>9}')
    print(f'  {"fita · bordas do painel":<34}R$ {br(PP["fita_base"]):>9}')
    print(f'  {f"⭐ {N_FRISO} frisos em perfil laqueado":<34}R$ {br(PP["friso"]):>9}')
    print(f'  {"estrutura de fixação":<34}R$ {br(PP["fixa"]):>9}')
    print(f'  {"consumíveis · 6%":<34}R$ {br(PP["cons"]):>9}')
    print(f'  {"embalagem · 2%":<34}R$ {br(PP["emb"]):>9}')
    print('  ' + '─'*46)
    print(f'  {"CUSTO DIRETO":<34}R$ {br(CD_PAINEL):>9}')
    print(f'  {"⭐ RT DO PROJETO INTEIRO":<34}R$ {br(RT_TOTAL):>9}')
    print('  ' + '─'*46)
    print(f'  {"a cobrir, no painel":<34}R$ {br(CD_PAINEL + RT_TOTAL):>9}')
    print(f'  {"PREÇO ⭐ dele":<34}R$ {br(PAINEL_PV):>9}')
    print(f'  {"MC que sobra no painel":<34}{MC_PAINEL*100:>10.1f}%')
    print(f'\n  ⭐ Os frisos são {PP["friso"]/CD_PAINEL*100:.0f}% do custo direto do painel: '
          f'de R$ {br(CD_SEM_FRISO)}')
    print(f'    sem eles para R$ {br(CD_PAINEL)} com eles, R$ {br(CD_PAINEL-CD_SEM_FRISO)} a mais.')

    print(f'\n{"═"*W}')
    print('⭐⭐ A RT DO PROJETO INTEIRO, ALOCADA SÓ NO PAINEL  [Jonathan 19/10]')
    print(f'{"═"*W}')
    print(f'  A RT devida à arquiteta é {RT_RATE:.1%} do preço de venda — 10% sobre o')
    print(f'  líquido, e o líquido é o bruto menos a nota. Sobre o TOTAL de')
    print(f'  R$ {br(TOTAL)}, dá R$ {br(RT_TOTAL)}.')
    print(f'\n  ⛔ ISSO NÃO MUDA O QUE A ARQUITETA RECEBE. Muda de onde sai: o')
    print(f'    rack passa a ser precificado SEM RT na cascata (base '
          f'{BASE*100:.2f}%)')
    print(f'    e o painel paga a conta dos dois.')
    print(f'\n  {"RACK · MC alvo":<34}{MC_ALVO*100:>9.1f}%   R$ {br(PV):>8}')
    print(f'  {"PAINEL · MC que sobra":<34}{MC_PAINEL*100:>9.1f}%   R$ {br(PAINEL_PV):>8}')
    print(f'  {"CONJUNTO":<34}{MC_CONJ*100:>9.1f}%   R$ {br(TOTAL):>8}')
    print(f'\n  ⚠⚠ O PAINEL FICA COM {MC_PAINEL:.1%} DE MC — ele carrega sozinho uma RT')
    print(f'    que é de R$ {br(TOTAL)} de projeto. E o CONJUNTO cai para '
          f'{MC_CONJ:.1%},')
    print(f'    contra os {MC_ALVO:.0%} do rack e os {M.MC_PISO:.0%} de piso da casa.')
    print(f'    ⭐ Para o painel segurar {MC_ALVO:.0%} carregando a mesma RT, o preço')
    print(f'      dele teria de ser R$ {br(PV_PAINEL_30)} — R$ {br(PV_PAINEL_30-PAINEL_PV)} acima dos '
          f'R$ {br(PAINEL_PV)}.')
    print(f'    ⛔ Não é erro de conta: é o efeito de concentrar num item a')
    print(f'      comissão do projeto inteiro. Fica registrado.')

    print(f'\n{"═"*W}')
    print(f'  {"RACK · sem RT":<34}R$ {br(PV):>9}')
    print(f'  {"PAINEL DE TV · liso com frisos":<34}R$ {br(PAINEL_PV):>9}')
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
    print(f'  · ⭐ A RT DE 10% CONTINUA NO PROJETO, mas agora SÓ NO PAINEL')
    print(f'    [Jonathan 19/10], para a arquiteta Junia Ordones. São')
    print(f'    R$ {br(RT_TOTAL)} sobre o total, pagos por dentro do painel — o rack')
    print(f'    saiu da cascata com RT e por isso caiu de R$ '
          f'{br(round(CD/(M.base(0, True, False)-MC_ALVO)/10)*10)} para R$ {br(PV)}.')
    print(f'  · ⚠ A MC DE {MC_ALVO:.0%} ESTÁ ABAIXO DO PISO DA CASA ({M.MC_PISO:.0%}) '
          f'[Jonathan 14/10].')
    _p35 = round(CD/(BASE-0.35)/10)*10
    print(f'    A 35% o rack sairia a R$ {br(_p35)} — a queda de margem devolve')
    print(f'    R$ {br(_p35-PV)} ao cliente e tira o mesmo da casa. Fica registrado.')
    print('  · ⚠ A ALTURA DO PAINEL NÃO VEIO. Não mexe no preço enquanto')
    print('    ficar abaixo de 2,75 — mas decide se ele sai inteiro. Medir.')
    print(f'  · ★ O FRISO EM PERFIL LAQUEADO está estimado em R$ {br(PERFIL_LAQ)}/m,')
    print('    com perfil, usinagem do rasgo e laca. Não está na base da casa')
    print('    e é 34% do custo direto do painel — vale cotar.')
    print('  · ⚠ O PAINEL EXISTENTE. O projeto trazia o rack SOLTO dele; agora')
    print('    vendemos um painel novo. Se o novo SUBSTITUI o atual, a')
    print('    RETIRADA do atual não está no preço. Confirmar com a Sandra.')
    print('  · "CONFERIR MEDIDAS E PONTO DE ENERGIA NO LOCAL": o ponto de')
    print('    energia é da elétrica, mas a fonte do LED fica embutida na')
    print('    nossa base — ela precisa de tomada alcançável e de manutenção.')
