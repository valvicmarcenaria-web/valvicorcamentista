# -*- coding: utf-8 -*-
"""ANA CAROLINA E ANDRÉ · Apto Funcionários, Ed. La Concordia, Rua Inconfidentes
307, apto 21, BH · projeto [35] de Ana Maria (Archicad, r00, 03/11/2026,
"estudo enviado para análise").

Três pranchas: 35_.1_SUITE_MASTER (A2) · 35_.1_QUARTO_GABRIEL (A3) ·
35_.1_CLOSET_ISABELLA (A2). ⛔ As elevações NÃO TÊM COTA nem NOTA DE MATERIAL:
larguras e profundidades vêm da planta (cotada), alturas e divisões internas
foram MEDIDAS NA ESCALA 1:25 (3,15 px/cm no PNG de 200 dpi).

Decisões [Jonathan, 05/11/2026]: ferragem BLUM · RT 10% · "no closet da suíte
master, considere até 10 gavetas/sapateiras".
Decisões [Jonathan, 06/11/2026]: "não tem roupeiro na suíte master, apenas o
closet" · roupeiro do Gabriel com DUAS PORTAS DE CORRER, uma delas de ESPELHO
PRATA, sistema deslizante SI FORMA · "os demais serão PORTAS DE GIRO com
puxador em cava" (closet da suíte master e closet da Isabella).
Decisões [Jonathan, 06/11/2026, na proposta]: corrediça Blum TANDEM com
BLUMOTION · dobradiça Blum CLIP top BLUMOTION · sistema de correr SI Ocean 80
da Siforma (o preço segue o "Sistema deslizante SI Forma" da Base, R$ 1.200).

Premissas minhas (vão como dúvida numerada na planilha):
  · TODO o MDF no Palha da Duratex [Jonathan, 06/11/2026] — nem o miolo
    fica em Branco TX; a fita é a de cor (R$ 3,00);
  · porta de giro em 15 mm (a espessura de porta da Base); módulo acima de 60
    leva DUAS folhas (roupeiros.md §8: módulo de 86 = 2 × 43); dobradiça Blum
    pela altura — acima de 200, cinco por folha; cava usinada de 1 m por folha;
  · folha de espelho que corre = "Porta de espelho em alumínio" da Base (folha
    pronta, sem chapa, sem fita, sem desempenador), como na Tereza Sá;
  · "sapateiro"/"sapateira" = gaveta baixa com corrediça (uma corrediça cada);
  · rodapé de 10 recuado em MDF de cor + perfil de proteção de piso.

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
    it['pecas'].append((nome, obs, c, l, qtd, chave, fita, tipo))

def F(it, nome, obs, qtd, un, chave):
    it['ferr'].append((nome, obs, qtd, un, chave))

def T(it, nome, obs, c, l, qtd, chave):
    """Terceirizado por m² (folha pronta): não entra no plano de corte."""
    it['terc'].append((nome, obs, c, l, qtd, 'm²', chave))

# ⭐ "TODOS OS MDFs SERÃO NO PADRÃO NUDE VEL GUARARAPES" [Jonathan, 06/11/2026],
#   e no mesmo dia: "será o PALHA DA DURATEX". Portas, caixaria, prateleiras,
#   fundos e caixas de gaveta. Chave própria do projeto na Base (importada),
#   preço da linha Melamínico Fosco — ⚠ confirmar o preço do Palha Duratex.
PALHA15, PALHA18, PALHA6 = 'MDF Palha 15', 'MDF Palha 18', 'MDF Palha 6'
COR15, COR18, COR6 = PALHA15, PALHA18, PALHA6
BR15, BR18, BR6 = PALHA15, PALHA18, PALHA6   # o miolo também é Palha

def gavetas(it, n, larg, alt, prof, frente=COR15, rotulo='Gaveta'):
    li = larg - 6.6
    P(it, f'{rotulo} · frente', '', larg, alt, n, frente, 2 * (larg + alt) / 100)
    P(it, f'{rotulo} · lateral da caixa', '', prof - 5, alt - 5, 2 * n, BR15, (prof - 5) / 100)
    P(it, f'{rotulo} · frente e traseira da caixa', '', li, alt - 5, 2 * n, BR15, li / 100)
    P(it, f'{rotulo} · fundo da caixa', 'encaixe em rasgo, sem fita', li + 1, prof - 6, n, BR6)
    F(it, 'Corrediça Blum TANDEM', f'oculta, com BLUMOTION · uma por {rotulo.lower()}', n, 'gaveta', 'Corrediça')

def prateleiras(it, n, vao, prof, chave, obs=''):
    P(it, 'Prateleira', obs or f'vão de {vao}', vao - 0.4, prof - 3, n, chave, vao / 100)
    F(it, 'Suporte de prateleira', 'jogo de 4 por prateleira interna', n, 'jogo', 'Suporte de prateleira')

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

def correr_siforma(it, larg_vao, alt):
    """Duas portas de correr no SI Forma, uma de MDF e uma de espelho prata [Jonathan, 06/11/2026]."""
    folha = round(larg_vao / 2 + 3, 1)
    P(it, 'Porta de correr', '18 mm · a folha de MDF, com transpasse', alt, folha, 1, COR18, 2 * (alt + folha) / 100)
    T(it, 'Porta de correr de espelho prata', 'folha pronta: esquadria de alumínio + espelho prata · sem chapa e sem fita',
      alt, folha, 1, 'Porta de espelho em alumínio')
    F(it, 'Sistema deslizante SI Ocean 80', 'Siforma · amortecimento nos dois sentidos · um conjunto para as duas folhas', 1, 'cj', 'Sistema deslizante SI Forma')
    F(it, 'Desempenador de porta', 'só na folha de MDF · dois por folha de 70 cm ou mais', 2 if folha >= 70 else 1, 'un',
      'Desempenador de porta')
    F(it, 'Cava usinada', 'puxador cava vertical na folha de MDF, 1 m', 1, 'm', 'Cava usinada')

# ⛔ SUÍTE MASTER: "não tem roupeiro na suíte master, apenas o closet"
#   [Jonathan, 06/11/2026] — o roupeiro de 200 da E1 saiu do orçamento.

# ═══ 01 · CLOSET SUÍTE MASTER · parede longa (CLOSET SUITE MASTER_E1) ══════
#   planta: 331 × 61 · quatro módulos de 80 · 265 do piso (255 + 10).
#   ⭐ "até 10 gavetas/sapateiras": 3 sapateiras no módulo 1, 4 gavetas no
#   módulo 3 (a prancha desenha 3) e 3 sapateiras no módulo A da E2 = 10.
#   ⭐ portas de giro: duas folhas por módulo de 80 = oito folhas de 41.
it = item('Closet suíte master', 'Armário da parede longa, portas de giro', '331 × 265 × 61',
          'planta 331 × 61 · quatro módulos de 80 medidos na E1 · 255 de caixa + 10 de rodapé · duas folhas por módulo')
P(it, 'Lateral de ponta', 'as duas pontas, para fora', 255, 61, 2, COR15, 2.55 + 0.61)
P(it, 'Divisória', 'entre os módulos', 252, 59, 3, BR15, 2.52)
P(it, 'Base e teto', 'emenda sobre a divisória do meio · 331 não sai de chapa', 164, 61, 4, BR15, 1.64)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 165, 252, 2, BR6)
prateleiras(it, 4, 80, 61, BR18, 'módulo 1 · 18 mm: vão de 80 passa dos 70')
gavetas(it, 3, 80, 18, 55, frente=BR15, rotulo='Sapateira')
P(it, 'Prateleira baixa do cabideiro', 'módulo 2 · 18 mm', 79.6, 58, 1, BR18, 0.80)
F(it, 'Cabideiro', 'módulos 2 e 4, cabideiro longo', 2, 'un', 'Cabideiro')
prateleiras(it, 5, 80, 61, BR18, 'módulo 3, acima das gavetas · 18 mm')
gavetas(it, 4, 80, 18, 55, frente=BR15)
giro(it, 8, 41.1, 254.5, '15 mm · duas folhas por módulo de 80 · puxador em cava')
rodape(it, 331)

# ═══ 01 · CLOSET SUÍTE MASTER · parede da porta (CLOSET SUITE MASTER_E2) ═══
#   planta: 185 (dois módulos de 89) + porta + 55 · prof. 60.
#   ⭐ portas de giro: duas folhas por módulo de 89, uma no módulo de 55.
it = item('Closet suíte master', 'Armários da parede da porta, portas de giro', '185 + 55 × 265 × 60',
          'planta 55 + 91 (porta) + 185 = 331 · prof. 60 · módulos de 89 medidos na E2 · cinco folhas')
P(it, 'Lateral de ponta', 'bloco de 185, as duas pontas', 255, 60, 2, COR15, 2.55 + 0.60)
P(it, 'Divisória', 'bloco de 185', 252, 58, 1, BR15, 2.52)
P(it, 'Base e teto', 'bloco de 185', 182, 60, 2, BR15, 1.82)
P(it, 'Fundo', 'bloco de 185 · encaixe em rasgo', 182, 252, 1, BR6)
prateleiras(it, 4, 89, 60, BR18, 'módulo A · 18 mm')
gavetas(it, 3, 89, 18, 55, frente=BR15, rotulo='Sapateira')
P(it, 'Prateleira baixa do cabideiro', 'módulo B · 18 mm', 88.6, 57, 1, BR18, 0.89)
F(it, 'Cabideiro', 'módulo B, cabideiro longo', 1, 'un', 'Cabideiro')
P(it, 'Lateral de ponta', 'módulo de 55, as duas pontas', 255, 60, 2, COR15, 2.55 + 0.60)
P(it, 'Base e teto', 'módulo de 55', 52, 60, 2, BR15, 0.52)
P(it, 'Fundo', 'módulo de 55 · encaixe em rasgo', 52, 252, 1, BR6)
prateleiras(it, 6, 52, 60, BR15, 'módulo de 55')
giro(it, 4, 46.0, 254.5, '15 mm · bloco de 185, duas folhas por módulo de 89 · puxador em cava')
giro(it, 1, 54.7, 254.5, '15 mm · módulo de 55, uma folha · puxador em cava')
rodape(it, 185); rodape(it, 55)

# ═══ 02 · QUARTO GABRIEL · roupeiro (ELEVAÇÃO E1, cotada) ═════════════════
#   195 × 270 × 65: 5 de folga + 65 maleiro + 100 cabideiro + 90 gavetas + 10.
#   Duas colunas: 3 gavetas + 1 sapateiro · 1 gaveta + 3 sapateiros.
#   ⭐ duas portas de correr no SI FORMA, uma de espelho prata [Jonathan, 06/11].
it = item('Quarto Gabriel', 'Roupeiro com portas de correr, uma de espelho', '195 × 265 × 65',
          'E1 cotada: 5 + 65 + 100 + 90 + 10 = 270 · 195 de largura · planta 65 de profundidade')
P(it, 'Lateral aparente', 'a que fica para o quarto', 255, 55, 1, COR15, 2.55 + 0.55)
P(it, 'Lateral de parede', '', 255, 55, 1, BR15, 2.55)
P(it, 'Base e teto', '', 192, 55, 2, BR15, 1.92)
P(it, 'Divisória', 'entre as duas colunas', 252, 53, 1, BR15, 2.52)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 192, 252, 1, BR6)
prateleiras(it, 4, 94, 55, BR18, 'maleiro e topo das gavetas, duas por coluna · 18 mm: vão de 94')
F(it, 'Cabideiro', 'um por coluna', 2, 'un', 'Cabideiro')
gavetas(it, 4, 94, 22, 50, frente=BR15)
gavetas(it, 4, 94, 22, 50, frente=BR15, rotulo='Sapateiro')
correr_siforma(it, 195, 253)
rodape(it, 195)

# ═══ 03 · CLOSET ISABELLA · armário da porta (ELEVAÇÃO E01) ═══════════════
#   planta 135 × 55 · duas colunas: maleiro 65, cabideiro longo, sapateiro.
#   ⭐ portas de giro: coluna de 65 passa dos 60 → duas folhas por coluna.
it = item('Closet Isabella', 'Armário da parede da porta, portas de giro', '135 × 268 × 55',
          'planta 135 × 55 · E01: 2 + 65 + 202,5 · duas colunas · quatro folhas')
P(it, 'Lateral de ponta', 'as duas pontas', 258, 55, 2, COR15, 2.58 + 0.55)
P(it, 'Divisória', '', 255, 53, 1, BR15, 2.55)
P(it, 'Base e teto', '', 132, 55, 2, BR15, 1.32)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 132, 255, 1, BR6)
prateleiras(it, 2, 65, 55, BR15, 'maleiro, um por coluna')
F(it, 'Cabideiro', 'cabideiro longo, um por coluna', 2, 'un', 'Cabideiro')
gavetas(it, 2, 65, 20, 45, frente=BR15, rotulo='Sapateiro')
giro(it, 4, 33.4, 257.5, '15 mm · duas folhas por coluna de 65 · puxador em cava')
rodape(it, 135)

# ═══ 03 · CLOSET ISABELLA · parede longa (ELEVAÇÃO E2) ════════════════════
#   planta 281 × 55 · quatro colunas de 70 · 255 + 10 · prateleiras, maleiros,
#   cabideiros e 12 gavetas e sapateiros (2+2 · 2+2 · 3+1 · nenhum).
#   ⭐ portas de giro: duas folhas por coluna de 70 = oito folhas de 35.
it = item('Closet Isabella', 'Armário da parede longa, portas de giro', '281 × 265 × 55',
          'planta 281 × 55 · E2: 170 + 100 = 270 · quatro colunas de 70 medidas na escala · oito folhas')
P(it, 'Lateral de ponta', 'as duas pontas', 255, 55, 2, COR15, 2.55 + 0.55)
P(it, 'Divisória', 'entre as colunas', 252, 53, 3, BR15, 2.52)
P(it, 'Base e teto', 'emenda sobre a divisória do meio · 281 não sai de chapa', 139, 55, 4, BR15, 1.39)
P(it, 'Fundo', 'duas peças · encaixe em rasgo', 139, 252, 2, BR6)
prateleiras(it, 10, 70, 55, BR15, 'coluna 1: três e o topo das gavetas · colunas 2 a 4: maleiro e meio')
F(it, 'Cabideiro', 'colunas 2 e 3, e dois na coluna 4', 4, 'un', 'Cabideiro')
gavetas(it, 7, 70, 22, 45, frente=BR15)
gavetas(it, 5, 70, 22, 45, frente=BR15, rotulo='Sapateiro')
giro(it, 8, 34.8, 254.5, '15 mm · duas folhas por coluna de 70 · puxador em cava')
rodape(it, 281)

AMBIENTES = ['Closet suíte master', 'Quarto Gabriel', 'Closet Isabella']
