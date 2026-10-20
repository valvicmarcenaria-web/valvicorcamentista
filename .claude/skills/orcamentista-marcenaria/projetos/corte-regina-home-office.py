# -*- coding: utf-8 -*-
"""REGINA — home office  [20/10/2026]

Briefing por WhatsApp, com uma imagem de referência:

  mesa 2,30 comprimento · 0,80 largura · 0,75 altura
  3 gavetas pequena e uma gaveta arquivo
  móvel para acoplar o PC (computador)
  painel no fundo com previsão de tomadas elétricas
  prateleira para finalizar o painel
  painel de 230 × 105 cm e prateleira de 230 × 25 cm,
  com ESPESSURA VISUAL DE 5 cm

⭐ [Jonathan 20/10] "MDF melamínico, corrediça oculta da rede, SEM RT e
   margem de contribuição de 35%."

⛔⛔ "ESPESSURA VISUAL DE 5 cm" NÃO É PEÇA DE 5 cm. MDF não existe em 50 mm,
   e colar três chapas para chegar lá seria jogar dinheiro fora. A peça é
   uma **caixa**: face em 18 mm e **testeira de 5 cm de altura** nas bordas
   que aparecem, com sarrafo de alma por dentro. O cliente vê 5 cm; a peça
   pesa o que pesa uma de 18.
   ⭐ É o que faz esse orçamento caber: pela leitura literal seriam três
     camadas de chapa em tudo.

⛔ O QUE CABE NA CHAPA. A chapa é 2,75 × 1,85 e as três peças grandes têm
   2,30 de comprimento: mesa (2,30 × 0,80), painel (2,30 × 1,05) e
   prateleira (2,30 × 0,25). Todas cabem INTEIRAS, sem emenda. ⚠ Mas o
   painel sozinho come 2,42 m² de uma chapa de 5,09 — e o resto da chapa
   vira um L que não serve para outra peça de 2,30.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
vg  = lambda v, n=2: f'{v:.{n}f}'.replace('.', ',')

CH_M2, APROV = 2.75*1.85, 0.80
MC_ALVO = 0.35                       # ⭐ [Jonathan 20/10]
RT_ON   = False                      # ⭐ [Jonathan 20/10] "sem RT"
BASE    = M.base(parcelas=0, rt=RT_ON, vendedor=False)

# ── insumos ──────────────────────────────────────────────────────────────
# ⭐ MDF MELAMÍNICO [Jonathan 20/10] — não é linha especial. Aparente na cor
#   amadeirada da imagem; miolo e caixaria em Branco TX.
BR   = {6: 190.0, 15: 260.0, 18: 330.0}
COR  = {6: 300.0, 15: 500.0, 18: 600.0}
FITA_BR, FITA_COR = 2.0 + 2.5, 3.0 + 2.5

# ⭐ [Jonathan 20/10] "corrediça oculta da rede" → "É HETTICH MESMO".
#   A oculta importada, R$ 190 o par — a de distribuição nacional sairia a
#   R$ 120. ⭐ E a garantia sobe junto: a oculta Hettich é a linha Gold da
#   casa, 10 ANOS, contra 5 da oculta nacional e 2 da telescópica.
CORR_OC   = 190.0
GARANTIA  = '10 anos'
SUP_PRAT  = 120.0    # ★ suporte oculto da prateleira, barra chata embutida
# ⛔ A imagem da cliente mostra PUXADOR DE BARRA PRETA nas gavetas — não
#   cava. O briefing escrito não fala de puxador; vale o que a imagem mostra.
PUXADOR   = 35.0     # ★ puxador em barra, preto fosco, por unidade
VISUAL    = 5.0      # cm de espessura aparente, por pedido da cliente

# ── as peças ─────────────────────────────────────────────────────────────
# (móvel, esp, descrição, c, l, q, cor, fc)
#   cor: 'cor' aparente · 'int' Branco TX
#   fc : 2 fita nos quatro lados · 1 só na frente · 0 nenhuma
PCS, FER, TER = [], {}, {}
def mov(mv): FER.setdefault(mv, 0.0); TER.setdefault(mv, 0.0)
def a(mv, esp, d, c, l, q, cor, fc=2): PCS.append((mv, esp, d, c, l, q, cor, fc))
def fer(mv, v): FER[mv] += v
def ter(mv, v): TER[mv] += v

def tampo_visual(mv, c, l, bordas, faces=1, cor='cor'):
    """Peça de ESPESSURA VISUAL: face(s) em 18, testeira de 5 cm nas bordas
    que aparecem e sarrafo de alma. `bordas` é a lista de comprimentos das
    arestas aparentes, em cm."""
    a(mv, 18, 'Face', c, l, faces, cor, 0)
    for i, b in enumerate(bordas):
        a(mv, 18, 'Testeira · a espessura aparente', b, VISUAL, 1, cor, 1)
    a(mv, 15, 'Sarrafo de alma', c, 4, 2, 'int', 0)

# ── 1 · MESA, 230 × 80 × 75 ──────────────────────────────────────────────
mov('Mesa')
tampo_visual('Mesa', 230, 80, [230, 80, 80])      # frente e duas laterais
a('Mesa', 18, 'Lateral de apoio',            72, 78, 1, 'cor', 2)
a('Mesa', 15, 'Travessa de amarração',      226, 10, 1, 'int', 1)

# ── 2 · GAVETEIRO, 3 gavetas pequenas e 1 arquivo ────────────────────────
mov('Gaveteiro')
a('Gaveteiro', 15, 'Lateral',                72, 55, 2, 'int', 1)
a('Gaveteiro', 15, 'Base e horizontais',     37, 55, 2, 'int', 1)
a('Gaveteiro',  6, 'Fundo',                  40, 72, 1, 'int', 0)
a('Gaveteiro', 18, 'Frente de gaveta',       38, 15, 3, 'cor', 2)
a('Gaveteiro', 18, 'Frente da gaveta arquivo', 38, 27, 1, 'cor', 2)
a('Gaveteiro', 15, 'Gaveta · laterais',      50, 12, 6, 'int', 1)
a('Gaveteiro', 15, 'Gaveta · frente e fundo',30, 12, 6, 'int', 1)
a('Gaveteiro', 15, 'Gaveta arquivo · laterais', 50, 24, 2, 'int', 1)
a('Gaveteiro', 15, 'Gaveta arquivo · frente e fundo', 30, 24, 2, 'int', 1)
a('Gaveteiro',  6, 'Gaveta · fundos',        30, 50, 4, 'int', 0)
fer('Gaveteiro', 4*CORR_OC + 4*PUXADOR)   # ⭐ quatro oculta e quatro puxadores

# ── 3 · MÓVEL DO PC, acoplado sob o tampo ────────────────────────────────
mov('Móvel do PC')
a('Móvel do PC', 15, 'Lateral',              50, 45, 2, 'cor', 1)
a('Móvel do PC', 15, 'Base e tampo',         22, 45, 2, 'cor', 1)
a('Móvel do PC',  6, 'Fundo',                25, 50, 1, 'int', 0)

# ── 4 · PAINEL DO FUNDO, 230 × 105 ───────────────────────────────────────
mov('Painel')
tampo_visual('Painel', 230, 105, [230, 230, 105, 105])   # perímetro inteiro
a('Painel', 15, 'Sarrafo de alma · travessa', 226, 4, 1, 'int', 0)
# ⛔ "previsão de tomadas elétricas": os recortes são nossos, a tomada não.

# ── 5 · PRATELEIRA, 230 × 25 ─────────────────────────────────────────────
mov('Prateleira')
tampo_visual('Prateleira', 230, 25, [230, 25, 25], faces=2)
ter('Prateleira', SUP_PRAT)

# ── o cálculo ────────────────────────────────────────────────────────────
MOVEIS = list(FER)
area, area_mv, fita_mv = {}, {}, {}
for mv, esp, d, c, l, q, cor, fc in PCS:
    k = ('Branco TX' if cor == 'int' else 'Cor', esp)
    area[k] = area.get(k, 0.0) + c*l*q/1e4
    area_mv[mv] = area_mv.get(mv, 0.0) + c*l*q/1e4
    ft = FITA_BR if k[0] == 'Branco TX' else FITA_COR
    fita_mv[mv] = fita_mv.get(mv, 0.0) + 2*(c+l)*q/100*{2: .75, 1: .4, 0: 0}[fc]*ft
preco  = lambda k: BR[k[1]] if k[0] == 'Branco TX' else COR[k[1]]
chapas = {k: -(-v/(CH_M2*APROV)//1) for k, v in area.items()}
taxa   = {k: preco(k)/(CH_M2*APROV) for k in area}
custo_ch = {k: chapas[k]*preco(k) for k in chapas}
sobra  = sum(custo_ch.values()) - sum(area[k]*taxa[k] for k in area)
at = sum(area_mv.values())
ch_mv = {}
for mv, esp, d, c, l, q, cor, fc in PCS:
    ch_mv[mv] = ch_mv.get(mv, 0.0) + c*l*q/1e4*taxa[('Branco TX' if cor == 'int'
                                                     else 'Cor', esp)]
for mv in MOVEIS: ch_mv[mv] += sobra*area_mv[mv]/at
CD = {mv: ((ch_mv[mv] + fita_mv.get(mv, 0))*1.06 + FER[mv] + TER[mv])
          *(1 + M.EMBALAGEM) for mv in MOVEIS}
PV = {mv: round(CD[mv]/(BASE - MC_ALVO)/10)*10 for mv in MOVEIS}
CD_TOT, TOTAL = sum(CD.values()), sum(PV.values())

if __name__ == '__main__':
    W = 86
    print('═'*W)
    print('REGINA — HOME OFFICE  ·  briefing de WhatsApp  ·  20/10/2026')
    print(f'MDF melamínico ⭐ · MC {MC_ALVO:.0%} ⭐ · SEM RT ⭐ · base {BASE*100:.2f}%')
    print('═'*W)

    print(f'\n{"PEÇA":<44}{"medida":>12}{"esp":>5}{"q":>3}{"m²":>8}')
    print('─'*W)
    mv_atual = None
    for mv, esp, d, c, l, q, cor, fc in PCS:
        if mv != mv_atual: print(f'{mv.upper()}'); mv_atual = mv
        tag = '' if cor == 'cor' else ' · Branco TX'
        print(f'  {d+tag:<42}{f"{c:.0f} × {l:.0f}":>12}{esp:>5}{q:>3}'
              f'{c*l*q/1e4:>8.2f}')

    print(f'\n{"═"*W}')
    print('CHAPA, POR COR E ESPESSURA')
    print(f'{"═"*W}')
    for k in sorted(area, key=lambda k: (k[0], k[1])):
        print(f'  {k[0]+" · "+str(k[1])+" mm":<30}{area[k]:>8.2f} m²'
              f'{chapas[k]:>6.0f} chapa{"s" if chapas[k] > 1 else " "}'
              f'   R$ {br(custo_ch[k]):>6}')
    print('  ' + '─'*52)
    print(f'  {"TOTAL":<30}{sum(area.values()):>8.2f} m²'
          f'{sum(chapas.values()):>6.0f}          R$ {br(sum(custo_ch.values())):>6}')
    print(f'\n  ⭐ A sobra comprada e não usada é R$ {br(sobra)} — '
          f'{sobra/sum(custo_ch.values()):.0%} da chapa.')
    print('    O painel de 2,30 × 1,05 come metade de uma chapa e deixa um L')
    print('    que não serve para outra peça de 2,30.')

    print(f'\n{"═"*W}')
    print('⛔⛔ A ESPESSURA VISUAL DE 5 cm')
    print(f'{"═"*W}')
    _vis = sum(c*l*q/1e4 for mv, esp, d, c, l, q, cor, fc in PCS
               if d.startswith('Testeira'))
    _tres = sum(c*l*q/1e4 for mv, esp, d, c, l, q, cor, fc in PCS
                if d == 'Face')*2       # as duas camadas extras da leitura literal
    print(f'  MDF não existe em 50 mm. A peça é uma CAIXA: face em 18 mm e')
    print(f'  TESTEIRA de {vg(VISUAL,0)} cm nas bordas que aparecem, com sarrafo de alma')
    print(f'  por dentro. São {_vis:.2f} m² de testeira — e é isso que o cliente vê.')
    print(f'\n  ⭐ PELA LEITURA LITERAL seriam três camadas de chapa em tudo:')
    print(f'    mais {_tres:.2f} m² de MDF de cor, ou cerca de '
          f'R$ {br(-(-_tres/(CH_M2*APROV)//1)*COR[18])} só de chapa,')
    print(f'    antes de fita e de mão de obra. A caixa entrega o mesmo')
    print(f'    desenho sem esse peso — literalmente, sem esse peso.')

    print(f'\n{"═"*W}')
    print('MÓVEL A MÓVEL')
    print(f'{"═"*W}')
    print(f'{"":<22}{"chapa":>8}{"fita":>7}{"ferr.":>8}{"terc.":>8}'
          f'{"CUSTO":>9}{"PREÇO":>9}')
    for mv in MOVEIS:
        print(f'{mv:<22}{ch_mv[mv]:>8.0f}{fita_mv.get(mv,0):>7.0f}'
              f'{FER[mv]:>8.0f}{TER[mv]:>8.0f}{CD[mv]:>9.0f}{PV[mv]:>9.0f}')
    print('─'*W)
    print(f'{"CUSTO DIRETO":<22}{"":>31}{CD_TOT:>9.0f}')
    print(f'{"INVESTIMENTO":<22}{"":>31}{"":>9}{TOTAL:>9.0f}')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print('  · ⚠ A COR NÃO VEIO. A imagem é amadeirada; orçei MDF melamínico')
    print(f'    DE COR (R$ {br(COR[18])} a chapa de 18) com caixaria em Branco TX.')
    print('    Amadeirado de linha especial muda o preço — confirmar o padrão.')
    # ⭐ quanto a mesa cairia sem a testeira de 5 cm no tampo
    _t = [(c, l, q) for mv, esp, d, c, l, q, cor, fc in PCS
          if mv == 'Mesa' and d.startswith('Testeira')]
    _dcd = (sum(c*l*q/1e4*taxa[('Cor', 18)] for c, l, q in _t)
            + sum(2*(c+l)*q/100*0.4*FITA_COR for c, l, q in _t))*1.06*(1+M.EMBALAGEM)
    _dpv = round(_dcd/(BASE - MC_ALVO)/10)*10
    print('  · ⚠ A ESPESSURA DA MESA NÃO VEIO. A cliente deu 5 cm de espessura')
    print('    visual para o PAINEL e a PRATELEIRA. Adotei o mesmo no tampo da')
    print('    mesa, que é o que a imagem mostra. Com tampo liso de 18 mm a')
    print(f'    mesa cairia R$ {br(_dpv)}, de R$ {br(PV["Mesa"])} para '
          f'R$ {br(PV["Mesa"]-_dpv)}. Confirmar.')
    print('  · ⚠ "PREVISÃO DE TOMADAS ELÉTRICAS": os recortes no painel são')
    print('    nossos; a tomada, o ponto e o circuito são da elétrica. Se a')
    print('    cliente quiser CAIXA DE TOMADA EMBUTIDA na marcenaria, é item')
    print('    à parte (a base da casa traz R$ 260).')
    print('  · ⚠ COMO A MESA SE APOIA. Orçei com o gaveteiro de um lado e uma')
    print('    lateral do outro, amarrados por travessa. Se a cliente quiser')
    print('    a mesa FLUTUANDO na parede, entra estrutura metálica e muda.')
    print(f'  · ⭐ CORREDIÇA OCULTA HETTICH [Jonathan 20/10], R$ {br(CORR_OC)} o par —')
    print('    confirmado por ele. A oculta nacional sairia a R$ 120, R$ 280')
    print(f'    a menos nas quatro gavetas. ⭐ E a Hettich traz {GARANTIA} de')
    print('    garantia, contra 5 da oculta nacional e 2 da telescópica.')
    print('  · ⚠ O ÁUDIO DE 6 SEGUNDOS que veio depois do briefing não foi')
    print('    transcrito para mim, e a mensagem seguinte foi apagada. Se')
    print('    houver escopo ali, não está neste preço.')
    print(f'  · ⛔ O PUXADOR NÃO ESTÁ NO BRIEFING ESCRITO, mas a imagem da')
    print(f'    cliente mostra BARRA PRETA nas gavetas. Orçei barra a '
          f'★ R$ {br(PUXADOR)}/un.')
    print('    Em puxador cava usinado na própria frente, a ferragem some e')
    print(f'    o gaveteiro cai R$ {br(round(4*PUXADOR*(1+M.EMBALAGEM)/(BASE-MC_ALVO)/10)*10)}.')
    print('  · ⚠ A IMAGEM MOSTRA A MESA VIRANDO A QUINA, com um retorno na')
    print('    parede da direita. O briefing escrito diz 2,30 × 0,80 e é isso')
    print('    que está orçado. Se houver retorno, é outro módulo.')
    print('  · ⛔ MEDIR NO LOCAL antes de cortar: as três peças de 2,30 cabem')
    print('    inteiras na chapa, mas só se a parede confirmar os 2,30.')
