# -*- coding: utf-8 -*-
"""ICA · LIVING — levantamento peça por peça  [27/10/2026]

⭐ [Jonathan 27/10] quatro furos no levantamento anterior:
     1 · não havia quantitativo de FITA DE BORDA
     2 · não puxou o custo da CORREDIÇA da base
     3 · o quantitativo de COLUNAS estava errado
     4 · as colunas têm 3000 de altura e a chapa dá 2730 — teria EMENDA

⭐⭐ A DECISÃO DAS COLUNAS, que é a mais importante deste arquivo:
   > "são 11 colunas formado por 4 peças 2 de 70mm 2 de 200mm — mas aqui
   > temos um detalhe importante. são colunas de 3000mm de altura, a chapa
   > tem 275 (-2cm de acerto de corte), ou seja, teria emenda. Para este
   > cliente em especial, após alinhamento entre as partes, combinamos que
   > as colunas não irão passar de 273."

   ⛔ A coluna NÃO é ripa maciça: é CAIXÃO de 70 × 200 mm, montado com
     quatro peças. A leitura de 26/10 chamou isso de "32 ripas de 7 cm" e
     errou a natureza da peça, não só a conta.
   ⭐ A geometria confirma o Jonathan: a cadeia da prancha fecha em
     11 × 7 + 10 × 10 = 177, e a cadeia vertical dá 300 + 20 = 320 — os
     20 cm de profundidade SÃO a peça de 200 mm.

⛔ Toda medida em CENTÍMETROS, como a prancha. Espessura em mm.
"""

# ── a chapa, como a Base de Custos declara ──────────────────────────────
CHAPA_C, CHAPA_L = 275.0, 185.0          # cm · confirmado em plano de corte
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875 m²
APROV    = 0.80
SANGRIA  = 2.0                           # cm de acerto de corte [Jonathan]
ALT_MAX  = CHAPA_C - SANGRIA             # ⭐ 273 — o teto de peça sem emenda

PD = 300.0                               # pé-direito do Living

ALTAS = []   # ⭐ toda peça que o projeto desenhou acima do que a chapa dá

def P(nome, movel, c, l, qtd=1, esp=18, fita=(0, 0), obs=''):
    """Uma peça. `fita` = (nº de arestas no COMPRIMENTO, nº na LARGURA).
    ⭐ É isto que faltava: sem declarar aresta por aresta não há metro de
      fita, e sem metro de fita não há nem material nem filetagem.

    ⛔⛔ E AQUI MORA A SEGUNDA DESCOBERTA DO DIA. O Jonathan cravou 273 para
      as COLUNAS porque a chapa não dá 300. Mas o Living tem pé-direito de
      300 e MAIS DE UM móvel sobe até lá — a lateral da cristaleira foi
      desenhada com 280. A regra dele, aplicada com coerência, rebaixa essa
      peça também. Então toda peça acima de 273 é ANOTADA e rebaixada, e o
      relatório mostra a lista: são decisões de projeto, não de corte."""
    def cabe(a, b): return a <= CHAPA_C and b <= CHAPA_L
    if not (cabe(c, l) or cabe(l, c)):
        maior, menor = max(c, l), min(c, l)
        if menor <= CHAPA_L and maior > ALT_MAX:
            ALTAS.append((movel, nome, maior, qtd))
            c, l = (ALT_MAX, l) if c >= l else (c, ALT_MAX)
        else:
            raise AssertionError(
                f'⛔ {nome} ({c}×{l}) NÃO CABE NA CHAPA de nenhum jeito')
    return dict(nome=nome, movel=movel, c=c, l=l, qtd=qtd, esp=esp,
                fita=fita, obs=obs)

def gaveta(movel, larg, prof, alt, n=1, rotulo='Caixa de gaveta'):
    """A caixa atrás da frente. ⭐ É o que mais se esquece de contar."""
    liq = larg - 3.6
    return [P(f'{rotulo} · lateral', movel, prof, alt, 2*n, 18, (1, 0)),
            P(f'{rotulo} · frente e costas', movel, liq, alt, 2*n, 18, (1, 0)),
            P(f'{rotulo} · fundo', movel, liq, prof, n, 6, (0, 0),
              'Fundo em 6 mm por encaixe em rasgo — ⛔ sem fita')]

