# -*- coding: utf-8 -*-
"""BRINQUEDOTECA — decomposição física peça a peça, com croqui.

[Jonathan 30/09] "um processo que utilizo muito e me ajuda a ter clareza é
fazer alguns croquis de cada peça e estimar o custo relacionado a ela. Por
exemplo, pega uma parede e desenha ela, vendo quantos perfis de metalon de
50×30 serão necessários."

⛔ O QUE ISTO CORRIGE: a primeira estimativa usou R$/m² adotado — número
   agregado, indefensável linha a linha. Aqui cada peça é desenhada, o
   perfil é contado e o custo sai da SOMA DAS PARTES. O preço do metalon é
   commodity e eu sei checar; "R$ 190/m² de parede estruturada" não era
   checável por ninguém.
"""
import math, pathlib
P = pathlib.Path(__file__).resolve().parent

# ── insumos de serralheria (preço de barra de 6 m, mercado BH) ───────────
# ★ a cotar, mas são COMMODITY — erram pouco e o Jonathan sabe conferir
BARRA = 6.0
MET = {                       # perfil: (R$/barra 6m, kg/m)
 '50x30x1,2' : (95.0,  1.44),   # parede, gradil — carga leve
 '40x40x1,5' : (122.0, 1.75),   # travamento, plataforma
 '60x40x2,0' : (210.0, 2.93),   # ESTRUTURAL — recebe pessoas
 '30x30x1,2' : (62.0,  1.03),   # frisos, arremates
}
def m_lin(perfil): return MET[perfil][0]/BARRA          # R$/m de material

MO_SERR   = 24.0    # ★ R$/m de perfil trabalhado: corte, solda, esmerilho, esquadro
CONSUM_S  = 0.07    # ★ eletrodo, disco, primer — 7% do material
CHUMB     = 4.20    # ★ parabolt 3/8 + bucha, por ponto
PARAF_M2  = 4.90    # ★ parafuso chapa-metalon, por m² de chapa

MDF_U18, MDF_U15 = 320.0, 260.0     # ★ MDF ultra premium cru
CH_UTIL = 2.75*1.85*0.85            # 85% de aproveitamento
SELAR_M2 = 18.0                     # ★ selador + lixa, preparo p/ pintura

ESPUMA_D23_M3 = 980.0   # ★ espuma D23 em placa
COURVIN_M2    = 58.0    # ★ courvin náutico
COSTURA_M2    = 95.0    # ★ corte e costura
PINT_AUTO_M2  = 220.0   # ★ cabine: primer, base, verniz

PECAS = []
def peca(nome, dim, linhas, obs=''):
    """linhas = [(descrição, quantidade, unidade, R$ unitário)]"""
    tot = sum(q*v for _, q, _, v in linhas)
    PECAS.append(dict(nome=nome, dim=dim, linhas=linhas, total=tot, obs=obs))
    return tot

# ══════════════════════════════════════════════════════════════════════════
# PEÇA 1 · PAREDE CENOGRÁFICA — o exemplo do Jonathan
# ══════════════════════════════════════════════════════════════════════════
# parede tipo 4,00 × 2,80 m · montante 50×30 a cada 60 cm · travessa a cada 1 m
L, H = 4.00, 2.80
n_mont = math.ceil(L/0.60) + 1                 # 8 montantes
m_mont = n_mont*H                              # 22,4 m
n_trav = math.ceil(H/1.00) + 1                 # 4 travessas
m_trav = n_trav*L                              # 16,0 m
m_perf = m_mont + m_trav                       # 38,4 m
n_chumb = n_mont*2 + n_trav*2                  # topo/base dos montantes + pontas
m2 = L*H
n_chapa = math.ceil(m2/CH_UTIL*10)/10

