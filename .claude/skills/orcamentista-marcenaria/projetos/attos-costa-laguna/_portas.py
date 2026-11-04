# -*- coding: utf-8 -*-
"""⚠⚠ SIMULAÇÃO, NÃO ESTÁ NO ORÇAMENTO — porta de passagem feita na fábrica.

⭐ [Jonathan, 04/11/2026] "vamos implementar a forma correta de calcular o
  custo de portas de passagem ... antes de aplicar vc valida comigo simulando
  duas portas uma lisa de 90X260 e outra ripada em uma face de 90X260".
⛔ Este arquivo NÃO é importado por levantamento.py. É a simulação para o
  senhor validar. Só depois do "pode aplicar" é que isto entra no motor.

⭐ O QUE A PESQUISA DEU (o senhor pediu): G-DOOR é da Guararapes — MDF de
  BAIXÍSSIMA DENSIDADE, 360 kg/m³, feito para ENCHIMENTO de porta interna e
  tamburato; substitui colmeia de papelão e sarrafeado de madeira. A chapa
  crua sai 2.750 × 2.055 × 29,2 mm.
  ⛔ E A CHAPA DELE NÃO É A NOSSA: 275 × 205,5, não 275 × 185. Reaproveitar
    CHAPA_M2 daria rateio errado — por isso a constante é separada.
"""
import importlib.util, sys, pathlib, contextlib, io, math

P = pathlib.Path(__file__).resolve().parent
def _imp(n, f):
    s = importlib.util.spec_from_file_location(n, P / f)
    m = importlib.util.module_from_spec(s); sys.modules[n] = m
    with contextlib.redirect_stdout(io.StringIO()): s.loader.exec_module(m)
    return m
b = _imp('b', 'base.py')

# ── o que o Jonathan cravou ─────────────────────────────────────────────
GDOOR_CHAPA = 600.0              # ⭐ "essa chapa Gdoor nos custa 600,00"
GDOOR_C, GDOOR_L = 275.0, 205.5  # cm · ficha Guararapes, 2750 × 2055
GDOOR_ESP = 29.2                 # mm
REGUA = 15.0                     # ⭐ "reguas de 15cm em torno da extençao"
METALON_BARRA = 100.0            # ⭐ "a barra de 3mt do perfil custa 100,00"
METALON_BARRA_M = 3.0
METALON_N = 2                    # ⭐ "nas portas ripadas adicionais dois perfis"
PELE = 6                         # mm · "duas chapas de 6mm de acabamento"
PELE_CH = 'MDF cor 6'

GDOOR_M2 = GDOOR_C * GDOOR_L / 10000          # 5,65125 m²
ESP_PORTA = GDOOR_ESP + 2 * PELE              # 41,2 mm


def _ch(area_m2, preco, chapa_m2=b.CHAPA_M2):
    """O rateio da casa: área ÷ (chapa × aproveitamento) × preço da chapa."""
    return area_m2 / (chapa_m2 * b.APROV) * preco


