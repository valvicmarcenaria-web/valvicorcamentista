"""CENTURION MOTORS — ⚠ ESTE ARQUIVO VIROU REPOSITÓRIO DE TEXTO.

⛔⛔ O QUE MUDOU EM 23/11/2026: o Jonathan apontou que "os itens nao estao
  separados", e a aba foi reconstruída no PADRÃO POR ITEM. Quem gera a aba
  agora é o `aba.py`; o `linhas()` daqui é do layout ANTIGO — painel
  agregado em cima e peças soltas embaixo — e NÃO é mais usado.

⭐ O que continua vivo aqui, e é por isso que o arquivo não foi apagado:
     NOTAS     as 21 notas da leitura da prancha
     DUVIDAS   as 8 dúvidas abertas
     FORA      o que não é marcenaria
  São TEXTO, não dependem de layout nenhum, e o `aba.py` os importa daqui
  em vez de duplicá-los. ⛔ Texto duplicado é texto que diverge.

⚠ O `formulas.py` foi APAGADO na mesma data: o `aba.py` faz o que ele
  fazia, e melhor — monta as fórmulas contra UMA tabela de parâmetros em
  vez de duas, e resolve as referências de linha em duas passadas, para
  não haver número de linha cravado em lugar nenhum.

⛔ NÃO acrescentar nada ao `linhas()` daqui. Se precisar mexer no layout,
  é no `aba.py`.
"""
import importlib.util, json, math, pathlib

AQUI = pathlib.Path(__file__).resolve().parent


def _mod(n, a):
    sp = importlib.util.spec_from_file_location(n, AQUI / a)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


b = _mod('cent_base', 'base.py')
lv = _mod('cent_lv', 'levantamento.py')
fo = _mod('cent_fmt', 'formato.py')

PLANILHA = '1viDAEugwv4IJgML4v0JJOpusjIkEQP8VyO2HzScwLRw'
ABA, SID = '01 Showroom · Centurion', 100
T = lv.T


def _n(v, casas=2):
    return round(float(v), casas)


def _br(v, casas=2):
    t = ('%0.*f' % (casas, v)).replace('.', ',')
    i, _, d = t.partition(',')
    neg, i = (i[0] == '-'), i.lstrip('-')
    out = ''
    while len(i) > 3:
        out, i = '.' + i[-3:] + out, i[:-3]
    return ('-' if neg else '') + i + out + (',' + d if d else '')


#   ⭐ O CUSTO DE CADA ITEM. A chapa é comprada por PADRÃO, inteira; cada
#     item leva a fatia da área que consumiu. Corte, consumíveis e
#     embalagem seguem a mesma proporção. É o mesmo rateio do Painel da
#     Sala, e a linha de conferência prova que fecha.
def custo_itens():
    out = []
    for it in lv.ITENS:
        c = 0.0
        for k, v in it.areas().items():
            preco = b.PRECO['%s %d' % k]
            rend = b.rend(k)
            c += v / rend * preco            # a fatia da chapa, sem arredondar
        c += it.c_fita() * b.FITA_PERDA * (b.FITA_22 + b.FILETE_MAQ)
        c += it.c_lin() + it.c_serv()
        out.append(c)
    #   o resto do custo direto (arredondamento de chapa, corte,
    #     consumíveis e embalagem) entra rateado pelo que cada item já pesa
    soma = sum(out)
    resto = T['direto'] - soma
    out = [c + resto * (c / soma) for c in out]
    #   ⛔ o último absorve o centavo, para a conferência fechar em ZERO
    out[-1] = T['direto'] - sum(out[:-1])
    return out


DIRETOS = custo_itens()
#   ⭐ as áreas do arco, para a nota que responde "por que 18 chapas?"
_COST_M2 = sum(n * A['envolvente_l'] * A['envolvente_a'] * 2 / 10000
               for _r, n, A in lv.ARCOS)
_ALIZ_M2 = sum(n * A['externo'] * b.ALIZAR_L / 10000 for _r, n, A in lv.ARCOS)
_ARCO_M2 = _COST_M2 + _ALIZ_M2
_PECA_M2 = sum(n * A['medio'] * b.MOLDURA_L / 10000 for _r, n, A in lv.ARCOS)
MIOLO_M2 = sum(n * (A['envolvente_l'] - 2 * b.MOLDURA_L)
               * (A['envolvente_a'] - b.MOLDURA_L) / 10000 * 2
               for _r, n, A in lv.ARCOS)


