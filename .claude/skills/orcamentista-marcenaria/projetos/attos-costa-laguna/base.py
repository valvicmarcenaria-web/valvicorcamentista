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
FILETE_MAO = 5.00        # R$/m · o que NÃO entra na máquina
#   ⭐⭐ E A RIPA ENTRA. [Jonathan, 04/11/2026] "a filetagem das reguas pode
#     considerar automatica" e, perguntado o alcance, "todo o ripado do
#     projeto". ⛔ Eu havia escrito o contrário em três lugares — "ripa de 2 cm
#     não entra na coladeira" — e a própria Base diz isso na linha "Filetagem
#     manual": aquela nota também está velha.
#   ⛔ E NÃO ERA POUCO: são 2.595,5 m dos 2.862 m de fita do projeto, 91% dela.
#     A R$ 5,00 davam R$ 12.977,30; a R$ 2,50 dão R$ 6.488,65.
#   ⭐ O preço mora AQUI, numa constante só dele, e não espalhado pelas três
#     chamadas de painel ripado. Para voltar atrás é esta linha, e só ela.
FILETE_RIPA = FILETE_MAQ  # ⭐ a filetagem da ripa · hoje = a automática
CORTE_CHAPA = 2.00       # ⭐ [Jonathan, 28/10/2026] por chapa COMPRADA
CORTE_PECA = 2.50        # ⭐ [Jonathan, 28/10/2026] por PEÇA cortada
#   ⛔⛔ E ESTES DOIS FALTAVAM NO MOTOR. Os últimos orçamentos todos os
#     trazem — a aba de ambiente tem as duas linhas e a Base tem as duas
#     chaves — e o Attos tinha nascido sem. Não é centavo: são 43 chapas e
#     algumas centenas de peças, serviço que a fábrica paga de verdade.
CONSUMIVEIS = 0.06       # 6% sobre chapa e fita
EMBALAGEM = 0.02         # 2% sobre o custo direto

