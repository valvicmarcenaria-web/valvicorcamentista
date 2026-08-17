# ELIUTON RIBEIRO — Residência Brisas da Pampulha

**Data:** 13/08 (bloqueio) → **17/08/2026 (projeto LIDO e orçado)**
**Autoria:** Arq. **Luciana Beatriz Simplício** — Núcleo SC Arquitetura ·
(31) 3004-3387 · CAU MG A54855-3
**Motor:** `corte-eliuton.py` · **Dúvidas:** `2026-eliuton-duvidas-tecnicas.md`

---

## O número

| Cenário | Ferragem | Custo direto | **Investimento** | MC real | Garantia |
|---|---|--:|--:|--:|--:|
| 1 · Telescópica | padrão · pistão simples | 48.252 | **R$ 103.800** | 33,5% | 2 anos |
| 2 · Hardt | Hardt · oculta Hardt · Blum HK-xs | 50.516 | **R$ 118.800** | 37,5% | 5 anos |
| 3 · Hettich | Novisys · oculta Quadro · Blum HK-xs | 51.510 | **R$ 134.500** | 41,7% | 10 anos |

**160,82 m² de chapa · 48 chapas · 66% de aproveitamento médio · 580 m de fita ·
72 dobradiças · 17 gavetas · 7 básculas · 30,3 m de cava usinada.**

Com RT de 10% para a arquiteta: **128.900 · 150.300 · 174.200** (+24% a +30%).

> ⚠ **Estes números são da 2ª rodada.** A 1ª saiu a 126.400 / 143.800 / 162.500 e
> o Jonathan apontou que estava alto demais. Estava — ver "A revisão" abaixo.
> A sanidade de R$/m² de chapa caiu de **846 para 739**, dentro da faixa da casa
> (626–834).

---

## Como o projeto foi lido

Os 19 PDFs chegaram por upload em 17/08. **Não eram raster** — como eu tinha
diagnosticado em 13/08 pelo OCR instável do conector do Drive. São **vetoriais
com o texto convertido em curvas**: por isso zero palavras extraíveis e por isso
o conector só devolvia o carimbo OCR-ado. Duas coisas diferentes que pareciam a
mesma.

Lidos com PyMuPDF, renderizados a 1,4× e ampliados onde a cota era pequena.

**A escala foi aferida no próprio desenho**, não assumida: a 1:25 em A3,
1 pt = 0,88195 cm reais. Medindo a porta de passagem desenhada, deu
**80,0 × 210,0** — exatamente a cota escrita `80X210`. Com a escala travada,
medi o painel ripado direto na geometria: **570,6 × 287,5 cm**, contra 572 na
cadeia de cotas da planta e 288 na elevação. Bate.

### ⚠ Os nomes dos arquivos não correspondem às folhas
| Arquivo | Folha real |
|---|---|
| `PR 05_COZINHA` | **08/08** — Área Gourmet, bancadas 02 e 03 |
| `PR 05_COZINHA (1)` | **05/08** — Cozinha, ilha |

O Jonathan tinha avisado em 13/08 que os dois `PR 05` não eram duplicatas.
Estava certo — e o motivo é este. **O carimbo é a única referência confiável.**

### São DUAS séries, não uma
- **01/08 a 08/08** — cozinha e área gourmet · datadas 12/12/25
- **01/10 a 10/10** — área de serviço e banheiros · datadas 17/12/25

⚠ **A folha 02/10 continua faltando.** É o detalhamento da área de serviço, e
as duas legendas da folha 01/10 ("portas de abrir" e "portas basculantes")
mandam ver o detalhe justamente nela.

---

## Escopo — 8 itens de orçamento

[Jonathan 17/08] **A cozinha vai como conjunto completo num item só.**

| # | Item | Folha | Cor | Chapa | Investimento (cen. 2) |
|---|---|---|---|--:|--:|
| 1 | **Cozinha — conjunto completo** · torre quente + nicho geladeira 187×70×290, acabamento superior, bancada 01 (355×70×88), aéreo (351×40×96, 5 portas), ilha (226×70×88) | 02–05/08 | Nogueira Persa + Sálvia | 56,42 m² | **37.000** |
| 2 | **Painel ripado do estar/jantar 572×288** | 02/08 | Nogueira Persa | 28,45 m² | **18.800** |
| 3 | Gourmet · bancada 02 + coluna da cervejeira 215×290 | 07–08/08 | Nogueira Persa | 17,97 m² | 14.100 |
| 4 | **Área de serviço 359×55×226** | 01/10 | Nogueira Persa | 32,10 m² | **23.600** |
| 5 | Lavabo externo · painel + gabinete + forro | 03/10 | Nogueira Persa | 6,01 m² | 4.100 |
| 6 | Banheiro master · espelheira + gabinete **ripado** | 06/10 | **Jequitibá** | 8,01 m² | 8.500 |
| 7 | Banheiro 02 (social 1º pav) | 07–08/10 | Nog. Persa + **Beige** | 6,34 m² | 5.900 |
| 8 | Banheiro 04 | 09–10/10 | Nogueira Persa | 5,52 m² | 6.800 |

