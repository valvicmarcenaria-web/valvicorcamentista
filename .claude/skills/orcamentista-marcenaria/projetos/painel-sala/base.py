# -*- coding: utf-8 -*-
"""PAINEL DA SALA — VISTA 2 · a chapa, a ripa e os preços deste orçamento.

⛔⛔ COPIA-SE O MODELO, NUNCA O ORÇAMENTO. O que vem de fora é a BASE DE
  CUSTOS DA CASA. Nenhum item e nenhum preço de outro cliente entra aqui.

⭐ [Jonathan, 17/11/2026] "O ripado vai só até onde termina a pedra, o nicho
  de pedra. Do nicho de pedra para a direita, o painel vai ser liso com as
  duas portas mimetizadas, mas não vai ser ripado. Considere o projeto, a
  quantidade de ripas, filetagem, tudo conforme o nosso padrão de cotação."
"""
import os as _os

# ── a chapa ─────────────────────────────────────────────────────────────
CHAPA_C, CHAPA_L = 275.0, 185.0
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875 m²
APROV = 0.80
ALT_MAX = CHAPA_C - 2.0                  # 273 — teto de peça sem emenda

#   ⚠⚠ "MDF GIANDUIA TRAMA - DURATEX" É A PRIMEIRA COTAÇÃO A FAZER. Trama
#     é padrão TEXTURIZADO, e a Base tem uma linha só para isso: "CHAPA —
#     COR E ACABAMENTO ESPECIAL · R$ 1.000,00". Orço no genérico de cor
#     (R$ 700) porque é o que a casa cobra por amadeirado de catálogo, e
#     deixo o interruptor: `ESPECIAL=1` roda tudo na linha de R$ 1.000.
#   ⛔ A DIFERENÇA ENTRE AS DUAS EXECUÇÕES É O QUE SE LEVA AO FORNECEDOR.
ESPECIAL = _os.environ.get('ESPECIAL') == '1'
_f = 1000.0 / 700.0 if ESPECIAL else 1.0
PRECO = {
    'MDF Gianduia 18': 700.0 * _f,
    'MDF Gianduia 15': 550.0 * _f,
    #   ⭐ só a estrutura de fixação, que fica atrás do painel e nunca
    #     aparece — 18 mm porque é ela que recebe o parafuso na alvenaria.
    'MDF Branco TX 18': 400.0,
    'MDF Branco TX 15': 350.0,
}

# ── A RIPA DESTE PROJETO NÃO É A RIPA DA CASA ───────────────────────────
#   ⭐⭐ A prancha crava: "RIPADO EM MDF GIANDUIA TRAMA DE 20MM E ESPAÇAMENTO
#     DE 20MM - DURATEX", e o detalhe 1/5 confirma com a cota 2 · 2 · 2.
#   ⛔ O PADRÃO DA CASA É RIPA DE 4 COM VÃO DE 2 — passo de 6. Aqui o passo
#     é 4, e isso não é detalhe de desenho: são 25 ripas por metro em vez
#     de 16,7. CINQUENTA POR CENTO MAIS RIPA E MAIS FILETAGEM por m² de
#     face. Quem copiar o passo da casa erra o orçamento para baixo.
RIPA_L, RIPA_VAO = 2.0, 2.0
PASSO = RIPA_L + RIPA_VAO                # 4,0
RIPA_PERDA = 1.10
RIPA_ESP_MM = 18                         # ⚠ a prancha pede 20 mm de relevo
#   ⛔⛔ E O VÃO TEM 2 CM DE PROFUNDIDADE: enxerga-se o fundo entre as ripas.
#     O substrato NÃO pode ser branco nem cru — sai no MESMO Gianduia. Foi
#     a primeira coisa que eu ia economizar e é a que apareceria na obra.
#   ⭐ E ELE SAI EM 18, NÃO EM 15. Em 15 os 4,41 m² de substrato compravam
#     DUAS chapas só para si (R$ 1.100) e sobravam 3,7 m² de uma cor que
#     mais nada no projeto usa. Em 18 ele entra na mesma pilha do liso e
#     das portas: 19,30 m² em cinco chapas, R$ 3.500 contra R$ 3.900.
#     ⛔ Economia de R$ 400 que não tira nada do móvel — ao contrário: 18 mm
#     segura melhor a ripa de 2 cm colada na frente.
SUBSTRATO_ESP_MM = 18

# ── fita, filetagem e consumíveis ───────────────────────────────────────
FITA_COR = 3.00
FITA_PERDA = 1.10
FILETE_MAQ = 2.50
FILETE_RIPA = FILETE_MAQ                 # R$/m · POR FACE de ripa
CORTE_CHAPA, CORTE_PECA = 2.00, 2.50
CONSUMIVEIS = 0.06
EMBALAGEM = 0.02

# ── terceirizados e ferragem ────────────────────────────────────────────
RIPADO_M2 = 180.0            # ⭐ Terceirizados · painel ripado, mão de obra
LED_M = 150.0                # ⭐ Ferragens · LED COB, conjunto completo
LED_FONTE = 120.0
SISTEMA_PIVO = 120.0         # ⭐ Ferragens · porta mimetizada
FECHO_ROLETE = 75.0
FERRAGEM_PORTA_OCULTA = SISTEMA_PIVO + FECHO_ROLETE      # 195 por folha
FRETE_VIAGEM = 200.0
VIAGENS = 2                  # ⚠ 6,82 m de painel e três folhas de porta

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


BASE_SEM_RT = cascata()                  # 0,8488
BASE_COM_RT = cascata(rt=0.10)           # 0,760875
assert abs(BASE_SEM_RT - 0.8488) < 1e-4
assert abs(BASE_COM_RT - 0.760875) < 1e-9

#   ⚠ O JONATHAN AINDA NÃO DISSE PREÇO, MC NEM RT NESTE PROJETO. Ele pediu
#     o LEVANTAMENTO DE CUSTOS em tabela, antes da proposta. Então aqui não
#     há preço fechado: o levantamento imprime o custo e, só como régua, o
#     preço nos dois extremos da faixa ideal da casa (35% e 40%), nos dois
#     cenários de RT. ⛔ Escolher MC por ele seria responder uma pergunta
#     que ele não fez.
FAIXA = (0.35, 0.40)

# ── o projeto ───────────────────────────────────────────────────────────
#   ⚠ As pranchas não trazem nome de cliente — só "SALA - VISTA 2" e a
#     página 18 do executivo. O nome entra na proposta, não aqui.
PROJETO = 'Sala · painel ripado com nicho'
EXECUTIVO = 'SALA - VISTA 2 (1/50) e NICHO RIPADO (1/30), pág. 18'
