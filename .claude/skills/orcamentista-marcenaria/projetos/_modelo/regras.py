# -*- coding: utf-8 -*-
"""AS REGRAS DA CASA — as mesmas dezessete do Painel do Michell.

⭐ Elas estão no MOTOR, não na lista: o orçamento as calcula a partir das
  peças, e quem foge delas é a exceção escrita na própria linha. O Painel as
  repete porque quem abre a planilha precisa saber o que já está contado sem
  ter de ler código.
"""
REGRAS = [
 '⛔ NÃO SE USA PINUS PARA NADA [Jonathan, 28/10/2026]. O engradado de '
 'painel virou TRAVESSA DE MDF tirada da própria chapa; o estrado de cama '
 'virou METALON. Não há uma única peça de pinus nos orçamentos da casa.',

 '⛔ NÃO SE USA PULSADOR EM GAVETA. Gaveta abre por CORREDIÇA TOUCH, R$ 500 '
 'o par, e a touch substitui o par de corrediça E o pulsador — ela DOBRA o '
 'custo de abrir, e é o que o senhor pediu. ⭐ Porta de giro e báscula '
 'seguem no pulsador.',

 '⭐ SUPORTE DE PRATELEIRA é jogo de QUATRO por prateleira, R$ 6,50 o jogo. '
 'O motor conta as prateleiras internas de cada móvel e lança sozinho — quem '
 'não leva (prateleira pendurada em haste, divisória que não é prateleira) '
 'tem "sem suporte" escrito na própria linha.',

 '⭐ ALMA DE AÇO em toda prateleira de vão acima de 1,20 m, R$ 50 a barra. '
 '⛔ É contra FLECHA, não contra empeno: 18 mm resolve o empeno e não '
 'resolve o vão.',

 '⭐ PRATELEIRA DE VÃO ACIMA DE 70 cm sai em 18 mm; abaixo disso, 15 mm. É a '
 'regra que decide a espessura em todo o projeto, e por isso o 18 aparece só '
 'onde o vão pede.',

 '⭐ MOLDURA DA MESMA COR DA FRENTE sai em PEÇA INTEIRA de 6 mm usinada na '
 'router, porque régua emendaria e a emenda apareceria. ⛔ MOLDURA DE OUTRA '
 'COR sai em QUATRO RÉGUAS, e régua não entra na coladeira: filetagem '
 'MANUAL, R$ 5,00 o metro, o dobro da automática.',

 '⭐ PALHINHA NATURAL É TAPECEIRO, R$ 650 o m² — NÃO é chapa de MDF. A '
 'frente é MDF com o campo em palhinha e a moldura em régua; a palha não '
 'entra na conta de chapa nem na de fita.',

 '⭐ CAMA LEVA ESTRADO EM METALON, R$ 250 por cama — em TODAS as camas. '
 '⛔ A exceção é onde o senhor pedir QUADRO DE SERRALHEIRO com malha de '
 'cordas náuticas, a R$ 250 o m².',

 '⛔ A CHAPA SE COMPRA EM NÚMERO CHEIO, por COR × ESPESSURA — é a regra de '
 'ferro. Chapa de 275 × 185 com 80% de aproveitamento, e peça inteira até '
 '273, que é a chapa menos o acerto de corte. O que passa de 273 vira '
 'emenda, e toda emenda é decisão de projeto, nunca minha.',

 '⭐ CORTE É DUAS LINHAS: R$ 2,00 por CHAPA comprada e R$ 2,50 por PEÇA '
 'cortada. ⛔ Conta a PEÇA, não a linha do orçamento: uma linha de quatro '
 'prateleiras são quatro peças.',

 '⭐ PERFIL DE PROTEÇÃO DE PISO, R$ 15 o metro linear, em tudo que toca o '
 'chão. É por extensão do móvel, e o motor o lança a partir da medida geral.',

 '⛔ MONTAGEM E FABRICAÇÃO ENTRAM COMO COMISSÃO na aba Preço e Comissões — '
 'NUNCA como dia de marceneiro no custo direto. A equipe é salário fixo: '
 'quem cobra mão de obra no custo direto cobra duas vezes.',

 '⛔⛔ A FRONTEIRA DO ESCOPO, DEFINITIVA [Jonathan, 29/10/2026]. PEDRA NUNCA '
 'É NOSSA — granito, quartzito, mármore, Nanoglass: bancada, sóculo, '
 'frontão, tampo, soleira e peitoril ficam fora do custo E fora da proposta, '
 'e não se lança a linha nem a zero. ⭐ MAS ESPELHO, VIDRO E SERRALHERIA QUE '
 'ESTÃO NA MARCENARIA SÃO NOSSOS: espelho de porta de roupeiro, vidro de '
 'cristaleira, estrado de cama, alma de aço, haste de prateleira. ⭐ O '
 'TESTE: sai no mesmo caminhão e é instalado pela mesma equipe? É nosso. '
 'Existe sem o móvel? Não é. ⛔ E o que é nosso tem de ter LINHA COM VALOR — '
 'linha a zero com promessa de fornecimento na proposta é prometer com o '
 'dinheiro do lucro.',

 '⭐ FRETE É UMA LINHA DO AMBIENTE, R$ 200 a viagem. A QUANTIDADE é a célula '
 'AMARELA no fim do painel de material de cada aba, e ela sai ZERO. Quem '
 'preenche é o senhor — o frete só aparece aqui e no Painel depois disso.',

 '⛔ A FERRAGEM DE MARCA SE CONTA PELO MOTOR, nunca de cabeça. '
 '`planilha.linhas_do_item(mv)` por móvel, somando por chave, UM AMBIENTE '
 'POR PROCESSO (há móveis homônimos entre módulos). ⚠ A corrediça touch '
 'entra por DOIS caminhos: o flag de GAVETAS e a lista OUTRAS. E PORTAS é '
 'folhas × dobradiças POR FOLHA — a quantidade é o produto.',

 '⭐ O ARTICULADOR AVENTOS É DE MOLAS, NÃO A GÁS — calibrado pelo peso da '
 'frente, sem pistão para perder pressão. ⛔ Dizer "articulador a gás" ao '
 'cliente é erro técnico que uma arquiteta derruba na hora.',

 '⭐ GARANTIA ESCALONADA PELA FERRAGEM [Jonathan, 29/10/2026]: linha Blum 30 '
 'anos, linha Hettich 10 anos, Hardt 5 anos, telescópica 2 anos — sobre a '
 'marcenaria. ⛔ Vale o tier MAIS BAIXO presente no projeto: uma telescópica '
 'esquecida derruba a casa inteira. ⚠ Articulador e pulsador Blum não sobem '
 'o tier: quem manda é a dobradiça e a corrediça.',
]