# ── ferragem · aba Ferragens ────────────────────────────────────────────
#   ⚠⚠ A DOBRADIÇA DO NÍVEL PADRÃO NUNCA FOI CRAVADA. A própria Base diz
#     "⛔ A DEFINIR — fica entre Bigfer Inox Click (R$ 10) e Bigfer Onix
#     (R$ 15)". Uso o TOPO da faixa, que é a escolha conservadora: se vier
#     mais barata, a margem sobe; ao contrário, ela evapora sem avisar.
#   ⛔⛔ E ERA AQUI QUE MORAVA UMA DIVERGÊNCIA QUE NÃO DAVA ERRO.
#     Este arquivo guardava a ferragem do nível Hardt/Bigfer (dobradiça R$ 15,
#     corrediça R$ 80) e o `cenarios.py` sobrescrevia por linha (R$ 50 e
#     R$ 150). Resultado: `levantamento.custo()` dizia R$ 67.590 e o cenário
#     Hettich dizia R$ 69.303 — R$ 1.713 de diferença para a MESMA casa, e
#     nenhum dos dois acusava nada.
#   ⭐ ESTE PROJETO NÃO OFERECE O NÍVEL PADRÃO: as duas linhas são Hettich e
#     Blum, e o Jonathan cravou dobradiça R$ 50 nas duas. Então o PADRÃO
#     deste arquivo passa a ser a linha HETTICH, e o cenário Hettich deixa de
#     sobrescrever coisa alguma. Um número só, e a trava no fim do cenarios.py
#     prova que os dois motores fecham no centavo.
DOBRADICA = 50.0                  # ⭐ Hettich e Blum, cravado [Jonathan, 03/11/2026]
DOBRADICA_VIDRO = 70.0
#   ⛔⛔ NÃO É USADA NESTE PROJETO, e a linha fica só para não perder o saber.
#     ⭐ [Jonathan, 04/11/2026] "as dobradiças do item 3, sao normais" — o item 3
#     é o ambiente 03, a Cozinha, e era o único lugar do projeto com dobradiça
#     de porta de vidro: 22 das 26 peças. Respondeu a pendência que eu havia
#     deixado aberta ("A COTAR na Base, faixa de 30 a 85").
#   ⭐ E BATE COM O QUE A PRÓPRIA PRANCHA DIZ: o vidro é "reflecta prata COM
#     PERFIL preto". Folha EMOLDURADA — a dobradiça parafusa no perfil, não no
#     vidro. Dobradiça de vidro é para folha SEM moldura, que este projeto não
#     tem. A premissa errada era minha, não da Base.
#   ⛔ Se algum dia entrar folha de vidro sem perfil, é esta constante que
#     volta — e ela volta A COTAR, com faixa de 30 a 85.
CORREDICA_PAR = 150.0             # ⭐ Hettich Quadro V6 · a linha-base deste projeto
#   ⚠ O Hardt Invisível P-10 de R$ 80 é o padrão da CASA, e segue na Base —
#     mas não é uma das duas linhas que o Attos recebe, então não entra aqui.
#   ⛔⛔ AQUI A BASE E O JONATHAN DISCORDAM, E SÃO R$ 408 NO PROJETO.
#     A Base de Custos importa R$ 800,00 para o "Dominus Rometal, 2 portas";
#     o Jonathan cravou 600 em 03/11/2026, respondendo à minha pergunta:
#     "versão hettich vamos usar Rometal de 600 e na BLUM Siforma de 900".
#     ⭐ A palavra dele é mais nova e é específica DESTE projeto, então vale
#     600 — e o travamento está na linha 49 da aba "Base (importada)" da
#     planilha, com o motivo impresso na própria linha, para ser desfeito
#     numa célula. ⚠ Repare que a Base tem OUTRO sistema a R$ 600, o SS-150,
#     também de 2 portas: é possível que o 600 dele seja esse. Não escolhi
#     por ele — registrei a divergência e segui com o número que ele disse.
SISTEMA_CORRER = 600.0            # ⭐ Rometal, a linha Hettich · Blum usa 900
# ⛔⛔ SÃO DOIS PRODUTOS DIFERENTES E EU USEI O ERRADO.
#   A Base (importada) separa, com todas as letras:
#     "Suporte oculto"        R$ 30,00/un  · ⭐ de 40 em 40 cm ·
#        ⛔ "é o de prateleira de PAREDE, não o jogo de quatro de armário"
#     "Suporte de prateleira" R$  6,50/jogo · ⭐ [Jonathan, 28/10] toda
#        prateleira INTERNA de armário leva composição de 4
#   A regra está na skill, item 2, e eu li e usei o de R$ 30 assim mesmo.
#   Prateleira de cristaleira é INTERNA: vai de jogo.
SUPORTE_JOGO = 6.50               # ⭐ por PRATELEIRA interna, composição de 4
SUPORTE_OCULTO = 30.0             # só prateleira de PAREDE, sem armário em volta
BASCULA_HK = 250.0                # Blum AVENTOS HK-XS · ⭐ a báscula da casa
DESEMPENADOR = 100.0              # ⭐⭐ padrão em TODA porta deslizante, e
                                  #   folha de 70 cm ou mais leva DOIS
