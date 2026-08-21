# ELIUTON RIBEIRO — Residência Brisas da Pampulha

**Data:** 13/08 (bloqueio) → **17/08/2026 (projeto LIDO e orçado)**
**Autoria:** Arq. **Luciana Beatriz Simplício** — Núcleo SC Arquitetura ·
(31) 3004-3387 · CAU MG A54855-3
**Motor:** `corte-eliuton.py` · **Proposta:** `build-eliuton.py` → `proposta-eliuton.pdf` (5 pág.)
**Prazo:** 90 a 120 dias **corridos** [Jonathan 17/08] · **Validade:** 7 dias (premissa)
**Dúvidas:** `2026-eliuton-duvidas-tecnicas.md`

---

## O número

| Cenário | Ferragem | Custo direto | **Investimento** | MC real | Garantia |
|---|---|--:|--:|--:|--:|
| 1 · Telescópica | padrão · pistão simples | 40.452 | **R$ 86.900** | 33,5% | 2 anos |
| 2 · Hardt | Hardt · oculta Hardt · Blum HK-xs | 42.716 | **R$ 100.400** | 37,5% | 5 anos |
| 3 · Hettich | Novisys · oculta Quadro · Blum HK-xs | 43.710 | **R$ 114.100** | 41,7% | 10 anos |

**160,82 m² de chapa · 48 chapas · 66% de aproveitamento médio · 580 m de fita ·
72 dobradiças · 17 gavetas · 7 básculas · 30,3 m de cava usinada.**

Com RT de 10% para a arquiteta: **108.100 · 127.100 · 147.800** (+24% a +30%).

> ⚠ **3ª rodada.** A 1ª saiu a 126.400 / 143.800 / 162.500; o Jonathan disse que
> estava alto demais e a auditoria achou nove erros. Na 2ª ele apontou o décimo,
> que era o maior de todos: **eu tinha lançado montagem no custo direto, e a
> Valvic nunca põe montagem no custo.**
> ⚠ **Mas montagem ENTRA no escopo.** A equipe é própria e isso é diferencial de
> venda — a proposta diz, em duas páginas, que a Valvic instala com equipe
> própria e não terceiriza a montagem. Custo e escopo são coisas diferentes.
> A sanidade de R$/m² de chapa foi de **846 → 739 → 624**, agora no piso da faixa
> da casa (626 no Rizzi) — que é onde um job grande tem de ficar, porque o custo
> fixo por m² dilui.

---

## 🔒 20/08/2026 — VERSÃO DE FECHAMENTO (4ª rodada)

`projetos/build-eliuton-fechamento.py` → **`proposta-eliuton-fechamento.pdf`**,
7 páginas. Uma linha só — a Intermediária. Proposta de fechamento não oferece
escolha, oferece decisão.

| | |
|---|---|
| Escopo | **6 conjuntos** — sem área de serviço e sem lavabo externo |
| Investimento cheio | R$ 81.200 |
| Condição especial de fechamento | **R$ 73.000** (economia R$ 8.200) |
| Entrada de 30 % na assinatura | R$ 21.900 |
| Saldo de 70 % à vista, pós-entrega | R$ 51.100 |
| Prazo | 65 dias corridos |
| Validade da condição | sábado, 22/08/2026 |

### ⛔ Tirar ambiente NÃO é subtrair a linha do rateio

O Jonathan mandou tirar **área de serviço e lavabo externo**. A conta que parece
certa — 100.500 − 15.000 − 3.400 = 82.100 — **está errada por dois motivos**.

**1 · Três coisas mudam quando um ambiente sai:**

| | |
|---|---|
| **Nesting** | 38 m² a menos não são 8 chapas a menos. A chapa parcial que sobrava para um ambiente vira sobra inteira. |
| **Logística** | 4 carretos viram 3. |
| **Custo fixo rateável** | Redistribui-se entre os que ficam — e **sobe o preço unitário de cada um**. |

Por isso o motor rodou de novo, com exclusão feita **antes** do levantamento:

```
EXCLUIR='Área de serviço|Lavabo externo' python3 corte-eliuton.py
```

Todos os conjuntos que ficam subiram:

| Conjunto | 8 itens | 6 itens |
|---|--:|--:|
| Cozinha — conjunto completo | 30.700 | **32.600** |
| Painel ripado | 20.400 | **16.400** |
| Área gourmet — bancada 02 | 12.000 | **12.600** |
| Banheiro master | 7.600 | **7.900** |
| Banheiro social | 5.200 | **5.400** |
| Banheiro 04 | 6.200 | **6.300** |
| **TOTAL** | 100.500 | **81.200** |

**2 · A realocação comercial caiu junto.** Em 17/08 o Jonathan tirou R$ 5.000 da
área de serviço e pôs no painel ripado — par de soma zero. Saindo a área de
serviço, o **+5.000 do ripado ficaria sem contraparte** e inflaria o total. Por
isso o ripado volta de 20.400 para 16.400. Uma subtração de linhas teria deixado
esses R$ 5.000 pendurados no ripado sem que ninguém percebesse.

