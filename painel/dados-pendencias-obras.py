# -*- coding: utf-8 -*-
"""Pendências de obra levantadas pelo Jonathan em 27/10/2026.

Fonte única: o relato do Jonathan. Nada aqui é inferido — datas foram apenas
convertidas de "hoje / amanhã / quinta" para o calendário.
"""

# (data, o que fazer, detalhe, tipo)   tipo: '' | 'crit' | 'dev'
OBRAS = [
 ('Jairo', 'Em execução', '', [
   ('27/10', 'Fixação do estofado na estrutura da cabeceira', '', ''),
   ('27/10', 'Tingimento da peça de madeira', '', ''),
   ('28/10', 'Reinstalação e finalização', '', ''),
 ]),
 ('Ana Carolina', 'Em execução', 'Cronograma alinhado com a cliente conforme comunicado pelo Deivison.', [
   ('27/10', 'Confirmar se as pendências são de fato apenas estas três',
    'Rodapé de alumínio · prateleiras do quarto do Vitor · led. Qualquer item fora desta lista, avisar antes de seguir.', 'dev'),
   ('28/10', 'CONFERIR as medidas do gaveteiro — validar se passa no vão da porta do cômodo',
    'Marcado como IMPORTANTE pelo Jonathan. Conferir antes de produzir ou de levar a peça.', 'crit'),
   ('29/10', 'Led — concluir', 'Agendado para conclusão na quinta.', ''),
   ('—',     'Rodapé de alumínio', '', ''),
   ('—',     'Prateleiras do quarto do Vitor', '', ''),
   ('—',     'Revestir os gaveteiros atuais e transformar em duas cômodas — SERVIÇO AUTORIZADO',
    'Rodízios industriais ocultos; dois deles com freio, com acesso na parte de trás.', ''),
   ('28/10', 'Devolver ao Jonathan: previsão de entrega das duas cômodas', '', 'dev'),
 ]),
 ('Simony', 'Agendada', '', [
   ('30/10', 'Reinstalação da bancada da Duda', 'Sexta, às 8:30.', ''),
   ('30/10', 'Acabamento do batente da porta da sala', 'Mesma ida de sexta, 8:30.', ''),
   ('30/10', 'Medir o espaço da sapateira', 'Alinhar com a cliente.', ''),
 ]),
 ('Leonardo', 'Em execução', 'Equipe de pintura entra na obra de segunda a quarta, 02 a 04/11.', [
   ('30/10', 'Marceneiro finalizar a obra', 'Requerido do marceneiro: até sexta.', ''),
   ('05/11', 'Levar as peças soltas — mesas, gaveteiros e nichos das plantas',
    'Alinhado com o cliente. Vão na quinta porque a pintura ocupa a obra de 02 a 04/11.', ''),
 ]),
 ('Rejane', 'Em pintura', 'Previsão de aproximadamente 10 dias para finalizar após a liberação da pintura.', [
   ('28/10', 'Liberar a pintura das peças', '', ''),
   ('07/11', 'Finalização após a pintura', 'Previsão de ~10 dias a contar de 28/10.', ''),
   ('28/10', 'Devolver ao Jonathan: dá para projetar entrega com a cliente em 15/11?',
    'Atenção: 15/11/2026 é domingo e feriado nacional. As opções úteis em volta são sexta 13/11 ou segunda 16/11.', 'dev'),
 ]),
 ('Juliana', 'Agendada', '', [
   ('04/11', 'Conclusão da obra', 'Alinhado para a quarta-feira.', ''),
 ]),
 ('Graciene', 'Agendada', '', [
   ('05/11', 'Entrega', 'Entrega alinhada para 05/11.', ''),
 ]),
 ('Andrea', 'Sem data', '', [
   ('28/10', 'Devolver ao Jonathan: projeção de entrega',
    'Financeiramente o ideal é entregar até 13/11 (sexta), se for possível. Se não couber, informar a data real.', 'dev'),
 ]),
 ('Cristiane · lâmina', 'Travada', 'A contagem do prazo só começa depois da medição — e a medição depende dos dois itens abaixo.', [
   ('—', 'Aguardando definição do eletro da área gourmet', '', ''),
   ('—', 'Aguardando remoção do móvel da sala para medição', '', ''),
   ('—', 'Prazo informado à cliente: 50 dias corridos APÓS a medição', '', ''),
 ]),
 ('Nadia', 'Em definição', '', [
   ('—', 'Em definição do puxador do closet', '', ''),
 ]),
 ('Richard', 'Em conclusão', '', [
   ('—', 'Obra em conclusão — confirmar o que falta para fechar', 'Sem data definida.', ''),
 ]),
 ('Larissa · Eliuton · Shelf · Daniel', 'Coordenação Bruna',
  'Estas quatro obras seguem sob coordenação da Bruna — não entram na coordenação de produção do Deivison.', []),
]

AGENDA = [
 ('Ter 27/10', 'Jairo', 'Fixação do estofado e tingimento da peça'),
 ('Qua 28/10', 'Jairo · Rejane · Ana Carolina', 'Reinstalação e finalização · liberar pintura · conferir medida do gaveteiro'),
 ('Qui 29/10', 'Ana Carolina', 'Concluir o led'),
 ('Sex 30/10', 'Simony · Leonardo', 'Bancada da Duda e batente, 8:30, e medir sapateira · marceneiro finaliza'),
 ('02 a 04/11', 'Leonardo', 'Equipe de pintura na obra'),
 ('Qua 04/11', 'Juliana', 'Conclusão da obra'),
 ('Qui 05/11', 'Graciene · Leonardo', 'Entrega · levar as peças soltas'),
 ('Sáb 07/11', 'Rejane', 'Fim da pintura — previsão de ~10 dias'),
 ('Sex 13/11', 'Andrea', 'Alvo financeiro de entrega, a confirmar'),
]
