# -*- coding: utf-8 -*-
"""ESTIMATIVA ITEM A ITEM — Residência Henrique e Karelen.

Padrão da casa: cada ITEM é um bloco autossuficiente dentro do ambiente.
O custo do item PUXA o que é dele; o que é do ambiente se rateia.

  do ITEM  .... chapa pela ÁREA, fita + filetagem, ferragem, terceirizado,
                corte por peça, consumíveis 6%, embalagem 3%
  do AMBIENTE . o ARREDONDAMENTO de chapa (a sobra que se compra e não se usa)
                e o corte por chapa — rateados pela área que cada item ocupa
                em cada material. A última linha absorve o centavo.

⚠ ORDEM DE GRANDEZA, não orçamento: 10 dos 15 ambientes, profundidades
  assumidas onde a prancha não cota, 12 padrões de MDF no piso do Fosco.
"""
import sys, os, math
_d = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_d, '..'))
import motor_mc as M

CHAPA_M2 = 2.75*1.85
APROV = {6: 0.55, 15: 0.82, 18: 0.82}
MDF   = {6: 300.0, 15: 500.0, 18: 600.0}
FITA, FILET, CONSUM = 3.0, 2.5, 0.06
CORTE_CH, CORTE_PC = 2.0, 2.5
SUP, ALMA = 6.50, 35.0
DOBR, CORR, PULS = 50.0, 400.0, 100.0
BASC_XS = 250.0   # Aventos HK-xs — portas pequenas (rack da sala de estar, 20 de altura)
BASC_S  = 390.0   # Aventos HK-S  — [Jonathan 26/11] basculas da cozinha. ⚠ custo estimado
PALHA, ESPELHO, VIDRO, LED = 650.0, 600.0, 250.0, 150.0
VIDRO_LAQ = 480.0   # vidro laqueado (pintado) ⚠ estimado
TOUCH     = 500.0   # corrediça touch (regra 5) — substitui corrediça E pulsador
MAOFRAN   = 300.0   # mão francesa invisível (serralheiro), por peça
REGUL     = 900.0   # ⚠ coluna de altura regulável 50/70 — ESTIMADO, não está na Base
CAVA, CORRER2, CORRER3, TRILHO, PIVO, CABIDE = 50.0, 700.0, 850.0, 350.0, 120.0, 60.0

ITENS = []          # (ambiente, nome, Item)

class I:
    def __init__(s, amb, nome, medida=''):
        s.amb, s.nome, s.medida = amb, nome, medida
        s.area, s.fita, s.pc, s.fer, s.ter = {}, 0.0, 0, 0.0, 0.0
        s.lista = []          # peças, uma a uma
        s.fers  = []          # (nome, qtd, custo unitário)
        s.ters  = []          # (nome, custo)
        s.det = []
        ITENS.append(s)
    # ---- chapa.  Toda peça entra em s.lista: (desc, C, L, qtd, esp, fita_m)
    def ch(s, esp, m2, pecas=1, fita_m=0.0, desc=None, C=None, L=None, q=1):
        s.area[esp] = s.area.get(esp, 0.0) + m2
        s.pc += pecas; s.fita += fita_m
        if desc: s.lista.append((desc, C, L, q, esp, fita_m))
        return s
    def _p(s, desc, C, L, q, esp, fita_m):
        """uma peça: área + fita, e registra a linha"""
        s.area[esp] = s.area.get(esp, 0.0) + C*L*q/1e4
        s.pc += q; s.fita += fita_m
        s.lista.append((desc, C, L, q, esp, fita_m))
        return s
    def caixa(s, C, A, P, esp=15, prat=0, div=0, fundo=True):
        s._p('lateral',    A, P, 2, esp, 2*(A+P)/100)
        s._p('tampo/base', C, P, 2, esp, 2*(C+P)/100)
        if prat: s._p('prateleira', C, P, prat, esp, prat*(C+P)/100)
        if div:  s._p('divisória',  A, P, div,  esp, div*(A+P)/100)
        if fundo: s._p('fundo', C, A, 1, 6, 0.0)
        return s
    def frente(s, L, A, q, esp=18, desc='frente'):
        s._ultL, s._ultq = L, q
        return s._p(desc, L, A, q, esp, 2*(L+A)*q/100)
    def painel(s, C, A, ripado=False, esp=18):
        if ripado:
            n = int(C/12)+1
            s._p('ripa', A, 10, n, esp, 0.0)
            s._p('base do ripado', C, A, 1, esp, 2*(C+A)/100)
        else:
            s._p('painel', C, A, 1, esp, 2*(C+A)/100)
            s._p('travessa de fixação', C, 10, 1, esp, 0.0)
        return s
    # ---- ferragem e terceiro
    def f(s, v, q=1, o=''):
        # ⭐ a Base cobra CAVA USINADA POR METRO, não por peça: converte pela
        #   largura da última frente lançada (é nela que a cava corre).
        if v == CAVA and getattr(s, '_ultL', None):
            q = round(q * s._ultL / 100.0, 2)
        s.fer += v*q
        if o: s.fers.append((o, q, v))
        if o: s.det.append('%s ×%g' % (o, q))
        return s
    def t(s, v, o=''):
        s.ter += v
        if o: s.ters.append((o, v))
        if o: s.det.append(o)
        return s
    def prat(s, n, vao_cm):
        s.f(SUP, n, 'suporte de prateleira')
        if vao_cm > 120: s.f(ALMA, n, 'alma de aço (vão >1,20 m)')
        return s

