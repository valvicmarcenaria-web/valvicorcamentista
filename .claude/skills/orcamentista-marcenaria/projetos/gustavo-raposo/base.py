# -*- coding: utf-8 -*-
"""O comum de todo ambiente do GUSTAVO RAPOSO: a chapa, a peça, a gaveta e
os preços. Casa inteira no Condomínio Vale dos Pinhais, Nova Lima (MG),
executivo da arquiteta Luiza Pacheco, Rev.00 de março de 2026.

⭐ Herdado do motor do ICA, que já carregava as regras cravadas pelo Jonathan
  em 28/10/2026 — cada uma nascida de um erro real. O que é regra da casa
  mora aqui; o que é prancha mora no arquivo do ambiente.

⛔ O QUE MUDA EM RELAÇÃO AO ICA, e por quê:
  1. A FERRAGEM É HETTICH NA CASA TODA, 10 anos de garantia uniformes.
  2. NOVE PADRÕES de MDF Duratex, todos de cor — nove arredondamentos.
  3. A COZINHA É LACA SAYERLACK M048, não melamínico: MDF cru mais pintura.
  4. A dobradiça de vidro tem modelo: GV48 1011, inox, 90°.
  5. ⛔ PEDRA NÃO ENTRA. Nenhuma bancada em granito, quartzito ou Nanoglass,
     nenhum sóculo de alvenaria, nenhum nicho revestido, nenhum box.
     ⭐ Mas espelho, vidro e serralheria que estão NA marcenaria são nossos.

⛔ Toda medida em CENTÍMETROS, como a prancha. Espessura em mm.
"""
CHAPA_C, CHAPA_L = 275.0, 185.0          # cm · confirmado em plano de corte
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875 m²
APROV    = 0.80
SANGRIA  = 2.0                           # cm de acerto de corte [Jonathan]
ALT_MAX  = CHAPA_C - SANGRIA             # ⭐ 273 — o teto de peça sem emenda

# ── preços, todos da Base de Custos ─────────────────────────────────────
# ⭐ A Base tem uma tabela de ESPESSURA PADRÃO POR APLICAÇÃO, e eu não a
#   estava seguindo:  estrutura e caixaria 15 · fundos 6 · porta 15 ·
#   prateleira 18 acima de 70 cm de vão.  ⛔ Eu vinha lançando caixaria e
#   porta em 18 mm, que é mais caro e não é o padrão da casa.
PRECO = {'MDF cor 18': 700.0, 'MDF cor 15': 550.0, 'MDF cor 6': 350.0,
         'MDF branco 18': 400.0, 'MDF branco 15': 350.0, 'MDF branco 6': 250.0,
         'MDF Branco TX 18': 400.0, 'MDF Branco TX 15': 350.0,
         'MDF Branco TX 6': 250.0,
         # ══ OS NOVE PADRÕES DO EXECUTIVO DA LUIZA PACHECO ══════════════
         # ⭐ Todos DURATEX, todos melamínico. ⛔ A chave é por COR: nove
         #   padrões são NOVE arredondamentos de chapa e nove compras, não
         #   uma. Cada um puxa no mínimo uma chapa inteira.
         # ⭐ Preço de COR confirmado pelo Jonathan em 28/10 no ICA
         #   ("branco diamante tem o mesmo preço de amadeirado"): 700/550/350
         #   vale para TODOS os padrões abaixo, inclusive os brancos de linha.
         'MDF Nogueira Caiena 18': 700.0, 'MDF Nogueira Caiena 15': 550.0,
         'MDF Nogueira Caiena 6': 350.0,
         'MDF Nogueira Thar 18': 700.0, 'MDF Nogueira Thar 15': 550.0,
         'MDF Nogueira Thar 6': 350.0,
         'MDF Off-White Suave 18': 700.0, 'MDF Off-White Suave 15': 550.0,
         'MDF Off-White Suave 6': 350.0,
         'MDF Branco Diamante 18': 700.0, 'MDF Branco Diamante 15': 550.0,
         'MDF Branco Diamante 6': 350.0,
         'MDF Azul Secreto 18': 700.0, 'MDF Azul Secreto 15': 550.0,
         'MDF Azul Secreto 6': 350.0,
         'MDF Pinole 18': 700.0, 'MDF Pinole 15': 550.0,
         'MDF Pinole 6': 350.0,
         # ⚠ Cinza Fóssil é LINHA VELLUTO: toque aveludado, não melamínico
         #   fosco comum, e costuma custar mais. Lançado como cor até o
         #   Jonathan dizer outra coisa. Fica na caixa de dúvidas.
         'MDF Cinza Fóssil 18': 700.0, 'MDF Cinza Fóssil 15': 550.0,
         'MDF Cinza Fóssil 6': 350.0,
         # ══ A COZINHA É LACA, E LACA NÃO É MELAMÍNICO ══════════════════
         # ⛔⛔ A prancha pede "MDF laqueado acetinado M048, Sayerlack" nos
         #   armários superior e inferior e no nicho. Laca é MDF **CRU** mais
         #   PINTURA EM CABINE — duas linhas, nunca uma. Lançar a cozinha em
         #   melamínico seria o erro da cômoda da Juliana outra vez: a
         #   proposta promete laca e o orçamento paga melamínico.
         # ⚠ O preço do CRU é derivado, não lido: a Base antiga traz a razão
         #   cru/fosco em 95/125 = 0,76, e aplico sobre os 700/550/350 de
         #   hoje. Está na caixa de dúvidas.
         'MDF Cru 18': 530.0, 'MDF Cru 15': 410.0, 'MDF Cru 6': 255.0}