def linhas():
    D = T['direto']
    L = [['  VALVIC MARCENARIA        01 SHOWROOM · CENTURION MOTORS'],
         ['  Projeto CLS Arquitetas Associadas · prancha 554, revisão 00 de '
          '17/11/2025 · Vila da Serra · forro amadeirado de %s m², %d pórticos '
          'curvos laqueados café, os painéis que a prancha marcava como '
          'adesivo e os espelhos em dois itens · ⛔ A LEGENDA DECIDE O '
          'ESCOPO: adesivo vira painel de MDF, MDF laqueado café é nosso, '
          'ESPELHO passou a ser nosso em 23/11/2026 e só a TINTA não é · '
          '⭐ MC de 55%% = alvo de 50%% + MÉDIO (5 pontos) · preço na '
          'aba Preço e Comissões'
          % (_br(b.FORRO_M2, 0), b.N_NICHOS + 1)],
         []]

    # ── ① O AMBIENTE ────────────────────────────────────────────────────
    L += [['  O AMBIENTE   ·   o que ele consome, por linha de material'], [],
          ['MATERIAL', 'ESPECIFICAÇÃO', 'QUANTIDADE', 'UN', 'CUSTO',
           '% DO CUSTO', 'R$ UNITÁRIO']]

    #   ⛔ A COLUNA TEM DE SOMAR O QUE O TOTAL DIZ. Eu exibia cada linha
    #     arredondada a 2 casas e o total pelo valor exato do motor: somar
    #     as 22 linhas na planilha dava R$ 96.913,75 contra R$ 96.913,76 no
    #     total. Um centavo, mas é a conta não fechando na cara de quem
    #     confere — e quem confere soma a COLUNA.
    #   ⭐ A última linha (embalagem) absorve a diferença dos arredondamentos,
    #     que é o mesmo mecanismo que o último item já usava.
    exibido = []

    def mat(rot, esp, qtd, un, custo, unit=None, ultima=False):
        if unit is None and qtd:
            unit = custo / qtd
        v = _n(custo)
        if ultima:
            v = _n(D - sum(exibido))
        exibido.append(v)
        #   ⭐ SEIS CASAS, não quatro: com quatro, a soma dos 22 percentuais
        #     dava 99,9% em vez de 100,0% — o erro de arredondamento de cada
        #     linha acumulava. ⛔ E aqui NÃO vale a regra de a última linha
        #     absorver, como no dinheiro: a coluna de dinheiro É a conta e
        #     tem de somar o total, mas cada percentual é uma razão da sua
        #     própria linha. Forçar a última a fechar faria ela mentir sobre
        #     si mesma. Mais precisão resolve sem mentir.
        L.append([rot, esp, _n(qtd, 2), un, v, _n(custo / D, 6),
                  _n(unit) if unit is not None else ''])

    for k, n in sorted(T['chapas'].items()):
        rend = b.rend(k)
        esp = ('área líquida de %s m² · rendimento de %s m² por chapa '
               '(%s × %s a 80%%) · ⛔ arredonda-se por PADRÃO × ESPESSURA'
               % (_br(T['area'][k]), _br(rend),
                  _br(b.folha(k)[0], 0), _br(b.folha(k)[1], 0)))
        if k[0] == lv.FLEX:
            esp = ('⭐ R$ 600,00 A CHAPA, PREÇO DO JONATHAN [23/11/2026] · '
                   '⛔ não é número da Base: a Base só tem compensado COMUM, '
                   'em chapa de 1600 × 2200, a R$ 150 (4 mm), e flexível é '
                   'outro produto. Eu havia ESTIMADO R$ 375, 2,5× o comum — '
                   'o dele é 60% mais alto, e é o que vale · ⚠ VALE SUBIR '
                   'ESTA LINHA PARA A BASE: todo projeto com curva vai '
                   'precisar dela · ' + esp)
        mat('%s %d mm' % k, esp, n, 'chapa', n * b.PRECO['%s %d' % k])

    fita_m = sum(it.c_fita() for it in lv.ITENS) * b.FITA_PERDA
    mat('Fita de borda de cor, 22 mm', 'bordas aparentes · R$ 3,00 o metro '
        'mais 10% de desperdício', fita_m, 'm', T['c_fita'])
    mat('Filetagem na coladeira automática', 'R$ 2,50 o metro · ⚠ é mão de '
        'obra por metro: vive fora dos dias de dupla', fita_m, 'm', T['c_filete'])

    for it in lv.ITENS:
        for x in it.lin + it.serv:
            mat(x['nome'], x['obs'], x['qtd'], x['un'],
                x['qtd'] * x['unit'], x['unit'])

    mat('Corte', '%d chapas a R$ 2,00 e %d peças a R$ 2,50'
        % (T['n_ch'], T['n_pc']), T['n_pc'], 'peça', T['c_corte'])
    mat('Consumíveis', '⭐ O PERCENTUAL É DIGITADO, na coluna QUANTIDADE · '
        'incide sobre chapa e fita · cola, lixa, parafuso, cavilha, tapa-furo '
        '· ⭐ O R$ UNITÁRIO AQUI É A BASE, não um preço: a soma da chapa e de '
        'TODA a fita · ⛔ a fita lançada como linha linear (o perímetro do '
        'forro e a frente das prateleiras, R$ %s) estava ficando fora desta '
        'base, porque só a fita do campo da peça entrava — o mesmo material '
        'contava ou não conforme COMO eu o lancei. Corrigido'
        % _br(sum(x['qtd'] * x['unit'] for it in lv.ITENS for x in it.lin
                  if 'Fita de borda' in x['nome'])),
        b.CONSUMIVEIS, '%', T['c_cons'])
    mat('Embalagem', '⭐ O PERCENTUAL É DIGITADO, na coluna QUANTIDADE · '
        'incide sobre tudo o que vem acima · papelão, filme e cantoneira · '
        '⭐ o R$ UNITÁRIO também é a BASE, não um preço · ⭐ esta linha '
        'absorve os centavos de arredondamento das linhas acima, para que '
        'somar a coluna dê exatamente o CUSTO DIRETO',
        b.EMBALAGEM, '%', T['c_emb'], ultima=True)
    L.append(['CUSTO DIRETO DO AMBIENTE', '', '', '', _n(D), 1.0])
    L += [[], []]

    # ── ② OS ITENS ──────────────────────────────────────────────────────
    #   ⭐⭐ AS DUAS COLUNAS DE TEMPO [Jonathan, 23/11/2026]: "adicione o campo
    #     para inserir o tempo de profissionais em cada item" · ele escolheu
    #     DIAS DE DUPLA, fabricação e montagem separados, e escolheu que o
    #     tempo NÃO SOMA ao custo.
    #   ⛔ E não somar é o certo, porque a aba Preço e Comissões avisa em
    #     caixa alta: "montagem e fabricação entram AQUI, como comissão —
    #     nunca como dia de marceneiro no custo direto: a equipe é salário
    #     fixo". Somar cobraria o mesmo trabalho duas vezes: a cascata já
    #     tira 2,28% de produção mais 2,28% de montagem do preço.
    #   ⭐ O que o tempo faz, então: alimenta o campo DIAS DE PROJETO do
    #     bloco O LUCRO DO PROJETO no Painel, que estava vazio, e permite
    #     ler MC por dia de cada móvel.
    L += [['  OS ITENS   ·   cada item é um móvel, e é assim que ele vai '
           'para a proposta   ·   ⭐ as duas colunas de DIAS são suas, em dias '
           'de dupla (1 marceneiro + 1 ajudante, 8 h) · ⛔ elas NÃO entram no '
           'custo: a cascata já paga fabricação e montagem como comissão'], [],
          ['ITEM', 'MÓVEL', 'MEDIDA', '', '', 'DIAS FABR.', 'DIAS MONT.',
           'CUSTO']]
    MED = {0: '%s m² de forro' % _br(b.FORRO_M2, 0),
           1: '%d arcos · moldura de %s cm, %s de profundidade'
              % (b.N_NICHOS + 1, _br(b.MOLDURA_L, 0), _br(b.NICHO_PROF, 0)),
           2: '%d fundos e %d prateleiras'
              % (b.N_NICHOS, b.N_NICHOS * b.PRAT_POR_NICHO),
           3: '%s m² de painel' % _br(lv.PAINEL_M2),
           4: '%s m² de base em Branco TX 18' % _br(lv.ESP_M2),
           5: '%s m² de espelho prata' % _br(lv.ESP_M2)}
    #   ⭐ a mesma regra do bloco acima: os valores EXIBIDOS têm de somar o
    #     total exibido, então o último item absorve o centavo dos
    #     arredondamentos — e não só o resto do rateio
    _vi = [_n(d) for d in DIRETOS]
    _vi[-1] = _n(D - sum(_vi[:-1]))
    #   ⭐ as duas células de DIAS saem VAZIAS, porque são dele para digitar.
    #     ⛔ Gravar zero ali seria mentir: zero é uma resposta, e vazio é a
    #     pergunta. O amarelo da formatação é o que diz "escreva aqui".
    for i, (it, v) in enumerate(zip(lv.ITENS, _vi)):
        L.append(['%02d' % (i + 1), it.nome, MED.get(i, ''), '', '', '', '', v])
        L.append(['', it.obs])
    #   ⭐ O TOTAL DOS DIAS é FÓRMULA, gravada à parte: tem de somar o que ele
    #     digitar, e por isso não pode ser valor.
    L.append(['TOTAL DO AMBIENTE', '', '', '', '', '', '', _n(D)])
    L.append(['⭐ CONFERÊNCIA — a soma dos itens contra o painel de material '
              '· ⛔ tem de dar ZERO: é o mesmo projeto contado por dois caminhos, '
              'por linha de material e por móvel.', '', '', '', '', '', '',
              _n(sum(DIRETOS) - D)])
    L += [[], []]

    # ── ③ O QUE NÃO É MARCENARIA ────────────────────────────────────────
    L += [['  O QUE NÃO É MARCENARIA   ·   está na prancha, não está '
           'nesta conta'], []]
    for n in FORA:
        L.append(['', n])
    L += [[], []]

    # ── ④ AS PEÇAS ──────────────────────────────────────────────────────
    L += [['  AS PEÇAS, ITEM POR ITEM   ·   cada linha é uma peça que vai '
           'para o plano de corte'], [],
          ['PEÇA', 'OBSERVAÇÃO', 'C', 'L', 'QTD', 'UN', 'CHAVE DA BASE',
           'CUSTO']]
    for it in lv.ITENS:
        L.append(['■ ' + it.nome, it.obs])
        for p in it.pecas:
            k = (p['mat'], p['esp'])
            rend = b.rend(p['mat'])
            area = p['L'] * p['A'] / 10000 * p['qtd']
            L.append([p['nome'], p['obs'], _n(p['L'], 1), _n(p['A'], 1),
                      p['qtd'], 'pç', '%s %d' % k,
                      _n(area / rend * b.PRECO['%s %d' % k])])
    L += [[], []]

    # ── ⑤ AS NOTAS ──────────────────────────────────────────────────────
    L += [['  AS NOTAS   ·   o que a leitura da prancha ensinou'], []]
    for n in NOTAS:
        L.append(['', n])
    L += [[], []]

    # ── ⑥ AS DÚVIDAS ────────────────────────────────────────────────────
    L += [['  AS DÚVIDAS   ·   ⛔ cada uma é dinheiro parado, e estão em '
           'ordem de quanto valem'], []]
    for d in DUVIDAS:
        L.append(['', d])
    return L


