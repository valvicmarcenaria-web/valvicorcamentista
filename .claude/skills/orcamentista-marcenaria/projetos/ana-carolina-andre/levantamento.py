# -*- coding: utf-8 -*-
"""ANA CAROLINA E ANDRÉ · Apto Funcionários, Ed. La Concordia, Rua Inconfidentes
307, apto 21, BH · projeto [35] de Ana Maria (Archicad, r00).

⭐⭐ REVISÃO DE 08/11/2026 [Jonathan, 09/11/2026]: "interno agora será BRANCO TX,
   externo em PALHA, no closet teremos um PAR DE PORTAS com aplicação de PALHA
   SINTÉTICA (mencionar isso na proposta), ferragens mantém BLUM. segue arquivos
   atualizados" — 35_.1_SUITE_MASTER_1 (A2) · 35_.1_QUARTO_GABRIEL_1 (A3) ·
   35_.1_CLOSET_ISABELLA_1 (A2), de 08/11/2026.
   E nas respostas do mesmo dia:
   · o par de palha sintética é o MÓDULO DE 50 do closet da suíte (lado Ana
     Carolina), o que a prancha chama de "1 porta de giro com tela para
     ventilação" — virou duas folhas;
   · o ROUPEIRO DA SUÍTE MASTER (200, "um lado pra cada") ENTRA na proposta;
   · o ARMÁRIO DO QUARTO ISABELLA (Quarto Isabella 01, 288,5) ENTRA;
   · "adicione dois cabideiros desse: Varotti calceiro Slow Sense FGVTN" — os
     dois CABIDEIROS CALCEIROS RETRÁTEIS do lado André, um por módulo.

A prancha nova É COTADA nas elevações: 270 do piso ao teto = 10 de rodapé +
260 de caixa · maleiro de 70 · cabideiro de 100 · 90 de gavetas.
A NOTA DE MATERIAL de todas as elevações: "interior em MDF BRANCO · exterior em
MDF DURATEX PALHA · ferragens BLUM · corrediças ocultas com freio".

Regra do que é PALHA (o exterior):
  · portas de giro, folhas de correr de MDF e o rodapé;
  · a lateral que aparece (a que fica para o quarto ou para a passagem);
  · a lateral fixa recuada do Quarto Isabella;
  · as frentes de gaveta que a prancha PINTA de Palha (o roupeiro da suíte e o
    armário do Quarto Isabella, que têm porta de correr).
O resto é BRANCO TX: caixaria, divisória, base e teto, fundo, prateleira,
caixas de gaveta e as frentes de gaveta atrás de porta de giro.

Premissas minhas (vão como dúvida numerada na planilha):
  · porta de giro em 15 mm, sobreposta à caixa inteira; módulo acima de 60
    leva DUAS folhas; cinco dobradiças Blum por folha (passa de 200); cava
    usinada de 1 m por folha;
  · folha de espelho que corre = "Porta de espelho em alumínio" da Base;
  · "sapateiro" = gaveta baixa com corrediça Blum (uma corrediça cada);
  · caixa de roupeiro de correr com 55 de fundo (os 65 da planta menos os 10
    do trilho);
  · rodapé de 10 recuado em Palha + perfil de proteção de piso.

Cada peça: (peça, observação, C, L, QTD, chave da Base, fita em m por peça, tipo
de fita) · ferragem: (peça, observação, QTD, UN, chave) · terceirizado por m²,
sem chapa: (peça, observação, C, L, QTD, UN, chave).
"""
ITENS = []      # (amb, nn, móvel, medida, cadeia, pecas, ferragens)

def item(amb, movel, medida, cadeia):
    d = dict(amb=amb, movel=movel, medida=medida, cadeia=cadeia, pecas=[], ferr=[], terc=[])
    ITENS.append(d); return d

def P(it, nome, obs, c, l, qtd, chave, fita=0.0, tipo=None):
    tipo = tipo or ('Fita Branco TX' if 'Branco' in chave else 'Fita cor')   # Palha → fita de cor
    it['pecas'].append((nome, obs, round(c, 1), round(l, 1), qtd, chave, fita, tipo))

def F(it, nome, obs, qtd, un, chave):
    it['ferr'].append((nome, obs, qtd, un, chave))

