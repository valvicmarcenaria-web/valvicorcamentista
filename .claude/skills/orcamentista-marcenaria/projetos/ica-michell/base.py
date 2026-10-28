# -*- coding: utf-8 -*-
"""O comum de todo ambiente do ICA: a chapa, a peça, a gaveta e os preços.

⭐ Nasceu do living.py quando a Cozinha chegou. São 20 ambientes — o que é
  regra da casa mora aqui; o que é prancha mora no arquivo do ambiente.

⛔ Toda medida em CENTÍMETROS, como a prancha. Espessura em mm.
"""
CHAPA_C, CHAPA_L = 275.0, 185.0          # cm · confirmado em plano de corte
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875 m²
APROV    = 0.80
SANGRIA  = 2.0                           # cm de acerto de corte [Jonathan]
ALT_MAX  = CHAPA_C - SANGRIA             # ⭐ 273 — o teto de peça sem emenda

# ── preços, todos da Base de Custos ─────────────────────────────────────
PRECO = {'MDF cor 18': 700.0, 'MDF cor 15': 550.0, 'MDF cor 6': 350.0,
         'MDF branco 18': 400.0, 'MDF branco 15': 350.0, 'MDF branco 6': 250.0}
FITA_CHEIA = 5.50   # fita de cor com filetagem · preço cheio da casa
FITA_PERD  = 0.10
CORREDICA  = 300.0  # Corrediça Blum, por gaveta
DOBRADICA  =  50.0  # Dobradiça Blum
DOBR_VIDRO =  70.0  # porta de vidro · A COTAR
BASCULA    = 250.0  # Blum AVENTOS HK-XS · ⭐ a báscula da casa
PULSADOR   = 100.0  # Blum Tip-on ou Servo · abertura por toque
CAVA_M     =  50.0  # cava usinada, por metro de frente
PUXADOR    = 172.71 # Alças Traso 416 mm, Zen Design · ⭐ o puxador do ICA
LED_M      = 150.0  # LED COB: fita, perfil, usinagem e instalação
ALMA       =  50.0  # barra chata 5 mm, 3 m · toda peça acima de 30 mm
SUPORTE    =  30.0  # suporte oculto de prateleira · de 40 em 40 cm
VIDRO_M2   =   0.0  # ⛔ reflecta champagne SEM PREÇO — a cotar
CONSUM, EMBAL = 0.06, 0.02
# ⛔⛔ SEM FONTE DE LED em lugar nenhum: as fitas da casa são 110 V
#   [Jonathan, 28/10/2026]

ALTAS = []   # ⭐ toda peça que o projeto desenhou acima do que a chapa dá

def P(nome, movel, c, l, qtd=1, chave='MDF cor 18', fita=(0, 0), obs=''):
    """Uma peça. `fita` = (nº de arestas no COMPRIMENTO, nº na LARGURA).

    ⭐ A CHAVE É POR COR, não só por espessura. Um ambiente com três padrões
      de MDF faz TRÊS arredondamentos de chapa, não um — cada cor é uma
      compra separada e puxa no mínimo uma chapa. Foi o erro que queimou a
      primeira versão desta planilha.

    ⛔ Peça acima de 273 é ANOTADA e rebaixada: é decisão de projeto, não de
      corte, e tem de aparecer na lista.
    """
    def cabe(a, b): return a <= CHAPA_C and b <= CHAPA_L
    if not (cabe(c, l) or cabe(l, c)):
        maior, menor = max(c, l), min(c, l)
        if menor <= CHAPA_L and maior > ALT_MAX:
            ALTAS.append((movel, nome, maior, qtd))
            c, l = (ALT_MAX, l) if c >= l else (c, ALT_MAX)
        else:
            raise AssertionError(f'⛔ {nome} ({c}×{l}) NÃO CABE NA CHAPA')
    return dict(nome=nome, movel=movel, c=c, l=l, qtd=qtd, chave=chave,
                fita=fita, obs=obs)

def gaveta(movel, larg, prof, alt, n=1, rotulo='Caixa de gaveta',
           cor='MDF branco 18', fundo='MDF branco 6'):
    """A caixa atrás da frente. ⭐ É o que mais se esquece de contar."""
    liq = larg - 3.6
    return [P(f'{rotulo} · lateral', movel, prof, alt, 2*n, cor, (1, 0)),
            P(f'{rotulo} · frente e costas', movel, liq, alt, 2*n, cor, (1, 0)),
            P(f'{rotulo} · fundo', movel, liq, prof, n, fundo, (0, 0),
              'Fundo em 6 mm por encaixe em rasgo — ⛔ sem fita')]

def ripado(movel, larg_total, alt, larg_ripa, vao, chave, obs=''):
    """Ripa solta com vão. ⭐ Conta a ripa, não o painel."""
    n = int(larg_total // (larg_ripa + vao)) + 1
    return [P(f'Ripa de {larg_ripa:g}', movel, larg_ripa, alt, n, chave, (2, 1),
              obs or f'Vão de {vao:g} entre as ripas · {n} ripas em {larg_total:g}')]

def fita_m(pecas, movel=None):
    return sum((nc*p['c'] + nl*p['l'])*p['qtd']/100 for p in pecas
               if movel is None or p['movel'] == movel
               for nc, nl in [p['fita']])
