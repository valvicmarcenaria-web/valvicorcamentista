# -*- coding: utf-8 -*-
"""APARTAMENTO JPC — a chapa, a peça e os preços deste orçamento.

⛔⛔ COPIA-SE O MODELO, NUNCA O ORÇAMENTO. O que vem de fora é a BASE DE
  CUSTOS DA CASA — chapa, fita, ferragem e a cascata de encargos —, que é
  dado da Valvic. Nenhum item, nenhuma medida e nenhum preço de outro
  cliente atravessa esta porta.

⭐ [Jonathan, 17/11/2026] "Faça esse orçamento em uma página. Bonito e
  organizado / Prazo de entrega 60 dias / Pagamento 50% + 50% / Ferragens
  Hettich / Preço de venda - R$ 6.700".

⭐ Duas pranchas PR 01 de Helena Antunes Arquitetura e Interiores, junho de
  2026: BANHO SUÍTE e BANHO SOCIAL. Dois gabinetes suspensos sob bancada de
  pedra. É o orçamento inteiro — não há mais nada no escopo.
"""

# ── a chapa ─────────────────────────────────────────────────────────────
CHAPA_C, CHAPA_L = 275.0, 185.0          # cm · Base de Custos
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875 m²
APROV = 0.80                             # aproveitamento

#   ⚠ AS PRANCHAS NÃO NOMEIAM ACABAMENTO. Nenhuma das duas diz cor, padrão
#     ou fornecedor — só hachura de pedra na bancada e linha cheia no
#     gabinete. Orço na linha GENÉRICA DE COR da Base (R$ 700 / 550 / 350),
#     que cobre qualquer amadeirado ou cor lisa de catálogo, e deixo escrito
#     na proposta. ⛔ Padrão especial — sincronizado, alto-relevo, super
#     matte — é a linha de R$ 1.000 da Base e muda o preço: roda com
#     ESPECIAL=1 para ver quanto.
import os as _os
ESPECIAL = _os.environ.get('ESPECIAL') == '1'
MDF_COR_18 = 1000.0 if ESPECIAL else 700.0
PRECO = {'MDF cor 18': MDF_COR_18, 'MDF cor 15': 550.0, 'MDF cor 6': 350.0}

#   ⚠ E ELAS TAMBÉM NÃO DIZEM "MDF RESISTENTE À UMIDADE". Gabinete de
#     banheiro embaixo de cuba é o lugar onde o MDF comum morre primeiro.
#     A Base da casa não tem linha de MDF-H, então o preço acima é o do MDF
#     comum — e a proposta diz, com todas as letras, o que está orçado.

# ── fita e consumíveis ──────────────────────────────────────────────────
FITA_COR = 3.00
FITA_PERDA = 1.10
CORTE_CHAPA, CORTE_PECA = 2.00, 2.50
CONSUMIVEIS = 0.06
EMBALAGEM = 0.02

# ── ferragem · A LINHA DO PROJETO ───────────────────────────────────────
#   ⭐ [Jonathan, 17/11/2026] "Ferragens Hettich" — o degrau Gold da aba
#     Ferragens da Base. Entre os dois Hettich do Gold fico com a SENSYS,
#     a mesma escolha do Charbel: 100 mil ciclos, pistão gel, ajuste 3D.
LINHA = 'Hettich'
DOBRADICA = 50.0                  # Hettich Sensys
DOBRADICA_NOME = 'Dobradiça Hettich Sensys'
CORREDICA_PAR = 150.0             # Hettich Quadro V6 · 30 kg, Silent System
CORREDICA_NOME = 'Corrediça Hettich Quadro V6, par'
#   ⛔⛔ A GARANTIA VALE PELO TIER MAIS BAIXO DO PROJETO [Jonathan,
#     29/10/2026]. Aqui só há Hettich: 10 anos, sem escalonamento.
GARANTIA_ANOS = 10
SUPORTE_JOGO = 6.50               # por prateleira INTERNA, jogo de 4
CAVA_M = 50.0                     # R$/m de frente · puxador cava usinado


def dobradicas(altura_cm):
    """⛔ É contagem, não estimativa: a Base cravou a tabela."""
    if altura_cm <= 90:  return 2
    if altura_cm <= 160: return 3
    if altura_cm <= 200: return 4
    return 5


# ── logística ───────────────────────────────────────────────────────────
#   ⭐ [Jonathan, 29/10/2026] R$ 200 por viagem. ⚠ DUAS, não uma e não
#     quatro: os dois gabinetes cabem no mesmo caminhão e sobem juntos, mas
#     gabinete de banheiro é instalado ANTES da pedra e volta-se depois do
#     assentamento para regular porta e gaveta. A segunda viagem é a do
#     ajuste, e ela existe neste tipo de obra sempre.
FRETE_VIAGEM = 200.0
VIAGENS = 2

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
assert abs(BASE_SEM_RT - 0.8488) < 1e-4

#   ⭐⭐ RT DE 10%, E ESTA É LEITURA MINHA — está escrito aqui porque custa
#     dinheiro. O Jonathan não falou de RT desta vez. Mas o projeto é de
#     Helena Antunes, detalhado prancha a prancha, e no outro job dela a
#     casa pagou RT ["vamos considerar RT", 30/09/2026]. A regra da casa é
#     "RT 10% quando há parceiro indicando", e aqui há.
#   ⛔ O ERRO ASSIMÉTRICO MANDA NA ESCOLHA: orçar COM RT e não pagar sobra
#     margem; orçar SEM e ter de pagar tira R$ 509 de um job de R$ 6.700,
#     que é quase um quinto da margem. Entre errar para cima e errar para
#     baixo num número que não me foi dito, erro do lado que não quebra.
#   ⚠ Sem vendedor: não foi dito, e inventar vendedor são mais 9 pontos.
#   ⭐ 50% + 50% não é cartão parcelado — `parcelas=0`.
RT = 0.10
VENDEDOR = 0.0
BASE = cascata(parcelas=0, rt=RT, vendedor=VENDEDOR)
assert abs(BASE - 0.760875) < 1e-9, BASE

# ── o fechamento ────────────────────────────────────────────────────────
#   ⭐⭐ COM PREÇO CRAVADO, A MC É LIDA E NÃO ESCOLHIDA:
#         MC = BASE − custo direto ÷ preço
#     `levantamento.py` imprime o número e a trava lá confere que o preço
#     volta nos R$ 6.700 exatos.
PRECO_FECHADO = 6700.00
PRAZO_DIAS = 60                  # dias CORRIDOS, da assinatura à entrega
VALIDADE_DIAS = 7
#   ⭐ [Jonathan, 17/11/2026] "Pagamento 50% + 50%". A segunda metade na
#     entrega é o natural da casa, e é o que a folha diz.
PAGAMENTO = [('Entrada, na assinatura', 0.50),
             ('Saldo, na entrega', 0.50)]
assert abs(sum(p for _, p in PAGAMENTO) - 1.0) < 1e-9

# ── o cliente ───────────────────────────────────────────────────────────
#   ⚠ "JPC" é como a prancha chama o apartamento. Não é nome de pessoa e
#     não vou inventar um: a folha sai com o nome do projeto.
PROJETO = 'Apartamento JPC'
ARQUITETA = 'Helena Antunes · Arquitetura e Interiores'
EXECUTIVO = 'Pranchas PR 01 · Banho Suíte e Banho Social · junho de 2026'
