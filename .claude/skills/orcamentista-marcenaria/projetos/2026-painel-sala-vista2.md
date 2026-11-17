# Painel da Sala — VISTA 2 · ripado, nicho de pedra e portas mimetizadas

**Pranchas:** `SALA - VISTA 2` (1/50) e `NICHO RIPADO` (1/30, pág. 18) · três
vistas mais detalhe 1/5 · renders do living e da sala de jantar.
**Pedido [Jonathan, 17/11/2026]:** *"O ripado vai só até onde termina a pedra,
o nicho de pedra. Do nicho de pedra para a direita, o painel vai ser liso com as
duas portas mimetizadas, mas não vai ser ripado. Considere o projeto, a
quantidade de ripas, filetagem, tudo conforme o nosso padrão de cotação. E faça
o levantamento dos custos e me apresente em formato de tabela antes de gerar a
proposta."*

**Entregue:** `projetos/painel-sala/` — `base.py`, `levantamento.py`,
`cenarios.py`. ⚠ **A proposta ainda não foi gerada**, como ele pediu.

---

## A geometria, lida das pranchas

Painel corrido de **682 × 277**, sobre sóculo de pedra de 15 (292 no total),
num volume de **50 de profundidade** (vista lateral e perspectiva, 1/30).

```
0 ──── 50 ─────────────────── 352 ── 366 ─ 449 ──── 592 ─ 662 ─ 682
│ porta │   nicho de pedra 302  │  ←──── PAINEL LISO 330 ───────→
│ ripada│   75 ripado em cima   │      porta 83    porta 70
│ 50×277│  131 de pedra         │      × 210       × 210
│       │   71 ripado embaixo   │
└──────── RIPADO 352 ──────────┘
```

Alturas, da vista lateral: **75 | 4 | 123 | 4 | 71 | 15 = 292**. O `4+123+4=131`
é o *"NICHO 131X302CM EM MÁRMORE TRAVERTINO ROMANO ESTUCADO"*.

### ⭐⭐ A trama deste projeto NÃO é a da casa

A prancha crava *"RIPADO EM MDF GIANDUIA TRAMA DE 20MM E ESPAÇAMENTO DE 20MM"*
e o detalhe 1/5 confirma com a cota `2 · 2 · 2`. **Passo de 4 cm**, contra os
6 cm do padrão da casa (ripa 4, vão 2):

| | este projeto (20/20) | padrão da casa (40/20) | a mais |
|---|--:|--:|--:|
| ripas | 162 | 108 | **+54** |
| metros de filete | 285,5 | 190,3 | **+95,2** |
| custo da filetagem | R$ 713,70 | R$ 475,80 | **+R$ 237,90** |

⛔ Quem copiar o passo da casa erra o orçamento para baixo.

### ⛔ E o vão tem 2 cm de profundidade

Enxerga-se o fundo entre as ripas. O substrato sai **no mesmo Gianduia**, não em
branco nem em cru. ⭐ E em **18 mm, não 15**: em 15 os 4,41 m² de substrato
compravam duas chapas só para si (R$ 1.100) e sobravam 3,7 m² de uma cor que
mais nada usa; em 18 ele entra na mesma pilha do liso e das portas — 19,27 m² em
cinco chapas. **R$ 434,52 de economia** sem tirar nada do móvel.

---

## O custo — R$ 8.332,44 de custo direto

| item | custo direto |
|---|--:|
| Painel ripado com o vão do nicho · 352 × 277 | R$ 2.878,80 |
| Porta ripada do armário, mimetizada · 50 × 277 | R$ 1.121,50 |
| Painel liso com os vãos das portas · 330 × 277 | R$ 1.333,95 |
| Duas portas mimetizadas de passagem · 83 e 70 × 210 | R$ 1.419,28 |
| Estrutura de fixação do painel | R$ 964,97 |
| Iluminação do nicho · fita 3000K | R$ 613,93 |
| **CUSTO DIRETO** | **R$ 8.332,44** |

| por natureza | |
|---|--:|
| MDF Gianduia 18 mm · 19,27 m² · 5 chapas | R$ 3.500,00 |
| MDF Branco TX 18 mm · 4,30 m² · 2 chapas (estrutura) | R$ 800,00 |
| Terceirizados · ripado R$ 1.042,96 + filete R$ 713,70 + LED R$ 453 | R$ 2.209,66 |
| Ferragem · 3 pivôs, 3 fechos, fonte | R$ 705,00 |
| Fita de borda · 59,4 m | R$ 195,99 |
| Consumíveis 6% · corte · embalagem 2% | R$ 521,80 |
| Frete · 2 viagens | R$ 400,00 |

---

## O que cada decisão custa

| | custo direto | |
|---|--:|--:|
| ripado até a pedra, liso dali (a ordem do Jonathan) | R$ 8.332,44 | — |
| ripado correndo os 682 inteiros | R$ 11.930,57 | **+R$ 3.598,13** |

⭐ **A ordem economiza R$ 3.598,13** — o ripado inteiro custaria 43% a mais.
São **82 ripas, 454 m de filete e 9,14 m² de mão de obra** que deixam de existir.

| a dúvida do Gianduia Trama | custo direto | |
|---|--:|--:|
| MDF cor de catálogo · R$ 700 a chapa | R$ 8.332,44 | — |
| padrão especial da Base · R$ 1.000 a chapa | R$ 9.954,24 | **+R$ 1.621,80** |

⚠ *Trama* é padrão texturizado. **É a primeira cotação a fazer** — vale 19% do
custo do projeto. Roda com `ESPECIAL=1`.

---

## A régua de preço — nenhum preço foi fechado

| | MC 35% | MC 40% |
|---|--:|--:|
| sem RT | R$ 16.706,65 | R$ 18.568,11 |
| com RT de 10% | R$ 20.279,75 | R$ 23.089,55 |

---

## ⛔ Fora do escopo — regra 19

Nicho **131 × 302 em mármore travertino romano estucado** · **sóculo em
alvenaria** revestido de mármore (a prancha diz alvenaria) · **rodapé de 15 cm**
em mármore · **janela 202 × 175** em vidro laminado com estrutura metálica.
⭐ A fita de LED do nicho **é nossa**: é usinada e embutida na marcenaria.

## Dúvidas abertas

1. ⭐ **O painel é pele sobre alvenaria, ou a marcenaria faz o volume de 50 de
   profundidade?** Assumi pele: a prancha diz *"sóculo em alvenaria"* e o nicho
   é revestido pelo marmorista. Se o volume for nosso, é outro orçamento.
2. ⭐ **O interior do "ARMÁRIO 50X274" atrás da porta ripada não está desenhado**
   — sem prateleira, divisória nem profundidade útil. **Não está orçado.**
3. ⚠ **Gianduia Trama é padrão especial?** Vale R$ 1.621,80.
4. ⚠ **A prancha pede relevo de 20 mm e cortamos de chapa de 18** — padrão da
   casa. Ou aceita-se 18, ou lamina-se, e aí muda.
5. ⚠ **Estrutura:** montantes a cada 60 cm passam 5% do rendimento de uma chapa
   e compram a segunda inteira (R$ 400). A cada 75 cm cabem numa só. Não mexi.
6. ⚠ **Nome do cliente** — as pranchas não trazem. Falta para a proposta.
