# -*- coding: utf-8 -*-
"""LUCIANA (pasta Drive 1iC5AVoqoM...) — LEVANTAMENTO 1ª RODADA.

Cliente: **Luciana** [Jonathan 18/08].

DECISÕES DO JONATHAN, 18/08:
  1 · chapa = MDF melamínico COR PADRÃO da tabela da casa (500/600/300)
  2 · cliente é a Luciana
  3 · escopo de ambientes fica EM ABERTO, define depois
  4 · pedras NÃO fazem parte do nosso escopo
  5 · básculas da cozinha em MDF — e SINALIZAR isso na proposta
      palhinha a R$ 550,00/m · escrivaninha com regulagem de altura é
      PROCESSO DE MARCENARIA, não mecanismo comprado
  MCs: telescópica 30% · Hardt 35% · Hettich 38%

Lidas 34 das ~80 pranchas, pelo conector do Drive (estas TÊM camada de texto —
ver `referencias/quantitativo.md`, "Prancha em PDF: três casos"). O texto vem
sem coordenadas, então a leitura dá **o móvel, o material e as larguras**, mas
não permite montar o corte peça a peça como no Eliuton.

⛔ POR ISSO ESTE ORÇAMENTO É DE PRIMEIRA RODADA, POR MÓDULO — não é plano de
   corte. Ordem de grandeza para decidir se o job avança, não número de
   contrato.

⛔ E O MAIOR BURACO: **"MDF A DEFINIR" em TODAS as pranchas.** O projeto nomeia
   quatro famílias de cor — rosa, cinza escuro, madeirado e neutra — e nenhuma
   linha, nenhum fabricante, nenhum código. Sem isso a chapa é chute: melamínico
   comum (R$ 600/chapa 18) e especial (R$ 1.200) separam o orçamento em dois.
"""
from collections import defaultdict
import math

CH_AREA = 2.75 * 1.85

A_, LIQF_, B_ = 0.162, 0.88, 0.043
BASE = 1 - A_ - LIQF_*B_
MC_RIPADO = 0.40
def div(mc, rt=False): return BASE - mc - (LIQF_*0.10 if rt else 0.0)
def preco(resto, rip, mc, rt=False):
    return resto/div(mc, rt) + rip/div(MC_RIPADO, rt)

# ── premissas de preço ─────────────────────────────────────────────────────
# ⚠ Chapa "cor" da casa. Se a linha escolhida for especial, multiplicar por 2.
PRC = {15: 500.0, 18: 600.0, 6: 300.0}
APROV = 0.78                 # aproveitamento médio de nesting da casa
FITA_M, FILET_M = 3.00, 2.50
CAVA_M = 25.0
SUP_PRAT = 1.50
LED_M = 28.0 + 38.0
ESPELHO_FL = 285.0           # por FOLHA, com perfil
VIDRO_REFL_FL = 450.0        # reflecta bronze c/ perfil champanhe
VIDRO_REFLET_FL = 410.0      # refletente/prata c/ perfil
RO65, TRILHO = 60.0, 60.0
RODIZIO = 25.0               # jogo por gaveta com rodízio embutido
VARAO = 45.0
PALHINHA_M  = 550.0          # R$/m linear de rolo [Jonathan 18/08]
ESTOFADOR   = 1800.0         # ⚠ a base tem POR PEÇA (cabeceira 650 ·
                             #   completo 1800), não por metro. A cabeceira
                             #   tem 3,08 m — adotei a linha 'completo'.

# ── três cenários [Jonathan 18/08] — MCs 30 / 35 / 38 ─────────────────────
CENARIOS = [
    ('I · Telescópica', 0.30, dict(dobr=6.0,  corr=40.0,  art=20.0),  '2 anos'),
    ('II · Hardt',      0.35, dict(dobr=8.0,  corr=70.0,  art=250.0), '5 anos'),
    ('III · Hettich',   0.38, dict(dobr=10.0, corr=120.0, art=250.0), '10 anos'),
]