# ══════════════ 01 · APOIO ════════════════════════════════════════════════
a = '01 Apoio'
I(a, 'Armário de portas de correr', '240 × 265 × 70') \
 .caixa(240,265,70,prat=9,div=2).frente(80,265,3) \
 .prat(9,92).f(CORR,2,'corrediça Movento').f(CAVA,2,'cava usinada') \
 .t(CORRER3+TRILHO,'sistema de correr 3 portas')
I(a, 'Painel de TV e rodapé', '383 × 270').painel(383,270)
I(a, 'Rack suspenso com frentes em palhinha', '191,2 × 22 × 45') \
 .caixa(191.2,22,45,fundo=False).f(CORR,4,'corrediça Movento') \
 .t(PALHA*191.2*22/1e4*1.1,'palhinha das frentes (tapeceiro)') \
 .t(300,'serralheiro: fixação em balanço')

# ══════════════ 02 · ÁREA DE SERVIÇO ══════════════════════════════════════
a = '02 Área de serviço'
I(a, 'Estante aberta da despensa', '212 × 180 × 45') \
 .caixa(212,180,45,prat=4).prat(4,212)
I(a, 'Gaveteiro da despensa', '210 × 90 × 45') \
 .caixa(210,90,45).frente(70,39,6).f(CORR,6,'corrediça Movento').f(CAVA,6,'cava usinada')
I(a, 'Coluna lateral', '50 × 270 × 45').caixa(50,270,45,prat=2).prat(2,50)
I(a, 'Armários da elevação C', '50 × 93 e 40 × 40') \
 .caixa(50,93,45).frente(50,93,1).f(DOBR,2,'dobradiça Blum') \
 .caixa(40,40,45).frente(40,40,1).f(DOBR,2,'dobradiça Blum') \
 ._p('prateleira',50,45,3,18,3*2*(50+45)/100).prat(3,50)
I(a, 'Porta de vidro da despensa', '79,9 × 209') \
 .t(VIDRO*79.9*209/1e4+200,'vidraceiro')

# ══════════════ 03 · BANHO SOCIAL ═════════════════════════════════════════
a = '03 Banho social'
I(a, 'Espelheira de correr com LED', '150 × 160 × 15') \
 .caixa(150,160,15,prat=4).prat(4,150) \
 .t(ESPELHO*150*160/1e4*1.1,'espelho Crystal Prata 5 mm, 2 folhas') \
 .t(CORRER2,'sistema de correr 2 portas').t(LED*3.0,'iluminação LED')
I(a, 'Prateleira em Imbuia sob a bancada', '150 × 22') \
 ._p('prateleira em Imbuia',150,22,1,18,2*(150+22)/100)

# ══════════════ 04 · COZINHA ═════════════════════════════════════════════
# [Jonathan 27/11] tres itens: ILHA · ADEGA · RESTANTE.
a = '04 Cozinha'

# --- ADEGA: o armario de portas de vidro da elevacao A -------------------
# [Jonathan 27/11] interior em MDF GIANDUIA TRAMA, frentes de gaveta em
# VIDRO LAQUEADO. O detalhamento nao poe gavetas neste armario (so 3 folhas
# de vidro de 132,6 / 131 / 132,9); as 16 gavetas de frente de vidro estao
# na SALA DE JANTAR, logo abaixo da cristaleira — o laqueado foi para la.
I(a, 'ADEGA — armário de portas de vidro', '408,5 × 60 × 35') \
 .caixa(408.5,60,35,prat=1,div=2).prat(1,131) \
 .f(DOBR,6,'dobradiça Blum') \
 .t(VIDRO*408.5*60/1e4*1.1+200,'3 folhas de vidro temperado (vidraceiro)') \
 .t(900,'serralheria: perfil metálico de moldura das 3 folhas') \
 .t(LED*4.1,'LED das prateleiras da adega')

