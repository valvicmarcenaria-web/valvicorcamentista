# -*- coding: utf-8 -*-
"""CENTURION MOTORS · showroom em Vila da Serra — a BASE DE CUSTOS deste job.

⭐ Projeto CLS Arquitetas Associadas, prancha 01 de 17/11/2025, revisão 00.
  Pranchas lidas: "554_Centurion ADESIVO ESPELHO E TINTA 01" (planta de
  forro) e "02" (vistas AA, BB e CC), mais o moodboard "Apresentacao
  Centurion_". Todos os números abaixo saem OU da prancha OU da Base de
  Custos da casa (13cZGej-...), nunca da minha memória.

⛔⛔ A LEGENDA DA PRANCHA DECIDE O ESCOPO, e ela tem quatro símbolos:
      ADESIVO            hachura rosa      → ⭐ VIRA PAINEL DE MDF
      ESPELHO            hachura diagonal  → ⛔ não é marcenaria
      MDF LAQUEADO CAFE  marrom sólido     → ⭐ os pórticos curvos
      TINTA PAREDE SW6069 hachura bege     → ⛔ é pintura, não é nossa
  ⚠ Eu quase li a hachura bege (que cobre quase toda a parede nas três
    vistas) como MDF laqueado. Não é: é TINTA. Só o marrom SÓLIDO é
    nosso. Ler a legenda antes de contar área foi o que salvou o
    orçamento de dobrar de tamanho sem motivo.

⭐ AS DECISÕES DO JONATHAN [23/11/2026], na ordem em que chegaram:
    forro              melamínico fosco amadeirado 18 mm, LISO
    nicho              30 cm de profundidade
    painel ex-adesivo  mesmo amadeirado do forro
    espelho            dois itens: o painel que recebe, e o espelho
    compensado flex.   R$ 600,00 a chapa
    laca               R$ 650,00 o m²
    MC                 55% (alvo 35% + COMPLEXO)
  ⭐ e as respondidas na própria planilha, na coluna ao lado da dúvida:
    arcos              MDF BRANCO — "Os arcos podem ser em mdf branco"
    fundo do nicho     MDF de 6 mm — "os fundos serao em mdf de 6mm"
    alizar             12 cm — "o alizar o projeto mostra 12cm"
    prateleiras        6 por nicho, 30 mm em duas peças de 15 mm
    amadeirado         R$ 700,00 — fica no genérico de cor
    estruturação       5 chapas brancas de 15 mm
    grafia do cliente  confirmada
  ⛔ e a regra que apagou quatro linhas: "nao usamos sarrafo de pinus".
"""
import math

# ── a chapa · aba MDF ───────────────────────────────────────────────────
CHAPA_C, CHAPA_L = 275.0, 185.0
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000        # 5,0875
APROV = 0.80                                 # rende 4,07 m² por chapa
REND = CHAPA_M2 * APROV

#   ⭐ "MDF Melamínico Fosco · Amadeirado e cor · Velluto, Essencial Wood,
#     Premium, Essencial" — a chapa de cor padrão da casa [Jonathan,
#     26/10/2026]. O padrão exato do amadeirado ainda não foi escolhido
#     pela arquiteta; entra no genérico de cor.
PRECO = {
    'MDF Amadeirado 18': 700.0,
    'MDF Amadeirado 15': 550.0,
    'MDF Amadeirado 6':  350.0,
    'MDF Branco TX 18':  400.0,
    'MDF Branco TX 15':  350.0,
    'MDF Branco TX 6':   250.0,
    #   ⭐⭐ R$ 600,00 A CHAPA, PREÇO DO JONATHAN [23/11/2026: "Compensado
    #     flexivel, custo - 600,00 a chapa"]. ⛔ Não é número da Base: a
    #     Base só tem compensado COMUM, em chapa de 1600 × 2200, a R$ 150
    #     (4 mm), e flexível é outro produto. Eu havia ESTIMADO 2,5× o
    #     comum, R$ 375 — o número dele é 60% mais alto, e é o que vale.
    #     ⭐ DÚVIDA FECHADA: era a primeira cotação a fazer da folha.
    'Compensado flexível 4': 600.0,
    #   ⭐ a fórmica do intradorso · R$ 150,00 a folha de 120 × 315
    'Fórmica 1': 150.0,
}
COMP_FLEX_C, COMP_FLEX_L = 220.0, 160.0      # a chapa de compensado é outra
COMP_FLEX_M2 = COMP_FLEX_C * COMP_FLEX_L / 10000      # 3,52
COMP_FLEX_REND = COMP_FLEX_M2 * APROV