# ════════════════════════════════════════════════════════════════════════
#  01 · LIVING — páginas 012 a 026 · 8 detalhamentos
#  MDF Nogueira Caiena (Duratex) · puxador cava na própria madeira
# ════════════════════════════════════════════════════════════════════════
D1 = 'DET 01 Sapateira com painel'
D2 = 'DET 02 Aparador com gaveta'
D3 = 'DET 03 Prateleira'
D4 = 'DET 04 Divisória em colunas'
D5 = 'DET 05 Jardineira com banco'
D6 = 'DET 06 Divisória com cristaleira'
D7 = 'DET 07 Estante'
D8 = 'DET 08 Painel com porta mimetizada'

# ⚠ A LARGURA DA SAPATEIRA MUDOU. A leitura de 26/10 anotou 82; a página 17
#   não tem cota de 82 — as horizontais são 1 · 17 · 33 · 42 · 142. Adoto
#   142 de largura e 42 de profundidade, e deixo marcado para conferir.
SP_C, SP_P = 142.0, 42.0

LIVING = [
 # ── DET 01 · SAPATEIRA COM PAINEL — 142 × 300 × 42 ⚠ ─────────────────
 #   cadeia 178 + 105 + 17 = 300 ⭐ · frentes 2 + 34 + 34 + 34 + 2 = 105 ⭐
 P('Painel',             D1, SP_C, 178, 1, 18, (2, 2), '⚠ largura a conferir: 142 na prancha, 82 na leitura anterior'),
 P('Lateral',            D1, SP_P, 105, 2, 18, (1, 0)),
 P('Base e topo',        D1, SP_C, SP_P, 2, 18, (1, 0)),
 P('Divisória',          D1, SP_C, SP_P, 2, 18, (1, 0), 'Separa as três frentes de 34'),
 P('Frente',             D1, SP_C, 34, 3, 18, (2, 2), 'Cava na própria madeira · ⚠ báscula ou gaveta, a definir'),
 P('Base recuada · frente', D1, SP_C, 17, 1, 18, (2, 2), 'Com LED'),
 P('Base recuada · lateral', D1, SP_P, 17, 2, 18, (1, 0)),
 P('Fundo',              D1, SP_C, 105, 1, 6, (0, 0), 'Encaixe em rasgo'),

 # ── DET 02 · APARADOR COM GAVETA — 185 × 55 × 50 ─────────────────────
 #   largura 8 + 34 + 8 + 135 = 185 ⭐ · altura 5 + 45 + 5 = 55 ⭐
 #   vista superior 50 + 135 = 185 ⭐ → profundidade 50
 P('Tampo e base',       D2, 185, 50, 2, 18, (1, 0), 'Prancha desenha 5 cm: ver linha de painel grosso'),
 P('Lateral',            D2, 50, 45, 2, 18, (1, 0)),
 P('Divisória',          D2, 50, 45, 2, 18, (1, 0), 'Os dois montantes de 8 da cadeia'),
 P('Frente da gaveta',   D2, 135, 45, 1, 18, (2, 2), 'Cava na própria madeira'),
 *gaveta(D2, 135, 50, 45, 1, 'Gaveta'),
 P('Fundo',              D2, 185, 45, 1, 6, (0, 0), 'Encaixe em rasgo'),

 # ── DET 03 · PRATELEIRA — 135 × 45, com iluminação ───────────────────
 P('Prateleira',         D3, 135, 45, 1, 18, (2, 2), '⚠ vão de 135 em 18 mm flecha — ver se a prancha pede 25 mm'),

 # ══ DET 04 · DIVISÓRIA EM COLUNAS ⭐⭐ ════════════════════════════════
 #   11 colunas · caixão de 70 × 200 mm · 4 peças cada [Jonathan 27/10]
 #   ⛔ projetadas com 300 de altura; a chapa dá 273 → SEM EMENDA a 273
 P('Coluna · face',      D4, ALT_MAX, 7,  22, 18, (2, 1),
   'Frente e costas do caixão · 2 por coluna × 11'),
 P('Coluna · lateral',   D4, ALT_MAX, 20, 22, 18, (2, 1),
   'Os dois lados de 20 cm · 2 por coluna × 11'),
 # ⚠ as colunas param em 273 e o pé-direito é 300: sobram 27 cm abertos.

 # ── DET 05 · JARDINEIRA COM BANCO — 520 ──────────────────────────────
 #   conjunto 10 + 500 + 10 + 80 + 103 · vista superior fecha 52 × 10 = 520
 P('Floreira · fundo',   D5, 250, 50, 2, 18, (1, 1),
   'Floreira suspensa de 500 em dois módulos de 250 — ⭐ 500 não cabe na chapa'),
 P('Floreira · frente e costas', D5, 250, 30, 4, 18, (2, 1)),
 P('Floreira · lateral e divisória', D5, 50, 30, 3, 18, (1, 1)),
 P('Banco · tampo',      D5, 80, 50, 1, 18, (2, 2), 'Com iluminação embaixo'),
 P('Banco · lateral',    D5, 50, 40, 2, 18, (1, 1)),
 P('Banco · costas',     D5, 80, 40, 1, 18, (1, 1)),

 # ── DET 06 · DIVISÓRIA COM CRISTALEIRA — 460 × 300 × 65 ──────────────
 #   largura 100 + 260 + 100 = 460 ⭐ · vista superior 16+2+15+16+16 = 65 ⭐
 #   coluna A 5+39+5+62+5+65+5+32+5+53+5+20 = 300 ⭐
 #   coluna B 5+54+2+53+2+53+2+53+2+54+2+20 = 300 ⭐
 P('Lateral',            D6, 65, 280, 2, 18, (1, 0)),
 P('Montante',           D6, 65, 280, 2, 18, (1, 0), 'Divide 460 em 100 + 260 + 100'),
 P('Montante interno',   D6, 65, 280, 3, 18, (1, 0),
   '⭐ a vista posterior fecha 65+65+65+65+100 = 360: o vão de 260 é QUATRO '
   'módulos de 65, não um vão livre de 260'),
 P('Prateleira · bandas de 100', D6, 100, 65, 10, 18, (1, 0),
   'Cinco por banda · cadeia 39 · 62 · 65 · 32 · 53'),
 P('Prateleira · módulos de 65', D6, 65, 65, 20, 18, (1, 0),
   'Cinco por módulo · cadeia 54 · 53 · 53 · 53 · 54'),
 P('Topo',               D6, 265, 65, 1, 18, (1, 0), 'Dois trechos somando 460'),
 P('Base recuada · frente', D6, 260, 20, 1, 18, (2, 2), 'Recuo de 20 com LED'),
 P('Fundo ripado · ripa', D6, 260, 10, 21, 18, (2, 2),
   'Vista posterior: cadeia 2 + 10 repetida fecha em 255 ≈ 260 · ripa de 10 com vão de 2'),
 P('Rack · frente de gaveta', D6, 65, 55, 4, 18, (2, 2),
   '⚠ quatro gavetas pela cadeia 65+65+65+65+100 = 360 · cava na própria madeira'),
 *gaveta(D6, 65, 60, 55, 4, 'Rack · gaveta'),

 # ── DET 07 · ESTANTE — 255 × 300 × 40 ────────────────────────────────
 #   largura 5+75+5+60+5+60+5+40 = 255 ⭐ · vertical 300 + 40 = 340 ⭐
 #   altura 5+48+5+48+5+48+5+48+5+43+35+5 = 300 ⭐
 P('Lateral e montante', D7, 40, 260, 5, 18, (1, 0), 'Quatro colunas: 75 · 60 · 60 · 40'),
 P('Prateleira · coluna de 75', D7, 75, 40, 4, 18, (1, 0), 'Vãos de 48'),
 P('Prateleira · colunas de 60', D7, 60, 40, 8, 18, (1, 0), 'Quatro por coluna'),
 P('Prateleira · coluna de 40', D7, 40, 40, 4, 18, (1, 0)),
 P('Base e topo',        D7, 255, 40, 2, 18, (1, 0)),
 P('Fundo ripado · ripa', D7, 255, 10, 24, 18, (2, 2), 'Nichos com fundo ripado'),
 P('Gaveteiro · frente', D7, 75, 35, 3, 18, (2, 2), 'Três gavetas · cava na própria madeira'),
 *gaveta(D7, 75, 35, 35, 3, 'Gaveteiro · gaveta'),

 # ── DET 08 · PAINEL COM PORTA MIMETIZADA — 400 × 300 ─────────────────
 #   largura 260 + 80 + 60 = 400 ⭐ · altura 90 + 210 = 300 ⭐
 P('Painel · módulo',    D8, 130, 300, 2, 18, (2, 2), 'Trecho de 260 em dois módulos'),
 P('Painel · trecho',    D8, 140, 300, 1, 18, (2, 2), 'Trechos de 80 e 60'),
 P('Painel · vão da porta, descontado', D8, 90, 210, -2, 18, (0, 0),
   '⭐ a porta mimetizada é folha separada: o vão dela sai da área do painel'),
 P('Porta mimetizada',   D8, 90, 210, 2, 18, (2, 2), 'De giro, com cava · ⚠ duas portas, a confirmar'),
]

