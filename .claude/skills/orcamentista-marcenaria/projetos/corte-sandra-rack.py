# -*- coding: utf-8 -*-
"""SANDRA DUARTE — rack da sala  [14/10/2026]

Prancha única A1, **arquiteta JUNIA ORDONES**, outubro/26, escala 1/25.
Residencial. ⛔ "AS MEDIDAS DEVERÃO SER CONFERIDAS NO LOCAL" e "CONFERIR
MEDIDAS E PONTO DE ENERGIA NO LOCAL PARA CONFIRMAR CORTES ANTES DA
PRODUÇÃO".

O MÓVEL — um rack só, SOLTO do painel existente, sobre rodízios ocultos.
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
  **MDF GUARARAPES LINHA METALIC, cor CHAMPAGNE** — ⛔ não está na base da
  casa. É linha premium; estimada abaixo e é o maior ★ do orçamento.
  **VIDRO TEMPERADO REFLECTA CHAMPAGNE** — 6, 8 e 10 mm.

⛔⛔ TUDO EM 30 mm — laterais, fundos, base, tampo inferior, nicho e
   prateleira. **MDF não existe em 30 mm**: é chapa dupla colada. Dobra a
   área de chapa de TODO o corpo, e em chapa cara.

★ Sem instrução de MC e de RT. Adotei **MC 35% e sem RT**, como no Sigma.
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
MC_ALVO = 0.35                        # ★ adotado
RT_ON   = True                        # ⭐ [Jonathan 14/10] "adicione a RT"
BASE = M.base(parcelas=0, rt=RT_ON, vendedor=False)

# ── insumos ──────────────────────────────────────────────────────────────
# ⛔⛔ A LINHA METALIC NÃO ESTÁ NA BASE DA CASA. A base traz MDF de cor a
#   R$ 500 (15 mm) e R$ 600 (18 mm). A Metalic é acabamento especial —
#   estimada em ~2,3× a chapa de cor. É o maior ★ deste orçamento.
METALIC_15 = 1150.0    # ★ chapa 15 mm Guararapes Metalic Champagne
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
PV_COR = round((((chapas+chapas_br)*600.0 + FITA_CUSTO)*1.06 + CD_VID + CD_FER + CD_LED)
               *(1 + M.EMBALAGEM)/(BASE - MC_ALVO)/10)*10

if __name__ == '__main__':
    W = 88
    print('═'*W)
    print('SANDRA DUARTE — RACK  ·  arquiteta Junia Ordones  ·  outubro/26')
    print(f'MC {MC_ALVO*100:.0f}% ★ · COM RT ⭐ · base {BASE*100:.2f}%')
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
    print(f'  ⛔ {chapas:.0f} de Metalic a ★ R$ {br(METALIC_15)} + {chapas_br:.0f} de Branco TX '
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
    print(f'\n  ⭐ A chapa é {CH_CUSTO/CD*100:.0f}% do custo direto e o vidro é '
          f'{CD_VID/CD*100:.0f}%.')
    print(f'    Juntos, {(CH_CUSTO+CD_VID)/CD*100:.0f}% — e os dois são ★ estimados.')
    print(f'\n  ⭐ E A METALIC CHAMPAGNE SAI BARATA NESTE MÓVEL. Em MDF de')
    print(f'    cor comum o rack daria R$ {br(PV_COR)} — a linha premium custa só')
    print(f'    R$ {br(PV-PV_COR)} a mais, {PV/PV_COR-1:.0%} do preço. O móvel é pequeno e, com')
    print('    o miolo em Branco TX, UMA chapa de Metalic resolve. É um bom')
    print('    argumento: o acabamento que a arquiteta especificou quase não')
    print('    pesa, e trocá-lo por chapa comum não compra quase nada.')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print(f'  · ⛔⛔ O PREÇO DA CHAPA METALIC. ★ R$ {br(METALIC_15)} é estimativa minha —')
    print('    a linha não está na base da casa. É a maior incerteza do')
    print('    orçamento e precisa de cotação antes de qualquer proposta.')
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
    print(f'    R$ {br(PV - round(CD/(_srt-MC_ALVO)/10)*10)}. ★ A MC de 35% continua adotada por mim.')
    print('  · "CONFERIR MEDIDAS E PONTO DE ENERGIA NO LOCAL": o ponto de')
    print('    energia é da elétrica, mas a fonte do LED fica embutida na')
    print('    nossa base — ela precisa de tomada alcançável e de manutenção.')