peca('Parede cenográfica (tipo)', f'{L:.2f} × {H:.2f} m = {m2:.2f} m²', [
 (f'Metalon 50×30×1,2 — {n_mont} montantes de {H:.2f} m',  m_mont, 'm', m_lin('50x30x1,2')),
 (f'Metalon 50×30×1,2 — {n_trav} travessas de {L:.2f} m',  m_trav, 'm', m_lin('50x30x1,2')),
 ('Mão de obra de serralheria',                            m_perf, 'm', MO_SERR),
 ('Consumível de solda e primer',        m_perf*m_lin('50x30x1,2'), 'vb', CONSUM_S),
 (f'Chumbador na alvenaria e laje — {n_chumb} pontos',     n_chumb, 'un', CHUMB),
 (f'MDF ultra premium 18 mm — {n_chapa:.1f} chapas',       n_chapa, 'chapa', MDF_U18),
 ('Parafuso de fixação chapa/metalon',                         m2, 'm²', PARAF_M2),
 ('Selagem e lixa — preparo para a pintura do cliente',        m2, 'm²', SELAR_M2),
], obs=f'{m_perf:.1f} m de metalon para {m2:.2f} m² de parede')

# ══════════════════════════════════════════════════════════════════════════
# PEÇA 2 · PASSARELA — estrutura que RECEBE PESSOAS
# ══════════════════════════════════════════════════════════════════════════
# 5,53 × 0,60 m a +2,85 · vão livre entre apoios ~2,7 m · 60×40×2,0
Lp, Bp = 5.53, 0.60
m_long = 2*Lp                                   # 2 longarinas
n_trans = math.ceil(Lp/0.50) + 1                # travessas a cada 50 cm
m_trans = n_trans*Bp
n_mao = 4                                       # mãos-francesas de apoio
m_mao = n_mao*0.85
m_pass = m_long + m_trans + m_mao
m2p = Lp*Bp

peca('Passarela estruturada', f'{Lp:.2f} × {Bp:.2f} m, a +2,85 m', [
 ('Metalon 60×40×2,0 — 2 longarinas',                m_long, 'm', m_lin('60x40x2,0')),
 (f'Metalon 40×40×1,5 — {n_trans} travessas',       m_trans, 'm', m_lin('40x40x1,5')),
 (f'Metalon 60×40×2,0 — {n_mao} mãos-francesas',      m_mao, 'm', m_lin('60x40x2,0')),
 ('Mão de obra de serralheria (solda estrutural)',   m_pass, 'm', MO_SERR*1.35),
 ('Consumível de solda',              m_pass*m_lin('60x40x2,0'), 'vb', CONSUM_S),
 ('Chumbador estrutural 1/2" — 16 pontos',               16, 'un', CHUMB*2.2),
 ('Compensado naval 18 mm (piso da passarela)',         1.0, 'chapa', 380.0),
 ('Piso vinílico',                                      m2p, 'm²', 120.0),
 ('Pintura automotiva (superfície desenvolvida)',   m2p*2.6, 'm²', PINT_AUTO_M2),
], obs=f'{m_pass:.1f} m de metalon · vão livre ~2,7 m entre apoios')

# ══════════════════════════════════════════════════════════════════════════
# PEÇA 3 · PLATAFORMA ACOLCHOADA (uma das cinco)
# ══════════════════════════════════════════════════════════════════════════
Lpl, Bpl, Hpl = 0.95, 0.60, 0.57
m_quadro = 2*(Lpl+Bpl)                          # quadro do tampo
m_pes = 4*Hpl                                   # 4 pés
m_trav_pl = 2*Bpl                               # travamento
m_pl = m_quadro + m_pes + m_trav_pl
m2pl = Lpl*Bpl
esp = 0.05                                      # espuma de 5 cm

