# -*- coding: utf-8 -*-
"""CENTURION MOTORS — A PLANILHA COMO MOTOR, NÃO COMO RELATÓRIO.

⛔⛔ O QUE ESTE ARQUIVO CONSERTA [Jonathan, 23/11/2026]: "vc esta me
  entregando a planilha sem formulas". Estava certo, e era de fundo: eu
  calculava tudo em Python e gravava o RESULTADO. A planilha virava um
  retrato — mudar uma medida, um preço ou uma espessura não recalculava
  nada, e quem recebia não podia experimentar cenário nenhum.

⭐ A ARQUITETURA, agora:
     AS PEÇAS       são a ENTRADA. Medida, quantidade e chave do material
                    continuam geradas pelo levantamento em Python, como o
                    MODELO manda ("esta seção é GERADA, nunca digitada").
     OS PARÂMETROS  são o que se digita: folha, aproveitamento e preço de
                    cada material, mais os preços por unidade. Amarelos.
     TODO O RESTO   é FÓRMULA. Área, número de chapas, custo, percentual,
                    consumíveis, embalagem, custo do item, conferência.

⛔ E O MOTIVO PELO QUAL EU FUI PELO PYTHON, que também precisa ser dito:
  a aba "Base (importada)" tem #REF! na célula D3 — o IMPORTRANGE nunca
  foi autorizado nesta cópia, então as chaves de chapa não têm preço. ⭐ O
  Painel já avisa que "nenhum script pode dar essa autorização por nós".
  Mas isso não era desculpa: o certo era montar as fórmulas contra um
  bloco de parâmetros local, que é o que faço aqui — e que funciona com ou
  sem a Base ligada.

⛔⛔ E A LIÇÃO MAIOR: eu vinha escrevendo NÚMEROS CALCULADOS DENTRO DOS
  TEXTOS de observação ("área líquida de 22,30 m²", "4 folhas", "R$ 600").
  Cada um deles é uma mentira esperando a próxima mudança. Número vive em
  CÉLULA, com formato; texto explica o porquê, não repete a conta.
"""
import importlib.util, pathlib

AQUI = pathlib.Path(__file__).resolve().parent


def _mod(n, a):
    sp = importlib.util.spec_from_file_location(n, AQUI / a)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


b = _mod('cent_base', 'base.py')
lv = _mod('cent_lv', 'levantamento.py')
fo = _mod('cent_fmt', 'formato.py')
pl = _mod('cent_pl', 'planilha.py')

#   ── o mapa de linhas, lido da classificação e não cravado ──
L = pl.linhas()
CL = fo.classifica(L)


def faixa(classe):
    d = [i for i, c in enumerate(CL) if c == classe]
    return (min(d) + 1, max(d) + 1) if d else (0, 0)


def linha_de(prefixo):
    for i, r in enumerate(L):
        if r and str(r[0] or '').startswith(prefixo):
            return i + 1
    return 0


MAT0, MAT1 = faixa('dado1')          # as linhas de material
ITE0, ITE1 = faixa('dado2')          # as linhas de item
PEC0, PEC1 = faixa('dado4')          # as linhas de peça
DIRETO = linha_de('CUSTO DIRETO DO AMBIENTE')
TOT_ITEM = linha_de('TOTAL DO AMBIENTE')
CONFER = linha_de('⭐ CONFERÊNCIA')

#   ── o bloco de parâmetros, depois de tudo ──
PAR0 = len(L) + 3                    # a linha da seção
PAR_CAB = PAR0 + 2
PAR_M0 = PAR_CAB + 1                 # primeira linha de material
CHAVES = sorted(lv.T['chapas'])      # (padrão, espessura)
PAR_M1 = PAR_M0 + len(CHAVES) - 1
PAR_U0 = PAR_M1 + 3                  # os preços por unidade
TAB_MAT = '$B$%d:$I$%d' % (PAR_M0, PAR_M1)
COL_REND, COL_PRECO = 7, 8           # dentro de TAB_MAT

#   ⭐ os preços que não são de folha · (rótulo, unidade, valor)
UNIT = [
    ('Fita de borda de cor, 22 mm', 'm', b.FITA_22),
    ('Filetagem automática', 'm', b.FILETE_MAQ),
    ('Perda de fita', '×', b.FITA_PERDA),
    ('Laca fosca PU', 'm²', b.LACA_M2),
    ('Alma de aço · barra de 3 m', 'barra', b.ALMA_BARRA),
    ('LED COB · conjunto completo', 'm', b.LED_M),
    ('Fonte de LED', 'un', b.LED_FONTE),
    ('Espelho prata', 'm²', b.ESPELHO_M2_PRECO),
    ('Frete de espelho', 'serviço', b.ESPELHO_FRETE),
    ('Cola de contato · lata de %d kg' % b.COLA_KG, 'lata', b.COLA_LATA),
    ('Corte · por chapa', 'chapa', b.CORTE_CHAPA),
    ('Corte · por peça', 'peça', b.CORTE_PECA),
    ('Consumíveis', '%', b.CONSUMIVEIS),
    ('Embalagem', '%', b.EMBALAGEM),
]
U = {u[0]: PAR_U0 + 3 + i for i, u in enumerate(UNIT)}   # rotulo -> linha


