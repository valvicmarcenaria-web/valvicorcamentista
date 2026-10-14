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

MC_ALVO = 0.37                      # ⭐ [Jonathan 13/10] — o que fabricamos
# ⭐⭐ [Jonathan 14/10] "considere uma MC de 25% para as portas, senão o
#   preço vai ficar inviável para o cliente". Faz sentido além do preço: a
#   porta pronta é REVENDA — chega montada, nós só penduramos. Margem segue
#   trabalho agregado, e aqui ele é pouco.
MC_PORTA = 0.25
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
#   ⭐⭐ [Jonathan 14/10] COTAÇÃO FECHADA, valores unitários, SEM DOBRADIÇA:
#     porta fumê R$ 1.300 · porta de espelho R$ 900.
PORTA_RB_UN  = 1300.0   # ⭐ porta pronta fumê, 52,5 × 250, a folha
PORTA_ESP_UN =  900.0   # ⭐ porta pronta de espelho, 56 × 250, a folha
# ⛔ A dobradiça NÃO vem com a porta — é compra nossa. Para folha de 2,50 de
#   altura e ~17 kg são QUATRO por folha. ★ E tem de ser a dobradiça que o
#   PERFIL aceita: ela não se encaixota no vidro, fixa no alumínio. Conferir
#   o modelo com o próprio fornecedor da porta.
DOBR_PERFIL  = 70.0     # ★ dobradiça para perfil de alumínio
N_DOBR       = 4        # por folha, de 2,50 de altura
INSTALA_UN   = 60.0     # ★ fixação e regulagem na nossa caixa, por folha
MDF_18    = 600.0    # MDF cor 18 mm — base da casa
FITA_M    = 3.0 + 2.5
DOBR_MDF   = 35.0    # dobradiça com amortecedor — base da casa

def preco(cd, mc=None):
    return cd/(BASE - (MC_ALVO if mc is None else mc))
def pv10(cd, mc=None):               # preço arredondado à dezena, como a casa
    return round(preco(cd, mc)/10)*10

# ── 16 folhas em REFLECTA BRONZE ─────────────────────────────────────────
area_f   = FOLHA_L*FOLHA_A
perim_f  = 2*(FOLHA_L + FOLHA_A)
RB = dict(
    porta   = N_VIDRO*PORTA_RB_UN,
    dobr    = N_VIDRO*N_DOBR*DOBR_PERFIL,
    instala = N_VIDRO*INSTALA_UN)
RB['cd'] = sum(RB.values())*(1 + M.EMBALAGEM)