O motor agora tem a exclusão embutida e recusa nome de ambiente que não exista,
para que a próxima redução de escopo não seja feita na mão.

### 4ª rodada — número redondo e entrada de 30 % exatos

[Jonathan] *"a entrada precisa corresponder a 30 % do valor, mas trabalhe com
valor cheio não quebrado."*

Os 10 % exatos davam R$ 73.080 — e 30 % disso é R$ 21.924, quebrado. Levando o
fechamento a **R$ 73.000 redondos**, os três números fecham limpos:

| | |
|---|--:|
| Fechamento | **R$ 73.000** |
| Entrada de 30 % | **R$ 21.900** |
| Saldo de 70 % | **R$ 51.100** |

⚠ **O desconto real vira 10,1 %, não 10 %.** Arredondar para baixo custa R$ 80 a
mais de desconto. Por isso a proposta **deixou de anunciar o percentual** e passou
a mostrar os dois valores e a economia em reais (R$ 8.200): dizer "−10 %" e
apresentar 81.200 → 73.000 daria ao cliente uma conta que não bate. A capa, o
título da página 2 e o cabeçalho da tabela foram todos reescritos por causa disso.

### Margem e caixa

| | Cheio | Fechamento |
|---|--:|--:|
| Preço | 81.200 | **73.000** |
| Custo direto | 34.418 | 34.418 |
| **MC real** | 37,6 % | **32,9 %** |

⚠ Entrada de R$ 21.900 contra custo direto de R$ 34.418 — cobre **64 %**,
deixando **R$ 12.518** de capital de giro por 65 dias. Voltar aos 30 % devolveu
ao cliente a folga que a entrada de R$ 27.000 tinha dado à Valvic: a exposição
sobe de R$ 7.418 para R$ 12.518.

A MC de 32,9 % segue abaixo da faixa ideal da casa (35–40 %), pelo mesmo motivo
de sempre: o desconto.

### O que a versão de fechamento tem que a de 17/08 não tinha

- **Memorial descritivo item a item** — os seis conjuntos com material,
  composição construtiva e o porquê das decisões técnicas (nicho de
  eletrodoméstico sem fundo, emenda da ripa de 288, RO65 em vez de SS150).
- **Especificação técnica geral** — chapa, borda, cava, ferragem, iluminação,
  espelho e vidro, serralheria e produção. **Sem quantitativo.**
- **Valor cheio e valor de fechamento lado a lado** em cada item e no resumo.
- Área de serviço e lavabo externo aparecem nomeados em **"não incluso"**, com a
  ressalva de que podem ser orçados à parte.

### 🐛 Um defeito que apareceu ao montar

`projetos/css-proposta.css` tinha **código Python colado depois do CSS**
(linhas 122–265, sobra de uma sessão antiga). O parser do navegador entrava em
erro ali e **engolia silenciosamente tudo que viesse depois** — as regras novas
desta proposta simplesmente não pintavam, sem erro nenhum. Arquivo truncado no
fim do CSS real (118 linhas).

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

| # | Item | Cor | Chapa | I | II | III |
|---|---|---|--:|--:|--:|--:|
| 1 | **Cozinha — conjunto completo** (torre + acabamento + bancada 01 + aéreo + ilha) | Nog. Persa + Sálvia | 56,42 m² | 25.300 | **30.700** | 36.000 |
| 2 | **Painel ripado do estar/jantar** 572×288 | Nogueira Persa | 28,45 m² | 20.400 | **20.400** | 20.400 |
| 3 | Área gourmet · bancada 02 + cervejeira | Nogueira Persa | 17,97 m² | 10.000 | **12.000** | 14.200 |
| 4 | **Área de serviço** 359×55×226 | Nogueira Persa | 32,10 m² | 11.600 | **15.000** | 18.200 |
| 5 | Lavabo externo · painel + gabinete + forro | Nogueira Persa | 6,01 m² | 2.600 | **3.400** | 3.900 |
| 6 | Banheiro master · espelheira + gabinete **ripado** | **Jequitibá** | 8,01 m² | 6.800 | **7.600** | 8.500 |
| 7 | Banheiro social 1º pav | Nog. Persa + **Beige** | 6,34 m² | 4.700 | **5.200** | 5.900 |
| 8 | Banheiro 04 | Nogueira Persa | 5,52 m² | 5.500 | **6.200** | 7.000 |
| | **TOTAL** | | **160,82 m²** | **86.900** | **100.500** | **114.100** |

**[Jonathan 17/08] Realocação comercial aplicada:** −R$ 5.000 da área de serviço,
+R$ 5.000 no painel ripado. O total não muda — é remanejamento de vitrine entre
itens, não mudança de escopo nem de margem.

**O painel ripado custa o mesmo nas três linhas.** É o único conjunto sem uma
dobradiça, corrediça ou báscula sequer — e como a diferença entre os cenários é
inteiramente ferragem, ele não se move. Virou argumento de página na proposta.