# ════════════════════════════════════════════════════════════════════════
#  PREÇOS — todos da Base de Custos (planilha única da casa)
# ════════════════════════════════════════════════════════════════════════
CHAPA18   = 700.0   # MDF Melamínico Fosco 18 mm · é a chapa de cor padrão
CHAPA6    = 350.0   # MDF Melamínico Fosco 6 mm · fundos
FITA_M    = 3.00    # Fita de borda cor 22 mm · + 10% de desperdício
FITA_PERD = 0.10
FILETE_M  = 2.50    # Filetagem na coladeira automática 15 e 18 mm
FITA_CHEIA= 5.50    # ⚠ a Base também traz o "preço cheio da casa" já com aplicação
CORREDICA = 80.0    # Hardt Invisível P-10 · ⭐ O PADRÃO DA CASA
DOBRADICA = 15.0    # ★ Bigfer Onix — ⛔ a linha "Padrão" da escada está VAZIA na Base
DOBR_VIDRO= 70.0    # Dobradiça para porta de vidro · A COTAR
CAVA_M    = 50.0    # Cava usinada, por metro de frente
LED_M     = 150.0   # LED COB conjunto completo: fita, perfil, usinagem e instalação
LED_PERFIL= 65.0    # ⚠ só o perfil com difusor — a Base alerta: fechar o que a linha inclui
FONTE     = 120.0   # uma a cada 8 a 10 m
ALMA      = 50.0    # barra chata 5 mm, 3 m · toda peça acima de 30 mm
SUPORTE   = 30.0    # suporte oculto de prateleira · de 40 em 40 cm

