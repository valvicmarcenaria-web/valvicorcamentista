# -*- coding: utf-8 -*-
"""Escopo de venda — Raquel Franco · quarto e banheiro.

Fonte: projeto executivo PRJ EXEC_RAQUEL FRANCO_rn (11 pranchas, designer
Rubia Nascimento, 10/2026) e o contrato, que exclui o roupeiro do escopo.
"""

OBRA = dict(
    cliente  = 'Raquel Franco',
    ambiente = 'Quarto e banheiro',
    designer = 'Rubia Nascimento · (31) 98318-7675',
    projeto  = 'PRJ EXEC_RAQUEL FRANCO_rn · 11 pranchas · 10/2026',
)

PECAS = [
 ('14', 'Escrivaninha', 'MDF Noce Amêndoa Duratex', '7',
  'Quatro gavetas · caixa de tomadas embutida · nicho na marcenaria'),
 ('15', 'Prateleira', 'MDF Cancún Sudati', '8', 'Laca fosca Sayerlack J029'),
 ('16', 'Armário aéreo maior', 'MDF Lume Guararapes', '8', 'Puxador passante'),
 ('17', 'Armário aéreo menor · 2 un', 'MDF Lume Guararapes', '8', 'Puxador passante'),
 ('18', 'Painel da persiana', 'MDF Lume Guararapes', '6 e 9',
  'Vão recuado para a persiana descer — <b>medida a alinhar com a arquiteta</b> antes de fabricar'),
 ('19', 'Gaveteiro', 'MDF Cancún Sudati', '5', 'Quatro gavetas · rodízio de silicone com trava'),
 ('20', 'Mesa de cabeceira', 'MDF Cancún Sudati', '3', 'Uma gaveta · interruptor com tomada'),
 ('21', 'Cabideiro · 4 un', 'MDF Lume Guararapes', '5', ''),
 ('22', 'Cama com cabeceira estofada', 'MDF + estofado', '4',
  'Execução nossa · <b>tecido do estofado a definir</b>'),
 ('23', 'Painel de meia parede', 'MDF Cancún Sudati', '9',
  'Filete em MDF Sal Rosa Arauco · <b>sem perfil metálico</b>'),
 ('24', 'Nicho do banheiro', 'MDF Lume Guararapes', '11', ''),
 ('25', 'Gabinete do banheiro', 'MDF Lume Guararapes', '11', 'Cinco prateleiras internas'),
 ('26', 'Acabamento do espelho · 2 un', 'MDF Lume Guararapes', '11',
  'Puxador passante · toalheiro de mão'),
]

MATERIAIS = ('MDF Noce Amêndoa Duratex · MDF Cancún Sudati · MDF Lume Guararapes · '
             'MDF Sal Rosa Arauco (filete) · laca fosca Sayerlack J029 · tecido do estofado (a definir)')

FERRAGENS = ('Puxador passante (aéreos e espelho) · rodízio de silicone com trava (gaveteiro) · '
             'corrediças e dobradiças de linha')

FORA = 'Puxador de porcelana Nanda Devi 151 — Meu Puxador, 12 un — fornecimento do cliente'

ROUPEIRO = ('O roupeiro da prancha 10 <b>não está incluso</b> — excluído do escopo em contrato. '
            'Não fabricar, não orçar e não comprar material para ele.')

DEFINIR = [
 ('Material dos armários do banheiro',
  'Os itens 24, 25 e 26 trazem <b>MDF Lume Guararapes</b>, mas a prancha 11 anota "usar MDF Verde/Ultra para armários". Divergência dentro do próprio projeto.'),
 ('Tecido do estofado da cabeceira',
  'A cama e a cabeceira são execução nossa. Definir o tecido com a cliente antes de comprar.'),
 ('Conferência de medidas no local',
  'Exigida em todas as pranchas. Há fotos de medição de 05/11 na pasta do cliente — confirmar se cobrem todos os ambientes.'),
 ('Vão da persiana',
  'O painel tem recuo para a persiana descer. <b>Alinhar a medida com a arquiteta</b> antes de fabricar.'),
]
