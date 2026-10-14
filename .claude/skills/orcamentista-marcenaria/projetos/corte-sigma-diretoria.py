# -*- coding: utf-8 -*-
"""SIGMA — sala de diretoria, Belo Horizonte  [14/10/2026]

Projeto: **BRAZ ARQUITETURA & INTERIORES**, executivo, outubro 2026,
16 pranchas A2. Cliente **Reginaldo**. Sala de **477 × 300**.
⛔ "*confirmar todas as medidas no local" e "conferir pé-direito no local"
   em TODAS as pranchas.

⭐ [Jonathan 14/10] MC de 35% · sem RT · corrediças ocultas.

AS CHAPAS DO PROJETO — todas Arauco, melamínico de cor
  MDF **JEQUITIBÁ** · MDF **GRAFITO** · MDF **LINO** (só no móvel 06)

O ESCOPO, pela planta de layout
  01 · APARADOR .......... 174 × 75 × 50, quatro portas em TELA DE BAMBU
  02 · PRATELEIRAS ....... três suspensas de 30 de profundidade, com LED
  03 · MESA DO DIRETOR ... 175 × 60 × 75, gaveteiro de quatro gavetas
  ⛔ 04 · MESA REDONDA com quatro cadeiras, "modelo a definir" — é
         MOBILIÁRIO SOLTO, não marcenaria. Não entra.
  05 · MÓVEL DO CAFÉ ..... 300 × 276 × 50 — estante de nove nichos com
         LED, espaço de frigobar e adega, e armário fechado de 100 com
         cofre e cinco gavetas
  06 · ADORNO DE PAREDE .. duas peças orgânicas em MDF Lino,
         RETROILUMINADAS, e uma prateleira suspensa

⛔ O QUE NÃO É NOSSO: a mesa redonda e as cadeiras, as poltronas, o tapete,
   o frigobar, a adega, O COFRE, a cortina de rolo, o piso vinílico, a
   pintura e as luminárias de teto. Da iluminação de marcenaria fazemos
   fita, perfil e usinagem; fonte, driver e circuito são da elétrica.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')

CH_M2, APROV = 2.75*1.85, 0.80
PRECO   = {6: 300.0, 15: 500.0, 18: 600.0}     # MDF cor — base da casa
FITA_M  = 3.0 + 2.5
MC_ALVO = 0.35          # ⭐ [Jonathan 14/10]
RT_ON   = False         # ⭐ [Jonathan 14/10]
BASE    = M.base(parcelas=0, rt=RT_ON, vendedor=False)

# ── ferragem e terceiros ────────────────────────────────────────────────
# ⚠ [Jonathan 14/10] "nossa dobradiça custa 12,00". A base da casa lança
#   R$ 35 (com amortecedor). Numa sala de diretoria o amortecimento é
#   esperado, então orçei com a da base — e o print mostra o que a simples
#   economizaria, para a decisão ser do Jonathan.
DOBR_AMORT, DOBR_SIMPLES = 35.0, 12.0
CORR_OCULTA = 190.0     # ★ Hettich oculta — AINDA NÃO COTADA
SUP_INV     = 60.0      # ★ suporte invisível de prateleira
PASSA_CABO  = 45.0      # ★ passador com tampa plástica preta
BAMBU_M2    = 480.0     # ★ TELA DE BAMBU aplicada em porta — ver EM ABERTO
CURVA_M2    = 420.0     # ★ recorte orgânico em CNC + fita flexível
LED_M       = 85.0      # ★ fita + perfil + usinagem + instalação, por metro

PCS, FER, TER, LED = {}, {}, {}, {}
FER_UN = {'dobr': DOBR_AMORT, 'corr': CORR_OCULTA, 'supinv': SUP_INV}
def amb(k):
    PCS.setdefault(k, []); TER.setdefault(k, 0.0); LED.setdefault(k, 0.0)
    FER.setdefault(k, dict.fromkeys(FER_UN, 0))
def a(k, esp, desc, c, l, q=1, fc=2):
    amb(k); PCS[k].append((esp, desc, c, l, q, fc))
def f(k, **kw):
    amb(k)
    for key, v in kw.items(): FER[k][key] += v
def ter(k, v): amb(k); TER[k] += v
def led(k, m): amb(k); LED[k] += m

# ══ 01 · APARADOR  174 × 75 × 50 ══════════════════════════════════════════
# Corpo de 65 em Jequitibá sobre sóculo de 10 em Grafito, tampo em Grafito.
# Quatro portas com TELA DE BAMBU, de ~43 de largura.
K = '01 · Aparador'
a(K,15,'Lateral',                  65,  50, 2)
a(K,15,'Base e tampo',            170,  50, 2)
a(K,15,'Divisória vertical',       65,  50, 1)
a(K,15,'Prateleira interna',       84,  50, 2)
a(K, 6,'Fundo',                   174,  65, 1, 1)
a(K,18,'Porta · moldura',          65,  43, 4)
a(K,15,'Sóculo',                  174,  10, 2)
a(K,15,'Sóculo · lateral',         50,  10, 2)
f(K, dobr=8)                       # duas por folha, folha de 65
ter(K, 4*0.35*0.57*BAMBU_M2)       # ★ tela de bambu nas quatro portas

# ══ 02 · PRATELEIRAS SUSPENSAS  três de 174 × 30 × 3 ═════════════════════
K = '02 · Prateleiras suspensas'
a(K,15,'Prateleira · duas camadas', 174, 30, 6)
f(K, supinv=9)
led(K, 3*1.74)                     # ⭐ fita sob cada prateleira

# ══ 03 · MESA DO DIRETOR  175 × 60 × 75 ═════════════════════════════════
# Tampo e pé em Jequitibá; gaveteiro de 35 com quatro gavetas em Grafito.
K = '03 · Mesa do diretor'
a(K,18,'Tampo',                   175,  60, 1)
a(K,18,'Testeira do tampo',       175,   5, 1)
a(K,18,'Testeira do tampo',        60,   5, 2)
a(K,18,'Pé · painel lateral',      75,  60, 1)
a(K,15,'Gaveteiro · lateral',      65,  60, 2)
a(K,15,'Gaveteiro · base e topo',  32,  60, 2)
a(K, 6,'Gaveteiro · fundo',        35,  65, 1, 1)
a(K,18,'Frente de gaveta',         34,  16, 4)
a(K,15,'Gaveta · lateral',         55,  13, 8, 1)
a(K,15,'Gaveta · frente e fundo',  30,  13, 8, 1)
a(K,15,'Gaveta · fundo',           30,  55, 4, 1)
a(K,15,'Sóculo do gaveteiro',      35,  10, 2)
f(K, corr=4)
ter(K, 2*PASSA_CABO)               # ★ dois passadores de cabo

# ══ 05 · MÓVEL DO CAFÉ  300 × 276 × 50 ═══════════════════════════════════
# Estante de 200 + armário fechado de 100. Corpo em Grafito, prateleiras e
# frentes do armário em Jequitibá.
K = '05 · Móvel do café'
# — estante de 200
a(K,15,'Lateral',                 276,  50, 2)
a(K,15,'Montante interno',        276,  50, 2)
a(K,15,'Prateleira · duas camadas', 40, 50, 16)   # 4 níveis × 2 vãos de 40
a(K,15,'Prateleira · duas camadas',120, 50, 8)    # 4 níveis × vão de 120
a(K, 6,'Fundo da estante',        200, 276, 1, 1)
a(K,15,'Base da parte baixa',     196,  50, 1)
a(K,15,'Divisória da parte baixa', 76,  50, 3)
a(K,15,'Prateleira do nicho',      89,  50, 1)
a(K,15,'Sóculo',                  149,  10, 2)    # ⛔ não há sóculo no frigobar
# — armário fechado de 100
a(K,15,'Armário · lateral',       276,  50, 2)
a(K,15,'Armário · base e topo',    96,  50, 2)
a(K,15,'Armário · prateleira',     96,  50, 4)
a(K,15,'Armário · divisória baixa',100,  50, 1)
a(K, 6,'Armário · fundo',         100, 276, 1, 1)
a(K,18,'Armário · porta de giro',  266, 48, 2)
a(K,18,'Frente de gaveta',         47,  18, 4)
a(K,18,'Frente de gavetão',        47,  26, 1)
a(K,15,'Gaveta · lateral',         45,  15, 10, 1)
a(K,15,'Gaveta · frente e fundo',  43,  15, 10, 1)
a(K,15,'Gaveta · fundo',           43,  45, 5, 1)
a(K,15,'Armário · sóculo',        100,  10, 2)
f(K, dobr=8, corr=5)               # porta de 266 pede quatro dobradiças
led(K, 4*2.00)                     # ⭐ fita em cada um dos quatro níveis

# ══ 06 · ADORNO DE PAREDE + PRATELEIRA ═══════════════════════════════════
# Duas peças orgânicas em MDF Lino, retroiluminadas, e prateleira de 81.
K = '06 · Adorno de parede'
a(K,18,'Peça orgânica maior',      105,  60, 1)
a(K,18,'Peça orgânica menor',       88,  64, 1)
a(K,15,'Estrutura de afastamento',  80,  10, 4, 1)
a(K,15,'Prateleira · duas camadas', 81,  20, 2)
f(K, supinv=3)
ter(K, (1.05*0.60 + 0.88*0.64)*CURVA_M2)   # ★ recorte orgânico e fita flexível
led(K, 1.05*2 + 0.88*2)            # ⭐ retroiluminação das duas peças

AMBS = list(PCS)

# ══════════════════════════════════════════════════════════════════════════
def calcula(dobr):
    area, ch, fita, area_k = {}, {}, {}, {}
    for k in AMBS:
        ch[k] = fita[k] = 0.0
        for esp, _, c, l, q, fc in PCS[k]:
            area[esp] = area.get(esp, 0.0) + c*l*q/1e4
            fita[k] += 2*(c+l)*q/100*(0.75 if fc == 2 else 0.4)*FITA_M
    chapas   = {e: -(-v/(CH_M2*APROV)//1) for e, v in area.items()}
    custo_ch = {e: chapas[e]*PRECO[e] for e in chapas}
    taxa = {e: PRECO[e]/(CH_M2*APROV) for e in area}
    for k in AMBS:
        area_k[k] = sum(c*l*q/1e4 for _, _, c, l, q, _ in PCS[k])
        ch[k] = sum(c*l*q/1e4*taxa[esp] for esp, _, c, l, q, _ in PCS[k])
    sobra = sum(custo_ch.values()) - sum(area[e]*taxa[e] for e in area)
    at = sum(area_k.values())
    for k in AMBS: ch[k] += sobra*area_k[k]/at
    fer_c = {k: (FER[k]['dobr']*dobr + FER[k]['corr']*CORR_OCULTA
                 + FER[k]['supinv']*SUP_INV) for k in AMBS}
    CDI = {k: ((ch[k] + fita[k])*1.06 + fer_c[k] + TER[k])*(1 + M.EMBALAGEM)
           for k in AMBS}
    PV  = {k: round(CDI[k]/(BASE - MC_ALVO)/10)*10 for k in AMBS}
    return dict(ch=ch, fita=fita, fer=fer_c, CDI=CDI, PV=PV, chapas=chapas,
                area=area, custo_ch=custo_ch, sobra=sobra,
                CD=sum(CDI.values()), TOT=sum(PV.values()))

R  = calcula(DOBR_AMORT)
RS = calcula(DOBR_SIMPLES)

LED_TOT = sum(LED.values())
LED_CD  = LED_TOT*LED_M*(1 + M.EMBALAGEM)
LED_PV  = round(LED_CD/(BASE - MC_ALVO)/10)*10
TOTAL   = R['TOT'] + LED_PV

if __name__ == '__main__':
    W = 92
    print('═'*W)
    print('SIGMA — SALA DE DIRETORIA  ·  Reginaldo  ·  Braz Arquitetura')
    print(f'MC {MC_ALVO*100:.0f}% · sem RT · corrediças ocultas · '
          f'base {BASE*100:.2f}%   [Jonathan 14/10]')
    print('═'*W)

    print(f'\n{"CHAPA":<12}{"área líq.":>12}{"chapas":>9}{"R$/chapa":>11}{"custo":>11}')
    print('─'*W)
    for e in sorted(R['area']):
        print(f'{e:>3} mm{"":<6}{br1(R["area"][e]):>10} m²{R["chapas"][e]:>9.0f}'
              f'{br(PRECO[e]):>11}{br(R["custo_ch"][e]):>11}')
    print('─'*W)
    print(f'{"TOTAL":<12}{br1(sum(R["area"].values())):>10} m²'
          f'{sum(R["chapas"].values()):>9.0f}{"":>11}'
          f'{br(sum(R["custo_ch"].values())):>11}')

    print(f'\n{"═"*W}')
    print(f'{"MÓVEL":<30}{"chapa":>9}{"fita":>8}{"ferr.+terc.":>13}'
          f'{"custo":>10}{"preço":>10}{"MC":>8}')
    print('─'*W)
    for k in AMBS:
        print(f'{k:<30}{br(R["ch"][k]):>9}{br(R["fita"][k]):>8}'
              f'{br(R["fer"][k]+TER[k]):>13}{br(R["CDI"][k]):>10}'
              f'{br(R["PV"][k]):>10}{(BASE-R["CDI"][k]/R["PV"][k])*100:>7.1f}%')
    print('─'*W)
    print(f'{"MARCENARIA":<30}{"":>9}{"":>8}{"":>13}{br(R["CD"]):>10}'
          f'{br(R["TOT"]):>10}{(BASE-R["CD"]/R["TOT"])*100:>7.1f}%')
    print(f'{"ILUMINAÇÃO · linha separada":<30}{"":>9}{"":>8}{"":>13}'
          f'{br(LED_CD):>10}{br(LED_PV):>10}')
    print('─'*W)
    print(f'{"INVESTIMENTO":<30}{"":>9}{"":>8}{"":>13}'
          f'{br(R["CD"]+LED_CD):>10}{br(TOTAL):>10}')

    print(f'\n{"═"*W}')
    print('⭐ ILUMINAÇÃO')
    print(f'{"═"*W}')
    print(f'  {br1(LED_TOT)} m de fita em perfil a R$ {br(LED_M)}/m ★')
    for k in AMBS:
        if LED[k]: print(f'    {k:<32}{br1(LED[k]):>7} m')
    print('  ⚠ Fonte, driver, circuito e interruptor são da elétrica.')

    print(f'\n{"═"*W}')
    print('⛔⛔ O TESTE DA HORA — esta obra é POUCA CHAPA E MUITA MÃO DE OBRA')
    print(f'{"═"*W}')
    HORAS = {'01 · Aparador': 26, '02 · Prateleiras suspensas': 8,
             '03 · Mesa do diretor': 22, '05 · Móvel do café': 92,
             '06 · Adorno de parede': 16}
    _mc = TOTAL - (R['CD'] + LED_CD) - TOTAL*(1 - BASE)
    _h = sum(HORAS.values())
    print(f'  {"":<30}{"preço":>10}{"horas ★":>10}{"MC/hora":>10}')
    print('  ' + '─'*62)
    for k in AMBS:
        _mck = R['PV'][k]*(BASE - R['CDI'][k]/R['PV'][k])
        print(f'  {k:<30}{br(R["PV"][k]):>10}{HORAS[k]:>10}'
              f'{br(_mck/HORAS[k]):>10}')
    print('  ' + '─'*62)
    print(f'  {"MARCENARIA":<30}{br(R["TOT"]):>10}{_h:>10}'
          f'{br((R["TOT"]*(BASE-R["CD"]/R["TOT"]))/_h):>10}')
    print(f'\n  ⛔ A casa já viu R$ 74 a R$ 133 de MC por hora em obra de')
    print('    marcenaria fina. Aqui a conta dá menos, e o motivo é')
    print('    estrutural: a MC é um PERCENTUAL DO PREÇO, e o preço nasce')
    print('    do MATERIAL. Numa obra de nove nichos, uma mesa e duas peças')
    print('    orgânicas em CNC, a chapa é pouca e a bancada é muita —')
    print(f'    {br1(sum(R["area"].values()))} m² de chapa para {_h} ★ horas de trabalho.')
    print('    ⭐ Não é erro do motor: é o modelo precificando material numa')
    print('      obra que vende hora. Se a fábrica estiver cheia, 35% aqui')
    print('      vale menos que 35% num roupeiro — e isso é decisão de')
    print('      agenda, não de orçamento.')
    print('    ★ As horas são MINHAS, por comparação com obras parecidas.')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print(f'  · ⛔⛔ A TELA DE BAMBU é o maior ★ do orçamento. Entrou a '
          f'R$ {br(BAMBU_M2)}/m²')
    print(f'    aplicada, sobre {br1(4*0.35*0.57)} m² nas quatro portas = '
          f'R$ {br(4*0.35*0.57*BAMBU_M2)} de custo.')
    print('    A casa tem base de PALHINHA (R$ 950/m² instalada, Jonathan')
    print('    09/10), não de tela de bambu — que é outro material e mais')
    print('    barato. ⚠ Precisa de cotação antes de fechar.')
    print(f'  · ⚠ A DOBRADIÇA. Orçada com amortecimento, a R$ {br(DOBR_AMORT)} — numa')
    print('    diretoria o amortecimento é esperado. [Jonathan 14/10] disse')
    print(f'    que a nossa custa R$ {br(DOBR_SIMPLES)}; com ela o total cairia para')
    print(f'    R$ {br(RS["TOT"]+LED_PV)}, R$ {br(TOTAL-RS["TOT"]-LED_PV)} a menos. A decisão é do Jonathan.')
    print(f'  · ⚠ A CORREDIÇA OCULTA entrou a R$ {br(CORR_OCULTA)} ★, o mesmo palpite do')
    print('    closet da Arthur & Yasmim — e segue sem cotação. São nove')
    print(f'    gavetas, R$ {br(9*CORR_OCULTA)} de compra.')
    print('  · ⛔ O COFRE do armário do móvel 05 é EQUIPAMENTO, não nosso.')
    print('    Fazemos o nicho; o cofre vem do cliente. O mesmo vale para o')
    print('    FRIGOBAR e a ADEGA — só o espaço é nosso.')
    print('  · ⛔ A MESA REDONDA (04) e as quatro cadeiras são "modelo a')
    print('    definir" na prancha: mobiliário solto, fora do orçamento.')
    print('  · ★ As PRATELEIRAS SUSPENSAS (02) não têm comprimento cotado na')
    print('    prancha. Adotei o mesmo do aparador, que é o que a projeção')
    print('    da planta mostra. A profundidade (30) e a espessura (3) estão.')
    print('  · ★ O ADORNO (06) tem as peças cotadas por envoltória, não por')
    print('    contorno. Orçei a área cheia do retângulo que as contém — é o')
    print('    que a chapa gasta de verdade, porque o recorte vira sobra.')
    print('  · ⚠ O PUXADOR é EMBUTIDO (cava usinada) no móvel 05. Nas demais')
    print('    frentes a prancha não especifica puxador — adotei cava também.')
    print('  · "CONFIRMAR TODAS AS MEDIDAS NO LOCAL" e "conferir pé-direito"')
    print('    estão em todas as pranchas. O móvel 05 tem 276 de altura: se o')
    print('    pé-direito vier menor, ele muda.')