# ── módulos: (ambiente, móvel, L, H, P, portas, gavetas, básculas, ripado?) ──
# L,H,P em cm. Onde a cota não estava legível na prancha, o valor vai marcado
# em PREM (premissa) e entra na lista de dúvidas.
M = []
def mod(amb, nome, L, H, P, portas=0, gav=0, basc=0, rip=0.0, af=None, obs=''):
    # af = área de chapa cravada, para prateleira solta (onde L×H não é frontal)
    M.append(dict(amb=amb, nome=nome, L=L, H=H, P=P, portas=portas, gav=gav,
                  basc=basc, rip=rip, af=af, obs=obs))

# ═══ A · COZINHA — parede de 428,5 ═════════════════════════════════════════
mod('Cozinha', 'Armários inferiores 428,5 × 41 prof — portas, gavetas e nichos '
    'de lava-louças, cervejeira e adega', 428.5, 88, 41, portas=7, gav=4)
mod('Cozinha', 'Armário suspenso 264 × 35 prof + básculas com LED e escorredor '
    'em inox', 264, 70, 35, basc=2, portas=3)
mod('Cozinha', 'Torre de fornos 98 × 70 prof, altura 211, com nicho de '
    'micro-ondas', 98, 211, 70, portas=4)
mod('Cozinha', 'Armário do nicho da geladeira, prof 70', 108, 211, 70, portas=2)
mod('Cozinha', 'Armário inferior com ripado vazado para ventilação da '
    'churrasqueira', 108, 88, 41, rip=108*88/10000)

# ═══ B · SALA / HOME THEATER — painel de 677 ═══════════════════════════════
mod('Sala · home theater', 'Painel de parede 677 × 273 com porta de correr de '
    'acesso ao corredor, puxador usinado no próprio material', 677, 273, 4)
mod('Sala · home theater', 'Cristaleira com portas de giro em vidro reflecta '
    'bronze e prateleiras com LED', 99.5, 218.5, 40, portas=2)
mod('Sala · home theater', 'Rack 183 × 62 × 45 prof, três gavetas, MDF madeirado',
    183, 62, 45, gav=3)
mod('Sala · home theater', 'Móvel inferior com portas de giro, puxador cava',
    245, 43.5, 45, portas=5)
mod('Sala · home theater', 'Nicho com fundo ripado e LED na parte superior',
    140, 69, 20, rip=140*69/10000)

# ═══ C · ESPAÇO KIDS — painel de 372,5 ════════════════════════════════════
mod('Espaço kids', 'Estrutura do rack 372,5 × 249, prof 45, com painel de fundo '
    'prof 4 e nicho central para suporte de TV', 372.5, 249, 45)
mod('Espaço kids', 'Painel sobreposto RIPADO prof 2 sobre a estrutura',
    350, 249, 2, rip=350*249/10000)
mod('Espaço kids', 'Prateleiras prof 20 — três de 1,29 m', 129, 3, 20,
    af=3*1.29*0.20)
mod('Espaço kids', 'Gavetões com rodízio embutido — quatro, 50 × 45',
    50, 46, 45, gav=4)

# ═══ D · QUARTO INFANTIL ══════════════════════════════════════════════════
mod('Quarto infantil', 'Cabeceira RIPADA 264 × 118 em MDF rosa, com rebaixo '
    'para persiana', 264, 118, 8, rip=264*118/10000)
mod('Quarto infantil', 'Guarda-roupa 200 × 200 × 70 prof — maleiro, varão, '
    'prateleiras, gavetas e quatro portas', 200, 200, 70, portas=4, gav=8)
mod('Quarto infantil', 'Gavetas com centro em palhinha e rodízio — quatro',
    50, 46, 45, gav=4)
mod('Quarto infantil', 'Nichos porta-livros com frente em palhinha — três',
    60, 15, 20)
