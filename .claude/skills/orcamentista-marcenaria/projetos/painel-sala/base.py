# -*- coding: utf-8 -*-
"""PAINEL DA SALA — VISTA 2 · a base, lida CÉLULA A CÉLULA da planilha.

⭐⭐ [Jonathan, 17/11/2026] "o quantitativo de chapas esta errado / vc
  quantificou onde esta as chapas da base onde as ripas serão coladas? /
  fita de borda tem certeza que é so isso? / e o custo da filetagem? /
  iluminação nao é nossa / e as dobradiças da porta a esquerda? / refaça
  com base nas planilhas."

⛔⛔ A PRIMEIRA VERSÃO SAIU DAS CONSTANTES QUE EU HERDEI DE OUTRO PROJETO,
  NÃO DA BASE. Cinco erros, e a planilha tinha a resposta dos cinco:

  1. PORTA DE PASSAGEM É 42 MM. A aba MDF, em "ESPESSURA PADRÃO POR
     APLICAÇÃO", crava: "Portas de passagem · 42 mm". Eu orcei duas folhas
     de 18. Uma folha de 42 é 18 + 18 + 6 — a MESMA ÁREA TRÊS VEZES.
  2. A FITA DAS RIPAS NÃO EXISTIA. Eu cobrei a FILETAGEM (a aplicação) e
     esqueci a FITA (o material) nos 285 m de ripa. A Base tem a linha
     pronta: "Fita de cor com filetagem, preço cheio da casa · R$ 5,50 ·
     já inclui a aplicação" — que é 3,00 de fita mais 2,50 de aplicação.
  3. A RIPA DE 2 CM NÃO ENTRA NA COLADEIRA. A Base separa "Filetagem na
     coladeira automática · 15 e 18 mm · R$ 2,50" de "Filetagem manual ·
     ripa de 6 mm E O QUE NÃO ENTRA NA MÁQUINA · R$ 5,00". Coladeira
     automática não pega peça de 20 mm de largura. É manual.
  4. A BORDA DE 42 MM PEDE FITA DE 50. "Fita de borda cor · 50 mm · R$ 7,00
     · para peça de 5 cm". Eu usei a de 22 mm em tudo.
  5. A PORTA DA ESQUERDA NÃO TINHA DOBRADIÇA NENHUMA. Ela é porta de
     ARMÁRIO, não de passagem: não é pivô, é dobradiça. E a tabela da Base
     manda CINCO, porque 277 passa de 200 cm.

  ⭐ E a ILUMINAÇÃO SAIU: "iluminação nao é nossa" [Jonathan, 17/11/2026].

Planilha: `Valvic · Base de Custos` · 13cZGej-AUTTyWZblqtraTBnc1HUECjT6fy3zy6R5mv4
"""
import os as _os

# ── a chapa · aba MDF ───────────────────────────────────────────────────
CHAPA_C, CHAPA_L = 275.0, 185.0          # MDF · "MEDIDA E RENDIMENTO"
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875
APROV = 0.80                             # MDF · "Aproveitamento · 80%"
ALT_MAX = CHAPA_C - 2.0

#   ⚠⚠ "MDF GIANDUIA TRAMA - DURATEX" É A PRIMEIRA COTAÇÃO A FAZER. Trama é
#     padrão texturizado, e a Base tem uma linha só para isso: "CHAPA — COR
#     E ACABAMENTO ESPECIAL · R$ 1.000,00 · confirmado em plano de corte".
#     Orço na linha "MDF Melamínico Fosco · Amadeirado e cor", que é a
#     chapa de cor padrão da casa, e deixo o interruptor ESPECIAL=1.
ESPECIAL = _os.environ.get('ESPECIAL') == '1'
_f = 1000.0 / 700.0 if ESPECIAL else 1.0
PRECO = {
    #   MDF · "MDF Melamínico Fosco · é a chapa de cor padrão da casa"
    'MDF Gianduia 18': 700.0 * _f,
    'MDF Gianduia 15': 550.0 * _f,
    'MDF Gianduia 6':  350.0 * _f,
    #   MDF · "CHAPA — BRANCO (interno de armário)" · nunca aparece
    'MDF Branco TX 18': 400.0,
    'MDF Branco TX 15': 350.0,
    'MDF Branco TX 6':  250.0,
}

