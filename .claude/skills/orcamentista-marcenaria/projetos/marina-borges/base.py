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

# ── ferragem · TUDO BLUM ────────────────────────────────────────────────
#   ⭐ Os mesmos preços que a casa cravou para a linha Blum em 03 e 04/11.
DOBRADICA = 50.0                  # Blum
CORREDICA_PAR = 300.0             # Blum Movento
#   ⛔ SIFORMA NÃO É BLUM [Jonathan, 09/11/2026]. A Blum é austríaca e faz
#     dobradiça, corrediça e pulsador; o sistema de correr SI Ocean 80 é da
#     SIFORMA. Eu tinha escrito "Blum SI Forma", que é duas empresas numa
#     linha só — e ficha técnica errada é o que o cliente confere.
SISTEMA_CORRER = 900.0            # Siforma SI Ocean 80
BASCULA_HK = 250.0                # Blum AVENTOS HK-XS
PULSADOR = 100.0                  # Blum Tip-on
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
#   ⭐⭐ [Jonathan, 09/11/2026] "vamos fechar o valor de venda em 625k na
#     linha blum". Na planilha ele girou a ALVO para 52% e, com os cinco
#     pontos de piso do quadro ⑤, a MC APLICADA saiu 57% em todos os nove
#     ambientes — preço de R$ 625.048,49. Este MC é a REALIZADA, que é o
#     que entra na conta aqui; a alvo de 52 só existe na planilha.
#   ⛔ 57% está 17 pontos acima da faixa ideal da casa (35% a 40%) e 22
#     acima do piso. Não é mais uma MC de trabalho: é posicionamento. Fica
#     escrito aqui para a próxima pessoa não achar que foi descuido.
MC = 0.57

#   ── o fechamento ─────────────────────────────────────────────────────
#   ⭐ [Jonathan, 09/11/2026], ditado inteiro. O modelo dá R$ 625.048,49 e
#   ⚠ E A DIFERENÇA DEIXOU DE SER ARREDONDAMENTO. Quando ele fechou, o
#     custo direto era R$ 119.306 e o modelo dava R$ 625.048 — R$ 48 de
#     sobra. Tirar o Branco TX do interior levou o custo a R$ 123.133, e a
#     MC de 57% agora pediria R$ 645.097. Manter os 625 mil é absorver
#     R$ 20 mil na margem, que cai de 57,0% para 56,4%. É decisão dele, e
#     fica escrita aqui para ninguém chamar de arredondamento.
PRECO_FECHADO = 625000.00
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
