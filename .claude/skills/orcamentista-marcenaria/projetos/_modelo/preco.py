# -*- coding: utf-8 -*-
"""O que faltava na aba Preço e Comissões: a nota de piso do bloco ⑤ e o
bloco ⑥ inteiro.

⛔⛔ POR QUE ISTO VIROU ARQUIVO [30/10/2026]: o Painel do Michell tem oito
  blocos e a aba Preço tem SEIS. Eu havia parado no ⑤. O ⑥ não é enfeite:
  é onde a aba declara o que ela NÃO faz, e é a única defesa contra alguém
  procurar aqui o que nunca esteve.

⛔ O ⑥ do Michell nomeia os itens que faltavam preço NAQUELE projeto. Isso
  é dado de cliente e não se copia (regra do Jonathan, 29/10). Aqui o texto
  aponta para o bloco O QUE AINDA NÃO TEM PREÇO do Painel, que cada projeto
  preenche com os seus.

⭐ As linhas são as mesmas do Michell, posição por posição:
     70 nota de piso do ⑤ · 72 cabeça do ⑥ · 74 a 78 os cinco parágrafos
"""

PISO = ('⛔ Médio é o PISO, não o zero: todo ambiente custa ao menos cinco '
        'pontos acima da MC alvo do projeto.')

CABECA6 = ('  ⑥ O QUE ESTA ABA NÃO FAZ   ·   para ninguém procurar o que '
           'não está aqui')

PARAGRAFOS = [
    '⛔⛔ O CUSTO DIRETO AINDA É UM PISO. Toda linha lançada a ZERO por '
    'falta de preço na Base aparece na aba do seu ambiente, zerada de '
    'propósito, para gritar — e o Painel as reúne no bloco O QUE AINDA NÃO '
    'TEM PREÇO. ⛔ Enquanto houver zero lá, o preço daqui é o MÍNIMO, nunca '
    'o fechado.',

    '⭐ A MC É ESCOLHIDA, NÃO DESCOBERTA. O método da casa diz: "levantar '
    'todos os custos a fim de se obter uma Margem de Contribuição '
    'específica que lhe é direcionada a cada projeto e nível de '
    'complexidade do projeto TODO ou de um item específico". É por isso que '
    'há duas MC aqui: a do projeto, na célula D7, e o ajuste por ambiente, '
    'na coluna DIFICULDADE do quadro ④. Um ambiente mais difícil carrega MC '
    'maior que o vizinho, e isso é decisão, não conta.',

    '⛔ MONTAGEM E FABRICAÇÃO SÃO COMISSÃO, NUNCA CUSTO DIRETO. A equipe é '
    'salário fixo: lançar dia de montador no custo direto conta a mesma mão '
    'de obra duas vezes. Elas estão na cascata, no degrau do líquido 2, '
    'somando 7,5% com projeto, coordenação e gestão.',

    '⚠ SEPARAR UMA LINHA DA PROPOSTA NÃO É DESCONTÁ-LA. Se o carreto ou a '
    'logística saírem do preço dos móveis e virarem bloco próprio, eles '
    'levam os MESMOS encargos — a nota fiscal, o cartão, o RT e as '
    'comissões caem sobre o faturamento, não sobre "móvel". Repassar a '
    'custo é pagar a NF e o RT do próprio bolso.',

    '⭐ PREÇO DECLARADO NÃO SE MEXE. Esta aba recalcula sozinha quando uma '
    'chapa muda de preço na Base — o que muda é a MC lida, não o preço já '
    'entregue ao cliente.',
]

def linhas(aba='Preço e Comissões'):
    """Duas gravações, porque as colunas diferem — como no Michell:
         B70 a nota de piso · B72 a cabeça do ⑥ · C74:C78 os parágrafos"""
    return [(f'{aba}!B70:B72', [[PISO], [''], [CABECA6]]),
            (f'{aba}!C74:C78', [[p] for p in PARAGRAFOS])]