# ── a fórmica do intradorso · [Jonathan, 23/11/2026] ───────────────────
#   ⭐⭐ "adicione um revestimento de formica no intradorso. a formica tem a
#     dimensao de 120X315 e custa 150,00 a folha"
#   ⭐⭐ E ISSO FECHA A DÚVIDA QUE EU HAVIA LEVANTADO. Eu tinha escrito que o
#     intradorso é compensado flexível de 4 mm, com veio e emenda, e que a
#     linha de laca da Base fala de "peça LISA" — então havia de confirmar
#     se os R$ 650 o m² cobriam massa e selador sobre compensado cru. A
#     fórmica é a resposta: ela TRANSFORMA o compensado em peça lisa, e aí
#     a linha de R$ 650 vale pelo que diz.
#   ⚠ A Base tem "Fórmica, laminado de alta pressão · Revestimento sobre
#     painel · a partir de R$ 400,00", sem dizer de que folha. O número
#     dele é R$ 150,00 pela folha de 120 × 315, e é o que vale.
FORMICA = 'Fórmica'
FORMICA_ESP = 1                              # ~0,8 mm · a chave pede inteiro
FORMICA_C, FORMICA_L = 315.0, 120.0
FORMICA_M2 = FORMICA_C * FORMICA_L / 10000   # 3,78
FORMICA_REND = FORMICA_M2 * APROV            # 3,024
FORMICA_PRECO = 150.00

# ── a cola de contato · [Jonathan, 23/11/2026] ─────────────────────────
#   ⭐ "acrescente mais uma lata de cola de contato de 14k no custo dos
#     nichos - custo de 600,00"
#   ⭐ "MAIS uma lata" porque a cola comum já está nos CONSUMÍVEIS, que são
#     6% sobre chapa e fita e cobrem "cola, lixa, parafuso, cavilha,
#     tapa-furo". Esta é uma lata INTEIRA a mais, e faz sentido: colar
#     laminado em superfície curva come cola de contato como nada.
COLA_LATA = 600.00
COLA_KG = 14

# ── o rendimento, por material ─────────────────────────────────────────
#   ⛔ Eram dois `if` espalhados em três arquivos — "COMP_FLEX_REND se o
#     material é compensado, senão REND". Com a fórmica entrando, viraria
#     três, e o terceiro é onde se esquece um. ⭐ Um dicionário só, e quem
#     pergunta usa `b.rend(material)`: material novo com folha própria se
#     acrescenta AQUI e nada mais precisa saber dele.
FLEX = 'Compensado flexível'
REND_DE = {FLEX: COMP_FLEX_REND, FORMICA: FORMICA_REND}
FOLHA_DE = {FLEX: (COMP_FLEX_C, COMP_FLEX_L),
            FORMICA: (FORMICA_C, FORMICA_L)}


def rend(material):
    """m² úteis por folha do material, já com o aproveitamento."""
    return REND_DE.get(material, REND)


def folha(material):
    """(comprimento, largura) da folha em cm."""
    return FOLHA_DE.get(material, (CHAPA_C, CHAPA_L))