O **painel ripado fica fora do item da cozinha** por dois motivos: é outra parede
(a do estar/jantar) e tem **MC própria de 40%**, então precisa de linha separada
no motor. Se o Jonathan quiser juntar comercialmente, é só somar: **R$ 46.100**.

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
| 9 | **Montagem lançada como custo direto.** Na 1ª rodada como 22 dias de dupla; na 2ª eu "corrigi" para 13. Errado das duas vezes — **a linha não existe**. Ver abaixo. | −R$ 13.200 |

### ⛔ O erro nº 9, que só o Jonathan pegou: montagem não entra na proposta

> *"Nunca consideramos montagem na proposta."* — Jonathan, 17/08.

Estava escrito em `validacao-orcamento.md`, na lista de **custos fixos**:
*"salários de toda a equipe (7 profissionais — marceneiros, montadores, etc.).
A produção é fixa, não por demanda."* E logo abaixo: *"o marceneiro tem salário
(fixo, fora do orçamento) e pode ter comissão (variável, dentro do orçamento).
Só a comissão entra."*

E a comissão **já está dentro do motor**, nos coeficientes `a = 0,162` e
`liqF·b = 0,0378`. Lançar dia de montador conta a mesma mão de obra duas vezes:
uma no salário que a empresa paga de qualquer jeito, outra na comissão que o
divisor já cobra. E ainda infla o preço, porque passa pelo divisor.

Na 2ª rodada eu tratei isso como "erro de escala" e fui de 22 para 13 dias.
Continuava errado — o problema não era o número de dias, era a linha existir.
Sobra o que é variável de verdade: **4 carretos + 3 visitas = R$ 3.150**.

**Efeito total das 9 correções:** 169,93 → **160,82 m²** · 49 → **48 chapas** ·
custo direto 61.219 → **42.716** · preço 143.800 → **100.400** no cenário 2.

### ⚠ Isso respinga na Honda
`corte-honda-minas-motos.py` tem `INSTAL = 1800` ("3 dias de dupla") no custo
direto. Pela regra, não deveria. Num job **já entregue a R$ 19.100**, o custo
direto real é R$ 6.799 e a **MC foi 44,4%, não os 35% declarados**. O job é mais
lucrativo do que está registrado. Não mexi no arquivo entregue.

---

## As premissas que ainda mexem no número

| # | Premissa adotada | Se mudar |
|---|---|--:|
| 1 | Chapa Arauco madeirada cotada como **cor** (500/600/300) | como **especial**: +R$ 57.000 de preço |
| 2 | **Ripado 100%** no painel do estar/jantar | a prancha diz "parte ripado parte liso" |
| 3 | Ripa 4,0 cm + espaçamento 1,5 (passo 5,5) | ilegível a 1:25 — só a arquiteta sabe |
| 4 | **4 carretos + 3 visitas = R$ 3.150** (sem montagem) | 7% do custo direto |
| 5 | Fundos **na cor** (as perspectivas mostram interior na cor) | em branco: −R$ 1.883 |
| 6 | MDF **Beige** só nas 4 prateleiras do banheiro 02 | trocar por Nogueira: −R$ 2.092 |
| 7 | Básculas do topo da área de serviço com **HK-xs** | 113 cm de altura pede **Aventos** (R$ 600 vs 250) |

A **1** é a mais cara de todas e a mais fácil de resolver: é uma ligação para o
fornecedor. **Nogueira Persa e Jequitibá são madeirados Arauco e a base da casa
nunca fechou o preço dessa linha** — o `corte-lm.py` deixou a marca "ver FLAG
premium" e ela nunca foi preenchida. Enquanto isso não fechar, o número tem
±R$ 57 mil de incerteza — mais da metade do preço do cenário 2. É o item nº 1 antes de propor qualquer coisa.

---

## Onde o dinheiro está

- **Cozinha (30.700), área de serviço (20.000) e painel ripado (15.400) somam
  66% do projeto.** São os três itens onde vale gastar tempo de conferência.
- O painel sozinho consome **28,45 m² de chapa (18%) e 305 m de fita (53% de
  toda a fita do projeto)**. É o gargalo de fita da casa — exatamente o que
  `laminacao-e-construcao.md` avisa.
- **Cor que não divide chapa cobra caro pelas peças pequenas:** Beige (1,33 m²)
  e Jequitibá 18 mm (0,77 m²) consomem chapa inteira cada.
- **R$/m² de chapa: 624.** Faixa da casa: 626 (Rizzi) · 647 (aéreo cozinha) ·
  739 (SPE decorado) · 834 (Honda, job pequeno). O Eliuton no piso da faixa é o
  esperado: é o maior job da base, e custo fixo por m² dilui com o tamanho.

---

## Inventário da pasta (19 arquivos)

| Série | Folhas | Conteúdo |
|---|---|---|
| Cozinha/Gourmet | 01–08 de 08 | layout, elevações, bancada 01, torre e aéreo, ilha, gourmet layout, gourmet elevação, gourmet bancadas 02/03 |
| Áreas molhadas | 01, 03–10 de 10 | serviço, lavabo, social térreo, master ×2, banheiro 02 ×2, banheiro 04 ×2 |
| Mestres | — | `PLANTAS COTADAS` (A0, vetorial) · `PROJ. ELTN_A3` (pacote de revestimento, 7 pág.) |

**Falta a 02/10.**