mod('Quarto infantil', 'Cômoda 150 × 50, MDF rosa, dois nichos com LED',
    150, 50, 50, gav=3)
mod('Quarto infantil', 'Móvel de estudo 215 × 80 × 55 prof — portas com centro '
    'em palhinha, básculas e nichos com LED', 215, 80, 55, portas=2, basc=2)
mod('Quarto infantil', 'Trocador com porta e gavetas — 70 × 95 × 55 prof',
    70, 95, 55, portas=1, gav=3)
mod('Quarto infantil', 'Escrivaninha com REGULAGEM DE ALTURA (processo de '
    'marcenaria) + móvel suspenso', 160, 75, 55, portas=2)
mod('Quarto infantil', 'Cabeceira RIPADA iluminada 239 × 118 em MDF rosa, com '
    'perfil de LED na parte superior', 239, 118, 8, rip=239*118/10000)

# ═══ E · SUÍTE CASAL (cama king) ══════════════════════════════════════════
mod('Suíte casal', 'Armário 208 × 221 com duas portas de correr em estrutura '
    'com vidro refletente — maleiro, varão, nichos, sapateiras e gavetas',
    208, 221, 66, gav=4)
mod('Suíte casal', 'Quadro da cabeceira estofada 308 × 120 (marcenaria; o '
    'revestimento é do estofador)', 308, 120, 5)
mod('Suíte casal', 'Nichos em MDF madeirado prof 20, com LED', 249, 45, 20)
mod('Suíte casal', 'Prateleiras superiores prof 18 — duas de 2,21 m',
    221, 3, 18, af=2*2.21*0.18)
mod('Suíte casal', 'Painel de nichos e prateleiras 307 × 204 — estrutura '
    'madeirada, prateleiras prof 15 com LED', 307, 204, 35, portas=6)

# ═══ F · SUÍTE 02 (cama queen) ════════════════════════════════════════════
mod('Suíte 02', 'Painel de cabeceira 271 × 45 em MDF, com recuo para descida '
    'de cortina', 271, 45, 6)
mod('Suíte 02', 'Criado-mudo / gaveteiro 45 × 45, três gavetas, cava central',
    45, 45, 45, gav=3)
mod('Suíte 02', 'Prateleira superior prof 20 — 2,71 m', 271, 3, 20,
    af=2.71*0.20)

# ═══ G · HOME OFFICE — parede de 346 ══════════════════════════════════════
mod('Home office', 'Bancada e rodobanca em MDF madeirado 346, com LED na parte '
    'superior da rodobanca', 346, 40, 70)
mod('Home office', 'Armário inferior 346 × 70 prof 45 — quatro portas e quatro '
    'gavetas, cava no mesmo material', 346, 70, 45, portas=4, gav=4)
mod('Home office', 'Armário 01 — 200 × 200 × 45, estrutura madeirada, frentes '
    'cinza escuro, portas e quatro gavetas', 200, 200, 45, portas=6, gav=4)
mod('Home office', 'Armário 02 — 200 × 200 × 45, prateleiras prof 41 e quatro '
    'gavetas', 200, 200, 45, portas=4, gav=4)
mod('Home office', 'Prateleiras prof 20 — 19 peças em quatro modelos',
    52, 3, 20, af=19*0.52*0.20)
mod('Home office', 'Gaveteiro inferior móvel com rodízio — quatro gavetas',
    45, 50, 45, gav=4)

# ═══ H · BANHO DA SUÍTE ═══════════════════════════════════════════════════
mod('Banho da suíte', 'Armário suspenso 196 × 35 com quatro portas de abrir em '
    'ESPELHO PRATA e LED na parte inferior', 196, 35, 35, portas=4)
mod('Banho da suíte', 'Armário inferior 215 — quatro gavetas, dois gavetões e '
    'duas básculas de roupa suja', 215, 85, 45, gav=6, basc=2)

