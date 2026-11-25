# -*- coding: utf-8 -*-
"""ESTIMATIVA DE ORDEM DE GRANDEZA — Residência Henrique e Karelen.

⚠⚠ ISTO NÃO É O ORÇAMENTO. É uma estimativa dos ambientes JÁ LEVANTADOS,
   para dar ordem de grandeza ao Jonathan antes de o levantamento fechar.
   O orçamento de verdade é peça a peça, na planilha, com o motor da casa.

O que torna isto estimativa, e não número fechado:
  1. faltam 5 ambientes (suíte 01, banho 01, suíte 02, banho 02, lavabo);
  2. faltam PROFUNDIDADES em quase todo armário — as pranchas cotam
     elevação, não planta de cada móvel. Onde falta, está assumido e
     marcado com `prof_assumida=True`;
  3. os 12 padrões de MDF do projeto não têm preço na Base: todos entram
     no PISO do Melamínico Fosco, que é um MÍNIMO.

Ferragem: tudo Blum [Jonathan 24-25/11/2026].
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import motor_mc as M

# ─── Base de preços (dados/materiais.json) ────────────────────────────────
CHAPA_M2   = 2.75 * 1.85          # 5,0875 m²
APROV      = {6: 0.55, 15: 0.82, 18: 0.82}
# ⚠ os 12 padrões do projeto caem no piso do Melamínico Fosco
MDF        = {6: 300.0, 15: 500.0, 18: 600.0}
FITA       = 3.0                  # fita de cor, por metro
FILETAGEM  = 2.5                  # máquina, por metro
CONSUM     = 0.06                 # 6% de (chapa + fita), regra dos motores
CORTE_CH   = 2.0
CORTE_PC   = 2.5
SUPORTE    = 6.50                 # por PRATELEIRA (regra 2)
ALMA       = 35.0                 # prateleira > 1,20 m (regra 4) ~ estimado
# ferragem Blum
DOBR       = 50.0                 # Blum Clip Top Blumotion  [Jonathan 25/11]
CORR       = 400.0                # Blum Movento (par)       ⚠ paridade Actro
BASC       = 250.0                # Aventos HK-xs
PULS       = 100.0                # Tip-on / Servo
# outros
PALHINHA   = 650.0                # m², tapeceiro (regra 7)
ESPELHO    = 600.0                # m², espelho prata
VIDRO      = 250.0                # m², temperado 8mm
LED        = 150.0                # metro (fita + perfil)
CAVA       = 50.0                 # cava 35° usinada, por peça
CORRER2    = 700.0                # Dominus 2 portas
CORRER3    = 850.0                # Dominus 3 portas
TRILHO3    = 350.0
PIVO       = 120.0

class Amb:
    def __init__(s, nome):
        s.nome = nome; s.area = {}; s.fita = 0.0; s.pc = 0
        s.fer = 0.0; s.ter = 0.0; s.notas = []
    def chapa(s, esp, m2, pecas=1, fita_m=0.0):
        s.area[esp] = s.area.get(esp, 0.0) + m2
        s.pc += pecas; s.fita += fita_m
    def f(s, v, q=1, o=''):
        s.fer += v*q
        if v == 400.0: s.n_corr = getattr(s,'n_corr',0) + q
        if v == 250.0: s.n_basc = getattr(s,'n_basc',0) + q
        if v ==  50.0: s.n_dobr = getattr(s,'n_dobr',0) + q
        if o: s.notas.append('%s ×%g' % (o, q))
    def t(s, v, o=''):
        s.ter += v
        if o: s.notas.append(o)

def caixa(a, C, A, P, esp=15, prat=0, div=0, fundo=True, frente=0.0, esp_frente=18):
    """Armário C×A×P (cm). frente = m² de porta/gaveta."""
    m2 = (2*A*P + 2*C*P + prat*C*P + div*A*P)/1e4
    n  = 4 + prat + div
    per = (2*(A+P)*2 + 2*(C+P)*2 + prat*(C+P)*2 + div*(A+P)*2)/100
    a.chapa(esp, m2, n, per*0.5)          # só as bordas aparentes
    if fundo: a.chapa(6, C*A/1e4, 1)
    if frente: a.chapa(esp_frente, frente, 1, 0.0)

def frente(a, larg, alt, qtd, esp=18):
    """Portas/gavetas: área + fita nos 4 lados de cada peça."""
    a.chapa(esp, larg*alt*qtd/1e4, qtd, 2*(larg+alt)*qtd/100)

def painel(a, C, A, ripado=False, esp=18):
    m2 = C*A/1e4
    a.chapa(esp, m2*(2.0 if ripado else 1.15), 1 if not ripado else int(C/12)+1,
            2*(C+A)/100)

# ══════════════════════════════════════════════════════════════════════════
A = {}

# ─── 1 · APOIO ────────────────────────────────────────────────────────────
x = A['01 Apoio'] = Amb('01 Apoio')
caixa(x, 240, 265, 70, prat=9, div=2)          # armário de correr
frente(x, 80, 265, 3)                          # 3 portas de correr
x.f(CORR, 2, 'corrediça gaveta'); x.f(CAVA, 2)
x.t(CORRER3 + TRILHO3, 'deslizante 3 portas')
for p in range(9): x.f(SUPORTE); x.f(ALMA if 240>120 else 0)
painel(x, 383, 270)                            # painel de TV + rodapé
caixa(x, 191.2, 22, 45, prat=0, fundo=False)   # rack suspenso
x.f(CORR, 4, 'corrediça rack'); x.f(PULS, 0)
x.t(PALHINHA*191.2*22/1e4*1.1, 'frentes em palhinha (tapeceiro)')
x.t(300, 'serralheiro: fixação do rack suspenso')

# ─── 2 · ÁREA DE SERVIÇO / DESPENSA (parcial) ─────────────────────────────
x = A['02 Área de serviço'] = Amb('02 Área de serviço')
caixa(x, 212, 180, 45, prat=4)                 # estante aberta
caixa(x, 210, 90, 45, prat=0)                  # gaveteiro
frente(x, 70, 39, 6)                           # 6 gavetas
x.f(CORR, 6); x.f(CAVA, 6)
for _ in range(4): x.f(SUPORTE); x.f(ALMA)
caixa(x, 50, 270, 45, prat=2)                  # coluna lateral
caixa(x, 50, 93, 45, prat=0); frente(x, 50, 93, 1); x.f(DOBR, 2)
caixa(x, 40, 40, 45, prat=0); frente(x, 40, 40, 1); x.f(DOBR, 2)
for _ in range(3): x.f(SUPORTE)
x.t(VIDRO*79.9*209/1e4 + 200, 'porta de vidro da despensa (vidraceiro)')
x.notas.append('⚠ PARCIAL: faltam pg 1, 3, 4, 5')

# ─── 3 · BANHO SOCIAL ─────────────────────────────────────────────────────
x = A['03 Banho social'] = Amb('03 Banho social')
caixa(x, 150, 160, 15, prat=4)                 # espelheira
x.t(ESPELHO*150*160/1e4*1.1, 'espelho Crystal Prata 5mm nas 2 portas')
x.t(CORRER2, 'correr 2 portas (espelheira)')
x.t(LED*1.5*2, 'LED das duas faces')
for _ in range(4): x.f(SUPORTE)
x.chapa(18, 150*22/1e4, 1, 2*(150+22)/100)     # prateleira Imbuia

# ─── 4 · COZINHA ──────────────────────────────────────────────────────────
x = A['04 Cozinha'] = Amb('04 Cozinha')
caixa(x, 408, 90, 35, prat=1, div=4)           # superior de básculas
frente(x, 82, 35, 10); frente(x, 82, 20, 3)    # 13 básculas
x.f(BASC, 13, 'Aventos HK-xs'); x.f(PULS, 13); x.f(DOBR, 26)
caixa(x, 408.5, 60, 35, prat=1, div=2)         # armário de portas de vidro
x.t(VIDRO*408.5*60/1e4*1.1 + 200, 'portas de vidro (3 folhas)')
x.f(DOBR, 6)
caixa(x, 408.5, 80, 77, prat=0, div=3)         # balcão inferior
frente(x, 112.8, 38.5, 4)                      # 4 gavetões
x.f(CORR, 4); x.f(CAVA, 4)
caixa(x, 59.6, 70, 77, prat=0, fundo=False)    # nicho do forno
caixa(x, 70, 90, 77, prat=0, fundo=False)      # nicho lava-e-seca
caixa(x, 370, 90, 90, prat=0, div=3)           # ILHA
frente(x, 91.5, 87, 1); x.f(DOBR, 2)           # porta de abrir
frente(x, 91.5, 38.5, 4); frente(x, 91.5, 20, 2); frente(x, 91.5, 19.1, 1)
x.f(CORR, 7); x.f(CAVA, 7)
x.t(300, 'serralheiro: recorte/ponto da chopeira')
x.notas.append('⚠ ilha tem PROJ. ALVENARIA no miolo — só frentes ou corpo todo?')

# ─── 5 · ESCRITÓRIO ───────────────────────────────────────────────────────
x = A['05 Escritório'] = Amb('05 Escritório')
painel(x, 270, 270)                            # painel Gianduia
x.chapa(18, 2*260*20/1e4, 2, 2*2*(260+20)/100) # 2 prateleiras Nogueira
x.t(2*300, 'mão francesa invisível ×2 (serralheiro)')
caixa(x, 190.7, 75, 50, prat=0, div=1)         # escrivaninha com nicho
frente(x, 45, 17, 4); x.f(CORR, 4); x.f(CAVA, 4)
caixa(x, 65, 64.8, 50, prat=0, fundo=False)    # lateral

# ─── 6 · QUARTO DE HÓSPEDES ───────────────────────────────────────────────
x = A['06 Quarto de hóspedes'] = Amb('06 Quarto de hóspedes')
painel(x, 347.9, 265)                          # painel da elevação A
caixa(x, 170, 260, 60, prat=2, div=1)          # guarda-roupa de correr
x.t(VIDRO*170*260/1e4*1.1 + CORRER2 + TRILHO3, 'vidro canelado 2 folhas + correr')
frente(x, 82.5, 16, 8); x.f(CORR, 8); x.f(CAVA, 8)
for _ in range(2): x.f(SUPORTE); x.f(ALMA)
x.f(60, 1, 'cabideiro')
painel(x, 105, 265)                            # painel/porta
x.f(DOBR, 3)
painel(x, 268, 225)                            # cabeceira Freijó
caixa(x, 60, 24, 35, prat=0, fundo=False)      # mesa de cabeceira
frente(x, 29, 20, 2); x.f(CORR, 2)
x.t(PALHINHA*60*20/1e4*1.2, 'palhinha da mesa de cabeceira')
caixa(x, 60, 270, 60, prat=2)                  # torre
frente(x, 54, 18, 4); x.f(CORR, 4)
x.t(PALHINHA*54*18*4/1e4*1.2, 'palhinha das 4 gavetas da torre')
for _ in range(2): x.f(SUPORTE)

# ─── 7 · SALA DE ESTAR ────────────────────────────────────────────────────
x = A['07 Sala de estar'] = Amb('07 Sala de estar')
painel(x, 415, 198)                            # painel acima do rack
caixa(x, 415, 72, 50, prat=1, div=4)           # rack
frente(x, 82, 20, 5, esp=18); frente(x, 82, 29, 5)
x.chapa(18, (82*20*5 + 82*29*5)/1e4, 10, 0)    # ⭐ ripado vazado: 2ª camada
x.f(BASC, 5, 'Aventos HK-xs (básculas ripadas)'); x.f(PULS, 5)
x.f(CORR, 5); x.f(CAVA, 5)
painel(x, 85, 270); x.f(DOBR, 3)               # porta de abrir
painel(x, 100, 270, ripado=True)               # fixo ripado
painel(x, 70, 270, ripado=True)                # fixo ripado
painel(x, 150, 270, ripado=True)               # PORTA PIVOTANTE ripada
x.t(PIVO*3 + 600, 'pivô de alta carga p/ folha de 150×270')
x.t(300, 'puxador em barra vazado em madeira Imbuia')
x.notas.append('⚠ prancha diverge: Nogueira 5×2 (elev.) vs Ipê Champagne 5×5 (DET 01)')

# ─── 8 · SALA DE JANTAR ───────────────────────────────────────────────────
x = A['08 Sala de jantar'] = Amb('08 Sala de jantar')
caixa(x, 150, 175, 35, prat=4, div=1)          # cristaleira
x.t(VIDRO*150*175/1e4*1.1 + 200, 'portas de vidro da cristaleira')
x.f(DOBR, 4)
for _ in range(4): x.f(SUPORTE); x.f(ALMA)
caixa(x, 372.5, 87, 40, prat=0, div=3)         # gaveteiro
frente(x, 92.6, 19.3, 16); x.f(CORR, 16); x.f(CAVA, 16)
caixa(x, 150, 87, 60, prat=0, div=1)           # nicho das adegas

# ─── 14 · SUÍTE MASTER ────────────────────────────────────────────────────
x = A['14 Suíte master'] = Amb('14 Suíte master')
painel(x, 454.5, 217, ripado=True)             # painel ripado Neblina 10×1
caixa(x, 50, 24, 40, prat=0, fundo=False)      # mesa de cabeceira
frente(x, 50, 20, 1); x.f(CORR, 1)
caixa(x, 50, 24, 40, prat=0, fundo=False)      # 2ª mesa (⚠ confirmar)
frente(x, 50, 20, 1); x.f(CORR, 1)
painel(x, 345.1, 255)                          # painel Nogueira elev. B
painel(x, 80, 255); x.f(DOBR, 3)               # porta embutida
caixa(x, 297.5, 75, 50, prat=0, div=2)         # escrivaninha de 297,5
x.t(300, 'serralheiro: fixação da escrivaninha em balanço')
x.notas.append('⚠ PARCIAL: faltam pg 1, 3, 5')

# ─── 15 · BANHO DA SUÍTE MASTER ───────────────────────────────────────────
x = A['15 Banho da suíte master'] = Amb('15 Banho da suíte master')
caixa(x, 143.4, 270, 60, prat=2, div=1)        # roupeiro com cabideiro
frente(x, 71, 270, 2); x.f(DOBR, 6)
for _ in range(2): x.f(SUPORTE); x.f(ALMA)
x.f(60, 1, 'cabideiro')
caixa(x, 182, 84, 60, prat=0, div=1)           # gaveteiro
frente(x, 89, 16, 8); x.f(CORR, 8); x.f(CAVA, 8)
caixa(x, 192, 160, 20, prat=3)                 # armário espelhado
x.t(ESPELHO*192*160/1e4*1.1, 'espelho Crystal Prata 5mm, 3 folhas')
x.t(CORRER3 + TRILHO3, 'correr 3 portas')
x.t(LED*2.0*3, 'LED do armário espelhado')
for _ in range(3): x.f(SUPORTE); x.f(ALMA)
caixa(x, 192, 75, 50, prat=0, div=2)           # armário sob a bancada
frente(x, 63, 37.5, 4)
x.chapa(18, 192*75/1e4, 4, 0)                  # frente RIPADA: 2ª camada
x.f(DOBR, 8)
x.t(ESPELHO*(87.9+120.3)*200/1e4*1.1, 'espelhos das outras duas paredes')
x.t(LED*(0.9+1.2)*2, 'LED dos espelhos')
x.notas.append('⚠ PARCIAL: faltam pg 6-9, 11, 12')

# ══════════════════════════════════════════════════════════════════════════
def custo(a):
    chapas = {}; c_ch = 0.0
    for esp, m2 in sorted(a.area.items()):
        n = -(-m2 / (CHAPA_M2 * APROV[esp]) // 1)   # teto
        n = int(max(1, n)); chapas[esp] = n; c_ch += n * MDF[esp]
    c_fita = a.fita * 1.15 * (FITA + FILETAGEM)
    c_cons = (c_ch + c_fita) * CONSUM
    c_corte = sum(chapas.values())*CORTE_CH + a.pc*CORTE_PC
    direto = c_ch + c_fita + c_cons + c_corte + a.fer + a.ter
    return dict(chapas=chapas, ch=c_ch, fita=c_fita, cons=c_cons,
                corte=c_corte, fer=a.fer, ter=a.ter,
                cd=M.com_embalagem(direto))

if __name__ == '__main__':
    import json
    out = {}
    for k in sorted(A):
        out[k] = custo(A[k]); out[k]['notas'] = A[k].notas
    print(json.dumps(out, ensure_ascii=False, default=float))
