# -*- coding: utf-8 -*-
"""CONCESSIONÁRIA HONDA — MINAS MOTOS SANTA EFIGÊNIA · marcenaria do SHOWROOM.

Fonte: 653_HON_EX_V1_AR18_R07.pdf — prancha AR-18, projeto EXECUTIVO,
Mímesis Arquitetura e Interiores (CAU-MG PJ34.285-8), rev. 07 de 06/08/2026
("ALTERAÇÃO SHOWROOM"). Cliente: Aliança Imobiliária Ltda.
Obra: Av. do Contorno, 3585 — Santa Efigênia, BH/MG.

═══════════════════════════════════════════════════════════════════════════════
O ESCOPO DE MARCENARIA SÃO DUAS PEÇAS — E SÓ DUAS.
═══════════════════════════════════════════════════════════════════════════════
A prancha traz DUAS tabelas separadas: "ESPECIFICAÇÃO DE MOBILIÁRIO" (MB01 a
MB40) e "ESPECIFICAÇÃO DE MARCENARIA" (MA01, MA02). Os 40 itens MB são padrão
Honda, Home Office, Leroy Merlin, Madeira Madeira — mobiliário comprado, NÃO é
marcenaria. Idem BG07 (bancada, outra disciplina) e os MB de padrão Honda
(balcão de peças, recepção, expositores, display Pro Honda, elevador de moto).

  MA-01  ARMÁRIO SUPERIOR — MDF AMÊNDOLA RÚSTICA (Duratex), básculas e
         prateleiras com detalhe em METALON pintura eletrostática PRETO
  MA-02  ARMÁRIO INFERIOR — MDF PALHA (Duratex), gavetas e portas de giro

═══════════════════════════════════════════════════════════════════════════════
GEOMETRIA — extraída dos vetores do PDF, não do olho.
═══════════════════════════════════════════════════════════════════════════════
Escala aferida no próprio desenho: 1,134 pt/cm (= 1/25 exato). Cada linha do
DWG foi lida em coordenada e convertida; as cotas anotadas conferem com o
traçado em todas as cadeias. Nota 2 da prancha: a cota anotada prevalece.

MA-01 — VISTA FRONTAL, prof. 30 cm, topo a 224 cm do piso acabado
  Largura 315,5 = [2+2+2] + 69,5 + 70 + 70 + [2+2+2] + 88 + [2+2+2]
  Os três grupos de 2+2+2 são as três PRUMADAS: MDF 2 · metalon 2 · MDF 2.
  Cadeia vertical esq.:  40 (básculas) · 30 · 2 (prateleira) · 62 · 90 (BG07)
  Cadeia vertical dir.:  2 · 36 (nicho) · 2 · 30 · 2 · 30 · 2 · 30
  Alturas apuradas (do piso):  topo 224 · fundo do caixote 184 ·
    prateleira longa 154/152 · prateleira do vão direito 122/120 ·
    metalon esq. 225,9→150,0 · metalon meio e dir. 225,9→118,0
  ⇒ Caixote A  213 × 40 × 30 — 3 básculas de 69,5 / 70 / 70 (vão livre 209,2)
    Caixote B   92 × 40 × 30 — NICHO ABERTO 88 × 36 (interior todo aparente)
    Prateleiras abertas apoiadas no metalon: 213 (alta) · 92 (alta) · 92 (baixa)

MA-02 — VISTA SUPERIOR + VISTA 01 + VISTA 02. Móvel em "L", altura 84 =
  sóculo 10 + corpo 74 (tampo 2 + frentes 72).
  A VISTA 01 está ESPELHADA em relação à planta — conferido por dois caminhos
  independentes: (a) o módulo hachurado de 55 na ponta direita da elevação é a
  perna B em corte, que na planta está à esquerda; (b) a sequência de módulos da
  planta (39,9 | 75,9 | 51,9) só fecha com as frentes da elevação
  (39 | 39+39 | gaveteiro 55) lida ao contrário. Bate nos dois.

  Perna A (VISTA 01)  corpo próprio 173,9 · prof. 57 — 1+2 portas de 39 e
                      gaveteiro de 55 com 4 gavetas de 16,5
  Perna B (VISTA 02)  corpo próprio 141,5 · prof. 60 — portas de 46 / 46 / 45,5
                      + 60,8 de CANTO CEGO (sem frente)
  Extensão total: perna A 234 (inclui o canto) · perna B 202 (inclui o canto).
  Frentes somadas 173,9 + 141,5 = 315,4 — o canto é contado uma vez só, na B.

  Puxador: CAVA EMBUTIDA usinada na própria frente (DT-01 inferior nas básculas
  do MA-01, DT-02 superior com tampo no MA-02). Não é perfil comprado.

Notas da prancha aplicadas: conferir medidas no local · conferir a parede de
fixação, drywall pede bucha específica · FIXAÇÃO INVISÍVEL · dobradiças COM
AMORTECIMENTO.
"""
from collections import defaultdict

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75 * 1.85                       # 5,0875 m²

