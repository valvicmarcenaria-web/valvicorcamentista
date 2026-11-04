# -*- coding: utf-8 -*-
"""O PAINEL, no mesmo layout do que fizemos para o Michell.

⛔⛔ O ERRO QUE ISTO CORRIGE [Jonathan, 30/10/2026]: "esta muuuuuito
  diferente". Estava. Eu havia copiado a PALETA do aba.py — o preto do
  título, o cinza do subtítulo, a régua, o teto dourado — e inventado o
  LAYOUT. Mas layout não é cor: o Painel do Michell tem OITO blocos e o meu
  tinha três. Faltavam a tabela por ambiente com dez colunas, o resumo de
  preço, o quadro de lucro contra o custo fixo dos dias, o que não é
  marcenaria, o que ainda não tem preço e as dezessete regras da casa.

⭐ A estrutura abaixo é a do Michell, linha por linha, lida do CSV exportado
  da própria planilha. O que muda é só o conteúdo: aqui ele nasce vazio.

⛔ As colunas são A..K. A é margem. Na tabela por ambiente:
     B ambiente · C pranchas · D itens · E chapas · F MDF · G fita ·
     H ferragem · I frete · J corte e consumíveis · K custo direto
"""
N_AMB = 20          # ⭐ linhas de ambiente reservadas: 24 a 43
L = {}              # mapa de linha, para quem for formatar depois

def _(*c):
    """Uma linha de 11 colunas, A..K, preenchendo o resto com vazio."""
    return list(c) + [''] * (11 - len(c))

