# -*- coding: utf-8 -*-
"""PAINEL DA SALA — o levantamento vira aba de planilha.

⭐ [Jonathan, 19/11/2026] "coloque o orcamento na planilha".

⛔⛔ COPIA-SE O MODELO, NUNCA O ORÇAMENTO DE OUTRO CLIENTE. A planilha deste
  job nasceu de `Valvic · PLANILHA BASE de Levantamento (modelo vazio)`
  (11IgmtI5Xd...), como o Painel da própria base manda em caixa alta. O
  arquivo de outro cliente carregaria os dados dele e quebraria o
  IMPORTRANGE [Jonathan, 29/10/2026].

⛔ A ORDEM É DESMESCLAR → GRAVAR VALOR → FORMATAR. Gravar valor sobre faixa
  mesclada escreve só a célula-âncora e descarta o resto SEM ERRO. No job do
  Charbel isso engoliu 33 linhas em silêncio.

Planilha: 1fiw2KEbRWGf6_U0w89geSBPdSaFWijbrEp3GlEtx3FQ
"""
import importlib.util, pathlib, json

AQUI = pathlib.Path(__file__).resolve().parent
def _mod(n, a):
    sp = importlib.util.spec_from_file_location(n, AQUI / a)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
b = _mod('ps_base', 'base.py')
lv = _mod('ps_lv', 'levantamento.py')
fo = _mod('ps_fmt', 'formato.py')

PLANILHA = '1fiw2KEbRWGf6_U0w89geSBPdSaFWijbrEp3GlEtx3FQ'
ABA, SID = '01 Sala · Painel ripado', 301
T = lv.T
REND = b.CHAPA_M2 * b.APROV


def _n(v, casas=2):
    """número puro, para a célula não virar texto"""
    return round(float(v), casas)


def _br(v):
    """1234.5 -> "1.234,50", para escrever o unitário DENTRO do rótulo"""
    return ('%0.2f' % v).replace('.', ',')