# ── as mesmas 16 folhas em MDF FENDI, branco por dentro ──────────────────
area_t  = N_VIDRO*area_f
chapas  = -(-area_t/(CH_M2*APROV)//1)
FE = dict(
    chapa = chapas*MDF_18,
    fita  = N_VIDRO*perim_f*FITA_M,
    dobr  = N_VIDRO*N_DOBR*DOBR_MDF)   # ⛔ mesma altura, mesmas quatro
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
    dobr    = ESP_N_FOLHAS*N_DOBR*DOBR_PERFIL,
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
    print(f'{"":<34}{"FUMÊ ⚠":>18}{"MDF FENDI":>16}')
    print('─'*W)
    print(f'{"porta pronta / chapa de 18":<34}{br(RB["porta"]):>18}{br(FE["chapa"]):>16}')
    print(f'{"fita de borda":<34}{"—":>18}{br(FE["fita"]):>16}')
    print(f'{"dobradiça · " + str(N_DOBR) + " por folha":<34}{br(RB["dobr"]):>18}{br(FE["dobr"]):>16}')
    print(f'{"fixação e regulagem":<34}{br(RB["instala"]):>18}{"—":>16}')
    print('─'*W)
    print(f'{"CUSTO DIRETO":<34}{br(RB["cd"]):>18}{br(FE["cd"]):>16}')
    print(f'{"preço":<34}{br(preco(RB["cd"])):>18}{br(preco(FE["cd"])):>16}')
    print(f'\n  ⭐ A porta de vidro é ITEM COMPRADO — entra pronta, a '
          f'R$ {br(PORTA_RB_UN)} a folha,')
    print(f'    SEM dobradiça [Jonathan 14/10]. A de Fendi nós fabricamos.')
    print(f'\n  ⚠⚠ A COTAÇÃO VOLTOU COMO "FUMÊ" E O PROJETO PEDE "REFLECTA')
    print('    BRONZE". Não é a mesma coisa: fumê é vidro TINGIDO na massa,')
    print('    cinza-marrom e translúcido; reflecta é vidro com CAMADA')
    print('    REFLETIVA, que espelha e custa mais. O render da arquiteta')
    print('    mostra as portas refletindo o ambiente — é reflecta.')
    print('    ⛔ Se o fornecedor cotou fumê, ou ele trocou o produto ou a')
    print('      palavra foi nossa. Confirmar ANTES de fechar: se for mesmo')
    print('      reflecta, o preço da folha sobe e todo este quadro anda.')

    print(f'\n{"═"*W}')
    print('⭐ O CUSTO DE CADA PORTA, UMA A UMA')
    print(f'{"═"*W}')
    print(f'  folha de {vg(FOLHA_L)} × {vg(FOLHA_A)} m = {vg(area_f)} m² de vão '
          f'e {vg(perim_f)} m de perímetro')
    print(f'\n{"":<40}{"bronze":>12}{"Fendi":>12}')
    print('─'*W)
    print(f'{"porta pronta ⭐ · chapa de 18":<40}'
          f'{br(RB["porta"]/N_VIDRO):>12}{br(FE["chapa"]/N_VIDRO):>12}')
    print(f'{"fita de borda":<40}{"—":>12}{br(FE["fita"]/N_VIDRO):>12}')
    print(f'{str(N_DOBR) + " dobradiças ★":<40}'
          f'{br(RB["dobr"]/N_VIDRO):>12}{br(FE["dobr"]/N_VIDRO):>12}')
    print(f'{"fixação e regulagem ★ · consumíveis":<40}'
          f'{br(RB["instala"]/N_VIDRO):>12}'
          f'{br(FE["cd"]/N_VIDRO - (FE["chapa"]+FE["fita"]+FE["dobr"])/N_VIDRO):>12}')
    print('─'*W)
    print(f'{"CUSTO DIRETO POR PORTA":<40}'
          f'{br(RB["cd"]/N_VIDRO):>12}{br(FE["cd"]/N_VIDRO):>12}')
    print(f'{"PREÇO POR PORTA  ·  MC 37%, sem RT":<40}'
          f'{br(preco(RB["cd"])/N_VIDRO):>12}{br(preco(FE["cd"])/N_VIDRO):>12}')

    print(f'\n  ⭐ A COTAÇÃO CHEGOU e o preço da porta está cravado. O que')
    print(f'    sobra de ★ na folha de vidro é só a dobradiça: '
          f'R$ {br(N_DOBR*DOBR_PERFIL)} dos')
    print(f'    R$ {br(RB["cd"]/N_VIDRO)} de custo — {N_DOBR*DOBR_PERFIL/(RB["cd"]/N_VIDRO)*100:.0f}%. '
          f'Erra 30% nela e o preço da porta')
    print(f'    anda R$ {br(preco(0.30*N_DOBR*DOBR_PERFIL*1.02))}. Não muda orçamento; muda conferência.')
    print(f'\n  ⚠ A dobradiça TEM DE SER A QUE O PERFIL ACEITA — ela fixa no')
    print('    alumínio, não se encaixota no vidro. Vale perguntar ao mesmo')
    print('    fornecedor qual modelo o perfil dele recebe, já que ele não')
    print('    fornece. E confirmar se quatro por folha bastam a 2,50 de')
    print('    altura: a tabela de alguns fabricantes pede cinco.')
    print(f'\n  ⚠ A PORTA DE FENDI TEM 2,50 DE ALTURA E 18 mm. Folha alta e')
    print('    estreita em melamínico empena com o tempo. ⭐ A de vidro não')
    print('    tem esse problema — o perfil de alumínio é o que a mantém reta.')
    print('    Na versão toda em Fendi isso precisa ser dito à cliente.')

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
    print(f'    duas folhas prontas .. R$ {br(ESP["porta"])}   ⭐ R$ {br(PORTA_ESP_UN)} a folha')
    print(f'    dobradiça ............ R$ {br(ESP["dobr"])}   ★ {N_DOBR} por folha')
    print(f'    fixação e regulagem .. R$ {br(ESP["instala"])}   ★')
    print(f'\n  ⭐ O ESPELHO É MAIS BARATO QUE O FUMÊ — R$ {br(PORTA_ESP_UN)} contra '
          f'R$ {br(PORTA_RB_UN)}')
    print('    a folha. Contraintuitivo e útil: a porta que a cliente quer na')
    print('    sapateira é a mais barata das três, não a mais cara.')
    print(f'\n  ⭐ DIVIDIR RESOLVE O PESO. Em folha única eram {vg(ESP_L*ESP_A)} m² — mais de')
    print('    25 kg só de vidro, de giro, em balanço numa folha de 2,50 de')
    print(f'    altura: descairia. Em duas de {vg(ESP_FL)}, cada folha fica com '
          f'{vg(ESP_FL*ESP_A)} m²')
    print('    e a dobradiça trabalha dentro do que aguenta. De giro passa a')
    print('    ser viável — não precisa ser de correr.')
    print('\n  ⚠ Ainda vale pedir, por comparação, o preço da folha única')
    print('    de 1,12 — para sabermos quanto custou a decisão de dividir, e')
    print('    não só que ela é a certa.')
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
    print('⭐⭐ OS CENÁRIOS — VALOR DE VENDA DAS PORTAS')
    print(f'{"═"*W}')
    print(f'  portas a MC {MC_PORTA*100:.0f}%  [Jonathan 14/10]  ·  '
          f'o resto do closet segue a {MC_ALVO*100:.0f}%')
    cd_fu = (PORTA_RB_UN  + N_DOBR*DOBR_PERFIL + INSTALA_UN)*(1 + M.EMBALAGEM)
    cd_es = (PORTA_ESP_UN + N_DOBR*DOBR_PERFIL + INSTALA_UN)*(1 + M.EMBALAGEM)
    cd_fe = FE['cd']/N_VIDRO
    u_fu, u_es, u_fe = (pv10(cd_fu, MC_PORTA), pv10(cd_es, MC_PORTA),
                        pv10(cd_fe, MC_PORTA))
    print(f'\n  {"unitário de venda":<34}{"custo":>10}{"venda":>10}')
    print('  ' + '─'*56)
    for nome, cd, pv in (('porta fumê', cd_fu, u_fu),
                         ('porta de espelho · sapateira', cd_es, u_es),
                         ('porta em MDF Fendi', cd_fe, u_fe)):
        print(f'  {nome:<34}{br(cd):>10}{br(pv):>10}')

    CEN = [('1 · mista',               5, 11, 2),
           ('2 · como o projeto',     16,  0, 2),
           ('3 · toda em Fendi',       0, 16, 2)]
    print(f'\n  {"":<24}{"fumê":>7}{"Fendi":>7}{"espelho":>9}'
          f'{"VENDA":>12}{"custo":>10}{"MC R$":>10}')
    print('  ' + '─'*80)
    TOT = {}
    for nome, nf, nd, ne in CEN:
        venda = nf*u_fu + nd*u_fe + ne*u_es
        custo = nf*cd_fu + nd*cd_fe + ne*cd_es
        TOT[nome] = (venda, custo)
        print(f'  {nome:<24}{nf:>7}{nd:>7}{ne:>9}{br(venda):>12}'
              f'{br(custo):>10}{br(venda*(BASE-custo/venda)):>10}')
    print('  ' + '─'*80)
    v1, v2, v3 = (TOT[c[0]][0] for c in CEN)
    print(f'  {"a V2 custa a mais que a V3":<24}{"":>23}{br(v2-v3):>12}')
    print(f'  {"a V1 custa a mais que a V3":<24}{"":>23}{br(v1-v3):>12}')

    print(f'\n  ⭐ O QUE A MC DE 25% FEZ COM O PREÇO:')
    for nome, nf, nd, ne in CEN:
        a37 = nf*pv10(cd_fu) + nd*pv10(cd_fe) + ne*pv10(cd_es)
        print(f'    {nome:<22} a 37% seria R$ {br(a37):>7}  ·  '
              f'a 25% é R$ {br(TOT[nome][0]):>7}  ·  '
              f'−R$ {br(a37-TOT[nome][0])}')
    print('\n    ⛔ E o que a casa abre de margem nisso, na V2, são')
    _a37 = 16*pv10(cd_fu) + 2*pv10(cd_es)
    _c37 = 16*cd_fu + 2*cd_es
    print(f'      R$ {br(_a37*(BASE-_c37/_a37) - v2*(BASE-TOT[CEN[1][0]][1]/v2))} — '
          f'de R$ {br(_a37*(BASE-_c37/_a37))} para R$ {br(v2*(BASE-TOT[CEN[1][0]][1]/v2))}.')
    print('      É uma decisão de preço, não um desconto: a porta chega')
    print('      montada e a margem de revenda não é a de fabricação.')

    print(f'\n  ⛔⛔ MAS ISSO PUXA A MC DO PROJETO PARA BAIXO DO PISO.')
    print('    Com porta a 25% e o resto a 37%, para a MC cheia voltar aos')
    print('    35% da casa o RESTO DO CLOSET precisa valer 5× as portas:')
    for nome, _nf, _nd, _ne in CEN:
        d = TOT[nome][0]
        print(f'      {nome:<22} portas R$ {br(d):>7}  →  resto ≥ R$ {br(5*d)}')
    print('    ⛔ Na V2 isso é improvável. Ou seja: a versão que o projeto')
    print('      desenhou é a que mais dilui a nossa margem — e é bom saber')
    print('      disso ANTES de a cliente escolher, não depois.')

    # ══ COMO NÃO SUPERFATURAR A PORTA ═════════════════════════════════
    print(f'\n{"═"*W}')
    print('⭐⭐ COMO NÃO SUPERFATURAR A PORTA  [Jonathan 14/10]')
    print(f'{"═"*W}')
    print(f'  Custo R$ {br(cd_fu)}, venda R$ {br(u_fu)} — '
          f'{u_fu/cd_fu:.2f}× o custo. É muito, e o')
    print('  motivo NÃO é a margem: é a CASCATA. A porta está pagando')
    print('  desgaste de serra, manutenção de máquina, programação e')
    print('  fabricação — e ela não encosta na serra. Chega montada.')
    print('\n  O que a porta comprada REALMENTE usa:')
    enc_cheio = M.encargos(0, RT_ON, False)
    USA = {'nota fiscal': 'sim, é faturada',
           'margem de erro': 'sim, quebra acontece',
           'desgaste de serra': '⛔ NÃO — não passa na serra',
           'manutenção de máquinas': '⛔ NÃO — não usa máquina',
           'produção · coordenacao': 'sim, alguém compra e confere',
           'produção · programacao': '⛔ NÃO — não há o que programar',
           'produção · fabricacao': '⛔ NÃO — não fabricamos',
           'produção · montagem': 'sim, nós penduramos'}
    for k, v in USA.items():
        if enc_cheio.get(k): print(f'    {k:<26}{enc_cheio[k]*100:>6.2f}%   {v}')
    LIQ = 1 - M.NF
    ENC_REV = M.NF + M.ERRO + LIQ*(M.PRODUCAO['coordenacao'] + M.PRODUCAO['montagem'])
    BASE_REV = 1 - ENC_REV
    print(f'\n  ⭐ base da casa {BASE*100:.2f}%  →  base de REVENDA '
          f'{BASE_REV*100:.2f}%')

    MARG_FIXA = 400.0    # ★ receber, guardar, pendurar, alinhar e garantir
    def pA(cd): return round(cd/(BASE - MC_PORTA)/10)*10
    def pB(cd): return round(cd/(BASE_REV - MC_PORTA)/10)*10
    def pC(cd): return round((cd + MARG_FIXA)/BASE_REV/10)*10

    POL = [('A · hoje — cascata cheia, MC 25%', pA),
           ('B · cascata de revenda, MC 25%',   pB),
           (f'C · cascata de revenda + R$ {br(MARG_FIXA)} por folha', pC)]
    print(f'\n  {"":<42}{"fumê":>9}{"espelho":>9}{"× custo":>10}')
    print('  ' + '─'*72)
    for nome, f_ in POL:
        print(f'  {nome:<42}{br(f_(cd_fu)):>9}{br(f_(cd_es)):>9}'
              f'{f_(cd_fu)/cd_fu:>9.2f}×')

    print(f'\n  {"":<42}{"V1":>9}{"V2":>9}{"V3":>9}')
    print('  ' + '─'*72)
    for nome, f_ in POL:
        t = [nf*f_(cd_fu) + nd*u_fe + ne*f_(cd_es) for _n, nf, nd, ne in CEN]
        print(f'  {nome:<42}' + ''.join(f'{br(x):>9}' for x in t))
    print('  ' + '─'*72)
    _mcA = 16*(pA(cd_fu)*BASE     - cd_fu) + 2*(pA(cd_es)*BASE     - cd_es)
    _mcB = 16*(pB(cd_fu)*BASE_REV - cd_fu) + 2*(pB(cd_es)*BASE_REV - cd_es)
    print(f'  {"↑ e a MC que a casa leva na V2:":<42}'
          f'{"":>9}{br(_mcA):>9}'.replace(br(_mcA), '') + '')
    print(f'    A · R$ {br(_mcA)}   ·   B · R$ {br(_mcB)}   ·   '
          f'C · R$ {br(18*MARG_FIXA)}')

    print('\n  ⭐⭐ A OPÇÃO C É A HONESTA, E NÃO SÓ POR SER MAIS BARATA:')
    print('    margem em PERCENTUAL sobre item comprado premia comprar caro —')
    print('    se o fornecedor subir o preço, a nossa margem em reais sobe')
    print('    junto, pelo mesmo trabalho. Em REAIS POR FOLHA isso não')
    print('    acontece: receber, guardar, pendurar, alinhar e garantir uma')
    print('    porta custa o mesmo, valha ela R$ 900 ou R$ 1.300.')
    print('\n  ⭐ E ela se apresenta bem ao cliente, em duas linhas. Na V2:')
    # ⛔ [Jonathan 14/10] "o fornecimento das portas não dá 32.670". Não dá
    #   mesmo: aquela linha tinha dobradiça e mão de obra dentro. FORNECIMENTO
    #   é só a folha comprada; dobradiça e fixação são serviço nosso.
    _compra = 16*PORTA_RB_UN + 2*PORTA_ESP_UN          # a nota do fornecedor
    _cd_forn = _compra*(1 + M.EMBALAGEM)
    _cd_serv = 18*(N_DOBR*DOBR_PERFIL + INSTALA_UN)*(1 + M.EMBALAGEM)
    _forn = round(_cd_forn/BASE_REV/10)*10
    _serv = round((_cd_serv + 18*MARG_FIXA)/BASE_REV/10)*10
    print(f'      fornecimento das portas · 18 folhas  R$ {br(_forn)}')
    print(f'      ferragem, instalação e garantia .... R$ {br(_serv)}')
    print(f'      {"":<36}  ─────────')
    print(f'      {"":<36}  R$ {br(_forn + _serv)}')
    print(f'\n    ⭐ A NOTA DO FORNECEDOR É R$ {br(_compra)} — 16 folhas de fumê a')
    print(f'      R$ {br(PORTA_RB_UN)} e 2 de espelho a R$ {br(PORTA_ESP_UN)}. A nossa linha de')
    print(f'      fornecimento fica R$ {br(_forn)}, {(_forn/_compra-1)*100:.0f}% acima — e isso NÃO é')
    print('      margem: é nota fiscal, margem de erro e as duas comissões')
    print('      que o item de fato usa. Se a cliente ligar para o vidraceiro,')
    print('      ela acha os R$ ' + br(_compra) + ' e a diferença se explica em uma frase.')
    print(f'\n    ⛔ A dobradiça sozinha é R$ {br(18*N_DOBR*DOBR_PERFIL)} de compra — '
          f'{18*N_DOBR*DOBR_PERFIL/_compra*100:.0f}% do valor')
    print('      das portas. Ela estava escondida dentro de "fornecimento" e')
    print('      é por isso que aquela linha tinha ficado inchada.')
    print(f'\n  ⚠ Os R$ {br(MARG_FIXA)} por folha são ★ meus. Mexa neles e tudo anda:')
    for mf in (300, 400, 500):
        t = [nf*round((cd_fu+mf)/BASE_REV/10)*10 + nd*u_fe
             + ne*round((cd_es+mf)/BASE_REV/10)*10 for _n, nf, nd, ne in CEN]
        print(f'      R$ {br(mf)} por folha →  V1 {br(t[0])}  ·  V2 {br(t[1])}'
              f'  ·  V3 {br(t[2])}')

    print(f'\n{"═"*W}')
    print('⛔⛔ O QUE FALTA — e por que ainda não há três preços')
    print(f'{"═"*W}')
    print(f'  1 · ✅ A COTAÇÃO DA PORTA CHEGOU [Jonathan 14/10]: fumê '
          f'R$ {br(PORTA_RB_UN)} e')
    print(f'      espelho R$ {br(PORTA_ESP_UN)} a folha, sem dobradiça. '
          f'É {RB["porta"]/RB["cd"]*100:.0f}% do custo da')
    print('      folha de vidro e deixou de ser palpite.')
    print('      ⚠ Faltou a resposta das outras perguntas da relação — a')
    print('        altura máxima de folha da linha é a que mais importa.')
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