def T(it, nome, obs, c, l, qtd, chave):
    """Terceirizado por m² (folha pronta, tela): não entra no plano de corte."""
    it['terc'].append((nome, obs, c, l, qtd, 'm²', chave))

# ⭐ EXTERIOR em PALHA DURATEX (chave própria do projeto na Base, preço da linha
#   Melamínico Fosco) · INTERIOR em BRANCO TX [Jonathan, 09/11/2026].
PALHA15, PALHA18, PALHA6 = 'MDF Palha 15', 'MDF Palha 18', 'MDF Palha 6'
COR15, COR18 = PALHA15, PALHA18
BR15, BR18, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 18', 'MDF Branco TX 6'

CAIXA = 260          # 270 do piso ao teto menos 10 de rodapé
DIV = CAIXA - 3      # divisória entre base e teto de 15
FOLHA = 259.5        # porta de giro: a caixa menos meio centímetro de folga

def gavetas(it, n, larg, alt, prof, frente=BR15, rotulo='Gaveta', obs=''):
    li = larg - 6.6
    P(it, f'{rotulo} · frente', obs or ('Palha, pintada na prancha' if frente == COR15 else 'Branco TX, atrás da porta'),
      larg, alt, n, frente, 2 * (larg + alt) / 100)
    P(it, f'{rotulo} · lateral da caixa', '', prof - 5, alt - 5, 2 * n, BR15, (prof - 5) / 100)
    P(it, f'{rotulo} · frente e traseira da caixa', '', li, alt - 5, 2 * n, BR15, li / 100)
    P(it, f'{rotulo} · fundo da caixa', 'encaixe em rasgo, sem fita', li + 1, prof - 6, n, BR6)
    F(it, 'Corrediça Blum TANDEM', f'oculta, com BLUMOTION · uma por {rotulo.lower()}', n, 'gaveta', 'Corrediça')

def prateleiras(it, n, vao, prof, chave, obs=''):
    P(it, 'Prateleira', obs or f'vão de {vao}', vao - 0.4, prof - 3, n, chave, vao / 100)
    F(it, 'Suporte de prateleira', 'jogo de 4 por prateleira interna', n, 'jogo', 'Suporte de prateleira')

def fixas(it, n, vao, prof, chave, obs):
    """Piso de maleiro e tampo das gavetas: fixos na caixa, sem suporte."""
    P(it, 'Prateleira fixa', obs, vao - 0.4, prof - 3, n, chave, vao / 100)

def rodape(it, L, chave=COR15):
    pecas = [L] if L <= 273 else [L / 2, L / 2]
    for x in pecas:
        P(it, 'Rodapé recuado', 'h 10, recuado da frente' + (' · emenda no meio' if len(pecas) > 1 else ''),
          x, 10, 1, chave, x / 100)
    F(it, 'Perfil de proteção de piso', 'no rodapé que toca o chão', round(L / 100, 2), 'm',
      'Perfil de proteção de piso')

def dobradicas(alt):
    return 2 if alt <= 90 else 3 if alt <= 160 else 4 if alt <= 200 else 5

def giro(it, n, larg, alt, obs, chave=COR15):
    """Porta de giro com puxador em cava [Jonathan, 06/11/2026]."""
    nd = dobradicas(alt)
    P(it, 'Porta de giro', obs, alt, larg, n, chave, 2 * (alt + larg) / 100)
    F(it, 'Dobradiça Blum CLIP top BLUMOTION', f'{nd} por folha de ' + f'{alt:g}'.replace('.', ',') + ' de altura', nd * n, 'un', 'Dobradiça')
    F(it, 'Cava usinada', 'puxador cava na própria folha, 1 m por folha', n, 'm', 'Cava usinada')