# --- ILHA -----------------------------------------------------------------
I(a, 'ILHA com chopeira', '370 × 90 × 90') \
 .caixa(370,90,90,div=3).frente(91.5,87,1).frente(91.5,38.5,4) \
 .frente(91.5,20,2).frente(91.5,19.1,1) \
 .f(DOBR,2,'dobradiça Blum').f(CORR,7,'corrediça Movento').f(CAVA,7,'cava usinada') \
 .t(300,'serralheiro: recorte e ponto da chopeira')

# --- RESTANTE: tudo o mais da cozinha num item so -------------------------
I(a, 'RESTANTE da cozinha', 'elevação A, 590,5 × 270') \
 .caixa(408,90,35,prat=1,div=4).frente(82,35,10).frente(82,20,3) \
 .f(BASC_S,13,'Aventos HK-S').f(PULS,13,'Tip-on').f(DOBR,26,'dobradiça Blum').prat(1,408) \
 .caixa(408.5,80,77,div=3).frente(112.8,38.5,4) \
 .f(CORR,4,'corrediça Movento').f(CAVA,4,'cava usinada') \
 .caixa(59.6,70,77,fundo=False).caixa(70,90,77,fundo=False)

# ══════════════ 05 · ESCRITÓRIO ═══════════════════════════════════════════
a = '05 Escritório'
I(a, 'Painel de parede', '270 × 270').painel(270,270)
I(a, 'Prateleiras com mão francesa invisível', '2 × 260 × 20') \
 ._p('prateleira',260,20,2,18,2*2*(260+20)/100).t(MAOFRAN*2,'mão francesa invisível ×2')
I(a, 'Escrivaninha com nicho e 4 gavetas', '190,7 × 75 × 50') \
 .caixa(190.7,75,50,div=1).frente(45,17,4) \
 .f(CORR,4,'corrediça Movento').f(CAVA,4,'cava usinada')
I(a, 'Lateral de fechamento', '65 × 64,8 × 50').caixa(65,64.8,50,fundo=False)

# ══════════════ 06 · QUARTO DE HÓSPEDES ═══════════════════════════════════
a = '06 Quarto de hóspedes'
I(a, 'Painel de parede com TV', '347,9 × 265').painel(347.9,265)
I(a, 'Guarda-roupa de correr em vidro canelado', '170 × 260 × 60') \
 .caixa(170,260,60,prat=2,div=1).frente(82.5,16,8).prat(2,170) \
 .f(CORR,8,'corrediça Movento').f(CAVA,8,'cava usinada').f(CABIDE,1,'cabideiro') \
 .t(VIDRO*170*260/1e4*1.1,'vidro canelado 2 folhas').t(CORRER2+TRILHO,'sistema de correr')
I(a, 'Painel-porta de passagem', '105 × 265').painel(105,265).f(DOBR,3,'dobradiça Blum')
I(a, 'Painel da cabeceira em Freijó Puro', '268 × 225').painel(268,225)
I(a, 'Mesa de cabeceira suspensa', '60 × 24 × 35') \
 .caixa(60,24,35,fundo=False).frente(29,20,2).f(CORR,2,'corrediça Movento') \
 .t(PALHA*60*20/1e4*1.2,'palhinha das 2 frentes')
I(a, 'Torre com gavetas em palhinha', '60 × 270 × 60') \
 .caixa(60,270,60,prat=2).frente(54,18,4).prat(2,60).f(CORR,4,'corrediça Movento') \
 .t(PALHA*54*18*4/1e4*1.2,'palhinha das 4 frentes')

# ══════════════ 07 · SALA DE ESTAR ════════════════════════════════════════
a = '07 Sala de estar'
I(a, 'Painel de parede acima do rack', '415 × 198').painel(415,198)
I(a, 'Rack com básculas e gavetas em ripado vazado', '415 × 72 × 50') \
 .caixa(415,72,50,prat=1,div=4).frente(82,20,5).frente(82,29,5) \
 ._p('ripa do vazado 2×2 · 2ª camada',82,20,5,18,0.0)._p('ripa do vazado 2×2 · 2ª camada',82,29,5,18,0.0) \
 .f(BASC_XS,5,'Aventos HK-xs').f(PULS,5,'Tip-on') \
 .f(CORR,5,'corrediça Movento').f(CAVA,5,'cava usinada').prat(1,415)
