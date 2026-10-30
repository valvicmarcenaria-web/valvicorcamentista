# -*- coding: utf-8 -*-
"""Apuração de ponto — outubro/2026. Douglas e Alex.

Jornada da casa: seg a qui 07:00–17:00 e sexta 07:00–16:00, com 1 h de
intervalo — 9 h de segunda a quinta, 8 h na sexta, 44 h semanais.
Salário de referência: R$ 1.621,00 · divisor 220 · adicional de 50%.
"""
SALARIO, DIVISOR, ADICIONAL = 1621.00, 220, 1.50
MES = 'outubro / 2026'

# (dia, entrada, saída, almoço, observação)   almoço None = não houve
DOUGLAS = [
 (1,'07:00','17:30','12:00-13:00',''), (2,'07:00','17:10','12:00-13:00',''),
 (5,'07:00','17:00','12:00-13:00',''), (6,'07:00','18:10','12:45-13:45',''),
 (7,'07:00','18:15','12:10-13:10',''), (8,'07:00','13:00','12:00-13:00','Saída antecipada — confirmada pela direção'),
 (9,'07:00','16:25','12:25-13:25',''), (13,'07:00','17:30','12:10-13:10',''),
 (14,'07:10','17:15','12:30-13:30','Entrada 10 min após o horário'),
 (15,'07:00','17:15','12:00-13:00',''), (16,'07:00','16:20','12:00-13:00',''),
 (19,'07:00','17:00','12:00-13:00',''), (20,'07:00','18:05','12:00-13:00',''),
 (22,'07:00','17:10','12:45-13:45',''), (23,'07:00','16:50','12:15-13:15',''),
 (26,'07:00','17:10','12:15-13:15',''), (27,'07:00','18:15','12:00-13:00',''),
 (28,'07:00','18:10','12:00-13:00',''), (29,'07:00','19:35','12:00-13:00','Jornada de 11h35'),
]
DOUGLAS_NOTA = 'A falta de 21/10 não entra nesta apuração — já foi descontada. O vale-transporte também não.'

ALEX = [
 (1,'07:00','17:00','12:00-13:00',''), (2,'07:00','17:00','12:00-13:00',''),
 (5,'07:00','18:05','12:00-13:00',''), (6,'07:00','18:43',None,'Sem intervalo'),
 (7,'07:00','17:27','12:00-13:00',''), (8,'07:00','18:36','12:00-13:00',''),
 (9,'07:00','16:00','12:00-13:00',''), (13,'07:00','19:16','12:00-13:00','Jornada de 11h16'),
 (14,'07:00','19:40','12:00-13:00','Jornada de 11h40'),
 (15,'07:00','17:11','12:00-13:00',''), (16,'07:00','17:20','12:00-13:00',''),
 (19,'07:00','19:40',None,'Sem intervalo · 12h40 de trabalho contínuo'),
 (20,'07:00','18:50',None,'Sem intervalo · há 2ª linha de 20/10 no relato, desconsiderada'),
 (21,'07:00','17:30',None,'Sem intervalo'), (22,'07:00','17:40',None,'Sem intervalo'),
 (23,'07:00','16:42','12:00-13:00',''), (26,'07:00','17:00',None,'Sem intervalo'),
 (27,'07:00','18:10','12:00-13:00',''), (28,'07:00','19:00','12:00-13:00',''),
 (29,'07:00','17:20','12:00-13:00',''),
]
ALEX_NOTA = ('O relato traz duas linhas com data 20/10 (saídas 18:50 e 18:40). Considerei uma só — '
             'é o que faz a apuração bater com o total somado pelo próprio colaborador (28,15). '
             'Confirmar a qual dia pertence a segunda linha.')

COLABORADORES = [('Douglas', DOUGLAS, DOUGLAS_NOTA), ('Alex', ALEX, ALEX_NOTA)]