peca('Plataforma acolchoada (cada)', f'{Lpl:.2f} × {Bpl:.2f} m, degrau de {Hpl:.2f} m', [
 ('Metalon 40×40×1,5 — quadro do tampo',           m_quadro, 'm', m_lin('40x40x1,5')),
 ('Metalon 40×40×1,5 — 4 pés e travamento',   m_pes+m_trav_pl, 'm', m_lin('40x40x1,5')),
 ('Mão de obra de serralheria',                        m_pl, 'm', MO_SERR),
 ('Consumível de solda',              m_pl*m_lin('40x40x1,5'), 'vb', CONSUM_S),
 ('Compensado naval 15 mm (base do tampo)',            0.25, 'chapa', 330.0),
 ('Espuma D23 de 5 cm',                          m2pl*esp, 'm³', ESPUMA_D23_M3),
 ('Courvin náutico (topo e saia)',                m2pl*2.1, 'm²', COURVIN_M2),
 ('Corte, costura e grampeamento',                m2pl*2.1, 'm²', COSTURA_M2),
 ('Pintura automotiva da estrutura aparente',      m2pl*1.4, 'm²', PINT_AUTO_M2),
 ('Chumbador — 4 pontos',                                 4, 'un', CHUMB),
], obs=f'{m_pl:.1f} m de metalon por plataforma · são 5 no projeto')

# ══════════════════════════════════════════════════════════════════════════
# CROQUIS
# ══════════════════════════════════════════════════════════════════════════
def svg_parede():
    esc = 90          # px por metro
    ox, oy = 70, 50
    w, h = L*esc, H*esc
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w+200}" height="{h+200}" '
         f'font-family="DejaVu Sans, sans-serif">',
         f'<rect width="100%" height="100%" fill="#fff"/>']
    # chapa de MDF ao fundo
    s.append(f'<rect x="{ox}" y="{oy}" width="{w}" height="{h}" fill="#F3EADA" '
             f'stroke="#C9A96A" stroke-width="1.5"/>')
    # montantes
    for i in range(n_mont):
        x = ox + i*(w/(n_mont-1))
        s.append(f'<rect x="{x-4}" y="{oy}" width="8" height="{h}" fill="#5C564C"/>')
    # travessas
    for j in range(n_trav):
        y = oy + j*(h/(n_trav-1))
        s.append(f'<rect x="{ox}" y="{y-4}" width="{w}" height="8" fill="#8A8377"/>')
    # cotas
    s.append(f'<line x1="{ox}" y1="{oy+h+28}" x2="{ox+w}" y2="{oy+h+28}" '
             f'stroke="#9C7A3C" stroke-width="1"/>')
    s.append(f'<text x="{ox+w/2}" y="{oy+h+22}" text-anchor="middle" font-size="13" '
             f'fill="#9C7A3C">{L:.2f} m</text>')
    s.append(f'<text x="{ox-14}" y="{oy+h/2}" text-anchor="middle" font-size="13" '
             f'fill="#9C7A3C" transform="rotate(-90 {ox-14} {oy+h/2})">{H:.2f} m</text>')
    # espaçamento entre montantes
    x0 = ox; x1 = ox + w/(n_mont-1)
    s.append(f'<line x1="{x0}" y1="{oy-18}" x2="{x1}" y2="{oy-18}" stroke="#9C7A3C"/>')
    s.append(f'<text x="{(x0+x1)/2}" y="{oy-24}" text-anchor="middle" font-size="11" '
             f'fill="#9C7A3C">{L/(n_mont-1)*100:.0f}</text>')
    # legenda
    ly = oy + h + 52
    for i, (cor, txt) in enumerate((('#5C564C', f'{n_mont} montantes · metalon 50×30×1,2 · {m_mont:.1f} m'),
                                    ('#8A8377', f'{n_trav} travessas · metalon 50×30×1,2 · {m_trav:.1f} m'),
                                    ('#C9A96A', f'MDF ultra premium 18 mm · {n_chapa:.1f} chapa(s)'))):
        s.append(f'<rect x="{ox}" y="{ly+i*20}" width="14" height="10" fill="{cor}"/>')
        s.append(f'<text x="{ox+22}" y="{ly+i*20+9}" font-size="12" fill="#333">{txt}</text>')
    s.append('</svg>')
    return '\n'.join(s)

