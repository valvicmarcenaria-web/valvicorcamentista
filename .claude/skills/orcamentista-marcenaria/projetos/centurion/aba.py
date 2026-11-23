# -*- coding: utf-8 -*-
"""CENTURION MOTORS — A ABA NO PADRÃO DA CASA, ITEM POR ITEM.

⛔⛔⛔ O QUE ESTE ARQUIVO CONSERTA [Jonathan, 23/11/2026]: "vc nao esta
  seguindo o padrao que estabelecemos na planilha. os itens nao estao
  separados. quero poder alterar o quantitativo de material de cada item
  sem comprometer o funcionamento da planilha."

  Estava certo. Eu vinha entregando um painel agregado em cima e TODAS as
  peças soltas embaixo, agrupadas só por um marcador ■, com a fita, a laca,
  o LED e a ferragem num painel único e o custo de cada item saído de um
  RATEIO meu. ⛔ Assim o item não é nada: é uma etiqueta. Mexer no
  quantitativo de um móvel não tinha como não contaminar os outros.

⭐ O PADRÃO DE VERDADE, que é o do Attos Costa Laguna e está na planilha
  desde 04/11/2026 — CADA ITEM É UM BLOCO AUTOSSUFICIENTE:

     ITEM 01 · nome do móvel                       medida geral
     a observação do item
     MATERIAL | ESPECIFICAÇÃO | C | L | QTD | UN | R$ UN | CUSTO || chave
     as peças de chapa dele ..................................
     a fita dele, a laca dele, o LED dele, a ferragem dele ...
     TOTAL DO ITEM 01                                  =SUM(I..:I..)

  ⭐ E então o painel do ambiente é DERIVADO: cada linha dele soma as peças
    POR CHAVE, com SUMPRODUCT e SUMIF. Ninguém digita o painel.
  ⭐ E o custo do item, no bloco OS ITENS, PUXA o TOTAL DO ITEM. Não há
    rateio nenhum: o item custa o que as peças dele custam.

⭐⭐ A DUPLA CONFERÊNCIA é o que prova que as duas contas são a mesma:
     soma dos itens (chapa em fração)  +  arredondamento para chapa cheia
                                       =  painel do ambiente
  Se der diferente, alguma peça está sem chave, ou uma chave não tem
  parâmetro. A planilha denuncia sozinha, na própria célula.

⭐ COMO AS LINHAS SE ACHAM: monto a aba numa passada, e onde uma fórmula
  precisa saber ONDE outra coisa ficou, deixo uma FUNÇÃO no lugar da
  célula. No fim, uma segunda passada resolve todas as funções com o mapa
  de linhas já completo. ⛔ É por isso que não há número de linha cravado
  em lugar nenhum deste arquivo: cravar linha é o erro que mais me custou.
"""
import importlib.util, math, pathlib

AQUI = pathlib.Path(__file__).resolve().parent


def _mod(n, a):
    sp = importlib.util.spec_from_file_location(n, AQUI / a)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


b = _mod('cent_base', 'base.py')
lv = _mod('cent_lv', 'levantamento.py')
#   ⭐ As NOTAS, as DÚVIDAS e O QUE NÃO É NOSSO são TEXTO — a leitura da
#     prancha, que não depende de layout nenhum. Importo de onde já estão
#     escritos em vez de copiar: texto duplicado é texto que diverge.
tx = _mod('cent_tx', 'planilha.py')
NOTAS, DUVIDAS, NAO_E_NOSSO = tx.NOTAS, tx.DUVIDAS, tx.FORA

T = lv.T
COL = 'BCDEFGHIJK'          # B=0 … K=9

#   ⭐ A MEDIDA GERAL de cada item · ⛔ montada com as CONSTANTES, nunca
#     com número digitado: se o Jonathan mudar a cota do nicho, esta coluna
#     muda com ela.
def _medidas():
    pr = lv.N_PRAT
    return {
        1: '%s m² · %s m de profundidade' % (('%0.0f' % b.FORRO_M2),
                                             ('%0.2f' % lv.FORRO_PROF
                                              ).replace('.', ',')),
        2: '%d arcos · moldura de %s cm, %s cm de profundidade'
           % (b.N_NICHOS + b.N_PASSAGEM, ('%0.0f' % b.MOLDURA_L),
              ('%0.0f' % b.NICHO_PROF)),
        3: '%d fundos de %s × %s · %d prateleiras de %s × %s'
           % (b.N_NICHOS, ('%0.1f' % b.NICHO_L).replace('.', ','),
              ('%0.0f' % b.NICHO_H), pr,
              ('%0.1f' % b.NICHO_L).replace('.', ','),
              ('%0.0f' % b.NICHO_PROF)),
        4: '%s m² de painel em %d panos' % (
            ('%0.2f' % sum(L * A / 10000 for _r, L, A in b.PAINEIS)
             ).replace('.', ','), len(b.PAINEIS)),
        5: '%s m² de base em %d panos' % (
            ('%0.2f' % sum(L * A / 10000 for _r, L, A in b.ESPELHOS)
             ).replace('.', ','), len(b.ESPELHOS)),
        6: '%s m² de espelho em %d panos' % (
            ('%0.2f' % sum(L * A / 10000 for _r, L, A in b.ESPELHOS)
             ).replace('.', ','), len(b.ESPELHOS)),
    }


def _br(v, casas=2):
    """número na folha brasileira · ⭐ só para TEXTO de observação."""
    t = ('%0.*f' % (casas, v)).replace('.', ',')
    i, _, d = t.partition(',')
    out = ''
    while len(i) > 3:
        out, i = '.' + i[-3:] + out, i[:-3]
    return i + out + (',' + d if d else '')