SISTEMA_PIVO = 120.0              # só o sistema, sem a folha
#   ⛔ ESTES TRÊS ESTAVAM DIGITADOS DENTRO DO LEVANTAMENTO, soltos. Um preço
#     que mora no meio do quantitativo não aparece quando se confere a
#     tabela de preços — e foi exatamente assim que a dobradiça a R$ 15
#     sobreviveu meia sessão. Preço mora aqui, e só aqui.
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
#   ⛔⛔ E OS R$ 420 SÃO POR METRO QUADRADO, NÃO POR FOLHA.
#     ⭐ [Jonathan, 04/11/2026] "a portas de vidro como por exemplo a da
#     cristaleira do item 3 é calculada pelo mt² ou seja, é 420 o mt quadrado".
#   ⛔ Eu havia lido a linha da Base como PREÇO DE FOLHA, e o erro não era de
#     conta: era de UNIDADE. Unidade errada não dá erro — dá um número.
#     E ele erra nos DOIS sentidos, o que é o que o torna invisível:
#       · a porta da cristaleira tem 70 × 269 = 1,883 m² → R$ 791, não R$ 420
#       · a porta do gourmet tem 47 × 71 = 0,334 m² → R$ 140, não R$ 420
#     Folha grande saía BARATA e folha pequena saía CARA, e o total do projeto
#     ficou só R$ 368 fora — perto o bastante para não chamar atenção.
#   ⚠ A prova de sanidade que eu usei para justificar o "por folha" era esta:
#     uma folha de 2,00 × 0,36 (0,72 m²) a R$ 660/m² dá R$ 475, parecido com
#     420. ⛔ O "parecido" foi o que me convenceu — e o parecido não é prova.
#   ⭐ [Jonathan, 04/11/2026] "atualize o preço da porta em reflecta para 650
#     o mt²". ⛔ Era 420 — o número que eu havia tirado da linha "420 preto"
#     da Base. ⭐ E os 650 confirmam a referência de obra que estava aqui
#     embaixo marcada com ⚠: a cristaleira da Kenia e do Fábio saiu a R$ 660/m²,
#     e eu tinha escrito que "a Base está 36% abaixo dela". Estava mesmo — a
#     referência de obra é que valia, e a diferença de 10 reais entre 650 e 660
#     é o que se espera de duas obras.
#   ⚠ TRAVADO AQUI, como o sistema de correr: a Base de Custos segue com 420
#     na linha "Reflecta prata, perfil preto". A aba Base (importada) imprime
#     o valor importado e o modo de desfazer, na própria linha.
VIDRO_M2 = 650.0         # R$/m² · reflecta prata com perfil preto · ⚠ PREMISSA
VIDRO_M2_REF = 660.0     # ⚠ referência de obra (cristaleira da Kenia e do
                         # Fábio), também por m². A Base está 36% ABAIXO dela:
                         # ou é outro vidro, ou aquela obra levou margem na
                         # linha. Fica registrado, não corrigido.

# ── PORTA DE PASSAGEM · a folha é FEITA, não comprada ───────────────────
#   ⭐⭐ [Jonathan, 04/11/2026] O MÉTODO, nas palavras dele:
#     "para fazer as portas fazemos um sanduiche com duas chapas de 6mm de
#      acabamento na cor especificada com um miolo de chapa Gdoor ... e nos
#      usamos reguas de 15cm em torno da extençao da porta (horizontal e
#      vertical). nas portas ripadas adicionais dois perfis de metalom para
#      evitar empenos ... ja o ripado segue o calculo padrão ... Adicionamos
#      isso mais o custo de cava e o sistema da porta, pivo ou deslizante."
#
#   ⛔ E ISSO MATA A LINHA "PORTA PRONTA". Eu tinha duas portas paradas no
#     orçamento "à espera de decisão" — porta de giro pronta a R$ 530 e porta
#     pivô pronta a R$ 840 — porque não sabia se a casa compra ou fabrica.
#     Fabrica. A dúvida morreu.
#
#   ⭐ G-DOOR, da pesquisa que o Jonathan mandou fazer: é da Guararapes, MDF
#     de BAIXÍSSIMA densidade (360 kg/m³), feito para ENCHIMENTO de porta
#     interna e tamburato — substitui colmeia de papelão e sarrafeado.
#   ⛔ E A CHAPA DELE NÃO É A NOSSA: 275 × 205,5, não 275 × 185. Reaproveitar
#     CHAPA_M2 daria rateio errado, por isso a área tem constante própria.
GDOOR_CHAPA = 600.0               # ⭐ R$/chapa, cravado pelo Jonathan
GDOOR_C, GDOOR_L = 275.0, 205.5   # cm · ficha Guararapes, 2750 × 2055
GDOOR_ESP = 29.2                  # mm · a espessura do miolo
GDOOR_CHAPA_M2 = GDOOR_C * GDOOR_L / 10000          # 5,65125 m²
GDOOR_M2 = GDOOR_CHAPA / (GDOOR_CHAPA_M2 * APROV)   # R$/m² de régua
#   ⚠ O 80% É CONSERVADOR AQUI, e de propósito: tira em régua é o corte mais
#     eficiente que existe. Da chapa saem 13 réguas de 15 × 275 (205,5 ÷ 15),
#     e uma porta de 90 × 260 pede 2,5 delas — 5,2 portas por chapa, R$ 115,38.
#     O rateio de 80% cobra R$ 132,71/m², que dá R$ 127,41. ⛔ É escolha, e é
#     do Jonathan: está registrado para o dia em que ele quiser o corte real.
REGUA_GDOOR = 15.0                # ⭐ "reguas de 15cm em torno da extençao"
PELE_PORTA = 6                    # mm · "duas chapas de 6mm de acabamento"
ESP_PORTA = GDOOR_ESP + 2 * PELE_PORTA              # 41,2 mm de folha
METALON_BARRA = 100.0             # ⭐ "a barra de 3mt do perfil custa 100,00"
METALON_BARRA_M = 3.0
METALON_N = 2                     # ⭐ "adicionais dois perfis de metalom"
#   ⚠ COBRADO POR BARRA, como a alma de aço — não por metro. Dois perfis de
#     2,60 m são 5,20 m e levam DUAS barras; por metro dariam R$ 173,33 em vez
#     de R$ 200. Perguntado ao Jonathan, sem resposta ainda: fica o conservador.

