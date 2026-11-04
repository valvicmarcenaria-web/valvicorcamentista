# -*- coding: utf-8 -*-
"""JAIRO — três camas  [07/10/2026]

⛔ NÃO É MOTOR DE CUSTO. O preço veio fechado do Jonathan (R$ 8.500 pelas
   três). Sem quantitativo não se calcula MC — o que se calcula é o TETO DE
   CUSTO que esse preço suporta, e o que cada forma de pagamento devolve
   à casa. É o mesmo tratamento das divisórias da United.

CONTEXTO
  Jairo Samuel, cliente com marcenaria em andamento (ver
  `2026-jairo-samuel-marcenaria.md`). RT 10% da Jéssica Sollero vale no
  projeto — aqui foi mantido, e o quadro mostra os dois cenários.

ESCOPO [Jonathan 07/10] — três camas: queen, viúva e solteiro
  · estrutura em MDF melamínico Carvalho Hanover de 30 mm
  · estrado em metalon 30 × 20, pintura eletrostática
  · apoios frontais tubulares de aço, base com tampa plástica e feltro
  · sapatas reguláveis, afastador do chão de 15 mm
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br2 = lambda v: f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')

TOTAL  = 8500.0
PRAZO  = '60 dias corridos'
I      = 0.012                       # 1,2% a.m. — a taxa da própria casa
TX_PP  = M.CARTAO_PP                 # 1,2% por parcela

BASE_RT  = M.base(parcelas=0, rt=True,  vendedor=False)   # 76,52%
BASE_SRT = M.base(parcelas=0, rt=False, vendedor=False)   # 85,35%

# ── a escada padrão da casa ───────────────────────────────────────────────
# ⭐ copiada da própria proposta do Jairo (`proposta-jairo-samuel.html`),
#   para não inventar um padrão que a casa não usa.
#   (rótulo, desconto, entrada, nº de parcelas no cartão, dia do saldo)
#   parcelas = 0 → o saldo vem por transferência, no dia indicado.
PADRAO = [
    ('30% de entrada + 10× no cartão',            0.00, 0.30, 10, None),
    ('50% de entrada + 8× no cartão',             0.03, 0.50,  8, None),
    ('70% de entrada + 6× no cartão',             0.05, 0.70,  6, None),
    ('70% de entrada + saldo por transferência',  0.07, 0.70,  0, 60),
]
# ⭐ [Jonathan 07/10] "desconto especial para pagamento à vista (60% + 40%)
#   de 10%" — fora da escada padrão, que para em 7%.
ESPECIAL = ('60% na assinatura + 40% na entrega', 0.10, 0.60, 0, 60)

def perfil(desc, ent, nparc, dia):
    """(o que o cliente paga, o que a casa recebe, valor presente)."""
    bruto = TOTAL*(1 - desc)
    e, saldo = bruto*ent, bruto*(1 - ent)
    if nparc:                                   # saldo no cartão
        parc  = saldo/nparc
        taxa  = saldo*TX_PP*nparc
        fluxo = [(0, e)] + [(30*k, parc*(1 - TX_PP*nparc))
                            for k in range(1, nparc + 1)]
    else:                                       # saldo por transferência
        taxa  = 0.0
        fluxo = [(0, e), (dia, saldo)]
    vp = sum(v/(1 + I)**(d/30) for d, v in fluxo)
    return bruto, bruto - taxa, vp

LINHAS = [(rot,) + perfil(d, e, n, dia) + (d, e, n, dia)
          for rot, d, e, n, dia in PADRAO + [ESPECIAL]]

if __name__ == '__main__':
    W = 84
    print('═'*W); print('JAIRO — três camas: queen, viúva e solteiro'); print('═'*W)
    print(f'\n  Investimento total ............... R$ {br(TOTAL)}')
    print(f'  Prazo ............................ {PRAZO}')

    print(f'\n{"═"*W}')
    print('AS FORMAS DE PAGAMENTO — o que cada uma devolve à casa')
    print(f'{"═"*W}')
    print(f'  {"":<40}{"cliente":>9}{"líquido":>9}{"VP":>9}{"vs melhor":>11}')
    melhor = max(x[3] for x in LINHAS)
    for rot, cli, liq, vp, *_ in LINHAS:
        est = ' ⭐' if rot.startswith('60%') else ''
        print(f'  {rot:<40}{br(cli):>9}{br(liq):>9}{br(vp):>9}'
              f'{vp-melhor:>+11.0f}{est}')

    _, _, liq_esp, vp_esp, *_ = (x for x in LINHAS if x[0].startswith('60%')).__next__()
    esp = [x for x in LINHAS if x[0].startswith('60%')][0]
    t7  = [x for x in LINHAS if x[0].startswith('70% de entrada + saldo')][0]
    c30 = [x for x in LINHAS if x[0].startswith('30%')][0]

    print(f'\n  ⛔ O DESCONTO ESPECIAL DE 10% É O PIOR NEGÓCIO DA MESA.')
    print(f'    Líquido: R$ {br(esp[2])} contra R$ {br(t7[2])} da opção de 7%')
    print(f'    e R$ {br(c30[2])} do cartão em 10× — que não tem desconto nenhum')
    print(f'    e ainda assim deixa R$ {br2(c30[2]-esp[2])} a mais, já paga a taxa.')
    print(f'    Em valor presente são R$ {br2(t7[3]-esp[3])} a menos que os 7%.')

    print(f'\n  ⛔ E ELE MATA A LINHA DE 7%. O especial pede MENOS entrada')
    print('    (60 contra 70) e dá MAIS desconto (10 contra 7): ninguém com')
    print('    calculadora escolhe a de 7% se as duas aparecerem juntas.')
    print('    Ou a de 7% sai do quadro, ou o especial vira carta de manga —')
    print('    oferecido no fechamento, não impresso ao lado dela.')

    print(f'\n{"═"*W}')
    print('TETO DE CUSTO — o que o preço suporta, já que não há quantitativo')
    print(f'{"═"*W}')
    print('  Sem levantamento não há MC. Há o teto que cada preço aguenta:')
    for rot, base in (('com RT de 10% (como no projeto do Jairo)', BASE_RT),
                      ('sem RT', BASE_SRT)):
        print(f'\n  {rot}   (base {base*100:.2f}%)')
        print(f'    {"":<30}{"a 8.500":>12}{"a 7.650 (−10%)":>18}')
        for lab, m in (('segurando a MC ideal de 40%', 0.40),
                       ('na MC padrão da casa, 38%',   0.38),
                       ('no PISO da casa, 35%',        0.35),
                       ('ponto de equilíbrio',         0.00)):
            print(f'    {lab:<30}{br(TOTAL*(base-m)):>12}'
                  f'{br(TOTAL*0.90*(base-m)):>18}')

    teto = TOTAL*0.90*(BASE_RT - 0.35)
    print(f'\n  ⚠ COM RT E COM O DESCONTO, o teto no piso da casa é')
    print(f'    R$ {br(teto)} — pelas TRÊS camas, R$ {br(teto/3)} cada.')
    print('    Dentro disso têm de caber:')
    print('      · ~12 m² de melamínico Carvalho Hanover (o painel de 30 mm')
    print('        é construído: melamínico vem em 15/18/25, não em 30)')
    print('      · ~34 m de metalon 30×20 SOLDADO e com pintura eletrostática')
    print('      · os apoios tubulares de aço, com tampa plástica e feltro')
    print('      · as sapatas reguláveis')
    print('    ⛔ Metade disso é SERRALHERIA, que é hora de terceiro e não')
    print('       cai com volume. É o item a conferir antes de assinar.')
