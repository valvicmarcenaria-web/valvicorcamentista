# -*- coding: utf-8 -*-
"""ANDREA · ADITIVO — A ESTRUTURA DE SUBSÍDIO TÉCNICO  [26/10/2026]

⭐ [Paula Galante → Jonathan, 26/10 15:50] a parceira mandou a estrutura:

     01  Execução de Marcenaria sob medida ................  R$ 16.500,00
     02  Subsídio Técnico (Adequação de Custo
         à Homologação do Projeto) ....................... − R$ 10.560,00
         VALOR LÍQUIDO A PAGAR PELO CLIENTE .............   R$  5.940,00

⭐ [Jonathan → Paula, 15:29] "sinalizo que vc esta pagando o valor ou faço
   somente o abatimento apresentando o novo valor?"
⭐ [Paula, 16:05] "Quero sim que a cliente saiba o quanto lamentei por este
   inconveniente e que estou arcando com parte do valor"

⛔⛔ O QUE ESTE ARQUIVO EXISTE PARA DIZER: **a receita da Valvic não muda,
   mas a GARANTIA dela muda inteira.** Antes, R$ 16.500 eram devidos por
   uma contratante dentro de um contrato assinado. Depois do subsídio,
   R$ 10.560 — 64% do aditivo — passam a ser devidos por um TERCEIRO que
   não assina esta folha. O documento só registra o abatimento.

   Se o subsídio não for liquidado, a Valvic não tem como cobrá-lo: a folha
   que ela mesma emitiu diz que a contratante deve R$ 5.940.

★ O preço não se mexe. Este arquivo NÃO recalcula preço — mede exposição.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location('an', P/'corte-andrea-aditivo.py')
an = importlib.util.module_from_spec(_s); sys.modules['an'] = an
_s.loader.exec_module(an)
M = an.M

_m  = lambda v: f'{abs(v):,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')
brc = lambda v: ('− ' if v < 0 else '') + _m(v)   # ⭐ o sinal aparece
br  = lambda v: f'{v:,.0f}'.replace(',', '.')
vg  = lambda v, n=1: f'{v:.{n}f}'.replace('.', ',')

# ── a estrutura da Paula ────────────────────────────────────────────────
EXECUCAO  = an.PV            # 16.500 — ⭐ o preço do Jonathan, intocado
SUBSIDIO  = 10560.00         # ⭐ [Paula 26/10] o que ela absorve
LIQUIDO   = EXECUCAO - SUBSIDIO

# ⛔⛔ TRAVAS
assert EXECUCAO == 16500.00, '⛔ O INVESTIMENTO NÃO É MAIS O DO JONATHAN'
assert LIQUIDO == 5940.00,   '⛔ A CONTA DA PAULA NÃO FECHA EM 5.940'
assert 0 < SUBSIDIO < EXECUCAO, '⛔ O SUBSÍDIO SAIU DA FAIXA'

CD   = an.custo(an.A_PISO)['cd']          # custo direto no ponto de piso
BASE = an.BASE

contrib = lambda receb: receb*BASE - CD   # o que sobra para custo fixo + lucro

if __name__ == '__main__':
    W = 78
    L = lambda r, v, s='': print(f'  {r:<46}{("− " if v<0 else "")}R$ {_m(v):>10}{s}')
    print('═'*W); print('ANDREA · ADITIVO — ESTRUTURA DE SUBSÍDIO TÉCNICO')
    print(f'base {BASE*100:.2f}% (sem RT, sem vendedor) · custo direto no piso '
          f'R$ {br(CD)}'); print('═'*W)

    print('\nA FOLHA, COMO A PAULA DESENHOU')
    print('─'*W)
    L('01 · execução de marcenaria sob medida', EXECUCAO)
    L('02 · subsídio técnico', -SUBSIDIO, '  ⭐ a parceira absorve')
    print('  ' + '─'*58)
    L('VALOR LÍQUIDO A PAGAR PELA CONTRATANTE', LIQUIDO)
    print(f'\n  o subsídio é {SUBSIDIO/EXECUCAO:.0%} do aditivo. '
          f'a contratante paga {LIQUIDO/EXECUCAO:.0%}.')

    print(f'\n{"═"*W}'); print('1 · A RECEITA DA VALVIC NÃO MUDA')
    print('═'*W)
    L('da contratante', LIQUIDO)
    L('da designer, via subsídio', SUBSIDIO)
    print('  ' + '─'*58)
    L('TOTAL A RECEBER', LIQUIDO+SUBSIDIO, '  = o preço do Jonathan')
    print(f'\n  MC {an.mc(an.A_PISO)*100:.1f}% · contribuição R$ {br(contrib(EXECUCAO))} '
          f'— idêntico ao cenário anterior.')
    print('  ⭐ o que muda não é quanto entra: é DE QUEM, e com que garantia.')

    print(f'\n{"═"*W}')
    print('2 · ⛔⛔ A EXPOSIÇÃO — SE O SUBSÍDIO NÃO FOR LIQUIDADO')
    print('═'*W)
    L('recebido (só a contratante)', LIQUIDO)
    L('custo direto do aditivo', -CD)
    print('  ' + '─'*58)
    L('CONTRIBUIÇÃO', contrib(LIQUIDO), '  ⛔ prejuízo')
    print(f'  {"MC":<46}{(BASE - CD/LIQUIDO)*100:>11.1f}%')
    print(f'\n  ⭐⭐ A OSCILAÇÃO: de +R$ {br(contrib(EXECUCAO))} para '
          f'R$ {br(contrib(LIQUIDO))} — um giro de')
    print(f'    R$ {br(contrib(EXECUCAO)-contrib(LIQUIDO))} dependendo de um '
          f'combinado que não está nesta folha.')
    print(f'  ⚠ A folha que a Valvic emite diz, por escrito, que a contratante')
    print(f'    deve R$ {brc(LIQUIDO)}. Nada nela torna ninguém devedor dos')
    print(f'    R$ {brc(SUBSIDIO)} restantes.')
    print('  ⭐ O CONSERTO É UMA LINHA DE TEXTO, não uma renegociação: dizer na')
    print('    própria folha QUEM concede o subsídio e que ele é liquidado')
    print('    direto junto à Valvic. Vira crédito contra terceiro, não')
    print('    desconto concedido. E é exatamente o que a Paula pediu —')
    print('    ela QUER que a cliente saiba que está arcando.')

    print(f'\n{"═"*W}')
    print('3 · ⛔ O "SEM VISAR LUCRO" — O QUE A CONTA PERMITE DIZER')
    print('═'*W)
    print('  ⭐ [Paula 16:05] "acho que vc deveria colocar o que você me disse')
    print('    que está colocando apenas o custo sem visar lucro"')
    print(f'\n  ⛔ A R$ {br(EXECUCAO)} isso NÃO É VERDADE na faixa provável de área:')
    print(f'  {"área de face":>14}{"MC":>10}   leitura')
    print('  ' + '─'*56)
    for a, rot in ((an.A_40,'topo da faixa ideal'), (an.A_PISO,'piso da casa'),
                   (20.0,'—'), (an.A_ZERO,'⛔ aqui sim: MC zero')):
        print(f'  {vg(a):>11} m²{an.mc(a)*100:>9.1f}%   {rot}')
    print(f'\n  ⭐⭐ O QUE É VERDADE E DIZ QUASE O MESMO: este aditivo foi orçado')
    print('    SEM RT e SEM comissão de vendedor, porque é adequação dentro de')
    print('    um contrato que já corre. Isso é desconto real e verificável:')
    b_avulso = M.base(parcelas=0, rt=True, vendedor=True)
    pv_avulso = CD/(b_avulso - an.MC_PISO)
    L('como serviço avulso, no piso da casa', pv_avulso)
    L('como adequação de contrato em curso', EXECUCAO, '  ⭐ praticado')
    print('  ' + '─'*58)
    L('diferença', pv_avulso-EXECUCAO,
      f'  −{(pv_avulso-EXECUCAO)/pv_avulso:.0%}')
    print(f'\n    base avulsa {b_avulso*100:.2f}% → base de adequação '
          f'{BASE*100:.2f}%: {(BASE-b_avulso)*100:.1f} pontos')
    print('    que a casa deixa na mesa por ser obra em andamento.')
    print('  ⭐ Dá para escrever "condição especial de adequação, sem o')
    print('    acréscimo aplicado a serviço avulso" — verdadeiro, auditável, e')
    print(f'    vale {(pv_avulso-EXECUCAO)/pv_avulso:.0%} de abatimento. '
          'Já "apenas o custo" é frase que a')
    print('    primeira cotação de concorrente desmonta, e vira precedente')
    print('    para a próxima adequação.')