def _n(v, casas=2):
    return round(v + 0.0, casas)


# ═══════════════════════════════════════════════════════════════════════
#   A ABA, EM CONSTRUÇÃO
# ═══════════════════════════════════════════════════════════════════════
class Aba:
    """Acumula linhas e lembra onde cada coisa ficou."""

    def __init__(self):
        self.L = []
        self.ix = {}            # nome -> linha (1-based)

    def add(self, *cels):
        self.L.append(list(cels))
        return len(self.L)      # ⭐ 1-based, que é o que a planilha usa

    def vazia(self):
        return self.add()

    def marca(self, nome, n=None):
        self.ix[nome] = len(self.L) if n is None else n
        return self.ix[nome]

    def resolve(self):
        """⭐ a segunda passada: agora toda função sabe onde tudo está."""
        out = []
        for r in self.L:
            lin = []
            for c in r:
                lin.append(c(self.ix) if callable(c) else c)
            while lin and lin[-1] in ('', None):
                lin.pop()
            out.append(lin)
        return out


# ═══════════════════════════════════════════════════════════════════════
#   ①  OS PARÂMETROS · UMA TABELA SÓ, e é a única coisa que se digita
# ═══════════════════════════════════════════════════════════════════════
#   ⛔ Antes eu tinha DUAS tabelas — chapas com 8 colunas e preços por
#     unidade com 3 — e cada fórmula precisava saber em qual procurar. Duas
#     tabelas é duas chances de procurar na errada. ⭐ Uma só, com a chave
#     na coluna B, o rendimento na H e o preço na I: TODA fórmula da aba
#     procura no mesmo lugar, pela chave.
CHAVES = sorted(T['chapas'])                      # (padrão, espessura)

ORIGEM = {
    'Compensado flexível': '⛔ não existe na Base · preço cravado pelo '
                           'Jonathan em 23/11/2026',
    'Fórmica': '⛔ a Base diz "a partir de R$ 400" sem dizer de que folha · '
               'preço cravado pelo Jonathan em 23/11/2026',
    'MDF Amadeirado': 'Base · MDF Melamínico Fosco, amadeirado e cor',
    'MDF Branco TX': 'Base · MDF Branco TX',
}

#   ⭐ (chave, unidade, preço, de onde vem) · é o que não se compra por folha
UNIT = [
    ('Fita de borda de cor, 22 mm', 'm', b.FITA_22,
     'Base · aba MDF · fita de cor, 22 mm'),
    ('Filetagem automática', 'm', b.FILETE_MAQ,
     'Base · coladeira automática · ⛔ serviço por metro, NÃO material: por '
     'isso fica fora da base dos consumíveis'),
    ('Laca fosca PU', 'm²', b.LACA_M2,
     '⭐ R$ 650 o m² cravado pelo Jonathan em 23/11/2026 · é a linha "Laca ou '
     'pintura em peça lisa" da Base, não a de R$ 300 dos jobs'),
    ('Alma de aço · barra de 3 m', 'barra', b.ALMA_BARRA,
     'Base · uma por prateleira, contra empeno'),
    ('LED COB · conjunto completo', 'm', b.LED_M,
     'Base · fita, perfil, usinagem e instalação'),
    ('Fonte de LED', 'un', b.LED_FONTE, 'Base · uma a cada 8 a 10 m'),
    ('Espelho prata', 'm²', b.ESPELHO_M2_PRECO,
     'Base · vidraceiro · ⛔ entra pela área da FOLHA, não pelo vão'),
    ('Frete de espelho', 'serviço', b.ESPELHO_FRETE,
     'Base · chapa de espelho não vai na carga de marcenaria'),
    ('Cola de contato · lata de %d kg' % b.COLA_KG, 'lata', b.COLA_LATA,
     '⭐ uma lata A MAIS, cravada pelo Jonathan em 23/11/2026 · a cola comum '
     'já está nos 6% de consumíveis'),
    ('Corte · por chapa', 'chapa', b.CORTE_CHAPA, 'Base da casa'),
    ('Corte · por peça', 'peça', b.CORTE_PECA, 'Base da casa'),
    ('Consumíveis', '% sobre chapa e fita', b.CONSUMIVEIS,
     'Base · cola, lixa, parafuso, cavilha, tapa-furo, fundo e verniz'),
    ('Embalagem', '% sobre o subtotal', b.EMBALAGEM,
     '⭐ 3% cravado pelo Jonathan em 19/11/2026 · a aba MDF da Base diz 2%'),
]
COL_REND, COL_PRECO = 7, 8      # dentro da tabela: H é a 7ª, I é a 8ª


def TAB(ix):
    return '$B$%d:$J$%d' % (ix['par_ini'], ix['par_fim'])


def _preco(ix, cel):
    return 'VLOOKUP(%s;%s;%d;FALSE)' % (cel, TAB(ix), COL_PRECO)


def _rend(ix, cel):
    return 'VLOOKUP(%s;%s;%d;FALSE)' % (cel, TAB(ix), COL_REND)


def _fixo(ix, chave):
    return _preco(ix, '"%s"' % chave)