# ── base de custos — dados/materiais.json (fonte única de verdade) ───────────
BRC6, BRC15, BRC18 = 190.0, 260.0, 330.0
COR18              = 600.0                  # MDF Melamínico Fosco 18mm (a linha da cor)

# Só há 18 mm nas duas cores: consolidar espessura dentro de cada cor derrubou
# 2 chapas (−R$ 1.000). No MA-01 a caixaria em 18 mm ainda é ganho estrutural —
# é um aéreo de 3,15 m em balanço. No MA-02 só o sóculo e a lateral aparente
# subiram de 15 para 18.
PRECO = {'BRC6': BRC6, 'BRC15': BRC15, 'BRC18': BRC18,
         'AMR18': COR18,                          # Amêndola Rústica — MA-01
         'PLH18': COR18}                          # Palha            — MA-02

FITA_BRC, FITA_COR = 2.0, 3.0               # R$/m  (+10% desperdício)
FILET_MAQ          = 2.50                   # R$/m — coladeira automática

DOBR_SENSYS  = 35.0    # un — Hettich Sensys c/ amortecimento (nota 4 da prancha)
PISTAO_AMORT = 30.0    # un — pistão a gás com amortecimento (báscula)
CORR_OCULTA  = 70.0    # par — Corrediça Oculta Hardt
SUP_PRAT     = 1.50    # un
USIN_CAVA    = 25.0    # R$/m — usinagem da cava embutida na CNC
FIX_INVIS    = 50.0    # un — suporte/mão-francesa oculta + bucha estrutural

# Serralheria MA-01 — 3 pórticos de metalon 20×20 com pintura eletrostática
# preta. ~9 m de barra + corte/solda + pintura + frete.
# [Jonathan 07/08] CRAVOU R$ 600 — eu tinha estimado 1.200 sem tabela da casa.
METALON_PACK = 600.0

