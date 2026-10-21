# -*- coding: utf-8 -*-
"""BRINQUEDOTECA · Eliza e Luiz Gustavo — v2, com a separação do Jonathan

[Jonathan 30/09] "precisamos ser mais realista, acho que vc superestimou
muito os custos" + a lista de 11 itens.

⛔ OS DOIS ERROS QUE EU CARREGAVA E QUE INFLAVAM TUDO

1 · USEI PREÇO DE VENDA COMO CUSTO DE MÃO DE OBRA.
    Marcenaria a R$ 65/h é o que se COBRA. Marceneiro com encargos custa
    R$ 36/h. Serralheria idem. Isso sozinho inflava ~R$ 12 mil.

2 · CALCULEI A SUPERFÍCIE DE PINTURA SOBRE A ÁREA EM PLANTA × 2,6.
    Chute em cima de chute. O certo é PERÍMETRO DO PERFIL × METRO LINEAR:
    metalon 60×40 tem 0,20 m de perímetro, então 1 m de perfil = 0,20 m² de
    superfície. A passarela caiu de 8,63 m² para 4,45 m² de pintura.

    E R$ 220/m² é preço de peça pequena e detalhada. Estrutura de metalon em
    lote pinta a R$ 120/m².

3 · A SELAGEM SAI. O Jonathan foi claro: as paredes entregam CRUAS, o
    acabamento é escolha e responsabilidade da cliente. Eu estava cobrando
    preparo de superfície num escopo que não tem preparo.
"""
import math
from collections import defaultdict
import motor_mc as M

# ══ INSUMOS — revisados para custo real de compra ════════════════════════
BARRA = 6.0
# ⭐ [Jonathan 21/10] "as paredes terão infraestrutura em serralheria com
#   metalon 50×30 em CHAPA 16". Chapa 16 é 1,5 mm; a 18 é 1,2. Mais grossa,
#   mais rígida — e é o que sustenta a ponte suspensa e a grade de cordas.
MET = {'50x30x1,2':(95.,0.160), '50x30x1,5':(118.,0.160),
       '40x40x1,5':(122.,0.160),
       '60x40x2,0':(210.,0.200), '30x30x1,2':(62.,0.120)}   # (R$/barra, perím. m)
PAREDE_PERFIL = '50x30x1,5'        # ⭐ chapa 16 [Jonathan 21/10]
mL   = lambda p: MET[p][0]/BARRA
perim= lambda p: MET[p][1]

MO_SERR_REP = 12.0   # ★ R$/m — peça repetitiva (parede): 45 m/dia
MO_SERR_EST = 26.0   # ★ R$/m — estrutural/complexo: 18 m/dia
MO_MARC_H   = 36.0   # ★ R$/h — marceneiro COM encargos (era 65, que é venda)
CONSUM_S    = 0.07
CHUMB, CHUMB_EST = 4.20, 9.24
PARAF_M2    = 4.90

MDF_U18, MDF_U15 = 280.0, 225.0   # ★ MDF ultra premium cru
COMP_PLAST18 = 240.0              # ★ compensado plastificado (uso seco)
COMP_NAV18   = 380.0              # ★ naval só onde há umidade/carga
FORMICA_M2   = 96.0               # ★ laminado + cola de contato
LACA_M2      = 210.0              # ★ laca branca aplicada (fundo + 2 demãos)

PINT_AUTO    = 120.0              # ★ R$/m² de superfície REAL, em lote
ESP = {'D23':820., 'D28':960., 'D33':1100.}   # ★ R$/m³ de placa
COURVIN, COSTURA = 52.0, 55.0     # ★ R$/m²
# ⭐ [Jonathan 14/10] o BANCO sai do courvin náutico e passa a estofado em
#   TECIDO (linho). ⚠ Tecido de linho em brinquedoteca mancha e não se
#   limpa como PVC — ver EM ABERTO no dossiê.
TECIDO_M2     = 95.0              # ★ linho para estofaria, por m²
# ⭐ [Jonathan 14/10] a ESCADA da casinha sai do aço e passa a MDF com
#   revestimento emborrachado. Sem metalon e sem pintura automotiva.
EMBORRACHADO  = 130.0             # ★ manta emborrachada aplicada, por m²
CORDA_COMB = 62.0                 # ★ combinada 16 mm, nacional
CABO_PERIM = 38.0                 # ★ cabo de aço 6 mm + esticador