def correr_siforma(it, larg_vao, alt, nfolhas=2):
    """Portas de correr no SI Forma, UMA de espelho prata e as outras de MDF Palha."""
    folha = round(larg_vao / nfolhas + 3, 1)
    nmdf = nfolhas - 1
    P(it, 'Porta de correr', '18 mm Palha · a folha de MDF, com transpasse', alt, folha, nmdf, COR18, 2 * (alt + folha) / 100)
    T(it, 'Porta de correr de espelho prata', 'folha pronta: esquadria de alumínio + espelho prata · sem chapa e sem fita',
      alt, folha, 1, 'Porta de espelho em alumínio')
    if nfolhas == 2:
        F(it, 'Sistema deslizante SI Ocean 80', 'Siforma · amortecimento nos dois sentidos · um conjunto para as duas folhas',
          1, 'cj', 'Sistema deslizante SI Forma')
    else:
        F(it, 'Sistema deslizante SI Ocean 80 · três folhas', 'Siforma · amortecimento nos dois sentidos · trilho duplo para três folhas',
          1, 'cj', 'Sistema deslizante SI Forma 3 portas')
    F(it, 'Desempenador de porta', 'só nas folhas de MDF · dois por folha de 70 cm ou mais', nmdf * (2 if folha >= 70 else 1), 'un',
      'Desempenador de porta')
    F(it, 'Cava usinada', 'puxador cava vertical nas folhas de MDF, 1 m por folha', nmdf, 'm', 'Cava usinada')

# ═══ 01 · SUÍTE MASTER · roupeiro (SUITE MASTER_E1, cotada) ═══════════════
#   "UM LADO PRA CADA": 200 = 2,5 + 96,5 + 2,5 + 96,5 + 2,5 · prof. 65 na planta.
#   70 de maleiro + 100 de cabideiro + 90 de gavetas + 10 de rodapé.
#   Lado esquerdo: 3 gavetas + 1 sapateiro · lado direito: 4 gavetas.
#   "armário com 2 portas de correr sendo uma de espelho prata".
it = item('Suíte master', 'Roupeiro com portas de correr, uma de espelho', '200 × 270 × 65',
          'E1 cotada: 70 + 100 + 90 + 10 = 270 · 200 = dois lados de 96,5 · planta 65 de fundo (55 de caixa + 10 de trilho)')
P(it, 'Lateral aparente', 'a que fica para o quarto', CAIXA, 55, 1, COR15, 2.60 + 0.55)
P(it, 'Lateral de parede', 'encostada na parede do closet', CAIXA, 55, 1, BR15, 2.60)
P(it, 'Base e teto', '', 197, 55, 2, BR15, 1.97)
P(it, 'Divisória', 'um lado para cada', DIV, 53, 1, BR15, DIV / 100)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 197, DIV, 1, BR6)
fixas(it, 4, 96.5, 55, BR18, 'piso do maleiro e tampo das gavetas, dois por lado · 18 mm: vão de 96,5')
F(it, 'Cabideiro', 'um por lado', 2, 'un', 'Cabideiro')
gavetas(it, 7, 96.5, 20, 50, frente=COR15)
gavetas(it, 1, 96.5, 20, 50, frente=COR15, rotulo='Sapateiro')
correr_siforma(it, 200, CAIXA - 1)
rodape(it, 200)

# ═══ 02 · CLOSET SUÍTE MASTER · lado Ana Carolina (CLOSET SUITE MASTER_E1) ═
#   331 de parede a parede = 2,5 + 4 × 79,5 + 4 × 2,5 · prof. 61.
#   Módulo 1: prateleira, cabideiro, 3 gavetas finas, 1 gaveta, 1 sapateiro.
#   Módulos 2 e 3: maleiro, cabideiro (no 3, de calças), 3 gavetas, 1 sapateiro.
#   Módulo 4: maleiro, cabideiro longo, 1 sapateiro.
#   "2 gavetas finas com tranca" · "armário com 8 portas de giro".
it = item('Closet suíte master', 'Armário do lado Ana Carolina, oito portas de giro', '331 × 270 × 61',
          'E1 cotada: 331 = quatro módulos de 79,5 · 70 + 100 + 90 + 10 = 270 · de parede a parede · oito folhas')
P(it, 'Lateral de parede', 'as duas pontas encostam na parede', CAIXA, 61, 2, BR15, 2.60)
P(it, 'Divisória', 'entre os módulos', DIV, 59, 3, BR15, DIV / 100)
P(it, 'Base e teto', 'emenda sobre a divisória do meio · 331 não sai de chapa', 164, 61, 4, BR15, 1.64)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 165, DIV, 2, BR6)
fixas(it, 7, 79.5, 61, BR18, 'piso dos três maleiros e tampo das gavetas dos quatro módulos · 18 mm')
prateleiras(it, 1, 79.5, 61, BR18, 'módulo 1, a prateleira do alto · 18 mm')
F(it, 'Cabideiro', 'um por módulo · o do módulo 3 é de calças, o do 4 é longo', 4, 'un', 'Cabideiro')
gavetas(it, 3, 79.5, 12, 55, rotulo='Gaveta fina')
F(it, 'Fechadura de gaveta', '"2 gavetas finas com tranca"', 2, 'un', 'Fechadura de gaveta')
gavetas(it, 7, 79.5, 18, 55)
gavetas(it, 4, 79.5, 18, 55, rotulo='Sapateiro')
giro(it, 8, 41.1, FOLHA, '15 mm Palha · duas folhas por módulo de 79,5 · puxador em cava')
rodape(it, 331)