# ═══ I · ÁREA DE SERVIÇO ══════════════════════════════════════════════════
mod('Área de serviço', 'Armário superior 158 + 84 + 84, portas e prateleiras',
    326, 73, 35, portas=5)
mod('Área de serviço', 'Armário inferior — três gavetões, três cestos de roupa '
    'suja e portas', 326, 85, 60, portas=4, gav=6)

# ═══ J · DESPENSA / ARMÁRIO DE SERVIÇO ════════════════════════════════════
mod('Despensa', 'Armários 293,5 × 173 — prateleiras, área livre para escada e '
    'vassouras e para objetos altos', 293.5, 173, 40, portas=6)

# ═══════════════════════════════════════════════════════════════════════════
# ÁREA DE CHAPA POR MÓDULO — método de 1ª rodada
# ═══════════════════════════════════════════════════════════════════════════
# Sem plano de corte, uso o fator empírico da casa: a área de chapa de um móvel
# fechado é ~2,6× a área frontal quando raso (P ≤ 25) e ~3,6× quando fundo.
# Aferido nos oito conjuntos do Eliuton, que TÊM corte peça a peça:
#   frontal 41,7 m² → chapa 160,8 m²  ⇒  3,86× na média ponderada.
# Uso 3,6 para móvel fundo e 2,6 para raso, e 1,9 para painel/prateleira solta.
def area_chapa(m):
    if m['af'] is not None: return m['af']
    front = m['L']*m['H']/10000
    # ⚠ AJUSTE 18/08 — eu estava usando 1,9× para painel liso, o que inflava
    #   25 m² num projeto cheio de painel de parede. Painel liso é a FACE mais
    #   os reforços: ~1,25×. O 1,9 vale para nicho, que tem fundo, laterais e
    #   prateleiras. Sintoma que denunciou: R$/m² de chapa abaixo da faixa da
    #   casa nos três cenários.
    if m['P'] <= 8:    f = 1.25        # painel de parede, cabeceira lisa
    elif m['P'] <= 25: f = 1.9         # nicho e prateleira funda
    elif m['P'] <= 40: f = 2.6         # armário raso, aéreo
    else: f = 3.6                      # móvel de caixaria funda
    return front*f

for m in M:
    m['area'] = area_chapa(m)
    m['front'] = m['L']*m['H']/10000

area_tot = sum(m['area'] for m in M)
area_rip = sum(m['rip'] for m in M)

# fita: perímetro das frentes + bordas de caixaria ≈ 3,6 m por m² de chapa
# (Eliuton: 580 m / 160,8 m² = 3,61)
fita_m = area_tot*3.61
cava_m = sum(m['L']/100*(m['portas']+m['gav']+m['basc'])*0.5 for m in M)

n_dobr = sum(m['portas']*2 + m['basc']*2 for m in M)
n_gav  = sum(m['gav'] for m in M)
n_basc = sum(m['basc'] for m in M)

chapas = math.ceil(area_tot/(CH_AREA*APROV))
custo_chapa = chapas*((PRC[15]+PRC[18])/2)          # mistura 15/18
custo_fita  = fita_m*1.10*FITA_M
custo_filet = fita_m*FILET_M
custo_cava  = cava_m*CAVA_M

