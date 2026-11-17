# Apartamento JPC — dois banhos

**Projeto:** Helena Antunes Arquitetura e Interiores · (31) 99111-8890
**Pranchas:** PR 01 · Banho Suíte e Banho Social · junho de 2026
**Pedido [Jonathan, 17/11/2026]:** *"Faça esse orçamento em uma página. Bonito e
organizado / Prazo de entrega 60 dias / Pagamento 50% + 50% / Ferragens Hettich
/ Preço de venda - R$ 6.700"*

**Entregue:** `projetos/jpc/` — `base.py`, `levantamento.py`, `cenarios.py`,
`proposta.py` → `Apartamento JPC · Proposta Valvic.pdf`, uma folha A4.

---

## O que foi lido das pranchas

| | Banho Suíte | Banho Social |
|---|---|---|
| gabinete | 67,5 × 63 × **49,5** | 88,5 × 63 × **45 ⚠** |
| frentes | 2 portas de 33,75 | 3 colunas de 29,5: 2 portas + 3 gavetas 15 / 15 / 33 |
| interno | 1 prateleira (tracejada) | nenhuma desenhada |
| suspenso | 20 cm do piso (vista lateral) | suspenso, sem cota |
| bancada de pedra | 69,5 × 55, cuba oval | 90,5 × 50,5, cuba oval |

⭐ **O nicho do papel higiênico é o único detalhe escrito à mão nas duas
folhas:** *"Porta papel higiênico recuado na marcenaria (profundidade 15 cm)"*.
A vista lateral cota a boca em **25 × 18**. É um caixote de cinco peças aberto
na lateral direita do gabinete da suíte, e é por isso que a prateleira de lá
morre antes do fim — ela não atravessa o vazio.

⚠ **A profundidade do Social não está cotada** — aquela folha não tem vista
lateral. Adotei **45**, que é a bancada de 50,5 com o mesmo recuo de 5,5 que a
suíte tem (55 → 49,5). A largura confirma a leitura: lá a bancada é 69,5 e o
gabinete 67,5; aqui 90,5 e 88,5 — os mesmos 2 cm nas duas folhas. Está na lista
"a conferir na medição" da proposta.

---

## A fronteira do escopo — regra 19

⛔ **A bancada de pedra e a cuba ficam fora**, nas duas folhas. Desenhadas,
hachuradas como granito, e não são marcenaria. Nem a zero.

⛔ **O espelho também fica fora, e esta foi a decisão difícil.** Ele está
desenhado, o CONTEÚDO da prancha diz MARCENARIA, e a regra manda incluir espelho
*"quando faz parte do móvel"*. **Este não faz:** está colado na parede acima da
bancada, não encosta no gabinete e existe sem ele — exatamente como a pedra. E
⚠ **não tem uma cota em nenhuma das duas folhas**: orçá-lo seria inventar a
medida. Vai NOMEADO na proposta, que é o segundo dos dois únicos estados que a
regra 19 admite. Se o Jonathan quiser incluir, é aditivo com medida conferida.

⭐ Na folha isso virou desenho: as duas elevações mostram a bancada de pedra
como uma tarja cinza escrita **"BANCADA DE PEDRA · FORA DO ESCOPO"**. O cliente
vê onde o nosso escopo começa, em vez de ler.

---

## O custo e a margem

| | |
|---|--:|
| chapa · 1 × 6 mm, 2 × 15 mm, 1 × 18 mm | R$ 2.150,00 |
| fita de borda · 26,21 m | R$ 86,49 |
| corte · 4 chapas, 35 peças | R$ 95,50 |
| consumíveis 6% | R$ 134,19 |
| **ferragem Hettich** · 8 Sensys, 3 pares Quadro V6, 2 suportes | R$ 863,00 |
| usinagem de cava · 2,15 m | R$ 107,50 |
| frete · 2 viagens | R$ 400,00 |
| embalagem 2% | R$ 68,73 |
| **CUSTO DIRETO** | **R$ 3.905,42** |

Rateio dos R$ 6.700 pelo custo direto: **Suíte R$ 2.507,33 · Social R$ 4.192,67**.

### ⛔⛔ A MC lida é 17,80% — metade do piso da casa

Com preço e linha cravados, a MC é **lida**, não escolhida:
`MC = BASE − custo ÷ preço` = 0,760875 − 3.905,42 ÷ 6.700 = **17,80%**.
A faixa ideal da casa é 35% a 40%. **O preço a 35% seria R$ 9.505.**

⭐⭐ **E a causa não é o preço, é o tamanho do job.** Dois móveis compram
**4 chapas inteiras** para usar 7,13 m² de peça:

| cenário | chapa | custo direto | MC a R$ 6.700 |
|---|--:|--:|--:|
| como a casa compra · chapa inteira | R$ 2.150,00 | R$ 3.905,42 | **17,8%** |
| se a sobra for usada · chapa fracionada | R$ 938,79 | R$ 2.591,26 | **37,4%** |

A sobra do arredondamento, com consumível e embalagem, é **R$ 1.314,15 — 33,6%
do custo direto inteiro**. ⭐ Ou seja: **R$ 6.700 é preço saudável se os dois
gabinetes correrem junto com outro job na mesma cor** (37,4%, dentro da faixa).
Sozinhos, como único job daquela chapa, são 17,8%. `cenarios.py` roda os dois.

### ⚠ O RT de 10% é leitura minha, não ordem

O Jonathan não falou de RT desta vez. O projeto é da Helena Antunes, detalhado
prancha a prancha, e no outro job dela a casa pagou RT [*"vamos considerar RT"*,
30/09/2026]. A regra é "RT 10% quando há parceiro indicando". **Sem RT a MC sobe
para 26,59%** — o RT custa **R$ 588,76** neste job. Orçar com e não pagar sobra
margem; orçar sem e ter de pagar tira um quinto da margem, e por isso errei para
o lado que não quebra.

---

## Dúvidas abertas

1. ⭐ **O espelho dos dois banhos é nosso?** Está fora por regra 19 e por falta
   de cota. Se for para incluir, preciso das medidas.
2. ⚠ **Profundidade do Banho Social** — adotei 45, a prancha não cota.
3. ⚠ **Padrão e cor do MDF** — nenhuma das folhas especifica. O preço vale para
   cor ou amadeirado de catálogo; especial (sincronizado, alto-relevo, super
   matte) é a linha de R$ 1.000 da Base e muda o custo. Roda com `ESPECIAL=1`.
4. ⚠ **MDF resistente à umidade** — gabinete de banheiro embaixo de cuba. A Base
   da casa não tem a linha, e o orçado é MDF comum.
5. ⚠ **Prateleiras internas do Social** — o desenho não mostra nenhuma. Segui o
   desenho e ofereci sem acréscimo na folha.
6. ⚠ **RT** — ver acima.