# ═══ 02 · CLOSET SUÍTE MASTER · lado André (CLOSET SUITE MASTER_E2) ═══════
#   185 = 2,5 + 88,5 + 2,5 + 89 + 2,5 · prof. 60 · da parede até a porta.
#   Cada módulo: maleiro, cabideiro e, embaixo, "cabideiro calceiro retrátil"
#   e um sapateiro. "armário com 4 portas de giro".
#   ⭐ os dois calceiros: Varotti Slow Sense FGVTN [Jonathan, 09/11/2026].
it = item('Closet suíte master', 'Armário do lado André, quatro portas de giro', '185 × 270 × 60',
          'E2 cotada: 185 = 88,5 + 89 · 70 + 100 + 90 + 10 = 270 · uma ponta na parede, a outra na passagem')
P(it, 'Lateral aparente', 'a que fica para a passagem da porta', CAIXA, 60, 1, COR15, 2.60 + 0.60)
P(it, 'Lateral de parede', '', CAIXA, 60, 1, BR15, 2.60)
P(it, 'Divisória', '', DIV, 58, 1, BR15, DIV / 100)
P(it, 'Base e teto', '', 182, 60, 2, BR15, 1.82)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 182, DIV, 1, BR6)
fixas(it, 4, 89, 60, BR18, 'piso do maleiro e divisão do calceiro, dois por módulo · 18 mm')
F(it, 'Cabideiro', 'um por módulo, no meio', 2, 'un', 'Cabideiro')
F(it, 'Cabideiro calceiro retrátil Slow Sense', 'Varotti FGVTN · deslizante, com amortecimento · um por módulo', 2, 'un',
  'Calceiro Slow Sense')
gavetas(it, 2, 89, 18, 55, rotulo='Sapateiro')
giro(it, 4, 46.1, FOLHA, '15 mm Palha · duas folhas por módulo de 89 · puxador em cava')
rodape(it, 185)

# ═══ 02 · CLOSET SUÍTE MASTER · módulo de 50 do lado Ana Carolina (E2) ════
#   55 = 2,5 + 50 + 2,5 · prof. 60 · da porta até a parede.
#   4 prateleiras + 3 gavetas + 1 sapateiro.
#   ⭐ "um par de portas com aplicação de PALHA SINTÉTICA" [Jonathan, 09/11/2026]
#   — a prancha desenha "1 porta de giro com tela para ventilação": viraram
#   duas folhas de MDF Palha 18 com requadro e a tela de palha sintética.
it = item('Closet suíte master', 'Módulo de 50 com par de portas em palha sintética', '55 × 270 × 60',
          'E2 cotada: 55 = 2,5 + 50 + 2,5 · 70 + 100 + 90 + 10 = 270 · duas folhas de 27,3 com requadro e tela')
P(it, 'Lateral aparente', 'a que fica para a passagem da porta', CAIXA, 60, 1, COR15, 2.60 + 0.60)
P(it, 'Lateral de parede', '', CAIXA, 60, 1, BR15, 2.60)
P(it, 'Base e teto', '', 52, 60, 2, BR15, 0.52)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 52, DIV, 1, BR6)
prateleiras(it, 4, 50, 60, BR15)
fixas(it, 1, 50, 60, BR15, 'tampo das gavetas')
gavetas(it, 3, 50, 18, 55)
gavetas(it, 1, 50, 18, 55, rotulo='Sapateiro')
P(it, 'Porta de giro com requadro', '18 mm Palha · moldura de 7 com o miolo vazado para a tela', FOLHA, 27.3, 2, COR18,
  2 * (FOLHA + 27.3) / 100 + 2 * (FOLHA - 14 + 27.3 - 14) / 100)
