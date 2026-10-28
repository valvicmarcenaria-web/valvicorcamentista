# -*- coding: utf-8 -*-
"""ICA · BANHO GOURMET — levantamento peça por peça  [28/10/2026]

páginas 088 a 093 · dois detalhamentos, dois itens, uma folha só de detalhe.

⭐⭐ O PRIMEIRO RIPADO DE VERDADE DO PROJETO. "Ripas de 3 cm com espaçamento
  de 3 cm", e a prancha traz um DET. RIPADO em escala 1/10 que mostra o
  corte: as ripas correm sobre um painel de base contínuo, e é o painel que
  aparece nos vãos de 3. Então são DUAS camadas, como na frente provençal —
  o painel de base e a ripa — e não uma chapa ranhurada.
  ⛔ Não confundir com o "fundo ripado" do Living, que é RANHURA na face.

⭐⭐ E A SERRA COME CHAPA. Tirar ripa de 3 cm é uma passada de serra a cada
  3 cm: a Base traz o fator 1,10 em Terceirizados e o motor nunca o tinha
  aplicado. Agora o ripado() devolve a perda como LINHA PRÓPRIA, para o
  plano de corte continuar dizendo quantas ripas existem de verdade.

⚠ A MÃO DE OBRA DO RIPADO NÃO ENTROU. A Base tem "Painel ripado · R$ 180/m²
  · ⚠ faixa observada de 70 a 420" e não diz se esse valor JÁ INCLUI a
  chapa. Lancei a chapa, que é certa, e deixei a mão de obra na caixa de
  dúvidas: somar os dois sem saber seria contar a chapa duas vezes. ⛔ Até
  essa resposta, o custo do ripado aqui é um PISO.

⛔ A BANCADA É GRANITO PRETO SÃO GABRIEL ESCOVADO, com 20 de espessura
  aparente. Marmoraria. A cuba é de sobrepor e a torneira é de parede alta.
"""
from base import P, ripado, acabamento, ALT_MAX, CHAPA_C, DOBRADICA, ALTAS

JR15 = 'MDF Jequitibá Rosa 15'
EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'

# ⭐⭐ ITEM ÚNICO [Jonathan, 28/10/2026]: "pode considerar um item unico".
#   A bancada e o painel ripado são a mesma parede do lavabo — o painel
#   começa onde a bancada acaba, e a fábrica os produz e entrega juntos.
I = 'DET 01 e 02 Bancada com armário e painel ripado'
I1 = I2 = I

BANHOGOURMET = [
 # ══ ITEM 01 · BANCADA COM ARMÁRIO — 75 × 53 × 60 ═════════════════════
 #  VISTA FRONTAL  37 + 38 = 75 · altura 20 de granito + 33 de armário = 53
 #  VISTA SUPERIOR e LATERAL  profundidade 60
 #  ⭐ as duas frentes são PORTAS RIPADAS: painel de base mais ripa de 3
 P('Lateral · DET 01', I1, 33, 60, 2, EST, (1, 0)),
 P('Base · DET 01', I1, 71, 60, 1, EST, (1, 0)),
 P('Travessa de apoio da bancada · DET 01', I1, 71, 10, 2, EST, (1, 0),
   'Frente e fundo · ⭐ a pedra apoia nelas, não em tampo cheio'),
 P('Fundo · DET 01', I1, 75, 33, 1, FUN, (0, 0), 'Encaixe em rasgo'),
 P('Frente · porta ripada esquerda · base · DET 01', I1, 37, 33, 1, JR15, (2, 2),
   '⭐ o painel de base é que aparece nos vãos de 3 entre as ripas: sai na '
   'cor da frente, não em branco'),
 P('Frente · porta ripada direita · base · DET 01', I1, 38, 33, 1, JR15, (2, 2),
   '⭐ idem · a prancha dá 37 e 38, não duas folhas iguais'),
 *ripado(I1, 37, 33, 3, 3, JR15, 'Porta esquerda · vão de 3 entre as ripas · '
         'laminada nos dois lados, que é o que o Jonathan fechou em 28/10'),
 *ripado(I1, 38, 33, 3, 3, JR15, 'Porta direita · vão de 3 entre as ripas · '
         'laminada nos dois lados'),

 # ══ ITEM 02 · PAINEL RIPADO — 80 × 154 ═══════════════════════════════
 #  DET. 02 PERSPECTIVA  80 de largura × 154 de altura
 #  DET. RIPADO 1/10     3 + 3 + 3 + 3 + 3 + 3 · ripa e vão alternados
 P('Painel de base · DET 02', I2, 80, 154, 1, JR15, (2, 2),
   '⭐ é ele que aparece nos vãos de 3 · o DET. RIPADO em 1/10 mostra as '
   'ripas correndo sobre um painel contínuo, não chapa ranhurada'),
 *ripado(I2, 80, 154, 3, 3, JR15, 'Painel ripado · 14 ripas de 3 com vão de '
         '3 em 80 · laminada nos dois lados'),
]