# ── espessura padrão por aplicação · aba MDF ────────────────────────────
ESP_ESTRUTURA = 15           # "Estrutura e caixaria · 15 mm"
ESP_FUNDO = 6                # "Fundos · 6 mm"
ESP_PORTA = 15               # "Portas · 15 mm"
ESP_PASSAGEM = 42            # ⛔ "Portas de passagem · 42 mm"
#   ⭐ 42 não é chapa: é tamponamento. 18 + 18 + 6 = 42, a mesma área três
#     vezes. As duas faces em Gianduia (a de dentro é VISTA do outro
#     ambiente) e o miolo em Branco TX de 6, que ninguém vê.
PASSAGEM_CAMADAS = ((18, 'MDF Gianduia'), (18, 'MDF Gianduia'),
                    (6, 'MDF Branco TX'))
assert sum(e for e, _m in PASSAGEM_CAMADAS) == ESP_PASSAGEM

# ── A RIPA DESTE PROJETO NÃO É A RIPA DA CASA ───────────────────────────
#   A prancha crava "RIPADO EM MDF GIANDUIA TRAMA DE 20MM E ESPAÇAMENTO DE
#   20MM - DURATEX", e o detalhe 1/5 confirma com a cota 2 · 2 · 2.
#   ⛔ O padrão da casa é ripa de 4 com vão de 2 — passo 6. Aqui o passo é
#     4: 25 ripas por metro em vez de 16,7.
RIPA_L, RIPA_VAO = 2.0, 2.0
PASSO = RIPA_L + RIPA_VAO
RIPA_ESP_MM = 18             # ⚠ a prancha pede 20 mm de relevo; cortamos de 18
#   Terceirizados · "Perda de serra ao tirar ripa · fator · R$ 1,10"
RIPA_PERDA = 1.10
#   ⛔⛔ E O VÃO TEM 2 CM DE PROFUNDIDADE: enxerga-se o fundo entre as ripas.
#     O substrato sai no MESMO Gianduia, e em 15 mm, que é a espessura de
#     tamponamento da Base.
SUBSTRATO_ESP_MM = 15

# ── fita de borda e filetagem · aba MDF ─────────────────────────────────
FITA_22 = 3.00               # "Fita de borda cor · 22 mm · R$ 3,00"
FITA_50 = 7.00               # "Fita de borda cor · 50 mm · R$ 7,00 · peça de 5 cm"
FITA_PERDA = 1.10            # "somar 10% de desperdício"
FILETE_MAQ = 2.50            # "Filetagem na coladeira automática · 15 e 18 mm"
FILETE_MAO = 5.00            # "Filetagem manual · ripa de 6 mm E O QUE NÃO
                             #  ENTRA NA MÁQUINA · mais lento"
FITA_CHEIA = 5.50            # "Fita de cor com filetagem, preço cheio da
                             #  casa · já inclui a aplicação" = 3,00 + 2,50
assert abs(FITA_22 + FILETE_MAQ - FITA_CHEIA) < 1e-9

#   ⛔⛔ A RIPA DE 2 CM DE LARGURA NÃO ENTRA NA COLADEIRA AUTOMÁTICA, e a
#     Base nomeia esse caso: "o que não entra na máquina · R$ 5,00". Então
#     a ripa custa fita MAIS filetagem manual, não a filetagem de máquina
#     que eu tinha usado sozinha.
#     `RIPA_NA_MAQUINA=1` roda o cenário barato, para comparar.
RIPA_NA_MAQUINA = _os.environ.get('RIPA_NA_MAQUINA') == '1'
FILETE_RIPA = FILETE_MAQ if RIPA_NA_MAQUINA else FILETE_MAO
FITA_RIPA_M = FITA_22 * FITA_PERDA + FILETE_RIPA        # 8,30 · ou 5,80

# ── consumíveis e embalagem · aba MDF ───────────────────────────────────
CONSUMIVEIS = 0.06           # "sobre chapa e fita · 6%"
EMBALAGEM = 0.02             # "sobre o custo direto · 2%"
CORTE_CHAPA, CORTE_PECA = 2.00, 2.50     # [Jonathan, 28/10/2026]

# ── terceirizados · aba Terceirizados ───────────────────────────────────
#   "Painel ripado · ⚠ faixa observada de 70 a 420 · DEPENDE DA LARGURA DA
#    RIPA E DO VÃO · m² · R$ 180,00"
#   ⚠ Com ripa de 2 cm e vão de 2 cm estamos no lado CARO dessa faixa, não
#     no meio. R$ 180 é o valor da Base e é o que uso; fica escrito que o
#     teto observado é R$ 420 e que esta trama é a mais fechada que já
#     fizemos.
RIPADO_M2 = 180.0