I(a, 'Porta de abrir em Capuccino', '85 × 270').painel(85,270).f(DOBR,3,'dobradiça Blum')
I(a, 'Parede ripada com porta pivotante oculta', '320 × 270') \
 .painel(100,270,ripado=True).painel(70,270,ripado=True).painel(150,270,ripado=True) \
 .t(PIVO*3+600,'pivô de alta carga para folha de 150 × 270') \
 .t(300,'puxador em barra vazado em madeira Imbuia')

# ══════════════ 08 · SALA DE JANTAR ═══════════════════════════════════════
a = '08 Sala de jantar'
I(a, 'Cristaleira com portas de vidro', '150 × 175 × 35') \
 .caixa(150,175,35,prat=4,div=1).prat(4,150).f(DOBR,4,'dobradiça Blum') \
 .t(VIDRO*150*175/1e4*1.1+200,'2 folhas de vidro (vidraceiro)')
I(a, 'Gaveteiro de 16 gavetas sob a pedra', '372,5 × 87 × 40') \
 .caixa(372.5,87,40,div=3,fundo=True) \
 .f(CORR,16,'corrediça Movento').f(CAVA,16,'cava usinada').frente(92.6,19.3,16)
I(a, 'Nicho das duas adegas', '150 × 87 × 60').caixa(150,87,60,div=1)

# ══════════════ 14 · SUÍTE MASTER ═════════════════════════════════════════
a = '14 Suíte master'
I(a, 'Painel ripado da cabeceira (Neblina, ripas 10×1)', '454,5 × 217') \
 .painel(454.5,217,ripado=True)
I(a, 'Mesas de cabeceira suspensas (2)', '2 × 50 × 24 × 40') \
 .caixa(50,24,40,fundo=False).frente(50,20,1).f(CORR,1,'corrediça Movento') \
 .caixa(50,24,40,fundo=False).frente(50,20,1).f(CORR,1,'corrediça Movento')
I(a, 'Painel de parede e porta embutida', '345,1 × 255  +  porta 80 × 255') \
 .painel(345.1,255).painel(80,255).f(DOBR,3,'dobradiça Blum')
I(a, 'Escrivaninha em balanço', '297,5 × 75 × 50') \
 .caixa(297.5,75,50,div=2).t(300,'serralheiro: fixação em balanço')

# ══════════════ 15 · BANHO DA SUÍTE MASTER ════════════════════════════════
a = '15 Banho da suíte master'
I(a, 'Roupeiro com cabideiro', '143,4 × 270 × 60') \
 .caixa(143.4,270,60,prat=2,div=1).frente(71,270,2).prat(2,143) \
 .f(DOBR,6,'dobradiça Blum').f(CABIDE,1,'cabideiro')
I(a, 'Gaveteiro de 8 gavetas', '182 × 84 × 60') \
 .caixa(182,84,60,div=1).frente(89,16,8) \
 .f(CORR,8,'corrediça Movento').f(CAVA,8,'cava usinada')
I(a, 'Armário espelhado de correr com LED', '192 × 160 × 20') \
 .caixa(192,160,20,prat=3).prat(3,192) \
 .t(ESPELHO*192*160/1e4*1.1,'espelho Crystal Prata 5 mm, 3 folhas') \
 .t(CORRER3+TRILHO,'sistema de correr 3 portas').t(LED*6.0,'iluminação LED')
I(a, 'Armário ripado sob a bancada', '192 × 75 × 50') \
 .caixa(192,75,50,div=2).frente(63,37.5,4)._p('ripa da frente · 2ª camada',192,75,1,18,0.0) \
 .f(DOBR,8,'dobradiça Blum')
I(a, 'Espelhos das outras duas paredes', '87,9 e 120,3 × 200') \
 .t(ESPELHO*(87.9+120.3)*200/1e4*1.1,'espelho Crystal Prata 5 mm') \
 .t(LED*4.2,'iluminação LED')

