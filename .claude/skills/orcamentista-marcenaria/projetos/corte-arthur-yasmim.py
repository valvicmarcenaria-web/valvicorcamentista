# -*- coding: utf-8 -*-
"""ARTHUR & YASMIM — closet · o que separa as três versões  [13/10/2026]

Caderno `Apresentação de Projeto de Arthur & Yasmim.pdf`. ⛔ 181 MB, imagem
pura, não abre pelo Drive nesta sessão — as páginas do CLOSET chegaram pelo
chat em 13/10. Não há páginas por módulo, então **a modulação completa ainda
não está fechada**.

⭐ [Jonathan 13/10]
   · versão principal com **corrediça oculta Hettich**
   · **downgrade** para **telescópica**, e SÓ isso muda
   · **sem RT** — a cliente fala direto com a casa
   · **MC de 37%**
   · **custo da iluminação separado**

⭐ O PEDIDO DA CLIENTE — três formas, 17 portas
   V1 ·  5 reflecta bronze + 11 Fendi + 1 espelho inteiriço (sapateira)
   V2 · 16 reflecta bronze + 1 espelho          ← como o projeto
   V3 · 16 Fendi + 1 espelho
   "a parte de dentro das portas que serão no Fendi podem ser brancas"

⛔⛔ ESTE MOTOR NÃO ORÇA O CLOSET INTEIRO — ainda não dá. Ele calcula, com
   as cotas que existem, **o que separa as três versões**: o Δ por folha
   entre reflecta bronze e Fendi. Como as três versões diferem SÓ nisso, o
   Δ responde a pergunta da cliente sem depender da modulação.

AS COTAS QUE EXISTEM
   closet ......... 410 de vão livre entre as duas fileiras · 260 de altura
   penteadeira .... 105 de largura (módulo 3, sem porta)
   módulo tipo .... 105 de largura com DUAS folhas → folha de 52,5
   sapateira ...... 110 + coluna lateral de 23 · prateleiras inclinadas
                    (porta-botas 42 no alto · vãos de 24 e 30)
   espelho ........ 112 × 250
   fileira direita  166 de comprimento
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')
vg  = lambda v, n=2: f'{v:.{n}f}'.replace('.', ',')

MC_ALVO = 0.37                      # ⭐ [Jonathan 13/10]
RT_ON   = False                     # ⭐ [Jonathan 13/10] sem RT
BASE    = M.base(parcelas=0, rt=RT_ON, vendedor=False)
CH_M2, APROV = 2.75*1.85, 0.80

# ── a folha ───────────────────────────────────────────────────────────────
FOLHA_L, FOLHA_A = 0.525, 2.50      # módulo de 105 com duas folhas
N_VIDRO, N_TOTAL = 16, 17           # 16 folhas + o espelho da sapateira
ESP_L, ESP_A = 1.12, 2.50           # o VÃO do espelho, cotado na prancha
# ⭐ [Jonathan 13/10] "a porta de espelho no vão de 1,12 precisa ser duas
#   portas". São duas folhas de 56 — e isso resolve o problema de peso que
#   eu tinha levantado: cada folha cai para metade da área.
ESP_N_FOLHAS = 2
ESP_FL = ESP_L/ESP_N_FOLHAS

# ── preços ────────────────────────────────────────────────────────────────
# ⭐⭐ [Jonathan 13/10] "nós adquirimos a porta PRONTA". A porta de vidro
#   não se monta aqui: entra como item comprado, folha a folha, com perfil,
#   vidro, dobradiça e puxador do fornecedor.
#   ⛔ Estes dois são ★ PLACEHOLDERS até a cotação voltar. A relação para
#     cotar está em `relacao-portas-arthur-yasmim.md`.
PORTA_RB_UN  = 1500.0   # ★ porta pronta reflecta bronze, 52,5 × 250, a folha
PORTA_ESP_UN = 1600.0   # ★ porta pronta de espelho, 56 × 250, a folha
INSTALA_UN   = 60.0     # ★ fixação e regulagem na nossa caixa, por folha
MDF_18    = 600.0    # MDF cor 18 mm — base da casa
FITA_M    = 3.0 + 2.5
DOBR_MDF   = 35.0    # dobradiça com amortecedor — base da casa

def preco(cd):  return cd/(BASE - MC_ALVO)

# ── 16 folhas em REFLECTA BRONZE ─────────────────────────────────────────
area_f   = FOLHA_L*FOLHA_A
perim_f  = 2*(FOLHA_L + FOLHA_A)
RB = dict(
    porta   = N_VIDRO*PORTA_RB_UN,
    instala = N_VIDRO*INSTALA_UN)
RB['cd'] = sum(RB.values())*(1 + M.EMBALAGEM)

# ── as mesmas 16 folhas em MDF FENDI, branco por dentro ──────────────────
area_t  = N_VIDRO*area_f
chapas  = -(-area_t/(CH_M2*APROV)//1)
FE = dict(
    chapa = chapas*MDF_18,
    fita  = N_VIDRO*perim_f*FITA_M,
    dobr  = N_VIDRO*2*DOBR_MDF)
FE['cd'] = (FE['chapa'] + FE['fita'])*1.06 + FE['dobr']
FE['cd'] *= (1 + M.EMBALAGEM)

DELTA_CD   = RB['cd'] - FE['cd']
DELTA_PV   = preco(DELTA_CD)
DELTA_FOLHA = DELTA_PV/N_VIDRO

# ── o espelho inteiriço da sapateira, igual nas três versões ─────────────
# ⛔ 1,12 × 2,50 = 2,8 m². Em espelho 4 mm isso passa de 25 kg só de vidro.
#   Numa folha de 2,50 de altura, de giro, a dobradiça trabalha em balanço.
ESP = dict(
    porta   = ESP_N_FOLHAS*PORTA_ESP_UN,
    instala = ESP_N_FOLHAS*INSTALA_UN)
ESP['cd'] = sum(ESP.values())*(1 + M.EMBALAGEM)
ESP['pv'] = preco(ESP['cd'])

# ── a corrediça: principal × downgrade ───────────────────────────────────
# ⭐ As gavetas ficam ATRÁS do vidro — com telescópica vê-se o trilho.
CORR_OCULTA = 190.0   # ★ Hettich oculta com amortecimento, por par
CORR_TELE   = 85.0    # corrediça telescópica — base da casa
N_GAV = 24            # ★ gavetas contadas nos renders; a confirmar
DELTA_CORR_CD = N_GAV*(CORR_OCULTA - CORR_TELE)*(1 + M.EMBALAGEM)
DELTA_CORR_PV = preco(DELTA_CORR_CD)

if __name__ == '__main__':
    W = 88
    print('═'*W)
    print('ARTHUR & YASMIM — closet  ·  o que separa as três versões')
    print(f'MC {MC_ALVO*100:.0f}% · sem RT · base {BASE*100:.2f}%   [Jonathan 13/10]')
    print('═'*W)

    print(f'\n{"═"*W}')
    print(f'AS 16 FOLHAS — folha de {vg(FOLHA_L)} × {vg(FOLHA_A)} m, módulo de duas')
    print(f'{"═"*W}')
    print(f'{"":<34}{"REFLECTA BRONZE":>18}{"MDF FENDI":>16}')
    print('─'*W)
    print(f'{"porta pronta / chapa de 18":<34}{br(RB["porta"]):>18}{br(FE["chapa"]):>16}')
    print(f'{"fita de borda":<34}{"—":>18}{br(FE["fita"]):>16}')
    print(f'{"dobradiça":<34}{"no fornecedor":>18}{br(FE["dobr"]):>16}')
    print(f'{"fixação e regulagem":<34}{br(RB["instala"]):>18}{"—":>16}')
    print('─'*W)
    print(f'{"CUSTO DIRETO":<34}{br(RB["cd"]):>18}{br(FE["cd"]):>16}')
    print(f'{"preço":<34}{br(preco(RB["cd"])):>18}{br(preco(FE["cd"])):>16}')
    print(f'\n  ⭐ A porta de vidro é ITEM COMPRADO [Jonathan 13/10] — entra')
    print(f'    pronta, a R$ {br(PORTA_RB_UN)} ★ a folha. A de Fendi nós fabricamos.')

    print(f'\n{"═"*W}')
    print('⭐ O CUSTO DE CADA PORTA, UMA A UMA')
    print(f'{"═"*W}')
    print(f'  folha de {vg(FOLHA_L)} × {vg(FOLHA_A)} m = {vg(area_f)} m² de vão '
          f'e {vg(perim_f)} m de perímetro')
    print(f'\n{"":<40}{"bronze":>12}{"Fendi":>12}')
    print('─'*W)
    print(f'{"porta pronta ★ · chapa de 18":<40}'
          f'{br(RB["porta"]/N_VIDRO):>12}{br(FE["chapa"]/N_VIDRO):>12}')
    print(f'{"fita de borda":<40}{"—":>12}{br(FE["fita"]/N_VIDRO):>12}')
    print(f'{"duas dobradiças":<40}'
          f'{"no fornecedor":>12}{br(FE["dobr"]/N_VIDRO):>12}')
    print(f'{"fixação e regulagem ★ · consumíveis":<40}'
          f'{br(RB["instala"]/N_VIDRO):>12}'
          f'{br(FE["cd"]/N_VIDRO - (FE["chapa"]+FE["fita"]+FE["dobr"])/N_VIDRO):>12}')
    print('─'*W)
    print(f'{"CUSTO DIRETO POR PORTA":<40}'
          f'{br(RB["cd"]/N_VIDRO):>12}{br(FE["cd"]/N_VIDRO):>12}')
    print(f'{"PREÇO POR PORTA  ·  MC 37%, sem RT":<40}'
          f'{br(preco(RB["cd"])/N_VIDRO):>12}{br(preco(FE["cd"])/N_VIDRO):>12}')

    print(f'\n  ⛔ O NÚMERO QUE FALTA É UM SÓ: quanto o fornecedor cobra pela')
    print('    folha pronta. Tudo o mais já está fechado. Quando a cotação')
    print('    voltar, é trocar uma linha do motor.')
    print(f'\n  {"compra a folha →":<20}'
          + ''.join(f'{br(v):>9}' for v in (900, 1200, 1500, 1800, 2100)))
    print('  ' + '─'*65)
    _l1 = '  preço por porta'.ljust(20)
    _l2 = '  V1 · 5 bronze'.ljust(20)
    _l3 = '  V2 · 16 bronze'.ljust(20)
    for c in (900, 1200, 1500, 1800, 2100):
        cd1 = (c + INSTALA_UN)*(1 + M.EMBALAGEM)
        d   = preco(cd1) - preco(FE['cd'])/N_VIDRO
        _l1 += f'{br(preco(cd1)):>9}'
        _l2 += f'{br(5*d):>9}'
        _l3 += f'{br(16*d):>9}'
    for ln in (_l1, '  ' + '─'*65, _l2, _l3): print(ln)
    print('\n    As duas últimas linhas são o quanto cada versão fica ACIMA da')
    print('    V3, que é toda em Fendi. ⛔ Entre as pontas da tabela a V2')
    print(f'    varia R$ {br(16*(preco((2100+INSTALA_UN)*1.02) - preco((900+INSTALA_UN)*1.02)))} — '
          f'é a cotação que decide o orçamento, não nós.')

    print(f'\n{"═"*W}')
    print('⭐ O Δ QUE RESPONDE A PERGUNTA DA CLIENTE')
    print(f'{"═"*W}')
    print(f'  cada folha de reflecta bronze custa, a mais que uma de Fendi:')
    print(f'    R$ {br(DELTA_CD/N_VIDRO)} de custo   ·   R$ {br(DELTA_FOLHA)} de preço')
    print(f'\n  {"":<40}{"bronze":>8}{"a mais que a V3":>18}')
    print('  ' + '─'*66)
    for nome, n in (('V3 · todas em Fendi', 0),
                    ('V1 · 5 bronze + 11 Fendi', 5),
                    ('V2 · todas em bronze, como o projeto', 16)):
        print(f'  {nome:<40}{n:>8}{br(n*DELTA_FOLHA):>18}')
    print(f'\n  ⛔ Entre a V2 e a V3 da cliente há R$ {br(16*DELTA_FOLHA)} — e isso')
    print('    é só a diferença das portas, sem contar o resto do closet.')
    print('    A escolha dela não é de cor: é de dezenas de milhares.')

    print(f'\n{"═"*W}')
    print('⭐ O ESPELHO DA SAPATEIRA — igual nas três versões')
    print(f'{"═"*W}')
    print(f'  Vão de {vg(ESP_L)} × {vg(ESP_A)} m, cotado na prancha, em '
          f'DUAS folhas de {vg(ESP_FL)}  [Jonathan 13/10]')
    print(f'  Custo R$ {br(ESP["cd"])}, preço R$ {br(ESP["pv"])}.')
    print(f'    duas folhas prontas .. R$ {br(ESP["porta"])}   ★ R$ {br(PORTA_ESP_UN)} a folha, a cotar')
    print(f'    fixação e regulagem .. R$ {br(ESP["instala"])}   ★')
    print(f'\n  ⭐ DIVIDIR RESOLVE O PESO. Em folha única eram {vg(ESP_L*ESP_A)} m² — mais de')
    print('    25 kg só de vidro, de giro, em balanço numa folha de 2,50 de')
    print(f'    altura: descairia. Em duas de {vg(ESP_FL)}, cada folha fica com '
          f'{vg(ESP_FL*ESP_A)} m²')
    print('    e a dobradiça trabalha dentro do que aguenta. De giro passa a')
    print('    ser viável — não precisa ser de correr.')
    print('\n  ⚠ Pedir ao fornecedor o preço das DUAS folhas e, por')
    print('    curiosidade, o da folha única de 1,12 — para sabermos quanto')
    print('    custa a decisão, e não só que ela é a certa.')
    print('  ⚠⚠ MAS A CLIENTE PEDIU "UMA PORTA INTEIRIÇA DE ESPELHO". Em duas')
    print('    folhas aparece uma JUNTA VERTICAL no meio do espelho, bem na')
    print('    altura do rosto. Ela precisa saber disso antes, não depois —')
    print('    e, se insistir em folha única, o caminho é DE CORRER.')
    print(f'\n  ⚠ E a CONTA DE PORTAS muda: {N_VIDRO} de vidro + {ESP_N_FOLHAS} de espelho = '
          f'{N_VIDRO+ESP_N_FOLHAS} folhas,')
    print(f'    não as {N_TOTAL} que a cliente contou. O escopo é o mesmo; o número')
    print('    que ela repetir ao marido é que não vai bater com o nosso.')

    print(f'\n{"═"*W}')
    print('⭐ PRINCIPAL × DOWNGRADE — só a corrediça muda')
    print(f'{"═"*W}')
    print(f'  oculta Hettich R$ {br(CORR_OCULTA)} o par ★ · telescópica R$ {br(CORR_TELE)} — base da casa')
    print(f'  sobre ★ {N_GAV} gavetas: R$ {br(DELTA_CORR_CD)} de custo, '
          f'R$ {br(DELTA_CORR_PV)} de preço.')
    print('\n  ⭐ AS GAVETAS FICAM ATRÁS DO VIDRO. Com telescópica vê-se o')
    print('    trilho pela lateral da gaveta, o dia inteiro, através da porta.')
    print('    Com a oculta não se vê nada e a gaveta parece flutuar. Num')
    print('    closet envidraçado esse é o argumento — não o amortecimento.')

    print(f'\n{"═"*W}')
    print('⛔⛔ O QUE FALTA — e por que ainda não há três preços')
    print(f'{"═"*W}')
    print(f'  1 · A COTAÇÃO DA PORTA PRONTA. É {RB["porta"]/RB["cd"]*100:.0f}% do custo da versão')
    print('      bronze e está ★ em placeholder. ⭐ A RELAÇÃO PARA COTAR JÁ')
    print('      ESTÁ PRONTA em `relacao-portas-arthur-yasmim.md`: folhas,')
    print('      medidas, especificação e as nove perguntas para o fornecedor.')
    print('  2 · A MODULAÇÃO. O caderno numera dez módulos mas não traz a')
    print('      página de cada um. Sem as larguras e profundidades não há')
    print('      preço do closet — só o Δ entre as versões, que é este.')
    print('  3 · "5 PORTAS NO REFLECTA BRONZE" — 5 é ímpar e os módulos são')
    print('      de duas folhas. Ou algum módulo tem folha única, ou ela')
    print('      contou por módulo em algum ponto. A confirmar com ela.')
    print('  4 · ILUMINAÇÃO EM LINHA SEPARADA [Jonathan 13/10]. Falta medir')
    print('      quantos metros de fita e em quantas prateleiras, e separar o')
    print('      que é nosso (perfil, usinagem, instalação) do que é da')
    print('      elétrica (fonte, driver, circuito).')
    print(f'  5 · ★ {N_GAV} gavetas foram CONTADAS NOS RENDERS. Muda o Δ da')
    print('      corrediça na proporção direta.')