# terceirizados e especiais identificados nas pranchas
TERC = [
 ('Banho da suíte', 'Espelho prata — 4 folhas de porta de abrir', 4*ESPELHO_FL, False),
 ('Suíte casal',    'Vidro refletente — 2 folhas de correr + sistema', 2*VIDRO_REFLET_FL + 2*RO65 + TRILHO, False),
 ('Sala · home theater', 'Vidro reflecta bronze — 2 folhas da cristaleira', 2*VIDRO_REFL_FL, False),
 ('Sala · home theater', 'Sistema de correr do painel de acesso ao corredor', 400.0, False),
 ('Quarto infantil', 'PALHINHA natural — 6,7 m de rolo (4 gavetas de 50, 3 porta-livros de 60, 2 portas do móvel de estudo) +15% de perda', 6.7*PALHINHA_M, False),
 ('Suíte casal',    'Estofador — cabeceira 308 × 120 ⚠ base tem por PEÇA, não por metro', ESTOFADOR, True),
 ('Quarto infantil', 'Varão cromado + rodízios embutidos', VARAO + 8*RODIZIO, False),
 ('Espaço kids',    'Rodízios embutidos — 4 gavetões', 4*RODIZIO, False),
 ('Home office',    'Rodízios do gaveteiro móvel', 4*RODIZIO, False),
 ('Vários',         'LED em perfil de alumínio — 21 m mapeados nas pranchas', 21*LED_M, False),
]
custo_terc = sum(v for _, _, v, _ in TERC)
terc_amb = defaultdict(float)
for a, d, v, e in TERC: terc_amb[a] += v

n_prat = 40
custo_sup = n_prat*4*SUP_PRAT
consum = (custo_chapa + custo_fita)*0.06
LOG = 4*600 + 3*250            # carretos + visitas · SEM montagem

BASE_CD = (custo_chapa + custo_fita + custo_filet + custo_cava + custo_sup
           + custo_terc + consum + LOG)
frac_rip = area_rip/area_tot
# o ripado leva a fatia proporcional de chapa/fita/filetagem/consumível/logística
cd_rip = (custo_chapa + custo_fita + custo_filet + consum + LOG)*frac_rip

W = 92
def brl(v): return f'{v:,.0f}'.replace(',', '.')

print('═'*W)
print('LUCIANA — LEVANTAMENTO DE 1ª RODADA   (pasta Drive 1iC5AVoqoM…)')
print('═'*W)
print('34 de ~80 folhas lidas · chapa: MDF melamínico COR PADRÃO da tabela')
print('⚠ ESTIMATIVA POR MÓDULO, não plano de corte — ver o cabeçalho do arquivo')

amb_area, amb_front = defaultdict(float), defaultdict(float)
for m in M:
    amb_area[m['amb']] += m['area']; amb_front[m['amb']] += m['front']

print(f'\nMÓVEIS LIDOS — {len(M)} itens em {len(amb_area)} ambientes\n')
atual = None
for m in M:
    if m['amb'] != atual:
        atual = m['amb']; print(f'  ── {atual.upper()}')
    fer = []
    if m['portas']: fer.append(f"{m['portas']} portas")
    if m['gav']:    fer.append(f"{m['gav']} gav")
    if m['basc']:   fer.append(f"{m['basc']} básc")
    rip = ' · RIPADO' if m['rip'] else ''
    print(f"     {m['nome'][:78]}")
    print(f"       {m['L']:.0f} × {m['H']:.0f} × {m['P']:.0f} prof"
          f"   ·  {m['area']:.2f} m² de chapa"
          f"{'  ·  ' + ' · '.join(fer) if fer else ''}{rip}")

print(f'\n{"─"*W}\nCOMPOSIÇÃO DO CUSTO DIRETO  (igual nos três, fora a ferragem)')
for rot, v in (('Chapas — %d, aproveitamento %d%%' % (chapas, APROV*100), custo_chapa),
               ('Fita (%.0f m) + filetagem' % fita_m, custo_fita+custo_filet),
               ('Usinagem de cava (%.1f m)' % cava_m, custo_cava),
               ('Suportes de prateleira', custo_sup),
               ('Terceirizados e especiais', custo_terc),
               ('Consumíveis (6%)', consum),
               ('Logística — 4 carretos + 3 visitas (montagem NÃO entra)', LOG)):
    print(f'    {rot:<66}R$ {brl(v):>9}')