# ── ferragem · aba Ferragens ────────────────────────────────────────────
#   "PORTAS DE PASSAGEM · Sistema pivô · conjunto · R$ 120,00"
SISTEMA_PIVO = 120.0
#   "Fecho rolete para porta pivotante · un · R$ 75,00"
FECHO_ROLETE = 75.0
#   ⭐⭐ A DOBRADIÇA DA PORTA DA ESQUERDA, que não existia no meu orçamento.
#     Ela é porta de ARMÁRIO: dobradiça, não pivô. A escada da Base:
#       Bigfer Inox Click 10 · Bigfer Onix 15 · Novisys 20 · Sensys 50
#     ⚠ O Jonathan não disse a linha deste projeto. Travertino romano,
#     Duratex Gianduia Trama e três portas mimetizadas são especificação de
#     alto padrão, e o degrau Gold da Base é Hettich. Vou de SENSYS e
#     deixo a escada impressa na tabela, para ele descer um degrau com um
#     número na mão em vez de um palpite.
#   ⛔ [Jonathan, 18/11/2026] "pode manter as ferragens dobradiça ... da
#     Blum". A Base: "Dobradiça Blum · ⭐ O QUE VALE HOJE · un · R$ 50,00".
#     ⭐⭐ E ISSO NÃO CUSTA UM CENTAVO: Sensys e Blum valem os MESMOS R$ 50
#     na Base. O que muda é a GARANTIA — a escada da casa dá 10 anos ao
#     degrau Gold (Hettich) e 30 ANOS ao Blum. Mesmo custo, vinte anos a
#     mais de promessa.
DOBRADICA = 50.0
DOBRADICA_NOME = 'Dobradiça Blum'
ESCADA_DOBRADICA = [('Bigfer Inox Click', 10.0), ('Bigfer Onix', 15.0),
                    ('Hettich Novisys', 20.0), ('Hettich Sensys', 50.0)]

#   ⭐⭐ E A GARANTIA SOBE JUNTO, DE GRAÇA. A política da casa
#     (`closer-vendas/referencias/garantia.md`, reafirmada pelo Jonathan em
#     29/10/2026) é escalonada por ferragem:
#         telescópica 2 anos · Hardt 5 · Hettich 10 · BLUM 30
#     A dobradiça Blum custa os MESMOS R$ 50 da Sensys na Base. Trocar a
#     linha não tirou um centavo do custo e devolveu VINTE ANOS de promessa.
#   ⛔ Regra do elo mais fraco: o pivô e o fecho rolete das portas de
#     passagem não estão na escada — quem manda nela é a dobradiça.
#   ⚠⚠ PENDÊNCIA DA CASA, e ela trava a impressão: garantia.md diz que "só o
#     termo de 10 anos está desenhado; o termo de 30 anos precisa existir
#     assinado antes de a proposta sair". A folha promete 30; o documento
#     tem de acompanhar.
#   ⚠ E a folha escreve "garantia sobre a marcenaria", NUNCA "garantia Blum
#     de fábrica": não existe termo de 30 anos publicado pela Blum.
GARANTIA_ANOS = 30
#   "Alma de aço · barra chata 5 mm, barra de 3 m · R$ 50,00 · contra empeno"
ALMA_BARRA = 50.0

