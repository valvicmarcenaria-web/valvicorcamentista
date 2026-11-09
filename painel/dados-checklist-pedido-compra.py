# -*- coding: utf-8 -*-
"""Checklist de informações obrigatórias no pedido de compra — Valvic."""

OBRIGATORIAS = [
 ('01', 'Descrição do item', 'O nome do produto como o fornecedor o chama, não como a gente chama internamente.'),
 ('02', 'Marca / fabricante', 'Quem fabrica. "MDF branco" não é pedido — Duratex, Arauco, Guararapes e Sudati têm branco diferente.'),
 ('03', 'Cor e acabamento', 'Nome <b>e</b> código. Fosco, acetinado, brilho, texturizado — o acabamento muda a peça e muda o preço.'),
 ('04', 'Dimensão', 'Espessura, largura, comprimento, diâmetro, curso. Na unidade certa, com a unidade escrita.'),
 ('05', 'Unidade de compra', 'Chapa, metro linear, metro quadrado, rolo, peça, par, jogo, quilo, litro. Nunca "um".'),
 ('06', 'Quantidade', 'Número inteiro na unidade do item 05, com a sobra técnica já considerada.'),
 ('07', 'Destino', 'Obra, cliente ou setor. É o que permite jogar o custo no projeto certo depois.'),
 ('08', 'Iluminação: kelvin e voltagem',
  'Havendo qualquer tipo de iluminação, <b>temperatura de cor em kelvin e voltagem são obrigatórias</b>. Sem elas, não compre.'),
]

EXEMPLOS = [
 ('MDF',
  'MDF <b>Noce Amêndoa</b> Duratex · acabamento texturizado · <b>18 mm</b> · duas faces · '
  'chapa de 2.750 × 1.840 mm · <b>6 chapas</b> · obra Attos, cozinha'),
 ('Fita de borda',
  'Fita de borda Duratex <b>Noce Amêndoa</b> — mesma cor e mesmo código da chapa · '
  '<b>22 mm</b> de largura · 0,45 mm de espessura · rolo de 50 m · <b>2 rolos</b> · obra Attos, cozinha'),
 ('Corrediça',
  'Corrediça oculta <b>Hettich</b>, com Silent System e extração total · acabamento zincado · '
  '<b>500 mm</b> de curso · carga de <b>30 kg</b> · unidade: par · <b>8 pares</b> · obra Attos, rack da sala de TV'),
 ('Vidro',
  'Vidro <b>Reflecta fumê</b> · <b>4 mm</b> · 580 × 1.140 mm · lapidado nas quatro faces · '
  'sem furação · temperado · unidade: peça · <b>2 peças</b> · obra Attos, aéreo da cozinha'),
]

CABECALHO = [
 'Fornecedor, CNPJ e contato de quem atendeu',
 'Número do pedido e data',
 'Quem solicitou e quem autorizou',
 'Prazo de entrega acordado, com data',
 'Endereço de entrega — fábrica ou obra',
 'Frete incluso ou por conta de quem, e com qual valor',
 'Forma e prazo de pagamento',
 'Condição de devolução de sobra ou peça errada',
]

FAMILIAS = [
 ('Chapa · MDF, MDP, compensado',
  'Fabricante · padrão e código da cor · espessura em mm · <b>uma ou duas faces</b> · dimensão da chapa · substrato · BP ou laminado'),
 ('Fita de borda',
  'Fabricante · cor e código <b>idênticos aos da chapa</b> · largura em mm · espessura (0,45 · 1,0 · 2,0) · metragem do rolo · com ou sem cola'),
 ('Ferragem de movimento',
  'Fabricante · linha e código · acabamento · curso ou comprimento · <b>capacidade de carga</b> · ângulo de abertura · amortecimento · unidade em peça, par ou jogo'),
 ('Puxador e metais',
  'Fabricante · modelo · acabamento · <b>medida entre furos</b> · comprimento total · quantidade'),
 ('Iluminação em LED',
  '<b>Voltagem</b> · potência por metro · <b>temperatura de cor em kelvin</b> · grau IP · metragem · fonte compatível e sua potência · dimerizável ou não · perfil e difusor'),
 ('Vidro e espelho',
  'Tipo (reflecta, incolor, fumê, bronze) · espessura · medida final · <b>lapidação ou bisotê</b> · furação · temperado ou comum'),
 ('Tinta, laca e verniz',
  'Fabricante · linha · <b>código da cor</b> · acabamento · base · catalisador e diluente · rendimento · quantidade em litros'),
 ('Insumo e abrasivo',
  'Fabricante · tipo · granulometria ou medida · formato · quantidade por caixa ou rolo'),
 ('Serviço de terceiro',
  'O que será feito · medida · prazo · local · <b>se o material é nosso ou dele</b> · quem recebe e confere'),
]

CONFERIR = [
 'A cor da fita confere com a cor da chapa, fabricante incluído?',
 'A espessura pedida é a do projeto, não a do hábito?',
 'A quantidade considera a sobra técnica e o que já há em estoque?',
 'O prazo de entrega cabe na data de produção da obra?',
 'O item tem código do fabricante, ou está descrito por adjetivo?',
 'Alguém além de quem pediu leu o pedido antes de enviar?',
]

ERROS = [
 ('"Branco" sem fabricante', 'Cada fábrica tem o seu. Chapa e fita de marcas diferentes não combinam na peça montada.'),
 ('Ferragem sem carga', 'Gaveta de 30 kg com corrediça de 15 kg é retrabalho na casa do cliente, não na fábrica.'),
 ('LED sem temperatura de cor', 'Dois ambientes com kelvin diferente aparecem lado a lado e não têm conserto depois de instalado.'),
 ('Quantidade sem unidade', 'Dez de fita pode virar dez metros ou dez rolos. Um dos dois para a produção.'),
]