O **painel ripado fica fora do item da cozinha** por dois motivos: é outra parede
(a do estar/jantar) e tem **MC própria de 40%**, então precisa de linha separada
no motor. Se o Jonathan quiser juntar comercialmente, é só somar: **R$ 55.800**.

**Banheiro social térreo (04/10) não tem marcenaria** — cuba esculpida,
prateleira, porta e nicho são todos em mármore travertino. A única peça de MDF
citada lá é a porta pivotante, que já está contada no painel da cozinha.

### Chapa especificada — a dúvida A/B está respondida
O executivo especifica **MDF ARAUCO 18 mm** em quatro acabamentos:
**Nogueira Persa** (a cor dominante) · **Sálvia** (verde — só a cozinha:
aéreo, bancada 01, ilha) · **Jequitibá** (só o banheiro master) ·
**Beige** (só as 4 prateleiras do nicho do banheiro 02).

---

## ⛔ O que NÃO está no número

**Todo o mármore.** As pranchas especificam Carrara e Travertino em
praticamente todo ambiente: bancadas 01, 02 e 03; a **ilha tipo cascata** e o
acabamento sob ela; o **ripado da bancada 03 do gourmet — que é de mármore, não
de madeira**; rodabancas; o "detalhe caixa" da cozinha; nichos com LED; cubas
esculpidas; prateleiras; a porta de manutenção do banheiro social.

Isso é marmoraria. Se a Valvic for fornecer, é orçamento à parte e muda o total.
**Perguntar ao Jonathan antes de mandar qualquer proposta.**

Também fora: louças e metais Deca, eletrodomésticos, churrasqueira, revestimentos,
e os móveis soltos (mesa Vicenza, cadeiras Napoli, buffet elipse, sofá e poltronas
Faruk, banquetas).

---

## Um erro que o motor pegou — e a guarda que ficou

A ripa do painel do estar/jantar tem **288 cm de altura**. A chapa tem
**275 × 185**. Ela não cabe — nem deitada, nem em pé.

O empacotador não reclamou: ele simplesmente abriu **uma chapa por ripa**.
Resultado: **111 chapas de Nogueira Persa com 9% de aproveitamento**, um número
que passa por plano de corte válido se ninguém olhar a coluna de aproveitamento.

Peça que não cabe na chapa **não é problema de empacotamento, é erro de projeto
de marcenaria**: ou emenda, ou muda o desenho. Aqui a emenda cai na horizontal
do acabamento sobre a porta de correr — ripa em 2 trechos de 144. Corrigido,
a Nogueira 18 mm caiu de 111 para **10 chapas** e o aproveitamento subiu para
69%.

**Ficou uma guarda no motor** que lista qualquer peça fora de chapa antes de
qualquer conta. Ela pegou uma segunda: o rodapé da área de serviço, 359 cm.
Ver `referencias/quantitativo.md`.

---

## A revisão — o que estava errado na 1ª rodada

O Jonathan olhou os R$ 143.800 e disse que estava alto demais. Estava. Auditei
peça a peça e achei nove erros — quatro de **material contado a mais** e cinco de
**preço unitário na convenção errada**.

### Material contado a mais

| # | Erro | Efeito |
|--:|---|--:|
| 1 | **Nicho de eletrodoméstico com fundo de MDF.** Geladeira, forno, micro-ondas e cervejeira precisam de ventilação e tomada — o fundo é a alvenaria, não uma chapa. | −6,2 m² |
| 2 | **Tampo contado duas vezes na torre.** O tampo sobre o nicho da geladeira **já é** a base do armário basculante de cima. | −0,7 m² |
| 3 | **Fundo do caixote de vidro do gourmet** lançado em duas linhas. | −0,4 m² |
| 4 | **Tampo de MDF sob bancada de mármore**, em 5 gabinetes. Vira travessa — quem faz o tampo é a marmoraria. Eu já fazia certo na bancada 01, na ilha e no gourmet; nos banheiros e no lavabo escorreguei. | −1,8 m² |

### Preço unitário na convenção errada

