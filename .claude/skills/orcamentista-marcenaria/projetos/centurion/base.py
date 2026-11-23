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

⭐ AS TRÊS DECISÕES DO JONATHAN [23/11/2026]:
    forro            melamínico fosco amadeirado 18 mm, LISO
    nicho            30 cm de profundidade
    painel ex-adesivo  mesmo amadeirado do forro
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
}
COMP_FLEX_C, COMP_FLEX_L = 220.0, 160.0      # a chapa de compensado é outra
COMP_FLEX_M2 = COMP_FLEX_C * COMP_FLEX_L / 10000      # 3,52
COMP_FLEX_REND = COMP_FLEX_M2 * APROV

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
SARRAFO_M = 8.00          # ⭐ "Sarrafo de pinus · Estrutura interna · R$ 8,00/m"
SUPORTE_OCULTO = 30.00    # ⭐ "de 40 em 40 cm"
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
PE_DIREITO = 291.0        # cota da VISTA AA, trecho alto

#   ── os pórticos · VISTA BB e VISTA AA ──
NICHO_L, NICHO_H = 104.1, 193.0     # vão interno · cotas da VISTA BB
NICHO_ABOBADA = 53.0                # a parte curva · raio ≈ 104,1/2 = 52,05
NICHO_RETO = NICHO_H - NICHO_ABOBADA
MOLDURA_L = 12.0                    # ⭐ "largura de 12cm" [Jonathan]
NICHO_PROF = 30.0                   # ⭐ decisão do Jonathan, 23/11/2026
N_NICHOS = 7                        # 5 na VISTA BB + 2 na VISTA AA
PASSAGEM_L = 115.0                  # o arco de passagem, VISTA BB
PRAT_POR_NICHO = 4                  # contadas na VISTA BB ampliada
PRAT_ESP = 18                       # cota 1,8 na VISTA BB
ALIZAR_L = 5.0                      # ⚠ largura do alizar não está em prancha

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
MC_ALVO = 0.35            # o piso da casa · fica em D7 da aba de preço
DIFICULDADE = 'Complexo'  # +20 pontos · fica em D41, célula amarela


def preco(custo, mc=MC):
    """PREÇO = custo ÷ (BASE − MC) · o modelo da casa, igual ao da planilha."""
    return custo / (BASE - mc)