#   ⛔⛔⛔ DUAS ARMADILHAS DE LOCALE pt-BR, as duas pegas em 23/11/2026
#     por olhar a planilha depois de gravar — nenhuma das duas aparece no
#     Python, só na célula:
#   (1) NA FÓRMULA, O DECIMAL É VÍRGULA. Escrevi IFERROR(...;0.8) e a
#       célula inteira virou #ERROR!, porque "0.8" não é número em pt-BR.
#       Eu já sabia que o separador de ARGUMENTO é ";" e não apliquei a
#       mesma regra ao decimal.
#   (2) NO PADRÃO DO TEXT(), O DECIMAL É PONTO. É o inverso: o padrão usa
#       símbolos neutros, então TEXT(22,4;"0,00") lê a vírgula como
#       separador de MILHAR e exibe "022". O certo é "0.00", que em pt-BR
#       EXIBE "22,40".
#   ⭐ Por isso as duas funções abaixo: número literal passa por N(), e
#     padrão de formato é sempre o neutro. Nunca escrever decimal solto.
def N(v):
    """um número literal DENTRO de fórmula · decimal com vírgula"""
    return ('%g' % v).replace('.', ',')


PAD2 = '"0.00"'        # ⭐ padrão NEUTRO, exibe 22,40 em pt-BR


def _txt(t):
    """⛔⛔ ASPA DUPLA DENTRO DE FÓRMULA QUEBRA A FÓRMULA. Eu escrevi uma
    citação do Jonathan entre aspas dentro de uma fórmula de texto e a
    célula inteira viraria erro de sintaxe. ⭐ No Sheets, a aspa literal
    dentro de string é DUPLICADA. Toda string que entra em fórmula passa
    por aqui — e é por isso que isto é função, e não um replace espalhado."""
    return t.replace('"', '""')

# ═══════════════════════════════════════════════════════════════════════
#   ②  AS FÓRMULAS · onde a planilha vira motor
# ═══════════════════════════════════════════════════════════════════════
#   ⭐ TODA fórmula aqui procura o preço e o rendimento PELA CHAVE, na
#     coluna K da própria linha. Nunca por posição. É o que permite ao
#     Jonathan inserir, apagar e reordenar peças sem quebrar nada.

def f_peca(r):
    """O custo de uma peça de chapa: área ÷ rendimento × preço da folha.

    ⭐ Isto é FRAÇÃO DE CHAPA, de propósito. A chapa inteira só aparece no
      painel do ambiente, onde se arredonda por PADRÃO × ESPESSURA — porque
      é ali que se compra. Ratear chapa cheia por item faria cada item
      pagar um pedaço de chapa que ele não usa."""
    return lambda ix: ('=IFERROR(ROUND($D{r}*$E{r}/10000*$F{r}/{rend}*{prec};2);'
                       '"")').format(r=r, rend=_rend(ix, '$K%d' % r),
                                     prec=_preco(ix, '$K%d' % r))


def f_insumo(r):
    """O custo de um insumo: quantidade × preço da unidade."""
    return lambda ix: ('=IFERROR(ROUND($F{r}*{prec};2);"")'
                       ).format(r=r, prec=_preco(ix, '$K%d' % r))


def f_total_item(a, z):
    """⭐ O TOTAL DO ITEM. É ELE que o bloco OS ITENS puxa — e é por isso
    que mexer no quantitativo de um item só mexe naquele item.

    ⛔⛔⛔ E POR QUE NÃO É UM SUM SIMPLES: `SUM($I$97:$I$103)` parece certo
      e falha no caso que mais importa. Quando se insere uma linha DENTRO
      do range, o Sheets estende a fórmula sozinho; quando se insere no FIM
      do bloco — logo acima do total, que é onde a pessoa naturalmente
      acrescenta —, o range NÃO cresce e a linha nova fica fora da soma,
      sem erro nenhum. Foi o que aconteceu em 23/11/2026 quando acrescentei
      a fita dos painéis: R$ 393,13 fora do total, e só a CONFERÊNCIA
      denunciou.
    ⭐ Com OFFSET, o total soma de $I$<primeira peça> até a linha
      IMEDIATAMENTE ACIMA de si mesmo, calculada por ROW() na hora. Não
      existe inserção que escape — que é exatamente o que o Jonathan pediu:
      "quero poder alterar o quantitativo de material de cada item sem
      comprometer o funcionamento da planilha"."""
    return lambda ix: ('=ROUND(SUM(OFFSET($I$%d;0;0;MAX(1;ROW()-%d);1));2)'
                       % (a, a))


#   ── as três varreduras do bloco AS PEÇAS ──
#   ⛔ A FAIXA DE PEÇAS TEM CABEÇALHOS DENTRO. Cada item traz a sua linha
#     "MATERIAL | ESPECIFICAÇÃO | C | L | QTD", e "C", "L" e "QTD" são
#     TEXTO nas colunas D, E e F. ⭐ Por isso todo SUMPRODUCT daqui usa
#     IF(ISNUMBER(...)): sem isso a fórmula inteira vira #VALUE!, e foi
#     assim que o Attos resolveu em 04/11/2026.
def _pecas(ix):
    return ix['pec_ini'], ix['pec_fim']


def f_area_chave(r):
    """A área líquida das peças de uma chave, em m² · ⭐ acrescente uma peça
    em AS PEÇAS e o número de chapas sobe sozinho."""
    def g(ix):
        a, z = _pecas(ix)
        return ('=ROUND(SUMPRODUCT(($K${a}:$K${z}=$B{r})*IF(ISNUMBER($D${a}:'
                '$D${z});$D${a}:$D${z}*$E${a}:$E${z}*$F${a}:$F${z};0))/10000;4)'
                ).format(a=a, z=z, r=r)
    return g


