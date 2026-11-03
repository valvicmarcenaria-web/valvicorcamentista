# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — a chapa, a peça e os preços deste orçamento.

⭐ Herdado do motor do Gustavo Raposo, que já carrega as regras cravadas pelo
  Jonathan. O que é regra da casa mora aqui; o que é prancha mora no arquivo
  do ambiente.

⛔ TODO PREÇO AQUI SAI DA `Valvic · Base de Custos`
  (13cZGej-AUTTyWZblqtraTBnc1HUECjT6fy3zy6R5mv4), lida em 03/11/2026.
  Nada é digitado de cabeça; o que a Base não tem entra como A COTAR e o
  orçamento mostra zero e grita — é a REGRA DOS DOIS ESTADOS.

⛔ O QUE ESTE PROJETO TEM DE PARTICULAR:
  1. ⛔⛔ O EXECUTIVO ESTÁ TODO VETORIZADO: zero cota extraível por texto.
     Tudo foi lido no olho, ampliando a prancha.
  2. ⭐ O ACABAMENTO É UM SÓ E AINDA NÃO FOI ESCOLHIDO: "MDF AMADEIRADO A
     DEFINIR". Entra como Melamínico Fosco de cor — 700/550/350 —, que é a
     chapa de cor padrão da casa. Trocar por lâmina natural dobra a chapa.
  3. ⛔ TRAVERTINO ROMANO ESCOVADO É PEDRA E ESTÁ FORA. O painel de jantar
     de 367 × 585 e o revestimento atrás da bancada do escritório são
     travertino, não marcenaria.
  4. ⭐ VIDRO REFLECTA é nosso — é vidro de porta de cristaleira e de
     armário, dentro da marcenaria.
  5. ⭐ O RIPADO É O ITEM DO PROJETO: 626 × 272 na cozinha e 316 × 272 no
     escritório, ripa de 2 cm com vão de 1 — passo de 3 cm.