ESTRUTURA, FUNDO_CH, PORTA_CH = 'MDF Branco TX 15', 'MDF Branco TX 6', 15
PRAT_VAO = 70.0   # vão acima disto pede 18 mm, contra empeno [Base]
# ⭐⭐ FITA E FILETAGEM SÃO DUAS COISAS [Jonathan, 28/10/2026]
#   > "nao vi o levamento de filetagem tbm"
#   Estavam, mas escondidas dentro de um preço só: os R$ 5,50 da "fita de
#   cor com filetagem" da Base são R$ 3,00 de fita MAIS R$ 2,50 de
#   filetagem. Juntas num número, nunca se vê que:
#     · a fita BRANCO TX custa R$ 2,00, não R$ 3,00 — e a caixaria toda é
#       branca, então metade dos metros estava precificada a mais
#     · a filetagem de RIPA e de chapa de 6 mm é MANUAL, R$ 5,00 — o dobro
#       da automática, porque não entra na coladeira
#   ⛔ Separar não é cosmética: muda o número nos DOIS sentidos.
FITA_COR, FITA_BRANCO   = 3.00, 2.00   # por metro de aresta
FILETE_AUTO, FILETE_MAO = 2.50, 5.00   # coladeira automática × à mão
FITA_CHEIA = 5.50   # ⚠ só para compatibilidade com o Living
FITA_PERD  = 0.10   # ⭐ 10% de desperdício é da FITA, que é material.
                    #   A filetagem é SERVIÇO, cobrado por metro de aresta
                    #   feita: não tem desperdício.
