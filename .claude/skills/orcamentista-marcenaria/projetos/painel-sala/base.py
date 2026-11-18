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
DOBRADICA = 50.0
DOBRADICA_NOME = 'Dobradiça Hettich Sensys'
ESCADA_DOBRADICA = [('Bigfer Inox Click', 10.0), ('Bigfer Onix', 15.0),
                    ('Hettich Novisys', 20.0), ('Hettich Sensys', 50.0)]
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
#   ⭐ O ARMÁRIO SUPERIOR É AÉREO DE VERDADE: a banda de cima vai de 2,17 m
#     a 2,92 m do piso. Porta de girar a essa altura, com 75 cm de largura,
#     abre na cara de quem está embaixo. A Base tem a resposta da casa:
#     "Blum AVENTOS HK-XS · ⭐ A BÁSCULA DA CASA · un · R$ 250,00".
BASCULA_HK = 250.0
BASCULA_NOME = 'Báscula Blum AVENTOS HK-XS'
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
KM_IDA = 320.0                 # ⚠ BH → GV por BR-381 e BR-116
KM_LEVE = 1.20                 # ⚠ utilitário · combustível, pedágio, desgaste
KM_CARGA = 1.80                # ⚠ caminhão com o painel
MARCENEIRO_H = 36.00           # ⭐ Base, Terceirizados · "hora com encargos"
#   ⛔ Era R$ 65 e a Base corrige: "Era 65, que é valor de VENDA, não custo".
HORAS_DIA = 8.0
HOSPEDAGEM_NOITE = 180.0       # ⚠ por pessoa, por noite
ALIMENTACAO_DIA = 80.0         # ⚠ por pessoa, por dia

#   ⭐ CONFERÊNCIA TÉCNICA — ela vem ANTES do corte, e é ela que transforma
#     "as medidas deverão ser conferidas no local" em medida de fábrica.
#     Um técnico, um dia e meio com a estrada, uma noite fora.
CONFERENCIA = dict(rotulo='Conferência técnica, antes do corte',
                   pessoas=1, dias=1.5, noites=1, km=KM_LEVE)
#   ⭐ INSTALAÇÃO — 6,82 m de painel, três folhas de porta mimetizada e a
#     estrutura chumbada na alvenaria. Dois montadores, três dias de obra,
#     duas noites fora.
INSTALACAO = dict(rotulo='Instalação em ' + OBRA,
                  pessoas=2, dias=3.0, noites=2, km=KM_CARGA)


def viagem(v):
    """Custo de uma ida a GV: veículo, mão de obra, cama e comida."""
    return dict(
        veiculo=KM_IDA * 2 * v['km'],
        equipe=v['pessoas'] * v['dias'] * HORAS_DIA * MARCENEIRO_H,
        hospedagem=v['pessoas'] * v['noites'] * HOSPEDAGEM_NOITE,
        alimentacao=v['pessoas'] * v['dias'] * ALIMENTACAO_DIA)


LOGISTICA = [CONFERENCIA, INSTALACAO]
CUSTO_GV = sum(sum(viagem(v).values()) for v in LOGISTICA)

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
#   ⭐⭐ [Jonathan, 17/11/2026] "vamos vender por 53.000 esse projeto" e, um
#     minuto depois, "alias, por 49.800". Vale o segundo.
#   ⭐ COM PREÇO CRAVADO, A MC É LIDA, NÃO ESCOLHIDA: MC = BASE − custo ÷ preço.
PRECO_FECHADO = 49800.00
#   ⚠ RT DE 10%, E É LEITURA MINHA — ele não disse. São pranchas executivas
#     de arquiteto, e a regra da casa é "RT 10% quando há parceiro
#     indicando". Orçar COM e não pagar sobra margem; orçar SEM e ter de
#     pagar tira 8,8 pontos de MC. Erro para o lado que não quebra, e o
#     levantamento imprime as duas leituras.
RT = 0.10
BASE = BASE_COM_RT
#   ⚠ Prazo e pagamento também não foram ditos. 60 dias corridos cabem na
#     conferência técnica, nos cinco dias de fábrica e nas duas viagens a
#     GV; 50% + 50% é o que ele fechou no JPC hoje de manhã.
PRAZO_DIAS = 60
VALIDADE_DIAS = 7
PAGAMENTO = [('Entrada, na assinatura', 0.50), ('Saldo, na entrega', 0.50)]
assert abs(sum(p for _, p in PAGAMENTO) - 1.0) < 1e-9

PROJETO = 'Sala · painel ripado com nicho'
EXECUTIVO = 'SALA - VISTA 2 (1/50) e NICHO RIPADO (1/30), pág. 18'
