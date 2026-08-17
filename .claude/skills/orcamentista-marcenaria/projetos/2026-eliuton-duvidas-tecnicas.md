# ELIUTON · Brisas da Pampulha — LEVANTAMENTO DE DÚVIDAS TÉCNICAS

**Data:** 13/08/2026 · **Antes do levantamento**, como pedido pelo Jonathan:
*"gere todo o levantamento de dúvidas técnicas antes para não cometermos erros."*

Cada pergunta aqui **muda um número**. Não há pergunta de curiosidade nesta lista —
onde eu souber responder sozinha, respondi e marquei como premissa.

---

# PARTE 1 — PARA A ARQUITETA / O CLIENTE

## A. Fronteira de escopo — o que é marcenaria nossa

| # | Pergunta | Por que muda o preço |
|--:|---|---|
| A1 | **Quais ambientes têm marcenaria Valvic?** As 5 pranchas de COZINHA e as 2 de A. GOURMET estão claras. E os 4 banheiros, o lavabo externo e a área de serviço? | O A3 legível só especifica **revestimento, louça e metal**. Se os banheiros tiverem **gabinete, nicho ou espelheira**, são 6 conjuntos a mais. Se não tiverem, saem da conta e não perco tempo com 9 pranchas. |
| A2 | **As bancadas são de pedra (marmoraria) ou nossas?** | O A3 fala em mármore travertino nas paredes. Bancada de pedra é **outra disciplina** — sai do nosso custo e do nosso prazo. Se for tampo em MDF, entra. |
| A3 | **Cubas, metais e louças** — todos Deca, por conta do hidráulico? | Confirmar que não fornecemos. |
| A4 | **Eletrodomésticos** (cooktop, forno, coifa, geladeira, adega, cervejeira) — do cliente? | Nós prevemos **só o vão e a usinagem**. Mas preciso das **medidas exatas** de cada um: vão errado é retrabalho de chapa inteira. |
| A5 | **Forro, sanca ou ripado de teto** entram no nosso escopo? | Ripado tem **MC própria de 40%** e é o item mais caro por m² do projeto. |
| A6 | **Portas de passagem** (giro, correr, pivotante) entram? | São item à parte na tabela da casa. |
| A7 | **Área de serviço** — armário, tanque, torre de máquinas? | O A3 dá 5,42 m² de piso, mas não diz o que é marcenaria. |

## B. Acabamentos — nenhum está definido

| # | Pergunta | Por que muda o preço |
|--:|---|---|
| B1 | **Qual chapa?** Fabricante, linha e cor. | ⚠️ **Não há UMA especificação de MDF em nenhum arquivo que consegui ler.** O A3 é só revestimento. Sem isso não existe orçamento — a chapa é a maior linha de custo. |
| B2 | **Interno branco ou na cor?** | Interno na cor pode somar **30–40%** na área de chapa da cor. |
| B3 | **O RIPADO** — existe? Onde? | Se existir: **qual perfil** (seção e passo), **maciço ou MDF**, **vazado ou aplicado sobre base**? Ripado é gargalo de fita: na cozinha Rizzi ele foi **42% de toda a fita do job**. |
| B4 | **Fita de borda 0,4 mm extra fina** em tudo? | Padrão da casa. Confirmar. |
| B5 | **Fundos em 6 mm com duplo revestimento?** | Padrão da casa. Em área molhada é o que sela contra umidade. |
| B6 | **Vidros e espelhos** — quais, onde, e são nossos? | Se houver cristaleira ou espelheira. ⚠️ **Armadilha de unidade:** a tabela da casa cota vidro e espelho **por folha**, não por m². |

## C. Obra

| # | Pergunta | Por que importa |
|--:|---|---|
| C1 | **Em que fase está a obra?** Dá para medir no local? | O prazo conta da liberação da frente de trabalho. |
| C2 | **Paredes: alvenaria ou drywall?** | Drywall exige bucha específica e, em aéreo longo, reforço estrutural que **não está no preço** se não for previsto. |
| C3 | **Pé-direito.** A única coisa que a `PLANTAS COTADAS` me devolveu foi *"PÉ DIREITO DUPLO"*. | Torre até o teto muda altura de porta e nº de dobradiças. |
| C4 | **Falta o `PR 02-10`** na pasta do Drive. | Sequência 01, _(falta)_, 03…10. |
| C5 | **Pedir o PDF vetorial** em vez do raster. | Com vetor eu leio cota a cota, como fiz na prancha AR-18 da Honda. Com raster, leio **visualmente** e a precisão cai. |

