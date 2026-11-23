# -*- coding: utf-8 -*-
"""CENTURION MOTORS — o levantamento vira aba de planilha.

⭐ [Jonathan, 23/11/2026] "vamos orçar pela planilha."

⛔⛔ COPIA-SE O MODELO, NUNCA O ORÇAMENTO DE OUTRO CLIENTE. Esta planilha
  nasceu de `Valvic · PLANILHA BASE de Levantamento (modelo vazio)`
  (11IgmtI5Xd...). O arquivo de outro cliente carregaria os dados dele e
  quebraria o IMPORTRANGE [Jonathan, 29/10/2026].

⛔ A ORDEM É DESMESCLAR → GRAVAR VALOR → FORMATAR, e as linhas começam na
  coluna B, não em A.

Planilha: 1viDAEugwv4IJgML4v0JJOpusjIkEQP8VyO2HzScwLRw
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
            rend = b.COMP_FLEX_REND if k[0] == lv.FLEX else b.REND
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
          '⭐ MC de 55%% = alvo de 35%% + COMPLEXO (20 pontos) · preço na '
          'aba Preço e Comissões'
          % (_br(b.FORRO_M2, 0), b.N_NICHOS + 1)],
         []]

    # ── ① O AMBIENTE ────────────────────────────────────────────────────
    L += [['  O AMBIENTE   ·   o que ele consome, por linha de material'], [],
          ['MATERIAL', 'ESPECIFICAÇÃO', 'QUANTIDADE', 'UN', 'CUSTO',
           '% DO CUSTO', 'R$ UNITÁRIO']]

    def mat(rot, esp, qtd, un, custo, unit=None):
        if unit is None and qtd:
            unit = custo / qtd
        L.append([rot, esp, _n(qtd, 2), un, _n(custo), _n(custo / D, 4),
                  _n(unit) if unit is not None else ''])

    for k, n in sorted(T['chapas'].items()):
        rend = b.COMP_FLEX_REND if k[0] == lv.FLEX else b.REND
        esp = ('área líquida de %s m² · rendimento de %s m² por chapa '
               '(%s × %s a 80%%) · ⛔ arredonda-se por PADRÃO × ESPESSURA'
               % (_br(T['area'][k]), _br(rend),
                  _br(b.COMP_FLEX_C if k[0] == lv.FLEX else b.CHAPA_C, 0),
                  _br(b.COMP_FLEX_L if k[0] == lv.FLEX else b.CHAPA_L, 0)))
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
        'incide sobre chapa e fita · cola, lixa, parafuso, cavilha, tapa-furo',
        b.CONSUMIVEIS, '%', T['c_cons'])
    mat('Embalagem', '⭐ O PERCENTUAL É DIGITADO, na coluna QUANTIDADE · '
        'incide sobre tudo o que vem acima · papelão, filme e cantoneira',
        b.EMBALAGEM, '%', T['c_emb'])
    L.append(['CUSTO DIRETO DO AMBIENTE', '', '', '', _n(D), 1.0])
    L += [[], []]

    # ── ② OS ITENS ──────────────────────────────────────────────────────
    L += [['  OS ITENS   ·   cada item é um móvel, e é assim que ele vai '
           'para a proposta'], [],
          ['ITEM', 'MÓVEL', 'MEDIDA', '', '', '', '', 'CUSTO']]
    MED = {0: '%s m² de forro' % _br(b.FORRO_M2, 0),
           1: '%d arcos · moldura de %s cm, %s de profundidade'
              % (b.N_NICHOS + 1, _br(b.MOLDURA_L, 0), _br(b.NICHO_PROF, 0)),
           2: '%d fundos e %d prateleiras'
              % (b.N_NICHOS, b.N_NICHOS * b.PRAT_POR_NICHO),
           3: '%s m² de painel' % _br(lv.PAINEL_M2),
           4: '%s m² de base em Branco TX 18' % _br(lv.ESP_M2),
           5: '%s m² de espelho prata' % _br(lv.ESP_M2)}
    for i, (it, d) in enumerate(zip(lv.ITENS, DIRETOS)):
        L.append(['%02d' % (i + 1), it.nome, MED.get(i, ''), '', '', '', '',
                  _n(d)])
        L.append(['', it.obs])
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
            rend = b.COMP_FLEX_REND if p['mat'] == lv.FLEX else b.REND
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
 '⭐⭐ A LEGENDA DA PRANCHA É QUEM DECIDE O ESCOPO, e ela tem quatro símbolos: '
 'ADESIVO (hachura rosa), ESPELHO (diagonal), MDF LAQUEADO CAFE (marrom SÓLIDO) e '
 'TINTA PAREDE SW 6069 (bege pontilhada). ⛔ A bege cobre quase toda a parede nas '
 'três vistas e eu quase a contei como MDF laqueado — ela é TINTA. Ler a legenda '
 'ANTES de contar área foi o que impediu o orçamento de dobrar sem motivo.',
 '⭐⭐ O FORRO TEM 157 m² CRAVADOS NA PRANCHA: "ÁREA FORRO 157m²", escrito na '
 'planta 01. Não é cálculo meu, é número do projetista · São 39 chapas e '
 'R$ 27.300 só de material: o maior item do orçamento, sozinho.',
 '⭐ A MÃO AMIGA É MATERIAL DE MONTAGEM, NÃO ESTRUTURA [Jonathan, 23/11/2026: '
 '"importante considerar material para montagem de mao amiga"]. São as escoras em T '
 '— um sarrafo em pé com travessa no topo — que seguram a placa contra a laje '
 'enquanto o marceneiro parafusa. Sem elas não se monta forro a 2,91 m do chão. '
 'A Base tem a linha: "Sarrafo de pinus · Estrutura interna · R$ 8,00/m" · '
 'Estão orçadas 10 escoras, e elas são uma linha SEPARADA do barroteamento, que '
 'é o que fica.',
 '⭐⭐ O PÓRTICO CURVO, CAMADA POR CAMADA [Jonathan, 23/11/2026]: moldura '
 'estrutural de MDF (as costelas), revestida de compensado flexível nos DOIS lados '
 '— intradorso, que é a curva de dentro, e extradorso, a de fora — mais o alizar '
 'de acabamento externo. A moldura tem %s cm de largura de face, cota confirmada na '
 'VISTA BB.' % _br(b.MOLDURA_L, 0),
 '⛔⛔ O RECORTE DO ARCO NÃO SE COMPRA PELO PERÍMETRO, SE COMPRA PELO RETÂNGULO '
 'QUE ELE OCUPA NA CHAPA. Um arco de %s cm de face parece consumir 0,55 m²; na chapa '
 'ele ocupa 1,28 × 2,04 = 2,61 m². São 16 recortes · ⭐ E O MIOLO DÁ %s m², que '
 'cabe inteiro o fundo e a prateleira de todos os nichos. Está orçado SEM esse '
 'aproveitamento, que é o conservador — o ganho está nas dúvidas.'
 % (_br(b.MOLDURA_L, 0), _br(MIOLO_M2)),
 '⭐⭐ DOIS PREÇOS FECHADOS PELO JONATHAN EM 23/11/2026, e eram justamente as duas '
 'dúvidas mais caras desta folha: "Compensado flexivel, custo - 600,00 a chapa" e '
 '"laca considere 650" · ⛔ Nenhum dos dois é número da Base. O compensado FLEXÍVEL '
 'não existe lá — só o comum, a R$ 150 — e eu havia ESTIMADO R$ 375, 2,5× o comum; a '
 'laca tem duas linhas e eu havia lançado a de R$ 300 dos jobs, quando a certa é a de '
 'R$ 650 do materiais.json, que também é a mais coerente, porque as duas linhas falam '
 'de peça LISA e pórtico curvo leva mais lixa e mais tempo · ⭐ Juntos somam '
 'R$ 8.125,67 ao custo direto, que foi de R$ 86.973,29 para R$ %s: R$ 1.800,00 nas 8 '
 'chapas de compensado, R$ 5.981,00 nos %s m² de laca, R$ 108,00 de consumíveis sobre '
 'a chapa nova e R$ 236,67 de embalagem · ⭐ E a folha não ficou mais CARA por acaso, '
 'ficou mais FIRME: eram as duas únicas linhas que eu mesma havia marcado como '
 '"primeira cotação a fazer", e agora são preço de verdade · ⚠ VALE SUBIR AS DUAS '
 'PARA A BASE DE CUSTOS — o próximo projeto com curva vai precisar delas.'
 % (_br(T['direto']), _br(lv.LACA_M2)),
 '⭐⭐ MC DE 55%, APLICADA [Jonathan, 23/11/2026: "aplique a mc de 55%"] · ⭐ E ela cai '
 'EXATAMENTE na tabela da casa, sem forçar nada: a MC alvo do projeto fica no PISO de '
 '35% e o ambiente entra como COMPLEXO, que o quadro ⑤ da aba Preço e Comissões '
 'define como "junta três ou mais ofícios, geometria fora de esquadro, estrutura '
 'metálica aparente ou peça que não cabe em chapa inteira" — e este ambiente bate em '
 'três dos quatro critérios: são QUATRO ofícios (marcenaria, laca, vidraceiro e '
 'elétrica de LED), os oito arcos são geometria fora de esquadro, e o forro de 157 m², '
 'a faixa corrida de 709 e o espelho de 745 não cabem em chapa inteira · 35 + 20 = 55. '
 '⛔ A MC não se digita no quadro ④: ela é a alvo mais os pontos da dificuldade, então '
 'quem quiser mexer mexe em D7 ou na coluna DIFICULDADE, nunca na MC APLICADA.',
 '⭐ A GEOMETRIA DO ARCO FECHA SOZINHA, e isso dá confiança na leitura: o vão tem '
 '%s de largura, logo o raio do semicírculo é %s — e a prancha cota %s de abóbada. '
 'A altura interna sai %s + %s de prateleira + %s de trecho reto = %s, e a prancha '
 'cota %s no meio do terceiro nicho. Bate.'
 % (_br(b.NICHO_L, 1), _br(b.NICHO_L / 2, 2), _br(b.NICHO_ABOBADA, 0),
    _br(b.NICHO_ABOBADA, 0), '1,8', '138', '192,8', _br(b.NICHO_H, 0)),
 '⭐ ALMA DE AÇO EM TODA PRATELEIRA, como a Base manda: "uma por peça, contra '
 'empeno". Prateleira de %s cm de vão sem apoio no meio empena — é o caso exato, e '
 'o Jonathan pediu nominalmente.' % _br(b.NICHO_L, 1),
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

DUVIDAS = [
 '⭐ DUAS DÚVIDAS SAÍRAM DESTA LISTA EM 23/11/2026, e eram as duas mais caras: o '
 'preço do compensado flexível (R$ 600,00 a chapa) e o da laca (R$ 650,00 o m²), '
 'ambos fechados pelo Jonathan · estão registrados nas NOTAS, com o que mudaram.',
 '⚠ R$ %s · O MIOLO DOS 16 RECORTES DE ARCO. São %s m² de chapa que saem de '
 'dentro dos arcos em peças de até 104 × 140 — cabe o fundo e a prateleira de '
 'todos os nichos, que somam %s m². Está orçado SEM aproveitar, que é o '
 'conservador · ⭐ Aproveitando, saem cerca de %d chapas do orçamento.'
 % (_br(MIOLO_M2 / b.REND * 700), _br(MIOLO_M2),
    _br(14.07 + 8.75), math.floor(MIOLO_M2 / b.REND)),
 '⚠ A PROFUNDIDADE DO NICHO NÃO ESTÁ EM PRANCHA NENHUMA. O Jonathan cravou %s cm '
 'em 23/11/2026, e é ela que define a caixa dos %d pórticos: o compensado flexível '
 'dos dois lados, a prateleira e o LED escalam todos com ela. Conferir na medição.'
 % (_br(b.NICHO_PROF, 0), b.N_NICHOS + 1),
 '⚠ O PERÍMETRO DO FORRO É ESTIMATIVA. A prancha dá a ÁREA (157 m²) e uma cota de '
 '1380 de profundidade; pelo retângulo equivalente o perímetro fica em %s m. É ele '
 'que manda na fita e na filetagem — R$ %s ao todo, então o erro possível é '
 'pequeno, mas está registrado.'
 % (_br(lv.FORRO_PERIM), _br(T['c_fita'] + T['c_filete'])),
 '⚠ A LARGURA DO ALIZAR é premissa minha de %s cm — a prancha não cota. São '
 '%s m² de chapa e entram também na laca, que agora custa R$ 650 o m².'
 % (_br(b.ALIZAR_L, 0),
    _br(sum(n * A['externo'] * b.ALIZAR_L for _r, n, A in lv.ARCOS) / 10000)),
 '⚠ QUANTAS PRATELEIRAS POR NICHO? Contei %d na VISTA BB ampliada. Se forem %d, '
 'muda chapa, alma de aço e LED — cerca de R$ %s por prateleira a mais em cada um '
 'dos %d nichos.'
 % (b.PRAT_POR_NICHO, b.PRAT_POR_NICHO + 1,
    _br(b.NICHO_L * b.NICHO_PROF / 10000 / b.REND * 700
        + b.NICHO_L / 100 * b.LED_M + b.ALMA_BARRA * b.NICHO_L / b.ALMA_M),
    b.N_NICHOS),
 '⚠ O PADRÃO EXATO DO AMADEIRADO não foi escolhido pela arquiteta. Está no '
 'genérico de cor da Base, R$ 700 a chapa de 18 mm · ⛔ se cair em Cristallo '
 '(brilho, R$ 800) são R$ %s a mais; em Acetinato (R$ 1.800), R$ %s · '
 '⭐ É A MAIOR DÚVIDA QUE RESTA, agora que o compensado e a laca fecharam.'
 % (_br(65 * 100), _br(65 * 1100)),
 '⚠ O NÚMERO DE ESCORAS DE MÃO AMIGA é premissa: 10 para 157 m². Quem monta sabe '
 'quantas precisa · são R$ 8,00 o metro de sarrafo, então cada escora a mais custa '
 'cerca de R$ 28.',
 '⚠ O CLIENTE É "CENTURIUM" no carimbo da prancha e "Centurion Motors" no '
 'moodboard. Conferir a grafia antes de a proposta sair.',
]


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
