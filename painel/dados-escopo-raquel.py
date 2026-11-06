# -*- coding: utf-8 -*-
"""Escopo de venda — Raquel Franco · Quarto e banheiro.

Fonte: projeto executivo PRJ EXEC_RAQUEL FRANCO_rn (11 pranchas, designer
Rubia Nascimento, 10/2026) e o registro comercial da planilha de gestão.
A proposta e o contrato não foram localizados no Drive.
"""

OBRA = dict(
    cliente   = 'Raquel Franco',
    ambiente  = 'Quarto e banheiro',
    designer  = 'Rubia Nascimento · (31) 98318-7675',
    projeto   = 'PRJ EXEC_RAQUEL FRANCO_rn · 11 pranchas · 10/2026',
    valor     = 'R$ 22.600,00',
    situacao  = 'Quitado',
)

MARCENARIA = [
 ('14', 'Escrivaninha', 'MDF Noce Amêndoa Duratex', '220 de comprimento · 72 h',
  '7', 'Quatro gavetas · caixa de tomadas embutida · nicho na marcenaria'),
 ('15', 'Prateleira', 'MDF Cancún Sudati', '140 × 25 × 2 h', '8', ''),
 ('16', 'Armário aéreo maior', 'MDF Lume Guararapes', '100 × 25 × 35 h', '8', 'Puxador passante'),
 ('17', 'Armário aéreo menor', 'MDF Lume Guararapes', '65 × 25 × 35 h · 2 un', '8', 'Puxador passante'),
 ('18', 'Painel da persiana', 'MDF Lume Guararapes', 'conforme prancha', '6 e 9',
  'Vão recuado para a persiana descer — conferir com o fornecedor da persiana antes de fabricar'),
 ('19', 'Gaveteiro', 'MDF Cancún Sudati', '50 × 45 × 55 h', '5',
  'Quatro gavetas · rodízio de silicone com trava'),
 ('20', 'Mesa de cabeceira', 'MDF Cancún Sudati', '40 × 30 × 8 h', '3', 'Uma gaveta · interruptor com tomada'),
 ('21', 'Cabideiro', 'MDF Lume Guararapes', '10 cm · 4 un', '5', ''),
 ('22', 'Cama com cabeceira estofada', 'MDF + estofado', 'conforme prancha', '4',
  'EXECUÇÃO NOSSA · cama e cabeceira · tecido do estofado a definir'),
 ('23', 'Painel de meia parede', 'MDF Cancún Sudati', '336 de comprimento · 87 h', '9',
  'Filete em MDF Sal Rosa Arauco · sem perfil metálico'),
]

BANHEIRO = [
 ('24', 'Nicho do banheiro', 'MDF Lume Guararapes', '27 × 12 × 165 h', '11', ''),
 ('25', 'Gabinete do banheiro', 'MDF Lume Guararapes', '89 × 27 × 60 h', '11',
  'Cinco prateleiras internas'),
 ('26', 'Acabamento do espelho', 'MDF Lume Guararapes', '76 cm · 2 un', '11',
  'Puxador passante · toalheiro de mão'),
]

ROUPEIRO = dict(
    prancha='10', medidas='267 × 152 · 60 cm de profundidade interna',
    texto=('<b>Reaproveitamento, não móvel novo.</b> Preservar a estrutura existente em madeira — base e laterais — '
           '<b>mediante conferência do estado de conservação e da estabilidade</b>. Reaproveitar as portas, com preparação '
           'da superfície e aplicação de <b>laca fosca Sayerlack J029</b>. Executar a nova organização interna em '
           '<b>MDF branco TX</b>: prateleiras, divisórias, gavetas e sapateira deslizante. Cabideiro oval. Vão como puxador. '
           '<b>Conferir as medidas internas e a compatibilidade das peças com a abertura das portas antes da fabricação.</b>'))

MATERIAIS = [
 ('MDF Noce Amêndoa Duratex', 'Escrivaninha'),
 ('MDF Cancún Sudati', 'Prateleira · gaveteiro · mesa de cabeceira · painel de meia parede'),
 ('MDF Lume Guararapes', 'Armários aéreos · painel da persiana · cabideiro · peças do banheiro'),
 ('MDF Sal Rosa Arauco', 'Filete do painel de meia parede'),
 ('MDF branco TX', 'Organização interna do roupeiro'),
 ('Laca fosca Sayerlack J029', 'Portas do roupeiro · prateleira'),
 ('Tecido do estofado', 'Cabeceira da cama — A DEFINIR'),
]

FERRAGENS = [
 'Puxador passante — armários aéreos e espelho do banheiro',
 'Rodízio de silicone com trava — gaveteiro',
 'Cabideiro oval — roupeiro',
 'Sapateira deslizante — roupeiro',
]

FORA = [
 'Puxador de porcelana Nanda Devi 151 — Meu Puxador, 12 un — fornecimento do cliente',
 'Papel de parede — Uau Bobinex, 12 rolos',
 'Pintura do quarto e do banheiro — Suvinil, acrílica e epóxi',
 'Persiana rolô blackout — Luiza Valentina, tecido a definir',
 'Espelho, tapetes, cadeira e peças de decoração',
 'Iluminação — lustre, luminárias e arandelas',
 'Pontos elétricos novos',
 'Roupa de cama personalizada',
]

DEFINIR = [
 ('Material dos armários do banheiro',
  'Os itens 24, 25 e 26 trazem <b>MDF Lume Guararapes</b>, mas a prancha 11 anota "usar MDF Verde/Ultra para armários". <b>Divergência dentro do próprio projeto.</b>'),
 ('O roupeiro está vendido?',
  'A prancha 10 não aparece na legenda de marcenaria do layout. Confirmar se o reaproveitamento foi contratado.'),
 ('Tecido do estofado da cabeceira',
  'A cama e a cabeceira são <b>execução nossa</b>. Falta definir o tecido com a cliente antes de comprar.'),
 ('Estado do roupeiro existente',
  'A execução depende da conferência da conservação e da estabilidade da estrutura. Se não passar, o escopo muda.'),
 ('Conferência de medidas no local',
  'Exigida em todas as pranchas. Há fotos de medição de 05/11 na pasta do cliente — confirmar se cobrem todos os ambientes.'),
 ('Vão da persiana',
  'O painel tem recuo para a persiana descer. Alinhar a medida com a Luiza Valentina antes de fabricar o painel.'),
]
