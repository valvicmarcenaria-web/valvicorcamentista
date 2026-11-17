# -*- coding: utf-8 -*-
"""PAINEL DA SALA — o que cada decisão custa, em reais.

⭐ Três perguntas que o levantamento sozinho não responde:
   1. quanto a ORDEM DO JONATHAN economizou — ripado até a pedra, e liso
      dali para a direita, contra o ripado correndo os 682 inteiros;
   2. quanto custa a dúvida do GIANDUIA TRAMA, se ele for padrão especial;
   3. onde o arredondamento de chapa cobra uma chapa inteira por 5% de área.
"""
import importlib.util, pathlib, copy

P = pathlib.Path(__file__).resolve().parent
def _mod(n, a):
    sp = importlib.util.spec_from_file_location(n, P / a)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
lv = _mod('ps_lv', 'levantamento.py'); b = lv.b
brl = lv.brl

BASE = lv.custo(lv.M)

#   ⭐⭐ O RIPADO CORRENDO OS 682: o liso vira substrato e ganha ripa em
#     cima, mais a mão de obra e a filetagem da face inteira.
_tudo = [copy.deepcopy(i) for i in lv.M]
_x = lv.Item('Ripado sobre os 330 do liso', '')
_x.ripado(lv.LISO_L, lv.ALT, 'Ripado do trecho liso')
_tudo.append(_x)
TUDO = lv.custo(_tudo)

print(f'\n  PAINEL DA SALA · VISTA 2 — O QUE CADA DECISÃO CUSTA\n')
print(f'  {"":<46}{"CUSTO DIRETO":>16}{"DIFERENÇA":>15}')
print('  ' + '─' * 77)
print(f'  {"Ripado até a pedra, liso dali (Jonathan, 17/11)":<46}'
      f'{brl(BASE["direto"]):>16}{"—":>15}')
print(f'  {"Ripado correndo os 682 inteiros":<46}'
      f'{brl(TUDO["direto"]):>16}'
      f'{"+ " + brl(TUDO["direto"] - BASE["direto"]):>15}')
print(f'\n  ⭐ A ordem economiza {brl(TUDO["direto"] - BASE["direto"])} de custo '
      f'direto: o ripado inteiro custaria '
      f'{(TUDO["direto"]/BASE["direto"]-1)*100:.0f}% a mais.')
_n = int(lv.LISO_L // b.PASSO)
print(f'     São {_n} ripas, {_n*lv.ALT/100*2:.0f} m de filete e '
      f'{lv.LISO_L*lv.ALT/10000:.2f} m² de mão de obra de painel ripado'
      f'\n     que deixam de existir.')

print(f'\n  ── a dúvida do Gianduia Trama ' + '─' * 48)
print(f'  {"MDF cor de catálogo · R$ 700 a chapa":<46}{brl(BASE["direto"]):>16}')
print(f'  {"Padrão especial da Base · R$ 1.000 a chapa":<46}'
      f'{brl(9954.24):>16}{"+ " + brl(9954.24 - BASE["direto"]):>15}')
print('  ⚠ "GIANDUIA TRAMA - DURATEX" é padrão texturizado. É a primeira\n'
      '    cotação a fazer, e ela vale 19% do custo do projeto.')

print(f'\n  ── o arredondamento da estrutura ' + '─' * 45)
_rend = b.CHAPA_M2 * b.APROV
for passo, n_m in [(60, 12), (70, 11), (75, 10), (80, 9)]:
    a = n_m * 0.08 * lv.ALT / 100 + 6 * (lv.LARG / 2 / 100) * 0.08
    ch = int(-(-a // _rend))
    print(f'  montantes a cada {passo} cm · {n_m:>2} un · {a:>4.2f} m² · '
          f'{ch} chapa(s) de Branco TX{brl(ch * 400):>12}')
print('  ⚠ A 60 cm a estrutura passa 5% do rendimento de uma chapa e compra\n'
      '    a SEGUNDA inteira. A 75 cm cabe numa só. Não mexi: afrouxar\n'
      '    montante para caber na chapa é decisão de obra, não minha.')
