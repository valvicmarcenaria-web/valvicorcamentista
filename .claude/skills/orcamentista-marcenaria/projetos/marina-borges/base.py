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

#   ⚠⚠ OS CINCO PADRÕES SÃO CINCO MATERIAIS, NÃO UM.
#     O executivo nomeia MDF Caribe Linha Dual Syncro (Guararapes), MDF
#     Cipres (Guararapes), MDF Fontana Linha Magma (Guararapes), MDF Cacao
#     Matt (Arauco) e MDF Cinza Sagrado (Duratex). Eles entram aqui como
#     materiais SEPARADOS porque não se corta Cipres de uma chapa de Caribe
#     — o arredondamento de chapa é por padrão, e com cinco padrões ele
#     pesa cinco vezes.
#   ⛔ O PREÇO ABAIXO AINDA É O GENÉRICO DA BASE. Dual Syncro e Magma são
#     linhas texturizadas de topo e não custam o mesmo que "MDF cor". A
#     cotação real é a primeira coisa a fazer, e mexer num número aqui
#     recalcula o orçamento inteiro.
MDF_COR_18, MDF_COR_15, MDF_COR_6 = 700.0, 550.0, 350.0
PADROES = ('MDF Caribe', 'MDF Cipres', 'MDF Fontana', 'MDF Cacao',
           'MDF Cinza Sagrado')
PRECO = {
    'MDF cor 18': MDF_COR_18, 'MDF cor 15': MDF_COR_15,
    'MDF cor 6': MDF_COR_6,
    'MDF Branco TX 18': 400.0, 'MDF Branco TX 15': 350.0,
    'MDF Branco TX 9': 300.0, 'MDF Branco TX 6': 250.0,
}
#   ⭐⭐ E A BASE TEM A LINHA QUE EU IA INVENTAR: "CHAPA — COR E ACABAMENTO
#     ESPECIAL · R$ 1.000,00 · confirmado em plano de corte". Dual Syncro e
#     Magma são exatamente isso — sincronizado e alto-relevo —, e Cacao Matt
#     é super-matte. Cipres e Cinza Sagrado são padrão amadeirado comum.
#   ⭐ Roda com `ESPECIAL=1` para precificar os três premium nessa linha. A
#     RESPOSTA DA COTAÇÃO É A DIFERENÇA ENTRE AS DUAS EXECUÇÕES — é assim que
#     a dúvida vira um número que se leva ao fornecedor.
import os as _os
ESPECIAL = _os.environ.get('ESPECIAL') == '1'
MDF_ESPECIAL_18 = 1000.0
PREMIUM = ('MDF Caribe', 'MDF Fontana', 'MDF Cacao')
for _m in PADROES:
    _f = MDF_ESPECIAL_18 / MDF_COR_18 if (ESPECIAL and _m in PREMIUM) else 1.0
    PRECO[f'{_m} 18'] = MDF_COR_18 * _f
    PRECO[f'{_m} 15'] = MDF_COR_15 * _f
    PRECO[f'{_m} 6'] = MDF_COR_6 * _f

# ── fita, filetagem e consumíveis ───────────────────────────────────────
FITA_COR, FITA_BRANCA = 3.00, 2.00
FITA_PERDA = 1.10
FILETE_MAQ = 2.50
FILETE_MAO = 5.00
FILETE_RIPA = FILETE_MAQ
CORTE_CHAPA, CORTE_PECA = 2.00, 2.50
CONSUMIVEIS = 0.06
EMBALAGEM = 0.02