# ── quem vai em que chapa · as respostas dele, uma a uma ───────────────
#   ⭐⭐ O ARCO VAI EM MDF BRANCO [Jonathan, 23/11/2026]: "Os arcos podem
#     ser em mdf branco". ⭐ É óbvio depois de dito: o pórtico é LACADO
#     CAFÉ, a laca cobre tudo, então pagar R$ 700 de chapa amadeirada para
#     escondê-la sob laca é jogar dinheiro fora. Branco 18 custa R$ 400 ·
#     vale para a costela E para o alizar, que também é lacado.
ARCO_MAT = 'MDF Branco TX'
ARCO_ESP = 18
#   ⭐⭐ O FUNDO DO NICHO VAI EM 6 mm [Jonathan, 23/11/2026]: "os fundos
#     serao em mdf de 6mm". A Base concorda em dois lugares: "MDF Branco TX
#     · Fundos · 6 mm" e a tabela de espessura, "Fundos · 6 mm · Duplo
#     revestimento · por encaixe em rasgo, SEM FITA".
#   ⚠ Mas o fundo AQUI é a face que se vê dentro do nicho — era ADESIVO na
#     prancha — logo vai AMADEIRADO de 6 mm (R$ 350), não branco.
FUNDO_ESP = 6
#   ⭐ A prateleira é peça vista, amadeirada, em duas camadas de 15 mm
#     (R$ 550 a chapa).
PRAT_MAT = 'MDF Amadeirado'

# ── fita e filetagem · aba MDF ─────────────────────────────────────────
FITA_22, FITA_PERDA = 3.00, 1.10
FILETE_MAQ, FILETE_MAO = 2.50, 5.00

# ── corte · base da casa ───────────────────────────────────────────────
CORTE_CHAPA, CORTE_PECA = 2.00, 2.50

# ── percentuais · aba MDF ──────────────────────────────────────────────
CONSUMIVEIS = 0.06        # sobre chapa e fita
EMBALAGEM = 0.03          # ⭐ 3%, como o Jonathan fixou em 19/11/2026

# ── ferragens e iluminação · aba Ferragens ─────────────────────────────
ALMA_BARRA = 50.00        # barra chata 5 mm, 3 m · uma por peça
ALMA_M = 300.0            # a barra tem 3 m
SUPORTE_OCULTO = 30.00    # ⭐ "de 40 em 40 cm"

# ── a estruturação · ⛔⛔ NÃO USAMOS SARRAFO DE PINUS ───────────────────
#   ⛔ [Jonathan, 23/11/2026] "nao usamos sarrafo de pinus". Eu havia
#     lançado 532,57 m de sarrafo a R$ 8,00 — R$ 4.260,59 — em quatro
#     linhas: barroteamento do forro, mão amiga, montante dos painéis e
#     montante da base do espelho. TODAS saem.
#   ⭐ E a Base já dizia o que entra, em dois lugares que eu não cruzei:
#       "MDF Branco TX · Estrutura e caixaria · 15 mm · R$ 350,00"
#       tabela ESPESSURA PADRÃO POR APLICAÇÃO: "Estrutura e caixaria · 15 mm"
#     A casa estrutura com CHAPA cortada em tira, não com madeira de lei.
#   ⭐ O número do forro é dele: "Considere 5 chapas brancas de 15mm para
#     estruturação" [23/11/2026], respondendo à dúvida da mão amiga.
ESTRUT = 'MDF Branco TX'
ESTRUT_ESP = 15
ESTRUT_CHAPAS_FORRO = 5   # ⭐ cravado pelo Jonathan · barrote + mão amiga
TIRA_L = 7.0              # ⚠ largura da tira de estrutura: premissa minha
#   ⭐ A Base avisa em caixa alta: "O LED INSTALADO APARECE DE R$ 66 A
#     R$ 150 POR METRO nos jobs, conforme entre só o perfil ou o conjunto
#     com fita, fonte, usinagem e instalação. Antes de orçar, fechar o que
#     a linha inclui." Fechado: CONJUNTO COMPLETO, porque o Jonathan pediu
#     "prateleiras ... com iluminação de led" — prateleira que acende.
LED_M = 150.00            # LED COB, conjunto completo
LED_FONTE = 120.00        # uma a cada 8 a 10 m

