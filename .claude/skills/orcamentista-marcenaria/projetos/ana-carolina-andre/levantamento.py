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

Premissas minhas (vão como dúvida numerada na planilha):
  · acabamento sem nota → Melamínico de cor (chave "MDF cor") no que se vê;
    Branco TX dentro dos roupeiros com porta;
  · roupeiros de 65 de profundidade (suíte e Gabriel) → PORTAS DE CORRER
    (Dominus, o sistema da casa); closets (suíte master e Isabella) → ABERTOS;
  · "sapateiro"/"sapateira" = gaveta baixa com corrediça (uma corrediça cada);
  · rodapé de 10 recuado em MDF de cor + perfil de proteção de piso.

Cada peça: (peça, observação, C, L, QTD, chave da Base, fita em m por peça, tipo
de fita) · ferragem: (peça, observação, QTD, UN, chave).
"""
ITENS = []      # (amb, nn, móvel, medida, cadeia, pecas, ferragens)

def item(amb, movel, medida, cadeia):
    d = dict(amb=amb, movel=movel, medida=medida, cadeia=cadeia, pecas=[], ferr=[])
    ITENS.append(d); return d

def P(it, nome, obs, c, l, qtd, chave, fita=0.0, tipo=None):
    tipo = tipo or ('Fita Branco TX' if 'Branco' in chave else 'Fita cor')
    it['pecas'].append((nome, obs, c, l, qtd, chave, fita, tipo))

def F(it, nome, obs, qtd, un, chave):
    it['ferr'].append((nome, obs, qtd, un, chave))

COR15, COR18, COR6 = 'MDF cor 15', 'MDF cor 18', 'MDF cor 6'
BR15, BR6 = 'MDF Branco TX 15', 'MDF Branco TX 6'

def gavetas(it, n, larg, alt, prof, frente=COR15, rotulo='Gaveta'):
    li = larg - 6.6
    P(it, f'{rotulo} · frente', '', larg, alt, n, frente, 2 * (larg + alt) / 100)
    P(it, f'{rotulo} · lateral da caixa', '', prof - 5, alt - 5, 2 * n, BR15, (prof - 5) / 100)
    P(it, f'{rotulo} · frente e traseira da caixa', '', li, alt - 5, 2 * n, BR15, li / 100)
    P(it, f'{rotulo} · fundo da caixa', 'encaixe em rasgo, sem fita', li + 1, prof - 6, n, BR6)
    F(it, 'Corrediça Blum', f'uma por {rotulo.lower()}', n, 'gaveta', 'Corrediça')

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

def correr2(it, larg_vao, alt, cor=COR18):
    folha = round(larg_vao / 2 + 3, 1)
    P(it, 'Porta de correr', '18 mm · duas folhas com transpasse', alt, folha, 2, cor, 2 * (alt + folha) / 100)
    F(it, 'Sistema de correr Dominus', 'flutuante, trilho oculto, duplo amortecimento · duas portas', 1, 'cj',
      'Sistema de correr Dominus')
    F(it, 'Trilho Dominus 2 m', 'superior e inferior do sistema', 1, 'un', 'Trilho Dominus 2 m')
    F(it, 'Desempenador de porta', 'dois por folha de 70 cm ou mais', 4 if folha >= 70 else 2, 'un',
      'Desempenador de porta')
    F(it, 'Cava usinada', 'puxador cava vertical na própria folha, 1 m por folha', 2, 'm', 'Cava usinada')

# ═══ 01 · SUÍTE MASTER · roupeiro da parede esquerda (SUITE MASTER_E1) ═════
#   planta: 200 × 65 · elevação: 270 do piso (260 de caixa + 10 de rodapé),
#   dois módulos de 95: cabideiro longo com gaveta baixa · sete nichos.
it = item('Suíte master', 'Roupeiro com portas de correr', '200 × 270 × 65',
          'planta 200 × 65 · altura medida na E1: 260 de caixa + 10 de rodapé · módulos 95 + 95')
P(it, 'Lateral aparente', 'a que fica para o quarto', 260, 55, 1, COR15, 2.60 + 0.55)
P(it, 'Lateral de parede', '', 260, 55, 1, BR15, 2.60)
P(it, 'Base e teto', '', 197, 55, 2, BR15, 1.97)
P(it, 'Divisória', 'entre os dois módulos', 257, 53, 1, BR15, 2.57)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 197, 257, 1, BR6)
prateleiras(it, 6, 95, 55, 'MDF Branco TX 18', 'vão de 95 · módulo dos nichos · 18 mm: passa dos 70')
P(it, 'Prateleira sobre a gaveta', 'fecha o cabideiro longo · 18 mm', 94.6, 52, 1, 'MDF Branco TX 18', 0.95)
F(it, 'Cabideiro', 'cabideiro longo', 1, 'un', 'Cabideiro')
gavetas(it, 1, 95, 15, 50, frente=BR15, rotulo='Gaveta baixa')
correr2(it, 200, 258)
rodape(it, 200)

# ═══ 02 · CLOSET SUÍTE MASTER · parede longa (CLOSET SUITE MASTER_E1) ══════
#   planta: 331 × 61 · quatro módulos de 80 · 265 do piso (255 + 10) · aberto.
#   ⭐ "até 10 gavetas/sapateiras": 3 sapateiras no módulo 1, 4 gavetas no
#   módulo 3 (a prancha desenha 3) e 3 sapateiras no módulo A da E2 = 10.
it = item('Closet suíte master', 'Armário aberto da parede longa', '331 × 265 × 61',
          'planta 331 × 61 · quatro módulos de 80 medidos na E1 · 255 de caixa + 10 de rodapé')
P(it, 'Lateral', 'as duas pontas', 255, 61, 2, COR15, 2.55 + 0.61)
P(it, 'Divisória', 'entre os módulos', 252, 59, 3, COR15, 2.52)
P(it, 'Base e teto', 'emenda sobre a divisória do meio · 331 não sai de chapa', 164, 61, 4, COR15, 1.64)
P(it, 'Fundo', 'à vista: closet aberto · encaixe em rasgo', 165, 252, 2, COR6)
prateleiras(it, 4, 80, 61, COR18, 'módulo 1 · 18 mm: vão de 80 passa dos 70')
gavetas(it, 3, 80, 18, 55, rotulo='Sapateira')
P(it, 'Prateleira baixa do cabideiro', 'módulo 2', 79.6, 58, 1, COR18, 0.80)
F(it, 'Cabideiro', 'módulos 2 e 4, cabideiro longo', 2, 'un', 'Cabideiro')
prateleiras(it, 5, 80, 61, COR18, 'módulo 3, acima das gavetas')
gavetas(it, 4, 80, 18, 55)
rodape(it, 331)

# ═══ 03 · CLOSET SUÍTE MASTER · parede da porta (CLOSET SUITE MASTER_E2) ═══
#   planta: 185 (dois módulos de 89) + porta + 55 · prof. 60 · aberto.
it = item('Closet suíte master', 'Armários abertos da parede da porta', '185 + 55 × 265 × 60',
          'planta 55 + 91 (porta) + 185 = 331 · prof. 60 · módulos de 89 medidos na E2')
P(it, 'Lateral', 'bloco de 185, as duas pontas', 255, 60, 2, COR15, 2.55 + 0.60)
P(it, 'Divisória', 'bloco de 185', 252, 58, 1, COR15, 2.52)
P(it, 'Base e teto', 'bloco de 185', 182, 60, 2, COR15, 1.82)
P(it, 'Fundo', 'bloco de 185 · à vista', 182, 252, 1, COR6)
prateleiras(it, 4, 89, 60, COR18, 'módulo A · 18 mm')
gavetas(it, 3, 89, 18, 55, rotulo='Sapateira')
P(it, 'Prateleira baixa do cabideiro', 'módulo B', 88.6, 57, 1, COR18, 0.89)
F(it, 'Cabideiro', 'módulo B, cabideiro longo', 1, 'un', 'Cabideiro')
P(it, 'Lateral', 'módulo de 55, as duas pontas', 255, 60, 2, COR15, 2.55 + 0.60)
P(it, 'Base e teto', 'módulo de 55', 52, 60, 2, COR15, 0.52)
P(it, 'Fundo', 'módulo de 55 · à vista', 52, 252, 1, COR6)
prateleiras(it, 6, 52, 60, COR15, 'módulo de 55')
rodape(it, 185); rodape(it, 55)

# ═══ 04 · QUARTO GABRIEL · roupeiro (ELEVAÇÃO E1, cotada) ═════════════════
#   195 × 270 × 65: 5 de folga + 65 maleiro + 100 cabideiro + 90 gavetas + 10.
#   Duas colunas: 3 gavetas + 1 sapateiro · 1 gaveta + 3 sapateiros.
it = item('Quarto Gabriel', 'Roupeiro com portas de correr', '195 × 265 × 65',
          'E1 cotada: 5 + 65 + 100 + 90 + 10 = 270 · 195 de largura · planta 65 de profundidade')
P(it, 'Lateral aparente', 'a que fica para o quarto', 255, 55, 1, COR15, 2.55 + 0.55)
P(it, 'Lateral de parede', '', 255, 55, 1, BR15, 2.55)
P(it, 'Base e teto', '', 192, 55, 2, BR15, 1.92)
P(it, 'Divisória', 'entre as duas colunas', 252, 53, 1, BR15, 2.52)
P(it, 'Fundo', 'encaixe em rasgo, sem fita', 192, 252, 1, BR6)
prateleiras(it, 4, 94, 55, 'MDF Branco TX 18', 'maleiro e topo das gavetas, duas por coluna · 18 mm: vão de 94')
F(it, 'Cabideiro', 'um por coluna', 2, 'un', 'Cabideiro')
gavetas(it, 4, 94, 22, 50, frente=BR15)
gavetas(it, 4, 94, 22, 50, frente=BR15, rotulo='Sapateiro')
correr2(it, 195, 253)
rodape(it, 195)

# ═══ 05 · CLOSET ISABELLA · armário da porta (ELEVAÇÃO E01) ═══════════════
#   planta 135 × 55 · duas colunas: maleiro 65, cabideiro longo, sapateiro.
it = item('Closet Isabella', 'Armário aberto da parede da porta', '135 × 268 × 55',
          'planta 135 × 55 · E01: 2 + 65 + 202,5 · duas colunas')
P(it, 'Lateral', 'as duas pontas', 258, 55, 2, COR15, 2.58 + 0.55)
P(it, 'Divisória', '', 255, 53, 1, COR15, 2.55)
P(it, 'Base e teto', '', 132, 55, 2, COR15, 1.32)
P(it, 'Fundo', 'à vista: closet aberto', 132, 255, 1, COR6)
prateleiras(it, 2, 65, 55, COR15, 'maleiro, um por coluna')
F(it, 'Cabideiro', 'cabideiro longo, um por coluna', 2, 'un', 'Cabideiro')
gavetas(it, 2, 65, 20, 45, rotulo='Sapateiro')
rodape(it, 135)

# ═══ 06 · CLOSET ISABELLA · parede longa (ELEVAÇÃO E2) ════════════════════
#   planta 281 × 55 · quatro colunas de 70 · 255 + 10 · prateleiras, maleiros,
#   cabideiros e 12 gavetas e sapateiros (2+2 · 2+2 · 3+1 · nenhum).
it = item('Closet Isabella', 'Armário aberto da parede longa', '281 × 265 × 55',
          'planta 281 × 55 · E2: 170 + 100 = 270 · quatro colunas de 70 medidas na escala')
P(it, 'Lateral', 'as duas pontas', 255, 55, 2, COR15, 2.55 + 0.55)
P(it, 'Divisória', 'entre as colunas', 252, 53, 3, COR15, 2.52)
P(it, 'Base e teto', 'emenda sobre a divisória do meio · 281 não sai de chapa', 139, 55, 4, COR15, 1.39)
P(it, 'Fundo', 'à vista · duas peças', 139, 252, 2, COR6)
prateleiras(it, 10, 70, 55, COR15, 'coluna 1: três e o topo das gavetas · colunas 2 a 4: maleiro e meio')
F(it, 'Cabideiro', 'colunas 2 e 3, e dois na coluna 4', 4, 'un', 'Cabideiro')
gavetas(it, 7, 70, 22, 45)
gavetas(it, 5, 70, 22, 45, rotulo='Sapateiro')
rodape(it, 281)

AMBIENTES = ['Suíte master', 'Closet suíte master', 'Quarto Gabriel', 'Closet Isabella']