# ⭐⭐ [Jonathan 21/10] AS TELAS DE PROTEÇÃO VIRAM MALHA DE CORDA NÁUTICA
#   "malha de cordas náuticas de 8 mm com 10 cm entre nós, com alguns fios
#    de cabo de aço de 3 mm entrelaçados para garantir mais resistência.
#    Para a estrutura suspensa será aplicado DUPLAMENTE, para diminuir o
#    espaço entre nós e garantir mais segurança. Fixadas com GANCHOS
#    SOLDADOS."
# ⛔ O custo do item deixa de ser uma tela comprada por m² e passa a ser
#   CORDA + CABO + GANCHO + TECELAGEM. A tecelagem é nó a nó: é mão de obra,
#   e é ela que manda no preço, não a corda.
CORDA_NAU8 = 8.50     # ★ corda náutica 8 mm, por metro
CABO_ACO3  = 6.50     # ★ cabo de aço 3 mm, por metro
GANCHO_SOL = 7.20     # ★ gancho soldado e acabado, por unidade
MALHA_MO   = 120.0    # ★ tecelagem nó a nó e tensionamento, por m²
NO_CM      = 10.0     # ⭐ [Jonathan] 10 cm entre nós
CABO_CM    = 50.0     # ★ um cabo de aço entrelaçado a cada 50 cm
GANCHO_CM  = 20.0     # ★ gancho a cada 20 cm no perímetro (10 na malha dupla)

# ⭐ [Jonathan 21/10] MÃO DE OBRA de pintura acrílica e de papel de parede.
#   ⛔ O FORNECIMENTO DO MATERIAL É DO CONTRATANTE — tinta, massa e papel
#     não estão no nosso preço. Só a aplicação.
PINT_ACRIL = 130.0    # ⭐ [Jonathan 21/10] R$/m² de aplicação
PAPEL_MO   = 45.0     # ★ aplicação de papel de parede, R$/m²

# ⭐ [Jonathan 21/10] o BANCO ganha acabamento: MDF Berneck padrão TABASCO.
TABASCO_CH = 600.0    # ★ chapa melamínica Berneck Tabasco, 18 mm

# ⭐ [Jonathan 21/10] "adicione a possibilidade de ser laqueado, custo
#   adicional para laca fosca será de 8k" — adicional AO PREÇO, cravado.
LACA_FOSCA_PV = 8000.0

M2_PINTURA, M2_PAPEL = [], []     # preenchidos pelas paredes

def sup(perfil, metros): return perim(perfil)*metros   # m² de pintura

def malha(a_m2, perim_m, dupla=False):
    """Malha de corda náutica de 8 mm, nós a cada 10 cm, com cabo de aço de
    3 mm entrelaçado. `dupla` = duas malhas cruzadas na ESTRUTURA SUSPENSA,
    que divide o vão entre nós pela metade.
    ⛔ 1 m² de malha de 10 × 10 cm leva 20 m de corda: dez fios num
      sentido e dez no outro, cada um com 1 m. A conta é essa, e é ela que
      mostra por que uma tela de corda não é uma tela comprada por m²."""
    f = 2 if dupla else 1
    m_corda = a_m2*(100.0/NO_CM)*2*f
    m_cabo  = a_m2*(100.0/CABO_CM)*2*f
    n_gancho = math.ceil(perim_m/(GANCHO_CM/100.0))*f
    return m_corda, m_cabo, n_gancho

ITENS = []
def it(nome, dim, linhas, obs=''):
    t = sum(q*v for _,q,_,v in linhas)
    ITENS.append(dict(nome=nome, dim=dim, linhas=linhas, total=t, obs=obs))
    return t