def parametros():
    """O bloco que se digita. Tudo em cima se calcula a partir dele."""
    out = [['  OS PARÂMETROS DESTE ORÇAMENTO   ·   ⭐ É DAQUI QUE TUDO EM '
            'CIMA SE CALCULA. As células amarelas são as únicas que se '
            'digita: mude um preço, uma folha ou um aproveitamento e a '
            'planilha inteira se refaz · ⛔ a aba "Base (importada)" tem '
            '#REF! em D3 porque o IMPORTRANGE nunca foi autorizado nesta '
            'cópia, e por isso os preços moram aqui — quando ela for '
            'liberada, estas células podem virar VLOOKUP nela'], [],
           ['CHAVE DA BASE', 'DE ONDE VEM', 'FOLHA C', 'FOLHA L', 'ÁREA m²',
            'APROV.', 'RENDIM. m²', 'R$ / FOLHA']]
    ORIGEM = {
        'Compensado flexível': '⛔ não existe na Base · preço do Jonathan, '
                               '23/11/2026',
        'Fórmica': '⛔ a Base diz "a partir de R$ 400" sem dizer de que '
                   'folha · preço do Jonathan, 23/11/2026',
        'MDF Amadeirado': 'Base · MDF Melamínico Fosco, amadeirado e cor',
        'MDF Branco TX': 'Base · MDF Branco TX',
    }
    for i, k in enumerate(CHAVES):
        r = PAR_M0 + i
        c, l = b.folha(k[0])
        out.append(['%s %d' % k, ORIGEM.get(k[0], ''), c, l,
                    '=ROUND($D%d*$E%d/10000;4)' % (r, r), b.APROV,
                    '=ROUND($F%d*$G%d;4)' % (r, r), b.PRECO['%s %d' % k]])
    out += [[], [],
            ['  OS PREÇOS POR UNIDADE   ·   ⭐ amarelo é digitado'], [],
            ['LINHA', 'UNIDADE', 'R$']]
    for rot, un, v in UNIT:
        out.append([rot, un, v])
    return out


def peca(r):
    """O custo de uma peça: área ÷ rendimento × preço da folha, e os dois
    saem do bloco de parâmetros pela CHAVE — nunca por posição."""
    return ('=IFERROR(ROUND($D{r}*$E{r}/10000*$F{r}'
            '/VLOOKUP($H{r};{t};{cr};FALSE)'
            '*VLOOKUP($H{r};{t};{cp};FALSE);2);"")'
            ).format(r=r, t=TAB_MAT, cr=COL_REND, cp=COL_PRECO)


def area_da_chave(cel_chave):
    """⭐ A ÁREA LÍQUIDA DE UM MATERIAL É A SOMA DAS PEÇAS QUE O USAM. É
    isto que faz a planilha virar motor: acrescente uma peça em AS PEÇAS e
    o número de chapas sobe sozinho."""
    return ('ROUND(SUMPRODUCT(($H${p0}:$H${p1}={c})*$D${p0}:$D${p1}'
            '*$E${p0}:$E${p1}*$F${p0}:$F${p1})/10000;4)'
            ).format(p0=PEC0, p1=PEC1, c=cel_chave)


if __name__ == '__main__':
    print('MAPA LIDO DA CLASSIFICAÇÃO')
    for n, v in [('material', (MAT0, MAT1)), ('itens', (ITE0, ITE1)),
                 ('peças', (PEC0, PEC1))]:
        print('  %-9s %3d a %3d' % (n, v[0], v[1]))
    for n, v in [('CUSTO DIRETO', DIRETO), ('TOTAL DO AMBIENTE', TOT_ITEM),
                 ('CONFERÊNCIA', CONFER), ('parâmetros', PAR0),
                 ('  materiais', PAR_M0), ('  por unidade', PAR_U0 + 2)]:
        print('  %-18s %3d' % (n, v))
    print('\n  TAB_MAT = %s' % TAB_MAT)
    print('\nEXEMPLO · o custo da primeira peça')
    print('  %s' % peca(PEC0))
    print('\nEXEMPLO · a área líquida de um material')
    print('  =%s' % area_da_chave('$B%d' % MAT0))