# ── peças  (material, descrição, comprimento, largura, qtd) ─────────────────
pecas = [
    # ═════════ MA-01 — ARMÁRIO SUPERIOR · Amêndola Rústica · prof. 30 ═══════
    # Caixote A — 213 × 40 × 30, três básculas. A BASE (face de baixo) é o que se
    # vê — é aéreo a 1,84 m do piso —, então vai na cor. O TAMPO não se vê e o
    # FUNDO encosta na parede [correção do Jonathan 07/08]: os dois em branco.
    ('AMR18', 'MA-01 · caixote A — lateral',                     40,  30, 2),
    ('AMR18', 'MA-01 · caixote A — base (aparente por baixo)',  213,  30, 1),
    ('BRC15', 'MA-01 · caixote A — tampo',                      213,  30, 1),
    ('BRC15', 'MA-01 · caixote A — divisória interna ⚠ ADIÇÃO',  36,  30, 2),
    ('BRC6',  'MA-01 · caixote A — fundo',                      213,  40, 1),
    ('AMR18', 'MA-01 · báscula 69,5',                          69.5,  36, 1),
    ('AMR18', 'MA-01 · báscula 70',                              70,  36, 2),

    # Caixote B — 92 × 40 × 30, NICHO ABERTO. Aqui o fundo É visto — não pela
    # parede, mas POR DENTRO, através do vão aberto de 88 × 36. Vai na cor, e sai
    # da sobra da chapa de 18 mm — evita puxar uma chapa de 6 mm da cor p/ 0,37 m².
    ('AMR18', 'MA-01 · caixote B (nicho) — lateral',             40,  30, 2),
    ('AMR18', 'MA-01 · caixote B (nicho) — tampo',               92,  30, 1),
    ('AMR18', 'MA-01 · caixote B (nicho) — base',                92,  30, 1),
    ('AMR18', 'MA-01 · caixote B (nicho) — fundo visto pelo vão', 92,  40, 1),

    # Prateleiras abertas sobre o metalon — aparentes dos dois lados.
    ('AMR18', 'MA-01 · prateleira longa (vão 213)',             213,  30, 1),
    ('AMR18', 'MA-01 · prateleira do vão direito',               92,  30, 2),

    # ═════════ MA-02 — ARMÁRIO INFERIOR EM "L" · Palha · alt. 84 ════════════
    # Perna A — corpo 174 × 57 prof. Módulos da planta: 39,9 | 75,9 | 51,9.
    ('BRC15', 'MA-02 · perna A — vertical (2 laterais + 2 div.)', 74,  57, 4),
    ('BRC15', 'MA-02 · perna A — base',                          174,  57, 1),
    ('PLH18', 'MA-02 · perna A — tampo/bancada do móvel',        174,  57, 1),
    ('BRC6',  'MA-02 · perna A — fundo',                         174,  74, 1),
    ('PLH18', 'MA-02 · perna A — porta de giro 39',               39,  72, 3),
    ('BRC18', 'MA-02 · perna A — prateleira (módulo 39)',         37,  55, 1),
    ('BRC18', 'MA-02 · perna A — prateleira (módulo 76)',         74,  55, 1),

    # Gaveteiro de 55 — 4 gavetas de 16,5 (frentes com cava entre elas).
    ('PLH18', 'MA-02 · frente de gaveta 55 × 16,5',               55, 16.5, 4),
    ('BRC15', 'MA-02 · gaveta — lateral',                         50,  14, 8),
    ('BRC15', 'MA-02 · gaveta — frente interna e costas',         47,  14, 8),
    ('BRC6',  'MA-02 · gaveta — fundo',                           47,  50, 4),

    # Perna B — 202 de extensão (inclui o canto cego de 60,8) × 60 prof.
    ('BRC15', 'MA-02 · perna B — vertical (2 laterais + 2 div.)', 74,  60, 4),
    ('BRC15', 'MA-02 · perna B — base',                          202,  60, 1),
    ('PLH18', 'MA-02 · perna B — tampo/bancada do móvel',        202,  60, 1),
    ('BRC6',  'MA-02 · perna B — fundo',                         202,  74, 1),
    ('PLH18', 'MA-02 · perna B — porta de giro 46',               46,  72, 2),
    ('PLH18', 'MA-02 · perna B — porta de giro 45,5',           45.5,  72, 1),
    ('BRC18', 'MA-02 · perna B — prateleira (módulo 92)',         90,  58, 1),
    ('BRC18', 'MA-02 · perna B — prateleira (módulo 48 + canto)', 48,  58, 1),

    # Sóculo recuado h=10 e a lateral aparente da ponta do "L".
    ('PLH18', 'MA-02 · sóculo — perna A',                        174,  10, 1),
    ('PLH18', 'MA-02 · sóculo — perna B',                        202,  10, 1),
    ('PLH18', 'MA-02 · sóculo — retornos laterais',               60,  10, 2),
    ('PLH18', 'MA-02 · lateral aparente da ponta',                74,  57, 1),
]

