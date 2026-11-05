# -*- coding: utf-8 -*-
"""CHARBEL CHELALA — a chapa, a peça e os preços deste orçamento.

⛔⛔ COPIA-SE O MODELO, NUNCA O ORÇAMENTO. O que vem de fora é a BASE DE
  CUSTOS DA CASA — chapa, fita, ferragem e a cascata de encargos —, que é
  dado da Valvic. Nenhum item, nenhuma medida e nenhum preço de outro
  cliente atravessa esta porta.

⭐ A LINHA DESTE JOB É BLUM, inteira. [Jonathan, 05/11/2026] "considere
  ferragens blum / rt de 10%", e depois a MC: 43% — a mesma que a linha
  Blum levou no Costa Laguna.
"""

# ── a chapa ─────────────────────────────────────────────────────────────
CHAPA_C, CHAPA_L = 275.0, 185.0          # cm · Base de Custos
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875 m²
APROV = 0.80                             # aproveitamento
SANGRIA = 2.0
ALT_MAX = CHAPA_C - SANGRIA              # 273 — teto de peça sem emenda

PRECO = {
    'MDF cor 18': 700.0, 'MDF cor 15': 550.0, 'MDF cor 6': 350.0,
    'MDF Branco TX 18': 400.0, 'MDF Branco TX 15': 350.0,
    'MDF Branco TX 9': 300.0, 'MDF Branco TX 6': 250.0,
}

# ── fita, filetagem e consumíveis ───────────────────────────────────────
FITA_COR, FITA_BRANCA = 3.00, 2.00
FITA_PERDA = 1.10
FILETE_MAQ = 2.50
FILETE_MAO = 5.00
FILETE_RIPA = FILETE_MAQ
CORTE_CHAPA, CORTE_PECA = 2.00, 2.50
CONSUMIVEIS = 0.06
EMBALAGEM = 0.02

# ── ferragem · TUDO BLUM ────────────────────────────────────────────────
#   ⭐ Os mesmos preços que a casa cravou para a linha Blum em 03 e 04/11.
DOBRADICA = 50.0                  # Blum
CORREDICA_PAR = 300.0             # Blum Movento
SISTEMA_CORRER = 900.0            # Blum SI Forma · "na BLUM Siforma de 900"
BASCULA_HK = 250.0                # Blum AVENTOS HK-XS
PULSADOR = 100.0                  # Blum Tip-on
SUPORTE_JOGO = 6.50               # por prateleira INTERNA, jogo de 4
SUPORTE_OCULTO = 30.0             # só prateleira de PAREDE
DESEMPENADOR = 100.0              # toda porta deslizante · 70 cm ou mais leva DOIS
ALMA_BARRA = 50.0                 # barra chata 5 mm, 3 m
CAVA_M = 50.0                     # R$/m de frente · puxador cava usinado


def dobradicas(altura_cm):
    """⛔ É contagem, não estimativa: a Base cravou a tabela."""
    if altura_cm <= 90:  return 2
    if altura_cm <= 160: return 3
    if altura_cm <= 200: return 4
    return 5


# ── terceirizados ───────────────────────────────────────────────────────
RIPADO_M2 = 180.0
RIPA_PERDA = 1.10
VIDRACEIRO_MIN = 200.0
SERRALHEIRO_MIN = 300.0

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


BASE_SEM_RT = cascata()
BASE_COM_UM = cascata(vendedor=0.10)
BASE_COM_DOIS = cascata(rt=0.10, vendedor=0.10)
assert abs(BASE_SEM_RT - 0.8488) < 1e-4
assert abs(BASE_COM_UM - 0.7609) < 1e-4
assert abs(BASE_COM_DOIS - 0.6730) < 1e-4

#   ⭐ [Jonathan, 05/11/2026] "rt de 10%". Sem vendedor — não foi dito, e
#     inventar um vendedor é inventar 8 pontos de preço.
RT = 0.10
VENDEDOR = 0.0
BASE = cascata(rt=RT, vendedor=VENDEDOR)
assert abs(BASE - BASE_COM_UM) < 1e-9, BASE      # 0,760875 · publicado 76,09%
MC = 0.43

# ── o cliente ───────────────────────────────────────────────────────────
#   ⚠ A pasta do Drive chama-se `marina_borges`, que é a ARQUITETA. O nome
#     que vai no orçamento, na planilha e na proposta é o do CLIENTE.
CLIENTE = 'Charbel Chelala'
ARQUITETA = 'Mariana Borges · Arquitetura & Interiores'
PROJETO = 'Apartamento · Belo Horizonte'
EXECUTIVO = 'Executivo OUT/2026 · rev. 3'
