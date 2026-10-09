# -*- coding: utf-8 -*-
"""RAQUEL OLIVEIRA — quarto infantil, Belo Horizonte  [09/10/2026]

Projeto: PRJ_EXEC_RAQUEL_O_rn, 10/2026, 6 pranchas A4. Designer **Rubia
Nascimento**. ⛔ "CONFERIR MEDIDAS NO LOCAL" e "EM CASO DE DÚVIDA, NÃO
EXECUTE: LIGUE PARA A DESIGNER" em todas as pranchas.

⛔⛔ A MAIOR PARTE DO QUE ESTÁ DESENHADO NÃO É MARCENARIA — papel de parede,
   pendentes, abajur, roupa de cama, cadeira, mesa lateral, pufe, dossel,
   quadros, suporte para violão e os colchões ficam fora.
   ⚠ O bandô da Vista 4 é "de gesso OU MDF": só é nosso se for MDF.

══ A ESTRUTURA DE PREÇO  [Jonathan 09/10] ════════════════════════════════
  "não faremos o roupeiro completamente novo não, será apenas as portas e
   as prateleiras · unifique o custo do roupeiro e das prateleiras, tanto
   da laca quanto em melamínico · a mesa com ajuste de altura o preço de
   venda é de 2.500 · a cama pode ser 5.900"

  · CAMA ........ R$ 5.900 de VENDA, fechado
  · MESA ........ R$ 2.500 de VENDA, fechado — agora com AJUSTE DE ALTURA
  · ROUPEIRO E PRATELEIRAS ... uma linha só, calculada, em duas versões:
      LACA ........ pinta a frente do roupeiro que já existe e as cinco
                    prateleiras de canto, que são novas
      MELAMÍNICO .. troca as PORTAS do roupeiro e faz as prateleiras de
                    canto em melamínico — ⛔ a caixaria do roupeiro FICA
"""
import importlib.util, pathlib, sys, math
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br1 = lambda v: f'{v:,.1f}'.replace(',','X').replace('.',',').replace('X','.')

CH_M2, APROV = 2.75*1.85, 0.80
PRECO   = {15: 500.0, 18: 600.0}        # MDF cor (Itapuã, Sal Rosa) — base
FITA_M  = 3.0 + 2.5                     # fita cor + filetagem
LACA_M2 = 650.0                         # base da casa, "m² em peça lisa"
MC_ALVO = 0.40                          # ⭐ [Jonathan 08/10]
BASE    = M.base(parcelas=0, rt=False, vendedor=False)   # ★ sem RT

# ⛔ [Jonathan 09/10] dobradiça de porta e puxador SAEM do custo e viram
#   exclusão escrita na proposta. O suporte invisível da prateleira FICA:
#   não é dobradiça nem puxador, e sem ele a prateleira não sobe.
SUPINV = 60.0

# ── itens a PREÇO FECHADO ─────────────────────────────────────────────────
# Mesma convenção das divisórias da United: entra pelo preço, e o custo é o
# implícito pela MC alvo. O que se audita é o TETO DE CUSTO.
FECHADOS = [
    ('Cama com bicama', 5900.0,
     'MDF Itapuã, cabeceira ripada, palha indiana nas laterais e bicama '
     'sobre rodízio'),
    ('Mesa com ajuste de altura', 2500.0,
     'tampo em Itapuã, laterais em Sal Rosa e ⭐ AJUSTE DE ALTURA. '
     '⛔ [Jonathan 09/10] o tampo NÃO É RIPADO — era leitura minha da '
     'textura do desenho. E ⛔ EM MELAMÍNICO NÃO SE ABAÚLA A QUINA: o '
     'revestimento é filme de superfície, arredondar expõe o miolo. '
     'A borda sai reta com fita, e isso está escrito na proposta.'),
]

# ── a linha calculada: ROUPEIRO + PRATELEIRAS ─────────────────────────────
# Frente do roupeiro: 250 × 268 = 6,70 m², em quatro portas.
FRENTE_M2 = 2.50*2.68
QUAD_M2   = math.pi*0.59**2/4                 # quadrante de 59, 0,273 m²
QUAD_N    = 5
# ⛔ 2 cm não é chapa: cada prateleira são duas de 15 coladas e usinadas.
QUAD_PCS  = QUAD_N*2