# ── fita: só as bordas que aparecem ────────────────────────────────────────
fitas = [
    # MA-01 — cor
    ('COR', 'MA-01 · básculas — perímetro',      2*(0.695+0.36) + 2*2*(0.70+0.36)),
    ('COR', 'MA-01 · caixote A — frentes de tampo, base e laterais',
                                                 2*2.13 + 2*0.40),
    ('COR', 'MA-01 · nicho — bordas aparentes',  2*0.92 + 2*0.40),
    ('COR', 'MA-01 · prateleira longa — frente e laterais',   2.13 + 2*0.30),
    ('COR', 'MA-01 · prateleiras do vão direito', 2*(0.92 + 2*0.30)),
    ('BRC', 'MA-01 · tampo e divisórias — canto frontal',     2.13 + 2*0.30),
    # MA-02 — cor
    ('COR', 'MA-02 · portas de giro — perímetro',
                                3*2*(0.39+0.72) + 2*2*(0.46+0.72) + 2*(0.455+0.72)),
    ('COR', 'MA-02 · frentes de gaveta — perímetro',   4*2*(0.55+0.165)),
    ('COR', 'MA-02 · tampo — frente e topos laterais', 1.74 + 0.57 + 2.02 + 0.60),
    ('COR', 'MA-02 · sóculo — borda superior',         1.74 + 2.02 + 2*0.60),
    ('COR', 'MA-02 · lateral aparente da ponta',       0.74 + 0.57),
    # MA-02 — branco (interno)
    ('BRC', 'MA-02 · verticais — canto frontal',       8*0.74),
    ('BRC', 'MA-02 · bases — frente',                  1.74 + 2.02),
    ('BRC', 'MA-02 · prateleiras — frente',            0.37 + 0.74 + 0.90 + 0.48),
    ('BRC', 'MA-02 · caixas de gaveta — borda superior', 4*(2*0.50 + 2*0.47)),
]

# ── nesting (função da casa) ───────────────────────────────────────────────
# Dois empacotadores por faixa guilhotinada, varridos em quatro ordenações cada,
# ficando com o melhor de tudo. Qualquer resultado é um plano de corte REAL —
# faixa guilhotinada é exatamente como a serra opera.
#
# ⚠ APRENDIZADO [Honda 07/08/2026] — o de "faixa corrente" (o único que a casa
# tinha) só tenta encaixar a peça na ÚLTIMA faixa aberta. Quando aparece uma peça
# larga no meio da fila, ele abre faixa nova e abandona a sobra das anteriores.
# Aqui isso custou uma chapa inteira de Amêndola: 3,98 m² (78% de UMA chapa) saía
# em 2. Empacotando à mão fecha em 1 com 166 dos 185 cm usados. O best-fit
# abaixo procura a MELHOR faixa já aberta em qualquer chapa e acha o mesmo 1.
def _pack_faixa(pcs):
    chapas = 0; y = x = faixa = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: chapas += 1; continue
        if x + c > CH_C: y += faixa; x = 0.0; faixa = 0.0
        if y + l > CH_L: chapas += 1; y = x = faixa = 0.0
        x += c; faixa = max(faixa, l)
    return chapas + 1

def _pack_bf(pcs):
    ch = []                    # ch[i] = [altura_usada, [[alt_faixa, sobra_larg], ...]]
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch.append([CH_L, []]); continue
        best = None
        for s in ch:
            for fx in s[1]:
                if fx[0] >= l and fx[1] >= c and (best is None or fx[1] < best[1]):
                    best = fx
        if best is not None: best[1] -= c; continue
        for s in ch:
            if s[0] + l <= CH_L:
                s[0] += l; s[1].append([l, CH_C - c]); break
        else:
            ch.append([l, [[l, CH_C - c]]])
    return len(ch)