---

# PARTE 2 — PARA O JONATHAN (decisões da casa)

## D. Os três cenários — BLUM FORA [Jonathan 13/08]

Nova escada: **telescópica 32% · Hardt 37% · Hettich 42%**. Isso **mata a dúvida D2** —
as três linhas já estão em `dados/materiais.json`, não há o que cotar.

Montei cada nível a partir da base. **Confirmar, não compor:**

| | 1 · **Telescópica** | 2 · **Hardt** | 3 · **Hettich** |
|---|---|---|---|
| **MC** | **32%** · div 0,48016 | **37%** · div 0,43016 | **42%** · div 0,38016 |
| Dobradiça | Padrão · R$ 6 | Hardt · R$ 8 | ❓ **Sensys R$ 35** ou Novisys R$ 10 |
| Corrediça | Telescópica · R$ 40/par | **Oculta Hardt** · R$ 70/par | ❓ **Quadro R$ 120** ou Actro R$ 400 |
| Báscula | Pistão · R$ 20 | Pistão amortecido · R$ 30 | Pistão amortecido · R$ 30 |
| **Garantia** | **2 anos** | **5 anos** | ❓ **não está na tabela** |

### D1 · Sensys ou Novisys no cenário 3
**Recomendo Sensys.** Novisys custa R$ 10 contra R$ 8 da Hardt — **25% de diferença,
imperceptível na mão**. Se o terceiro nível for Novisys, ele deixa de se distinguir do
segundo na dobradiça, e a escada perde o degrau logo onde o cliente mais toca: a porta.
Com Sensys (R$ 35) a diferença é **4,4×** e se sente.

### D2 · ~~Cotar a linha Blum~~ — **RESOLVIDO**, a Blum saiu.

### D3 · Quadro ou Actro nas gavetas do cenário 3
Quadro R$ 120 · Actro R$ 400. Adotei **Quadro** — a Actro triplica a linha e cria um
degrau grande demais para um projeto residencial.

### D4 · A garantia do cenário 3
A tabela corrigida da casa cobre dois dos três: **telescópica = 2 anos · oculta Hardt =
5 anos**. **Falta o número da Hettich.** É o argumento mais forte dos três cenários —
ver o achado abaixo.

### D5 · Puxadores entram nos cenários?
Cava usinada, perfil Rometal (RM195 R$ 250/3m · RM213 R$ 100/3m) ou puxador aparente?
**Não está nos três cenários e pesa.**

---

## ⚠️ O ACHADO QUE MUDA O DISCURSO DE VENDA

Com a Blum fora, **a escada de ferragem estreitou muito**. Medido num exemplo
ilustrativo (40 dobradiças, 15 gavetas, 6 básculas, R$ 25.000 de custo direto sem
ferragem, igual nos três):

| Cenário | Custo da ferragem | Preço | Δ |
|---|--:|--:|--:|
| 1 · Telescópica | R$ 960 | R$ 54.065 | — |
| 2 · Hardt | R$ 1.550 | R$ 61.721 | +14% |
| 3 · Hettich | R$ 3.380 | R$ 74.653 | **+38%** |

Do primeiro ao terceiro, **a ferragem sobe R$ 2.420 de custo e o preço sobe R$ 20.587**.

> **88% da diferença entre o cenário mais barato e o mais caro é MARGEM. 12% é peça a
> mais.**

Isso não está errado — é a política de preço do Jonathan e ela é dele. Mas o cliente
que comparar as três colunas vai sentir um salto de 38% e perguntar o que mudou. **A
resposta não pode ser "é Hettich"**, porque em peça a diferença é pequena.

**A resposta tem de ser a garantia e o mecanismo:** 2 anos contra 5 anos contra o
número da Hettich; corrediça que corre por baixo e some contra trilho aparente;
amortecimento no corpo da dobradiça contra porta que bate. Por isso **D4 é a pergunta
mais importante desta lista** — sem o terceiro número de garantia, o terceiro cenário
não tem como se defender.

---

## E. Regra do ripado — MC 40%

O Jonathan definiu: **todas as partes com ripado a MC 40%** (divisor 0,40016),
independente do cenário.