| # | Erro | Efeito |
|--:|---|--:|
| 5 | **Cava cobrada por peça.** `materiais.json` traz "R$ 50/peça", mas a Honda usou **R$ 25/m** — e foi esse que o Jonathan validou num job real. A CNC cobra percurso, e percurso é metro linear. R$ 50 × 50 frentes virou R$ 25 × 30,3 m. | −R$ 1.744 |
| 6 | **Espelho cotado por m²** — a **armadilha nº 4 da minha própria lista**: *"a casa cota vidro e espelho por FOLHA, não por m²"*. Caí nela. R$ 285/folha com perfil. | −R$ 542 |
| 7 | **SS150 em porta de banheiro.** SS150 é sistema de **roupeiro** — folha pesada, 65 cm de profundidade. Porta de espelho num armário de **15 cm** é RO65 Rometal. | −R$ 1.610 |
| 8 | **LED a R$ 150/m.** A decomposição rastreável do `chapas.md` dá R$ 66/m (fita 28 + perfil 38). | −R$ 341 |
| 9 | **Montagem escalada por m² de chapa.** Peguei a Honda (22,89 m² → 3 dias) e multipliquei: 22 dias. Errado — **montagem escala por conjunto e por complexidade, não por área**. Uma chapa de fundo de 3 m² não custa nada de montagem; um caixote pequeno com ferragem custa meio dia igual. Contado conjunto a conjunto: 13 dias. | −R$ 6.250 |

**Efeito total:** 169,93 → **160,82 m²** · 49 → **48 chapas** · custo direto
61.219 → **50.516** · preço 143.800 → **118.800** no cenário 2.

O erro nº 9 sozinho valia R$ 14.500 de preço — mais que os oito outros somados.
E os R$ 10.950 que ficaram **continuam sendo estimativa minha**. É o Jonathan
quem crava.

---

## As premissas que ainda mexem no número

| # | Premissa adotada | Se mudar |
|---|---|--:|
| 1 | Chapa Arauco madeirada cotada como **cor** (500/600/300) | como **especial**: +R$ 57.000 de preço |
| 2 | **Ripado 100%** no painel do estar/jantar | a prancha diz "parte ripado parte liso" |
| 3 | Ripa 4,0 cm + espaçamento 1,5 (passo 5,5) | ilegível a 1:25 — só a arquiteta sabe |
| 4 | **13 dias de dupla** + 4 carretos + 3 visitas = R$ 10.950 | 22% do custo direto |
| 5 | Fundos **na cor** (as perspectivas mostram interior na cor) | em branco: −R$ 1.883 |
| 6 | MDF **Beige** só nas 4 prateleiras do banheiro 02 | trocar por Nogueira: −R$ 2.092 |
| 7 | Básculas do topo da área de serviço com **HK-xs** | 113 cm de altura pede **Aventos** (R$ 600 vs 250) |

A **1** é a mais cara de todas e a mais fácil de resolver: é uma ligação para o
fornecedor. **Nogueira Persa e Jequitibá são madeirados Arauco e a base da casa
nunca fechou o preço dessa linha** — o `corte-lm.py` deixou a marca "ver FLAG
premium" e ela nunca foi preenchida. Enquanto isso não fechar, o número tem
±R$ 57 mil de incerteza. É o item nº 1 antes de propor qualquer coisa.

---

## Onde o dinheiro está

- **Cozinha (37.000), área de serviço (23.600) e painel ripado (18.800) somam
  67% do projeto.** São os três itens onde vale gastar tempo de conferência.
- O painel sozinho consome **28,45 m² de chapa (18%) e 305 m de fita (53% de
  toda a fita do projeto)**. É o gargalo de fita da casa — exatamente o que
  `laminacao-e-construcao.md` avisa.
- **Cor que não divide chapa cobra caro pelas peças pequenas:** Beige (1,33 m²)
  e Jequitibá 18 mm (0,77 m²) consomem chapa inteira cada.
- **R$/m² de chapa: 739.** Faixa da casa: 626 (Rizzi) · 647 (aéreo cozinha) ·
  739 (SPE decorado) · 834 (Honda). Bate exatamente com o SPE decorado, que é o
  job mais parecido em porte e acabamento.

---

## Inventário da pasta (19 arquivos)

| Série | Folhas | Conteúdo |
|---|---|---|
| Cozinha/Gourmet | 01–08 de 08 | layout, elevações, bancada 01, torre e aéreo, ilha, gourmet layout, gourmet elevação, gourmet bancadas 02/03 |
| Áreas molhadas | 01, 03–10 de 10 | serviço, lavabo, social térreo, master ×2, banheiro 02 ×2, banheiro 04 ×2 |
| Mestres | — | `PLANTAS COTADAS` (A0, vetorial) · `PROJ. ELTN_A3` (pacote de revestimento, 7 pág.) |

**Falta a 02/10.**