# ⭐⭐ A CASA INTEIRA É HETTICH [Jonathan, 29/10/2026]
#   O executivo da Luiza Pacheco vem MISTO: corrediça invisível em dez
#   ambientes e TELESCÓPICA em cinco (suíte master, closet master, armários
#   da suíte 01, closet das filhas, suíte hóspedes). Pela regra do elo mais
#   fraco uma telescópica derrubaria a garantia da casa inteira para 2 anos.
#   ⛔ Nenhuma telescópica comum entra: onde a prancha pede telescópica, SOBE
#     para Hettich oculta. A garantia é UNIFORME de 10 anos, e o termo de 10
#     anos é o único que existe desenhado.
# ⭐ O PREÇO SAI DA RAZÃO APURADA NO ICA, não de chute: 0,71 sobre a Blum.
#   ferragens.md fixou a faixa em 0,70–0,72 e mandou usar o TOPO, porque na
#   compra com CNPJ a Blum dá desconto maior e uma razão baixa demais
#   superestima a economia do cenário Hettich. Conferido contra o
#   cenarios.json do ICA: 1174,50 de diferença sobre 4050 de troca = 0,71.
RAZAO_HETT = 0.71
CORREDICA  = round(300.0 * RAZAO_HETT, 2)   # 213,00 · Hettich oculta, por gaveta
DOBRADICA  = round( 50.0 * RAZAO_HETT, 2)   #  35,50 · Hettich Sensys
# ⭐ DOBRADIÇA DE PORTA DE VIDRO — modelo cravado [Jonathan, 29/10/2026]
#   GV48 ref. 1011, 90°, aço inox, fixação alvenaria/vidro, kit de 2.
#   ⛔ Porta de vidro temperado NÃO aceita dobradiça de caneco: depois de
#     temperado o vidro não se fura. Quem segura a folha é a garra de inox.
#   ⚠ R$ 95,00 é ESTIMATIVA declarada — o site do fornecedor não resolve na
#     sessão e o varejo Pix de hoje vai de R$ 77 a R$ 140. A cotar.
#   ⭐ Duas por folha até 1,00 m de altura, TRÊS acima disso.
DOBR_VIDRO =  95.0  # ⚠ GV48 1011 · a cotar
BASCULA    = 250.0  # Blum AVENTOS HK-XS · ⭐ a báscula da casa
PULSADOR   = 100.0  # ⛔ FORA DA COZINHA [Jonathan, 28/10/2026]
SLIM       =  35.0  # ⭐ Puxador slim Rometal · é o que abre a báscula
#   > "nas básculas da cozinha iremos considerar o articular Hk-xs da blum
#   >  e puxador slim da rometal (R$ 35,00 und). ou seja, nao teremos o
#   >  pulsador blum."
#   ⭐ A própria Base já avisava: "PULSADOR E PUXADOR SLIM NÃO SE SOMAM na
#     mesma frente. São R$ 65 de diferença por porta." Em 17 básculas,
#     R$ 1.105.
CAVA_M     =  50.0  # cava usinada, por metro de frente
PUXADOR    = 172.71 # Alças Traso 416 mm · ⚠ o maior da linha, não é o do ICA
PUXADOR_128 = 110.0 # ⭐ Alças Traso 128 mm [Jonathan, 28/10/2026]
#   ⚠ A Base trazia R$ 56,69 para o 128 mm, de "média de três lojas", no
#     acabamento PRETO. A busca de varejo de hoje achou de R$ 44,92 a
#     R$ 109,22, e o topo da faixa é o níquel velho — que é onde o R$ 110
#     do Jonathan cai. ⭐ Não é divergência: é outro acabamento.
MOLDURA_MO = 0.0    # ⛔ moldura provençal, por frente — SEM PREÇO na Base
LED_M      = 150.0  # LED COB: fita, perfil, usinagem e instalação
ALMA       =  50.0  # barra chata 5 mm, 3 m · toda peça acima de 30 mm
# ⛔⛔ O SUPORTE OCULTO SAIU [Jonathan, 28/10/2026]
#   > "prateleiras internas dos armarios nao ultilizamos suporte oculto,
#   >  mas precisamos considerar que toda prateleira interna existe a
#   >  composição de 4 suportes em um custo total de 6.50"
#   ⭐ A regra agora é POR PRATELEIRA, não por par de pinos a cada 40 cm:
#     toda prateleira interna de armário custa R$ 6,50 de suporte além da
#     peça e da fita. E por ser "toda", ela não se declara — ela se CONTA
#     das peças, em `prateleiras()`. Declarar à mão é esquecer à mão.
SUPORTE    =   6.50  # jogo de 4 suportes, por PRATELEIRA interna
ALMA_VAO   = 120.0   # ⭐ prateleira de vão acima disto pede alma de aço
                     #   [Jonathan, 28/10] — contra flecha, não contra empeno