⛔ Toda medida em CENTÍMETROS, como a prancha. Espessura em mm.
"""

# ── a chapa ─────────────────────────────────────────────────────────────
CHAPA_C, CHAPA_L = 275.0, 185.0          # cm · Base de Custos, "MEDIDA E RENDIMENTO"
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875 m²
APROV = 0.80                             # Base de Custos
SANGRIA = 2.0                            # cm de acerto de corte
ALT_MAX = CHAPA_C - SANGRIA              # ⭐ 273 — o teto de peça sem emenda
#   ⭐ E É POR ISSO QUE A RIPA DE 272 CABE: sobra 1 cm. Fosse 274 e o painel
#     inteiro precisaria de emenda, que é outro projeto.

# ── chapa, por padrão e espessura · Base de Custos, aba MDF ─────────────
PRECO = {
    # "MDF AMADEIRADO A DEFINIR" → Melamínico Fosco, a chapa de cor da casa
    'MDF cor 18': 700.0, 'MDF cor 15': 550.0, 'MDF cor 6': 350.0,
    # interno de armário
    'MDF Branco TX 18': 400.0, 'MDF Branco TX 15': 350.0,
    'MDF Branco TX 6': 250.0, 'MDF Branco TX 9': 300.0,
}

# ── fita, filetagem e consumíveis · aba MDF ─────────────────────────────
FITA_COR = 3.00          # R$/m, 22 mm · somar 10% de desperdício
FITA_BRANCA = 2.00       # R$/m, 22 mm
FITA_PERDA = 1.10        # ⭐ os 10% de desperdício, da própria Base
FILETE_MAQ = 2.50        # R$/m · coladeira automática, 15 e 18 mm
FILETE_MAO = 5.00        # R$/m · ripa e o que não entra na máquina
CONSUMIVEIS = 0.06       # 6% sobre chapa e fita
EMBALAGEM = 0.02         # 2% sobre o custo direto

# ── ferragem · aba Ferragens ────────────────────────────────────────────
#   ⚠⚠ A DOBRADIÇA DO NÍVEL PADRÃO NUNCA FOI CRAVADA. A própria Base diz
#     "⛔ A DEFINIR — fica entre Bigfer Inox Click (R$ 10) e Bigfer Onix
#     (R$ 15)". Uso o TOPO da faixa, que é a escolha conservadora: se vier
#     mais barata, a margem sobe; ao contrário, ela evapora sem avisar.
DOBRADICA = 15.0                  # Bigfer Onix · ⚠ confirmar com o Jonathan
DOBRADICA_VIDRO = 70.0            # ⚠ A COTAR na Base · faixa observada 30 a 85
CORREDICA_PAR = 80.0              # Hardt Invisível P-10 · ⭐ o padrão da casa
SUPORTE_PRAT = 30.0               # suporte oculto · ⭐ de 40 em 40 cm
ALMA_BARRA = 50.0                 # barra chata 5 mm, 3 m
PULSADOR = 100.0                  # Blum Tip-on
FECHO_TOQUE_VIDRO = 45.0          # aba Vidro
CAVA_M = 50.0                     # R$/m de frente · biblioteca do motor
#   ⚠ CONFLITO NA PRÓPRIA BASE: "Cava usinada, por metro de frente" diz
#     R$ 50/m na aba Ferragens e "Usinagem de cava embutida na CNC" diz
#     R$ 25/m na aba Terceirizados. Uso 50 (o conservador) e registro.

# ── dobradiças por porta, pela altura · aba Ferragens ───────────────────
def dobradicas(altura_cm):
    """⛔ É contagem, não estimativa: a Base cravou a tabela."""
    if altura_cm <= 90:  return 2
    if altura_cm <= 160: return 3
    if altura_cm <= 200: return 4
    return 5

# ── terceirizados · aba Terceirizados ───────────────────────────────────
RIPADO_M2 = 180.0        # ⚠ faixa observada de 70 a 420, "depende da largura
                         #   da ripa e do vão". A nossa é ripa de 2 com vão de
                         #   1 — passo de 3 cm, que é FINO e cai na metade cara
                         #   da faixa. ⚠ CONFERIR com o Jonathan antes de fechar.
RIPA_PERDA = 1.10        # "Perda de serra ao tirar ripa", fator da Base
VIDRACEIRO_MIN = 200.0   # mínimo por serviço
SERRALHEIRO_MIN = 300.0  # mínimo por serviço

# ── vidro · aba Vidro ───────────────────────────────────────────────────
#   ⛔⛔ O EXECUTIVO PEDE "VIDRO REFLECTA CRISTAL" E A BASE NÃO TEM ESSE
#     PADRÃO. Tem reflecta prata (340 sem perfil, 410 champanhe, 420 preto),
#     reflecta bronze (380/450/460/470) e um "Reflecta champagne" que está
#     A COTAR desde o projeto da Sandra. Cristal é o tom claro, então o
#     vizinho é a PRATA. Entra como prata com perfil preto e fica marcado:
#     é premissa, não cotação.
VIDRO_FOLHA = 420.0      # reflecta prata com perfil preto · ⚠ PREMISSA
VIDRO_M2_REF = 660.0     # referência de obra: cristaleira 2,00 × 0,36, Kenia
                         # e Fábio · serve de prova de sanidade da folha

# ── a cascata de encargos · aba Comissões ───────────────────────────────
#   ⛔ A BASE MUDA CONFORME TENHA RT E VENDEDOR, e são quase 9 pontos cada.
BASE_SEM_RT = 0.8488     # sem RT e sem vendedor, 0 parcelas
BASE_COM_UM = 0.7609     # com RT OU com vendedor · "o caso mais comum da casa"
BASE_COM_DOIS = 0.6730   # com RT E com vendedor
#   ⚠⚠ QUAL VALE NO ATTOS É PERGUNTA ABERTA. O projeto vem de executivo de
#     arquiteto, o que normalmente puxa RT; mas no Gustavo Raposo, que também
#     veio de arquiteta, a casa fechou SEM RT. Calculo em SEM RT e registro
#     que, havendo RT, o preço sobe ~11,6% para manter a mesma MC.
BASE = BASE_SEM_RT

MC_PISO = 0.35           # piso da casa
MC_FAIXA = (0.35, 0.40)  # faixa ideal


def preco(custo_direto, mc, base=BASE):
    """⛔ PREÇO = custo direto ÷ (BASE − MC). A conta da Base de Custos,
       não uma paralela."""
    assert mc < base, f'MC {mc} não cabe na BASE {base}'
    return custo_direto / (base - mc)


def mc_de(custo_direto, preco_venda, base=BASE):
    return base - custo_direto / preco_venda


# ── a chapa que uma área consome ────────────────────────────────────────
def chapas(area_m2):
    """⛔ NÃO EXISTE 2,7 CHAPAS, SÃO 3 — e cada padrão × espessura puxa no
       mínimo uma chapa, mesmo que leve uma peça só."""
    import math
    return max(1, math.ceil(area_m2 / (CHAPA_M2 * APROV)))


if __name__ == '__main__':
    print(f'chapa {CHAPA_C:.0f} × {CHAPA_L:.0f} = {CHAPA_M2:.4f} m² · '
          f'aproveitamento {APROV:.0%} · peça máxima {ALT_MAX:.0f} cm')
    print(f'BASE {BASE:.2%} · piso de MC {MC_PISO:.0%}')
    for mc in (0.35, 0.40, 0.45):
        print(f'  MC {mc:.0%} → divisor {BASE-mc:.4f} · '
              f'R$ 1.000 de custo vira R$ {preco(1000, mc):,.2f}')
