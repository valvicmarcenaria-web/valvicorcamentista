# -*- coding: utf-8 -*-
"""CENTURION MOTORS — Showroom Vila da Serra · projeto CLS Arquitetas  [26/11/2026]

⭐ [Jonathan, 26/11/2026] "vamos montar com esse cenario": preço fechado por item, total R$ 295.500.
   Custo de material R$ 86.383 (29,2%) · impostos e comissões R$ 55.628 (18,8%) · margem R$ 153.490 — MC 51,9%.
⛔ Custo e MC ficam aqui, NUNCA na proposta.
"""
# (item, descrição sem medida, preço, custo)
VALORES = [
    ('Forro amadeirado', 'Em MDF amadeirado, sobre o salão e a área de convivência.', 92000, 27000),
    ('Nichos e pórticos', 'Pórticos curvos laqueados café, nichos com fundo amadeirado, prateleiras com alma de aço e luz embutida, e os arcos de acesso.', 110000, 35608),
    ('Painéis de parede', 'Revestimento das paredes em MDF amadeirado, no lugar do adesivo indicado no projeto.', 59000, 13000),
    ('Painéis para colagem do espelho', 'A base em MDF que recebe os espelhos, alinhada aos painéis vizinhos.', 9500, 1321),
    ('Espelhos', 'Espelho prata colado sobre os painéis, com transporte e instalação.', 25000, 9454),
]
TOTAL = sum(v for _, _, v, _ in VALORES)
CUSTO = sum(c for *_, c in VALORES)
assert TOTAL == 295500 and CUSTO == 86383