# ── ⭐⭐ AS BANDAS VIRARAM ARMÁRIO [Jonathan, 18/11/2026] ────────────────
#   "a parte superior e a parte inferior de onde está o nicho de pedra
#    também serão armários, não serão apenas painéis. Então temos que
#    considerar tanto o custo de material de estrutura quanto de ferragem."
#   ⛔ E ISSO ARRASTA UMA FERRAGEM QUE NÃO ESTAVA EM LUGAR NENHUM: porta
#     mimetizada em ripado NÃO TEM PUXADOR. Cava usinada cortaria a trama
#     justamente onde ela precisa correr inteira. Logo, abertura por TOQUE:
#     "Pulsador outros · un · R$ 70,00" da aba Ferragens.
#   ⚠ E o pulsador vale também para a porta de 50 × 277, que eu já tinha
#     orçado "sem puxador" sem dizer COMO ela abre.
#   ⛔ Eu tinha o genérico de R$ 70. Blum é a linha de cima da
#     Base: "Pulsador Blum Tip-on ou Servo · Abertura por toque ·
#     un · R$ 100,00 · Jonathan, 26/10/2026". São R$ 30 por folha
#     e NOVE folhas de armário — as duas de passagem abrem na
#     maçaneta, não no toque.
PULSADOR = 100.0
PULSADOR_NOME = 'Pulsador Blum Tip-on, abertura por toque'
#   ⛔⛔ A BÁSCULA SAIU [Jonathan, 18/11/2026]: "não será a báscula, será a
#     porta de giro na parte superior também". Eu tinha posto quatro
#     AVENTOS HK-XS a R$ 250 porque a banda de cima vai de 2,17 m a 2,92 m
#     do piso e porta de girar a essa altura abre na cara de quem está
#     embaixo. Ele decidiu de giro, e é decisão dele.
#     ⭐ Troca R$ 1.000 de báscula por 8 dobradiças de R$ 50: devolve R$ 600.
#   ⚠ FICA REGISTRADO O QUE SE PERDE: a folha de 75 × 75 a 2,17 m abre para
#     fora e para baixo, e quem estiver na mesa de jantar leva a quina na
#     cabeça. A báscula sobe. É o tipo de coisa que não aparece no
#     orçamento e aparece na obra.
#   ⛔ REGRA 2 DA CASA [Jonathan, 28/10/2026]: "prateleiras internas dos
#     armarios nao ultilizamos suporte oculto, mas precisamos considerar
#     que toda prateleira interna existe a composição de 4 suportes em um
#     custo total de 6.50". ⚠ NÃO é o "Suporte oculto · R$ 30" da Base:
#     aquele é só para prateleira de PAREDE.
SUPORTE_JOGO = 6.50
#   profundidade útil dentro do volume de 50, descontada a frente
#   (folha de 15 mm mais ripa de 18 mm = 33 mm)
PROF_UTIL = 46.0
#   ⚠ 302 cm de banda dividida em QUATRO vãos. A prancha não desenha
#     divisão nenhuma — e não desenha de propósito: a junta das folhas cai
#     DENTRO do vão de 2 cm da trama e some. Quatro é o que dá folha de
#     75,5, que é o limite confortável de uma báscula HK-XS.
VAOS_BANDA = 4


def dobradicas(altura_cm):
    """Ferragens · "REGRA · quantas dobradiças por porta, pela altura"."""
    if altura_cm <= 90:  return 2
    if altura_cm <= 160: return 3
    if altura_cm <= 200: return 4
    return 5


# ── logística · ⛔⛔ O JOB É EM GOVERNADOR VALADARES ─────────────────────
#   ⭐⭐ [Jonathan, 17/11/2026] "deixe claro na proposta que é com a
#     conferencia tecnica e instalação em Governador Valadares".
#   ⛔ ISSO DERRUBA A LINHA QUE EU TINHA. Os R$ 200 por viagem que o
#     Jonathan cravou em 29/10 são número de Belo Horizonte: caminhão sai,
#     entrega e volta no mesmo turno. GV fica a 320 km — 640 de ida e
#     volta —, e a equipe dorme fora. Eu tinha R$ 400 de frete no projeto
#     inteiro; só a instalação passa de quatro mil.
#   ⚠ A aba MDF tem QUATRO linhas de frete e as quatro estão VAZIAS, de
#     propósito: "linha criada e vazia de propósito: assim o orçamento
#     mostra zero e grita". Ela gritou. Como não há número na casa, monto
#     a logística linha a linha, e marco com ⚠ tudo o que é estimativa
#     minha — para o Jonathan trocar UM número, não o bloco inteiro.
OBRA = 'Governador Valadares'

