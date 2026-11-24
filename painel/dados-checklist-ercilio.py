# -*- coding: utf-8 -*-
"""Dados do checklist de finalização da obra do Ercílio.

Editar aqui; o layout está em gerar-checklist-ercilio.py.
Lista relacionada pelo Jonathan por ambiente em 24/11/2026.
"""

CLIENTE  = 'Ercílio'
EMISSAO  = '24/11/2026'
NOTA_ORDEM = ('O tampo da bancada entra primeiro: ele vai ser deslocado na instalação, '
              'e só depois disso a frente da gaveta é ajustada. Fazer na ordem evita refazer.')

# (ambiente, [(item, especificação)])
AMBIENTES = [
    ('Quarto casal', [
        ('Instalar o tampo da bancada', 'tampo com caixa elétrica · haverá deslocamento do tampo'),
        ('Ajustar a frente da gaveta', 'só depois do tampo no lugar definitivo'),
        ('Reinstalar 3 corrediças ocultas de 50 cm', 'roupeiro · 3 unidades'),
        ('Instalar a porta de acesso ao banho', ''),
        ('Fitar a cabeceira', ''),
        ('Instalar fita de LED na cabeceira', 'conferir o ponto de alimentação antes'),
    ]),
    ('Banho casal', [
        ('Instalar trilhos e portas de espelho', ''),
    ]),
    ('Cozinha', [
        ('Trocar a fita de acabamento da lateral esquerda', '1 m · Branco TX · 10 cm'),
        ('Colar fórmica na testeira', ''),
    ]),
    ('Sala', [
        ('Engrossar e fitar o painel de acabamento da porta',
         'régua 5 × 2,60 m em 6 mm + fita pau-ferro brilhante 22 mm'),
        ('Colar fita no rodapé do painel da sala', 'carvalho Lir 65 mm · 30 cm bastam'),
    ]),
    ('Banho social', [
        ('Reinstalar a porta e o envelopamento', ''),
    ]),
]

# (material, para quê)
MATERIAL = [
    ('Régua 5 × 2,60 m · 6 mm', 'engrossar o painel da porta · sala'),
    ('Fita pau-ferro brilhante 22 mm', 'painel da porta · sala'),
    ('Fita carvalho Lir 65 mm · 30 cm', 'rodapé do painel · sala'),
    ('Fita Branco TX 10 cm · 1 m', 'lateral esquerda · cozinha'),
    ('Fórmica', 'testeira · cozinha'),
    ('Fita de borda da cabeceira', 'cabeceira · quarto casal'),
    ('3 corrediças ocultas de 50 cm', 'roupeiro · quarto casal'),
    ('Fita de LED', 'cabeceira · quarto casal'),
    ('Trilhos e portas de espelho', 'banho casal'),
]

LINHAS_NOVAS = 5