# ── terceirizados · aba Terceirizados ──────────────────────────────────
#   ⭐⭐ R$ 650,00 O m², DECISÃO DO JONATHAN [23/11/2026: "laca considere
#     650"]. É a linha ALTA da Base — "Laca ou pintura em peça lisa",
#     R$ 650,00/m², do materiais.json — e não a de R$ 300,00 dos jobs, que
#     eu havia lançado (faixa de 210 a 650).
#   ⭐ E faz sentido: as duas linhas da Base falam de peça LISA, e pórtico
#     curvo não é peça lisa. Lixar e lacar curva leva mais tempo, então o
#     TETO da faixa é o lugar certo. DÚVIDA FECHADA.
LACA_M2 = 650.00
MARCENEIRO_H = 36.00

# ── o dia da dupla · mecanismo do Jonathan [19/11/2026] ────────────────
#   ⭐ Um marceneiro mais um ajudante, 8 h. O Jonathan cravou R$ 500,00 na
#     célula única da planilha do Painel da Sala; repito aqui.
DUPLA_DIA = 500.00

# ── a geometria, lida das pranchas ─────────────────────────────────────
FORRO_M2 = 157.0          # ⭐ CRAVADO na prancha 01: "ÁREA FORRO 157m²"
#   ⭐⭐ O FORRO VAI EM 15 mm [Jonathan, 23/11/2026]: "as chapas do teto
#     podem ser de 15mm". Eram 18 mm, a R$ 700 a chapa; 15 mm custa R$ 550.
#   ⭐ E faz sentido mais do que pelo preço: forro PENDE DA LAJE, então
#     cada quilo a menos é menos esforço na fixação e na mão amiga. A
#     chapa de 15 pesa cerca de 17% menos que a de 18 — numa área de
#     157 m², são quase 200 kg de diferença pendurados no teto.
#   ⚠ A contrapartida é a barriga entre barrotes: 15 mm cede mais que 18,
#     e a malha de cerca de 75 × 120 que as 5 chapas de estruturação dão
#     pode ter de fechar. Está dimensionado nas dúvidas.
FORRO_ESP = 15
PE_DIREITO = 291.0        # cota da VISTA AA, trecho alto

#   ── os pórticos · VISTA BB e VISTA AA ──
NICHO_L, NICHO_H = 104.1, 193.0     # vão interno · cotas da VISTA BB
NICHO_ABOBADA = 53.0                # a parte curva · raio ≈ 104,1/2 = 52,05
NICHO_RETO = NICHO_H - NICHO_ABOBADA
MOLDURA_L = 12.0                    # ⭐ "largura de 12cm" [Jonathan]
NICHO_PROF = 30.0                   # ⭐ decisão do Jonathan, 23/11/2026
N_NICHOS = 7                        # 5 na VISTA BB + 2 na VISTA AA
PASSAGEM_L = 115.0                  # o arco de passagem, VISTA BB

#   ⭐⭐ A PRATELEIRA, COMO O JONATHAN MANDOU [23/11/2026]: "considere 6 em
#     cada, com 30mm de espessura, duas peças de 15mm". Eu havia contado 4
#     na VISTA BB e lançado 18 mm de uma peça.
#   ⛔ São DUAS mudanças que se multiplicam: 6 em vez de 4 (+50%) e duas
#     peças em vez de uma (×2) — a área de chapa triplica, de 8,74 m² para
#     26,23 m². E o LED e a alma de aço seguem o NÚMERO de prateleiras.
#   ⭐ 30 mm num vão de 104 cm é coerente com a Base, que manda 18 mm acima
#     de 70 cm de vão: aqui o vão é maior e a peça é mais grossa, com alma.
PRAT_POR_NICHO = 6
PRAT_ESP = 30                       # ⭐ 30 mm montados
PRAT_CAMADAS = 2                    # ⭐ duas peças de 15 mm coladas
PRAT_ESP_PECA = 15