#   ⭐⭐ OS NÚMEROS SÃO DO JONATHAN [19/11/2026], não meus. Ele mandou o
#     conjunto fechado da obra especial de GV, e isso APOSENTA a minha
#     tabela de km × R$/km, hospedagem por noite e alimentação por dia.
#     Eu estava estimando R$ 3.420; o real é R$ 5.200 — eu estava
#     R$ 1.780 abaixo, 52% a menos no bloco.
#   ⛔ DUAS VIAGENS, DE NATUREZAS DIFERENTES:
#       · a MEDIÇÃO é bate-volta, no mesmo dia, e cobra POR PESSOA;
#       · a INSTALAÇÃO leva carreto (o painel não cabe no Mobi), o Mobi
#         com a dupla, 4 diárias de Airbnb e 4 dias de alimentação.
#   ⭐ As 4 diárias e os 4 dias de comida BATEM com DIAS_MONTAGEM = 4.
#     Se ele mudar os dias de montagem, estas duas linhas mudam junto —
#     na planilha são campos amarelos lado a lado, de propósito.
MEDICAO_UNIT = 350.00          # bate-volta, POR PESSOA
MEDICAO_QTD = 1                # ⚠ quantas pessoas vão medir
CARRETO_UNIT = 2500.00         # caminhão HR, a viagem de carga
CARRETO_QTD = 1
COMBUSTIVEL_UNIT = 400.00      # Mobi, a viagem
COMBUSTIVEL_QTD = 1
PEDAGIO_UNIT = 170.00          # Mobi, a viagem
PEDAGIO_QTD = 1
AIRBNB_UNIT = 225.00           # R$ 900 pelas 4 diárias
AIRBNB_QTD = 4
ALIMENTACAO_UNIT = 110.00      # R$ 440 por pessoa pelos 4 dias
ALIMENTACAO_QTD = 8            # 2 pessoas × 4 dias

#   ⛔ A ORDEM IMPORTA: é a ordem em que as linhas entram na planilha, e
#     a planilha pinta a QUANTIDADE de amarelo em todas.
LOGISTICA = [
    dict(rotulo='Medição · bate-volta, por pessoa',
         qtd=MEDICAO_QTD, un='pessoa', unit=MEDICAO_UNIT,
         obs='a conferência técnica antes do corte · vai e volta no mesmo '
             'dia, sem dormir fora · ⚠ hoje está 1 pessoa'),
    dict(rotulo='Carreto · caminhão HR',
         qtd=CARRETO_QTD, un='viagem', unit=CARRETO_UNIT,
         obs='leva o painel · ⛔ é a maior linha da logística e sozinha '
             'vale metade do bloco'),
    dict(rotulo='Mobi · combustível',
         qtd=COMBUSTIVEL_QTD, un='viagem', unit=COMBUSTIVEL_UNIT,
         obs='o carro que leva a dupla, ida e volta'),
    dict(rotulo='Mobi · pedágio',
         qtd=PEDAGIO_QTD, un='viagem', unit=PEDAGIO_UNIT,
         obs='ida e volta'),
    dict(rotulo='Airbnb · diária',
         qtd=AIRBNB_QTD, un='diária', unit=AIRBNB_UNIT,
         obs='R$ 900 pelas 4 diárias · ⭐ são os MESMOS 4 dias de '
             'montagem: mexeu num, mexa no outro'),
    dict(rotulo='Alimentação · por pessoa, por dia',
         qtd=ALIMENTACAO_QTD, un='pessoa-dia', unit=ALIMENTACAO_UNIT,
         obs='R$ 440 por pessoa pelos 4 dias · 2 pessoas × 4 dias'),
]
CUSTO_GV = sum(v['qtd'] * v['unit'] for v in LOGISTICA)


# ── ⭐⭐ O DIA DA DUPLA [Jonathan, 19/11/2026] ──────────────────────────
#   "considerando dias de fabricação e dias de montagem. Ambos serão
#    baseados em custo de uma dupla de profissionais, sendo um marceneiro e
#    um ajudante... preencher o campo do custo do dia da dupla (de uma forma
#    que seja um preenchimento único e que se replique em todos os
#    ambientes) e preencha de forma unitária em cada ambiente esse tempo."
#
#   ⭐ UM NÚMERO SÓ, REPLICADO. Na planilha ele mora numa célula amarela da
#     aba "Preço e Comissões" e cada ambiente a referencia — trocar ali
#     move o projeto inteiro.
MARCENEIRO_H = 36.00           # ⭐ Base, Terceirizados · "hora com encargos"
#   ⛔ Era R$ 65 e a Base corrige: "Era 65, que é valor de VENDA, não custo".
#   ⚠ O AJUDANTE NÃO EXISTE NA BASE. 60% do marceneiro é premissa minha, e é
#     o primeiro número que o Jonathan deve trocar.
AJUDANTE_H = MARCENEIRO_H * 0.60
HORAS_DIA = 8.0
DUPLA_DIA = (MARCENEIRO_H + AJUDANTE_H) * HORAS_DIA      # R$ 460,80