def svg_passarela():
    esc = 80; ox, oy = 70, 60
    w = Lp*esc; hh = 34
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w+180}" height="300" '
         f'font-family="DejaVu Sans, sans-serif">',
         '<rect width="100%" height="100%" fill="#fff"/>']
    # longarinas (vista lateral)
    s.append(f'<rect x="{ox}" y="{oy}" width="{w}" height="10" fill="#3A342C"/>')
    s.append(f'<rect x="{ox}" y="{oy+hh}" width="{w}" height="10" fill="#3A342C"/>')
    # travessas
    for i in range(n_trans):
        x = ox + i*(w/(n_trans-1))
        s.append(f'<rect x="{x-3}" y="{oy+8}" width="6" height="{hh-6}" fill="#8A8377"/>')
    # mãos-francesas
    for i in range(n_mao):
        x = ox + (i+0.5)*(w/n_mao)
        s.append(f'<line x1="{x}" y1="{oy+hh+10}" x2="{x-46}" y2="{oy+hh+72}" '
                 f'stroke="#3A342C" stroke-width="7"/>')
    # parede
    s.append(f'<rect x="{ox-26}" y="{oy-30}" width="18" height="200" fill="#E6DFD2"/>')
    # piso
    s.append(f'<rect x="{ox}" y="{oy-11}" width="{w}" height="11" fill="#C9A96A"/>')
    s.append(f'<text x="{ox+w/2}" y="{oy-20}" text-anchor="middle" font-size="12" '
             f'fill="#9C7A3C">compensado naval 18 mm + piso vinílico</text>')
    s.append(f'<line x1="{ox}" y1="{oy+hh+96}" x2="{ox+w}" y2="{oy+hh+96}" stroke="#9C7A3C"/>')
    s.append(f'<text x="{ox+w/2}" y="{oy+hh+90}" text-anchor="middle" font-size="13" '
             f'fill="#9C7A3C">{Lp:.2f} m · a +2,85 m do piso</text>')
    ly = oy + hh + 118
    for i, (cor, txt) in enumerate((('#3A342C', f'2 longarinas + {n_mao} mãos-francesas · metalon 60×40×2,0 · {m_long+m_mao:.1f} m'),
                                    ('#8A8377', f'{n_trans} travessas · metalon 40×40×1,5 · {m_trans:.1f} m'))):
        s.append(f'<rect x="{ox}" y="{ly+i*20}" width="14" height="10" fill="{cor}"/>')
        s.append(f'<text x="{ox+22}" y="{ly+i*20+9}" font-size="12" fill="#333">{txt}</text>')
    s.append('</svg>')
    return '\n'.join(s)

if __name__ == '__main__':
    br = lambda v: f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')
    (P/'croqui-parede.svg').write_text(svg_parede(), encoding='utf-8')
    (P/'croqui-passarela.svg').write_text(svg_passarela(), encoding='utf-8')
    print('═'*82)
    print('DECOMPOSIÇÃO FÍSICA — peça a peça')
    print('═'*82)
    for pc in PECAS:
        print(f'\n━━ {pc["nome"].upper()}   ·   {pc["dim"]}')
        if pc['obs']: print(f'   {pc["obs"]}')
        print()
        for d, q, u, v in pc['linhas']:
            print(f'   {d:<50}{q:>7.2f} {u:<6} × {br(v):>7} = {br(q*v):>9}')
        print(f'   {"":<50}{"":>7} {"":<6}   {"CUSTO":>7}   {br(pc["total"]):>9}')
    print('\n' + '─'*82)
    m2par = L*H
    print(f'  parede    R$ {br(PECAS[0]["total"]/m2par)}/m²   '
          f'(o chute agregado anterior dava R$ 270,00/m²)')
    m2pas = Lp*Bp
    print(f'  passarela R$ {br(PECAS[1]["total"]/m2pas)}/m²   '
          f'(o chute anterior dava R$ 780,00/m²)')
    print(f'  plataforma R$ {br(PECAS[2]["total"])} cada   '
          f'(o chute anterior dava R$ 950,00)')