# ── ferragem, declarada item a item ─────────────────────────────────────
#  ⭐ [Jonathan 27/10] "não puxou o custo da corrediça da base" — aqui estão
#    TODAS as gavetas do Living, não só a que faltava.
GAVETAS = [(D2, 'Aparador · gaveta de 135',       1, 450),   # ⭐ A QUE FALTAVA
           (D6, 'Rack · gavetas de 65',           4, 550),
           (D7, 'Gaveteiro · gavetas de 75',      3, 400)]
PORTAS  = [(D8, 'Porta mimetizada de giro 90 × 210', 2, 5, DOBRADICA),
           (D6, 'Porta de cristaleira em vidro reflecta', 4, 3, DOBR_VIDRO)]
CAVA    = [(D1, 'Frentes da sapateira', 3, 142), (D2, 'Frente da gaveta', 1, 135),
           (D6, 'Frentes do rack',      4,  65), (D7, 'Gaveteiro',        3,  75),
           (D8, 'Portas mimetizadas',   2,  90)]
LED     = [(D1, 'Base da sapateira', 1.42), (D3, 'Prateleira',          1.35),
           (D5, 'Banco',            0.80), (D6, 'Base recuada',         2.60),
           (D6, 'Prateleiras da cristaleira · 5 × 100', 5.00)]
# ⭐ a alma de aço: uma barra por peça acima de 30 mm. O Jonathan corrigiu a
#   CONTAGEM das colunas (32 → 11), não o princípio.
ALMAS   = [(D4, 'Colunas · caixão de 70 × 200 mm', 11),
           (D2, 'Tampo e base de 5 cm',             2),
           (D2, 'Montantes de 8 cm',                2)]