# ⭐ ESTRADO EM METALON [Jonathan, 28/10/2026]
#   > "Todas as camas teremos a aplicação de estrado em metalom, tanto
#   >  para a superior quanto para a inferior. o custo de cada quadro é
#   >  de 250,00"
#   ⛔ O estrado deixa de ser painel de MDF: é quadro de metalon, e é
#     serralheria. Um quadro por leito — beliche tem dois, bicama tem dois.
METALON    = 250.0   # por quadro de estrado
# ⭐ CORREDIÇA TOUCH [Jonathan, 28/10/2026]
#   > "no caso de corrediças com abertura por toque, considere a corrediça
#   >  touch, não precisa de pulsador. a corrediça com toque considere o
#   >  custo de 500,00"
#   ⛔ Ela SUBSTITUI o par de corrediça comum E o pulsador — os dois.
CORREDICA_TOUCH = 500.0
# ⭐ PERFIL DE PROTEÇÃO DE PISO [Jonathan, 28/10/2026]
#   > "Todos os paineis que estao em contado direto no piso terá aplicação
#   >  de aluminio/perfil inox de proteção, calcule a extensao linear, o
#   >  custo por mt linear é de 15,00"
PERFIL_PISO = 15.0   # por metro linear de painel que toca o chão
# ⭐ os dois serviços de corte, por ambiente [Jonathan, 28/10/2026]
CORTE_CHAPA, CORTE_PECA = 2.00, 2.50
# ⭐ MALHA DE CORDAS NÁUTICAS [Jonathan, 28/10/2026, Suíte 03 item 3]
#   > "na base da cama superior, inferior e bicama considere a estrutura de
#   >  serralheria, considere a malha de cordas naulticas a 250,00 mt²"
#   ⛔ É o que substitui o estrado nas três bases da Suíte 03: quadro de
#     serralheria com a malha tecida dentro. Por m² de vão, como a palhinha
#     e o estofado — não por chapa.
MALHA_CORDAS = 250.0  # por m² de vão
SUPORTE_OCULTO = 30.0  # ⛔ legado: não se usa mais em prateleira de armário
CABIDEIRO  = 120.0  # cabideiro em metal preto ou grafite · Base, por unidade
# ⭐ reforço estrutural interno. A prancha da Lavanderia manda "prever
#   reforço para suportar lava e seca cheia": o apoio sobe para 18 mm e
#   recebe sarrafo. Sarrafo é material de estrutura, não aparece e não leva
#   fita — por isso entra por metro, como o LED, e não como peça de chapa.
# ⛔⛔ PINUS ESTÁ PROIBIDO [Jonathan, 28/10/2026]
#   > "Não usamos peças de pinus para nada."
#   O sarrafo some do vocabulário da casa. Onde ele segurava alguma coisa,
#   entra uma de três: ENGRADADO DE MDF (travessa tirada da própria chapa,
#   `engradado()`), ESTRADO EM METALON (cama) ou SERRALHERIA ESTRUTURAL
#   (quando o que segura é estrutura de verdade). A constante fica aqui
#   zerada e a chave sai da Base, para que nenhum ambiente a use calado.
SARRAFO    =   0.0  # ⛔ PROIBIDO — ver auditor, regra 9
PERDA_RIPA =   1.10 # ⭐ Base, Terceirizados: perda de serra ao tirar ripa
# ⭐ ferragem de uma vez só, declarada por OUTRAS no ambiente. O preço
#   mora aqui e no 'precos' da planilha; vazio na Base continua vazio aqui.
# ⭐ ferragem e terceirizado de uma vez só, declarados por OUTRAS no ambiente.
#   ⛔ A regra de ouro da Base vale aqui: linha com R$ 0,00 é BURACO CONHECIDO,
#     não item esquecido. O item existe, a unidade está definida, e o preço
#     falta — o orçamento mostra zero e denuncia.
PRECO_OUTRAS = {
 # ══ O QUE O EXECUTIVO DO GUSTAVO RAPOSO TROUXE DE NOVO ═════════════════
 # ⭐⭐ LACA SAYERLACK M048 ACETINADA — a cozinha inteira.
 #   Laca é MDF cru MAIS pintura em cabine, e a pintura é por m² de peça.
 #   R$ 650/m² é o número da casa (validacao-orcamento.md, o caso da cômoda
 #   da Juliana). ⚠ É o preço da peça LISA; a prancha pede moldura de 5 cm
 #   em toda frente, e frente com relevo pinta mais devagar. Fica na caixa
 #   de dúvidas: perguntar o acréscimo da frente usinada.
 'Laca Sayerlack M048 acetinada': 650.0,   # por m² de peça pintada
 # ⭐⭐ ESPELHO — e ele tem DOIS preços, porque são duas construções
 #   diferentes [ferragens.md, Jonathan 29/08/2026]:
 #     · folha que ABRE ou CORRE → porta pronta terceirizada, perfil de
 #       alumínio + espelho prata com película de segurança. R$ 700/m² posto
 #       na obra, e ⛔ NÃO entra no plano de corte: não há chapa, não há fita
 #       e não há cava, porque o puxador é do perfil.
 #     · espelho FIXO colado no MDF → R$ 600/m² mais a chapa por baixo.
 'Porta de espelho em alumínio': 700.0,    # por m² de folha · correr ou giro
 'Espelho prata colado': 600.0,            # por m² · fixo, sobre a chapa
 # ⭐ Os quatro espelhos de banheiro são NOSSOS, COM VALOR [Jonathan, 29/10]:
 #   a moldura é usinada por nós e o espelho vem da vidraçaria.
 #   ⚠ A prancha diz "moldura em dourado". Dourado não é padrão melamínico:
 #     ou é laca sobre MDF cru, ou é perfil metálico. Lancei como laca e
 #     deixei a pergunta na caixa de dúvidas.
 # ⚠ SISTEMA DE CORRER SS-150 — a prancha nomeia o modelo em três armários
 #   (suíte 01, duas elevações, e suíte hóspedes): "portas de correr
 #   flutuantes com sistema sem amortecedor SS-150". ⛔ Não é o Dominus da
 #   Base e não tem linha própria. Lançado pelo Dominus de 2 portas como
 #   INTERINO DECLARADO, porque zerar o sistema de um armário de 4 m não
 #   grita: mente para baixo.
 'Sistema de correr SS-150': 1840.0,  # ⚠ interino: preço do Dominus 2p
 'Puxador NEO32 Bronze': 0.0,         # ⛔ por unidade · SEM PREÇO · a cotar
 # ⭐ PALHINHA NATURAL — a Suíte 02 · Filhas pede "frente com moldura em MDF
 #   e palhinha" no armário, na mesa e na mesa de cabeceira.
 #   ⛔ NÃO é a chapa melamínica que imita o desenho: é tapeceiro, por m² de
 #     vão, a R$ 650 [Jonathan, 28/10/2026].
 'Palhinha natural': 650.0,      # por m² de vão
 # ⭐ SERRALHERIA DENTRO DA MARCENARIA — é nossa pela fronteira do escopo:
 #   sai no mesmo caminhão e é instalada pela mesma equipe. As estruturas
 #   cilíndricas douradas que sustentam a mesa (Ø5 cm) e a mesa de cabeceira
 #   (Ø2,5 cm) da Suíte 02. ⛔ Valor FECHADO por peça, nunca por chave de
 #   preço unitário [regra 12 do quantitativo].
 'Serralheria estrutural': 0.0,  # ⛔ valor fechado, vem do ambiente
 'Rodízio de gaveteiro': 0.0,    # ⛔ por unidade · SEM PREÇO · suíte 01
 # ══ O COMUM DA CASA, que vale em todo projeto ══════════════════════════
 'Pulsador': 100.0,              # ⭐ o "fecho-toque" da Suíte 02 é isto
 'Estofamento em linho': 600.0,  # por m²
 'Estrado em metalon': METALON,  # por quadro de leito
 'Corrediça touch': CORREDICA_TOUCH,
 'Perfil de proteção de piso': PERFIL_PISO,
 'Suporte de prateleira': SUPORTE,
 'Corte por chapa': CORTE_CHAPA,
 'Corte por peça': CORTE_PECA,
 'Cabideiro': CABIDEIRO,
 'Carreto': 0.0,
 'Vidro temperado incolor': 0.0,  # ⛔ por m² · cristaleira · a cotar
 'Puxador passante': 100.0,
 'Malha de cordas náuticas': MALHA_CORDAS,
 'MDF Branco Diamante 25': 600.0,
}
VIDRO_M2   =   0.0  # ⛔ reflecta champagne SEM PREÇO — a cotar
# ⭐ SERRALHERIA ESTRUTURAL [Jonathan, 28/10/2026]
#   > "No banco suspenso do living considere uma estrutura de serralheria
#   >  estrutural com um custo de 2.500"
#   ⛔ Não confundir com o rodapé de 3 cm, que a casa faz em MDF melamínico
#     por decisão do Jonathan de 26/10. Aqui é estrutura de verdade: o banco
#     é SUSPENSO e o que o segura não é a marcenaria.
#   ⭐ Entra como VALOR FECHADO por móvel, não por metro: foi assim que o
#     Jonathan deu, e banco suspenso é projeto, não metro linear.
PRECO.update(PRECO_OUTRAS)   # ⭐ o custo() do auditor busca tudo em PRECO
CONSUM, EMBAL = 0.06, 0.02
# ⛔⛔ SEM FONTE DE LED em lugar nenhum: as fitas da casa são 110 V
#   [Jonathan, 28/10/2026]