# ── os três cenários ──────────────────────────────────────────────────────
print(f'\n{"═"*W}\nOS TRÊS CENÁRIOS   [MCs cravadas pelo Jonathan em 18/08]')
print('═'*W)
print(f'  {"":<18}{"ferragem":>10}{"custo direto":>14}{"INVESTIMENTO":>15}'
      f'{"MC":>6}{"garantia":>11}')
RES = []
for nome, mc, f, gar in CENARIOS:
    cf = n_dobr*f['dobr'] + n_gav*f['corr'] + n_basc*f['art']
    cd = BASE_CD + cf
    inv = round(preco(cd - cd_rip, cd_rip, mc)/500)*500
    RES.append((nome, mc, f, gar, cf, cd, inv))
    print(f'  {nome:<18}{brl(cf):>10}{brl(cd):>14}{brl(inv):>15}'
          f'{mc*100:>5.0f}%{gar:>11}')

# ── rateio por ambiente, nos três ─────────────────────────────────────────
print(f'\n{"─"*W}\nINVESTIMENTO POR AMBIENTE')
rateavel = custo_chapa + custo_fita + custo_filet + custo_cava + custo_sup + consum + LOG
print(f'  {"ambiente":<26}{"chapa":>8}{"I · 30%":>12}{"II · 35%":>12}{"III · 38%":>12}')
somas = [0, 0, 0]
for a in amb_area:
    fr = amb_area[a]/area_tot
    linha = []
    for k, (nome, mc, f, gar, cf, cd, inv) in enumerate(RES):
        d = sum(m['portas']*2 + m['basc']*2 for m in M if m['amb'] == a)
        g = sum(m['gav'] for m in M if m['amb'] == a)
        b = sum(m['basc'] for m in M if m['amb'] == a)
        exato = d*f['dobr'] + g*f['corr'] + b*f['art'] + terc_amb[a]
        cda = exato + rateavel*fr
        ra = sum(m['rip'] for m in M if m['amb'] == a)
        cda_r = rateavel*fr*(ra/amb_area[a] if amb_area[a] else 0)
        v = round(preco(cda - cda_r, cda_r, mc)/500)*500
        somas[k] += v; linha.append(v)
    print(f'  {a:<26}{amb_area[a]:>8.2f}' + ''.join(f'{brl(x):>12}' for x in linha))
# o rateio de "Vários" (LED) fica fora dos ambientes — soma no fim
falta = [RES[k][6] - somas[k] for k in range(3)]
print(f'  {"LED e itens compartilhados":<26}{"":>8}' + ''.join(f'{brl(x):>12}' for x in falta))
print(f'  {"TOTAL":<26}{area_tot:>8.2f}' + ''.join(f'{brl(RES[k][6]):>12}' for k in range(3)))

print(f'\n  R$/m² de chapa: ' + ' · '.join(f'{RES[k][6]/area_tot:.0f}' for k in range(3))
      + '   (faixa da casa 626–834)')
print('  ⚠ Fica ABAIXO da faixa nos dois primeiros cenários. Duas causas conhecidas,')
print('    nenhuma delas erro: (1) as MCs deste job são 30/35/38, contra 32/37/42 do')
print('    Eliuton — 2 pontos de MC valem ~5% no preço; (2) são 286 m² de chapa contra')
print('    161 do Eliuton, e custo fixo por m² dilui com o tamanho.')
print('    Se o Jonathan quiser o job dentro da faixa, o caminho é MC, não custo.')
print(f'  Ripado: {area_rip:.2f} m² ({frac_rip*100:.0f}%) precificado à parte a MC 40%')

print(f'\n{"─"*W}\nTERCEIRIZADOS E ESPECIAIS')
for a, d, v, est in TERC:
    print(f'  {a:<22}{d[:56]:<56}R$ {brl(v):>7}')
print(f'  {"":<22}{"TOTAL":<56}R$ {brl(custo_terc):>7}')
print('═'*W)
