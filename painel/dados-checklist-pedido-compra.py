# -*- coding: utf-8 -*-
"""Checklist de informações obrigatórias no pedido de compra — Valvic."""

OBRIGATORIAS = [
 ('01', 'Descrição do item', 'O nome do produto como o fornecedor o chama, não como a gente chama internamente.'),
 ('02', 'Marca / fabricante', 'Quem fabrica. "MDF branco" não é pedido — Duratex, Arauco, Guararapes e Sudati têm branco diferente.'),
 ('03', 'Linha, modelo e código', 'A referência do catálogo do fabricante. É o que elimina a interpretação do vendedor.'),
 ('04', 'Cor e acabamento', 'Nome <b>e</b> código. Fosco, acetinado, brilho, texturizado — o acabamento muda a peça e muda o preço.'),
 ('05', 'Dimensão', 'Espessura, largura, comprimento, diâmetro, curso. Na unidade certa, com a unidade escrita.'),
 ('06', 'Unidade de compra', 'Chapa, metro linear, metro quadrado, rolo, peça, par, jogo, quilo, litro. Nunca "um".'),
 ('07', 'Quantidade', 'Número inteiro na unidade do item 06, com a sobra técnica já considerada.'),
 ('08', 'Destino', 'Obra, cliente ou setor. É o que permite jogar o custo no projeto certo depois.'),
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
  'Tensão · potência por metro · <b>temperatura de cor em kelvin</b> · grau IP · metragem · fonte compatível e sua potência · dimerizável ou não · perfil e difusor'),
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
