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
MET = {'50x30x1,2':(95.,0.160), '40x40x1,5':(122.,0.160),
       '60x40x2,0':(210.,0.200), '30x30x1,2':(62.,0.120)}   # (R$/barra, perím. m)
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
CORDA_COMB = 62.0                 # ★ combinada 16 mm, nacional
CABO_PERIM = 38.0                 # ★ cabo de aço 6 mm + esticador

def sup(perfil, metros): return perim(perfil)*metros   # m² de pintura

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
], obs=f'⭐ corda: {M_CORDA:.1f} m × R$ {CORDA_COMB:.2f}/m')

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
 ('Espuma D33 de 4 cm — recebe pisada',            A_pl*0.04,'m³',ESP['D33']),
 ('Courvin náutico',                                A_pl*2.1,'m²',COURVIN),
 ('Corte, costura e grampeamento',                  A_pl*2.1,'m²',COSTURA),
 ('Chumbador',                                       N_PL*4.0,'un',CHUMB),
 (f'Pintura automotiva — {S_pl:.2f} m²',                 S_pl,'m²',PINT_AUTO),
], obs=f'{m_pl:.1f} m de metalon no conjunto · D33 porque a criança PISA em pé')

# ══ 4 · PISCINA DE ESPUMA — só a estrutura, sem os blocos ════════════════
A_PO, PROF = 2.535*2.425, 0.55
m_po = 2*(2.535+2.425)*2 + 8*PROF          # quadro superior, inferior e pés
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
 (f'Pintura automotiva — {S_po:.2f} m²',                 S_po,'m²',PINT_AUTO),
], obs='⛔ SEM OS BLOCOS, conforme instrução — ver nota no relatório')

# ══ 5 · BANCO EXTENSO ════════════════════════════════════════════════════
L_BC, B_BC = 5.53, 0.50
m_bc = 2*L_BC + math.ceil(L_BC/0.8+1)*B_BC + 8*0.38
S_bc = sup('40x40x1,5', m_bc)
it('Banco extenso', f'{L_BC:.2f} × {B_BC:.2f} m', [
 ('Metalon 40×40×1,5 — quadro, pés e travamento',        m_bc,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                          m_bc,'m',MO_SERR_REP),
 ('Consumível de solda',        m_bc*mL('40x40x1,5'),'vb',CONSUM_S),
 ('Compensado plastificado 18 mm — base do assento',      1.0,'ch',COMP_PLAST18),
 ('Espuma D28 de 5 cm — assento de uso intenso',
                                       L_BC*B_BC*0.05,'m³',ESP['D28']),
 ('Courvin náutico',                    L_BC*B_BC*1.9,'m²',COURVIN),
 ('Corte, costura e grampeamento',      L_BC*B_BC*1.9,'m²',COSTURA),
 ('Chumbador',                                           14.0,'un',CHUMB),
 (f'Pintura automotiva — {S_bc:.2f} m²',                 S_bc,'m²',PINT_AUTO),
])

# ── helper de parede estruturada em MDF ultra CRU ────────────────────────
def parede(nome, L, H, dim_extra='', mont=0.60, trav=1.00, dupla=False,
           forra=None, obs=''):
    n_m = math.ceil(L/mont)+1; m_m = n_m*H
    n_t = math.ceil(H/trav)+1; m_t = n_t*L
    m_p = m_m+m_t; m2 = L*H*(2 if dupla else 1)
    n_ch = math.ceil(m2/(2.75*1.85*0.85)*10)/10
    lin = [
     (f'Metalon 50×30×1,2 — {n_m} montantes a cada {mont*100:.0f} cm',
                                                     m_m,'m',mL('50x30x1,2')),
     (f'Metalon 50×30×1,2 — {n_t} travessas',        m_t,'m',mL('50x30x1,2')),
     ('Mão de obra de serralheria (peça repetitiva)', m_p,'m',MO_SERR_REP),
     ('Consumível de solda',      m_p*mL('50x30x1,2'),'vb',CONSUM_S),
     ('Chumbador',                            (n_m+n_t)*2,'un',CHUMB),
     (f'MDF ultra premium 18 mm CRU — {n_ch:.1f} chapas', n_ch,'ch',MDF_U18),
     ('Parafuso chapa/metalon',                        m2,'m²',PARAF_M2),
     ('Mão de obra de marcenaria — corte e fixação', m2*0.55,'h',MO_MARC_H),
    ]
    if forra: lin.append(forra)
    return it(nome, f'{L:.2f} × {H:.2f} m · {m2:.2f} m² de chapa {dim_extra}',
              lin, obs=obs or f'{m_p:.1f} m de metalon · entrega CRUA')

