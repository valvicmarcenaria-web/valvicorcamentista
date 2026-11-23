# -*- coding: utf-8 -*-
"""CENTURION MOTORS — a linha do ambiente no Painel, e os rótulos do bloco.

⛔⛔ O ERRO QUE ESTE ARQUIVO EXISTE PARA NÃO REPETIR: eu renomeei as colunas
  do quadro de ambientes (FITA → "FITA, SARRAFO E LED", FERRAGEM → "ALMA DE
  AÇO", FRETE → "LACA E FONTES") e deixei os rótulos do bloco ONDE ESTÁ O
  DINHEIRO como estavam no MODELO. Cada linha do bloco passou a mostrar o
  número da coluna SEGUINTE: "Frete do projeto" exibia R$ 9.953,57 e
  chamava isso de "49,76785 viagens". ⭐ É o mesmo erro que o Jonathan pegou
  no Painel da Sala em 19/11/2026 — RÓTULO E FÓRMULA SE ESCREVEM NA MESMA
  PASSADA, porque nada quebra e tudo continua somando.

⭐ O que é FÓRMULA no Painel (não se grava, se deixa em paz):
     G14..G19   = SUM da coluna F..K do quadro de ambientes
     H14..H19   = % do custo
     I14..I19   = REPT("█"; ...) · a barra de proporção
     J24        = ROUND(K24 − F24 − G24 − H24 − I24; 2)
     K44, F44…  = SUM das linhas 24:43
  ⭐ Logo a soma das colunas SEMPRE fecha com o custo direto, por
    construção: J é o resto. Basta gravar F, G, H, I e K certos.
"""
import importlib.util, pathlib

AQUI = pathlib.Path(__file__).resolve().parent


def _mod(n, a):
    sp = importlib.util.spec_from_file_location(n, AQUI / a)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


b = _mod('cent_base', 'base.py')
lv = _mod('cent_lv', 'levantamento.py')

PLANILHA = '1viDAEugwv4IJgML4v0JJOpusjIkEQP8VyO2HzScwLRw'
T = lv.T

#   ── a alma de aço sai dos serviços e vai para a sua própria coluna ──
ALMA = sum(x['qtd'] * x['unit'] for it in lv.ITENS for x in it.serv
           if 'Alma de aço' in x['nome'])

COLUNAS = dict(
    #   F · a chapa inteira, em número cheio
    mdf=T['c_chapa'],
    #   G · tudo que se compra por metro: fita, filetagem e LED
    #   ⛔ O SARRAFO SAIU DAQUI em 23/11/2026 — "nao usamos sarrafo de
    #     pinus" — e a estruturação virou CHAPA, logo migrou para a coluna
    #     F. Esta coluna perdeu R$ 4.260,59 e o rótulo teve de mudar junto.
    fita=T['c_fita'] + T['c_filete'] + T['c_lin'],
    #   H · a alma de aço, sozinha, porque é ela que a prateleira pede
    alma=ALMA,
    #   I · o que é serviço ou avulso: laca, fonte, espelho e frete
    laca=T['c_serv'] - ALMA,
    #   K · o custo direto do ambiente · J se deduz dele
    direto=T['direto'],
)

#   ⭐ OS RÓTULOS, casando com o que cada coluna CARREGA DE FATO
ROTULOS = [
    'Chapa — MDF, compensado flexível e a tira de estrutura, em número cheio',
    'Fita, filetagem e LED — o que se compra por metro',
    'Alma de aço — uma barra por prateleira, contra empeno',
    'Laca, espelho e avulsos — o que é serviço de terceiro',
    'Corte, consumíveis e embalagem',
]
CAB = ['AMBIENTE', 'PRANCHAS', 'ITENS', 'CHAPAS', 'CHAPA',
       'FITA, FILETAGEM E LED', 'ALMA DE AÇO', 'LACA, ESPELHO E AVULSOS',
       'CORTE E CONSUM.', 'CUSTO DIRETO']

LINHA_AMB = ['01 Showroom · Centurion',
             '554_Centurion ADESIVO ESPELHO E TINTA 01 e 02 · CLS, rev. 00 '
             'de 17/11/2025',
             len(lv.ITENS), T['n_ch'],
             round(COLUNAS['mdf'], 2), round(COLUNAS['fita'], 2),
             round(COLUNAS['alma'], 2), round(COLUNAS['laca'], 2)]


def _br(v, casas=2):
    t = ('%0.*f' % (casas, v)).replace('.', ',')
    i, _, d = t.partition(',')
    out = ''
    while len(i) > 3:
        out, i = '.' + i[-3:] + out, i[:-3]
    return i + out + (',' + d if d else '')


if __name__ == '__main__':
    print('\n  A LINHA DO AMBIENTE  ' + '─' * 50)
    for rot, k in [('F · Chapa', 'mdf'), ('G · Fita, filetagem e LED', 'fita'),
                   ('H · Alma de aço', 'alma'),
                   ('I · Laca, espelho e avulsos', 'laca')]:
        print('  %-32s %14s' % (rot, _br(COLUNAS[k])))
    resto = (COLUNAS['direto'] - COLUNAS['mdf'] - COLUNAS['fita']
             - COLUNAS['alma'] - COLUNAS['laca'])
    print('  %-32s %14s   ⭐ fórmula J24' % ('J · Corte, consum. e embal.',
                                             _br(resto)))
    print('  %-32s %14s' % ('K · CUSTO DIRETO', _br(COLUNAS['direto'])))
    print('  %-32s %14s   (corte %s + consum %s + embal %s)'
          % ('  conferência do resto', _br(resto - T['c_corte'] - T['c_cons']
                                           - T['c_emb']),
             _br(T['c_corte']), _br(T['c_cons']), _br(T['c_emb'])))
    print('\n  %d itens · %d chapas' % (len(lv.ITENS), T['n_ch']))
    print('\n  O PREÇO  ' + '─' * 50)
    p = b.preco(T['direto'])
    print('  MC aplicada %.0f%% = alvo %.0f%% + %s (20 pontos)'
          % (b.MC * 100, b.MC_ALVO * 100, b.DIFICULDADE))
    print('  %-32s %14s' % ('PREÇO DE VENDA', _br(p)))
    print('  %-32s %14s' % ('margem de contribuição', _br(p * b.MC)))