T(it, 'Palha sintética', 'tela aplicada por trás do requadro · ventila o módulo', FOLHA - 14 + 3, 27.3 - 14 + 3, 2, 'Palha sintética')
F(it, 'Dobradiça Blum CLIP top BLUMOTION', f'{dobradicas(FOLHA)} por folha de 259,5 de altura', 2 * dobradicas(FOLHA), 'un', 'Dobradiça')
F(it, 'Cava usinada', 'puxador cava na própria folha, 1 m por folha', 2, 'm', 'Cava usinada')
rodape(it, 55)

# ═══ 03 · QUARTO GABRIEL · roupeiro (ELEVAÇÃO E1, cotada) ═════════════════
#   195 × 270 × 65: 70 de maleiro + 100 de cabideiro + 90 de gavetas + 10.
#   Duas colunas: 3 gavetas + 1 sapateiro · 1 gaveta + 3 sapateiros.
#   ⭐ duas portas de correr no SI FORMA, uma de espelho prata [Jonathan, 06/11].
it = item('Quarto Gabriel', 'Roupeiro com portas de correr, uma de espelho', '195 × 270 × 65',
          'E1 cotada: 70 + 100 + 90 + 10 = 270 · 195 de largura · planta 65 de fundo (55 de caixa + 10 de trilho)')
P(it, 'Lateral aparente', 'a que fica para o quarto', CAIXA, 55, 1, COR15, 2.60 + 0.55)
P(it, 'Lateral de parede', '', CAIXA, 55, 1, BR15, 2.60)
P(it, 'Base e teto', '', 192, 55, 2, BR15, 1.92)
P(it, 'Divisória', 'entre as duas colunas', DIV, 53, 1, BR15, DIV / 100)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 192, DIV, 1, BR6)
fixas(it, 4, 94, 55, BR18, 'piso do maleiro e tampo das gavetas, dois por coluna · 18 mm: vão de 94')
F(it, 'Cabideiro', 'um por coluna', 2, 'un', 'Cabideiro')
gavetas(it, 4, 94, 22, 50)
gavetas(it, 4, 94, 22, 50, rotulo='Sapateiro')
correr_siforma(it, 195, CAIXA - 1)
rodape(it, 195)

# ═══ 04 · CLOSET ISABELLA · armário da porta (ELEVAÇÃO E01, cotada) ═══════
#   135 = 2,5 + 85,5 + 2,5 + 42 + 2,5 · prof. 60 na planta.
#   Coluna de 85,5: maleiro, 4 prateleiras, 2 sapateiros.
#   Coluna de 42: maleiro, cabideiro longo, 1 sapateiro.
#   "armário com 3 portas de giro".
it = item('Closet Isabella', 'Armário da parede da porta, três portas de giro', '135 × 270 × 60',
          'E01 cotada: 135 = 85,5 + 42 · 270 do piso ao teto · uma ponta na porta, a outra na parede · três folhas')
P(it, 'Lateral aparente', 'a que fica para a porta', CAIXA, 60, 1, COR15, 2.60 + 0.60)
P(it, 'Lateral de parede', '', CAIXA, 60, 1, BR15, 2.60)
P(it, 'Divisória', '', DIV, 58, 1, BR15, DIV / 100)
P(it, 'Base e teto', '', 132, 60, 2, BR15, 1.32)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 132, DIV, 1, BR6)
fixas(it, 2, 85.5, 60, BR18, 'coluna de 85,5: piso do maleiro e tampo dos sapateiros · 18 mm')
fixas(it, 2, 42, 60, BR15, 'coluna de 42: piso do maleiro e tampo do sapateiro')
prateleiras(it, 4, 85.5, 60, BR18, 'coluna de 85,5 · 18 mm')
F(it, 'Cabideiro', 'cabideiro longo na coluna de 42', 1, 'un', 'Cabideiro')
gavetas(it, 2, 85.5, 20, 55, rotulo='Sapateiro')
gavetas(it, 1, 42, 20, 55, rotulo='Sapateiro')
giro(it, 2, 44.5, FOLHA, '15 mm Palha · duas folhas na coluna de 85,5 · puxador em cava')
giro(it, 1, 45.6, FOLHA, '15 mm Palha · uma folha na coluna de 42 · puxador em cava')
rodape(it, 135)