SUPORTES= [(D7, 'Prateleiras da estante · 16 × 2', 32),
           (D6, 'Prateleiras da cristaleira',      10)]

def conta(pecas=LIVING):
    br = lambda v: f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')
    W = 76
    print('═'*W); print('01 · LIVING — ICA · Jéssica e Michell')
    print(f'MDF Nogueira Caiena (Duratex) · chapa {CHAPA_C:g} × {CHAPA_L:g} cm '
          f'· altura máxima {ALT_MAX:g} cm'); print('═'*W)

    # ── 1 · CHAPA, arredondada para cima por espessura ──────────────────
    area, fita_m = {}, 0.0
    por_movel = {}
    for p in pecas:
        a = p['c'] * p['l'] * p['qtd'] / 10000
        area[p['esp']] = area.get(p['esp'], 0) + a
        por_movel[p['movel']] = por_movel.get(p['movel'], 0) + a
        nc, nl = p['fita']
        fita_m += (nc * p['c'] + nl * p['l']) * p['qtd'] / 100
    print('\n⬛ CHAPA — ⛔ arredondada para cima, nunca em fração')
    print(f"  {'espessura':<12}{'área':>9}{'chapas':>9}{'R$/chapa':>11}{'custo':>12}")
    print('  ' + '─'*53)
    cust_chapa = 0.0
    for esp, a in sorted(area.items()):
        n = max(1, -(-a / (CHAPA_M2 * APROV) // 1))
        pr = CHAPA18 if esp >= 15 else CHAPA6
        c = n * pr; cust_chapa += c
        print(f'  {esp:>2} mm{"":<7}{a:>7.2f} m²{n:>9.0f}{br(pr):>11}{br(c):>12}')
    print('  ' + '─'*53)
    print(f"  {'TOTAL':<32}{'':>9}{br(cust_chapa):>20}")

    # ── 2 · FITA DE BORDA ⭐ o furo nº 1 ────────────────────────────────
    fita_c = fita_m * (1 + FITA_PERD)
    print(f'\n⬛ FITA DE BORDA — ⭐ não existia no levantamento anterior')
    print(f'  filetamento declarado aresta a aresta{fita_m:>22.1f} m')
    print(f'  + {FITA_PERD:.0%} de desperdício{br(fita_c):>37} m')
    # ⛔ o desperdício é de MATERIAL: compra-se mais rolo do que se aplica.
    #   A filetagem é serviço sobre o perímetro REAL — fileta-se o que se
    #   fileta. Somar os 10% nos dois inflava o serviço.
    f_mat, f_ser = fita_c * FITA_M, fita_m * FILETE_M
    print(f'  material · fita de cor 22 mm a R$ {FITA_M:.2f}/m{br(f_mat):>22}')
    print(f'  serviço · filetagem a R$ {FILETE_M:.2f}/m sobre o perímetro real'
          f'{br(f_ser):>13}')
    print('  ' + '─'*53)
    print(f"  {'TOTAL':<32}{br(f_mat+f_ser):>29}")
    print(f'  ⚠ a Base traz um preço cheio da casa, já com aplicação, a '
          f'R$ {FITA_CHEIA:.2f}/m → {br(fita_m*FITA_CHEIA)}')
    print('    ⛔ e isso NÃO é conferência independente: 3,00 + 2,50 = 5,50 é')
    print('      a mesma conta por outro caminho.')

    # ── 3 · FERRAGEM E LUZ ──────────────────────────────────────────────
    print('\n⬛ FERRAGEM, CAVA E ILUMINAÇÃO')
    tot = 0.0
    def L(rot, q, un, pr, obs=''):
        nonlocal tot
        v = q * pr; tot += v
        print(f'  {rot:<44}{q:>5.0f} {un:<5}{br(v):>11} {obs}')
    print('  ── corrediças ─────────────────────────────────────────────')
    for mov, rot, q, mm in GAVETAS:
        L(f'{rot} · {mm} mm', q, 'par', CORREDICA,
          '⭐' if mov == D2 else '')
    print('  ── dobradiças ─────────────────────────────────────────────')
    for mov, rot, nq, nd, pr in PORTAS:
        L(rot, nq*nd, 'un', pr, '★ linha a definir' if pr == DOBRADICA else '⛔ a cotar')
    print('  ── cava usinada, por metro de frente ──────────────────────')
    cava_m = sum(q*c/100 for _, _, q, c in CAVA)
    L('Cava na própria madeira', cava_m, 'm', CAVA_M)
    print('  ── iluminação ─────────────────────────────────────────────')
    led_m = sum(m for _, _, m in LED)
    L('LED conjunto completo', led_m, 'm', LED_M, '⚠ ver nota')
    L('Fonte de LED', max(1, -(-led_m//9)), 'un', FONTE)
    print('  ── estrutura ──────────────────────────────────────────────')
    for mov, rot, q in ALMAS: L(f'Alma de aço · {rot}', q, 'barra', ALMA)
    for mov, rot, q in SUPORTES: L(f'Suporte oculto · {rot}', q, 'un', SUPORTE)
    print('  ' + '─'*53)
    print(f"  {'TOTAL':<44}{'':>11}{br(tot):>11}")

    # ── 4 · FECHAMENTO ──────────────────────────────────────────────────
    mat = cust_chapa + f_mat + tot
    geral = cust_chapa + f_mat + f_ser + tot
    print(f'\n{"═"*W}'); print('FECHAMENTO — custo de material e ferragem do Living')
    print('═'*W)
    for rot, v in (('chapa', cust_chapa), ('fita, material', f_mat),
                   ('fita, filetagem', f_ser), ('ferragem, cava e luz', tot)):
        print(f'  {rot:<44}{br(v):>20}')
    print('  ' + '─'*66)
    print(f'  {"TOTAL DO LIVING":<44}{br(geral):>20}')
    print(f'\n  por móvel (área de chapa):')
    for m, a in sorted(por_movel.items(), key=lambda t: -t[1]):
        print(f'    {m:<38}{a:>7.2f} m²')

    # ── 5 · O QUE PRECISA DE DECISÃO ────────────────────────────────────
    print(f'\n{"═"*W}'); print('⛔ DECISÕES EM ABERTO'); print('═'*W)
    if ALTAS:
        print(f'  ⛔⛔ PEÇAS DESENHADAS ACIMA DOS {ALT_MAX:g} CM QUE A CHAPA DÁ —')
        print('     rebaixadas aqui pelo mesmo critério das colunas:')
        for mov, nome, alt, q in ALTAS:
            print(f'       {mov[:30]:<32}{nome:<20}{alt:g} cm × {q}')
    gr = sum(p['c']*p['l']*p['qtd']/10000 for p in pecas
             if p['movel'] == D2 and p['nome'] in ('Tampo e base', 'Divisória'))
    print(f'\n  ⚠ PAINEL GROSSO. O DET 02 desenha tampo e base de 5 cm e')
    print(f'    montantes de 8 cm. A conta acima está em 18 mm simples. Dobrar')
    print(f'    a chapa nessas peças acrescenta {gr:.2f} m² — cerca de '
          f'{br(-(-gr/(CHAPA_M2*APROV)//1)*CHAPA18)} em chapa.')
    print(f'\n  ⚠ AS COLUNAS PARAM EM {ALT_MAX:g} E O PÉ-DIREITO É {PD:g}:')
    print(f'    sobram {PD-ALT_MAX:g} cm abertos no topo. O topo de cada coluna')
    print(f'    passa a ser VISTO — já está com fita na conta. Falta dizer se')
    print(f'    entra travessa de arremate nesse vão.')

def colunas():
    """⭐⭐ DET 04 · a resposta à pergunta do Jonathan, aberta."""
    br = lambda v: f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')
    W = 76
    N, FACE, LADO = 11, 7.0, 20.0
    print(f'\n{"═"*W}'); print('⭐⭐ DET 04 · AS COLUNAS, ABERTAS'); print('═'*W)
    print(f'  {N} colunas · caixão de {FACE*10:g} × {LADO*10:g} mm · quatro peças cada')
    print(f'  {"":4}2 faces de {FACE:g} cm  +  2 lados de {LADO:g} cm   = 4 peças')
    print(f'  {"":4}{N} × 4 = {N*4} peças, todas de {ALT_MAX:g} cm')

    print(f'\n  ⛔ A EMENDA, E POR QUE ELA NÃO ACONTECE')
    print(f'    projeto desenha              {PD:g} cm de altura')
    print(f'    chapa                        {CHAPA_C:g} cm')
    print(f'    − acerto de corte            {SANGRIA:g} cm')
    print(f'    = peça inteira até           {ALT_MAX:g} cm   ⭐ o teto sem emenda')
    print(f'    acordado com o cliente       {ALT_MAX:g} cm   ⭐ [Jonathan 27/10]')
    print(f'    → sobra aberta no topo       {PD-ALT_MAX:g} cm')

    # ── a conferência geométrica: é corte em tiras, não nesting ────────
    larg = [LADO]*(N*2) + [FACE]*(N*2)
    tiras, atual = [], 0.0
    layout = []
    for w in sorted(larg, reverse=True):
        if atual + w > CHAPA_L: tiras.append(layout); layout, atual = [], 0.0
        layout.append(w); atual += w
    if layout: tiras.append(layout)
    area = sum(w*ALT_MAX for w in larg)/10000
    n_area = max(1, -(-area/(CHAPA_M2*APROV)//1))
    print(f'\n  ⭐ CONFERÊNCIA DA CHAPA, POR DOIS CAMINHOS')
    print(f'    pela área:      {area:.2f} m² ÷ ({CHAPA_M2:.4f} × {APROV:.0%}) '
          f'→ arredonda para {n_area:.0f} chapas')
    print(f'    pela geometria: as peças têm {ALT_MAX:g} de comprimento, então é')
    print(f'                    corte em TIRAS, e o que limita é a largura:')
    for i, t in enumerate(tiras, 1):
        uso = sum(t)
        print(f'      chapa {i}: ' + ' + '.join(f'{w:g}' for w in t)
              + f' = {uso:g} de {CHAPA_L:g} cm  ({uso/CHAPA_L:.0%})')
    print(f'                    → {len(tiras)} chapas')
    ok = '⭐ os dois caminhos batem' if len(tiras) == n_area else \
         '⛔ OS DOIS CAMINHOS DIVERGEM — vale olhar o plano de corte'
    print(f'    {ok}')
    print(f'    aproveitamento real {area/(len(tiras)*CHAPA_M2):.1%} — '
          f'contra os {APROV:.0%} de premissa')

    # ── o que a decisão dos 273 poupou ────────────────────────────────
    sobra = PD - ALT_MAX
    emenda_m2 = sum(w*sobra for w in larg)/10000
    print(f'\n  ⭐ O QUE OS {ALT_MAX:g} POUPARAM')
    print(f'    manter os {PD:g} cm exigiria emendar {N*4} peças: mais '
          f'{emenda_m2:.2f} m² de chapa,')
    print(f'    {N*4} emendas a esquadrejar e colar, e {N*4} juntas à vista num')
    print(f'    brise que se olha de perto. ⛔ Emenda em peça esbelta é onde o')
    print(f'    móvel abre com o tempo.')

    # ── fita e alma, só das colunas ───────────────────────────────────
    f_vert = N * 4 * ALT_MAX / 100          # as quatro arestas verticais
    f_topo = N * 2*(FACE+LADO) / 100        # ⭐ o topo virou peça vista
    print(f'\n  ⬛ FITA DAS COLUNAS')
    print(f'    4 arestas verticais × {ALT_MAX:g} cm × {N} colunas{f_vert:>18.1f} m')
    print(f'    topo de cada coluna — ⭐ passou a ser visto{f_topo:>17.1f} m')
    print(f'    {"":48}{"─"*8}')
    print(f'    {"":48}{f_vert+f_topo:>7.1f} m')
    print(f'\n  ⬛ ALMA DE AÇO · {N} barras, uma por coluna{br(N*ALMA):>21}')
    print(f'    ⭐ o Jonathan corrigiu a CONTAGEM (32 → {N}), não o princípio:')
    print(f'      o caixão montado tem {FACE*10:g} mm e a regra da casa manda alma')
    print(f'      em toda peça acima de 30 mm.')

if __name__ == '__main__':
    conta()
    colunas()