ALTAS = []   # ⭐ toda peça que o projeto desenhou acima do que a chapa dá

def P(nome, movel, c, l, qtd=1, chave='MDF cor 18', fita=(0, 0), obs=''):
    """Uma peça. `fita` = (nº de arestas no COMPRIMENTO, nº na LARGURA).

    ⭐ A CHAVE É POR COR, não só por espessura. Um ambiente com três padrões
      de MDF faz TRÊS arredondamentos de chapa, não um — cada cor é uma
      compra separada e puxa no mínimo uma chapa. Foi o erro que queimou a
      primeira versão desta planilha.

    ⛔ Peça acima de 273 é ANOTADA e rebaixada: é decisão de projeto, não de
      corte, e tem de aparecer na lista.
    """
    def cabe(a, b): return a <= CHAPA_C and b <= CHAPA_L
    if not (cabe(c, l) or cabe(l, c)):
        maior, menor = max(c, l), min(c, l)
        if menor <= CHAPA_L and maior > ALT_MAX:
            ALTAS.append((movel, nome, maior, qtd))
            c, l = (ALT_MAX, l) if c >= l else (c, ALT_MAX)
        else:
            raise AssertionError(f'⛔ {nome} ({c}×{l}) NÃO CABE NA CHAPA')
    return dict(nome=nome, movel=movel, c=c, l=l, qtd=qtd, chave=chave,
                fita=fita, obs=obs)