| # | Pergunta |
|--:|---|
| E1 | **O ripado é linha separada no preço** (o cliente vê "ripado R$ X" à parte), ou é diluído no valor do móvel que o contém? |
| E2 | Nos cenários 1 e 2 o ripado sai **mais caro** que o resto do móvel (40% > 32% e > 37%); no cenário 3 sai **mais barato** (40% < 42%). **Confirma que é assim mesmo?** |

## F. Comercial

| # | Pergunta | Impacto |
|--:|---|---|
| F1 | **Tem RT para a arquiteta Luciana Beatriz Simplício?** | **A maior alavanca do orçamento.** Com RT 10% os divisores caem para 0,39216 / 0,34216 / 0,29216 — o cenário Hettich fica **30% mais caro**. Na Honda foi a primeira pergunta e a resposta mudou tudo. |
| F2 | **Situação de caixa** — define a MC mínima aceitável. | Piso da casa: 28%. Os três cenários já estão acima. |
| F3 | **Prazo de entrega.** | |
| F4 | **Condição de pagamento.** | Se for transferência/PIX, a taxa de cartão (~7,2%, dentro do `a = 0,162`) não é paga e a **margem real sobe ~7 pontos**. |
| F5 | **Validade da proposta.** | |

---

# PREMISSAS QUE VOU ADOTAR se não houver resposta

Adoto e **declaro na proposta** — assim nada fica escondido:

| | Premissa |
|---|---|
| Espessuras | **15 mm** caixaria · **18 mm** prateleiras, portas e frentes · **6 mm** fundos |
| Prateleira | vão livre acima de 70 cm → **18 mm** (anti-empeno) |
| Fundos | 6 mm com **duplo revestimento** |
| Fita | **0,4 mm** extra fina em todas as bordas aparentes |
| Interno | **branco**, exceto nicho aberto (interior aparente vai na cor) |
| Profundidades | cozinha inf. 60 · sup. 35 · roupeiro 65 · bancada 50 cm |
| Dobradiças | por altura de porta: até 90 cm = 2 · 90–160 = 3 · 160–200 = 4 |
| Logística | por ambiente — carretos + visitas técnicas + equipe de montagem |
| Consumíveis | 6% sobre chapa + fita |

---

# ARMADILHAS DESTE JOB — já mapeadas, para não repetir erro

| | Armadilha | Como evito |
|---|---|---|
| 1 | **Desenho raster.** A leitura será visual, não vetorial. | Pedir vetorial. Se não vier, declarar as cotas lidas e marcar as estimadas. |
| 2 | **Nesting subempacota.** | Dois empacotadores (faixa + best-fit) × 4 ordenações. Aproveitamento acima de ~75% numa chapa só → conferir à mão. |
| 3 | **Cor × espessura puxa chapa mínima.** | Testar consolidar espessura dentro da cor — no Honda economizou 2 chapas. |
| 4 | **Vidro/espelho por folha, não por m².** | Nunca usar os R$ da tabela como R$/m². |
| 5 | **Crédito de área ≠ crédito de chapa.** | Se um item sair do escopo, **re-rodar o nesting**, nunca estimar o delta por m². |
| 6 | **Visibilidade se decide por FACE, não por peça.** | A mesma chapa pode ter uma face contra a parede e a outra dentro de um nicho aberto. |
| 7 | **Sanidade: R$/m² de chapa.** | Faixa da casa: 626 (Rizzi) · 647 (aéreo cozinha) · 739 (SPE decorado) · 834 (Honda, job pequeno). Fora da faixa = investigar antes de entregar. |
| 8 | **Ripado é gargalo de fita.** | Na Rizzi foi 42% de toda a fita. Contar ripa a ripa, não por área. |

---

## O que ainda falta para eu começar o levantamento

**Os 7 PDFs no chat:** `PR 01` a `PR 05` COZINHA e `PR 06`/`PR 07` A. GOURMET.
É o único bloqueio que resta — as decisões de ferragem já estão quase todas fechadas.
Testei o leitor do Drive em quatro deles — **todos devolvem só o carimbo OCR-ado**,
inclusive os dois `PR 05`, que voltam idênticos porque a única coisa que o OCR pega é
o carimbo, que é igual nos dois. A diferença de conteúdo entre eles é real; eu é que
não a enxergo por esse caminho.