# ── ferragem · A LINHA DO PROJETO ───────────────────────────────────────
#   ⭐⭐ [Jonathan, 10/11/2026] "vamos fechar a proposta dela em hettich a
#     397.000". A escada de posicionamento da aba Ferragens da Base tem
#     quatro degraus, e o Gold é Hettich. Entre os dois Hettich do Gold eu
#     fiquei com a SENSYS, não com a Novisys: é a que sustenta o mesmo
#     argumento que a proposta fazia com o Blum — 100 mil ciclos, pistão
#     gel, ajuste 3D, iF Award — e custa os MESMOS R$ 50 da dobradiça Blum
#     na nossa Base. ⚠ A Novisys devolveria R$ 3.182,40 de margem e é a
#     "Silent System econômico": troca de produto, não de preço.
#   ⛔ TODO O GANHO DE SAIR DO BLUM ESTÁ NAS 27 GAVETAS. A dobradiça não
#     muda de preço; a corrediça cai de R$ 300 para R$ 150. São R$ 4.050,
#     R$ 4.161,60 já com a embalagem — e vinte anos de garantia a menos.
LINHA = 'Hettich'
DOBRADICA = 50.0                  # Hettich Sensys · 100 mil ciclos
DOBRADICA_NOME = 'Dobradiça Hettich Sensys'
CORREDICA_PAR = 150.0             # Hettich Quadro V6 · 30 kg, Silent System
CORREDICA_NOME = 'Corrediça Hettich Quadro V6, par'
#   ⛔ SIFORMA NÃO É HETTICH, como não era Blum [Jonathan, 09/11/2026]. O
#     sistema de correr SI Ocean 80 é da SIFORMA, e sai inalterado: ele
#     nunca esteve no degrau que o Jonathan trocou.
SISTEMA_CORRER = 900.0            # Siforma SI Ocean 80
BASCULA_HK = 250.0                # ⚠ ainda Blum AVENTOS HK-XS · não usado neste projeto
PULSADOR = 70.0                   # "Pulsador outros" da Base · era 100 no Tip-on
PULSADOR_NOME = 'Pulsador de abertura por toque'
#   ⛔⛔ A GARANTIA VALE PELO TIER MAIS BAIXO DO PROJETO [Jonathan,
#     29/10/2026]: Blum 30 anos, HETTICH 10, Hardt 5, telescópica 2. Sair
#     do Blum derruba a proposta inteira de 30 para 10 — e a folha "por que
#     Blum" foi escrita em cima dos 30. Este número manda na proposta.
GARANTIA_ANOS = 10
SUPORTE_JOGO = 6.50               # por prateleira INTERNA, jogo de 4
SUPORTE_OCULTO = 30.0             # só prateleira de PAREDE
DESEMPENADOR = 100.0              # toda porta deslizante · 70 cm ou mais leva DOIS
ALMA_BARRA = 50.0                 # barra chata 5 mm, 3 m
CAVA_M = 50.0                     # R$/m de frente · puxador cava usinado
PUXADOR_BOTAO = 45.0              # ⭐ Ferragens · Alças Traso 32 mm, gold escovado
FERRAGEM_PORTA_OCULTA = 120.0 + 75.0   # ⭐ sistema pivô + fecho rolete, da Base


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

#   ⭐⭐ ESTES NÚMEROS SÃO DA BASE DE CUSTOS DA CASA, não meus.
#     Eu tinha escrito onze premissas de mercado aqui. Abri a planilha
#     `Valvic · Base de Custos` e nove delas já existiam — algumas pela
#     METADE do que eu tinha chutado. ⛔ A premissa que a casa já respondeu
#     não é premissa, é desleixo. Cada linha abaixo diz de onde veio.
PORTA_VIDRO_PERFIL = 1400.0  # ⭐ Terceirizados · "Porta de espelho · alumínio
                             #   mais espelho com película · R$ 1.200 + R$ 200
                             #   de frete, cerca de 1.400 posto na obra"
PORTA_CRISTALEIRA = 500.0    # ⭐ Vidro · obra Kenia e Fábio 12/06/2026: porta
                             #   de giro de cristaleira 2,00 × 0,36 = R$ 475,
                             #   cerca de R$ 660 por m²
PORTA_REFLECTA = 450.0       # ⭐ Vidro · reflecta bronze com perfil champanhe,
                             #   por folha
ESPELHO_M2 = 600.0           # ⭐ Vidro · espelho prata  (eu tinha posto 450)
LED_M = 150.0                # ⭐ Ferragens · "LED COB, conjunto completo:
                             #   fita, perfil, usinagem e instalação"
LED_FONTE = 120.0            # ⭐ Ferragens  (eu tinha posto 250)
BOTTON = 50.0                # ⭐ Ferragens · "Sensor ou interruptor"
RODAPE_INOX_M = 85.0         # ⭐ Terceirizados · "Rodapé ou recuo em perfil de
                             #   inox" · ⚠ VER A REGRA DO RODAPÉ, logo abaixo
FRISO_LAQUEADO_M = 160.0     # ⚠ proxy · "Friso em perfil laqueado" é o mais
                             #   perto que a Base tem da fita de latão dourado
SERRALHERIA_M = 180.0        # ⭐ Terceirizados · "estrutura metálica preta
                             #   pronta, por metro linear"
CABIDEIRO = 120.0            # ⭐ Ferragens · por UNIDADE, não por metro
DOBRADICA_VIDRO = 70.0       # ⭐ Ferragens · porta de alumínio e vidro
SISTEMA_PIVO = 120.0         # ⭐ Ferragens · só o sistema
FECHO_ROLETE = 75.0          # ⭐ Ferragens · fecho rolete para porta pivotante
SARRAFO_PINUS_M = 8.0        # ⭐ Ferragens · estrutura interna
PERFIL_PISO_M = 15.0         # ⭐ [Jonathan, 28/10/2026] em TODO painel que
                             #   toca o chão