def nest(items):
    if not items: return 0
    base = [(max(c, l), min(c, l)) for c, l in items]
    ordens = [lambda p: -p[1], lambda p: (-p[1], -p[0]),
              lambda p: -p[0], lambda p: -p[0]*p[1]]
    chapas = min(pk(sorted(base, key=k))
                 for pk in (_pack_faixa, _pack_bf) for k in ordens)
    area = sum(c*l for c, l in items)/10000
    return max(chapas, -(-int(area/(CH_AREA*0.80)*1000)//1000) or 1)

por_mat, area_mat = defaultdict(list), defaultdict(float)
for mat, desc, c, l, q in pecas:
    for _ in range(q):
        por_mat[mat].append((c, l))
        area_mat[mat] += c*l/10000
CHAPAS = {m: nest(v) for m, v in por_mat.items()}

# rateio por móvel (para separar MA-01 de MA-02 no orçamento)
area_movel = defaultdict(float)
for mat, desc, c, l, q in pecas:
    area_movel['MA-01' if desc.startswith('MA-01') else 'MA-02'] += c*l*q/10000

print('═'*94)
print('HONDA · MINAS MOTOS SANTA EFIGÊNIA — MARCENARIA DO SHOWROOM  (prancha AR-18 R07)')
print('═'*94)
print('\nESCOPO')
for d in ('MA-01  Armário superior  315,5 × 30 prof · topo a 224 do piso · Amêndola Rústica',
          '       3 básculas (69,5 / 70 / 70 × 36) · nicho aberto 88 × 36 · 3 prateleiras',
          '       3 prumadas de metalon 20×20 com pintura eletrostática preta',
          'MA-02  Armário inferior em "L" · alt. 84 (sóculo 10 + corpo 74) · Palha',
          '       Perna A 234 (corpo 174 × 57) — 3 portas de 39 + gaveteiro de 4 gavetas',
          '       Perna B 202 (corpo 141,5 × 60) — portas de 46 / 46 / 45,5 + canto cego',
          '       Puxador em cava embutida usinada (DT-01 e DT-02)'):
    print('  ' + d)

print('\nPLANO DE CORTE  (nesting por cor × espessura — cores nunca dividem chapa)')
custo_chapa = 0.0
NOME = {'BRC6': 'Branco 6', 'BRC15': 'Branco 15', 'BRC18': 'Branco 18',
        'AMR18': 'Amêndola 18', 'PLH18': 'Palha 18'}
for m in sorted(CHAPAS, key=lambda k: (k[:3], k)):
    n = CHAPAS[m]; c = n*PRECO[m]; custo_chapa += c
    ap = area_mat[m]/(n*CH_AREA)*100
    print(f'  {NOME[m]:<13}{area_mat[m]:>6.2f} m²  →  {n} chapa(s) × R$ {PRECO[m]:>6.2f}'
          f'  = R$ {c:>8,.2f}   aprov. {ap:>3.0f}%')
tot_ch = sum(CHAPAS.values()); area_tot = sum(area_mat.values())
print(f'  {"TOTAL":<13}{area_tot:>6.2f} m²  →  {tot_ch} chapas'
      f'                    R$ {custo_chapa:>8,.2f}   médio '
      f'{area_tot/(tot_ch*CH_AREA)*100:.0f}%')
print(f'  Área por móvel:  MA-01 {area_movel["MA-01"]:.2f} m²  ·  '
      f'MA-02 {area_movel["MA-02"]:.2f} m²')

print('\nFITA DE BORDA  (+10% de desperdício)')
m_cor = sum(m for t, _, m in fitas if t == 'COR')
m_brc = sum(m for t, _, m in fitas if t == 'BRC')
custo_fita  = m_cor*1.10*FITA_COR + m_brc*1.10*FITA_BRC
custo_filet = (m_cor + m_brc)*FILET_MAQ
for t, d, m in fitas:
    print(f'  {d:<56}{m:>7.2f} m   {t}')
print(f'  {"— cor (Amêndola + Palha)":<56}{m_cor:>7.2f} m × R$ {FITA_COR:.2f}')
print(f'  {"— branco":<56}{m_brc:>7.2f} m × R$ {FITA_BRC:.2f}')
print(f'  {"material da fita":<56}{m_cor+m_brc:>7.2f} m       R$ {custo_fita:>8,.2f}')
print(f'  {"filetagem na coladeira":<56}{m_cor+m_brc:>7.2f} m × R$ {FILET_MAQ:.2f} '
      f'= R$ {custo_filet:>8,.2f}')

print('\nFERRAGENS E USINAGEM')
N_DOBR  = 6*2                      # 6 portas de giro de 72 cm → 2 dobradiças cada
N_PIST  = 3*2                      # 3 básculas → 2 pistões a gás cada
N_GAV   = 4
N_PRAT  = 4                        # prateleiras do MA-02 (as do MA-01 vão no metalon)
M_CAVA  = (0.695+0.70+0.70) + 4*0.55 + (3*0.39 + 2*0.46 + 0.455)
N_FIX   = 8                        # pontos de fixação invisível do aéreo de 3,15 m
ferr = [
    (f'Dobradiça Hettich Sensys c/ amortecimento — {N_DOBR} un', N_DOBR*DOBR_SENSYS),
    (f'Pistão a gás com amortecimento (básculas) — {N_PIST} un', N_PIST*PISTAO_AMORT),
    (f'Corrediça oculta Hardt — {N_GAV} pares',                  N_GAV*CORR_OCULTA),
    (f'Suporte de prateleira — {N_PRAT*4} un',                   N_PRAT*4*SUP_PRAT),
    (f'Usinagem da cava embutida (DT-01/DT-02) — {M_CAVA:.2f} m', M_CAVA*USIN_CAVA),
    (f'Fixação invisível do MA-01 — {N_FIX} pontos',             N_FIX*FIX_INVIS),
]
custo_ferr = sum(v for _, v in ferr)
for d, v in ferr: print(f'  {d:<62}R$ {v:>8,.2f}')
print(f'  {"TOTAL":<62}R$ {custo_ferr:>8,.2f}')

print('\nTERCEIRIZADO')
print(f'  {"Serralheria — 3 pórticos metalon 20×20 c/ pint. eletrostática ⚠":<62}'
      f'R$ {METALON_PACK:>8,.2f}')

# ── fechamento de custo ────────────────────────────────────────────────────
consum = (custo_chapa + custo_fita)*0.06
MAT    = custo_chapa + custo_fita + custo_filet + custo_ferr + consum + METALON_PACK
CARRETO, VISITA, INSTAL = 600.0, 500.0, 1800.0
LOG = CARRETO + VISITA + INSTAL
fixedR = MAT + LOG

print('\n' + '─'*94)
print(f'  {"Chapas":<62}R$ {custo_chapa:>8,.2f}')
print(f'  {"Fita (material)":<62}R$ {custo_fita:>8,.2f}')
print(f'  {"Filetagem (aplicação)":<62}R$ {custo_filet:>8,.2f}')
print(f'  {"Ferragens e usinagem":<62}R$ {custo_ferr:>8,.2f}')
print(f'  {"Serralheria (metalon)":<62}R$ {METALON_PACK:>8,.2f}')
print(f'  {"Consumíveis (6% de chapa + fita)":<62}R$ {consum:>8,.2f}')
print(f'  {"Carretos · 2 visitas técnicas · instalação (3 dias de dupla)":<62}'
      f'R$ {LOG:>8,.2f}')
print(f'  {"CUSTO DIRETO":<62}R$ {fixedR:>8,.2f}')

# rateio proporcional à área de chapa, com os itens exatos atribuídos
cd_ma01_exato = METALON_PACK + N_PIST*PISTAO_AMORT + N_FIX*FIX_INVIS \
              + (0.695+0.70+0.70)*USIN_CAVA
cd_ma02_exato = N_DOBR*DOBR_SENSYS + N_GAV*CORR_OCULTA + N_PRAT*4*SUP_PRAT \
              + (4*0.55 + 3*0.39 + 2*0.46 + 0.455)*USIN_CAVA
rateavel = fixedR - cd_ma01_exato - cd_ma02_exato
p01 = area_movel['MA-01']/area_tot
cd01 = cd_ma01_exato + rateavel*p01
cd02 = cd_ma02_exato + rateavel*(1-p01)

# ── preço ──────────────────────────────────────────────────────────────────
# a=0,162 · liqF=0,88 · b=0,043 — este conjunto JÁ É a configuração SEM RT.
a_, liqF_, b_ = 0.162, 0.88, 0.043
def div_(mc, rt): return 1 - a_ - liqF_*b_ - mc - (liqF_*0.10 if rt else 0.0)

MC, RT = 0.35, False   # [Jonathan 07/08] sem RT · MC 32% → 35%
div = div_(MC, RT)
inv01 = round(cd01/div/100)*100
inv02 = round(cd02/div/100)*100
tabela = inv01 + inv02

print('\n' + '═'*94)
print(f'PREÇO — MC {MC*100:.0f}% · {"COM" if RT else "SEM"} RT · divisor {div:.5f}')
print('═'*94)
print(f'  MA-01 · Armário superior   R$ {cd01:>9,.2f} ÷ {div:.5f} = '
      f'R$ {cd01/div:>9,.2f}  →  R$ {inv01:>7,.0f}')
print(f'  MA-02 · Armário inferior   R$ {cd02:>9,.2f} ÷ {div:.5f} = '
      f'R$ {cd02/div:>9,.2f}  →  R$ {inv02:>7,.0f}')
print(f'  {"TOTAL DE TABELA":<52}          R$ {tabela:>7,.0f}')
print(f'  MC conferida: {(tabela - tabela*(a_+liqF_*b_) - fixedR)/tabela*100:.1f}%')

# ── teste de sanidade: R$ por m² de chapa, contra jobs já fechados ─────────
print('\n  SANIDADE — R$ de venda por m² de chapa')
for rot, rs, m2 in (('Cozinha Rizzi (residencial)',   36700, 58.64),
                    ('Armário superior de cozinha',    9700, 15.00),
                    ('SPE decorado (comercial)',     101200, 137.00),
                    ('→ HONDA showroom',             tabela, area_tot)):
    print(f'    {rot:<30}{rs/m2:>7,.0f} R$/m²')
fixo = METALON_PACK + N_FIX*FIX_INVIS + LOG
print(f'    Acima da faixa porque é job PEQUENO com custo fixo alto: serralheria,')
print(f'    fixação invisível e 3 dias de instalação = {fixo/fixedR*100:.0f}% do custo direto')
print(f'    (R$ {fixo:,.2f} de R$ {fixedR:,.2f}). R$ {tabela/tot_ch:,.0f} por chapa em {tot_ch} chapas.')

print('\n  ESCADA DE PAGAMENTO (padrão da casa)')
for d, desc in [('Entrada 30% + até 10× no cartão', 0.00),
                ('Entrada 50% + até 8× no cartão',  0.03),
                ('Entrada 70% + até 6× no cartão',  0.05),
                ('Entrada 70% + restante em transferência', 0.07)]:
    v = round(tabela*(1-desc)/100)*100
    mc_v = (v - v*(a_+liqF_*b_) - fixedR)/v*100
    print(f'    {d:<46}{"—" if not desc else f"−{desc*100:.0f}%":>5}   '
          f'R$ {v:>8,.0f}   MC {mc_v:.1f}%')

print('\n' + '═'*94)
print('SENSIBILIDADE — a RT pesa mais que a MC')
print('═'*94)
print(f'  {"":<8}{"sem RT":>14}{"com RT 10%":>14}')
for mc in (0.30, 0.35, 0.40):
    s = round(fixedR/div_(mc, False)/100)*100
    c = round(fixedR/div_(mc, True)/100)*100
    print(f'  MC {mc*100:.0f}% {s:>13,.0f} {c:>13,.0f}')
print('  Projeto de escritório de arquitetura (Mímesis) — CONFIRMAR se há RT.')

print('\n' + '─'*94)
print('✅ FECHADO PELO JONATHAN [07/08]')
for f in ('RT: NÃO tem. MC 35% (subiu de 32%).',
          'Chapa Duratex Amêndola Rústica e Palha na linha Fosco (18 mm R$ 600) — confirmado.',
          'Serralheria do metalon: R$ 600 (eu tinha estimado 1.200).',
          'Tampo do MA-02 em MDF Palha 18 mm — confirmado, não é pedra.',
          'Fixação invisível do MA-01 orçada como está — conferir a parede na obra.',
          'Pagamento: 50% de entrada + 50% na entrega.',
          'O FUNDO do MA-01 encosta na parede — em branco. Só a BASE vai na cor.'):
    print('  · ' + f)

print('\n⚠ PREMISSAS ASSUMIDAS (não estão na prancha) — valem para a produção')
for f in ('Interno BRANCO, exceto o nicho do MA-01, que é aberto e vai todo na cor.',
          '2 divisórias internas no caixote A: a prancha desenha 209 cm de vão sem apoio,',
          '  que empenaria tampo e base. Ficam atrás das básculas fechadas.',
          '1 prateleira por módulo de porta no MA-02 (4 no total) — a prancha não desenha.',
          'Travessa de metalon sob a prateleira de 213 cm do MA-01 (flexiona em 18 mm).',
          'FORA DO ESCOPO: cervejeira, adega, bancada BG07 e os 40 itens MB.'):
    print('  · ' + f if not f.startswith('  ') else '   ' + f.strip())