def _peca(pcs, fer, laca_m2):
    """Custo direto de um conjunto de peças, com o rateio de chapa próprio."""
    area = {}
    for esp, _, c, l, q in pcs:
        area[esp] = area.get(esp, 0.0) + c*l*q/1e4
    chapas   = {e: -(-v/(CH_M2*APROV)//1) for e, v in area.items()}
    custo_ch = sum(chapas[e]*PRECO[e] for e in chapas)
    fita = sum(2*(c+l)*q/100*0.75*FITA_M for _, _, c, l, q in pcs)
    laca = laca_m2*LACA_M2
    cd = ((custo_ch + fita + laca)*1.06 + fer)*(1 + M.EMBALAGEM)
    return cd, dict(chapas=chapas, custo_ch=custo_ch, fita=fita, laca=laca,
                    laca_m2=laca_m2, fer=fer, area=area, CD=cd)

# ⭐ [Jonathan 09/10] "refaça colocando separado apenas o valor das
#   prateleiras." As duas linhas voltam a ser independentes.
def prateleiras(versao):
    """As cinco de canto, em quadrante. Novas nas duas versões."""
    pcs = [(15, 'Prateleira de canto · camada', 59, 59, QUAD_PCS)]
    fer = QUAD_N*2*SUPINV          # ⛔ suporte invisível fica: não é
                                   #   dobradiça nem puxador
    laca_m2 = 0.0 if versao == 'melaminico' else (
        # as duas faces da prateleira pronta, mais o canto curvo
        QUAD_N*QUAD_M2*2 + QUAD_N*(math.pi*0.59/2 + 2*0.59)*0.02)
    return _peca(pcs, fer, laca_m2)

def roupeiro(versao):
    """A frente do roupeiro. Laqueada no lugar, ou portas novas."""
    if versao == 'melaminico':
        # ⭐ só as PORTAS. A caixaria do roupeiro fica onde está.
        return _peca([(18, 'Porta nova do roupeiro', 268, 62.5, 4)], 0.0, 0.0)
    # a frente que já existe é lixada, preparada e laqueada no lugar
    return _peca([], 0.0, FRENTE_M2)

CD_P = {v: prateleiras(v) for v in ('laca', 'melaminico')}
CD_R = {v: roupeiro(v)    for v in ('laca', 'melaminico')}
# preço que a MC alvo pediria, antes da decisão comercial
PV_P0 = {v: round(CD_P[v][0]/(BASE - MC_ALVO)/10)*10 for v in CD_P}
PV_R0 = {v: round(CD_R[v][0]/(BASE - MC_ALVO)/10)*10 for v in CD_R}
TOT   = {v: sum(p for _, p, _ in FECHADOS) + PV_P0[v] + PV_R0[v] for v in PV_R0}

# ⭐ [Jonathan 09/10] "essas prateleiras representam 1 terço do valor que
#   você colocou em ambos os cenários · refaça redistribuindo os valores
#   entre itens sem alterar o valor inicial."
#   ⛔ O TOTAL NÃO MUDA. O que muda é só ONDE o valor aparece: a sobra vai
#     para o roupeiro, que é a outra linha calculada — cama e mesa têm
#     preço fechado pelo Jonathan e não se mexem.
PRAT_FATOR = 1/3
PV_P = {v: round(PV_P0[v]*PRAT_FATOR/10)*10 for v in PV_P0}
PV_R = {v: TOT[v] - sum(p for _, p, _ in FECHADOS) - PV_P[v] for v in PV_P}
CD_F  = {n: p*(BASE - MC_ALVO) for n, p, _ in FECHADOS}   # custo implícito
CD_T  = {v: sum(CD_F.values()) + CD_P[v][0] + CD_R[v][0] for v in PV_R}

NOME_V = {'laca': 'Laca fosca Sayerlack J029',
          'melaminico': 'Portas novas em MDF melamínico'}

if __name__ == '__main__':
    W = 88
    print('═'*W); print('RAQUEL OLIVEIRA — quarto infantil  ·  PRJ_EXEC_RAQUEL_O_rn')
    print('═'*W)
    print(f'\n{"ITEM":<40}{"laca":>13}{"melamínico":>14}')
    print('─'*W)
    for n, p, _ in FECHADOS:
        print(f'{n:<40}{br(p):>13}{br(p):>14}   fechado')
    print(f'{"Prateleiras de canto":<40}'
          f'{br(PV_P["laca"]):>13}{br(PV_P["melaminico"]):>14}')
    print(f'{"Roupeiro · a frente":<40}'
          f'{br(PV_R["laca"]):>13}{br(PV_R["melaminico"]):>14}')
    print('─'*W)
    print(f'{"INVESTIMENTO":<40}{br(TOT["laca"]):>13}{br(TOT["melaminico"]):>14}')
    print(f'{"  custo direto":<40}{br(CD_T["laca"]):>13}{br(CD_T["melaminico"]):>14}')
    print(f'{"  MC":<40}{(BASE-CD_T["laca"]/TOT["laca"])*100:>12.1f}%'
          f'{(BASE-CD_T["melaminico"]/TOT["melaminico"])*100:>13.1f}%')

    print(f'\n{"═"*W}')
    print('A LINHA CALCULADA, POR DENTRO')
    print(f'{"═"*W}')
    for rot_, dd in (('PRATELEIRAS DE CANTO', CD_P), ('ROUPEIRO · A FRENTE', CD_R)):
        print(f'\n  {rot_:<28}{"laca":>13}{"melamínico":>14}')
        for rot, k in (('chapa','custo_ch'), ('fita','fita'), ('laca','laca'),
                       ('ferragem ★','fer'), ('CUSTO DIRETO','CD')):
            print(f'  {rot:<28}{br(dd["laca"][1][k]):>13}'
                  f'{br(dd["melaminico"][1][k]):>14}')
    print(f'  {"chapas (un)":<28}'
          f'{sum(CD_R["laca"][1]["chapas"].values()):>13.0f}'
          f'{sum(CD_R["melaminico"][1]["chapas"].values()):>14.0f}')
    print(f'\n  LACA ........ {br1(CD_R["laca"][1]["laca_m2"])} m² de laca: a frente do roupeiro '
          f'({br1(FRENTE_M2)} m²)')
    print('                mais as duas faces e o canto das cinco prateleiras.')
    print('                ⛔ As portas e a caixaria FICAM — é pintura no lugar.')
    print('  MELAMÍNICO .. portas novas (as quatro, a frente inteira) e as')
    print('                prateleiras em melamínico. ⛔ A CAIXARIA DO ROUPEIRO')
    print('                FICA ONDE ESTÁ: não é móvel novo.')

    print(f'\n{"═"*W}')
    print('⛔⛔ O QUE O FATOR DE 1/3 FAZ COM A LINHA DAS PRATELEIRAS')
    print(f'{"═"*W}')
    print('  O total não mudou — mudou onde o valor aparece. Mas a linha')
    print('  das prateleiras passou a ser vendida ABAIXO DO CUSTO DIRETO:')
    print(f'\n  {"":<34}{"laca":>12}{"melamínico":>14}')
    for rot, d in (('custo direto das prateleiras', lambda v: CD_P[v][0]),
                   ('preço pela MC de 40%',         lambda v: PV_P0[v]),
                   ('preço agora, a 1/3',           lambda v: PV_P[v])):
        print(f'  {rot:<34}{br(d("laca")):>12}{br(d("melaminico")):>14}')
    for v, lab in (('laca','laca'), ('melaminico','melamínico')):
        mc = (BASE - CD_P[v][0]/PV_P[v])*100
        print(f'  MC da linha em {lab:<19}{mc:>11.0f}%' if v=='laca'
              else f'  MC da linha em {lab:<19}{"":>12}{mc:>13.0f}%')
    print()
    print('  ⭐ Como o TOTAL é o mesmo, a MARGEM DO TRABALHO não muda: o que')
    print(f'     sai das prateleiras entra no roupeiro, que vai a '
          f'R$ {br(PV_R["laca"])} / R$ {br(PV_R["melaminico"])}.')
    print('  ⛔ O RISCO É SE A CLIENTE COMPRAR SÓ AS PRATELEIRAS. Nesse')
    print('     recorte a casa vende abaixo do custo. Se houver chance de')
    print('     fatiar o pedido, a linha precisa de piso.')

    print(f'\n{"═"*W}')
    print('⚠ E UM ERRO MEU QUE ISSO EXPÔS — a laca das prateleiras')
    print(f'{"═"*W}')
    _conv = QUAD_N*QUAD_M2*LACA_M2
    _hoje = CD_P['laca'][1]['laca']
    print(f'  Lancei a laca das prateleiras pelas DUAS FACES: '
          f'{br1(CD_P["laca"][1]["laca_m2"])} m² = R$ {br(_hoje)}.')
    print(f'  A convenção da casa é "m² EM PEÇA LISA" — a peça entra UMA')
    print(f'  vez, com o verso junto: {br1(QUAD_N*QUAD_M2)} m² = R$ {br(_conv)}.')
    print(f'  ⛔ São R$ {br(_hoje-_conv)} de custo a mais que eu pus. Não corrigi')
    print('     porque corrigir muda o TOTAL, e o Jonathan pediu para não')
    print('     mudar. ★ Fica para decisão: se corrigir, o total cai.')

    print(f'\n{"═"*W}')
    print('⛔⛔ PINTAR A FRENTE CUSTA MAIS QUE TROCAR AS PORTAS')
    print(f'{"═"*W}')
    _lf = FRENTE_M2*LACA_M2
    _pn = CD_R['melaminico'][1]['custo_ch'] - CD_R['laca'][1]['custo_ch'] \
          + (CD_R['melaminico'][1]['fer'] - CD_R['laca'][1]['fer'])
    print(f'  lacar a frente do roupeiro ({br1(FRENTE_M2)} m² a R$ {br(LACA_M2)}) .. R$ {br(_lf)}')
    print(f'  fazer as quatro portas novas (sem ferragem) ...... R$ {br(_pn)}')
    print(f'  ⭐ A PORTA NOVA CUSTA {_pn/_lf*100:.0f}% DO QUE CUSTA PINTAR A VELHA.')
    print()
    print('  É o mesmo que o Jonathan viu no roupeiro completo: a R$ 650/m²,')
    print('  a laca é cara demais para competir com chapa. E a porta nova')
    print('  resolve o que a pintura não resolve — borda nova e dez anos')
    print('  de garantia sobre uma peça que é nossa.')
    print(f'\n  No total: R$ {br(TOT["laca"])} contra R$ {br(TOT["melaminico"])} — '
          f'R$ {br(TOT["laca"]-TOT["melaminico"])} de diferença.')

    print(f'\n{"═"*W}')
    print('TETO DE CUSTO DOS ITENS FECHADOS')
    print(f'{"═"*W}')
    print('  Vieram pelo preço, então o que se audita é o custo que cabem:')
    print(f'  {"":<30}{"venda":>10}{"a 40%":>10}{"a 35%":>10}{"equilíbrio":>12}')
    for n, p, _ in FECHADOS:
        print(f'  {n:<30}{br(p):>10}{br(p*(BASE-0.40)):>10}'
              f'{br(p*(BASE-0.35)):>10}{br(p*BASE):>12}')
    print('\n  ⚠ A CAMA leva palha indiana a R$ 950/m² INSTALADA. Em 1,60 m²')
    print('    (as duas laterais) são R$ 1.520 — ou seja, a palha sozinha come')
    print(f'    {1520/(5900*(BASE-0.40))*100:.0f}% do teto de custo da cama a 40% de MC.')
    print('    ⛔ Se a palha pegar também a cabeceira, não fecha em R$ 5.900.')
    print('  ⚠ A MESA ganhou AJUSTE DE ALTURA — mecanismo que não estava no')
    print('    projeto nem no preço anterior. ★ Confirmar o sistema e o custo.')