# ── ferragem, declarada item a item ─────────────────────────────────────
GAVETAS = []
PORTAS  = [(I1, 'Duas portas ripadas de 33 de altura', 2, 2, DOBRADICA)]
BASCULAS= []
CAVA     = []
PUXADORES= []
MOLDURA  = []
LED      = []
CABIDEIROS = []
SARRAFOS = []
SUPORTES = []
ALMAS    = []
SERRALHERIA = []
# ⭐ O ESPELHO ENTRA NA CONTA [Jonathan, 28/10/2026]: "considere o espelho".
#   Até aqui ele estava em NÃO É MARCENARIA, como vidraçaria de terceiro —
#   e estava errado: quem compra e instala é a casa. 75 × 180 = 1,35 m².
VIDRO   = [(I, 'Espelho de 75 × 180 da ELEVAÇÃO 01', 1, 75, 180, 'Espelho')]
# ⭐ A PORTA RIPADA NÃO TEM PUXADOR DESENHADO, e uma face ripada não aceita
#   cava: quem sobra é o pulsador. A prancha não escreve nenhum dos três, e
#   a dúvida 03 põe os números das alternativas na mesa.
OUTRAS   = [(I, 'Perfil de proteção de piso', 'O painel ripado de 80 corre '
             'do piso ao teto e encosta no chão · a bancada é suspensa',
             0.80, 'm', 'Perfil de proteção de piso'),
            (I1, 'Pulsador', 'Duas portas ripadas · abre por toque, sem '
             'ferragem à vista · ⚠ a prancha não desenha puxador nenhum',
             2, 'un', 'Pulsador')]

CABECA = {
 I: ('75 × 53 × 60  +  80 × 154 × 3',
     'DET 01 bancada com armário 75 × 53 × 60, em 37 + 38, com 20 de '
     'granito sobre 33 de armário ⭐ as duas frentes são PORTAS RIPADAS, '
     'painel de base mais ripa de 3 com vão de 3 · DET 02 painel ripado '
     '80 × 154 × 3, com o DET RIPADO em 1/10 mostrando 3 + 3 + 3 alternados '
     'sobre painel contínuo · ⭐ item único [Jonathan, 28/10]: é a mesma '
     'parede, e o painel começa onde a bancada acaba'),
}