#   ⛔⛔ E A EQUIPE NÃO ENTRA NA LOGÍSTICA, senão eu pagaria duas vezes. O
#     bloco de GV paga carreto, carro, cama e comida; a MÃO DE OBRA é dia
#     de dupla, aqui. Esse efeito colateral não aparece em lugar nenhum da
#     planilha — some no total.
#   ⭐ OS DOIS CAMPOS QUE O AMBIENTE DIGITA. São dias de DUPLA, não de
#     pessoa: 6 dias de bancada para 83 peças, 162 ripas coladas e 292 m de
#     filetagem manual; 4 dias de montagem, que são os MESMOS 4 das
#     diárias de Airbnb e dos 4 dias de alimentação.
#   ⚠ E O DIA DE QUEM VAI MEDIR NÃO ESTÁ AQUI. A medição bate-volta paga
#     o deslocamento (R$ 350 por pessoa) e não paga a diária de quem foi:
#     640 km de estrada consomem o dia inteiro. São R$ 288 de um marceneiro
#     sozinho, ou R$ 460,80 se for a dupla. Fica de FORA até o Jonathan
#     dizer — basta somar 1 em DIAS_MONTAGEM.
DIAS_FABRICACAO = 6.0
DIAS_MONTAGEM = 4.0


# ── a cascata · aba Comissões ───────────────────────────────────────────
ENCARGO_BRUTO = 0.05 + 0.02 + 0.005 + 0.005
NOTA_FISCAL = 0.05
CARTAO_PARCELA = 0.012
COMISSOES_INTERNAS = 0.075


def cascata(parcelas=0, rt=0.0, vendedor=0.0):
    cartao = CARTAO_PARCELA * parcelas
    bruto = ENCARGO_BRUTO + cartao
    liquido = 1 - NOTA_FISCAL - cartao
    sobre_liquido = (rt + vendedor) * liquido
    liquido2 = liquido - sobre_liquido
    return 1 - bruto - sobre_liquido - liquido2 * COMISSOES_INTERNAS


BASE_SEM_RT = cascata()
BASE_COM_RT = cascata(rt=0.10)
assert abs(BASE_SEM_RT - 0.8488) < 1e-4
assert abs(BASE_COM_RT - 0.760875) < 1e-9

FAIXA = (0.35, 0.40)

# ── o fechamento ────────────────────────────────────────────────────────
#   ⭐ COM PREÇO CRAVADO, A MC É LIDA, NÃO ESCOLHIDA: MC = BASE − custo ÷ preço.
#   O preço deste job andou três vezes, e o registro fica:
#     17/11  "vamos vender por 53.000"  →  "alias, por 49.800"
#     18/11  as duas bandas viram armário: a R$ 49.800 a MC caiu a 31,07%
#     18/11  "Ajuste o valor para 53.500"  ← vale este
#   ⭐ E ele recompõe o que o escopo novo tinha comido: 34,81% com RT, contra
#     os 31,74% de R$ 49.800. Quase de volta ao piso de 35% da casa.
PRECO_FECHADO = 53500.00
#   ⚠ RT DE 10%, E É LEITURA MINHA — ele não disse. São pranchas executivas
#     de arquiteto, e a regra da casa é "RT 10% quando há parceiro
#     indicando". Orçar COM e não pagar sobra margem; orçar SEM e ter de
#     pagar tira 8,8 pontos de MC. Erro para o lado que não quebra, e o
#     levantamento imprime as duas leituras.
RT = 0.10
BASE = BASE_COM_RT
#   ⭐ [Jonathan, 18/11/2026] "Altere o prazo para 90 dias". Eu tinha lido
#     60 e ele corrigiu — 90 é o que cabe de verdade: a conferência técnica
#     em GV vem ANTES do corte, e só depois dela nasce o plano de corte.
#   ⚠ O pagamento continua sendo leitura minha: 50% + 50%, como ele fechou
#     no JPC na véspera.
PRAZO_DIAS = 90
VALIDADE_DIAS = 7
PAGAMENTO = [('Entrada, na assinatura', 0.50), ('Saldo, na entrega', 0.50)]
assert abs(sum(p for _, p in PAGAMENTO) - 1.0) < 1e-9

PROJETO = 'Sala · painel ripado com nicho'
EXECUTIVO = 'SALA - VISTA 2 (1/50) e NICHO RIPADO (1/30), pág. 18'
