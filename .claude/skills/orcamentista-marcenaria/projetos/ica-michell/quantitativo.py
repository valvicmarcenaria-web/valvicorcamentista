# -*- coding: utf-8 -*-
"""Quantitativo por ambiente do projeto ICA, declarado peça por peça.

⭐ Existe para que a conta não seja digitada à mão: a cota vem da prancha
(conferida pela cadeia que fecha, em geo.py), e daqui saem as linhas da aba
do ambiente na planilha do Google.

⛔ Toda medida está em CENTÍMETROS, como a prancha. Espessura em mm.
"""
CHAPA_M2, APROV = 5.0875, 0.80

def P(nome, movel, c, l, qtd=1, esp=18, obs=''):
    return dict(nome=nome, movel=movel, c=c, l=l, qtd=qtd, esp=esp, obs=obs)

def gaveta(movel, larg, prof, alt, n=1, rotulo='Caixa de gaveta'):
    """A caixa que vai atrás da frente: duas laterais, frente e costas em
    18 mm, fundo em 6 mm. ⭐ É o que mais se esquece de contar."""
    liq = larg - 3.6                      # desconta as duas laterais
    return [P(f'{rotulo} · lateral', movel, prof, alt, 2 * n, 18),
            P(f'{rotulo} · frente e costas', movel, liq, alt, 2 * n, 18),
            P(f'{rotulo} · fundo', movel, liq, prof, n, 6, 'Fundo em 6 mm')]

def ripado(movel, larg_total, alt, larg_ripa, vao, esp=18, obs=''):
    n = int(larg_total // (larg_ripa + vao)) + 1
    return [P(f'Ripa de {larg_ripa:g}', movel, larg_ripa, alt, n, esp,
              obs or f'Vão de {vao:g} entre as ripas · {n} ripas em {larg_total:g}')]

# ════════════════════════════════════════════════════════════════════════
# 02 · COZINHA — páginas 028 a 042 · 5 detalhamentos
# Verde Floresta (Velluto) · Jequitibá Rosa (Essencial Wood) · Branco interno
# ════════════════════════════════════════════════════════════════════════
IL = 'DET 01 Ilha'          # 245 × 90 × 130 · base 5 · laterais 5 · cava
TG = 'DET 02 Torre geladeira'   # 110 × 300 × 80 · laterais 3
S1 = 'DET 03 Superior 01'   # 405 × 103 × 67
S2 = 'DET 04 Superior 02'   # 405 × 40 × 37 · LED
BA = 'DET 05 Bancada'       # 405 × 90 × 80 · armário 60 de prof · base 5

COZINHA = [
    # ── DET 01 · ILHA ─────────────────────────────────────────────────
    P('Lateral',            IL, 130,  85, 2, 18, 'Prancha desenha 5 cm: ver linha de painel grosso'),
    P('Fundo',              IL, 235,  85, 1, 18),
    P('Base inferior',      IL, 235, 130, 1, 18, 'Apoiada na base melamínica de 3 cm'),
    P('Tampo de apoio',     IL, 235, 130, 1, 18, 'Recebe o quartzito'),
    P('Divisória interna',  IL, 130,  85, 4, 18, 'Módulos 60 · 69 · 38 · 60'),
    P('Frente',             IL, 235,  85, 1, 18, 'Três gavetões, duas gavetas, uma porta e porta tempero · cava usinada'),
    *gaveta(IL, 60, 55, 40, 3, 'Gavetão'),
    *gaveta(IL, 60, 55, 20, 2, 'Gaveta'),
    *ripado(IL, 245, 76, 3, 3, 18, 'Vista posterior · ripas de 3 com vão de 3'),
    # ── DET 02 · TORRE DA GELADEIRA ───────────────────────────────────
    P('Lateral',            TG,  80, 300, 2, 18, 'Prancha desenha 3 cm: ver linha de painel grosso'),
    P('Fundo',              TG, 104, 300, 1, 18),
    P('Base e topo',        TG, 104,  80, 2, 18),
    P('Tampo do nicho',     TG, 104,  80, 1, 18, 'A 197 do chão, sobre a geladeira'),
    P('Prateleira',         TG, 104,  80, 1, 18, 'Entre os dois nichos de 46'),
    P('Báscula',            TG, 104,  46, 2, 18, 'Cadeia 10 + 46 + 46 em 103'),
    # ── DET 03 · ARMÁRIO SUPERIOR 01 ──────────────────────────────────
    P('Base e topo',        S1, 405,  67, 2, 18, 'Fechamento superior na faixa de 10'),
    P('Lateral',            S1,  67, 103, 2, 18),
    P('Divisória',          S1,  67,  93, 5, 18, 'Cadeia 2+74+2+63+2+69+2+63+2+75+2+47+2 = 405'),
    P('Prateleira',         S1,  70,  67, 6, 18, 'Uma por vão · divide 93 em 44 + 44'),
    P('Báscula',            S1,  70,  46, 10, 18, 'Cinco módulos em duas fileiras'),
    P('Porta de giro',      S1,  47, 103, 1, 18, 'Módulo de 50'),
    # ── DET 04 · ARMÁRIO SUPERIOR 02 ──────────────────────────────────
    P('Base e topo',        S2, 405,  37, 2, 18),
    P('Lateral',            S2,  37,  40, 2, 18),
    P('Divisória',          S2,  37,  40, 5, 18, 'Mesma cadeia 77·65·71·65·77·50'),
    P('Báscula',            S2,  67,  40, 6, 18, 'Uma por módulo'),
    # ── DET 05 · BANCADA COM ARMÁRIO ──────────────────────────────────
    P('Base e tampo',       BA, 343,  60, 2, 18, 'Trechos de 215 e 128 · lava-louças de 62 no meio'),
    P('Fundo',              BA, 343,  80, 1, 18),
    P('Lateral e divisória',BA,  60,  80, 6, 18, 'Módulos 95 · 35 · 85 | 68 · 60'),
    P('Frente',             BA, 343,  80, 1, 18, 'Seis gavetões, gavetão de lixeira e porta de giro · cava'),
    *gaveta(BA, 85, 55, 40, 6, 'Gavetão'),
    *gaveta(BA, 60, 55, 40, 1, 'Gavetão lixeira'),
    P('Porta tempero',      BA,  35,  80, 1, 18, 'Módulo de 35'),
]

def resumo(pecas, titulo):
    print(f'\n{"═"*70}\n{titulo}\n{"═"*70}')
    por_esp, por_movel = {}, {}
    for p in pecas:
        a = p['c'] * p['l'] * p['qtd'] / 10000
        por_esp[p['esp']] = por_esp.get(p['esp'], 0) + a
        por_movel[p['movel']] = por_movel.get(p['movel'], 0) + a
    print(f'{len(pecas)} linhas de peça')
    for e, a in sorted(por_esp.items()):
        print(f'  {e:>2} mm: {a:7.2f} m²  →  {a/(CHAPA_M2*APROV):5.2f} chapas')
    print('  por móvel:')
    for m, a in sorted(por_movel.items(), key=lambda t: -t[1]):
        print(f'    {m:26} {a:7.2f} m²')
    tot = sum(por_esp.values())
    print(f'  TOTAL {tot:.2f} m² · {tot/(CHAPA_M2*APROV):.2f} chapas')

if __name__ == '__main__':
    resumo(COZINHA, '02 · COZINHA')
    print('\nLINHAS PARA A PLANILHA:')
    for p in COZINHA:
        print(f"{p['nome']}\t{p['movel']}\t{p['c']:g}\t{p['l']:g}\t{p['qtd']}\t{p['esp']}\t{p['obs']}")