def f_chapas(r):
    """⛔ A REGRA DE FERRO: a chapa é a unidade de compra e arredonda-se
    para cima POR PADRÃO × ESPESSURA. Meia chapa não existe na nota."""
    def g(ix):
        a, z = _pecas(ix)
        #   ⛔⛔⛔ A TOLERÂNCIA DO ROUND(...;6) NÃO É ENFEITE. Sem ela, uma
        #     divisão que dá 6,000090 em vez de 6 arredonda para 7 e compra
        #     uma chapa do nada. Foi o que aconteceu com o fundo do nicho
        #     em 23/11/2026: o aproveitamento guardado com 4 casas perdia
        #     um décimo de milésimo e o ROUNDUP cobrava R$ 350 a mais ·
        #     ⭐ O motor em Python já fazia math.ceil(round(x, 6)) — a
        #     planilha tinha de fazer o mesmo, senão as duas contas divergem
        #     e a conferência acusa sem dizer por quê.
        return ('=ROUNDUP(ROUND(SUMPRODUCT(($K${a}:$K${z}=$B{r})*IF(ISNUMBER('
                '$D${a}:$D${z});$D${a}:$D${z}*$E${a}:$E${z}*$F${a}:$F${z};0))'
                '/10000/{rend};6);0)').format(a=a, z=z, r=r,
                                              rend=_rend(ix, '$B%d' % r))
    return g


def f_qtd_chave(r):
    """A quantidade de um insumo, somada pela chave."""
    def g(ix):
        a, z = _pecas(ix)
        return '=ROUND(SUMIF($K${a}:$K${z};$B{r};$F${a}:$F${z});4)'.format(
            a=a, z=z, r=r)
    return g


def f_custo_linha(r):
    """quantidade da linha × preço da chave da linha"""
    return lambda ix: '=ROUND($D%d*%s;2)' % (r, _preco(ix, '$B%d' % r))


def f_pct(r):
    return lambda ix: '=IFERROR(ROUND($F%d/$F$%d;6);"")' % (r, ix['direto'])


# ═══════════════════════════════════════════════════════════════════════
#   ③  A ABA, MONTADA
# ═══════════════════════════════════════════════════════════════════════
#   ⭐ as chaves de insumo que o projeto usa de fato, na ordem da tabela
CH_UNIT = [k for k, _u, _v, _o in UNIT]
USADAS = []
for _it in lv.ITENS:
    for _x in _it.lin + _it.serv:
        if _x['chave'] not in USADAS:
            USADAS.append(_x['chave'])
INSUMOS = [k for k in CH_UNIT if k in USADAS]      # ⭐ ordem da tabela
#   ⛔ CONFERÊNCIA DE CONSTRUÇÃO: chave lançada que não está na tabela de
#     parâmetros é linha sem preço, e é erro meu, não do Jonathan.
_orfas = [k for k in USADAS if k not in CH_UNIT]
assert not _orfas, 'chave sem parâmetro: %s' % _orfas

ESPEC = {
    'Fita de borda de cor, 22 mm':
        'Aresta vista, mais %d%% de desperdício · ⛔ só onde se vê: borda que '
        'encosta em peça laqueada não leva fita'
        % round((b.FITA_PERDA - 1) * 100),
    'Filetagem automática':
        'Coladeira automática · ⛔ serviço por metro, não material — fica fora '
        'da base dos consumíveis',
    'Laca fosca PU':
        'Face da moldura, intradorso e alizar dos pórticos · ⛔ NÃO o '
        'extradorso, que fica revestido e cru entre pórticos',
    'Alma de aço · barra de 3 m': 'Uma por prateleira montada, contra empeno',
    'LED COB · conjunto completo':
        'Fita, perfil, usinagem e instalação · uma régua por prateleira',
    'Fonte de LED': 'Uma a cada 8 a 10 m de régua',
    'Espelho prata': 'Vistas AA e CC, colado sobre o painel de MDF',
    'Frete de espelho': 'Carga própria do vidraceiro',
    'Cola de contato · lata de %d kg' % b.COLA_KG:
        'Uma lata inteira A MAIS, para a fórmica e o compensado em curva',
}


MEDIDA = _medidas()