# ── a cascata de encargos · aba Comissões ───────────────────────────────
#   ⛔ A BASE MUDA CONFORME TENHA RT E VENDEDOR, e são quase 9 pontos cada.
#   ⛔⛔ E ESTES TRÊS NÚMEROS ERAM ARREDONDADOS. A Base de Custos PUBLICA
#     84,88% / 76,09% / 67,30%, mas o que ela CALCULA é 0,84875 / 0,760875 /
#     0,673. Usar o publicado custou R$ 10 de diferença entre o meu preço e
#     o da planilha — e R$ 10 que ninguém explica é pior que R$ 10.
#   ⭐ Então a BASE deixa de ser constante e passa a ser a CASCATA, a mesma
#     que a aba Preço e Comissões monta. E a prova de que a fórmula é a
#     certa está no assert abaixo: ela reproduz os TRÊS números publicados.
ENCARGO_BRUTO = 0.05 + 0.02 + 0.005 + 0.005   # NF, margem de erro, serra, manutenção
NOTA_FISCAL = 0.05
CARTAO_PARCELA = 0.012   # ⛔ ACUMULA: 10× são 12%, não 1,2%
COMISSOES_INTERNAS = 0.075   # produção, montagem, projeto, coordenação e gestão,
                             # todas sobre o LÍQUIDO 2


def cascata(parcelas=0, rt=0.0, vendedor=0.0):
    """A BASE — o que sobra do preço para o custo direto e para a margem.

    ⭐ Três degraus, e cada um incide sobre o que sobrou do anterior:
       1) sobre o BRUTO: nota fiscal, cartão, margem de erro, serra, manutenção
       2) sobre o LÍQUIDO (bruto menos NF e cartão): RT e vendedor
       3) sobre o LÍQUIDO 2 (líquido menos RT e vendedor): as cinco comissões
    """
    cartao = CARTAO_PARCELA * parcelas
    bruto = ENCARGO_BRUTO + cartao
    liquido = 1 - NOTA_FISCAL - cartao
    sobre_liquido = (rt + vendedor) * liquido
    liquido2 = liquido - sobre_liquido
    return 1 - bruto - sobre_liquido - liquido2 * COMISSOES_INTERNAS


BASE_SEM_RT = cascata()                       # 0,84875 · publicado 84,88%
BASE_COM_UM = cascata(vendedor=0.10)          # 0,760875 · publicado 76,09%
BASE_COM_DOIS = cascata(rt=0.10, vendedor=0.10)   # 0,673 · publicado 67,30%
#   ⭐⭐ A PROVA: a cascata reproduz os três números que a Base PUBLICA.
#     Se ela errasse a mecânica, não bateria em três pontos diferentes.
assert abs(BASE_SEM_RT - 0.8488) < 0.0001, BASE_SEM_RT
assert abs(BASE_COM_UM - 0.7609) < 0.0001, BASE_COM_UM
assert abs(BASE_COM_DOIS - 0.6730) < 0.0001, BASE_COM_DOIS
#   ⭐ [Jonathan, 03/11/2026] "tem comissão do vendedor (10%)" — resolvido.
#     A BASE sai de 84,88% e vai para **76,09%**, que é a linha "com RT OU com
#     vendedor" da aba Comissões.
#   ⛔⛔ E ISSO NÃO É UM AJUSTE PEQUENO: são 8,79 pontos de BASE. Para manter
#     a MESMA MC o preço sobe 1/(0,7609−mc) ÷ 1/(0,8488−mc) — na MC de 42%,
#     **+25,8%**. Comissão de vendedor não sai da margem: sai do preço.
BASE = BASE_COM_UM

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
