# -*- coding: utf-8 -*-
"""CHARBEL CHELALA · apartamento BH — O QUANTITATIVO, peça por peça.

⭐ Sai das pranchas 15 a 25 do executivo de Mariana Borges (OUT/2026, rev. 3).
  Cada item deste arquivo aponta para a folha e a vista de onde veio, e as
  medidas são as COTAS DO DESENHO — não há peça aqui sem cota, e onde a
  cota não existe está escrito que não existe.

⛔⛔ O QUE NÃO É NOSSO NÃO ENTRA. Quartzito Verde Guatemala, ônix
  retroiluminado, granito Grigio Carnico, cuba esculpida, rodaparede,
  prateleiras de mármore, forno, frigobar, adega Elettromec, alvenaria,
  gesso e papel de parede estão desenhados nas mesmas folhas e ficaram de
  fora. ⭐ Espelho, vidro e perfil metálico QUE ESTÃO DENTRO DA MARCENARIA
  são nossos — essa é a regra da casa, e aqui ela vale muito dinheiro: o
  closet inteiro é porta de perfil com vidro.

⚠⚠ AS PREMISSAS QUE AINDA NÃO SÃO COTAÇÃO estão todas em `base.py`, uma
  por linha, marcadas com ⚠. Mexer numa delas recalcula tudo.
"""
import math, importlib.util, sys, pathlib, contextlib, io

AQUI = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location('b', AQUI / 'base.py')
b = importlib.util.module_from_spec(_s); sys.modules['b'] = b
with contextlib.redirect_stdout(io.StringIO()):
    _s.loader.exec_module(b)

CARIBE = 'MDF Caribe'            # Linha Dual Syncro · Guararapes
CIPRES = 'MDF Cipres'            # Guararapes
FONTANA = 'MDF Fontana'          # Linha Magma · Guararapes
CACAO = 'MDF Cacao'              # Matt · Arauco
CINZA = 'MDF Cinza Sagrado'      # Duratex
#   ⛔⛔ O BRANCO TX SAIU DAQUI EM 09/11/2026. [Jonathan: "não tem nada de
#     branco tx no projeto"] — e ele está certo: a prancha 21 nomeia só
#     MDF Cipres Guararapes e MDF Cacao Matt Arauco, e nenhuma das onze
#     folhas escreve Branco TX em lugar nenhum. O branco no interior era
#     PADRÃO DA CASA que eu apliquei por hábito, não leitura da prancha.
#   ⭐ A REGRA NOVA É MAIS SIMPLES E MAIS CARA: o interior sai no padrão do
#     próprio ambiente. Caixa, gaveta e fundo acompanham a face.
#   ⚠ ISSO MEXE NO CUSTO: eram 23 chapas de Branco TX a R$ 350 e R$ 250.
#     Agora elas entram no padrão, que custa R$ 550 e R$ 350 — e, em troca,
#     deixam de arredondar uma chapa própria, porque se somam à área que o
#     ambiente já comprava.
INTERNO = {'01 Cozinha': CARIBE, '02 Hall e Jantar': CARIBE,
           '03 Estar e TV': CARIBE, '04 Acessos e Corredor': CARIBE,
           '05 Suíte': CIPRES, '06 Closet': CIPRES, '07 Banho da Suíte': CINZA,
           '08 Banheiro Social': CINZA, '09 Quarto': CIPRES}

RIPA_L, RIPA_VAO = 4.0, 2.0
PASSO = RIPA_L + RIPA_VAO