# ═══ 04 · CLOSET ISABELLA · parede longa (ELEVAÇÃO E2, cotada) ════════════
#   281 de parede a parede · três colunas de 90,3 · prof. 58 na planta.
#   Coluna 1: maleiro, prateleira, 2 gavetas, 2 sapateiros.
#   Coluna 2: maleiro, cabideiro, 2 gavetas, 2 sapateiros.
#   Coluna 3: maleiro, cabideiro, 3 gavetas finas, 2 sapateiros.
#   "armário com 6 portas de giro".
it = item('Closet Isabella', 'Armário da parede longa, seis portas de giro', '281 × 270 × 58',
          'E2 cotada: 65 + 100 + 100 + 5 de folga · 281 de parede a parede · três colunas de 90,3 · seis folhas')
P(it, 'Lateral de parede', 'as duas pontas encostam na parede', CAIXA, 58, 2, BR15, 2.60)
P(it, 'Divisória', 'entre as colunas', DIV, 56, 2, BR15, DIV / 100)
P(it, 'Base e teto', 'emenda sobre a divisória · 281 não sai de chapa', 139, 58, 4, BR15, 1.39)
P(it, 'Fundo', 'duas peças · encaixe em rasgo', 139, DIV, 2, BR6)
fixas(it, 6, 90.3, 58, BR18, 'piso do maleiro e tampo das gavetas, dois por coluna · 18 mm')
prateleiras(it, 1, 90.3, 58, BR18, 'coluna 1 · 18 mm')
F(it, 'Cabideiro', 'colunas 2 e 3', 2, 'un', 'Cabideiro')
gavetas(it, 4, 90.3, 20, 50)
gavetas(it, 3, 90.3, 12, 50, rotulo='Gaveta fina')
gavetas(it, 6, 90.3, 20, 50, rotulo='Sapateiro')
giro(it, 6, 46.6, FOLHA, '15 mm Palha · duas folhas por coluna de 90,3 · puxador em cava')
rodape(it, 281)

# ═══ 05 · QUARTO ISABELLA · armário (QUARTO ISABELLA 01, cotada) ══════════
#   288,5 × 270 × 65 · três colunas de cerca de 92,8 · 70 + 100 + 100.
#   Coluna 1: maleiro e 3 prateleiras · coluna 2: maleiro, cabideiro e
#   4 gavetas · coluna 3: maleiro, cabideiro e 1 gaveta.
#   "armário com 3 portas de correr sendo uma com espelho prata" ·
#   "lateral fixa e recuada para cortina".
it = item('Quarto Isabella', 'Armário com três portas de correr, uma de espelho', '288,5 × 270 × 65',
          'planta 288,5 × 65 · QUARTO ISABELLA 01: 70 + 100 + 100 = 270 · três colunas · 55 de caixa + 10 de trilho')
P(it, 'Lateral aparente', 'a que fica para a porta do quarto', CAIXA, 55, 1, COR15, 2.60 + 0.55)
P(it, 'Lateral de parede', 'do lado da janela, atrás da lateral fixa', CAIXA, 55, 1, BR15, 2.60)
P(it, 'Lateral fixa recuada', '18 mm Palha · do piso ao teto, recuada para a cortina passar', 270, 50, 1, COR18, 2.70 + 0.50)
P(it, 'Divisória', 'entre as colunas', DIV, 53, 2, BR15, DIV / 100)
P(it, 'Base e teto', 'emenda sobre a divisória · 288 não sai de chapa', 143, 55, 4, BR15, 1.43)
P(it, 'Fundo', 'duas peças · encaixe em rasgo', 143, DIV, 2, BR6)
fixas(it, 5, 92.8, 55, BR18, 'piso dos três maleiros e tampo das gavetas das colunas 2 e 3 · 18 mm')
prateleiras(it, 3, 92.8, 55, BR18, 'coluna 1 · 18 mm')
F(it, 'Cabideiro', 'colunas 2 e 3', 2, 'un', 'Cabideiro')
gavetas(it, 5, 92.8, 22, 50, frente=COR15)
correr_siforma(it, 288.5, CAIXA - 1, nfolhas=3)
rodape(it, 288.5)

AMBIENTES = ['Suíte master', 'Closet suíte master', 'Quarto Gabriel', 'Closet Isabella', 'Quarto Isabella']