FORA = [
 '⛔ TODA A PINTURA. A hachura bege pontilhada da legenda é "TINTA PAREDE SW 6069" e '
 'cobre a maior parte das três vistas. Não é marcenaria · ⚠ Eu quase a li como MDF '
 'laqueado, o que teria dobrado o orçamento sem motivo: só o marrom SÓLIDO da legenda '
 'é nosso.',
 '⛔ A TINTA DE FUNDO atrás dos painéis e o reboco: a parede chega pronta e aprumada '
 'para receber a marcenaria · ⭐ O ESPELHO SAIU DESTA LISTA em 23/11/2026: agora ele '
 'é nosso, em dois itens.',
 '⛔ A ILUMINAÇÃO DO FORRO. Os renders mostram fitas de LED correndo no teto e '
 'sanca acesa. O Jonathan pediu LED nas PRATELEIRAS, e só isso está orçado · no '
 'forro deixamos o rasgo e a passagem; fita, fonte e acionamento são do elétrico.',
 '⛔ A OBRA CIVIL, a bancada de mármore preto do bar, o piso, a escada e os pontos '
 'de fixação na laje e na alvenaria.',
 '⚠ OS QUADROS, as arandelas e o mobiliário solto que aparecem nas vistas e nos '
 'renders — mesa, cadeira, sofá, poltrona e tapete. Não são marcenaria sob medida.',
]

