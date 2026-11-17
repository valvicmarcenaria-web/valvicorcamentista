# -*- coding: utf-8 -*-
"""JPC — de onde vem a MC de 17,8%, e o que a mudaria.

⭐⭐ A PERGUNTA QUE ESTE ARQUIVO RESPONDE: R$ 6.700 em dois gabinetes de
  banheiro dá 17,8% de margem de contribuição, contra um piso de 35% e uma
  faixa ideal de 35% a 40% na casa. Antes de dizer isso ao Jonathan eu
  precisava saber SE O NÚMERO É DO PREÇO OU DO TAMANHO DO JOB.

  É do tamanho. Dois móveis compram 4 chapas inteiras para usar 7,13 m²
  de peça — sobra que não some, fica no galpão e entra no próximo job da
  mesma cor. Este arquivo põe os dois mundos lado a lado.
"""
import importlib.util, pathlib

_aqui = pathlib.Path(__file__).resolve().parent
def _mod(nome, arq):
    sp = importlib.util.spec_from_file_location(nome, _aqui / arq)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m

b = _mod('jpc_base', 'base.py')
lv = _mod('jpc_lv', 'levantamento.py')

CEN = [('Como a casa compra · chapa inteira', True),
       ('Se a sobra for usada · chapa fracionada', False)]

print(f'\n  APARTAMENTO JPC · o que mexe na margem de R$ {b.PRECO_FECHADO:,.0f}\n'
      .replace(',', '.'))
print(f'  {"CENÁRIO":<42}{"CHAPA":>11}{"CUSTO":>12}{"MC":>9}'
      f'{"PREÇO A 35%":>14}')
print('  ' + '─' * 88)
for rot, arr in CEN:
    T = lv.custo(lv.M, arredonda=arr)
    d = T['direto']
    mc = b.BASE - d / b.PRECO_FECHADO
    p35 = d / (b.BASE - 0.35)
    print(f'  {rot:<42}{lv.brl(T["c_chapa"]):>11}{lv.brl(d):>12}'
          f'{mc*100:>8.1f}%{lv.brl(p35):>14}')

T1 = lv.custo(lv.M, True); T0 = lv.custo(lv.M, False)
dif = T1['direto'] - T0['direto']
print('  ' + '─' * 88)
print(f'  {"a sobra do arredondamento, com consumível e embalagem":<42}'
      f'{lv.brl(dif):>23}')
print(f'  {"quanto ela pesa no custo direto":<42}'
      f'{dif / T1["direto"] * 100:>22.1f}%')

print('\n  ── e a pergunta do preço ' + '─' * 60)
for rot, mc in [('piso da casa', 0.35), ('faixa ideal, meio', 0.375),
                ('teto da faixa ideal', 0.40)]:
    print(f'     {("preço a MC de %.1f%% · " % (mc*100)) + rot:<44}'
          f'{lv.brl(T1["direto"] / (b.BASE - mc)):>26}')
print(f'     {"preço fechado pelo Jonathan":<44}'
      f'{lv.brl(b.PRECO_FECHADO):>26}')
print(f'     {"MC que ele compra":<44}'
      f'{(b.BASE - T1["direto"] / b.PRECO_FECHADO)*100:>25.2f}%')

#   ⚠ E O RT, que é leitura minha e não ordem do Jonathan — ver base.py.
sem = b.cascata() - T1['direto'] / b.PRECO_FECHADO
print(f'\n     {"a mesma MC se NÃO houver RT para a arquiteta":<44}'
      f'{sem*100:>25.2f}%')
print(f'     {"o que o RT de 10% custa neste job":<44}'
      f'{lv.brl((sem - (b.BASE - T1["direto"]/b.PRECO_FECHADO)) * b.PRECO_FECHADO):>26}')