# ══ 6 · PAREDE DE DESENHO com painel em fórmica ══════════════════════════
parede('Parede de desenho (painel em fórmica)', 4.00, 2.55,
       forra=('Laminado fórmica branca + cola de contato', 4.00*1.60,'m²',FORMICA_M2),
       obs='fórmica branca na faixa de alcance da criança — escreve e apaga')

# ══ 7 · PAREDE ESTRUTURAL 1 (efeito tijolinho, por conta da cliente) ═════
parede('Parede estrutural 1 (efeito tijolinho)', 8.165, 2.80,
       obs='⛔ o efeito de tijolinho é da CLIENTE — entregamos o MDF cru e plano')

# ══ 8 · ESTRUTURA DA CASINHA — paredes e escada ══════════════════════════
parede('Casinha — paredes', 2.85, 2.85, dupla=True, mont=0.50,
       obs='fachada e laterais, dupla face · entrega CRUA')
m_ec = 2*2.6 + 8*0.30
it('Casinha — escada', '2,60 m de lance', [
 ('Metalon 40×40×1,5 — banzos e degraus',                m_ec,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                          m_ec,'m',MO_SERR_EST),
 ('Consumível de solda',        m_ec*mL('40x40x1,5'),'vb',CONSUM_S),
 ('Compensado plastificado 18 mm — piso dos degraus',     0.9,'ch',COMP_PLAST18),
 ('Espuma D33 de 3 cm — forração do degrau',         3.6*0.03,'m³',ESP['D33']),
 ('Courvin náutico',                                  3.6*1.6,'m²',COURVIN),
 ('Corte, costura e grampeamento',                    3.6*1.6,'m²',COSTURA),
 ('Chumbador',                                           10.0,'un',CHUMB),
 (f'Pintura automotiva — {sup("40x40x1,5", m_ec):.2f} m²',
                                      sup('40x40x1,5', m_ec),'m²',PINT_AUTO),
])

# ══ 9 · JANELAS E PÓRTICOS MOLDURADOS — laca branca ══════════════════════
N_JAN, N_PORT = 4, 2
A_LACA = N_JAN*1.9 + N_PORT*3.4
it('Janelas e pórticos moldurados', f'{N_JAN} janelas + {N_PORT} pórticos · laca branca', [
 ('MDF ultra 15 mm — folhas, marco, peitoril e moldura',   2.8,'ch',MDF_U15),
 ('Metalon 30×30×1,2 — reforço de marco',                 22.0,'m',mL('30x30x1,2')),
 ('Friso decorativo usinado',                             34.0,'m',14.0),
 ('Veneziana fixa usinada (ripa a ripa)',                  4.4,'m²',185.0),
 ('Mão de obra de marcenaria (usinagem e montagem)',      46.0,'h',MO_MARC_H),
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

# ══ 11 · COZINHA DE BRINQUEDO ════════════════════════════════════════════
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
BASE = M.base(parcelas=0, rt=False, vendedor=False)
MC = 0.42

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
    print(f'{"":<44}{"custo":>12}{"venda":>12}')
    tot_v = 0
    for n, i in enumerate(ITENS, 1):
        p = round(i['total']/(BASE-MC)/10)*10; tot_v += p
        print(f'  {n:>2} {i["nome"]:<40}{br0(i["total"]):>12}{br0(p):>12}')
    print(f'  {"":<43}{"":>12}{"":>12}')
    print(f'  {"Soma dos itens":<43}{br0(CD_SIS):>12}')
    print(f'  {"+ logística, 18 dias de equipe, 3 visitas":<43}{br0(LOG):>12}')
    print(f'  {"+ consumíveis de fábrica (3%)":<43}{br0(CONSUM):>12}')
    print(f'  {"+ embalagem (2%)":<43}{br0(CD-(CD_SIS+LOG+CONSUM)):>12}')
    print(f'  {"CUSTO DIRETO":<43}{br0(CD):>12}')
    P = round(CD/(BASE-MC)/100)*100
    print(f'\n  BASE {BASE*100:.2f}% · MC {MC:.0%}   →   INVESTIMENTO  R$ {br0(P)}')
    print(f'\n  v1 (agregada)     R$ 445.000')
    print(f'  v1 (decomposta)   R$ 318.100')
    print(f'  v2 (esta)         R$ {br0(P)}   ·  {P/318100-1:+.1%} sobre a v1 decomposta')