def monta():
    A = Aba()

    #   ── título e subtítulo ──
    A.add('  VALVIC MARCENARIA        01 SHOWROOM · CENTURION MOTORS')
    A.add('  Projeto CLS Arquitetas Associadas · prancha 554, revisão 00 de '
          '17/11/2025 · Vila da Serra · forro amadeirado, %d pórticos curvos '
          'laqueados café (%d nichos e %d de acesso aos ambientes), os painéis '
          'que a prancha marcava como adesivo e os espelhos em dois itens · '
          '⛔ A LEGENDA DECIDE O ESCOPO: adesivo vira painel de MDF, MDF '
          'laqueado café é nosso, ESPELHO passou a ser nosso em 23/11/2026 e '
          'só a TINTA não é · ⭐ MC de %d%% = alvo de %d%% + %s (%d pontos) · '
          'preço na aba Preço e Comissões'
          % (b.N_NICHOS + b.N_PASSAGEM, b.N_NICHOS, b.N_PASSAGEM,
             round(b.MC * 100), round(b.MC_ALVO * 100), b.DIFICULDADE,
             round(b.PONTOS[b.DIFICULDADE] * 100)))
    A.vazia()

    # ══ O AMBIENTE ══════════════════════════════════════════════════════
    A.add('  O AMBIENTE   ·   ⭐ NÃO SE DIGITA NADA AQUI. Cada linha soma as '
          'peças de AS PEÇAS pela CHAVE, e o preço sai de OS PARÂMETROS. '
          'Mude uma peça lá embaixo e esta tabela se refaz · ⛔ a chapa '
          'arredonda para número cheio POR PADRÃO × ESPESSURA, porque é '
          'assim que se compra')
    A.vazia()
    A.add('MATERIAL', 'ESPECIFICAÇÃO', 'QUANTIDADE', 'UN', 'CUSTO',
          '% DO CUSTO')

    #   ── uma linha por chave de chapa ──
    #   ⭐ A ESPECIFICAÇÃO TAMBÉM É FÓRMULA. Ela mostra a área líquida e o
    #     rendimento, e é exatamente por isso que tem de ser fórmula: número
    #     calculado dentro de texto FIXO é mentira esperando a próxima
    #     mudança. Dentro de uma fórmula, nunca mente.
    A.marca('amb_ini', len(A.L) + 1)
    for k in CHAVES:
        r = len(A.L) + 1
        c, l = b.folha(k)
        nota = ''
        if k == ('MDF Amadeirado', b.FUNDO_ESP):
            nota = (' · ⛔⛔ UMA PEÇA POR CHAPA, não pela média: o fundo do '
                    'nicho tem %s × %s e os %s cm só entram no lado de %s — '
                    'a sobra de %s cm não comporta o segundo [Jonathan, '
                    '23/11/2026: \"cada um deles gasta 1 chapa de 6mm para o '
                    'fundo\"]'
                    % (_br(b.NICHO_L, 1), _br(b.NICHO_H, 0), _br(b.NICHO_H, 0),
                       _br(c, 0), _br(c - b.NICHO_H, 0)))
            nota = _txt(nota)
        A.add('%s %d' % k,
              (lambda rr, kk, cc, ll, nt: lambda ix:
               ('="%s · "&TEXT(%s;' + PAD2 + ')&" m² de peças · folha de '
                '%s × %s, rendimento de "&TEXT(%s;' + PAD2 + ')&" m² por '
                'chapa%s"')
               % (_txt(ORIGEM.get(kk[0], 'Base')),
                  f_area_chave(rr)(ix)[1:], _br(cc, 0), _br(ll, 0),
                  _rend(ix, '$B%d' % rr), nt))(r, k, c, l, nota),
              f_chapas(r), 'chapas', f_custo_linha(r), f_pct(r))
    A.marca('amb_chapa_fim', len(A.L))

    #   ── uma linha por insumo, somado pela chave ──
    for k in INSUMOS:
        r = len(A.L) + 1
        un = next(u for kk, u, _v, _o in UNIT if kk == k)
        A.add(k, ESPEC.get(k, ''), f_qtd_chave(r), un, f_custo_linha(r),
              f_pct(r))
    A.marca('amb_mat_fim', len(A.L))

    #   ── corte, consumíveis e embalagem ──
    r = len(A.L) + 1
    A.add('Corte · por chapa', 'Serviço de corte, por chapa comprada',
          lambda ix: '=SUM($D$%d:$D$%d)' % (ix['amb_ini'],
                                            ix['amb_chapa_fim']),
          'chapas',
          (lambda rr: lambda ix: '=ROUND($D%d*%s;2)'
           % (rr, _fixo(ix, 'Corte · por chapa')))(r), f_pct(r))
    A.marca('corte_ch', r)

    #   ⛔ O CORTE POR PEÇA CONTA A PEÇA, NÃO A CHAPA. E "peça" aqui é a
    #     linha que tem C e L preenchidos: insumo não tem medida, e
    #     cabeçalho tem TEXTO, que o ISNUMBER descarta.
    r = len(A.L) + 1
    A.add('Corte · por peça',
          'Serviço de corte, por peça cortada · ⛔ conta a PEÇA: toda linha '
          'de AS PEÇAS que tem C e L preenchidos',
          lambda ix: ('=SUMPRODUCT(IF(ISNUMBER($D${a}:$D${z})*ISNUMBER('
                      '$E${a}:$E${z});$F${a}:$F${z};0))'
                      ).format(a=ix['pec_ini'], z=ix['pec_fim']),
          'peças',
          (lambda rr: lambda ix: '=ROUND($D%d*%s;2)'
           % (rr, _fixo(ix, 'Corte · por peça')))(r), f_pct(r))
    A.marca('corte_pc', r)

    #   ⭐ CONSUMÍVEIS: 6% sobre CHAPA E FITA, e nada mais. A filetagem é
    #     serviço por metro; a laca, o LED e o espelho são de terceiro.
    #   ⛔⛔ E A FITA LANÇADA POR METRO TAMBÉM É FITA: o SUMIF por "Fita*"
    #     pega as duas, a do forro e a da prateleira. Antes, fita lançada
    #     como linha linear ficava FORA da base, e o mesmo material entrava
    #     ou não conforme COMO eu o lançava.
    r = len(A.L) + 1
    A.add('Consumíveis',
          'Cola, lixa, parafuso, cavilha, tapa-furo, fundo e verniz · %d%% '
          'sobre chapa e fita · ⛔ a filetagem NÃO entra: é mão de obra por '
          'metro, não material' % round(b.CONSUMIVEIS * 100),
          '', lambda ix: '=TEXT(%s;"0%%")' % _fixo(ix, 'Consumíveis'),
          lambda ix: ('=ROUND((SUM($F$%d:$F$%d)+SUMIF($B$%d:$B$%d;"Fita*";'
                      '$F$%d:$F$%d))*%s;2)'
                      % (ix['amb_ini'], ix['amb_chapa_fim'],
                         ix['amb_ini'], ix['amb_mat_fim'],
                         ix['amb_ini'], ix['amb_mat_fim'],
                         _fixo(ix, 'Consumíveis'))), f_pct(r))
    A.marca('consum', r)

    r = len(A.L) + 1
    A.add('Embalagem',
          'Papelão, filme, cantoneira, tinner e estopa · %d%% sobre o '
          'subtotal · ⭐ cravado pelo Jonathan em 19/11/2026; a regra escrita '
          'da casa dizia 2%% e estava atrás da decisão'
          % round(b.EMBALAGEM * 100),
          '', lambda ix: '=TEXT(%s;"0%%")' % _fixo(ix, 'Embalagem'),
          lambda ix: '=ROUND(SUM($F$%d:$F$%d)*%s;2)'
                     % (ix['amb_ini'], ix['consum'], _fixo(ix, 'Embalagem')),
          f_pct(r))
    A.marca('embal', r)

    r = len(A.L) + 1
    A.add('CUSTO DIRETO DO AMBIENTE', '', '', '',
          lambda ix: '=ROUND(SUM($F$%d:$F$%d);2)' % (ix['amb_ini'],
                                                     ix['embal']),
          f_pct(r))
    A.marca('direto', r)
    A.vazia()

    # ══ OS ITENS ════════════════════════════════════════════════════════
    A.add('  OS ITENS   ·   cada móvel com o SEU custo, porque é assim que a '
          'fábrica trabalha e é assim que o cliente corta escopo · ⭐ o custo '
          'de cada linha PUXA o TOTAL DO ITEM lá embaixo: não há rateio '
          'nenhum, o item custa o que as peças dele custam')
    A.vazia()
    #   ⭐ OS DIAS DE DUPLA [Jonathan, 23/11/2026]: "adicione o campo para
    #     inserir o tempo de profissionais em cada item, igual fizemos no
    #     orcamento da Kamila". ⭐ Ele escolheu dias de DUPLA, fabricação e
    #     montagem separados, e SÓ INFORMAÇÃO — não entra no custo.
    #   ⚠ As duas colunas são AMARELAS: é ele que preenche.
    A.add('ITEM', 'MÓVEL', 'MEDIDA GERAL', 'DIAS FABR.', 'DIAS MONT.', '',
          '', 'CUSTO')
    A.marca('ite_ini', len(A.L) + 1)
    for i, it in enumerate(lv.ITENS, 1):
        #   ⭐ D é a MEDIDA GERAL, não a observação: quem lê a lista de
        #     itens quer saber o TAMANHO do móvel, e a observação inteira
        #     mora no bloco do item, lá embaixo.
        A.add(i, it.nome, MEDIDA.get(i, ''), '', '', '', '',
              (lambda n: lambda ix: '=$I$%d' % ix['total_%d' % n])(i))
    A.marca('ite_fim', len(A.L))
    A.vazia()

    #   ══ A DUPLA CONFERÊNCIA ══════════════════════════════════════════
    #   ⭐⭐ É ELA QUE PROVA QUE A PLANILHA ESTÁ CERTA. As duas contas saem
    #     dos mesmos lançamentos por caminhos diferentes:
    #        pelos ITENS   · cada peça paga a FRAÇÃO de chapa que ocupa
    #        pelo AMBIENTE · a chapa é comprada INTEIRA
    #     A diferença é o arredondamento, e só ele. Se a conferência não der
    #     zero, há peça sem chave ou chave sem parâmetro — e a célula
    #     denuncia na hora, sem eu precisar conferir nada.
    r = len(A.L) + 1
    A.add('Soma dos itens · chapa rateada em fração', '', '', '', '', '', '',
          lambda ix: '=ROUND(SUM($I$%d:$I$%d);2)' % (ix['ite_ini'],
                                                     ix['ite_fim']))
    A.marca('conf_soma', r)
    r = len(A.L) + 1
    A.add('Arredondamento de chapa para número cheio · ⛔ a regra de ferro: '
          'meia chapa não existe na nota do fornecedor', '', '', '', '', '',
          '',
          lambda ix: ('=ROUND(SUM($F$%d:$F$%d)-SUMPRODUCT(SUMIF($K$%d:$K$%d;'
                      '$B$%d:$B$%d;$I$%d:$I$%d));2)'
                      % (ix['amb_ini'], ix['amb_chapa_fim'],
                         ix['pec_ini'], ix['pec_fim'],
                         ix['amb_ini'], ix['amb_chapa_fim'],
                         ix['pec_ini'], ix['pec_fim'])))
    A.marca('conf_arred', r)
    r = len(A.L) + 1
    A.add('MATERIAL E FERRAGEM, PELO RATEIO DOS ITENS', '', '', '', '', '',
          '', lambda ix: '=ROUND($I$%d+$I$%d;2)' % (ix['conf_soma'],
                                                    ix['conf_arred']))
    A.marca('conf_rateio', r)
    r = len(A.L) + 1
    A.add('Material e ferragem, pelo painel do ambiente', '', '', '', '', '',
          '', lambda ix: '=ROUND(SUM($F$%d:$F$%d);2)' % (ix['amb_ini'],
                                                         ix['amb_mat_fim']))
    A.marca('conf_painel', r)
    A.add('⭐ CONFERÊNCIA — as duas contas têm de dar a mesma coisa', '', '',
          '', '', '', '',
          lambda ix: '=ROUND($I$%d-$I$%d;2)' % (ix['conf_rateio'],
                                                ix['conf_painel']))
    A.add('', '⭐ E A SEGUNDA CONFERÊNCIA, que pega LINHA ENGOLIDA: toda '
          'linha com medida ou quantidade e com chave tem de ter custo · '
          '⛔⛔ E AQUI EU CORRIJO UM DIAGNÓSTICO MEU QUE ESTAVA ERRADO. Por '
          'duas vezes uma linha apareceu pela metade depois de gravar e eu '
          'escrevi que "gravação em bloco perde linha, com status de '
          'sucesso". Não era isso. Em 23/11/2026 fui olhar: a aba tinha '
          'CÉLULAS MESCLADAS de B a K, sobradas do layout anterior, em '
          'linhas que no layout novo são de DADO. Célula mesclada aceita '
          'valor só na âncora e descarta o resto da linha em silêncio — a '
          'API responde "success" e conta as células como gravadas · ⭐ A '
          'cura é desmesclar a aba inteira e mesclar de volta só título, '
          'subtítulo e seção, que é texto corrido. ⛔ A lição que eu havia '
          'escrito culpava a ferramenta e me faria quebrar as gravações em '
          'pedaços cada vez menores sem nunca resolver.')
    r = len(A.L) + 1
    A.add('⭐ CONFERÊNCIA — linha de AS PEÇAS sem custo (tem de ser zero)',
          '', '', '', '', '', '',
          lambda ix: ('=SUMPRODUCT((($D$%d:$D$%d<>"")+($F$%d:$F$%d<>"")>0)*'
                      '($K$%d:$K$%d<>"")*($I$%d:$I$%d=""))'
                      % (ix['pec_ini'], ix['pec_fim'],
                         ix['pec_ini'], ix['pec_fim'],
                         ix['pec_ini'], ix['pec_fim'],
                         ix['pec_ini'], ix['pec_fim'])))
    A.vazia()

    # ══ O QUE NÃO É MARCENARIA ══════════════════════════════════════════
    A.add('  O QUE NÃO É MARCENARIA   ·   está na prancha, não está nesta '
          'conta')
    A.vazia()
    for t in NAO_E_NOSSO:
        A.add('', t)
    A.vazia()

    # ══ AS PEÇAS, ITEM POR ITEM ═════════════════════════════════════════
    #   ⭐⭐⭐ ESTA É A SEÇÃO QUE O JONATHAN PEDIU EM 23/11/2026, e é o
    #     coração da planilha: CADA ITEM É UM BLOCO FECHADO. Tem o seu
    #     cabeçalho, as suas peças, os seus insumos e o seu TOTAL. Mexer no
    #     quantitativo de um item não toca em nenhum outro — e o painel do
    #     ambiente lá em cima se refaz sozinho, porque soma POR CHAVE.
    A.add('  AS PEÇAS, ITEM POR ITEM   ·   ⭐ É AQUI QUE SE TRABALHA. Cada '
          'linha é uma peça que vai para o plano de corte ou um insumo que '
          'vai para a ordem de compra · mude C, L ou QTD e o custo da peça, '
          'o total do item, o painel do ambiente e o preço de venda se '
          'refazem na mesma hora · ⛔ a CHAVE NA BASE (coluna K) é o que '
          'liga a linha ao preço: linha sem chave é linha sem custo, e a '
          'conferência lá em cima acusa')
    A.vazia()
    A.marca('pec_ini', len(A.L) + 1)
    for i, it in enumerate(lv.ITENS, 1):
        #   ── a testeira do item ──
        medida = MEDIDA.get(i, '')
        A.add('ITEM %02d' % i, it.nome, '', '', '', '', '', medida)
        A.add('', it.obs)
        A.add('MATERIAL', 'ESPECIFICAÇÃO', 'C', 'L', 'QTD', 'UN', 'R$ UN',
              'CUSTO', '', 'chave na Base')
        a = len(A.L) + 1
        #   ── as peças de chapa dele ──
        for pc in it.pecas:
            r = len(A.L) + 1
            ch = '%s %d' % (pc['mat'], pc['esp'])
            #   ⭐ a peça cujo aproveitamento a tabela de parâmetros deriva
            if (pc['mat'], pc['esp']) == ('MDF Amadeirado', b.FUNDO_ESP):
                A.marca('fundo', r)
            A.add(pc['nome'], pc['obs'] or '—', _n(pc['L'], 1),
                  _n(pc['A'], 1), pc['qtd'], 'm²',
                  (lambda rr: lambda ix: '=IFERROR(%s;"")'
                   % _preco(ix, '$K%d' % rr))(r),
                  f_peca(r), '', ch)
        #   ⛔⛔⛔ A FITA QUE MORA NO CAMPO `fita` DA PEÇA TAMBÉM É UMA
        #     LINHA. Eu lanço fita de dois jeitos — no campo `fita` de cada
        #     peça (os painéis) e como linha `.m()` quando a borda não é
        #     por peça (o perímetro do forro, a prateleira montada). ⭐ Só
        #     o segundo virava linha na aba, e os R$ 418,20 de fita e
        #     filetagem dos painéis de parede DESAPARECIAM: o motor em
        #     Python os cobrava, a planilha não, e a diferença só apareceu
        #     quando comparei os dois totais na mão.
        #   ⭐ Agora o campo `fita` vira DUAS linhas no bloco do item, com
        #     chave e tudo — e a planilha passa a ser autossuficiente, que
        #     é o que o Jonathan pediu.
        fita_pc = sum(pc['fita'] for pc in it.pecas)
        extra = []
        if fita_pc:
            mt = _n(fita_pc * b.FITA_PERDA, 4)
            extra = [
                dict(nome='Fita de borda de cor, 22 mm · aresta a aresta das '
                          'peças', qtd=mt, un='m',
                     chave='Fita de borda de cor, 22 mm',
                     obs='⭐ o perímetro de cada peça deste item, mais %d%% '
                         'de desperdício · ⛔ esta linha nasce do campo de '
                         'fita das peças: antes ela existia no motor e NÃO '
                         'na planilha, e eram R$ 418,20 que ninguém via'
                         % round((b.FITA_PERDA - 1) * 100)),
                dict(nome='Filetagem na coladeira automática · peças deste '
                          'item', qtd=mt, un='m',
                     chave='Filetagem automática',
                     obs='mesma metragem da fita · ⛔ serviço, não material'),
            ]

        #   ── a fita, a laca, o LED e a ferragem DELE ──
        for x in it.lin + it.serv + extra:
            r = len(A.L) + 1
            A.add(x['nome'], x['obs'] or '—', '', '', _n(x['qtd'], 4),
                  x['un'],
                  (lambda rr: lambda ix: '=IFERROR(%s;"")'
                   % _preco(ix, '$K%d' % rr))(r),
                  f_insumo(r), '', x['chave'])
        z = len(A.L)
        r = A.add('TOTAL DO ITEM %02d' % i, '', '', '', '', '', '',
                  f_total_item(a, z))
        A.marca('total_%d' % i, r)
        A.vazia()
    A.marca('pec_fim', len(A.L))
    return A