NOTAS = [
 '⭐⭐ AS DUAS COLUNAS DE DIAS, NO BLOCO OS ITENS [Jonathan, 23/11/2026]: "adicione o '
 'campo para inserir o tempo de profissionais em cada item" · ⭐ A unidade é DIA DE '
 'DUPLA, que é o mecanismo da casa: um marceneiro mais um ajudante, 8 horas, '
 'R$ %s o dia — o número que o Jonathan cravou na planilha do Painel da Sala em '
 '19/11/2026. Fabricação e montagem em colunas separadas, porque são momentos '
 'diferentes e quem monta não é necessariamente quem faz · ⛔⛔ E ELAS NÃO SOMAM AO '
 'CUSTO, por decisão dele e porque a aba Preço e Comissões avisa em caixa alta: '
 '"montagem e fabricação entram AQUI, como comissão — nunca como dia de marceneiro '
 'no custo direto: a equipe é salário fixo". Somar cobraria o mesmo trabalho duas '
 'vezes, já que a cascata tira %s%% de comissão de produção mais %s%% de montagem '
 'do preço · ⭐ O que elas fazem: a soma alimenta o campo DIAS DE PROJETO no bloco '
 'O LUCRO DO PROJETO do Painel, que estava vazio e é o único campo digitado de lá, '
 'e permite ler quanto cada móvel devolve de margem por dia de fábrica · ⚠ Eu não '
 'preenchi nenhuma: quem sabe quantos dias cada peça leva é quem a faz, e zero '
 'numa célula amarela seria uma resposta onde devia haver uma pergunta.'
 % (_br(b.DUPLA_DIA), '2,28', '2,28'),
 '⭐⭐ A LEGENDA DA PRANCHA É QUEM DECIDE O ESCOPO, e ela tem quatro símbolos: '
 'ADESIVO (hachura rosa), ESPELHO (diagonal), MDF LAQUEADO CAFE (marrom SÓLIDO) e '
 'TINTA PAREDE SW 6069 (bege pontilhada). ⛔ A bege cobre quase toda a parede nas '
 'três vistas e eu quase a contei como MDF laqueado — ela é TINTA. Ler a legenda '
 'ANTES de contar área foi o que impediu o orçamento de dobrar sem motivo.',
 '⭐⭐ O FORRO TEM 157 m² CRAVADOS NA PRANCHA: "ÁREA FORRO 157m²", escrito na '
 'planta 01. Não é cálculo meu, é número do projetista · Sozinho ele consome '
 '38,6 chapas de amadeirado, R$ %s de material: o maior item do orçamento.'
 % _br(b.FORRO_M2 / b.REND * 700),
 '⛔⛔ NÃO USAMOS SARRAFO DE PINUS [Jonathan, 23/11/2026]. Eu havia lançado 532,57 m '
 'de sarrafo a R$ 8,00 o metro — R$ 4.260,59 — em QUATRO linhas: barroteamento do '
 'forro, escoras de mão amiga, montante dos painéis e montante da base do espelho. '
 'Todas saíram · ⭐ E a Base já dizia o que entra, em dois lugares que eu não cruzei: '
 '"MDF Branco TX · Estrutura e caixaria · 15 mm · R$ 350,00" e, na tabela ESPESSURA '
 'PADRÃO POR APLICAÇÃO, "Estrutura e caixaria · 15 mm". A casa estrutura com CHAPA '
 'CORTADA EM TIRA, não com madeira de lei · ⛔⛔ E PIOR: ELE NÃO PRECISAVA TER ME DITO. '
 'A REGRA 1 DA CASA está escrita no próprio Painel desta planilha desde 28/10/2026: '
 '"⛔ NÃO SE USA PINUS PARA NADA. O engradado de painel virou TRAVESSA DE MDF tirada '
 'da própria chapa; o estrado de cama virou METALON. Não há uma única peça de pinus '
 'nos orçamentos da casa." Eu montei esse Painel e lancei pinus de todo modo · ⭐ A '
 'regra até dá o substituto exato que acabei usando: travessa de MDF tirada da '
 'própria chapa · ⛔ Ler as regras da casa ANTES de lançar material, não depois de '
 'ser corrigida · E isso muda de COLUNA no Painel: a '
 'estruturação deixou de ser material por metro e virou chapa, que se compra inteira '
 'e se arredonda por padrão × espessura.',
 '⭐ A MÃO AMIGA É MATERIAL DE MONTAGEM, NÃO ESTRUTURA [Jonathan, 23/11/2026: '
 '"importante considerar material para montagem de mao amiga"]. São as escoras em T '
 '— uma tira em pé com travessa no topo — que seguram a placa contra a laje enquanto '
 'o marceneiro parafusa. Sem elas não se monta forro a 2,91 m do chão · ⭐ O número é '
 'dele: "Considere 5 chapas brancas de 15mm para estruturação", e essas 5 chapas '
 'cobrem o barroteamento E as escoras, %s m² de chapa que dão %s m de tira de %.0f '
 'cm · ⚠ Isso é uma malha de cerca de 75 × 120, mais aberta que os 60 × 120 que eu '
 'havia assumido com sarrafo.'
 % (_br(lv.ESTRUT_M2_FORRO), _br(lv.ESTRUT_TIRA_FORRO, 1), b.TIRA_L),
 '⭐⭐ O PÓRTICO CURVO, CAMADA POR CAMADA [Jonathan, 23/11/2026]: moldura '
 'estrutural de MDF (as costelas), revestida de compensado flexível nos DOIS lados '
 '— intradorso, que é a curva de dentro, e extradorso, a de fora — mais o alizar '
 'de acabamento externo. A moldura tem %s cm de largura de face, cota confirmada na '
 'VISTA BB, e o alizar tem os mesmos %s cm, que foi ele quem corrigiu: "o alizar o '
 'projeto mostra 12cm" · ⭐⭐ E A CHAPA DO PÓRTICO É MDF BRANCO, não amadeirado — '
 '"Os arcos podem ser em mdf branco". É óbvio depois de dito: a peça é LACADA CAFÉ, '
 'a laca cobre tudo, e pagar R$ 700 de chapa amadeirada para esconder sob laca é '
 'jogar dinheiro fora. Branco 18 custa R$ 400, e são %s m² entre costela e alizar · '
 '⭐⭐ E O INTRADORSO TEM UMA CAMADA A MAIS, de 23/11/2026: sobre o compensado '
 'flexível vai FÓRMICA, e só depois a laca. São CINCO camadas no total, de dentro '
 'para fora: laca café, fórmica, compensado flexível, costela de MDF branco 18 e, do '
 'outro lado, compensado flexível de novo — mais o alizar arrematando contra a '
 'parede.'
 % (_br(b.MOLDURA_L, 0), _br(b.ALIZAR_L, 0),
    _br(sum(n * A['envolvente_l'] * A['envolvente_a'] * 2 / 10000
            for _r, n, A in lv.ARCOS)
        + sum(n * A['externo'] * b.ALIZAR_L / 10000
              for _r, n, A in lv.ARCOS))),
 '⭐⭐ A FÓRMICA NO INTRADORSO [Jonathan, 23/11/2026]: "adicione um revestimento de '
 'formica no intradorso. a formica tem a dimensao de 120X315 e custa 150,00 a folha" '
 '· ⭐⭐ E ISSO FECHA A DÚVIDA QUE EU HAVIA LEVANTADO uma mensagem antes: eu escrevi '
 'que o intradorso é compensado flexível de 4 mm, com veio e emenda, e que a linha de '
 'laca da Base fala de "peça LISA" — logo havia de confirmar se os R$ 650 o m² '
 'cobriam massa e selador sobre compensado cru. A fórmica é a resposta: ela '
 'TRANSFORMA o compensado em peça lisa, e aí a linha de R$ 650 vale pelo que diz · '
 'São %s m² de intradorso em %d folhas de %.0f × %.0f, R$ %s · ⚠ A Base tem "Fórmica, '
 'laminado de alta pressão · Revestimento sobre painel · a partir de R$ 400,00" sem '
 'dizer de que folha; o número dele é R$ %.0f e é o que vale · ⛔⛔ ATENÇÃO NO PLANO '
 'DE CORTE: a folha tem %.0f cm e o intradorso do nicho desenvolve %s cm — CADA ARCO '
 'LEVA EMENDA. Ela desaparece sob a laca, mas tem de estar prevista.'
 % (_br(lv._intra), T['chapas'].get((b.FORMICA, b.FORMICA_ESP), 0),
    b.FORMICA_C, b.FORMICA_L,
    _br(T['chapas'].get((b.FORMICA, b.FORMICA_ESP), 0) * b.FORMICA_PRECO),
    b.FORMICA_PRECO, b.FORMICA_C, _br(b.NICHO['interno'], 1)),
 '⭐ A COLA DE CONTATO, UMA LATA A MAIS [Jonathan, 23/11/2026]: "acrescente mais uma '
 'lata de cola de contato de 14k no custo dos nichos - custo de 600,00" · ⭐ "MAIS '
 'uma lata" é a palavra que importa: a cola comum já está nos CONSUMÍVEIS de 6%%, '
 'que cobrem "cola, lixa, parafuso, cavilha, tapa-furo". Esta é uma lata INTEIRA a '
 'mais, e faz sentido — colar laminado em superfície curva bebe cola de contato como '
 'nada: são %s m² de compensado flexível mais %s m² de fórmica, tudo em curva · '
 '⭐ Lançada no item 02, junto com o material que ela cola, e não no 03: o item 02 se '
 'chama pórtico curvo, mas é nele que os %d nichos são construídos. Separar a cola do '
 'que ela adere faria o rateio do custo mentir.'
 % (_br(T['area'].get((lv.FLEX, 4), 0)), _br(lv._intra), b.N_NICHOS),
 '⛔⛔ POR QUE OS ARCOS CONSOMEM TANTA CHAPA [pergunta do Jonathan, 23/11/2026: "por '
 'que os arcos estao consumindo 18 chapas?"] · ⭐ Primeiro desfazendo as 18: os ARCOS '
 'consomem %s m² — costela %s mais alizar %s — que são %d chapas, e a BASE DO ESPELHO '
 'consome as outras %d. Juntas dão %s m² e arredondam para 18 · ⛔⛔ E AS %d DOS ARCOS '
 'SÃO QUASE TODAS MIOLO: a moldura de %s cm de face soma %s m² de PEÇA, e o retângulo '
 'que ela ocupa na chapa soma %s m². São %.0f%% de desperdício, e não há como fugir: '
 'recorte curvo se compra pelo RETÂNGULO ENVOLVENTE, nunca pelo perímetro · ⭐⭐ MAS O '
 'MIOLO NÃO É LIXO, É A BASE DO ESPELHO. De dentro de cada arco sai uma peça inteira '
 'de até 104 × 140: são %s m² de Branco 18 em peças GRANDES, e a base do espelho pede '
 '%s m². Cabe inteiro, com folga · ⭐ Encaixando as duas coisas no mesmo plano de '
 'corte, as 18 chapas viram %d e R$ %s saem do orçamento · ⚠ Os outros %s m² de '
 'desperdício são os cantos do retângulo, retalho pequeno que não serve para peça '
 'grande · ⛔ Está orçado SEM aproveitar, que é o conservador: quem corta decide.'
 % (_br(_ARCO_M2), _br(_COST_M2), _br(_ALIZ_M2),
    math.ceil(_ARCO_M2 / b.REND), math.ceil(lv.ESP_M2 / b.REND),
    _br(_ARCO_M2 + lv.ESP_M2), math.ceil(_ARCO_M2 / b.REND),
    _br(b.MOLDURA_L, 0), _br(_PECA_M2), _br(_COST_M2),
    (_COST_M2 - _PECA_M2) / _COST_M2 * 100,
    _br(MIOLO_M2), _br(lv.ESP_M2), math.ceil(_ARCO_M2 / b.REND),
    _br(math.ceil(lv.ESP_M2 / b.REND) * 400),
    _br(_COST_M2 - _PECA_M2 - MIOLO_M2)),
 '⭐⭐ O FORRO VAI EM 15 mm [Jonathan, 23/11/2026]: "as chapas do teto podem ser de '
 '15mm". Eram 18, a R$ 700 a chapa; 15 custa R$ 550 · ⭐ São R$ 5.850,00 menos de '
 'chapa e R$ 6.387,03 menos de custo direto, que caiu de R$ 98.053,51 para R$ %s — e '
 'o preço desceu R$ 24.401,28 · ⭐ E o motivo técnico é melhor que o preço: forro '
 'PENDE DA LAJE, e a chapa de 15 pesa cerca de 17%% menos que a de 18. Em %s m² são '
 'quase 200 kg de menos pendurados no teto, o que alivia a fixação, a mão amiga e a '
 'montagem · ⚠ A contrapartida está nas dúvidas: 15 mm faz mais barriga entre '
 'barrotes que 18.'
 % (_br(T['direto']), _br(b.FORRO_M2, 0)),
 '⛔⛔ O RECORTE DO ARCO NÃO SE COMPRA PELO PERÍMETRO, SE COMPRA PELO RETÂNGULO '
 'QUE ELE OCUPA NA CHAPA. Um arco de %s cm de face parece consumir 0,55 m²; na chapa '
 'ele ocupa 1,28 × 2,04 = 2,61 m². São 16 recortes · ⭐⭐ E O MIOLO FICOU MAIS VALIOSO '
 'DEPOIS QUE OS ARCOS VIRARAM BRANCOS: são %s m² de MDF BRANCO 18, que é exatamente '
 'a chapa da base do espelho (%s m²) — cabe inteiro, com folga. Antes o miolo era '
 'amadeirado e teria de servir para fundo ou prateleira, que mudaram de espessura e '
 'não encaixam mais · Está orçado SEM aproveitar, e o ganho está na primeira dúvida.'
 % (_br(b.MOLDURA_L, 0), _br(MIOLO_M2), _br(lv.ESP_M2)),
 '⭐⭐ DOIS PREÇOS FECHADOS PELO JONATHAN EM 23/11/2026, e eram justamente as duas '
 'dúvidas mais caras desta folha: "Compensado flexivel, custo - 600,00 a chapa" e '
 '"laca considere 650" · ⛔ Nenhum dos dois é número da Base. O compensado FLEXÍVEL '
 'não existe lá — só o comum, a R$ 150 — e eu havia ESTIMADO R$ 375, 2,5× o comum; a '
 'laca tem duas linhas e eu havia lançado a de R$ 300 dos jobs, quando a certa é a de '
 'R$ 650 do materiais.json, que também é a mais coerente, porque as duas linhas falam '
 'de peça LISA e pórtico curvo leva mais lixa e mais tempo · ⭐ Os dois juntos '
 'somaram R$ 8.125,67, levando o custo direto de R$ 86.973,29 para R$ 95.098,96: '
 'R$ 1.800,00 nas 8 chapas de compensado, R$ 5.981,00 na laca, R$ 108,00 de '
 'consumíveis sobre a chapa nova e R$ 236,67 de embalagem · ⚠ e as respostas que ele '
 'deu depois, na própria planilha, mais a correção da base dos consumíveis, levaram '
 'o custo a R$ %s — a laca já está em %s m² '
 'porque o alizar passou a ter 12 cm · ⭐ A folha não ficou mais CARA por acaso, '
 'ficou mais FIRME: eram as duas únicas linhas que eu mesma havia marcado como '
 '"primeira cotação a fazer", e agora são preço de verdade · ⚠ VALE SUBIR AS DUAS '
 'PARA A BASE DE CUSTOS — o próximo projeto com curva vai precisar delas.'
 % (_br(T['direto']), _br(lv.LACA_M2)),
 '⭐⭐ MC DE 55%, APLICADA [Jonathan, 23/11/2026: "aplique a mc de 55%"] · ⭐ A MC '
 'aplicada não se digita: ela é a MC ALVO do projeto mais os pontos da DIFICULDADE '
 'do ambiente, pela tabela do quadro ⑤ da aba Preço e Comissões — Médio +5, Difícil '
 '+10, Complexo +20, e "Médio é o PISO, não o zero" · ⭐⭐ E OS 55% TÊM DOIS '
 'CAMINHOS, que dão o mesmo preço: eu havia posto a alvo no piso de 35% mais '
 'COMPLEXO, porque a definição de Complexo descreve este ambiente palavra por '
 'palavra — cinco ofícios (marcenaria, laminador, laca, vidraceiro e elétrica), oito '
 'arcos fora de esquadro e peças que não cabem em chapa inteira. O Jonathan preferiu '
 'o outro caminho: digitou alvo de 50% e deixou a dificuldade em MÉDIO. 50 + 5 = 55, '
 'igual · ⭐ A diferença não é de preço, é de onde a margem fica ANCORADA: na escolha '
 'do projeto, e não na complexidade do ambiente · ⚠ E tem uma consequência para '
 'depois: se entrar um segundo ambiente simples, ele herda a alvo de 50% e sai '
 'também a 55%, quando a tabela da casa o poria em 40%. Com um ambiente só, dá no '
 'mesmo.',
 '⭐ A GEOMETRIA DO ARCO FECHA SOZINHA, e isso dá confiança na leitura: o vão tem '
 '%s de largura, logo o raio do semicírculo é %s — e a prancha cota %s de abóbada. '
 'A altura interna sai %s + %s de prateleira + %s de trecho reto = %s, e a prancha '
 'cota %s no meio do terceiro nicho. Bate.'
 % (_br(b.NICHO_L, 1), _br(b.NICHO_L / 2, 2), _br(b.NICHO_ABOBADA, 0),
    _br(b.NICHO_ABOBADA, 0), '1,8', '138', '192,8', _br(b.NICHO_H, 0)),
 '⭐⭐ A PRATELEIRA, E POR QUE ELA TEM DUAS CAMADAS [Jonathan, 23/11/2026]: '
 '"considere 6 em cada, com 30mm de espessura, duas peças de 15mm" · ⭐ Duas peças de '
 '15 em vez de uma de 30 não é só o que existe em estoque: é ONDE A ALMA DE AÇO '
 'MORA. Rasga-se uma das faces, assenta-se a barra chata e cola-se a outra camada '
 'em cima — a alma fica embutida, invisível, e a peça de %d mm sai monolítica. Numa '
 'peça inteira de 30 a alma teria de ser fresada por baixo e apareceria · ⛔ São '
 '%d prateleiras × 2 camadas = %d peças, e a área de chapa TRIPLICOU: eu havia '
 'contado 4 por nicho em uma camada de 18 mm, 8,74 m²; agora são %s m² em %s de '
 '15 mm, a R$ 550 a chapa · ⭐ E a Base justifica a espessura: ela manda 18 mm acima '
 'de 70 cm de vão, e aqui o vão é de %s cm.'
 % (b.PRAT_ESP, b.N_NICHOS * b.PRAT_POR_NICHO,
    b.N_NICHOS * b.PRAT_POR_NICHO * b.PRAT_CAMADAS,
    _br(b.N_NICHOS * b.PRAT_POR_NICHO * b.PRAT_CAMADAS * b.NICHO_L
        * b.NICHO_PROF / 10000), b.PRAT_MAT, _br(b.NICHO_L, 1)),
 '⭐ ALMA DE AÇO EM TODA PRATELEIRA, como a Base manda: "uma por peça, contra '
 'empeno" — e uma por PRATELEIRA, não uma por camada: são %d almas, %d barras de '
 '3 m, R$ 750,00 · Prateleira de %s cm de vão sem apoio no meio empena, e o '
 'Jonathan pediu nominalmente · ⭐ é ela que explica as duas camadas de 15 mm: a '
 'barra chata mora ENTRE elas.'
 % (b.N_NICHOS * b.PRAT_POR_NICHO,
    math.ceil(b.N_NICHOS * b.PRAT_POR_NICHO * b.NICHO_L / b.ALMA_M),
    _br(b.NICHO_L, 1)),
 '⭐⭐ ONDE ACABA A LACA E COMEÇA O AMADEIRADO, DENTRO DO NICHO [Jonathan, '
 '23/11/2026]: "os nichos serão laqueados nas laterais, amadeirado sera apenas o '
 'fundo e as prateleiras" · ⭐ Isso confirma a leitura e dá nome à peça: a "lateral '
 'do nicho" é o INTRADORSO, a superfície curva de compensado flexível que corre pelos '
 '%.0f cm de profundidade e que se vê de dentro do vão — %s m² nos 8 arcos. Laqueada '
 'café, junto com a face frontal da moldura (%s m²) e o alizar (%s m²): %s m² ao todo, '
 'R$ %s · ⭐ E amadeirado só o que ele disse: o fundo em 6 mm (%s m²) e as prateleiras '
 'em duas camadas de 15 (%s m²) · ⛔⛔ E ISSO CORRIGIU A FITA: eu fitava a frente MAIS '
 'os dois lados de 30 cm de cada prateleira, mas a prateleira vai de lateral a '
 'lateral e essas bordas encostam no intradorso LAQUEADO — não se vê, não se fita. '
 'Eram 25,2 m de fita e de filetagem a mais, R$ 152,46 · ⭐ E A LATERAL LAQUEADA GANHOU '
 'UMA CAMADA em 23/11/2026: a laca vai sobre FÓRMICA, não sobre o compensado cru — '
 'era isso que faltava para a linha de "peça LISA" da Base valer pelo que diz.'
 % (b.NICHO_PROF, _br(lv._intra), _br(lv._face), _br(lv._aliz),
    _br(lv.LACA_M2), _br(lv.LACA_M2 * b.LACA_M2),
    _br(b.N_NICHOS * b.NICHO_L * b.NICHO_H / 10000),
    _br(b.N_NICHOS * b.PRAT_POR_NICHO * b.PRAT_CAMADAS * b.NICHO_L
        * b.NICHO_PROF / 10000)),
 '⭐ O FUNDO DO NICHO VAI EM 6 mm [Jonathan, 23/11/2026]: "os fundos serao em mdf '
 'de 6mm" · A Base concorda em dois lugares — "MDF Branco TX · Fundos · 6 mm" e a '
 'tabela de espessura, "Fundos · 6 mm · por encaixe em rasgo, SEM FITA" — e é por '
 'isso que a linha do fundo não leva borda nenhuma nesta folha · ⚠ Mas AMADEIRADO '
 'de 6 mm (R$ 350), não branco: este fundo é a face que se vê dentro do nicho, a '
 'que a prancha marcava como ADESIVO.',
 '⛔ O LED É CONJUNTO COMPLETO, NÃO SÓ O PERFIL. A Base avisa em caixa alta que o '
 'LED instalado vai de R$ 66 a R$ 150 o metro "conforme entre só o perfil ou o '
 'conjunto com fita, fonte, usinagem e instalação. Antes de orçar, fechar o que a '
 'linha inclui". Fechado no CONJUNTO, porque prateleira que acende é o conjunto '
 'inteiro · São %s m de régua e %d fontes.'
 % (_br(b.N_NICHOS * b.PRAT_POR_NICHO * b.NICHO_L / 100), math.ceil(
     b.N_NICHOS * b.PRAT_POR_NICHO * b.NICHO_L / 100 / 9)),
 '⭐⭐ O ESPELHO VIROU DOIS ITENS [Jonathan, 23/11/2026]: "um item considerando os '
 'paineis para receber a colagem dos espelhos. e outro item com os espelhos." ⛔ Isso '
 'TIROU o espelho de "o que não é marcenaria": a regra da casa é que vidro e espelho '
 'só entram quando fazem parte do MÓVEL, e agora fazem · ⭐ Separar os dois é certo, '
 'porque são dois fornecedores, dois preços e dois prazos — e a Base avisa que "a '
 'medida sai depois do móvel montado, nunca antes", então o espelho é a ÚLTIMA coisa '
 'a entrar na obra · O substrato vai em Branco TX 18, não em amadeirado: a face some '
 'inteira sob o espelho e a chapa custa R$ 400 em vez de R$ 700, o que economiza '
 'R$ 1.800,00 nas 6 chapas.',
 '⛔⛔ ERRO QUE EU COMETI E QUE NÃO QUEBRA NADA: lancei o forro como 39 peças do '
 'tamanho da chapa, e o motor — que já divide área por RENDIMENTO — aplicou o '
 'aproveitamento de 80% DUAS VEZES. Os 157 m² viraram 198 e as 39 chapas viraram '
 '49: dez chapas de R$ 700 saídas do nada, R$ 7.000, sem nada quebrar · ⭐ Quem '
 'lança área lança ÁREA; o rendimento é do motor.',
]