FRETE_VIAGEM = 200.0         # ⭐ [Jonathan, 29/10/2026]

#   ⛔⛔ A REGRA DO RODAPÉ, e ela contradiz a prancha de propósito.
#     [Jonathan, 26/10/2026] "RODAPÉ E BASE DE 3 CM NÃO É SERRALHERIA. A
#     prancha de arquiteto pede base metálica; nós fazemos em MDF
#     melamínico." ⚠ Aqui a prancha pede RODAPÉ INOX h = 2 em cinco folhas.
#     Orço o inox, porque é o que está desenhado e a Base tem o preço — e
#     deixo escrito que a casa sabe trocar por MDF, e quanto isso devolve.
RODAPE_EM_MDF = False

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
#   ⭐⭐ A MC DEIXOU DE SER ESCOLHIDA E PASSOU A SER LIDA. Até 09/11 o
#     Jonathan girava a MC e o modelo dava o preço. Em 10/11 ele cravou os
#     dois lados — linha Hettich E R$ 397.000 — e aí a MC é o que sobra:
#         MC = base de 76,0875% − custo direto ÷ preço
#     Com o custo de R$ 118.971,23 da linha Hettich, dá 46,1199%.
#   ⛔ AS OITO CASAS NÃO SÃO PRECIOSISMO. Com quatro, o modelo devolve
#     R$ 397.000,85 e a planilha passa a mostrar 85 centavos de diferença
#     contra o preço fechado — um "quase" que alguém um dia vai tentar
#     explicar. Este número foi LIDO do preço, não escolhido: é
#     base − custo ÷ preço, com o custo da linha Hettich.
#   ⭐ 46,1% continua acima da faixa ideal da casa (35% a 40%) e 11 pontos
#     acima do piso de 35%. Não é desconto: é um degrau abaixo do
#     posicionamento de 57% que ele tinha pedido na linha Blum.
MC = 0.46119935

#   ── o fechamento ─────────────────────────────────────────────────────
#   ⭐⭐ [Jonathan, 10/11/2026] "vamos fechar a proposta dela em hettich a
#     397.000". Preço e linha ditados juntos, e é o preço que manda.
#   ⚠ O QUE ISSO MUDA CONTRA O FECHAMENTO ANTERIOR, de 625 mil em Blum:
#         preço    R$ 625.000,00  →  R$ 397.000,00   (−R$ 228.000,00)
#         custo    R$ 123.132,83  →  R$ 118.971,23   (−R$   4.161,60)
#         margem   R$ 352.414,04  →  R$ 183.096,14   (−R$ 169.317,90)
#         MC               56,4%  →          46,1%
#         garantia      30 anos   →        10 anos
#   ⛔⛔ E O EMPATE CAIU PARA 46 DIAS DE FÁBRICA, contra uma entrega
#     prometida de 120 dias corridos. A R$ 4.000 de custo fixo por dia, a
#     margem de R$ 183.096 paga 46 dias de fábrica EXCLUSIVA. Acima disso,
#     397 mil só pagam a casa se outro job correr ao lado. Está escrito
#     aqui porque é a conta que decide, e não é a MC.
PRECO_FECHADO = 397000.00
PRAZO_DIAS = 120                 # dias CORRIDOS, da assinatura à entrega
VALIDADE_DIAS = 7                # validade da proposta
#   40% de entrada + 3 parcelas de 20%, a primeira em 60 dias da assinatura.
#   ⚠ As duas seguintes a 90 e 120 dias é LEITURA MINHA: ele disse só a
#     primeira. Mensal é o natural, e 120 fecha junto com a entrega.
PAGAMENTO = [('Entrada, na assinatura', 0.40, 0),
             ('1ª parcela', 0.20, 60),
             ('2ª parcela', 0.20, 90),
             ('3ª parcela', 0.20, 120)]
assert abs(sum(p for _, p, _ in PAGAMENTO) - 1.0) < 1e-9

# ── o cliente ───────────────────────────────────────────────────────────
#   ⚠ A pasta do Drive chama-se `marina_borges`, que é a ARQUITETA. O nome
#     que vai no orçamento, na planilha e na proposta é o do CLIENTE.
CLIENTE = 'Charbel Chelala'
ARQUITETA = 'Mariana Borges · Arquitetura & Interiores'
PROJETO = 'Apartamento · Belo Horizonte'
EXECUTIVO = 'Executivo OUT/2026 · rev. 3'
