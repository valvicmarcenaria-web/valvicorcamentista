# -*- coding: utf-8 -*-
"""Escopo de venda — Attos Henrique Salles · Costa Laguna.

Fonte: contrato de prestação de serviços de 06/11/2026 (14 itens em 7
ambientes + cortesia, R$ 164.000,00) e a proposta de marcenaria linha
Hettich de novembro de 2026. Projeto executivo Costa Laguna ATTOS Rev. 03.
"""

OBRA = dict(
    cliente  = 'Attos Henrique Salles',
    obra     = 'Costa Laguna · Alphaville Lagoa dos Ingleses, Nova Lima',
    projeto  = 'Executivo Costa Laguna ATTOS · Rev. 03',
    escopo   = '14 itens em 7 ambientes + cortesia',
)

PRAZOS = [
 ('Medição técnica', 'Até 7 dias corridos após a assinatura (06/11/2026)'),
 ('Entrega geral', '70 dias corridos contados da medição — não da assinatura'),
 ('Escritório', 'Instalado até 10/12/2026, independentemente do prazo do restante'),
 ('Garantia', '10 anos marcenaria e ferragem de movimento · 2 anos instalação e regulagem · LED pelo fabricante'),
]

ESCRITORIO = [
 ('Prazo fora do cronograma',
  'O escritório é <b>contratual para 10/12/2026, instalado</b>. Não entra na fila dos 70 dias — '
  'produção, carga e instalação precisam de janela própria.'),
 ('Divergência entre o 3D e o projeto técnico',
  'O render do anteprojeto e o executivo <b>não batem neste ambiente</b>. '
  'Resolver a divergência antes de detalhar; nada corta até ela estar fechada.'),
 ('Fixação da pedra',
  'A bancada avança em mesa com apoio metálico. <b>Alinhar o método de fixação da pedra com a marcenaria</b> '
  'junto à marmoraria — a pedra é fornecimento de terceiro, o apoio é nosso.'),
]

ITENS = [
 ('Cozinha', 'Painel ripado do corredor', 'Duas portas pivotantes (vestiário e despensa) girando dentro do painel — fechadas, viram ripa'),
 ('Cozinha', 'Cristaleira', 'Portas de vidro reflecta, perfil, prateleiras e nicho inferior'),
 ('Cozinha', 'Armário superior com portas de vidro', 'Sobre a bancada existente · altura livre fecha na medição'),
 ('Cozinha', 'Coluna de eletrodoméstico', 'De piso a teto, com vão de forno e micro-ondas'),
 ('Escritório', 'Painel ripado de fundo', 'Parede inteira do fundo, na mesma cadência da casa'),
 ('Escritório', 'Armário superior, bancada e armário inferior', 'Bancada corre sobre o armário e avança em mesa, com apoio metálico na ponta · armário inferior com gaveteiro'),
 ('Sala de TV', 'Painel ripado com duas portas de manutenção', 'Acesso ao quadro de energia e à rede hidráulica · portas mimetizadas na ripa · pulsador apenas se necessário'),
 ('Sala de TV', 'Painel liso', 'Recebe a televisão, em continuidade com o ripado, sem fio aparente entre eles'),
 ('Sala de TV', 'Rack de TV suspenso', 'Gavetões sobre corrediça oculta, atravessando a junção dos dois painéis'),
 ('Suíte', 'Parede painelada da TV', 'Painel de ponta a ponta com as duas portas mimetizadas · puxador em cava usinada na própria peça'),
 ('Suíte', 'Painel ripado da cabeceira', 'O ripado sobe atrás da cama'),
 ('Suíte 01', 'Cabeceira estofada', 'Base de MDF, espuma e revestimento · fecha a medida na medição'),
 ('Hall', 'Painel do hall', 'Porta da lavanderia mimetizada no painel · bit de canto'),
 ('Jantar', 'Aparador suspenso', 'Portas de giro e gaveta interna, suspenso do piso'),
 ('Hóspedes', 'Painel liso · CORTESIA', 'À direita do ar-condicionado · mesmo padrão dos painéis da casa · fecha a medida na medição'),
]

FERRAGENS = ('Corrediça oculta Hettich com Silent System e extração total, até 30 kg por gaveta · '
             'dobradiça Hettich Sensys com amortecimento integrado e regulagem nos três sentidos · '
             'sistema pivotante nas portas do corredor · pulsador Blum TIP-ON nas portas de manutenção da sala de TV <b>apenas se necessário</b> · '
             'puxador em cava usinada na suíte e no hall')

ESTRUTURA = ('MDF em padrões a definir entre as partes · caixaria 15 mm, fundos 6 mm, portas, frentes e prateleiras '
             'com vão acima de 70 cm em 18 mm · vidro reflecta · iluminação em LED embutida · estofado da cabeceira')

FORA = ('<b>Pedra:</b> painel de travertino do jantar, bancadas, soleiras e peitoris — marmoraria. '
        '<b>Eletrodomésticos, metais e obra:</b> cooktop, forno, coifa, cubas, torneiras, alvenaria, elétrica, forro, piso e pintura. '
        '<b>Retirados nesta versão:</b> armário do gourmet, painel liso e cabeceira estofada da suíte, mesas de cabeceira e painel da rouparia.')

DEFINIR = [
 ('Cores e padrões de MDF',
  'O contrato traz "MDF nos padrões que serão definidos entre as partes". <b>Definir as cores de toda a casa com o cliente</b> antes de comprar chapa.'),
 ('Perfil de alumínio na base dos painéis',
  'Definir o perfil de proteção da base. <b>Levar ao cliente uma ou mais soluções em protótipo</b> — decisão apresentada, não descrita.'),
 ('Portas pivotantes da cozinha',
  'Alinhar o <b>modelo de fechadura</b> e estruturar o <b>puxador na própria ripa</b>, de preferência sem avançar para a frente da peça.'),
 ('Portas de manutenção da sala de TV',
  'São <b>duas portas simples</b>, não estrutura de porta de passagem, para acesso ao quadro de energia e à hidráulica. <b>Esconder o transpasse da porta entre as ripas.</b> Pulsador <b>apenas se necessário</b>.'),
 ('Ponto de alimentação do LED da cozinha',
  '<b>Salientar com o cliente</b> a necessidade de dispor do ponto de alimentação. Sem ele, não há iluminação na entrega.'),
 ('Dobradiça e vidro da cozinha',
  'Aéreo da cozinha: <b>dobradiça black Bigfer</b> e <b>vidro Reflecta fumê</b>.'),
 ('Painel de TV da suíte',
  'Ficou alinhado com o cliente que a <b>porta abre para o lado direito</b>. Projetar isso para o cliente validar, e <b>validar também a largura da porta</b>.'),
 ('Medidas que fecham na medição',
  'Cabeceira da suíte 01, painel do quarto de hóspedes, altura livre sob o aéreo da cozinha e a posição das portas de manutenção da sala de TV.'),
]