#   ⭐⭐ OITO DÚVIDAS FECHADAS EM 23/11/2026 — seis respondidas pelo Jonathan
#     na própria planilha, na coluna ao lado de cada uma, mais o compensado e
#     a laca que vieram no chat. O que sobra é só o que ninguém ainda sabe.
DUVIDAS = [
 '⭐⭐ R$ %s · O MIOLO DOS 16 RECORTES DE ARCO, E AGORA ELE VALE MAIS. São %s m² de '
 'chapa que saem de dentro dos arcos em peças de até 104 × 140 · ⭐ e desde que os '
 'arcos passaram a ser MDF BRANCO 18, o miolo é BRANCO 18 — que é exatamente a '
 'chapa da base do espelho, %s m². CABE INTEIRO, com folga · ⛔ Está orçado SEM '
 'aproveitar, que é o conservador: aproveitando, saem as %d chapas de Branco 18 da '
 'base do espelho, R$ %s · ⭐ É a decisão de corte mais rentável da folha, e só '
 'depende do plano de corte encaixar as duas coisas na mesma chapa.'
 % (_br(math.ceil(lv.ESP_M2 / b.REND) * 400), _br(MIOLO_M2), _br(lv.ESP_M2),
    math.ceil(lv.ESP_M2 / b.REND), _br(math.ceil(lv.ESP_M2 / b.REND) * 400)),
 '⚠⚠ R$ %s · A FÓRMICA É O SUBSTRATO DA LACA, OU É O ACABAMENTO? O Jonathan disse '
 '"ADICIONE um revestimento de formica no intradorso" — adicione, não troque — e uma '
 'mensagem antes havia dito que "os nichos serão laqueados nas laterais" · ⭐ Entendi '
 'que a fórmica entra SOB a laca: ela transforma o compensado flexível, que tem veio '
 'e emenda, na PEÇA LISA que a linha de R$ %.0f o m² da Base descreve, e era '
 'exatamente a dúvida que eu havia levantado. Com isso o intradorso leva compensado + '
 'fórmica + laca, e a laca segue cobrindo os %s m² · ⛔ MAS SE A FÓRMICA FOR O '
 'ACABAMENTO FINAL, a laca sai do intradorso: %s m² a R$ %.0f = R$ %s fora do '
 'orçamento, e a laca cai para %s m², só face e alizar · ⭐ É a maior consequência de '
 'uma palavra nesta folha, e a cola de contato que ele mandou acrescentar sugere '
 'colagem de laminado, não pintura — o que reforça a leitura de SUBSTRATO.'
 % (_br(lv._intra * b.LACA_M2), b.LACA_M2, _br(lv.LACA_M2), _br(lv._intra),
    b.LACA_M2, _br(lv._intra * b.LACA_M2), _br(lv.LACA_M2 - lv._intra)),
 '⚠ A PROFUNDIDADE DO NICHO NÃO ESTÁ EM PRANCHA NENHUMA. O Jonathan cravou %s cm '
 'em 23/11/2026, e é ela que define a caixa dos %d pórticos: o compensado flexível '
 'dos dois lados, a prateleira, o LED e a ÁREA LAQUEADA DA LATERAL escalam todos '
 'com ela. Conferir na medição · ⭐ cada 5 cm de profundidade a mais valem cerca de '
 'R$ %s de laca, R$ %s de compensado e R$ %s de prateleira.'
 % (_br(b.NICHO_PROF, 0), b.N_NICHOS + 1,
    _br(sum(n * A['interno'] for _r, n, A in lv.ARCOS) * 5 / 10000 * b.LACA_M2),
    _br(sum(n * (A['interno'] + A['externo']) for _r, n, A in lv.ARCOS) * 5
        / 10000 / b.rend(b.FLEX) * b.PRECO['Compensado flexível 4']),
    _br(b.N_NICHOS * b.PRAT_POR_NICHO * b.PRAT_CAMADAS * b.NICHO_L * 5
        / 10000 / b.REND * b.PRECO['MDF Amadeirado 15'])),
 '⚠ A EMENDA DA FÓRMICA. A folha tem %.0f cm e o intradorso do nicho desenvolve %s '
 'cm: cada um dos %d arcos leva emenda. Ela desaparece sob a laca, mas tem de estar '
 'no plano de corte, e quem corta decide onde — de preferência no trecho reto, nunca '
 'no meio da abóbada · ⚠ Lancei %d folhas pelo rendimento de 80%% da casa; se a '
 'emenda exigir sobreposição generosa, pode ir a %d, R$ %.0f a mais.'
 % (b.FORMICA_C, _br(b.NICHO['interno'], 1), b.N_NICHOS + 1,
    T['chapas'].get((b.FORMICA, b.FORMICA_ESP), 0),
    T['chapas'].get((b.FORMICA, b.FORMICA_ESP), 0) + 1, b.FORMICA_PRECO),
 '⚠ A FITA DA PRATELEIRA. A borda da prateleira montada tem %d mm, porque são duas '
 'camadas de %d coladas — e a fita da Base tem 22 mm. Peça de 30 mm pede fita de 35 '
 'mm, que a Base não lista · lancei a de 22 mm a R$ 3,00 o metro, R$ %s nos %s m de '
 'perímetro das %d prateleiras. ⭐ Fita de 35 mm costuma custar cerca de metade mais, '
 'o que daria uns R$ %s a mais — pouco dinheiro, mas é material que não existe na '
 'Base e precisa de linha própria.'
 % (b.PRAT_ESP, b.PRAT_ESP_PECA, _br(lv.PRAT_PERIM * b.FITA_PERDA * b.FITA_22),
    _br(lv.PRAT_PERIM * b.FITA_PERDA), b.N_NICHOS * b.PRAT_POR_NICHO,
    _br(lv.PRAT_PERIM * b.FITA_PERDA * b.FITA_22 * 0.5)),
 '⚠ AS 5 CHAPAS DE ESTRUTURAÇÃO COBREM SÓ O FORRO? O Jonathan cravou "5 chapas '
 'brancas de 15mm para estruturação" respondendo à dúvida da MÃO AMIGA, então '
 'entendi que são do FORRO — barroteamento mais escora — e acrescentei %s m² de '
 'tira para os painéis de parede e a base do espelho, que também precisam de '
 'montante aprumado. Dá %d chapas no total, R$ %s · ⛔ Se as 5 já eram para tudo, '
 'saem 2 chapas, R$ 700.'
 % (_br(lv.PAINEL_TIRA * b.TIRA_L / 100 + lv.ESP_TIRA * b.TIRA_L / 100),
    T['chapas'].get((b.ESTRUT, b.ESTRUT_ESP), 0),
    _br(T['chapas'].get((b.ESTRUT, b.ESTRUT_ESP), 0) * 350)),
 '⚠ A LARGURA DA TIRA DE ESTRUTURA é premissa minha de %.0f cm — quem corta decide. '
 'Ela não muda o número de chapas do forro, que o Jonathan cravou, mas muda os '
 'painéis e a base: tira mais larga, mais chapa.' % b.TIRA_L,
 '⚠ O PERÍMETRO DO FORRO É ESTIMATIVA. A prancha dá a ÁREA (157 m²) e uma cota de '
 '1380 de profundidade; pelo retângulo equivalente o perímetro fica em %s m. É ele '
 'que manda na fita e na filetagem do forro — R$ %s —, então o erro possível é '
 'pequeno, mas está registrado.'
 % (_br(lv.FORRO_PERIM), _br(lv.FORRO_PERIM * b.FITA_PERDA
                             * (b.FITA_22 + b.FILETE_MAQ))),
]
#   ⭐ A GRAFIA DO CLIENTE SAIU DAS DÚVIDAS em 23/11/2026: o Jonathan
#     confirmou, e a proposta sai como "Centurion Motors", que é a do
#     moodboard e a que ele usa. No carimbo da prancha está "CENTURIUM".


if __name__ == '__main__':
    L = linhas()
    (AQUI / 'planilha.json').write_text(
        json.dumps({ABA: L}, ensure_ascii=False, indent=1), encoding='utf-8')
    cl = fo.classifica(L)
    from collections import Counter
    print('%d linhas · %s' % (len(L), dict(Counter(cl))))
    print('custo direto %s · soma dos itens %s · diferença %s'
          % (_br(T['direto']), _br(sum(DIRETOS)),
             _br(sum(DIRETOS) - T['direto'])))
    print('miolo dos recortes %s m² · %d chapas' % (_br(MIOLO_M2),
                                                       math.floor(MIOLO_M2 / b.REND)))