def porta(largura, altura, ripada=False, nome=''):
    L = []                                      # (linha, conta, R$)
    a_porta = largura * altura / 10000

    # ① as duas peles de 6 mm, na cor
    for face in ('face A', 'face B'):
        L.append((f'pele de 6 mm · {face}',
                  f'{largura:g} × {altura:g} = {a_porta:.3f} m²',
                  _ch(a_porta, b.PRECO[PELE_CH])))

    # ② o miolo de G-Door, em réguas de 15 no perímetro
    v_n, v_c = 2, altura                        # as duas verticais, altura cheia
    h_n, h_c = 2, largura - 2 * REGUA           # as duas horizontais, entre elas
    a_gd = (v_n * REGUA * v_c + h_n * REGUA * h_c) / 10000
    L.append((f'miolo G-Door · {v_n} réguas de {REGUA:g} × {v_c:g} e '
              f'{h_n} de {REGUA:g} × {h_c:g}',
              f'{a_gd:.3f} m² de régua · chapa de {GDOOR_C:g} × {GDOOR_L:g} '
              f'a R$ {GDOOR_CHAPA:,.0f}',
              _ch(a_gd, GDOOR_CHAPA, GDOOR_M2)))

    # ③ fita e filetagem da aresta DA PORTA
    per = 2 * (largura + altura) / 100
    L.append(('fita de borda da porta', f'perímetro {per:.2f} m + 10% = '
              f'{per * b.FITA_PERDA:.2f} m',
              per * b.FITA_PERDA * b.FITA_COR))
    L.append(('filetagem da porta', f'{per:.2f} m à máquina',
              per * b.FILETE_MAQ))

    if ripada:
        # ④ o ripado, pelo cálculo padrão da casa
        n = math.floor((largura + 1) / 3)       # ripa 2, vão 1, passo 3
        larg_eq = 2 * n * b.RIPA_PERDA          # a perda de serra na largura
        a_rip = larg_eq * altura / 10000
        L.append((f'{n} ripas de 2 × {altura:g}',
                  f'⭐ área equivalente {larg_eq:.0f} × {altura:g} = '
                  f'{a_rip:.3f} m² em MDF 18',
                  _ch(a_rip, b.PRECO['MDF cor 18'])))
        f_rip = n * altura / 100 * 2            # as duas arestas à vista
        L.append(('fita das ripas', f'{n} × 2 × {altura:g} cm = {f_rip:.0f} m '
                  f'+ 10% = {f_rip * b.FITA_PERDA:.1f} m',
                  f_rip * b.FITA_PERDA * b.FITA_COR))
        L.append(('filetagem MANUAL das ripas',
                  f'{f_rip:.0f} m a R$ {b.FILETE_MAO:,.2f} · ⛔ ripa de 2 cm '
                  'não entra na coladeira', f_rip * b.FILETE_MAO))
        L.append(('laminação do ripado',
                  f'{a_porta:.3f} m² a R$ {b.RIPADO_M2:,.0f}',
                  a_porta * b.RIPADO_M2))
        # ⑤ os dois metalons contra empeno
        nb = math.ceil(altura / 100 / METALON_BARRA_M) * METALON_N
        L.append((f'{METALON_N} perfis de metalon',
                  f'{METALON_N} × {altura:g} cm → {nb} barra(s) de '
                  f'{METALON_BARRA_M:g} m a R$ {METALON_BARRA:,.0f}',
                  nb * METALON_BARRA))

    sub = sum(x[2] for x in L)
    print(f'\n{"═" * 78}\n  {nome}   ·   {largura:g} × {altura:g} · '
          f'espessura {ESP_PORTA:.1f} mm\n{"═" * 78}')
    for lin, conta, v in L:
        print(f'  {lin:<44} R$ {v:>9,.2f}')
        print(f'      {conta}')
    print(f'  {"─" * 44} {"─" * 13}')
    print(f'  {"MATERIAL E MÃO DE OBRA DA FOLHA":<44} R$ {sub:>9,.2f}')
    print(f'  {"+ cava usinada · 1 m a R$ " + f"{b.CAVA_M:,.0f}":<44} '
          f'R$ {b.CAVA_M:>9,.2f}')
    print(f'  {"+ sistema PIVÔ":<44} R$ {b.SISTEMA_PIVO:>9,.2f}')
    print(f'  {"  ou sistema DESLIZANTE":<44} R$ {b.SISTEMA_CORRER:>9,.2f}')
    print(f'  {"─" * 44} {"─" * 13}')
    print(f'  {"A FOLHA COM CAVA E PIVÔ":<44} '
          f'R$ {sub + b.CAVA_M + b.SISTEMA_PIVO:>9,.2f}')
    print(f'  {"A FOLHA COM CAVA E DESLIZANTE":<44} '
          f'R$ {sub + b.CAVA_M + b.SISTEMA_CORRER:>9,.2f}')
    print(f'  ⛔ e isto é CUSTO DIRETO de folha: ainda não leva consumíveis '
          f'(6%),\n     embalagem (2%), corte nem frete.')
    return sub


if __name__ == '__main__':
    a = porta(90, 260, ripada=False, nome='PORTA LISA')
    z = porta(90, 260, ripada=True,  nome='PORTA RIPADA EM UMA FACE')
    print(f'\n{"═" * 78}\n  A DIFERENÇA\n{"═" * 78}')
    print(f'  ripada − lisa  R$ {z - a:,.2f}   ·   {z / a - 1:.0%} mais caro')
    print(f'  ⭐ e ela é quase toda FITA E FILETAGEM DE RIPA, não chapa.')
    print(f'\n{"═" * 78}\n  PROVA DE SANIDADE DO G-DOOR · o rateio contra o '
          f'corte real\n{"═" * 78}')
    nr = math.floor(GDOOR_L / REGUA)
    print(f'  da chapa saem {nr} réguas de {REGUA:g} × {GDOOR_C:g} '
          f'({GDOOR_L:g} ÷ {REGUA:g})')
    v = math.ceil(260 / GDOOR_C)
    print(f'  cada porta de 90 × 260 pede 2 réguas de 260 (1 chapa-régua cada,')
    print(f'    sobra 15 cm) e 2 de 60 (4 por régua, logo 1 régua serve 2)')
    print(f'  → 2,5 réguas por porta · {nr} ÷ 2,5 = {nr / 2.5:.1f} portas por '
          f'chapa')
    print(f'  corte real:   R$ {GDOOR_CHAPA / (nr / 2.5):>8,.2f} por porta')
    print(f'  rateio 80%:   R$ {_ch(((2 * REGUA * 260) + (2 * REGUA * 60)) / 10000, GDOOR_CHAPA, GDOOR_M2):>8,.2f} por porta')
    print(f'  ⚠ O rateio de 80% cobra MAIS que o corte real, porque tira em')
    print(f'    régua é o corte mais eficiente que existe. É conservador —')
    print(f'    mas é uma escolha, e é sua.')