def gaveta(movel, larg, prof, alt, n=1, rotulo='Caixa de gaveta',
           cor=ESTRUTURA, fundo=FUNDO_CH):
    """A caixa atrás da frente. ⭐ É o que mais se esquece de contar."""
    liq = larg - 3.6
    return [P(f'{rotulo} · lateral', movel, prof, alt, 2*n, cor, (1, 0)),
            P(f'{rotulo} · frente e costas', movel, liq, alt, 2*n, cor, (1, 0)),
            P(f'{rotulo} · fundo', movel, liq, prof, n, fundo, (0, 0),
              'Fundo em 6 mm por encaixe em rasgo — ⛔ sem fita')]

def prateleiras(pecas, movel=None):
    """⭐⭐ Nº de PRATELEIRAS INTERNAS de armário — a conta do suporte.

    [Jonathan, 28/10/2026] "toda prateleira interna de armários tem um
    custo além da peça e da fita de borda de 6.50 de suporte".

    ⛔ Por ser "toda", ela NÃO se declara: se declarar, esquece. Ela se
      conta das peças, como a lista de chapas se conta. Quem não leva
      suporte — prateleira que encaixa em rasgo, prateleira pendurada em
      haste, prateleira fixa cavilhada — diz `sem suporte` na obs, e aí a
      exceção fica escrita na linha do orçamento, não na minha cabeça.
    """
    n = 0
    for p in pecas:
        if movel and p['movel'] != movel: continue
        nome = p['nome'].lower()
        if 'moldura' in nome or 'sem suporte' in p['obs'].lower(): continue
        if any(w in nome for w in ('prateleira', 'sapateira', 'maleiro')):
            n += p['qtd']
    return n

def almas_de_prateleira(pecas, movel=None):
    """⭐ Nº de prateleiras que pedem ALMA DE AÇO, pelo vão.

    [Jonathan, 28/10/2026] "prateleiras acima de 1.20mt vamos considerar
    alma de aço". ⛔ É contra FLECHA, não contra empeno: 18 mm resolve o
    empeno e não resolve o vão. Uma barra por prateleira — a barra tem
    3 m e nenhuma prateleira do projeto passa disso.

    Como o suporte, ela se CONTA das peças. Quem não leva diz `sem alma`
    na obs, e a exceção fica escrita na linha.
    """
    n = 0
    for p in pecas:
        if movel and p['movel'] != movel: continue
        nome = p['nome'].lower()
        if 'prateleira' not in nome or 'moldura' in nome: continue
        if 'sem alma' in p['obs'].lower(): continue
        if max(p['c'], p['l']) > ALMA_VAO: n += p['qtd']
    return n