# ═══════════════════════════════════════════════════════════════════════
#   ④  O QUE SE ESCREVE E O QUE SE DIGITA · notas, dúvidas e parâmetros
# ═══════════════════════════════════════════════════════════════════════
def fecha(A):
    """As três seções finais · ⭐ OS PARÂMETROS vem por último porque é o
    único bloco que se DIGITA, e tudo em cima aponta para ele."""
    A.add('  AS NOTAS   ·   o que a leitura da prancha ensinou, e o que o '
          'Jonathan corrigiu')
    A.vazia()
    for t in NOTAS:
        A.add('', t)
    A.vazia()

    A.add('  AS DÚVIDAS   ·   ⛔ cada uma é dinheiro parado · ⭐ responda na '
          'coluna ao lado e eu recalculo')
    A.vazia()
    for t in DUVIDAS:
        A.add('', t)
    A.vazia()

    #   ══ OS PARÂMETROS ════════════════════════════════════════════════
    A.add('  OS PARÂMETROS DESTE ORÇAMENTO   ·   ⭐⭐ É DAQUI QUE TUDO EM '
          'CIMA SE CALCULA, e é o ÚNICO bloco que se digita. Mude um preço, '
          'uma folha ou um aproveitamento e a planilha inteira se refaz · '
          '⛔ a aba "Base (importada)" tem #REF! em D3 porque o IMPORTRANGE '
          'nunca foi autorizado nesta cópia — por isso os preços moram aqui, '
          'e só o Jonathan pode liberar aquela aba (abrir, clicar no #REF! '
          'de D3, PERMITIR ACESSO: nenhum script faz isso por nós)')
    A.vazia()
    A.add('CHAVE', 'DE ONDE VEM', 'FOLHA C', 'FOLHA L', 'ÁREA m²', 'APROV.',
          'RENDIM. m²', 'R$', 'UN')
    A.marca('par_ini', len(A.L) + 1)
    for k in CHAVES:
        r = len(A.L) + 1
        c, l = b.folha(k)
        ap = b.aprov(k)
        obs = ORIGEM.get(k[0], 'Base')
        aprov, rend_f = _n(ap, 4), None
        if k == ('MDF Amadeirado', b.FUNDO_ESP):
            obs += (' · ⛔⛔ APROVEITAMENTO DE UMA PEÇA POR CHAPA, NÃO OS '
                    '80%% DA MÉDIA: o fundo do nicho é peça grande que não '
                    'repete na chapa [Jonathan, 23/11/2026] · ⭐ e o APROV. '
                    'ao lado é FÓRMULA, tirada da própria peça: muda a cota '
                    'do nicho, muda o aproveitamento, e o número de chapas '
                    'continua certo sozinho')
            #   ⭐⭐ O APROVEITAMENTO DO FUNDO É DERIVADO DA PEÇA. Cravar
            #     39,49% funcionaria hoje e mentiria na primeira vez que a
            #     cota do nicho mudasse. ⛔ E o IFERROR cai nos 80% da casa
            #     se alguém apagar a peça — com N(), porque decimal literal
            #     dentro de fórmula pt-BR leva VÍRGULA.
            #   ⭐⭐ AQUI A CONTA VAI AO CONTRÁRIO, e de propósito. Para
            #     chapa normal o RENDIMENTO vem do aproveitamento. Para a
            #     peça que não repete, o rendimento É A ÁREA DE UMA PEÇA, e
            #     o aproveitamento é que deriva dele. ⛔ Passar pelo
            #     aproveitamento arredondado foi o que criou a sétima chapa.
            aprov = (lambda rr: lambda ix:
                     '=IFERROR(ROUND($H%d/$F%d;4);%s)' % (rr, rr, N(b.APROV)))(r)
            rend_f = (lambda rr: lambda ix:
                      '=IFERROR(ROUND($D$%d*$E$%d/10000*%s;6);ROUND($F%d*$G%d;4))'
                      % (ix['fundo'], ix['fundo'], N(b.FUNDO_POR_CHAPA),
                         rr, rr))(r)
        A.add('%s %d' % k, obs, _n(c, 1), _n(l, 1),
              '=ROUND($D%d*$E%d/10000;4)' % (r, r), aprov,
              rend_f if rend_f else '=ROUND($F%d*$G%d;4)' % (r, r),
              _n(b.PRECO['%s %d' % k]), 'folha')
    for ch, un, v, orig in UNIT:
        A.add(ch, orig, '', '', '', '', '', _n(v, 4), un)
    A.marca('par_fim', len(A.L))
    A.vazia()
    A.add('', '⭐ A COLUNA APROV. É A QUE DENUNCIA PEÇA QUE NÃO ENCAIXA. '
             '80% é a média da casa e vale para peça que repete na chapa. '
             'Quando uma peça é grande e não repete, o aproveitamento real '
             'despenca — e é o aproveitamento REAL que tem de estar aqui, '
             'senão a planilha compra menos chapa do que o marceneiro '
             'precisa. ⛔ Foi exatamente esse o erro de 23/11/2026.')
    return A


def gera():
    return fecha(monta()).resolve()
