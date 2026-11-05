# -*- coding: utf-8 -*-
"""BAR CARIOCANDO — a chapa, a peça e os preços deste orçamento.

⛔⛔ ESTE ARQUIVO NÃO FOI COPIADO DO ORÇAMENTO DE OUTRO CLIENTE. O que vem
  de fora é a BASE DE CUSTOS DA CASA — preço de chapa, de fita, de ferragem
  e a cascata de encargos —, que é dado da Valvic e não do Attos, do Michel
  nem de ninguém. ⭐ Copia-se o MODELO; nunca o orçamento.

⛔ E O QUE FICOU DE FORA DE PROPÓSITO: estofado, mesa de cabeceira, porta de
  passagem e sistema de correr não existem neste job. Constante que não é
  usada é constante que um dia alguém usa por engano.
"""

# ── a chapa ─────────────────────────────────────────────────────────────
CHAPA_C, CHAPA_L = 275.0, 185.0          # cm · Base de Custos
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875 m²
APROV = 0.80                             # aproveitamento, Base de Custos

# ── chapa, por padrão e espessura ───────────────────────────────────────
#   ⭐ "MDF AMÊNDOLA RÚSTICA, REF.: DURATEX" é melamínico de cor: entra na
#     linha de chapa COLORIDA da Base, igual ao amadeirado do executivo.
PRECO = {
    'MDF cor 18': 700.0, 'MDF cor 15': 550.0, 'MDF cor 6': 350.0,
    'MDF Branco TX 18': 400.0, 'MDF Branco TX 15': 350.0,
    'MDF Branco TX 6': 250.0,
}

# ── fita, filetagem e consumíveis ───────────────────────────────────────
FITA_COR, FITA_BRANCA = 3.00, 2.00       # R$/m, 22 mm
FITA_PERDA = 1.10                        # 10% de desperdício, da própria Base
FILETE_MAQ = 2.50                        # R$/m · coladeira automática
FILETE_RIPA = FILETE_MAQ                 # ⭐ [Jonathan, 04/11/2026] ripa entra na automática
CORTE_CHAPA, CORTE_PECA = 2.00, 2.50     # R$ por chapa comprada / por peça cortada
CONSUMIVEIS = 0.06                       # 6% sobre chapa e fita
EMBALAGEM = 0.02                         # 2% sobre o custo direto

# ── ferragem ────────────────────────────────────────────────────────────
#   ⭐ [Jonathan, 05/11/2026] "faça apenas em uma linha hettich". ⛔ E neste
#     job a linha Hettich NÃO aparece na corrediça — não há uma gaveta no
#     desenho. Ela aparece na DOBRADIÇA, que é a única ferragem de movimento
#     das dez portas. Dizer "linha Hettich" aqui é dizer Sensys.
DOBRADICA = 50.0                  # Hettich Sensys · o mesmo valor cravado em 03/11
SUPORTE_JOGO = 6.50               # por prateleira INTERNA, composição de 4


def dobradicas(altura_cm):
    """⛔ É contagem, não estimativa: a Base cravou a tabela."""
    if altura_cm <= 90:  return 2
    if altura_cm <= 160: return 3
    if altura_cm <= 200: return 4
    return 5


# ── terceirizados ───────────────────────────────────────────────────────
RIPADO_M2 = 180.0        # ⚠ faixa de 70 a 420 na Base, "depende da largura da
                         #   ripa e do vão". A daqui é ripa de 4 com vão de 2 —
                         #   passo de 6, o DOBRO do passo do Attos, portanto a
                         #   metade das peças por metro. ⚠ 180 é o meio da faixa
                         #   e segue por conferir.
RIPA_PERDA = 1.10        # perda de serra ao tirar ripa

# ── a cascata de encargos ───────────────────────────────────────────────
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


BASE_SEM_RT = cascata()                            # 0,84875
BASE_COM_UM = cascata(vendedor=0.10)               # 0,760875
BASE_COM_DOIS = cascata(rt=0.10, vendedor=0.10)    # 0,673
assert abs(BASE_SEM_RT - 0.8488) < 1e-4
assert abs(BASE_COM_UM - 0.7609) < 1e-4
assert abs(BASE_COM_DOIS - 0.6730) < 1e-4

#   ⛔⛔ AQUI MORA A MAIOR ALAVANCA COMERCIAL DESTE ORÇAMENTO, e ela é uma
#     PERGUNTA, não uma conta: este job tem RT de arquiteto? tem vendedor?
#     São dois escritórios assinando a prancha (Chico Albano e Biri) e um
#     cliente comercial. Entre a base sem ninguém e a base com os dois vão
#     quase 18 pontos de preço.
#   ⭐ Enquanto ninguém responde, vale a publicada SEM RT E SEM VENDEDOR —
#     a mais barata das três, que é a escolha que NÃO esconde custo.
BASE = BASE_SEM_RT
MC = 0.38                # ⭐ a MC de referência da casa, linha Hettich