def engradado(movel, metros, chave, rot='', larg=5.0):
    """⭐ O que substitui o sarrafo de pinus, que está PROIBIDO.

    [Jonathan, 28/10/2026] "Não usamos peças de pinus para nada." Onde
    havia engradado interno, entra TRAVESSA DE MDF tirada da própria
    chapa — mesma cor, mesma compra, sem fornecedor novo. ⛔ A travessa
    não aparece e não leva fita.
    """
    import math
    n = max(1, math.ceil(metros*100/ALT_MAX))
    return [P('Engradado · travessa de MDF', movel, ALT_MAX, larg, n, chave,
              (0, 0), (rot + ' · ' if rot else '') +
              f'{metros:g} m de travessa de {larg:g} cm, tirada da chapa · '
              '⛔ sem fita: é estrutura interna e não aparece · ⛔ substitui '
              'o sarrafo de pinus, que a casa não usa')]

def ripado(movel, larg_total, alt, larg_ripa, vao, chave, obs=''):
    """Ripa solta com vão. ⭐ Conta a ripa, não o painel."""
    n = int(larg_total // (larg_ripa + vao)) + 1
    # ⭐⭐ LAMINAÇÃO NOS DOIS LADOS [Jonathan, 28/10/2026]
    #   > "nas ripas de 3cm, considere a laminação em ambos os lados"
    #   ⛔ Eu tinha (2, 1): filetava as duas pontas de 3 cm e UM lado longo.
    #     Numa ripa solta, com vão, os dois lados longos ficam à vista — são
    #     QUATRO arestas, e as longas são as que valem metro. Numa ripa de
    #     3 × 103 isso é 1,09 m contra 2,12 m: a conta dobra.
    #   ⛔ E ripa não entra na coladeira: a filetagem é MANUAL, R$ 5,00.
    #   ⭐⭐ E A SERRA COME CHAPA. A Base traz "Perda de serra ao tirar ripa ·
    #     fator 1,10" e o motor nunca a aplicou: tirar 3 cm de ripa de uma
    #     chapa não é cortar um painel, é uma passada de serra a cada 3 cm.
    #     Entra como LINHA PRÓPRIA, não embutida na ripa, para que o plano
    #     de corte continue dizendo a verdade sobre quantas ripas existem.
    area = n * larg_ripa
    return [P(f'Ripa de {larg_ripa:g}', movel, larg_ripa, alt, n, chave, (2, 2),
              obs or f'Vão de {vao:g} entre as ripas · {n} ripas em '
                     f'{larg_total:g} · laminada nos dois lados'),
            P(f'Ripa de {larg_ripa:g} · perda de serra', movel,
              round(area * (PERDA_RIPA - 1), 1), alt, 1, chave, (0, 0),
              f'⭐ fator 1,10 da Base · a serra come chapa a cada '
              f'{larg_ripa:g} cm de ripa · ⛔ é perda, não peça: sem fita')]

# ⛔ MOLDURA_L SAIU. Era a largura da travessa, e era premissa minha: a
#   prancha não a cotava e eu adotei 7 cm. Não existe mais travessa.

def provencal(nome, movel, c, l, qtd, cor15, cor6, obs=''):
    """⭐⭐ FRENTE PROVENÇAL — DUAS PEÇAS INTEIRAS  [Jonathan, 28/10/2026]
       > "para as demais frentes provençais nao considere reguas, considere
       >  outra peça de igual tamanho pois é retirada uma peça inteira e
       >  feito a usinagem na router"

       base ........ 15 mm na cor, medida cheia da frente
       moldura ..... OUTRA peça inteira de 6 mm, MESMA medida, usinada na
                     router — não são quatro réguas montadas

    ⛔⛔ EU ORÇAVA RÉGUA, E RÉGUA NÃO É O QUE SAI DA FÁBRICA. Montava a
      moldura com quatro travessas de 7 cm coladas em volta. A fábrica tira
      uma peça inteira e usina o relevo na router: o que vai para o plano de
      corte é um RETÂNGULO CHEIO de 6 mm, não quatro tiras. Três coisas
      mudam de uma vez:

      1. A CHAPA DE 6 MM SOBE. Quatro réguas de 7 cm numa frente de 60 × 85
         davam 0,20 m²; a peça inteira dá 0,51 m². É duas vezes e meia mais
         de chapa de 6 — e chapa se arredonda inteira.
      2. A FILETAGEM MANUAL SOME. A régua de 6 mm não entrava na coladeira e
         ia à mão, a R$ 5,00. Agora o 6 é COLADO sobre o 15 e o conjunto vai
         à coladeira como uma peça só, de 21 mm, no automático. Por isso a
         peça de 6 entra com fita (0, 0): quem leva o perímetro é a base,
         uma vez só, pelos dois.
      3. A PREMISSA DA TRAVESSA MORRE. Não há largura de régua para adivinhar
         — e com ela morre o limite de tamanho: uma frente de 10 cm, que não
         comportava duas travessas de 7, agora é provençal como qualquer
         outra.

    ⛔ A MÃO DE OBRA continua sem preço na Base, mas agora tem nome certo:
      é USINAGEM NA ROUTER por frente, não montagem de travessa.
    """
    return [P(nome, movel, c, l, qtd, cor15, (2, 2), obs),
            P(f'{nome} · moldura usinada', movel, c, l, qtd, cor6, (0, 0),
              'Peça inteira de 6 mm, mesma medida da base, relevo usinado na '
              'router · colada sobre a base: o perímetro vai na fita da base, '
              '⛔ sem fita própria para não contar o mesmo metro duas vezes')]

def _fita_chave(chave):
    return 'Fita Branco TX' if 'ranco' in chave else 'Fita cor'

def _filete_chave(chave, nome):
    """⛔ Ripa e chapa de 6 mm não entram na coladeira: filetagem à mão.

    ⛔ A REGRA É A ESPESSURA, NÃO A PALAVRA. Eu tinha posto 'ravessa' aqui,
      pensando nas travessas de 6 mm da moldura provençal — e a regra pegou
      a "travessa sobre as portas" do Living, que é painel de 180 × 63 em
      18 mm e entra na coladeira sem dificuldade. Cobrava R$ 5,00 onde são
      R$ 2,50. ⭐ As travessas da moldura já caem aqui pela espessura, que
      é o critério de verdade: quem não entra na máquina é o 6 mm e a ripa.
    """
    return ('Filetagem manual' if chave.endswith(' 6') or 'Ripa' in nome
            else 'Filetagem automática')

def acabamento(pecas, movel=None):
    """⭐ Metros por CHAVE de acabamento, que é o levantamento que faltava.
      A fita leva os 10% de desperdício porque é material; a filetagem não,
      porque é serviço por metro de aresta feita.

    ⛔⛔ O TOTAL DO AMBIENTE É A SOMA DOS MÓVEIS JÁ ARREDONDADOS, não o
      arredondamento da soma. Parece preciosismo e não é: a aba soma com
      SOMASE os valores por móvel, que saem arredondados em 0,1 m, e eu
      arredondava o total do ambiente. Deu R$ 0,54 de diferença entre o
      script e a planilha — pequena, mas é exatamente o tipo de divergência
      que a linha de CONFERÊNCIA existe para não deixar passar. ⭐ E a aba
      está certa: é por móvel que a fábrica executa.
    """
    if movel is None:
        tot = {}
        for mv in dict.fromkeys(p['movel'] for p in pecas):
            for k, v in acabamento(pecas, mv).items():
                tot[k] = round(tot.get(k, 0.0) + v, 1)
        return tot
    out = {}
    for p in pecas:
        if p['movel'] != movel: continue
        nc, nl = p['fita']
        m = (nc*p['c'] + nl*p['l'])*p['qtd']/100
        if m <= 0: continue
        fk = _fita_chave(p['chave'])
        lk = _filete_chave(p['chave'], p['nome'])
        out[fk] = out.get(fk, 0.0) + m*(1 + FITA_PERD)
        out[lk] = out.get(lk, 0.0) + m
    return {k: round(v, 1) for k, v in out.items() if round(v, 1) > 0}

PRECO_ACAB = {'Fita cor': FITA_COR, 'Fita Branco TX': FITA_BRANCO,
              'Filetagem automática': FILETE_AUTO, 'Filetagem manual': FILETE_MAO}

def fita_m(pecas, movel=None):
    """⚠ Só o metro cru, sem desperdício. O Living ainda usa."""
    return sum((nc*p['c'] + nl*p['l'])*p['qtd']/100 for p in pecas
               if movel is None or p['movel'] == movel
               for nc, nl in [p['fita']])