class Item:
    def __init__(self, nome, folha, obs='', ambiente=''):
        self.nome, self.folha, self.obs = nome, folha, obs
        self.ambiente = ambiente
        self.interno = INTERNO.get(ambiente, CIPRES)
        self.pecas, self.terc, self.fer = [], [], []

    def p(self, nome, L, A, esp, mat, qtd=1, fita=0.0, obs=''):
        self.pecas.append(dict(nome=nome, L=L, A=A, esp=esp, mat=mat,
                               qtd=qtd, fita=fita, obs=obs))
        return self

    def t(self, nome, q, unit, un='m²'):
        if q: self.terc.append((nome, q, unit, un))
        return self

    def f(self, nome, q, unit):
        if q: self.fer.append((nome, q, unit))
        return self

    # ── os quatro gestos que se repetem em trinta e oito itens ──────────
    def caixa(self, L, A, P, mat, div=0, prat=0, fundo=6, esp=15, nome='caixa'):
        """⭐ Lateral, divisória, tampo, base, fundo e prateleira.
        ⛔ Peça com mais de 273 cm não existe: a chapa é 275 e a sangria é
          2. Tampo e base de armário longo saem emendados, e é por isso que
          a conta é de ÁREA e não de peça inteira."""
        n_lat = 2 + div
        self.p(f'{nome} · laterais e divisórias', P, A, esp, mat, n_lat, A / 100)
        self.p(f'{nome} · tampo e base', L, P, esp, mat, 2, L / 100)
        if fundo:
            self.p(f'{nome} · fundo', L, A, fundo, mat, 1)
        if prat:
            larg = (L - n_lat * 1.5) / (div + 1)
            self.p(f'{nome} · prateleiras', larg, P - 2, esp, mat, prat, larg / 100)
            self.f('Suporte de prateleira Blum, jogo de 4', prat, b.SUPORTE_JOGO)
        return self

    def porta(self, larg, alt, n, mat, esp=18, cava=False, botao=False,
              nome='porta de abrir'):
        self.p(f'{n} × {nome} {larg:.0f} × {alt:.0f}', larg, alt, esp, mat, n,
               (larg + alt) * 2 / 100)
        self.f('Dobradiça Blum', n * b.dobradicas(alt), b.DOBRADICA)
        if cava:
            self.t('Puxador cava usinado', n * larg / 100, b.CAVA_M, 'm')
        if botao:
            self.f('Puxador cilíndrico / botão h = 110', n, b.PUXADOR_BOTAO)
        return self

    def gaveta(self, larg, alt, prof, n, mat, esp=18, cava=False, botao=False):
        self.p(f'{n} × frente de gaveta {larg:.0f} × {alt:.0f}', larg, alt, esp,
               mat, n, (larg + alt) * 2 / 100)
        #   ⭐ a caixa da gaveta some do olho, mas sai no padrão do ambiente:
        #     neste projeto não há interior branco em lugar nenhum
        self.p(f'{n} × caixa de gaveta', (larg + prof) * 2, 13, 15,
               self.interno, n, (larg + prof) * 2 / 100)
        self.p(f'{n} × fundo de gaveta', larg, prof, 6, self.interno, n)
        self.f('Corrediça Blum Movento, par', n, b.CORREDICA_PAR)
        if cava:
            self.t('Puxador cava usinado', n * larg / 100, b.CAVA_M, 'm')
        if botao:
            self.f('Puxador cilíndrico / botão h = 110', n, b.PUXADOR_BOTAO)
        return self

    def ripado(self, larg, alt, esp_cm, mat, nome='ripado'):
        """⭐ Ripa não é peça: é ÁREA EQUIVALENTE de chapa, mais a mão de
        obra de colagem e a filetagem das duas faces de cada ripa."""
        n = max(1, int(larg // PASSO))
        esp_chapa, camadas = (15, 2) if esp_cm >= 2.5 else (18, 1)
        self.p(f'{nome} · {n} ripas de {RIPA_L:g} × {alt:.0f}',
               RIPA_L * n * b.RIPA_PERDA, alt, esp_chapa, mat, camadas,
               obs=f'área equivalente · {camadas} camada(s) de {esp_chapa} mm')
        self.t('Painel ripado, mão de obra', larg * alt / 10000, b.RIPADO_M2)
        self.t('Filetagem de ripa', n * alt / 100 * 2, b.FILETE_RIPA, 'm')
        return self

    def led(self, metros, fontes=1, bottons=0):
        self.t('Fita LED, perfil de embutir e difusor', metros, b.LED_M, 'm')
        self.f('Fonte de LED', fontes, b.LED_FONTE)
        self.f('Botton de acionamento na marcenaria', bottons, b.BOTTON)
        return self


M = []
AMB = ['']          # ⭐ o ambiente corrente · uma aba da planilha por ambiente
def ambiente(nome):
    AMB[0] = nome

def novo(nome, folha, obs=''):
    it = Item(nome, folha, obs, AMB[0]); M.append(it); return it


#   ⭐ Cada ambiente leva o seu frete, que na planilha da casa é a única
#     célula digitada da aba. Viagem é de ida: ambiente grande leva duas.
VIAGENS = {'01 Cozinha': 2, '02 Hall e Jantar': 1, '03 Estar e TV': 2,
           '04 Acessos e Corredor': 1, '05 Suíte': 2, '06 Closet': 2,
           '07 Banho da Suíte': 1, '08 Banheiro Social': 1, '09 Quarto': 2}


# ════════════════════════════════════════════════════════════════════════
# COZINHA · folhas 15 e 16
# ════════════════════════════════════════════════════════════════════════

ambiente('01 Cozinha')
# ─── 01 ─────────────────────────────────────────────────────────────────
it = novo('Cozinha · armário superior da vista 01', 15,
          '383,00 × 87,00 · 7 folhas de abrir · puxador cava no próprio material')
it.caixa(383, 87, 35, it.interno, div=5, prat=6)
it.porta(383 / 7, 87, 7, CARIBE, cava=True)
it.p('nicho aberto · fundo e laterais', 45, 30.24, 15, CARIBE, 3, .45)

# ─── 02 ─────────────────────────────────────────────────────────────────
it = novo('Cozinha · varal retrátil estilo gaveta', 15,
          '75,00 × 12,00 · corre como gaveta, logo leva par de corrediça')
it.p('frente do varal', 75, 12, 18, CARIBE, 1, (75 + 12) * 2 / 100)
it.p('estrutura do varal', 75, 55, 15, it.interno, 2, .75)
it.f('Corrediça Blum Movento, par', 1, b.CORREDICA_PAR)

# ─── 03 ─────────────────────────────────────────────────────────────────
it = novo('Cozinha · armário inferior da vista 01', 15,
          '383,00 × 76/90 × 65 · 2 portas de 40, 4 gavetas e o painel do forno')
it.caixa(383, 85, 60, it.interno, div=4, prat=3)
it.porta(40, 90, 2, CARIBE, cava=True)
it.gaveta(83.76, 38, 55, 2, CARIBE, cava=True)
it.gaveta(40, 38, 55, 1, CARIBE, cava=True)
it.gaveta(22, 76, 55, 1, CARIBE, cava=True)
it.p('painel fixo para encaixe do forno', 72, 76, 18, CARIBE, 1,
     (72 + 76) * 2 / 100)
it.t('Rodapé inox h = 2', 3.83, b.RODAPE_INOX_M, 'm')

# ─── 04 ─────────────────────────────────────────────────────────────────
it = novo('Cozinha · armário superior da vista 02', 16,
          '219,00 × 98,00 · 7 folhas: 31,5 · 31,5 · 27,5 · 27,5 · 23 · 35 · 35')
it.caixa(219, 98, 35, it.interno, div=3, prat=4)
it.porta(31.5, 98, 2, CARIBE, cava=True)
it.porta(27.5, 65, 2, CARIBE, cava=True)
it.porta(23, 98, 1, CARIBE, cava=True)
it.porta(35, 65, 2, CARIBE, cava=True)
it.p('módulos de 33 sob os superiores', 57, 33, 18, CARIBE, 2, (57 + 33) * 2 / 100)

# ─── 05 ─────────────────────────────────────────────────────────────────
it = novo('Cozinha · torre central com o QDC embutido', 16,
          '72 × 247 × 60 · a porta de 170, o módulo de 88 + 53 e a tampa do quadro')
it.caixa(72, 247, 60, it.interno, div=2, prat=4)
it.porta(45, 170, 1, CARIBE, cava=True)
it.porta(72, 88, 1, CARIBE, cava=True)
it.porta(72, 53, 1, CARIBE, cava=True)
it.p('tampa de inspeção do QDC', 31, 31, 18, CARIBE, 1, (31 + 31) * 2 / 100)
it.p('módulo de 30,5 sob o QDC', 72, 30.5, 18, CARIBE, 1, (72 + 30.5) * 2 / 100)

# ─── 06 ─────────────────────────────────────────────────────────────────
#   ⛔ O MÓDULO DE 121 × 82 DA VISTA 02 NÃO ENTRA. A própria folha escreve
#     "Painel fixo em ALVENARIA" em cima dele, e alvenaria é obra. ⚠ Mas
#     ele está DESENHADO EM MADEIRA, e a dúvida vale ~1 m² de Caribe mais
#     a frente. Está em `_LEITURA.md` como pergunta para a arquiteta.
it = novo('Cozinha · armário baixo de apoio da vista 02', 16,
          '60 × 72 × 35 · o único volume da vista 02 que a folha chama de MDF Caribe')
it.caixa(60, 72, 35, it.interno, div=0, prat=2)
it.porta(60, 72, 1, CARIBE, cava=True)

ambiente('02 Hall e Jantar')
# ─── 07 ─────────────────────────────────────────────────────────────────
it = novo('Hall · divisória da vista 04', 16,
          '109,00 × 237,00 × 7,00 · moldura curva r = 10 e 2 gavetas de 51,5 na base')
it.p('faces da divisória', 109, 237, 18, CARIBE, 2, (109 + 237) * 2 / 100)
it.p('miolo e travamento da divisória', 7, 237, 18, CARIBE, 4, 2.37)
it.gaveta(51.5, 39, 20, 2, CARIBE, cava=True)
it.t('Usinagem de moldura curva r = 10', (109 + 237) * 2 / 100, b.FILETE_MAO, 'm')
#   ⛔ o painel de ônix retroiluminado de 103 × 175 é da marmoraria

# ─── 08 ─────────────────────────────────────────────────────────────────
it = novo('Jantar · cristaleira da vista 03', 16,
          '109,00 × 247,00 × 36 · vitrine de 139 com porta de perfil e vidro, '
          'aparador de 107 × 36 e base de 2 portas')
it.caixa(109, 247, 36, CARIBE, div=1, prat=8, nome='vitrine e base')
it.t('Porta de cristaleira em perfil com vidro', 2, b.PORTA_CRISTALEIRA,
     'folha')
it.f('Dobradiça Blum para porta de vidro', 2 * b.dobradicas(139),
     b.DOBRADICA_VIDRO)
it.p('tampo do aparador', 107, 36, 18, CARIBE, 1, (107 + 36) * 2 / 100)
it.porta(50, 67, 2, CARIBE, cava=True)
it.ripado(109, 36, 2.0, CARIBE, 'acabamento curvo ripado do aparador')
it.led(4 * 1.07, fontes=1, bottons=1)

# ─── 09 ─────────────────────────────────────────────────────────────────
it = novo('Hall · forro em madeira', 16,
          '108,00 × 109,00 · desenvolvimento de 141,37 pelo detalhe')
it.p('réguas do forro do hall', 141.37, 109, 18, CARIBE, 1, (141.37 + 109) * 2 / 100)
it.t('Sarrafo de pinus para fixação do forro', 4 * 1.4137, b.SARRAFO_PINUS_M, 'm')


# ════════════════════════════════════════════════════════════════════════
# ESTAR & TV · folha 17
# ════════════════════════════════════════════════════════════════════════

ambiente('03 Estar e TV')
# ─── 10 ─────────────────────────────────────────────────────────────────
it = novo('Estar · painel fixo da vista 05', 17,
          '255,00 de altura · 124 à esquerda, 30 à direita e as faixas de 29 e 68 '
          'em volta da pedra de 193 × 147')
it.p('painel lateral esquerdo', 124, 255, 18, CARIBE, 1, (124 + 255) * 2 / 100)
it.p('faixa lateral direita', 30, 255, 18, CARIBE, 1, (30 + 255) * 2 / 100)
it.p('faixa acima da pedra', 203, 29, 18, CARIBE, 1, (203 + 29) * 2 / 100)
it.t('Sarrafo de pinus para estrutura do painel', 8 * 357 / 100, b.SARRAFO_PINUS_M, 'm')
it.t('Perfil de proteção de piso', 3.57, b.PERFIL_PISO_M, 'm')
#   ⛔ a pedra vertical de 193 × 147 × 4 é da marmoraria, e os fixadores
#     metálicos de apoio dela também — a folha diz "estrutura metálica"

# ─── 11 ─────────────────────────────────────────────────────────────────
it = novo('Estar · adega com portas em vidro reflecta bronze', 17,
          '35,00 × 141,50 de adega · porta de 88 × 141 em 2 folhas de 43,75')
it.caixa(88, 141.5, 35, CARIBE, div=1, prat=4, nome='adega')
it.t('Porta em reflecta bronze com perfil champanhe', 2, b.PORTA_REFLECTA,
     'folha')
it.f('Dobradiça Blum para porta de vidro', 2 * b.dobradicas(141),
     b.DOBRADICA_VIDRO)
it.t('Estrutura metálica de suporte das garrafas', 2 * 1.415, b.SERRALHERIA_M,
     'm')
it.led(2 * 1.41, fontes=1, bottons=1)

# ─── 12 ─────────────────────────────────────────────────────────────────
it = novo('Estar · base do rack · portas ripadas e nichos', 17,
          '367 × 68 · 1 porta de abrir e 2 de correr, todas em MDF ripado Caribe')
it.caixa(367, 68, 50, it.interno, div=4, prat=2)
it.p('substrato da porta de abrir ripada', 35, 68, 15, CARIBE, 1,
     (35 + 68) * 2 / 100)
it.ripado(35, 68, 3.0, CARIBE, 'porta de abrir ripada')
it.p('substrato das portas de correr ripadas', 90, 68, 15, CARIBE, 2,
     (90 + 68) * 2 / 100)
it.ripado(180, 68, 3.0, CARIBE, 'portas de correr ripadas')
it.f('Sistema de correr Siforma SI Ocean 80', 1, b.SISTEMA_CORRER)
it.f('Desempenador de porta deslizante', 4, b.DESEMPENADOR)
it.p('nichos abertos do rack', 45, 68, 15, CARIBE, 4, .68)
it.t('Rodapé inox h = 2', 3.67, b.RODAPE_INOX_M, 'm')
it.led(3.67, fontes=1, bottons=2)
#   ⛔ frigobar 40 L e adega 14 garrafas Elettromec são do cliente

# ─── 13 ─────────────────────────────────────────────────────────────────
it = novo('Jantar · os dois pés da mesa', 17,
          'Pé 01 ovalado de 22 × 40 em planta · Pé 02 de Ø 28 · ambos com '
          'entalhamento diagonal · h = 73 até o tampo de quartzito')
it.p('lâminas do Pé 01 · miolo laminado', 40, 22, 18, CARIBE, 10)
it.p('lâminas do Pé 02 · miolo laminado', 28, 28, 18, CARIBE, 10)
it.p('envolvente entalhada dos dois pés', 100, 73, 6, CARIBE, 2, 1.46)
it.t('Usinagem CNC do entalhamento diagonal, o par', 1, 1500.0, 'par')
#   ⛔ o tampo de 150 × 77 em quartzito é da marmoraria


# ════════════════════════════════════════════════════════════════════════
# ACESSOS E CORREDOR · folha 18
# ════════════════════════════════════════════════════════════════════════

ambiente('04 Acessos e Corredor')
# ─── 14 ─────────────────────────────────────────────────────────────────
it = novo('Corredor · painel fixo com as duas portas embutidas', 18,
          '346,53 × 255,00 · 137 + 74 + 30,53 + 105 · a porta da suíte e a do '
          'quarto somem dentro do painel')
it.p('painel fixo do corredor', 346.53, 255, 18, CARIBE, 1,
     (346.53 + 255) * 2 / 100)
it.t('Sarrafo de pinus para estrutura do painel', 8 * 346.53 / 100, b.SARRAFO_PINUS_M, 'm')
it.t('Perfil de proteção de piso', 3.4653, b.PERFIL_PISO_M, 'm')
it.p('folha da porta da suíte', 104, 208, 18, CARIBE, 1, (104 + 208) * 2 / 100)
it.p('folha da porta do quarto', 105, 208, 18, CARIBE, 1, (105 + 208) * 2 / 100)
it.p('miolo sarrafeado das duas folhas', 104, 208, 15, it.interno, 2)
it.f('Dobradiça Blum', 2 * b.dobradicas(208), b.DOBRADICA)
it.f('Sistema pivô e fecho rolete de porta embutida', 2,
     b.FERRAGEM_PORTA_OCULTA)
it.t('Puxador cava usinado', 2 * 2.08, b.CAVA_M, 'm')
#   ⛔ a faixa de quartzito que atravessa o painel de 105 é da marmoraria

# ─── 15 ─────────────────────────────────────────────────────────────────
it = novo('Corredor · painel da vista 08', 18, '74,00 × 260,00 × 14,20')
it.p('painel da vista 08', 74, 260, 18, CARIBE, 1, (74 + 260) * 2 / 100)
it.p('caixa de profundidade 14,2', 14.2, 260, 15, CARIBE, 2, 2.60)
it.p('tampo e base da vista 08', 74, 14.2, 15, CARIBE, 2, .74)

# ─── 16 ─────────────────────────────────────────────────────────────────
it = novo('Corredor · painel da vista 07 com espelho', 18,
          '260,00 de altura · espelho de 75 × 220 fixado na marcenaria')
it.p('painel da vista 07', 149, 260, 18, CARIBE, 1, (149 + 260) * 2 / 100)
it.p('moldura de 8 em volta do espelho', 8, 220, 18, CARIBE, 4, 2.20)
it.t('Espelho fixado na marcenaria', .75 * 2.20, b.ESPELHO_M2)

# ─── 17 ─────────────────────────────────────────────────────────────────
it = novo('Corredor · ARMÁRIO F', 18,
          '90,40 × 250,00 × 37,05 · acabamento curvo ripado · 4 folhas')
it.caixa(90.4, 250, 37.05, it.interno, div=1, prat=4)
it.porta(45, 144, 2, CARIBE, botao=True)
it.porta(45, 68.36, 2, CARIBE, botao=True)
it.ripado(90.4, 250, 2.0, CARIBE, 'acabamento curvo ripado do armário F')
#   ⛔ a faixa de quartzito de 105,49 que corta o armário é da marmoraria


# ════════════════════════════════════════════════════════════════════════
# SUÍTE · folhas 19, 20 e 21
# ════════════════════════════════════════════════════════════════════════

ambiente('05 Suíte')
# ─── 18 ─────────────────────────────────────────────────────────────────
#   ⚠⚠ O FORRO DA SUÍTE NÃO TEM COTA. O mapa-chave da folha 19 mostra a
#     área em L de MDF Cipres ao lado da área de pintura branco neve, mas
#     sem nenhuma dimensão. 9,0 m² é LEITURA DO MAPA pela proporção com o
#     painel da cabeceira (357,5), não cota. Tem de ser medido.
FORRO_SUITE_M2 = 9.0
_forro = ('%.1f' % FORRO_SUITE_M2).replace('.', ',')
it = novo('Suíte · forro em MDF Cipres', 19,
          f'⚠ {_forro} m² lidos do mapa-chave — A FOLHA NÃO COTA ESTE FORRO')
it.p('réguas do forro da suíte', FORRO_SUITE_M2 * 10000 / 60, 60, 18, CIPRES, 1,
     FORRO_SUITE_M2 * 4)
it.t('Sarrafo de pinus para fixação do forro', 8 * 3.0, b.SARRAFO_PINUS_M, 'm')

# ─── 19 e 20 ────────────────────────────────────────────────────────────
for v, espelho in ((12, False), (13, True)):
    it = novo(f'Suíte · divisória MDF da vista {v}', 19,
              f'190,00 × 260,00 × 7,00 · ripado vazado de 4 × 240 × 4,20 na faixa '
              f'de 45{" · espelho de 83 × 235" if espelho else ""}')
    it.p('face em MDF Cipres', 145, 260, 18, CIPRES, 1, (145 + 260) * 2 / 100)
    it.p('face em MDF Fontana Linha Magma', 145, 251, 18, FONTANA, 1,
         (145 + 251) * 2 / 100)
    it.p('miolo e travamento da divisória', 7, 260, 18, CIPRES, 4, 2.60)
    it.ripado(45, 240, 4.2, CIPRES, f'ripado vazado da vista {v}')
    it.t('Perfil de proteção de piso', 1.90, b.PERFIL_PISO_M, 'm')
    if espelho:
        it.t('Espelho fixado na marcenaria', .83 * 2.35, b.ESPELHO_M2)

# ─── 21 ─────────────────────────────────────────────────────────────────
it = novo('Suíte · armário e nichos', 19,
          '138,00 × 140,00 · nichos de 52 e de 41 + 41 · 1 gaveta de 79 · '
          '4 fitas de LED')
it.caixa(138, 140, 35, CIPRES, div=2, prat=4)
it.p('fundo dos nichos em Fontana Magma', 52, 39, 6, FONTANA, 1, .52)
it.gaveta(79, 33, 32, 1, CIPRES, botao=True)
it.p('lateral de acabamento de 17', 17, 138, 18, CIPRES, 1, (17 + 138) * 2 / 100)
it.led(4 * 1.38, fontes=1, bottons=1)

# ─── 22 ─────────────────────────────────────────────────────────────────
it = novo('Suíte · painel da cabeceira', 19,
          '357,50 × 278,00 · Cipres em cima (140) e Fontana Magma embaixo (118) · '
          'bits de 0,5 e 1,5 · 2 fitas de LED')
it.p('faixa superior em MDF Cipres', 357.5, 140, 18, CIPRES, 1,
     (357.5 + 140) * 2 / 100)
it.p('faixa inferior em MDF Fontana Magma', 357.5, 118, 18, FONTANA, 1,
     (357.5 + 118) * 2 / 100)
it.p('rodapé e remate de 18', 38.5, 18, 18, CIPRES, 2, .56)
it.t('Sarrafo de pinus para estrutura do painel', 8 * 357.5 / 100, b.SARRAFO_PINUS_M, 'm')
it.t('Perfil de proteção de piso', 3.575, b.PERFIL_PISO_M, 'm')
it.t('Usinagem de bit de 0,5 e de 1,5', (357.5 * 3) / 100, b.FILETE_MAQ, 'm')
it.led(2 * 3.575, fontes=1, bottons=1)

# ─── 23 ─────────────────────────────────────────────────────────────────
it = novo('Suíte · sapateira da vista 10', 19,
          '90,00 de frente × 248,00 · 2 folhas, de 23,5 e de 44 pelo detalhe da folha 20')
it.caixa(90, 248, 35, CIPRES, div=1, prat=8)
it.porta(23.5, 248, 1, CIPRES, botao=True)
it.porta(44, 248, 1, CIPRES, botao=True)
it.p('nicho aberto de 55 ao lado', 55, 248, 18, CIPRES, 1, (55 + 248) * 2 / 100)

# ─── 24 ─────────────────────────────────────────────────────────────────
it = novo('Suíte · painel da vista 11', 20,
          '288,00 × 258,00 · Cacao Matt em cima, Fontana Magma no meio, Cipres '
          'embaixo · prateleira de 225,5 × 28 · rodapé inox')
it.p('faixa superior em Cacao Matt', 225.5, 51, 18, CACAO, 1, (225.5 + 51) * 2 / 100)
it.p('prateleira do painel', 225.5, 28, 18, CACAO, 1, (225.5 + 28) * 2 / 100)
#   ⭐ 225,5 de vão livre: a Base manda alma de aço acima de 1,20 m, e é
#     contra FLECHA, não contra empeno — prateleira comprida barriga.
it.f('Alma de aço · barra chata de 3 m', 1, b.ALMA_BARRA)
it.p('área central em Fontana Magma', 225.5, 101, 18, FONTANA, 1,
     (225.5 + 101) * 2 / 100)
it.p('laterais de 47 e de 38 em Fontana Magma', 47, 101, 18, FONTANA, 2, 1.01)
it.p('faixa inferior em MDF Cipres', 288, 92, 18, CIPRES, 1, (288 + 92) * 2 / 100)
it.t('Sarrafo de pinus para estrutura do painel', 6 * 288 / 100, b.SARRAFO_PINUS_M, 'm')
it.t('Perfil de proteção de piso', 2.88, b.PERFIL_PISO_M, 'm')
it.t('Rodapé inox h = 2', 2.88, b.RODAPE_INOX_M, 'm')
it.t('Usinagem de bit de 0,5', 288 * 2 / 100, b.FILETE_MAQ, 'm')
it.led(2.255, fontes=1, bottons=1)

# ─── 25 ─────────────────────────────────────────────────────────────────
it = novo('Suíte · bancada com 4 gavetas', 20,
          '178,00 × 40,00 × 75,00 · Cacao Matt · acabamento curvo r = 20')
it.caixa(178, 60, 40, it.interno, div=3, prat=0, fundo=6)
it.p('tampo da bancada', 178, 40, 18, CACAO, 1, (178 + 40) * 2 / 100)
it.gaveta(39, 58.5, 38, 4, CACAO, botao=True)
it.p('saia e remate de 10', 178, 10, 18, CACAO, 1, (178 + 10) * 2 / 100)
it.t('Usinagem de acabamento curvo r = 20', 1.78, b.FILETE_MAO, 'm')

# ─── 26 ─────────────────────────────────────────────────────────────────
#   ⚠ A FOLHA DESENHA UMA, MAS A CAMA TEM DOIS LADOS. As vistas 12C e 12D
#     são duas vistas da MESMA peça, e o detalhe vem no singular. Orço
#     DUAS — e a pergunta está registrada, porque a diferença é uma peça
#     inteira e não um arredondamento.
N_CABECEIRA = 2
it = novo(f'Suíte · {N_CABECEIRA} mesas de cabeceira', 20,
          '65,00 × 40,00 × 50,00 · 3 gavetas de 49 × 14 · tampo Fontana Magma, '
          'corpo Cipres, fita metálica em latão dourado · r = 8')
it.caixa(65, 50, 40, CIPRES, div=0, prat=0, nome='corpo')
it.p('tampo em Fontana Magma', 65, 40, 18, FONTANA, N_CABECEIRA, (65 + 40) * 2 / 100)
it.gaveta(49, 14, 36, 3 * N_CABECEIRA, CIPRES)
for _p in list(it.pecas):                 # ⭐ a caixa foi somada uma vez só
    if _p['nome'].startswith('corpo') and N_CABECEIRA > 1:
        _p['qtd'] *= N_CABECEIRA
it.t('Friso em perfil laqueado · ⚠ proxy da fita de latão dourado',
     (0.65 * 2 + 0.40 * 2) * N_CABECEIRA, b.FRISO_LAQUEADO_M, 'm')
it.t('Usinagem de acabamento curvo r = 8', 2.1 * N_CABECEIRA, b.FILETE_MAO, 'm')

ambiente('06 Closet')
# ─── 27 · O CLOSET ──────────────────────────────────────────────────────
#   ⭐⭐ A MAIOR PEÇA DO APARTAMENTO, e a mais cara por um motivo que o
#     desenho esconde e o render grita: AS PORTAS NÃO SÃO DE MDF. São
#     perfil metálico dourado com vidro, de piso a teto, nas três vistas.
it = novo('Closet · vista 9A', 21,
          '418,50 × 257,00 · 55 + 48,5 + 48,5 + 50,5 + 8 + 87 + 87 + 32 · '
          '4 portas de perfil e vidro, 6 gavetas, 3 nichos, 2 maleiros')
it.caixa(418.5, 257, 60, CIPRES, div=5, prat=7)
it.t('Porta de closet em perfil de alumínio com vidro', 4,
     b.PORTA_VIDRO_PERFIL, 'folha')
it.f('Dobradiça Blum para porta de vidro', 4 * b.dobradicas(257),
     b.DOBRADICA_VIDRO)
it.gaveta(48.5, 14, 55, 4, CIPRES, botao=True)
it.gaveta(87, 14, 55, 2, CIPRES, botao=True)
it.p('maleiros', 48.5, 60, 18, CIPRES, 2, .485)
it.p('fundo dos 3 nichos', 50.5, 40, 6, CIPRES, 3, .505)
it.f('Cabideiro em metal', 3, b.CABIDEIRO)
it.p('lateral de acabamento de 55', 55, 257, 18, CIPRES, 1, (55 + 257) * 2 / 100)
it.p('lateral de acabamento de 32', 32, 257, 18, CIPRES, 1, (32 + 257) * 2 / 100)
it.led(10.0, fontes=2, bottons=2)

# ─── 28 ─────────────────────────────────────────────────────────────────
it = novo('Closet · vista 9B', 21,
          '150,00 × 257,00 · 43,5 + 43,5 + 53 · 3 portas de perfil e vidro')
it.caixa(150, 257, 60, CIPRES, div=2, prat=3)
it.t('Porta de closet em perfil de alumínio com vidro', 3,
     b.PORTA_VIDRO_PERFIL, 'folha')
it.f('Dobradiça Blum para porta de vidro', 3 * b.dobradicas(257),
     b.DOBRADICA_VIDRO)
it.p('maleiro', 150, 60, 18, CIPRES, 1, 1.50)
it.f('Alma de aço · barra chata de 3 m', 1, b.ALMA_BARRA)   # 150 de vão
it.f('Cabideiro em metal', 2, b.CABIDEIRO)
it.led(6.0, fontes=1, bottons=1)

# ─── 29 ─────────────────────────────────────────────────────────────────
it = novo('Closet · sapateira da vista 9C', 21,
          '90,00 × 257,00 · 2 portas de perfil e vidro · 8 × 22,50 = 180 de '
          'prateleira INCLINADA em cada coluna')
it.caixa(90, 257, 35, CIPRES, div=1, prat=0)
it.t('Porta de closet em perfil de alumínio com vidro', 2,
     b.PORTA_VIDRO_PERFIL, 'folha')
it.f('Dobradiça Blum para porta de vidro', 2 * b.dobradicas(257),
     b.DOBRADICA_VIDRO)
it.p('prateleiras inclinadas', 44, 33, 18, CIPRES, 16, .44)
it.f('Suporte de prateleira Blum, jogo de 4', 16, b.SUPORTE_JOGO)
it.t('Usinagem de encaixe inclinado de prateleira', 16 * .44, b.FILETE_MAQ, 'm')
it.led(8.0, fontes=1, bottons=1)


# ════════════════════════════════════════════════════════════════════════
# BANHO DA SUÍTE · folha 22   ·   BANHEIRO SOCIAL · folha 23
# ════════════════════════════════════════════════════════════════════════

ambiente('07 Banho da Suíte')
# ─── 30 ─────────────────────────────────────────────────────────────────
it = novo('Banho da suíte · espelheira superior', 22,
          '183,00 × 110,00 × 17,00 · 4 folhas espelhadas · LED no eixo h = 90')
it.caixa(183, 110, 17, it.interno, div=3, prat=4)
it.p('estrutura das 4 folhas espelhadas', 40.44, 110, 18, CINZA, 4,
     (40.44 + 110) * 2 / 100)
it.t('Espelho colado na folha', 1.52 * 1.10, b.ESPELHO_M2)
it.f('Dobradiça Blum', 4 * b.dobradicas(110), b.DOBRADICA)
it.led(1.83, fontes=1, bottons=1)

# ─── 31 ─────────────────────────────────────────────────────────────────
it = novo('Banho da suíte · armário inferior', 22,
          '103,00 × 55,00 × 40,00 · 2 portas de 32,5 e 3 gavetas de 34')
it.caixa(103, 55, 40, it.interno, div=2, prat=1)
it.porta(32.5, 55, 2, CINZA, cava=True)
it.gaveta(34, 17, 36, 3, CINZA, cava=True)
#   ⚠ a "bancada nova" de 80 da mesma folha não entra: a folha não diz o
#     material e bancada de banho, neste projeto, tem sido sempre pedra

ambiente('08 Banheiro Social')
# ─── 32 ─────────────────────────────────────────────────────────────────
it = novo('Banheiro social · ARMÁRIO H', 23,
          '77,00 × 168,00 · 2 portas de 38,25 × 138 · nicho de 27 na base')
it.caixa(77, 168, 33, it.interno, div=0, prat=3)
it.porta(38.25, 138, 2, CINZA, cava=True)
it.p('nicho aberto da base', 77, 27, 18, CINZA, 2, (77 + 27) * 2 / 100)

# ─── 33 ─────────────────────────────────────────────────────────────────
it = novo('Banheiro social · ARMÁRIO G', 23,
          '70,00 × 140,00 × 19,00 · porta espelhada · puxador cava na própria '
          'estrutura do espelho')
it.caixa(70, 140, 19, it.interno, div=0, prat=2)
it.p('estrutura da folha espelhada', 60, 138, 18, CINZA, 1, (60 + 138) * 2 / 100)
it.t('Espelho colado na folha', .60 * 1.38, b.ESPELHO_M2)
it.f('Dobradiça Blum', b.dobradicas(138), b.DOBRADICA)
it.t('Puxador cava usinado na estrutura do espelho', 1.38 * 2, b.CAVA_M, 'm')
it.led(1.40 * 2, fontes=1, bottons=1)

# ─── 34 ─────────────────────────────────────────────────────────────────
it = novo('Banheiro social · espelho da vista 16', 23, '140,00 × 140,00')
it.t('Espelho fixado, 140 × 140', 1.40 * 1.40, b.ESPELHO_M2)
it.t('Sarrafo de pinus de apoio do espelho', 3 * 1.40, b.SARRAFO_PINUS_M, 'm')


# ════════════════════════════════════════════════════════════════════════
# QUARTO · folhas 24 e 25
# ════════════════════════════════════════════════════════════════════════

ambiente('09 Quarto')
# ─── 35 ─────────────────────────────────────────────────────────────────
it = novo('Quarto · armário com portas de correr', 24,
          '305,00 × 255,00 × 64,00 · 2 folhas de correr de 97,5 em Cacao Matt · '
          'nichos abertos em Cipres · retorno em L de 105')
it.caixa(305, 255, 64, CIPRES, div=3, prat=6)
it.p('folhas de correr em Cacao Matt', 97.5, 251, 18, CACAO, 2,
     (97.5 + 251) * 2 / 100)
it.f('Sistema de correr Siforma SI Ocean 80', 1, b.SISTEMA_CORRER)
it.f('Desempenador de porta deslizante', 4, b.DESEMPENADOR)
it.p('puxador da porta em MDF Cipres', 10, 251, 18, CIPRES, 2, 2.51)
it.p('bancada e prateleira do armário', 118, 36, 18, CIPRES, 2, (118 + 36) * 2 / 100)
it.p('retorno em L', 105, 69, 18, CIPRES, 2, (105 + 69) * 2 / 100)
it.led(3.05, fontes=1, bottons=1)

# ─── 36 ─────────────────────────────────────────────────────────────────
it = novo('Quarto · móvel baú com porta retrátil', 24,
          '209,00 × 36,00 · 118 + 91 · porta retrátil em Cacao Matt')
it.caixa(209, 36, 64, it.interno, div=1, prat=0)
it.p('frente retrátil em Cacao Matt', 91, 36, 18, CACAO, 1, (91 + 36) * 2 / 100)
it.p('frente fixa de 118 em Cacao Matt', 118, 36, 18, CACAO, 1,
     (118 + 36) * 2 / 100)
it.f('Sistema de porta retrátil', 1, b.SISTEMA_CORRER)
it.f('Pulsador Blum Tip-on', 1, b.PULSADOR)

# ─── 37 ─────────────────────────────────────────────────────────────────
it = novo('Quarto · painel fixo com espelho', 25,
          '333,00 × 255,00 × 13,00 · 227 de painel + 106 de moldura · '
          'espelho de 75 × 220 fixado na marcenaria')
it.p('painel fixo em MDF Cipres', 227, 255, 18, CIPRES, 1, (227 + 255) * 2 / 100)
it.p('moldura do espelho', 106, 248, 18, CIPRES, 1, (106 + 248) * 2 / 100)
it.p('caixa de profundidade 13', 13, 255, 15, CIPRES, 2, 2.55)
it.t('Sarrafo de pinus para estrutura do painel', 8 * 333 / 100, b.SARRAFO_PINUS_M, 'm')
it.t('Perfil de proteção de piso', 3.33, b.PERFIL_PISO_M, 'm')
it.t('Espelho fixado na marcenaria', .75 * 2.20, b.ESPELHO_M2)

# ─── 38 ─────────────────────────────────────────────────────────────────
it = novo('Quarto · revestimento por baixo da viga', 25, '333,00 × 23,00')
it.p('revestimento da viga', 333, 23, 18, CIPRES, 1, (333 + 23) * 2 / 100)
it.t('Sarrafo de pinus de fixação', 2 * 3.33, b.SARRAFO_PINUS_M, 'm')


# ════════════════════════════════════════════════════════════════════════
# O MOTOR · idêntico ao do Bar Cariocando, pelo mesmo motivo
# ════════════════════════════════════════════════════════════════════════
def _levanta(it):
    area, fita_cor, fita_br, pecas = {}, 0.0, 0.0, 0
    for p in it.pecas:
        k = (p['mat'], p['esp'])
        area[k] = area.get(k, 0.0) + p['L'] * p['A'] / 10000 * p['qtd']
        pecas += p['qtd']
        #   ⛔ SEM BRANCO TX, TODA A FITA É DE COR. A fita branca a R$ 2,00
        #     existia só porque o interior era branco; agora o interior é o
        #     padrão do ambiente e a fita acompanha a face, a R$ 3,00.
        fita_cor += p['fita'] * p['qtd']
    return dict(area=area, fita_cor=fita_cor, fita_br=fita_br, pecas=pecas,
                c_terc=sum(q * u for _n, q, u, _un in it.terc),
                c_fer=sum(q * u for _n, q, u in it.fer))


def frete():
    """⭐ O frete é POR AMBIENTE e some de todo orçamento feito a olho.
    Na planilha da casa ele é a única célula digitada da aba."""
    return {a: v * b.FRETE_VIAGEM for a, v in VIAGENS.items()}


def custo(itens):
    """⭐⭐ O ARREDONDAMENTO DE CHAPA É DO PROJETO, NÃO DO ITEM.

    ⛔ Se cada item arredondasse as suas chapas, 38 itens em 7 materiais
      dariam dezenas de chapas de sobra imaginárias, e a soma dos itens
      estouraria o preço do projeto sem ninguém reclamar.
    ⭐ Quem compra chapa é o PROJETO. A conta de chapa do item é
      fracionária, e a sobra do arredondamento é RATEADA pela área — que é
      o que a causa. Assim a soma dos itens É o preço do projeto, por
      construção, e a trava no fim deste arquivo prova isso toda vez."""
    L = [(it, _levanta(it)) for it in itens]
    area = {}
    for _it, q in L:
        for k, a in q['area'].items():
            area[k] = area.get(k, 0.0) + a
    rend = b.CHAPA_M2 * b.APROV
    chapas = {k: math.ceil(a / rend) for k, a in area.items()}
    preco = {k: b.PRECO[f'{k[0]} {k[1]}'] for k in area}
    c_chapa = sum(n * preco[k] for k, n in chapas.items())
    sobra = {k: chapas[k] * preco[k] - area[k] / rend * preco[k] for k in area}
    n_chapas, n_pecas = sum(chapas.values()), sum(q['pecas'] for _i, q in L)

    def _item(q):
        ch = sum(a / rend * preco[k] + sobra[k] * (a / area[k])
                 for k, a in q['area'].items())
        corte = (n_chapas * b.CORTE_CHAPA * (q['pecas'] / n_pecas)
                 + q['pecas'] * b.CORTE_PECA)
        fita = (q['fita_cor'] * b.FITA_COR + q['fita_br'] * b.FITA_BRANCA) * b.FITA_PERDA
        cons = (ch + fita) * b.CONSUMIVEIS
        return (ch + fita + corte + cons + q['c_terc'] + q['c_fer']) * (1 + b.EMBALAGEM)

    c_fita = sum(q['fita_cor'] * b.FITA_COR + q['fita_br'] * b.FITA_BRANCA
                 for _i, q in L) * b.FITA_PERDA
    diretos = [_item(q) for _it, q in L]
    #   ⭐ O FRETE É DO AMBIENTE, e tem de cair dentro do item para que a
    #     soma dos itens continue sendo o preço do projeto. Rateio pelo
    #     custo direto de cada item dentro do seu ambiente.
    F = frete()
    base_amb = {}
    for (it, _q), d in zip(L, diretos):
        base_amb[it.ambiente] = base_amb.get(it.ambiente, 0.0) + d
    diretos = [d + F.get(it.ambiente, 0.0) * (d / base_amb[it.ambiente])
               for (it, _q), d in zip(L, diretos)]
    c_frete = sum(F.values())
    return dict(area=area, chapas=chapas, preco=preco, c_chapa=c_chapa,
                pecas=n_pecas, n_chapas=n_chapas,
                fita_cor=sum(q['fita_cor'] for _i, q in L),
                fita_br=sum(q['fita_br'] for _i, q in L), c_fita=c_fita,
                c_corte=n_chapas * b.CORTE_CHAPA + n_pecas * b.CORTE_PECA,
                c_cons=(c_chapa + c_fita) * b.CONSUMIVEIS,
                c_terc=sum(q['c_terc'] for _i, q in L),
                c_fer=sum(q['c_fer'] for _i, q in L),
                c_frete=c_frete, diretos=diretos, direto=sum(diretos), L=L)


def brl(v):
    return 'R$ ' + f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')


def preco_item(direto):
    return direto / (b.BASE - b.MC)


def por_ambiente():
    """⭐ O que cada aba da planilha recebe: custo direto, preço e abertura."""
    T = custo(M)
    R = {}
    for (it, q), d in zip(T['L'], T['diretos']):
        a = R.setdefault(it.ambiente, dict(itens=[], direto=0.0, pecas=0,
                                           area={}, fita_cor=0.0, fita_br=0.0,
                                           c_terc=0.0, c_fer=0.0, folhas=set()))
        a['itens'].append((it, d))
        a['direto'] += d
        a['pecas'] += q['pecas']
        a['fita_cor'] += q['fita_cor']; a['fita_br'] += q['fita_br']
        a['c_terc'] += q['c_terc']; a['c_fer'] += q['c_fer']
        a['folhas'].add(it.folha)
        for k, v in q['area'].items():
            a['area'][k] = a['area'].get(k, 0.0) + v
    return T, R


if __name__ == '__main__':
    W = 100
    T = custo(M)
    #   ⛔ O RÓTULO SE CALCULA, nunca se digita.
    _c = ' e '.join([t for t, v in (('RT de %.0f%%' % (b.RT * 100), b.RT),
                                    ('vendedor de %.0f%%' % (b.VENDEDOR * 100),
                                     b.VENDEDOR)) if v]) or 'sem RT e sem vendedor'
    print('═' * W)
    print(f'{b.CLIENTE.upper()} · {b.PROJETO} — {b.EXECUTIVO}')
    print(f'  ferragem BLUM · BASE {b.BASE:.2%} (com {_c}) · MC {b.MC:.0%}')
    print('═' * W)
    for it, direto in zip(M, T['diretos']):
        pv = preco_item(direto)
        print(f'■ [folha {it.folha}] {it.nome}')
        print(f'    {it.obs}')
        print('    %-58s %14s   %14s' % ('', brl(direto), brl(pv)))
    print('─' * W)
    print('  CHAPAS')
    for k in sorted(T['chapas']):
        print('    %-26s %6.2f m²  →  %2d chapa(s) × %-12s = %s'
              % (f'{k[0]} {k[1]} mm', T['area'][k], T['chapas'][k],
                 brl(T['preco'][k]), brl(T['chapas'][k] * T['preco'][k])))
    print('    %-26s %6.1f m de cor · %.1f m de branca'
          % ('FITA', T['fita_cor'], T['fita_br']))
    print()
    for rot, v in (('chapa', T['c_chapa']), ('fita', T['c_fita']),
                   ('corte', T['c_corte']), ('consumíveis', T['c_cons']),
                   ('terceirizado', T['c_terc']), ('ferragem Blum', T['c_fer']),
                   ('frete · %d viagens' % sum(VIAGENS.values()), T['c_frete'])):
        print('    %-44s %16s' % (rot, brl(v)))
    print('    %-44s %16s' % ('CUSTO DIRETO (com embalagem)', brl(T['direto'])))
    print('─' * W)
    pv = preco_item(T['direto'])
    assert abs(pv - sum(preco_item(d) for d in T['diretos'])) < 0.01, \
        '⛔ a soma dos itens não bate com o motor'
    print('  %-44s %16s' % (f'PREÇO · BLUM, MC {b.MC:.0%}', brl(pv)))
    print('  %-44s %16s' % ('  MC realizada', f'{b.BASE - T["direto"] / pv:.1%}'))
    print('  %-44s %16s' % ('  itens · peças · chapas',
                            f'{len(M)} · {T["pecas"]} · {T["n_chapas"]}'))
    print('═' * W)