def montar(sub, regras):
    r, V = 1, []
    def add(linha): V.append(linha)
    add(_('  VALVIC MARCENARIA        LEVANTAMENTO DE QUANTITATIVO'))
    add(_('', sub))
    add(_())
    add(_('', '  O CONJUNTO   ·   onde o levantamento está, e o que ele já '
              'permite dizer'))
    add(_())
    add(_('', 'AMBIENTES PRECIFICADOS', '', 'ITENS DE MÓVEL', '',
              'CHAPAS DE MDF', '', 'CUSTO DIRETO LEVANTADO', '',
              'PREÇO DE VENDA'))
    add(_())                                            # 7 · os números
    add(_())
    add(_('', '  ⛔⛔ O PRIMEIRO PASSO DESTA PLANILHA, e sem ele tudo sai '
              '#DIV/0!: abra a aba "Base (importada)" e clique no #REF! da '
              'célula D3, depois em PERMITIR ACESSO. É o Google pedindo '
              'autorização para ligar esta planilha à Base de Custos, e ele '
              'pede uma vez em CADA cópia nova — nenhum script pode dar essa '
              'autorização por nós.   ⭐ DEPOIS DISSO: duplique a aba "00 '
              'Ambiente (modelo)" uma vez por ambiente, renomeie para "01 '
              'Cozinha", "02 Lavanderia" e assim por diante, e acrescente '
              'uma linha aqui embaixo e outra no quadro ④ da aba "Preço e '
              'Comissões" para cada uma.   ⚠ O custo direto é sempre um '
              'PISO enquanto houver linha lançada a zero por falta de preço '
              'na Base: o preço que sai daqui é o MÍNIMO, nunca o fechado.'))
    add(_())
    add(_('', '  ONDE ESTÁ O DINHEIRO   ·   a abertura do que já foi '
              'levantado, não do projeto inteiro'))
    add(_())
    add(_('', 'LINHA', '', '', '', '', 'VALOR', '% DO CUSTO', 'PROPORÇÃO'))
    add(_('', 'MDF — chapa, em número cheio e por cor'))
    add(_('', 'Fita de borda e filetagem'))
    add(_('', 'Ferragem, terceirizados e iluminação'))
    add(_('', 'Frete do projeto · R$ 200 a viagem  '))
    add(_('', 'Corte, consumíveis e embalagem'))
    add(_('', 'CUSTO DIRETO DO LEVANTADO'))
    add(_()); add(_()); add(_())
    add(_('', 'AMBIENTE', 'PRANCHAS', 'ITENS', 'CHAPAS', 'MDF', 'FITA',
              'FERRAGEM', 'FRETE', 'CORTE E CONSUM.', 'CUSTO DIRETO'))
    for _i in range(N_AMB): add(_())                    # 24 a 43
    add(_('', 'TOTAL DO QUE ESTÁ LEVANTADO'))           # 44
    add(_()); add(_()); add(_())
    add(_('', '  O PREÇO DO PROJETO   ·   a conta inteira mora na aba ao '
              'lado, "Preço e Comissões" · aqui fica só o resumo'))
    add(_())
    add(_('', '', '⭐ ESTE QUADRO NÃO SE DIGITA. A margem, as parcelas, o RT '
              'e a comissão do vendedor são escolhidos na aba Preço e '
              'Comissões, nas quatro células amarelas — e cada ambiente '
              'ainda pode levar um ajuste de MC próprio, no quadro ④ de lá, '
              'para quando um deles for mais complexo que o vizinho. '
              '⛔ O custo direto continua sendo um PISO: enquanto houver '
              'linha lançada a zero por falta de preço na Base, o preço '
              'abaixo é o MÍNIMO, nunca o fechado.'))
    add(_())
    add(_('', 'LINHA', '', '', '', '', 'VALOR', 'COMO SE CHEGA'))
    add(_('', 'Custo direto levantado', '', '', '', '', '',
              'soma dos ambientes · é o TOTAL da tabela acima'))
    add(_('', 'MC alvo do projeto', '', '', '', '', '',
              'escolhida na aba ao lado · piso da casa 35%, faixa ideal de '
              '35% a 40%'))
    add(_('', 'Soma dos encargos sobre o preço', '', '', '', '', '',
              'nota fiscal, cartão, margem de erro, serra, manutenção, RT, '
              'vendedor e as cinco comissões internas'))
    add(_('', 'Base do modelo de custo', '', '', '', '', '',
              '1 menos os encargos · é o que sobra do preço para o custo '
              'direto e para a margem'))
    add(_('', 'PREÇO DE VENDA', '', '', '', '', '',
              'custo direto ÷ (base − MC), ambiente por ambiente, somado'))
    add(_('', 'Margem de contribuição em R$', '', '', '', '', '',
              'o que sobra depois do custo direto e de todos os encargos'))
    add(_('', 'MC média realizada', '', '', '', '', '',
              'tem de bater com a alvo quando nenhum ambiente leva ajuste'))
    add(_())
    add(_('  O LUCRO DO PROJETO   ·   a margem paga o custo fixo dos dias '
          'que o projeto ocupa a fábrica?   ·   ⭐ o único campo seu aqui '
          'é DIAS'))
    add(_())
    add(_('', 'LINHA', '', '', '', '', 'VALOR', 'COMO SE CHEGA'))
    add(_('', 'Margem de contribuição do projeto', '', '', '', '', '',
              'o quadro acima: preço menos custo direto e menos todos os '
              'encargos'))
    add(_('', 'Custo fixo da empresa, por mês', '', '', '', '', '',
              '⛔ a preencher · folha mais estrutura, sem investimentos · '
              'pode vir sozinho da N.GESTÃO por IMPORTRANGE'))
    add(_('', 'Custo fixo por dia', '', '', '', '', '',
              'o mês dividido por 30 dias de calendário'))
    add(_('', '⭐ DIAS DE PROJETO', '', '', '', '', '',
              '⭐ ESTE CAMPO É SEU: quantos dias este projeto ocupa a '
              'fábrica, da primeira chapa à última montagem'))
    add(_('', 'Custo fixo alocado ao projeto', '', '', '', '', '',
              'o que a empresa gasta de estrutura enquanto este projeto roda'))
    add(_('', '⭐ LUCRO DO PROJETO', '', '', '', '', '',
              'margem menos o custo fixo dos dias · é o que sobra DE VERDADE'))
    add(_('', '', '⚠⚠ ESTA CONTA ALOCA O CUSTO FIXO INTEIRO AO PROJETO, como '
              'se ele fosse a única coisa na fábrica nos dias digitados. É a '
              'leitura CONSERVADORA, e ela responde à pergunta que importa: '
              '"enquanto este projeto estiver aqui, ele paga a casa?". '
              '⛔ Se três projetos correm juntos, o custo fixo se divide '
              'entre eles e o lucro real deste é MAIOR que o número acima — '
              'o número é um PISO, nunca um teto.'))
    add(_()); add(_()); add(_())
    add(_('', '  O QUE NÃO É MARCENARIA   ·   está na prancha, não está '
              'nesta conta'))
    add(_('', '', '⛔ PEDRA NUNCA É NOSSA: granito, quartzito, mármore, '
              'silestone, Nanoglass — bancada, sóculo, frontão, tampo, '
              'soleira e peitoril'))
    add(_('', '', 'Louças, metais, cubas, torneiras e eletrodomésticos'))
    add(_('', '', 'Revestimentos, pinturas, papel de parede e forro'))
    add(_('', '', 'Mobiliário solto, luminárias, tapetes e cortinas'))
    add(_('', '', 'Box de banheiro em vidro — box existe sem o móvel, e por '
              'isso é do vidraceiro'))
    add(_())
    add(_('  O QUE AINDA NÃO TEM PREÇO   ·   cada um destes pode mexer no '
          'número de cima'))
    add(_('', '', '⛔ Preencher aqui, ambiente por ambiente, o que sair a '
              'ZERO no painel de material de cada aba. Linha com R$ 0,00 é '
              'BURACO CONHECIDO, não item esquecido: o item existe, a '
              'unidade está definida, e o preço falta.'))
    add(_()); add(_())
    add(_('', '  AS REGRAS DA CASA   ·   o que vale em TODO ambiente · ⭐ '
              'estão no MOTOR, não na lista: o orçamento as calcula a partir '
              'das peças, e quem foge delas é a exceção escrita na linha'))
    add(_())
    for i, reg in enumerate(regras, 1):
        add(_('', i, reg))
    return V