FOLHA = dict(
 aba='BANHO GOURMET',
 sub='Jéssica e Michell · Projeto ICA · páginas 088 a 093 · dois itens, uma '
     'cor aparente só, Jequitibá Rosa Linha Essencial Wood · ⭐ o primeiro '
     'RIPADO de verdade do projeto: ripa de 3 com vão de 3 sobre painel de '
     'base, em duas camadas · caixaria em Branco TX 15 · peça inteira até '
     f'{ALT_MAX:g}, que é a chapa de {CHAPA_C:g} menos o acerto de corte',
 chapa_txt={JR15: 'Jequitibá Rosa Linha Essencial Wood · ripas, painéis de base e frentes',
            EST:  'Estrutura e caixaria · o padrão da Base para caixaria',
            FUN:  'Fundos · encaixe em rasgo, sem fita'},
 nota='⛔ O FRETE ESTÁ ZERADO DE PROPÓSITO: as linhas de frete da Base não '
      'têm preço ainda. Preencher lá e elas aparecem aqui sozinhas.   '
      '⚠⚠ A MÃO DE OBRA DO RIPADO NÃO ESTÁ NESTA CONTA. A Base traz '
      '"Painel ripado · R$ 180/m²" e não diz se esse valor já inclui a '
      'chapa. Lancei a chapa, que é certa, e deixei a mão de obra na caixa '
      'de dúvidas — somar os dois sem saber seria contar a chapa duas '
      'vezes. ⛔ Até essa resposta, o custo do ripado aqui é um PISO: são '
      '1,8 m² de painel ripado entre as duas portas e o painel do DET 02.   '
      '⛔ A BANCADA É GRANITO PRETO SÃO GABRIEL ESCOVADO, de marmoraria, '
      'com 20 de espessura aparente.',
 duvidas=[
  'A MÃO DE OBRA DO RIPADO: a Base traz "Painel ripado · R$ 180/m² · ⚠ faixa '
  'observada de 70 a 420 · depende da largura da ripa e do vão", e NÃO diz se '
  'esse valor já inclui a chapa. Lancei só a chapa — painel de base mais ripa '
  '— e deixei a mão de obra fora. ⚠ Se os R$ 180 forem SERVIÇO, faltam uns '
  'R$ 330 aqui; se forem o item inteiro, está certo como está. ⛔ É a '
  'pergunta que decide o preço deste ambiente, e ela volta em todo ripado do '
  'projeto.',
  'O PAINEL DE BASE DO RIPADO saiu em Jequitibá Rosa, não em branco: com vão '
  'de 3 cm entre ripas de 3 cm, METADE da área do painel fica à vista. ⚠ Se '
  'o desenho quiser o fundo escuro, de contraste, muda a cor e muda o preço '
  'da chapa. O DET. RIPADO em 1/10 desenha os dois na mesma madeira.',
  'AS PORTAS RIPADAS NÃO TÊM PUXADOR DESENHADO. A prancha não escreve cava, '
  'não escreve puxador e não escreve fecho toque — e uma porta ripada de 33 '
  'precisa abrir de algum jeito. ⭐ Orcei PULSADOR, R$ 100 cada, porque é o '
  'único modo que não aparece no desenho: uma face ripada não aceita cava '
  'sem cortar a ripa, e puxador aparafusado o desenho mostraria. ⚠ As '
  'alternativas: cava usinada sairia R$ 37 pelas duas; Alças Traso 128, '
  'R$ 220. Decisão de desenho, e vale R$ 163 para baixo ou R$ 20 para cima.',
  'A BANCADA TEM 53 DE ALTURA TOTAL, com 20 de granito e 33 de armário. ⚠ É '
  'baixo para um lavatório: o normal é 85 a 90. Ou o móvel é suspenso e a '
  'prancha não cotou a altura do piso, ou a elevação resolve isso — a '
  'ELEVAÇÃO 01 traz 37 + 33 + 20 e também não fecha os 90. Confirmar antes '
  'do corte, porque muda a lateral e o fundo.',
  'O NICHO ILUMINADO da ELEVAÇÃO 03 aparece em letra e NÃO tem detalhamento. '
  '⚠ Não está nesta conta: sem medida, sem profundidade e sem saber se é '
  'nicho de alvenaria revestido ou caixa de marcenaria. Se for nosso, é um '
  'terceiro item neste ambiente.',
  'O ESPELHO DE 75 × 180 da ELEVAÇÃO 01 não é nosso, mas quem o fixa é. ⚠ '
  'Espelho desse tamanho costuma pedir moldura ou sarrafo de apoio em '
  'marcenaria. A prancha não desenha nenhum dos dois.',
  '⛔ A BASE METÁLICA DE 3 CM aparece aqui como em todo o projeto e continua '
  'NÃO LANÇADA em nenhum ambiente. ⚠ São uns 3 m de rodapé por ambiente, e já '
  'são seis ambientes.'],
 nao_marcenaria=[
  'Bancada em granito Preto São Gabriel escovado, 75 × 60 com 20 de espessura aparente',
  'Cuba Quadrada de Sobrepor 40 cm Branco Slim - Deca e Torneira Monocomando Alta '
  'Michigan Cromada - Bela Metais',
  'Espelho de 75 × 180 da ELEVAÇÃO 01',
  'Bacia para Caixa Acoplada Branco Carrara - Deca, chuveiro e registros',
  'Nicho iluminado da ELEVAÇÃO 03 — citado em letra, sem detalhamento'],
 notas=[
  '⭐⭐ O PRIMEIRO RIPADO DE VERDADE DO PROJETO, e ele é de DUAS CAMADAS. O '
  'DET. RIPADO em escala 1/10 mostra o corte: as ripas de 3 correm sobre um '
  'painel de base contínuo, e é esse painel que aparece nos vãos de 3. Não é '
  'chapa ranhurada — isso é o "fundo ripado" do Living, que é outra coisa.',
  '⭐⭐ A SERRA COME CHAPA, e agora isso está na conta. A Base traz "Perda de '
  'serra ao tirar ripa · fator 1,10" e o motor nunca a aplicava: tirar ripa '
  'de 3 cm é uma passada de serra a cada 3 cm. Entra como LINHA PRÓPRIA, '
  'marcada como perda, para o plano de corte continuar dizendo quantas ripas '
  'existem de verdade.',
  '⭐ A LAMINAÇÃO DA RIPA É NOS DOIS LADOS, como o senhor fechou em 28/10: '
  'numa ripa solta, com vão, os dois lados longos ficam à vista. São quatro '
  'arestas por ripa, e a filetagem é MANUAL, R$ 5,00 — ripa não entra na '
  'coladeira. São 28 ripas aqui.',
  '⚠ UMA COR SÓ DE FRENTE no ambiente inteiro: Jequitibá Rosa Linha Essencial '
  'Wood, a mesma do DET 01 e do DET 03 da Área Gourmet. É o padrão dos '
  'ambientes de convívio desta casa.',
  '⚠ NENHUMA PEÇA PASSA DA CHAPA. A maior é o painel de base de 154 × 80, e '
  'ele cabe inteiro nos 275 × 185.'],
)
