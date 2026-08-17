# ELIUTON RIBEIRO — Residência Brisas da Pampulha

**Data:** 13/08 (bloqueio) → **17/08/2026 (projeto LIDO e orçado)**
**Autoria:** Arq. **Luciana Beatriz Simplício** — Núcleo SC Arquitetura ·
(31) 3004-3387 · CAU MG A54855-3
**Motor:** `corte-eliuton.py` · **Dúvidas:** `2026-eliuton-duvidas-tecnicas.md`

---

## O número

| Cenário | Ferragem | Custo direto | **Investimento** | MC real | Garantia |
|---|---|--:|--:|--:|--:|
| 1 · Telescópica | padrão · pistão simples | 58.955 | **R$ 126.400** | 33,4% | 2 anos |
| 2 · Hardt | Hardt · oculta Hardt · Blum HK-xs | 61.219 | **R$ 143.800** | 37,4% | 5 anos |
| 3 · Hettich | Novisys · oculta Quadro · Blum HK-xs | 62.213 | **R$ 162.500** | 41,7% | 10 anos |

**169,93 m² de chapa · 49 chapas · 68% de aproveitamento médio · 580 m de fita ·
94 dobradiças · 17 gavetas · 9 básculas · 50 cavas usinadas.**

Com RT de 10% para a arquiteta: **157.100 · 182.000 · 210.500** (+24% a +30%).

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

## Escopo — 12 conjuntos de marcenaria

| # | Conjunto | Folha | Cor | Chapa | Investimento (cen. 2) |
|---|---|---|---|--:|--:|
| 1 | Torre quente + nicho geladeira · 187×70×290 | 04/08 | Nogueira Persa | 18,75 m² | 14.300 |
| 2 | Acabamento superior (faixa 15 sob o forro) | 02–04/08 | Nogueira Persa | 0,81 m² | 500 |
| 3 | Bancada 01 · armário inferior 355×70×88 | 03/08 | Sálvia | 16,19 m² | 12.100 |
| 4 | Aéreo 351×40×96 · 5 portas | 04/08 | Sálvia | 12,81 m² | 8.900 |
| 5 | Ilha 226×70×88 | 05/08 | Sálvia | 12,59 m² | 9.600 |
| 6 | **Painel ripado do estar/jantar 572×288** | 02/08 | Nogueira Persa | 28,45 m² | **20.800** |
| 7 | Gourmet · bancada 02 + cervejeira 215×290 | 07–08/08 | Nogueira Persa | 19,77 m² | 17.100 |
| 8 | **Área de serviço 359×55×226** | 01/10 | Nogueira Persa | 32,54 m² | **26.600** |
| 9 | Lavabo externo · painel + gabinete | 03/10 | Nogueira Persa | 6,59 m² | 4.900 |
| 10 | Banheiro master · espelheira + gabinete **ripado** | 06/10 | **Jequitibá** | 8,73 m² | 11.000 |
| 11 | Banheiro 02 (social 1º pav) | 07–08/10 | Nog. Persa + **Beige** | 6,67 m² | 8.800 |
| 12 | Banheiro 04 | 09–10/10 | Nogueira Persa | 6,02 m² | 9.200 |

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

## As premissas que mais mexem no número

| # | Premissa adotada | Se mudar |
|---|---|--:|
| 1 | Chapa Arauco madeirada cotada como **cor** (500/600/300) | como **especial**: +R$ 58.100 de preço |
| 2 | **Ripado 100%** no painel do estar/jantar | a prancha diz "parte ripado parte liso" |
| 3 | Ripa 4,0 cm + espaçamento 1,5 (passo 5,5) | ilegível a 1:25 — só a arquiteta sabe |
| 4 | **22 dias de dupla** + 5 carretos + 4 visitas = R$ 17.200 | 28% do custo direto |
| 5 | Fundos **na cor** (as perspectivas mostram interior na cor) | em branco: −R$ 2.274 |
| 6 | MDF **Beige** só nas 4 prateleiras do banheiro 02 | trocar por Nogueira: −R$ 2.092 |
| 7 | Básculas do topo da área de serviço com **HK-xs** | 113 cm de altura pede **Aventos** (R$ 600 vs 250) |

A **1** é a mais cara de todas e a mais fácil de resolver: é uma ligação para o
fornecedor. **Nogueira Persa e Jequitibá são madeirados Arauco e a base da casa
nunca fechou o preço dessa linha** — o `corte-lm.py` deixou a marca "ver FLAG
premium" e ela nunca foi preenchida. Enquanto isso não fechar, o número tem
±R$ 58 mil de incerteza. É o item nº 1 antes de propor qualquer coisa.

---

## Onde o dinheiro está

- **Painel ripado (20.800) e área de serviço (26.600) somam 33% do projeto.**
  São os dois conjuntos onde vale gastar tempo de conferência.
- O painel sozinho consome **28,45 m² de chapa (17%) e 305 m de fita (53% de
  toda a fita do projeto)**. É o gargalo de fita da casa — exatamente o que
  `laminacao-e-construcao.md` avisa.
- A **cava usinada** aparece 50 vezes: R$ 2.500 de custo, R$ 5.800 de preço.
  Se virar perfil Rometal muda a conta e a estética; decisão do Jonathan (D5).
- **Cor que não divide chapa cobra caro pelas peças pequenas:** Beige (1,33 m²)
  e Jequitibá 18 mm (0,77 m²) consomem chapa inteira cada.

---

## Inventário da pasta (19 arquivos)

| Série | Folhas | Conteúdo |
|---|---|---|
| Cozinha/Gourmet | 01–08 de 08 | layout, elevações, bancada 01, torre e aéreo, ilha, gourmet layout, gourmet elevação, gourmet bancadas 02/03 |
| Áreas molhadas | 01, 03–10 de 10 | serviço, lavabo, social térreo, master ×2, banheiro 02 ×2, banheiro 04 ×2 |
| Mestres | — | `PLANTAS COTADAS` (A0, vetorial) · `PROJ. ELTN_A3` (pacote de revestimento, 7 pág.) |

**Falta a 02/10.**