#   ⭐ O ALIZAR TEM 12 cm [Jonathan, 23/11/2026]: "o alizar o projeto mostra
#     12cm". Eu havia lançado 5 cm como premissa, e estava errada: ele tem a
#     mesma largura da moldura, o que faz sentido numa peça que arremata
#     contra a parede · ⛔ isso mais que dobra a área do alizar, e o alizar
#     é peça LACADA, logo a laca sobe também.
ALIZAR_L = 12.0

#   ── os espelhos · VISTA AA e VISTA CC ──
#   ⭐ [Jonathan, 23/11/2026] "os espelhos vamos fazer da seguinte forma.
#     Um item considerando os paineis para receber a colagem dos espelhos.
#     e outro item com os espelhos."
#   ⛔ Isso TIRA o espelho de "o que não é marcenaria". A regra da casa é
#     que espelho e vidro só entram quando fazem parte do MÓVEL — e agora
#     fazem: nós entregamos o painel e colamos o espelho nele.
#   ⚠ A Base avisa duas coisas na aba Vidro, e as duas mudam cronograma:
#     "Vidraceiro. A medida sai depois do móvel montado, nunca antes." e
#     "O VIDRO ENTRA PELA ÁREA DA FOLHA, não pelo vão."
ESPELHO_M2_PRECO = 600.00      # "Espelho prata · R$ 600,00/m²"
ESPELHO_FRETE = 200.00         # "Frete de espelho · serviço"
#     (rótulo, largura, altura) — cota a cota
ESPELHOS = [
    ('VISTA AA \u00b7 espelho de 350', 350.0, 207.0),
    ('VISTA CC \u00b7 espelho de 745', 745.0, 220.0),
]
#   ⭐ O SUBSTRATO N\u00c3O \u00c9 AMADEIRADO. Ele some inteiro sob o espelho, ent\u00e3o
#     vai em Branco TX 18: R$ 400 a chapa contra R$ 700. Espelho colado
#     pede base plana e est\u00e1vel, e 18 mm \u00e9 o que a Base manda para pe\u00e7a
#     que n\u00e3o pode empenar.
ESPELHO_SUBSTRATO = 'MDF Branco TX'

#   ── os painéis que eram adesivo · as três vistas ──
#     (rótulo, largura, altura) — cada um lido da sua cota
PAINEIS = [
    ('VISTA AA · três painéis de 95',        3 * 95.0, 291.0),
    ('VISTA AA · painel de 102',                 102.0, 291.0),
    ('VISTA AA · moldura do espelho, laterais',   60.0, 227.0),
    ('VISTA AA · moldura do espelho, topo',      350.0,  20.0),
    ('VISTA CC · faixa corrida de 709',          709.0, 220.0),
    ('VISTA BB · parede dos quadros',            474.0, 220.0),
]


def arco(raio_interno, reto, largura=MOLDURA_L):
    """Um pórtico, em números. Devolve os três perímetros que mandam no
    material: o de dentro (intradorso), o de fora (extradorso) e o do
    eixo da moldura, que é o que vale para a face vista e o alizar."""
    ri, re = raio_interno, raio_interno + largura
    rm = raio_interno + largura / 2
    return dict(interno=2 * reto + math.pi * ri,
                externo=2 * reto + math.pi * re,
                medio=2 * reto + math.pi * rm,
                #   ⛔ o retângulo que o recorte ocupa na chapa: é ELE que
                #     se compra, não o perímetro. O miolo volta ao plano de
                #     corte, e isso está escrito na folha.
                envolvente_l=2 * re,
                envolvente_a=reto + re)


NICHO = arco(NICHO_L / 2, NICHO_RETO)
PASSAGEM = arco(PASSAGEM_L / 2, NICHO_RETO)

# ── a cascata · a mesma do Painel da Sala, conferida com o Jonathan ────
NOTA_FISCAL = 0.09
ENCARGO_BRUTO = NOTA_FISCAL + 0.02 + 0.005 + 0.005
CARTAO_PARCELA = 0.012
COMISSOES_INTERNAS = 0.075