def linhas():
    L = [['  VALVIC MARCENARIA        01 SALA · PAINEL RIPADO'],
         ['  Executivo SALA · VISTA 2 (1/50) e NICHO RIPADO (1/30, pág. 18) · '
          'obra em %s · painel corrido de %.0f × %.0f sobre sóculo de pedra de 15 · '
          'ripado até 352, onde a pedra termina, e liso nos %.0f seguintes · '
          'trama de 20/20, passo de 4 cm'
          % (b.OBRA, lv.LARG, lv.ALT, lv.LISO_L)],
         []]

    # ── ① O AMBIENTE ────────────────────────────────────────────────────
    L += [['  O AMBIENTE   ·   o que ele consome, por linha de material'], [],
          ['MATERIAL', 'ESPECIFICAÇÃO', 'QUANTIDADE', 'UN', 'CUSTO',
           '% DO CUSTO', 'R$ UNITÁRIO']]
    D = T['direto']
    #   ⭐ `unit` só existe nas linhas de logística e de dupla: são as que o
    #     ambiente DIGITA, e nelas o custo é fórmula (quantidade × unitário).
    #     Nas demais o custo vem da Base e não há o que digitar.
    def mat(rot, esp, qtd, un, custo, unit=None):
        #   ⛔ O UNITÁRIO NÃO PODE FICAR EM BRANCO [Jonathan, 19/11/2026]:
        #     "o valor unitario dos itens na aba 01 sala estao em branco".
        #     Eu abri a coluna e enchi só as oito linhas digitadas — as
        #     outras vinte ficaram vazias, e coluna com cabeçalho e sem
        #     número parece erro, não parece escolha. Agora TODA linha tem:
        #     amarela onde se digita, cinza onde eu derivo de custo ÷ qtd.
        if unit is None and qtd:
            unit = custo / qtd
        lin = [rot, esp, _n(qtd, 2), un, _n(custo), _n(custo / D, 4),
               _n(unit) if unit is not None else '']
        L.append(lin)

    for k, n in sorted(T['chapas'].items()):
        mat('%s %d mm' % k, 'área líquida de %.2f m² · rendimento de %.2f m² por '
            'chapa (275 × 185 a 80%%) · ⛔ arredonda-se por PADRÃO × ESPESSURA'
            % (T['area'][k], REND), n, 'chapa', n * T['preco'][k])
    f22 = sum(i.fita22 for i in lv.M); f50 = sum(i.fita50 for i in lv.M)
    frp = sum(i.fita_ripa for i in lv.M)
    mat('Fita de borda de cor, 22 mm', 'peças, folhas e marcos · R$ 3,00 o metro '
        'mais 10% de desperdício', f22, 'm', f22 * b.FITA_22 * b.FITA_PERDA)
    mat('Fita de borda de cor, 50 mm', '⛔ a borda das portas de passagem tem 42 mm '
        'e NÃO leva fita de 22 · R$ 7,00 o metro mais 10%', f50, 'm',
        f50 * b.FITA_50 * b.FITA_PERDA)
    mat('Fita de borda de cor, 22 mm · ripas', 'as DUAS faces e os dois topos de cada '
        'uma das %d ripas' % sum(int(l // b.PASSO) for l, _a, _r in lv.BANDAS),
        frp, 'm', frp * b.FITA_22 * b.FITA_PERDA)
    mat('Filetagem manual', '⛔ coladeira automática não pega peça de 20 mm de '
        'largura: a Base nomeia o caso em "o que não entra na máquina · R$ 5,00"',
        frp, 'm', frp * b.FILETE_RIPA)
    mat('Filetagem na coladeira automática', 'as demais peças, 15 e 18 mm · R$ 2,50 o metro',
        f22 + f50, 'm', (f22 + f50) * b.FILETE_MAQ)
    ag = {}
    for it, _q in T['L']:
        for n, qt, u in it.fer:
            a = ag.setdefault(n, [0, u]); a[0] += qt
    ESP_FER = {
        'Dobradiça Blum': '⭐ 21 folhas de armário · a tabela da Base manda 2 até 90 cm, '
                          '3 até 160, 4 até 200 e 5 acima · é a linha que dá 30 anos de garantia',
        'Pulsador Blum Tip-on, abertura por toque': '⛔ porta mimetizada em ripado NÃO tem '
                          'puxador: cava cortaria a trama. Nove folhas de armário',
        'Suporte de prateleira, jogo de 4': '⭐ regra 2 da casa: é a PRATELEIRA a unidade, '
                          'não o par de pinos — R$ 6,50 o jogo de quatro',
        'Alma de aço, barra chata de 3 m': '⚠ a folha de 50 × 277 em 15 mm pede barra chata '
                          'contra empeno',
        'Sistema pivô de porta mimetizada': 'as duas portas de passagem',
        'Fecho rolete para porta pivotante': 'as duas portas de passagem',
    }
    for n, (qt, u) in ag.items():
        mat(n, ESP_FER.get(n, ''), qt, 'un', qt * u)
    m2r = sum(l * a / 10000 for l, a, _r in lv.BANDAS)
    mat('Painel ripado, mão de obra', '⚠ R$ 180 o m² na Base, que avisa "faixa observada '
        'de 70 a 420 · depende da largura da ripa e do vão" — trama de 20/20 é a mais '
        'fechada que já fizemos', m2r, 'm²', T['c_terc'])
    mat('Corte', '%d chapas a R$ 2,00 e %d peças a R$ 2,50 · ⛔ a ripa NÃO entra nesta '
        'contagem: quem paga o corte das tiras é a mão de obra de painel ripado'
        % (T['n_chapas'], T['pecas']), T['pecas'], 'peça', T['c_corte'])
    #   ⭐⭐ OS TRÊS CAMPOS QUE O AMBIENTE DIGITA [Jonathan, 19/11/2026].
    #     Na planilha a QUANTIDADE destes três é célula AMARELA, e o custo é
    #     fórmula. O custo do dia da dupla mora numa célula só, na aba
    #     "Preço e Comissões", e todos os ambientes a referenciam.
    #   ⭐⭐ O CUSTO ESPECIAL DE GV, LINHA A LINHA [Jonathan, 19/11/2026].
    #     Cada uma tem a QUANTIDADE amarela e o unitário escrito no
    #     rótulo, para ele trocar UM número sem refazer o bloco.
    for v in b.LOGISTICA:
        mat(v['rotulo'],
            '⭐ DIGITE A QUANTIDADE E O UNITÁRIO · %s · ⛔ obra especial em '
            '%s: estes são os números do Jonathan, não estimativa minha — as '
            'QUATRO linhas de frete da Base continuam vazias, "A COTAR"'
            % (v['obs'], b.OBRA),
            v['qtd'], v['un'], v['qtd'] * v['unit'], v['unit'])
    mat('Fabricação · dupla de marceneiro e ajudante',
        '⭐ A QUANTIDADE É DIGITADA: dias de DUPLA, não de pessoa · 83 peças, '
        '162 ripas coladas e 292 m de filetagem manual · o custo do dia vem '
        'da célula única da aba "Preço e Comissões"',
        b.DIAS_FABRICACAO, 'dia', b.DIAS_FABRICACAO * b.DUPLA_DIA, b.DUPLA_DIA)
    mat('Montagem · dupla de marceneiro e ajudante',
        '⭐ A QUANTIDADE É DIGITADA: são os MESMOS %d dias das diárias de '
        'Airbnb e dos %d dias de alimentação, lá em cima — mexeu num, mexa '
        'nos três · ⛔ a equipe NÃO entra na logística: aquele bloco paga '
        'carreto, carro, cama e comida, e a mão de obra é esta linha · '
        '⚠ o dia de quem vai MEDIR não está aqui nem lá: o bate-volta paga '
        'a estrada, não a diária. Somar 1 dia custa R$ 460,80'
        % (b.AIRBNB_QTD, b.ALIMENTACAO_QTD // 2),
        b.DIAS_MONTAGEM, 'dia', b.DIAS_MONTAGEM * b.DUPLA_DIA, b.DUPLA_DIA)
    mat('Consumíveis', '⭐ O PERCENTUAL É DIGITADO, na coluna QUANTIDADE · '
        'incide sobre chapa e fita · cola, lixa, parafuso, cavilha, tapa-furo', b.CONSUMIVEIS, '%', T['c_cons'])
    mat('Embalagem', '⭐ O PERCENTUAL É DIGITADO, na coluna QUANTIDADE · '
        'incide sobre tudo menos a logística e a dupla · papelão, filme '
        'e cantoneira',
        b.EMBALAGEM, '%', T['c_emb'])
    L.append(['CUSTO DIRETO DO AMBIENTE', '', '', '', _n(D), 1.0])
    L += [[], []]

    # ── ② OS ITENS ──────────────────────────────────────────────────────
    L += [['  OS ITENS   ·   cada item é um móvel, e é assim que ele vai para a proposta'],
          [],
          ['ITEM', 'MÓVEL', 'MEDIDA', '', '', '', '', 'CUSTO',
           'MATERIAL DO ITEM']]
    MED = {0: '302 × 75 × 50', 1: '302 × 71 × 50', 2: '50 × 277 × 50',
           3: '330 × 277', 4: '83 × 210 e 70 × 210, folha de 42 mm', 5: '682 × 277'}
    #   ⭐⭐ O ITEM NÃO PODE SER VALOR CONGELADO [Jonathan, 19/11/2026:
    #     "me explique ... -R$ 553,81"]. Eu escrevi os seis itens como
    #     número fixo e depois fiz o painel de material virar fórmula — aí
    #     ele andou (dia da dupla, embalagem, um dia a mais) e os itens
    #     ficaram para trás. A linha de conferência gritou, que é o que ela
    #     existe para fazer, mas o certo é ela nunca ter o que gritar.
    #   ⭐ Vai para a planilha o MATERIAL PURO de cada móvel — sem embalagem,
    #     sem logística, sem dupla — e o custo do item é fórmula:
    #       item = material do item ÷ soma dos materiais × CUSTO DIRETO
    #     Ratear o total pela fatia de material dá exatamente o mesmo que
    #     somar o material e ratear só o frete, porque embalagem e frete são
    #     os dois proporcionais. E a soma dos materiais é a MESMA base da
    #     embalagem, SUM(F7:F24)+F33 — conferida, ao centavo.
    _mat = [(d - T['c_frete'] * (d / T['direto'])) / (1 + b.EMBALAGEM)
            for d in T['diretos']]
    for i, ((it, _q), d, mt) in enumerate(zip(T['L'], T['diretos'], _mat)):
        L.append(['%02d' % (i + 1), it.nome, MED.get(i, ''), '', '', '', '',
                  _n(d), _n(mt)])
        L.append(['', it.obs])
    L.append(['⭐ CONFERÊNCIA — a soma dos itens contra o painel de material · '
              '⛔ tem de dar ZERO: é o mesmo projeto contado por dois caminhos, '
              'por linha de material e por móvel. Qualquer número aqui é custo '
              'que um lado cobra e o outro não.',
              '', '', '', '', '', '', _n(sum(T['diretos']) - D)])
    L += [[], []]

    # ── ③ O QUE NÃO É MARCENARIA ────────────────────────────────────────
    L += [['  O QUE NÃO É MARCENARIA   ·   está na prancha, não está nesta conta'],
          [],
          ['', '⛔ O NICHO 131 × 302 EM MÁRMORE TRAVERTINO ROMANO ESTUCADO. Regra 19 '
           '[Jonathan, 29/10/2026]: pedra nunca é nossa. A marcenaria entrega o vão pronto '
           'para recebê-lo.'],
          ['', '⛔ O SÓCULO, que a própria prancha diz ser EM ALVENARIA revestida de '
           'mármore, e o RODAPÉ de 15 cm em travertino.'],
          ['', '⛔ A ILUMINAÇÃO DO NICHO [Jonathan, 18/11/2026] "iluminação nao é nossa". '
           'A prancha pede PREVER fita de LED 3000 K, e prever é o elétrico: deixamos o rasgo '
           'e a passagem; fita, fonte e acionamento são de outro.'],
          ['', '⛔ A JANELA 202 × 175 em vidro laminado com estrutura metálica preta, e '
           'toda a alvenaria, elétrica e revestimento — inclusive os pontos de fixação.'],
          ['', '⚠ O PUXADOR DAS DUAS PORTAS DE PASSAGEM aparece no render e NÃO está '
           'especificado no executivo: não está orçado. As nove folhas de armário não levam '
           'puxador nenhum, por decisão de projeto — abrem no toque.'],
          [], []]

    # ── ④ AS PEÇAS ──────────────────────────────────────────────────────
    L += [['  AS PEÇAS, ITEM POR ITEM   ·   cada linha é uma peça que vai para o plano de corte'],
          [],
          ['PEÇA', 'OBSERVAÇÃO', 'C', 'L', 'QTD', 'UN', 'CHAVE DA BASE', 'CUSTO']]
    for it, q in T['L']:
        L.append(['■ ' + it.nome, it.obs])
        for p in it.pecas:
            area = p['L'] * p['A'] / 10000 * p['qtd']
            L.append([p['nome'], p['obs'], _n(p['L'], 1), _n(p['A'], 1),
                      p['qtd'], 'pç', '%s %d' % (p['mat'], p['esp']),
                      _n(area / REND * T['preco'][(p['mat'], p['esp'])])])
    L += [[], []]

    # ── ⑤ AS NOTAS ──────────────────────────────────────────────────────
    L += [['  AS NOTAS   ·   o que a leitura da prancha ensinou'], []]
    for n in NOTAS:
        L.append(['', n])
    L += [[], []]

    # ── ⑥ AS DÚVIDAS ────────────────────────────────────────────────────
    L += [['  AS DÚVIDAS   ·   ⛔ cada uma é dinheiro parado, e estão em ordem de quanto valem'],
          []]
    for d in DUVIDAS:
        L.append(['', d])
    return L


NOTAS = [
 '⭐⭐ A TRAMA DESTE PROJETO NÃO É A DA CASA. A prancha crava "RIPADO EM MDF GIANDUIA '
 'TRAMA DE 20MM E ESPAÇAMENTO DE 20MM - DURATEX" e o detalhe 1/5 confirma com a cota '
 '2 · 2 · 2. Passo de 4 cm, contra os 6 cm do nosso padrão (ripa 4, vão 2): são 25 '
 'ripas por metro em vez de 16,7. CINQUENTA POR CENTO MAIS RIPA E MAIS FILETAGEM por '
 'm² de face. Quem copiar o passo da casa erra o orçamento para baixo.',
 '⛔⛔ E O VÃO TEM 2 CM DE PROFUNDIDADE: enxerga-se o fundo entre as ripas. O substrato '
 'sai no MESMO Gianduia, nunca em branco nem em cru. Foi a primeira coisa que eu ia '
 'economizar e é a que apareceria na obra.',
 '⛔ PORTA DE PASSAGEM É 42 MM, não 18. A aba MDF da Base crava em "ESPESSURA PADRÃO POR '
 'APLICAÇÃO". Folha de 42 é tamponamento: 18 + 18 + 6, a MESMA ÁREA TRÊS VEZES. E a borda '
 'de 42 mm pede fita de 50, não a de 22.',
 '⛔ A FITA DAS RIPAS NÃO EXISTIA no primeiro levantamento: eu cobrei a FILETAGEM (a '
 'aplicação) e esqueci a FITA (o material) nos 292 m de ripa. A Base tem o par pronto — '
 '"fita de cor com filetagem, preço cheio da casa, R$ 5,50, já inclui a aplicação" = '
 '3,00 + 2,50.',
 '⭐ A DOBRADIÇA BLUM CUSTA OS MESMOS R$ 50 DA HETTICH SENSYS na Base — e a escada de '
 'garantia da casa dá 10 anos ao Hettich e 30 ao Blum. Trocar a linha não custou um '
 'centavo e devolveu vinte anos de promessa. ⚠ Pendência: só o termo de 10 anos está '
 'desenhado; o de 30 precisa existir assinado antes de a proposta sair.',
 '⚠ A BÁSCULA SAIU POR DECISÃO [Jonathan, 18/11/2026]: a banda de cima vai de 2,17 m a '
 '2,92 m do piso, e porta de girar de 75 × 75 a essa altura abre para fora e para baixo, '
 'na cara de quem está na mesa de jantar. A báscula sobe. Fica escrito porque não aparece '
 'no orçamento e aparece na obra.',
 '⭐⭐ O DIA DA DUPLA [Jonathan, 19/11/2026]: fabricação e montagem deixaram de ser '
 'comissão e passaram a ser DIAS DE DUPLA — um marceneiro (R$ 36/h, da Base) mais um '
 'ajudante (R$ 21,60/h, ⚠ premissa minha de 60%: a Base não tem a linha), 8 h por dia = '
 'R$ 460,80. O custo do dia é UMA célula, na aba "Preço e Comissões"; os dias são '
 'digitados em cada ambiente. ⛔ E a equipe NÃO entra na logística: aquele bloco paga '
 'carreto, carro, cama e comida, e nada de mão de obra — as duas coisas juntas '
 'pagariam a montagem duas vezes, e isso some no total sem avisar.',
 '⭐⭐ O CUSTO ESPECIAL DE GOVERNADOR VALADARES [Jonathan, 19/11/2026] substituiu a '
 'minha tabela de km × R$/km. São seis linhas, todas números dele: medição bate-volta '
 'R$ 350 por pessoa; carreto de caminhão HR R$ 2.500; Mobi com R$ 400 de combustível e '
 'R$ 170 de pedágio; Airbnb R$ 900 pelas 4 diárias; alimentação R$ 440 por pessoa pelos '
 '4 dias, com duas pessoas. ⛔ DÁ R$ 5.200 E EU ESTIMAVA R$ 3.420: eu estava R$ 1.780 '
 'ABAIXO, metade disso só no carreto, que sozinho vale quase o que eu punha no bloco '
 'inteiro. A lição é a de sempre — quando a Base diz "A COTAR", a resposta está com '
 'quem compra, não comigo.',
 '⛔⛔ A CASCATA AINDA COBRA COMISSÃO DE PRODUÇÃO (2,14%) E DE MONTAGEM (2,14%), '
 'R$ 2.287,12 no total — e o modelo diz em caixa alta que "montagem e fabricação '
 'entram AQUI, como comissão — nunca como dia de marceneiro no custo direto". Com a '
 'dupla no custo direto, as duas linhas pagam o MESMO trabalho. ⭐ Zerando as duas, a '
 'MC deste projeto sobe de 26,91% para 31,18% sem mexer no preço. ⚠ DECISÃO PENDENTE '
 'do Jonathan.',
 '⭐ OS TRÊS ARMÁRIOS NÃO ESTÃO NO EXECUTIVO. A prancha desenha o painel como superfície '
 'contínua; as bandas acima e abaixo do nicho e a coluna de 50 viraram armário por decisão '
 'de 18/11/2026, com caixa, prateleira e ferragem em cada vão. A proposta diz isso em '
 'bloco destacado.',
]

DUVIDAS = [
 '⚠ R$ 4.608 · OS DIAS DE DUPLA. A logística de GV saiu desta lista: os R$ 5.200 são '
 'números do Jonathan, não estimativa. O que continua sendo premissa é a mão de obra. '
 'A HORA DO AJUDANTE (R$ 21,60, 60% do marceneiro) NÃO EXISTE NA BASE: é o primeiro '
 'número a trocar, e ele mexe em TODOS os ambientes de uma vez, porque o dia da dupla é '
 'uma célula só. E os DIAS — 6 de fábrica, 4 de montagem — são estimativa de quem leu '
 'a prancha, não apontamento de quem fez. ⚠ Falta ainda o DIA DE QUEM VAI MEDIR: os '
 'R$ 350 do bate-volta pagam os 640 km, não a diária de quem dirigiu.',
 '⚠ R$ 2.132 · "GIANDUIA TRAMA - DURATEX" é padrão ESPECIAL? Trama é texturizado, e a Base '
 'tem a linha "CHAPA — COR E ACABAMENTO ESPECIAL · R$ 1.000,00". Orçado no genérico de cor, '
 'R$ 700. É a primeira cotação a fazer.',
 '⚠ R$ 1.222 · a estrutura de fixação é nossa ou a parede já vem pronta? Está orçada, e '
 'saiu da FOLHA a pedido [Jonathan, 18/11/2026] — não do custo.',
 '⚠ R$ 745 · a ripa de 2 cm entra na coladeira automática? A Base separa "filetagem na '
 'coladeira · R$ 2,50" de "filetagem manual · ripa de 6 mm E O QUE NÃO ENTRA NA MÁQUINA · '
 'R$ 5,00". Orçado como manual.',
 '⚠ o painel é PELE sobre alvenaria, ou a marcenaria faz o volume de 50 de profundidade? '
 'Assumi pele: a prancha diz "sóculo em ALVENARIA" e o nicho é revestido pelo marmorista.',
 '⚠ a prancha pede relevo de 20 mm e cortamos de chapa de 18, que é o padrão da casa. Ou '
 'se aceita 18, ou se lamina — e aí muda.',
 '⚠ RT de 10% é leitura minha: o Jonathan não disse. São pranchas executivas de arquiteto '
 'e a regra da casa é "RT quando há parceiro indicando". Sem RT a MC vai de 26,91% a 35,69%.',
 '⚠ o NOME DO CLIENTE não está em nenhuma das pranchas, e a capa da proposta hoje sai sem ele.',
]


if __name__ == '__main__':
    L = linhas()
    (AQUI / 'planilha.json').write_text(
        json.dumps({ABA: L}, ensure_ascii=False, indent=1), encoding='utf-8')
    cl = fo.classifica(L)
    from collections import Counter
    print('%d linhas · %s' % (len(L), dict(Counter(cl))))
    print('custo direto %.2f · soma dos itens %.2f · diferença %.2f'
          % (T['direto'], sum(T['diretos']), sum(T['diretos']) - T['direto']))
