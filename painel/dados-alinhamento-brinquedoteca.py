# -*- coding: utf-8 -*-
"""Alinhamento técnico da brinquedoteca Eliza & Luiz Gustavo.

Extraído da proposta comercial. Toda informação negocial — valores, prazos,
condições de pagamento, validade e garantia — foi removida de propósito:
este documento vai para a produção cruzar com o projeto executivo.
"""

OBRA = dict(
    cliente  = 'Eliza & Luiz Gustavo',
    objeto   = 'Brinquedoteca',
    projeto  = 'Helena Antunes Arquitetura e Interiores',
    oficios  = 'Serralheria · marcenaria · estofaria · pintura automotiva · instalação',
)

SISTEMAS = [
 ('Infraestrutura metálica', [
   'Paredes sobem sobre <b>metalon 50 × 30 em chapa 16</b> — chapa mais grossa que a de divisória comum, escolhida por resistência e segurança.',
   'Atenção reforçada onde ficam a <b>ponte suspensa</b> e a <b>grade de cordas suspensa</b>.',
   'Estrutura de aço recebe <b>pintura automotiva em cabine</b> — a mesma aplicada em carroceria.',
 ]),
 ('Malha de corda', [
   '<b>Corda náutica de 8 mm</b>, tecida <b>nó a nó</b> — não é tela de rede.',
   '<b>10 cm entre nós.</b>',
   'Fios de <b>cabo de aço de 3 mm entrelaçados</b> para resistência.',
   'Na <b>estrutura suspensa a malha é dupla</b>, reduzindo o vão entre nós pela metade.',
   'Fixação por <b>ganchos soldados</b> — nunca por amarração.',
   'Inclui a <b>rede do mezanino</b>.',
 ]),
 ('Amortecimento', [
   'Cada uso pede uma espuma distinta: a que afunda na piscina, a que sustenta no degrau, a que absorve na parede.',
   '<b>Espuma de alta densidade</b> nas plataformas de subida e no painel de guarda-corpo da piscina.',
   '<b>D33 de 20 mm</b> nas plataformas acolchoadas — parte superior e curva.',
   '<b>D33 de 45 mm</b> na almofada do assento do banco extenso.',
   '<b>Piso emborrachado de 20 mm</b> na piscina de espuma.',
   'Revestimento em <b>tecido a definir com a cliente</b>. <b>Couro natural não está contemplado.</b>',
 ]),
 ('Superfície', [
   '<b>MDF ultra premium cru</b>, entregue <b>plano e alinhado</b>, pronto para o acabamento.',
   'Banco extenso em <b>MDF melamínico</b> — cor sugerida: padrão <b>Tabasco da Berneck</b>. É sugestão, sujeita a confirmação ou troca.',
 ]),
 ('Acabamento de fábrica', [
   'Janelas e pórticos em <b>laca branca</b>, com <b>friso</b> e <b>usinagem plana no estilo veneziana</b>.',
   'Painéis entregues crus, planos e alinhados — a pintura acrílica e o papel são aplicados por nós, com material da cliente.',
 ]),
]

CONJUNTOS = [
 ('01', 'Passarela suspensa', 'Estrutura em aço com pintura automotiva.'),
 ('02', 'Gradis de contenção',
  'Quadro metálico com corda de alma em aço. Malha de corda náutica de 8 mm com 10 cm entre nós e fios de cabo de aço de 3 mm entrelaçados. Na estrutura suspensa a malha é dupla. Fixada com ganchos soldados. Inclui a rede do mezanino.'),
 ('03', 'Plataformas acolchoadas',
  'Estrutura em serralheria revestida em compensado, pontas curvas, espuma D33 de 20 mm na parte superior e na curva, revestimento completo em tecido.'),
 ('04', 'Piscina de espuma',
  'Estrutura de contenção, fundo e paredes acolchoados, piso emborrachado de 20 mm.'),
 ('05', 'Banco extenso',
  'Estrutura em MDF melamínico — sugestão de cor: padrão Tabasco da Berneck. Assento com almofada em espuma D33 de 45 mm, revestida em tecido a definir.'),
 ('06', 'Parede norte',
  'Estrutura em aço e MDF ultra premium cru, pronto para o efeito tijolinho. <b>O efeito de tijolinho não é nosso.</b>'),
 ('07', 'Casinha — paredes', 'Fachada e laterais em MDF ultra premium cru.'),
 ('08', 'Casinha — escada', 'MDF ultra premium, com os degraus em revestimento emborrachado.'),
 ('09', 'Janelas e pórticos moldurados',
  'Estilo veneziana em usinagem plana, com frisos, em laca branca. Inclui a placa decorativa personalizada e os nichos da parede de tijolinhos.'),
 ('10', 'Escorregador com túnel curvo',
  'Teto em arco sobre gabarito, pista em laminado e gradil de proteção.'),
 ('11', 'Toldo personalizado', 'Sob medida, em lona, com estrutura tubular e fixação.'),
 ('12', 'Pintura ou papel de parede — aplicação',
  'Mão de obra da pintura acrílica dos painéis, por dentro e por fora, ou da aplicação de vinil adesivo e papel na torre. <b>O material é fornecido pela cliente.</b>'),
 ('13', 'Cozinha de brinquedo', 'Módulo lúdico sob medida, em MDF ultra premium cru.'),
]

ACOMPANHA = [
 'Projeto executivo', 'Estrutura metálica em chapa 16', 'Chapas', 'Espumas', 'Tecidos',
 'Cordas e malha de corda náutica', 'Rede do mezanino', 'Laca das janelas',
 'Pintura automotiva', 'Transporte', 'Montagem',
]

NAO_INCLUSO = [
 'Blocos de espuma da piscina', 'Base imantada', 'Conjunto de mesas com cadeiras', 'Balanço',
 'Material de pintura e de vinílicos — tinta, massa, vinil e papel',
 'Revestimento de piso interno da casinha', 'Couro natural em qualquer revestimento',
 'O efeito de tijolinho da parede norte',
 'Obra civil, elétrica, piso e revestimentos do ambiente',
]

A_DEFINIR = [
 ('Tecido dos acolchoados', 'A definir com a cliente. Couro natural está fora do escopo.'),
 ('Cor do banco extenso', 'Tabasco da Berneck é sugestão — confirmar ou trocar com a cliente.'),
 ('Conferência de medidas no local', 'As medidas são conferidas no local <b>antes</b> da fabricação.'),
 ('Pintura acrílica e papel da torre', 'Mão de obra nossa; tinta, massa, vinil e papel vêm da cliente.'),
]