def cascata(parcelas=0, rt=0.0, vendedor=0.0):
    cartao = CARTAO_PARCELA * parcelas
    bruto = ENCARGO_BRUTO + cartao
    liquido = 1 - NOTA_FISCAL - cartao
    sobre_liquido = liquido * (rt + vendedor)
    liquido2 = liquido - sobre_liquido
    return 1 - bruto - sobre_liquido - liquido2 * COMISSOES_INTERNAS


BASE_SEM_RT = cascata()
BASE_COM_RT = cascata(rt=0.10)
assert abs(BASE_SEM_RT - 0.81175) < 1e-9, BASE_SEM_RT

RT = 0.0
BASE = BASE_SEM_RT
FIXO_DIA = 4000.0         # custo fixo por dia de fábrica · para o empate

# ── a margem · [Jonathan, 23/11/2026] "aplique a mc de 55%" ────────────
#   ⭐⭐ 55% é MC APLICADA, e na planilha ela não se digita: é a MC ALVO do
#     projeto MAIS os pontos da DIFICULDADE do ambiente. O quadro ⑤ da aba
#     Preço e Comissões tem a tabela:
#         Médio     +5     "marcenaria de caixa, o que a fábrica faz todo dia"
#         Difícil   +10    "usinagem de relevo, palhinha, segundo ofício"
#         Complexo  +20    "três ou mais ofícios, geometria fora de esquadro,
#                           estrutura metálica aparente ou peça que não cabe
#                           em chapa inteira"
#     ⛔ E a própria aba avisa: "Médio é o PISO, não o zero".
#   ⭐ Então 55% cai EXATAMENTE na tabela da casa, sem forçar nada: MC alvo
#     no piso de 35% + COMPLEXO (20) = 55%. E Complexo é a classificação
#     honesta deste ambiente, critério por critério: são quatro ofícios
#     (marcenaria, laca, vidraceiro e elétrica de LED), os oito arcos são
#     geometria fora de esquadro, e o forro de 157 m², a faixa de 709 e o
#     espelho de 745 não cabem em chapa inteira. Três dos quatro batem.
MC = 0.55
#   ⭐⭐ E ELE ESCOLHEU O OUTRO CAMINHO PARA OS MESMOS 55% [23/11/2026]: em
#     vez do piso de 35% mais COMPLEXO (20 pontos), digitou MC alvo de 50%
#     e deixou a dificuldade em MÉDIO (5 pontos). 50 + 5 = 55, igual.
#   ⭐ A diferença não é de preço, é de onde a margem está ANCORADA: na
#     escolha do projeto, e não na complexidade do ambiente. Faz sentido
#     para quem não quer usar a dificuldade como alavanca.
#   ⚠ Mas tem uma consequência: se entrar um segundo ambiente simples,
#     ele herda a alvo de 50% e sai também a 55%, quando a tabela da casa
#     o poria em 40%. Com um ambiente só, dá no mesmo.
MC_ALVO = 0.50            # ⭐ o número dele · fica em D7 da aba de preço
DIFICULDADE = 'Médio'     # ⭐ fica em D41, célula amarela
#   ⛔ A TABELA DO QUADRO ⑤, COMO DADO E NÃO COMO TEXTO SOLTO. Eu tinha
#     "(20 pontos)" cravado numa linha de print, e quando o Jonathan trocou
#     COMPLEXO por MÉDIO a linha passou a dizer "Médio (20 pontos)" — que
#     é falso, Médio vale 5. Número que descreve outro número tem de ser
#     DERIVADO dele, nunca digitado ao lado.
PONTOS = {'Médio': 0.05, 'Difícil': 0.10, 'Complexo': 0.20}
assert abs(MC_ALVO + PONTOS[DIFICULDADE] - MC) < 1e-9, (MC_ALVO, DIFICULDADE, MC)


def preco(custo, mc=MC):
    """PREÇO = custo ÷ (BASE − MC) · o modelo da casa, igual ao da planilha."""
    return custo / (BASE - mc)
