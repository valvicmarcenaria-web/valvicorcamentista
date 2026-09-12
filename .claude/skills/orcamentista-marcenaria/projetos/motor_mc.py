# -*- coding: utf-8 -*-
"""MODELO DE CUSTO E MARGEM DE CONTRIBUIÇÃO DA VALVIC — fonte única.

⛔ NENHUM motor redefine coeficiente de encargo. Todos importam daqui.
   Antes de 12/09/2026 cada `corte-*.py` carregava a sua cópia de
   `A_, LIQF_, B_` e as três não batiam entre si nem com a planilha.

Método cravado pelo Jonathan em 12/09/2026 — ver
`referencias/modelo-de-custo.md` para a íntegra e as decisões de base.

A CASCATA, sobre o PREÇO DE VENDA (bruto):

  1. sobre o BRUTO, direto
       nota fiscal ................................... 5,0%
       taxa de máquina de cartão ..... 1,2% × nº de parcelas  (só se houver cartão)
       margem de erro ................................ 2,0%
       desgaste de serra e fresa ..................... 0,5%
       manutenção de máquinas ........................ 0,5%

  2. LÍQUIDO = bruto − nota fiscal − taxa de cartão
       RT ................................. 10% do líquido  (quando aplicável)
       comissão de vendedor ............... 10% do líquido  (quando aplicável)

  3. LÍQUIDO 2 = líquido − RT − comissão de vendedor
       comissões de produção .............. 7% do líquido 2
         coordenação 1,0 · programação 1,0 · fabricação 2,5 · montagem 2,5

  BASE = 1 − (soma de tudo acima, como fração do preço)
  PREÇO para uma MC alvo  =  custo_direto / (BASE − MC)
  MC conferida            =  BASE − custo_direto / preço
"""

NF        = 0.05      # nota fiscal, sobre o bruto
CARTAO_PP = 0.012     # taxa de máquina POR PARCELA, sobre o valor total
ERRO      = 0.02      # margem de erro, sobre o bruto
SERRA     = 0.005     # desgaste de serra e fresa, sobre o bruto
MANUT     = 0.005     # manutenção de máquinas, sobre o bruto
RT        = 0.10      # sobre o líquido (bruto − NF − cartão)
VENDEDOR  = 0.10      # sobre o líquido, mesma base do RT
PRODUCAO  = dict(coordenacao=0.010, programacao=0.010,
                 fabricacao=0.025, montagem=0.025)   # sobre o líquido 2
PROD      = sum(PRODUCAO.values())                   # 7,0%
EMBALAGEM = 0.02      # sobre o CUSTO DIRETO do projeto, não sobre o preço

MC_PISO, MC_IDEAL = 0.35, (0.35, 0.40)


def encargos(parcelas=0, rt=True, vendedor=True):
    """Encargos percentuais sobre o preço, abertos linha a linha."""
    cartao = CARTAO_PP * parcelas
    liq    = 1 - NF - cartao                   # base do RT e do vendedor
    e_rt   = liq * RT       if rt       else 0.0
    e_vend = liq * VENDEDOR if vendedor else 0.0
    liq2   = liq - e_rt - e_vend               # base das comissões de produção
    d = {'nota fiscal': NF, 'taxa de cartão': cartao, 'margem de erro': ERRO,
         'desgaste de serra': SERRA, 'manutenção de máquinas': MANUT,
         'RT': e_rt, 'comissão de vendedor': e_vend}
    for k, v in PRODUCAO.items():
        d[f'produção · {k}'] = liq2 * v
    return d


def base(parcelas=0, rt=True, vendedor=True):
    """Fração do preço que sobra para custo direto + MC."""
    return 1 - sum(encargos(parcelas, rt, vendedor).values())


def preco(custo_direto, mc, parcelas=0, rt=True, vendedor=True):
    """Preço que entrega a MC alvo, arredondado à centena."""
    d = base(parcelas, rt, vendedor) - mc
    if d <= 0:
        raise ValueError(f'MC de {mc:.1%} não cabe: a base é {d+mc:.5f}')
    return round(custo_direto/d/100)*100


def mc(preco_venda, custo_direto, parcelas=0, rt=True, vendedor=True):
    """MC conferida de um preço já fechado."""
    return base(parcelas, rt, vendedor) - custo_direto/preco_venda


def com_embalagem(custo_sem_embalagem):
    """Embalagem = 2% do custo direto, SOMADA ao resto.

    [Jonathan 12/09] Ela NÃO substitui os consumíveis. Consumível é cola,
    parafuso, limpeza e acabamento aplicados NO móvel (os motores usam 6% de
    chapa + fita); embalagem é caixa e plástico para TRANSPORTAR o móvel. As
    duas linhas convivem no custo direto.
    """
    return custo_sem_embalagem * (1 + EMBALAGEM)


if __name__ == '__main__':
    W = 92
    def brl(v, n=2): return f'{v:,.{n}f}'.replace(',', '§').replace('.', ',').replace('§', '.')
    print('═'*W); print('MODELO DE CUSTO VALVIC — encargos como % do preço de venda'); print('═'*W)
    CEN = (('à vista · com RT e vendedor',    dict()),
           ('à vista · sem RT',               dict(rt=False)),
           ('à vista · sem RT e sem vendedor',dict(rt=False, vendedor=False)),
           ('cartão 6× · com RT e vendedor',  dict(parcelas=6)),
           ('cartão 10× · com RT e vendedor', dict(parcelas=10)),
           ('cartão 10× · sem RT',            dict(parcelas=10, rt=False)))
    linhas = list(encargos())
    print(f'  {"encargo":<26}' + ''.join(f'{n.split(" · ")[0][:9]:>11}' for n, _ in CEN))
    for L in linhas:
        print(f'  {L:<26}' + ''.join(f'{encargos(**k)[L]*100:>10.2f}%' for _, k in CEN))
    print('  ' + '-'*(26+11*len(CEN)))
    print(f'  {"TOTAL DE ENCARGOS":<26}' + ''.join(f'{sum(encargos(**k).values())*100:>10.2f}%' for _, k in CEN))
    print(f'  {"BASE (custo + MC)":<26}' + ''.join(f'{base(**k)*100:>10.2f}%' for _, k in CEN))
    print(f'  {"MC máxima possível":<26}' + ''.join(f'{base(**k)*100:>10.2f}%' for _, k in CEN))
    print(f'\n  Piso da casa: MC {MC_PISO:.0%} · faixa ideal {MC_IDEAL[0]:.0%}–{MC_IDEAL[1]:.0%}')
    print(f'\n  ⚠ Com cartão em 10× a base cai de {base()*100:.2f}% para '
          f'{base(parcelas=10)*100:.2f}% — {(base()-base(parcelas=10))*100:.1f} pontos.')
    print(f'    Preço de tabela com cartão NÃO é o mesmo preço de tabela à vista.')
    print('═'*W)