# ══════════════ CÁLCULO ═══════════════════════════════════════════════════
def fechar():
    ambs = {}
    for it in ITENS: ambs.setdefault(it.amb, []).append(it)
    res = {}
    for amb, its in ambs.items():
        # chapas do AMBIENTE (é assim que se compra)
        area_amb = {}
        for it in its:
            for e, m2 in it.area.items(): area_amb[e] = area_amb.get(e, 0.0) + m2
        chapas, sobra = {}, {}
        for e, m2 in area_amb.items():
            n = max(1, math.ceil(round(m2/(CHAPA_M2*APROV[e]), 6)))
            chapas[e] = n
            sobra[e] = n*MDF[e] - m2/APROV[e]/CHAPA_M2*MDF[e]   # o que se compra e não se usa
        corte_ch = sum(chapas.values())*CORTE_CH
        linhas = []
        for k, it in enumerate(its):
            c_ch = sum(m2/APROV[e]/CHAPA_M2*MDF[e] for e, m2 in it.area.items())
            # rateio do arredondamento e do corte por chapa, pela área em cada material
            rat = sum(sobra[e]*(m2/area_amb[e]) for e, m2 in it.area.items())
            a_tot = sum(area_amb.values()) or 1
            rat += corte_ch*(sum(it.area.values())/a_tot)
            c_fita = it.fita*1.15*(FITA+FILET)
            c_cons = (c_ch + rat + c_fita)*CONSUM
            c_corte = it.pc*CORTE_PC
            cd = M.com_embalagem(c_ch + rat + c_fita + c_cons + c_corte + it.fer + it.ter)
            linhas.append(dict(it=it, ch=c_ch+rat, fita=c_fita, cons=c_cons,
                               corte=c_corte, fer=it.fer, ter=it.ter, cd=cd))
        res[amb] = dict(chapas=chapas, itens=linhas, cd=sum(l['cd'] for l in linhas))
    return res

# ══════════════ 2b · ÁREA DE SERVIÇO — complemento (lavanderia) ═══════════
a = '02 Área de serviço'
I(a, 'Armário de básculas da lavanderia', '170 × 80 × 40') \
 .caixa(170,80,40,div=1).frente(85,37.5,4) \
 .f(BASC_S,4,'Aventos HK-S').f(PULS,4,'Tip-on').f(DOBR,8,'dobradiça Blum')
I(a, 'Armários sob a bancada em L', '170 + 200 × 88 × 60') \
 .caixa(170,88,60,div=1).caixa(200,88,60,div=2) \
 .frente(63.8,88,2).frente(41,88,1).frente(60,88,1) \
 .f(DOBR,8,'dobradiça Blum').f(CAVA,4,'cava usinada').prat(1,41) \
 .f(CABIDE,1,'cabideiro inox')
I(a, 'Armários da elevação A', '40 × 80  ·  70 + 64 + 64 × 88') \
 .caixa(40,80,40,prat=1).caixa(70,88,60).caixa(128,88,60,div=1) \
 .frente(64,78,2).f(DOBR,4,'dobradiça Blum').prat(1,40)
I(a, 'Painel de fechamento da elevação A', '89,6 × 255').painel(89.6,255)
I(a, 'Armário alto e nicho da elevação E', '40 × 40  ·  30') \
 .caixa(40,40,40).caixa(30,30,40,fundo=False).f(DOBR,2,'dobradiça Blum')
I(a, 'Porta de vidro da área de serviço', '80 × 209') \
 .t(VIDRO*80*209/1e4*1.1+200,'vidraceiro')

# ══════════════ 9 · SUÍTE 01 (menina) ═════════════════════════════════════
a = '09 Suíte 01 (menina)'
I(a, 'Painel ripado da elevação A', '304,5 × 110') \
 .painel(304.5,110,ripado=True)
I(a, 'Prateleiras com mão francesa invisível', '2 × 100 × 27') \
 ._p('prateleira em Tauari',100,27,2,18,2*2*(100+27)/100).t(MAOFRAN*2,'mão francesa invisível ×2')
I(a, 'Escrivaninha com altura regulável', '282,5 × 50') \
 .caixa(282.5,50,50,div=3,fundo=False).frente(70,12,4) \
 .f(TOUCH,4,'corrediça TOUCH (fecho toque)') \
 .t(REGUL,'⚠ mecanismo de altura regulável 50/70 cm')
I(a, 'Painel, porta de correr e rodapé (elev. B)', '437,5 × 270') \
 .painel(437.5,270).frente(90,260,1) \
 .t(CORRER2+TRILHO,'sistema de correr')
I(a, 'Prateleira Tauari da elevação B', '59,5 × 27') \
 ._p('prateleira em Tauari',59.5,27,1,18,2*(59.5+27)/100).t(MAOFRAN,'mão francesa invisível')