# ══ 1 · PASSARELA SUSPENSA ═══════════════════════════════════════════════
Lp, Bp = 5.53, 0.60
n_tr = math.ceil(Lp/0.50)+1
m60 = 2*Lp + 4*0.85          # longarinas + mãos-francesas
m40 = n_tr*Bp
S = sup('60x40x2,0', m60) + sup('40x40x1,5', m40)
it('Passarela suspensa', f'{Lp:.2f} × {Bp:.2f} m, a +2,85 m', [
 ('Metalon 60×40×2,0 — 2 longarinas e 4 mãos-francesas',   m60,'m',mL('60x40x2,0')),
 (f'Metalon 40×40×1,5 — {n_tr} travessas a cada 50 cm',    m40,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria estrutural',            m60+m40,'m',MO_SERR_EST),
 ('Consumível de solda',      (m60+m40)*mL('60x40x2,0'),'vb',CONSUM_S),
 ('Chumbador estrutural 1/2"',                            16.0,'un',CHUMB_EST),
 ('Compensado naval 18 mm — piso (recebe carga)',          1.0,'ch',COMP_NAV18),
 (f'Pintura automotiva — {S:.2f} m² de superfície real',     S,'m²',PINT_AUTO),
], obs=f'{m60+m40:.1f} m de metalon · pintura por PERÍMETRO DO PERFIL, não por planta')

# ══ 2 · GRADIS DE CONTENÇÃO DAS REDES (com as cordas) ════════════════════
L_GR, H_GR, PASSO = 9.13, 1.10, 0.12
n_fios = math.ceil(H_GR/PASSO)
M_CORDA = n_fios*L_GR
m_gr = 2*L_GR + math.ceil(L_GR/1.2+1)*H_GR
S_gr = sup('50x30x1,2', m_gr)
A_TELA, PERIM_TELA = 14.0, 26.0
# ⭐ a malha continua calculada — não para entrar no preço, mas para eu
#   saber o tamanho do buraco entre o que a folha promete e o que a conta
#   paga. É esse número que vai para o dossiê e para a cotação.
_mc, _mb, _mg = malha(A_TELA, PERIM_TELA, dupla=True)
_MALHA_EST = (_mc*CORDA_NAU8 + _mb*CABO_ACO3 + _mg*GANCHO_SOL
              + A_TELA*MALHA_MO)
_MALHA_NA_CONTA = 14.0*250.0
it('Gradis de contenção das redes', f'{L_GR:.2f} × {H_GR:.2f} m · {n_fios} fios', [
 ('Metalon 50×30×1,2 — quadro e montantes',               m_gr,'m',mL('50x30x1,2')),
 ('Mão de obra de serralheria',                           m_gr,'m',MO_SERR_EST),
 ('Consumível de solda',         m_gr*mL('50x30x1,2'),'vb',CONSUM_S),
 (f'⭐ Corda combinada 16 mm (alma de aço) — {M_CORDA:.1f} m',
                                                       M_CORDA,'m',CORDA_COMB),
 ('Terminal, prensa-cabo e olhal',                    n_fios*2,'un',22.0),
 ('Passagem e tensionamento da corda',                 M_CORDA,'m',6.0),
 ('Chumbador',                                            14.0,'un',CHUMB),
 (f'Pintura automotiva — {S_gr:.2f} m²',                  S_gr,'m²',PINT_AUTO),
 # [Jonathan 30/09] a rede e as telas passam a ESTAR INCLUSAS
 ('Rede de descanso do mezanino — poliamida malha 4 cm',   3.97,'m²',320.0),
 ('Cabo de aço 6 mm no perímetro da rede',                 10.0,'m',CABO_PERIM),
 ('Esticador, sapatilha e grampo',                         16.0,'un',28.0),
 ('Chumbador estrutural da rede',                          18.0,'un',CHUMB_EST),
 ('Instalação e tensionamento da rede',                     8.0,'h',42.0),
 ('Metalon 30×30×1,2 — quadro das telas',                  26.0,'m',mL('30x30x1,2')),
 ('Mão de obra de serralheria das telas',                  26.0,'m',MO_SERR_REP),
 # ⭐⭐ [Jonathan 21/10] A TELA VIRA MALHA DE CORDA NÁUTICA — mas ele foi
 #   explícito depois: "o custo dos gradis de contenção NÃO É PARA MUDAR
 #   VALOR, é só para mudar texto. Valor será acrescentado apenas conforme
 #   solicitação." Então a linha mantém o MESMO valor da tela que havia, e
 #   só a descrição muda.
 # ⚠⚠ MINHA ESTIMATIVA POR COMPONENTE NÃO FECHA COM ESSE VALOR. Corda,
 #   cabo, gancho e tecelagem, pelas minhas taxas, dariam R$ {_MALHA_EST:,.0f}
 #   — contra os R$ {14*250:,.0f} desta linha. Ou as minhas taxas estão altas, ou
 #   a malha custa mais do que o orçamento paga. ⛔ COTAR ANTES DE FECHAR.
 ('⭐ Malha de corda náutica com cabo de aço entrelaçado, '
  'dupla na estrutura suspensa, em ganchos soldados',      14.0,'m²',250.0),
], obs=f'⭐ corda do gradil: {M_CORDA:.1f} m · ⭐ malha de corda náutica em '
       f'{A_TELA:.0f} m², valor mantido [Jonathan 21/10] · inclui a REDE')

# ══ 3 · PLATAFORMAS ACOLCHOADAS ══════════════════════════════════════════
Lpl, Bpl, Hpl, N_PL = 0.95, 0.60, 0.57, 5
m_pl = (2*(Lpl+Bpl) + 4*Hpl + 2*Bpl)*N_PL
S_pl = sup('40x40x1,5', m_pl)
A_pl = N_PL*Lpl*Bpl
it('Plataformas acolchoadas', f'{N_PL} un de {Lpl:.2f} × {Bpl:.2f} m', [
 ('Metalon 40×40×1,5 — quadro, pés e travamento',        m_pl,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                          m_pl,'m',MO_SERR_REP),
 ('Consumível de solda',        m_pl*mL('40x40x1,5'),'vb',CONSUM_S),
 ('Compensado plastificado 18 mm — base do tampo',       1.25,'ch',COMP_PLAST18),
 # ⭐ [Jonathan 21/10] "nas plataformas de subida do espaço de cordas …
 #   será utilizada espuma D33 de 20 mm. Tecido a ser definido."
 ('⭐ Espuma D33 de 20 mm — recebe pisada',         A_pl*0.02,'m³',ESP['D33']),
 ('⭐ Tecido de revestimento · a definir',           A_pl*2.1,'m²',TECIDO_M2),
 ('Corte, costura e grampeamento',                  A_pl*2.1,'m²',COSTURA),
 ('Chumbador',                                       N_PL*4.0,'un',CHUMB),
 (f'Pintura automotiva — {S_pl:.2f} m²',                 S_pl,'m²',PINT_AUTO),
], obs=f'{m_pl:.1f} m de metalon no conjunto · D33 porque a criança PISA em pé')

# ══ 4 · PISCINA DE ESPUMA — só a estrutura, sem os blocos ════════════════
A_PO, PROF = 2.535*2.425, 0.55
m_po = 2*(2.535+2.425)*2 + 8*PROF          # quadro superior, inferior e pés
A_GC = 2*(2.535+2.425)*0.40                # painel de guarda-corpo, 40 cm
S_po = sup('40x40x1,5', m_po)
it('Piscina de espuma — estrutura', f'{A_PO:.2f} m² × {PROF:.2f} m de profundidade', [
 ('Metalon 40×40×1,5 — quadro e montantes de contenção', m_po,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                          m_po,'m',MO_SERR_REP),
 ('Consumível de solda',        m_po*mL('40x40x1,5'),'vb',CONSUM_S),
 ('Compensado plastificado 18 mm — fundo e laterais',     3.4,'ch',COMP_PLAST18),
 ('Espuma D23 de 5 cm — fundo e paredes do poço', A_PO*2.3*0.05,'m³',ESP['D23']),
 ('Courvin náutico',                               A_PO*2.3,'m²',COURVIN),
 ('Corte, costura e grampeamento',                 A_PO*2.3,'m²',COSTURA),
 ('Chumbador',                                           16.0,'un',CHUMB),
 # ⭐ [Jonathan 21/10] "… e no painel de guarda-corpo da piscina serão
 #   utilizados espuma D33 de 20 mm. Tecido a ser definido."
 ('⭐ Espuma D33 de 20 mm — painel de guarda-corpo', A_GC*0.02,'m³',ESP['D33']),
 ('⭐ Tecido de revestimento · a definir',            A_GC*1.9,'m²',TECIDO_M2),
 ('Corte, costura e grampeamento do guarda-corpo',    A_GC*1.9,'m²',COSTURA),
 (f'Pintura automotiva — {S_po:.2f} m²',                 S_po,'m²',PINT_AUTO),
], obs='⛔ SEM OS BLOCOS, conforme instrução · ⭐ guarda-corpo acolchoado em '
       f'D33 de 20 mm, {A_GC:.1f} m²')

# ══ 5 · BANCO EXTENSO ════════════════════════════════════════════════════
L_BC, B_BC = 5.53, 0.50
m_bc = 2*L_BC + math.ceil(L_BC/0.8+1)*B_BC + 8*0.38
S_bc = sup('40x40x1,5', m_bc)
A_TAB = L_BC*0.38 + 2*B_BC*0.38            # frente e as duas cabeceiras
it('Banco extenso', f'{L_BC:.2f} × {B_BC:.2f} m', [
 ('Metalon 40×40×1,5 — quadro, pés e travamento',        m_bc,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                          m_bc,'m',MO_SERR_REP),
 ('Consumível de solda',        m_bc*mL('40x40x1,5'),'vb',CONSUM_S),
 ('Compensado plastificado 18 mm — base do assento',      1.0,'ch',COMP_PLAST18),
 ('Espuma D28 de 5 cm — assento de uso intenso',
                                       L_BC*B_BC*0.05,'m³',ESP['D28']),
 ('⭐ Tecido de linho para estofaria',  L_BC*B_BC*1.9,'m²',TECIDO_M2),
 ('Corte, costura e grampeamento',      L_BC*B_BC*1.9,'m²',COSTURA),
 # ⭐ [Jonathan 21/10] "uma sugestão é aplicar o padrão TABASCO da Berneck"
 (f'⭐ MDF Berneck padrão Tabasco — fechamento aparente, {A_TAB:.1f} m²',
                                               A_TAB/4.07,'ch',TABASCO_CH),
 ('Fita de borda e montagem do fechamento',            A_TAB,'m²',PARAF_M2),
 ('Chumbador',                                           14.0,'un',CHUMB),
 (f'Pintura automotiva — {S_bc:.2f} m²',                 S_bc,'m²',PINT_AUTO),
], obs='⭐ acabamento em MDF Berneck padrão Tabasco, sugestão da casa')

# ── helper de parede estruturada em MDF ultra CRU ────────────────────────
def parede(nome, L, H, dim_extra='', mont=0.60, trav=1.00, dupla=False,
           forra=None, obs='', papel=False):
    n_m = math.ceil(L/mont)+1; m_m = n_m*H
    n_t = math.ceil(H/trav)+1; m_t = n_t*L
    m_p = m_m+m_t; m2 = L*H*(2 if dupla else 1)
    n_ch = math.ceil(m2/(2.75*1.85*0.85)*10)/10
    lin = [
     (f'⭐ Metalon 50×30 CHAPA 16 — {n_m} montantes a cada {mont*100:.0f} cm',
                                                  m_m,'m',mL(PAREDE_PERFIL)),
     (f'⭐ Metalon 50×30 CHAPA 16 — {n_t} travessas', m_t,'m',mL(PAREDE_PERFIL)),
     ('Mão de obra de serralheria (peça repetitiva)', m_p,'m',MO_SERR_REP),
     ('Consumível de solda',     m_p*mL(PAREDE_PERFIL),'vb',CONSUM_S),
     ('Chumbador',                            (n_m+n_t)*2,'un',CHUMB),
     (f'MDF ultra premium 18 mm CRU — {n_ch:.1f} chapas', n_ch,'ch',MDF_U18),
     ('Parafuso chapa/metalon',                        m2,'m²',PARAF_M2),
     ('Mão de obra de marcenaria — corte e fixação', m2*0.55,'h',MO_MARC_H),
    ]
    if forra: lin.append(forra)
    (M2_PAPEL if papel else M2_PINTURA).append(m2 if dupla else L*H*2)
    return it(nome, f'{L:.2f} × {H:.2f} m · {m2:.2f} m² de chapa {dim_extra}',
              lin, obs=obs or f'{m_p:.1f} m de metalon CHAPA 16 · entrega CRUA')

# ══ 6 · ⛔ PAREDE DE DESENHO — FORA DO ESCOPO [Jonathan 14/10] ═══════════
#   "vamos tirar o painel de desenho". O item saiu INTEIRO, não só a
#   fórmica: era uma parede estruturada de 4,00 × 2,55 que existia para
#   receber o painel. ⚠ Se a parede tiver de ficar sem o painel, é outro
#   item — ver EM ABERTO no dossiê.

# ══ 7 · PAREDE ESTRUTURAL 1 (efeito tijolinho, por conta da cliente) ═════
parede('Parede estrutural 1 (efeito tijolinho)', 8.165, 2.80,
       obs='⛔ o efeito de tijolinho é da CLIENTE — entregamos o MDF cru e plano')

# ══ 8 · ESTRUTURA DA CASINHA — paredes e escada ══════════════════════════
# ⭐ [Jonathan 21/10] a casinha é a TORRE PRINCIPAL: nela vai papel de
#   parede, não pintura acrílica.
parede('Casinha — paredes', 2.85, 2.85, dupla=True, mont=0.50, papel=True,
       obs='fachada e laterais, dupla face · entrega CRUA · ⭐ recebe papel')
# ⭐ [Jonathan 14/10] "as escadas serão em MDF com revestimento
#   emborrachado. Não terá aço em pintura." Sai o metalon, sai a pintura
#   automotiva, sai a espuma com courvin. Entra MDF e manta emborrachada.
M2_LAT = 2*2.60*0.35*2       # duas laterais, duas camadas
M2_DEG = 8*0.70*0.30         # oito degraus
M2_REV = M2_DEG*1.30         # revestimento com o espelho e a quina do degrau
it('Casinha — escada', '2,60 m de lance', [
 ('MDF ultra premium 18 mm — laterais em duas camadas', M2_LAT/4.07,'ch',MDF_U18),
 ('MDF ultra premium 18 mm — degraus',                  M2_DEG/4.07,'ch',MDF_U18),
 ('⭐ Revestimento emborrachado dos degraus',                M2_REV,'m²',EMBORRACHADO),
 ('Usinagem, montagem e esquadro',                             18.0,'h',MO_MARC_H),
 ('Fita de borda e consumível de montagem',          M2_LAT+M2_DEG,'m²',PARAF_M2),
 ('Chumbador e ferragem de fixação',                           14.0,'un',CHUMB),
], obs='⭐ sem aço e sem pintura automotiva [Jonathan 14/10]')

# ══ 9 · JANELAS E PÓRTICOS MOLDURADOS — laca branca ══════════════════════
N_JAN, N_PORT = 4, 2
A_LACA = N_JAN*1.9 + N_PORT*3.4
it('Janelas e pórticos moldurados', f'{N_JAN} janelas + {N_PORT} pórticos · laca branca', [
 ('MDF ultra 15 mm — folhas, marco, peitoril e moldura',   2.8,'ch',MDF_U15),
 ('Metalon 30×30×1,2 — reforço de marco',                 22.0,'m',mL('30x30x1,2')),
 ('Friso decorativo usinado',                             34.0,'m',14.0),
 ('Estilo veneziana — usinagem plana na face',             4.4,'m²',110.0),
 ('Mão de obra de marcenaria (usinagem e montagem)',      38.0,'h',MO_MARC_H),
 (f'⭐ Laca branca aplicada — {A_LACA:.1f} m²',          A_LACA,'m²',LACA_M2),
 ('Dobradiça e ferragem das folhas de giro',              14.0,'un',12.0),
], obs='⭐ único item com acabamento nosso — o resto entrega cru')

# ══ 10 · ESCORREGADOR COM TÚNEL DE TETO CURVO E GRADIL ═══════════════════
L_TU, B_TU, H_TU = 3.60, 0.60, 1.40
n_arco = math.ceil(L_TU/0.40)+1
m_tu = 16.0
it('Escorregador com túnel de teto curvo', f'{L_TU:.2f} m · vão {B_TU:.2f} × {H_TU:.2f} m', [
 (f'MDF ultra 15 mm — {n_arco} arcos usinados',            2.6,'ch',MDF_U15),
 ('Compensado flexível 6 mm — casca do teto curvo',        3.4,'ch',250.0),
 ('Compensado naval 18 mm — pista (recebe carga)',         1.2,'ch',COMP_NAV18),
 ('Metalon 40×40×1,5 — estrutura e gradil de proteção',   m_tu,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                           m_tu,'m',MO_SERR_EST),
 ('Mão de obra de marcenaria — gabarito e curvatura',     30.0,'h',MO_MARC_H),
 ('Laminado de alta pressão na pista (deslizamento)',      2.4,'m²',FORMICA_M2),
 ('Corda do gradil do túnel',                             18.0,'m',CORDA_COMB),
 (f'Pintura automotiva — {sup("40x40x1,5", m_tu):.2f} m²',
                                      sup('40x40x1,5', m_tu),'m²',PINT_AUTO),
], obs='a curvatura é HORA de marcenaria sobre gabarito, não chapa')

# ══ 11 · ⭐ PINTURA ACRÍLICA E PAPEL DE PAREDE — SÓ A MÃO DE OBRA ════════
# [Jonathan 21/10] "adicionar a mão de obra da pintura acrílica nos painéis
#   e aplicação de papel de parede na torre principal. OBS: o fornecimento
#   dos materiais será por conta do contratante. A nível de cálculo de
#   custo, considere R$ 130,00 o metro quadrado da pintura. Considere a
#   pintura interna e externa."
# ⛔⛔ TINTA, MASSA E PAPEL NÃO ESTÃO NO NOSSO PREÇO. Isso tem de estar na
#   proposta com todas as letras, senão a casa compra tinta de graça.
A_PINT, A_PAPEL = sum(M2_PINTURA), sum(M2_PAPEL)
it('Pintura acrílica e papel de parede — mão de obra',
   f'{A_PINT:.1f} m² de pintura · {A_PAPEL:.1f} m² de papel', [
 (f'⭐ Pintura acrílica — interna e externa, {A_PINT:.1f} m²',
                                                  A_PINT,'m²',PINT_ACRIL),
 (f'⭐ Aplicação de papel de parede na torre principal, {A_PAPEL:.1f} m²',
                                                 A_PAPEL,'m²',PAPEL_MO),
], obs='⛔ MÃO DE OBRA APENAS — tinta, massa e papel são fornecimento do '
       'contratante [Jonathan 21/10]')

# ══ 12 · COZINHA DE BRINQUEDO ════════════════════════════════════════════
it('Cozinha de brinquedo', 'módulo lúdico sob medida', [
 ('MDF ultra 18 mm — corpo, bancada e frentes',            3.0,'ch',MDF_U18),
 ('MDF ultra 15 mm — internos e fundo',                    1.0,'ch',MDF_U15),
 ('Dobradiça Hettich Novisys',                            10.0,'un',10.0),
 ('Corrediça telescópica',                                 3.0,'par',40.0),
 ('Cooktop, torneira e pia lúdicos',                       1.0,'vb',560.0),
 ('Puxador e botões',                                     14.0,'un',16.0),
 ('Mão de obra de marcenaria',                            20.0,'h',MO_MARC_H),
], obs='entrega CRUA, como as paredes')

# ══ CONSOLIDAÇÃO ═════════════════════════════════════════════════════════
CD_SIS = sum(i['total'] for i in ITENS)
LOG = 6*150.0 + 18*260.0 + 3*275.0
CONSUM = CD_SIS*0.03
CD = (CD_SIS + LOG + CONSUM)*(1 + M.EMBALAGEM)
# [Jonathan 30/09] entra RT e a MC sobe para 45%
RT_ON = True
BASE = M.base(parcelas=0, rt=RT_ON, vendedor=False)
MC = 0.45

# [Jonathan 30/09] preço CRAVADO, não calculado por MC
PRECO_FIXO = {'Cozinha de brinquedo': 12000}
# [Jonathan 30/09] investimento cravado em 185.000 sobre um custo direto de
# R$ 61.296,38 — o que embutiu uma MC de 43,38%.
# ⭐ [Jonathan 14/10] o escopo mudou: saiu a parede de desenho e a escada
#   deixou de ser de aço. O preço NÃO pode ficar cravado: o cliente levaria
#   menos pelo mesmo valor. O alvo passa a cair na MESMA PROPORÇÃO do custo,
#   o que preserva exatamente a margem que o Jonathan cravou.
ALVO_30_09, CD_30_09 = 185000, 61296.38
ALVO_TOTAL = round(ALVO_30_09*CD/CD_30_09/10)*10

# custo direto de cada item = custo próprio + sua fatia de logística,
# consumível e embalagem, rateada pelo custo (regra da casa)
CDI = {i['nome']: i['total']*CD/CD_SIS for i in ITENS}
# o total é CRAVADO: a cozinha tem preço próprio e o restante é rateado
_resto = [n for n in CDI if n not in PRECO_FIXO]
_alvo  = ALVO_TOTAL - sum(PRECO_FIXO.values())
_base  = sum(CDI[n] for n in _resto)
PV = dict(PRECO_FIXO)
for n in _resto: PV[n] = round(CDI[n]*_alvo/_base/10)*10
_dif = _alvo - sum(PV[n] for n in _resto)
_mai = max(_resto, key=lambda n: PV[n]); PV[_mai] += _dif
TOT = sum(PV.values())
MC_REAL = {n: BASE - CDI[n]/PV[n] for n in PV}
assert TOT == ALVO_TOTAL
MC_CRAVADA_30_09 = 0.43382

if __name__ == '__main__':
    br  = lambda v: f'{v:,.2f}'.replace(',','§').replace('.',',').replace('§','.')
    br0 = lambda v: f'{v:,.0f}'.replace(',','.')
    W = 96
    print('═'*W); print('BRINQUEDOTECA · v2 — custos revisados, separação do Jonathan'); print('═'*W)
    for n, i in enumerate(ITENS, 1):
        p = round(i['total']/(BASE-MC)/10)*10
        print(f'\n{"─"*W}\n{n:>2} · {i["nome"].upper()}   ·   {i["dim"]}')
        if i['obs']: print(f'     {i["obs"]}')
        for d,q,u,v in i['linhas']:
            print(f'       {d:<52}{q:>8.2f} {u:<4} × {br(v):>8} = {br(q*v):>10}')
        print(f'       {"CUSTO":<52}{"":>8} {"":<4}   {"":>8}   {br(i["total"]):>10}')
        print(f'       {"VENDA (MC "+f"{MC:.0%}"+")":<52}{"":>8} {"":<4}   {"":>8}   {br0(p):>10}')
    print(f'\n{"═"*W}')
    print(f'{"":<44}{"custo":>12}{"venda":>12}{"MC":>8}')
    for k, i in enumerate(ITENS, 1):
        nm = i['nome']; fx = ' ←cravado' if nm in PRECO_FIXO else ''
        print(f'  {k:>2} {nm:<40}{br0(CDI[nm]):>12}{br0(PV[nm]):>12}'
              f'{MC_REAL[nm]*100:>7.1f}%{fx}')
    print(f'  {"":<43}{"":>12}{"":>12}')
    print(f'  {"Soma dos itens":<43}{br0(CD_SIS):>12}')
    print(f'  {"+ logística, 18 dias de equipe, 3 visitas":<43}{br0(LOG):>12}')
    print(f'  {"+ consumíveis de fábrica (3%)":<43}{br0(CONSUM):>12}')
    print(f'  {"+ embalagem (2%)":<43}{br0(CD-(CD_SIS+LOG+CONSUM)):>12}')
    print(f'  {"CUSTO DIRETO":<43}{br0(CD):>12}')
    P = TOT
    print(f'\n  BASE {BASE*100:.2f}% · MC alvo {MC:.0%} · MC real {(BASE-CD/TOT)*100:.1f}%')
    print(f'  INVESTIMENTO  R$ {br0(P)}')
    print(f'    brinquedoteca (11 itens)   R$ {br0(P-PRECO_FIXO["Cozinha de brinquedo"]):>9}')
    print(f'    cozinha de brinquedo       R$ {br0(PRECO_FIXO["Cozinha de brinquedo"]):>9}  ← cravado')
    print(f'\n  v1 (agregada)     R$ 445.000')
    print(f'  v1 (decomposta)   R$ 318.100')
    print(f'  v2 (esta)         R$ {br0(P)}   ·  {P/318100-1:+.1%} sobre a v1 decomposta')