I(a, 'Painel ripado da elevação C', '304,5 × 110') \
 .painel(304.5,110,ripado=True)
I(a, 'Armário da planta (parede do topo)', '298,5 × 270 × 59,5') \
 .caixa(198.5,270,59.5,prat=2,div=1).caixa(100,270,59.5,prat=2) \
 .frente(99,260,2).frente(100,260,1).f(DOBR,9,'dobradiça Blum').prat(4,99)

# ══════════════ 11 · SUÍTE 02 (menino) ════════════════════════════════════
a = '11 Suíte 02 (menino)'
I(a, 'Painel ripado azul petróleo (elev. A)', '304,5 × 120 · ripas 1×1') \
 .painel(304.5,120,ripado=True)
I(a, 'Painel e porta (elev. B)', '437,5 × 260') \
 .painel(437.5,260).frente(103,260,1) \
 .t(CORRER2+TRILHO,'sistema de correr').f(DOBR,3,'dobradiça Blum')
I(a, 'Painel ripado e nichos Tauari (elev. C)', '304,5 × 208 · ripas 10×2') \
 .painel(304.5,208,ripado=True) \
 .caixa(70,20,25,fundo=True).caixa(70,20,25,fundo=True)
I(a, 'Escrivaninha com altura regulável', '304,5 × 50') \
 .caixa(304.5,50,50,div=3,fundo=False).frente(70,12,4) \
 .f(TOUCH,4,'corrediça TOUCH (fecho toque)') \
 .t(REGUL,'⚠ mecanismo de altura regulável 50/70 cm')
I(a, 'Guarda-roupa de 3 portas de correr (elev. D)', '437,5 × 270 × 60') \
 .caixa(437.5,270,60,prat=3,div=2).frente(145.8,268,3) \
 .prat(3,145).f(CABIDE,2,'cabideiro') \
 .t(CORRER3+TRILHO,'sistema de correr 3 portas')

# ══════════════ 10 · BANHO 01 (da suíte da menina) ════════════════════════
# MDF GIANDUIA-LIDER. ⛔ bancada e cuba em pietra Lombarda Viva Sabbia
# 90x90 Portobello, box de vidro e rodapé em pietra: não são nossos.
a = '10 Banho 01'
I(a, 'Torre de armário', '58 × 270 × 35') \
 .caixa(58,270,35,prat=2,div=0).frente(56,106,1).frente(56,68,1) \
 .prat(2,58).f(DOBR,4,'dobradiça Blum').f(CAVA,2,'cava usinada')
I(a, 'Gaveteiro sob a bancada', '123 × 61 × 45') \
 .caixa(123,61,45,fundo=True).frente(121,20,3) \
 .f(CORR,3,'corrediça Movento').f(CAVA,3,'cava usinada')
I(a, 'Espelho com fixação flutuante e LED', '123 × 152,5') \
 .t(ESPELHO*123*152.5/1e4*1.1,'espelho Crystal Prata 5 mm') \
 .t(LED*3.0,'iluminação LED')

# ══════════════ 12 · BANHO 02 (da suíte do menino) ════════════════════════
# MDF GIANDUIA-LIDER. Ambiente de 235 × 270. ⛔ bancada esculpida em pietra
# (110 × 55 × 20, cuba 60 × 35), louças e metais Mix and Match: não são nossos.
a = '12 Banho 02'
I(a, 'Gaveteiro sob a bancada', '110 × 61 × 45') \
 .caixa(110,61,45,fundo=True).frente(108,20,3) \
 .f(CORR,3,'corrediça Movento').f(CAVA,3,'cava usinada')
I(a, 'Espelho com fixação flutuante e LED', '110 × 150') \
 .t(ESPELHO*110*150/1e4*1.1,'espelho Crystal Prata 5 mm') \
 .t(LED*2.7,'iluminação LED')

# ══════════════ 13 · LAVABO ═══════════════════════════════════════════════
# MDF GIANDUIA-LIDER. ⛔ bancada e cuba esculpida em pedra, espelho redondo
# com moldura e revestimento: conferir com a prancha 02/04 a 04/04.
a = '13 Lavabo'
I(a, 'Gabinete suspenso', '100 × 50 × 45') \
 .caixa(100,50,45,fundo=True).frente(98,20,2) \
 .f(CORR,2,'corrediça Movento').f(CAVA,2,'cava usinada')
I(a, 'Espelho', '80 × 120') \
 .t(ESPELHO*80*120/1e4*1.1,'espelho Crystal Prata 5 mm').t(LED*2.0,'iluminação LED')
