# ELIUTON · Brisas da Pampulha — LEVANTAMENTO DE DÚVIDAS TÉCNICAS

**Data:** 13/08/2026 · **Antes do levantamento**, como pedido pelo Jonathan:
*"gere todo o levantamento de dúvidas técnicas antes para não cometermos erros."*

Cada pergunta aqui **muda um número**. Não há pergunta de curiosidade nesta lista —
onde eu souber responder sozinha, respondi e marquei como premissa.

---

# 🔄 17/08/2026 — O PROJETO CHEGOU. O QUE AS PRANCHAS RESPONDERAM

Os 19 PDFs subiram no chat e foram lidos vetorialmente. Levantamento e preço em
`corte-eliuton.py`; leitura e números em `2026-eliuton-brisas-da-pampulha.md`.

## ✅ Respondido pelo desenho — não precisa perguntar

| # | Resposta |
|--:|---|
| A1 | **12 conjuntos de marcenaria**: cozinha (torre, bancada 01, aéreo, ilha, acabamento), painel ripado do estar/jantar, gourmet (bancada 02 + cervejeira), área de serviço, lavabo externo e 3 banheiros. O **social térreo não tem marcenaria** — é todo mármore. |
| A2 | **As bancadas são de pedra.** Carrara e Travertino, em todo ambiente. Fora do nosso custo — mas *quem fornece* ainda é pergunta (ver abaixo). |
| A3 | Louças e metais **Deca**, especificados peça a peça. Não fornecemos. |
| A5 | **Existe ripado** e existe **acabamento de forro em MDF** (lavabo externo, 130 × 40). |
| A7 | **Área de serviço tem sim** — e é o 2º maior conjunto do job: 359 × 55 × 226, com nichos de máquina e secadora, 2 varais retráteis, 2 gavetões e tábua de passar embutida. |
| B1 | **MDF ARAUCO 18 mm** em quatro acabamentos: **Nogueira Persa** (dominante) · **Sálvia** (só a cozinha) · **Jequitibá** (só o master) · **Beige** (só 4 prateleiras do banheiro 02). |
| B2 | **Interno na cor.** As perspectivas de armário aberto mostram o interior todo na cor. |
| B6 | **Espelhos:** portas espelhadas de correr no master (3 folhas), banheiro 02 (2) e banheiro 04 (2). **Vidro:** 2 portas basculantes do gourmet, com estrutura em metal fendi. |
| C3 | **Pé-direito 308, forro rebaixado 288** na cozinha; 240 na área de serviço; 270 nos banheiros. |
| C5 | ⚠️ **As pranchas SEMPRE foram vetoriais.** O que engana é que o texto foi convertido em curvas — daí zero palavras extraíveis e o conector do Drive só devolver o carimbo OCR-ado. Diagnóstico de 13/08 corrigido. |

## ❓ O que o desenho NÃO resolve — e continua valendo dinheiro

| # | Pergunta | Impacto |
|--:|---|--:|
| **B1b** | **Preço de compra da linha Arauco madeirada.** Nogueira Persa e Jequitibá não têm preço fechado na base — o `corte-lm.py` deixou "ver FLAG premium" e nunca preencheu. | **±R$ 58.100** no preço. **É o item nº 1.** |
| **B3b** | **Passo do ripado.** A 1:25 uma ripa de 4 cm dá 1,6 mm no papel — não dá para ler. Premissa: régua 4,0 + espaçamento 1,5. | muda ripa a ripa e a fita |
| **B3c** | A prancha diz "painel **parte ripado parte liso**" mas a elevação mostra tudo ripado. **Qual é?** | o painel é 17% da chapa e 53% da fita |
| **A2b** | **A Valvic fornece o mármore ou não?** | escopo inteiro à parte |
| **C4** | **Falta a folha 02/10** — detalhe da área de serviço. É ela que diz se as portas do topo são de abrir ou basculantes. | báscula de 113 cm não é HK-xs, é **Aventos**: R$ 600 vs 250 |
| **A4** | **Medidas exatas dos eletros.** As pranchas dão o vão, não o aparelho. Geladeira 103, cervejeira 70, forno e micro em nicho de 58 e 40. | vão errado = chapa refeita |
| **F1** | **RT para a arquiteta.** | **+24% a +30%** — segue a maior alavanca isolada |
| **D5** | **Puxadores.** O projeto pede "puxador tipo cava" 50 vezes. Adotei **cava usinada R$ 50/peça**. | R$ 2.500 de custo, R$ 5.800 de preço |
| **F2–F5** | Caixa, prazo, pagamento, validade. | |

**Nova, que só apareceu com o desenho na mão:** os **22 dias de dupla + 5 carretos
+ 4 visitas (R$ 17.200)** são estimativa minha e valem **28% do custo direto**.
Não há na base um job desse porte para calibrar. **O Jonathan precisa cravar.**

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

## D. Os três cenários — FECHADOS [Jonathan 13/08]

**Telescópica 32% · Hardt 37% · Hettich 42%.** Blum fora como linha, **mas as básculas
dos cenários 2 e 3 são Blum HK-xs a R$ 250**.

| | 1 · **Telescópica** | 2 · **Hardt** | 3 · **Hettich** |
|---|---|---|---|
| **MC** | **32%** · div 0,48016 | **37%** · div 0,43016 | **42%** · div 0,38016 |
| Dobradiça | Padrão · R$ 6 | Hardt · R$ 8 | ✅ **Novisys · R$ 10** |
| Corrediça | Telescópica · R$ 40/par | Oculta Hardt · R$ 70/par | ✅ **Oculta Quadro · R$ 120/par** |
| Báscula | Pistão simples · R$ 20 | ✅ **Blum HK-xs · R$ 250** | ✅ **Blum HK-xs · R$ 250** |
| **Garantia** | **2 anos** | **5 anos** | ✅ **10 anos** |

✅ **Os três cenários estão fechados.** Só falta D5 (puxadores).

### ✅ D1 · A escada de garantia fecha em 2 · 5 · 10 — e **dobra a cada degrau**
Era a pergunta mais importante da lista e agora tem resposta. **É isso que sustenta
comercialmente a escada de preço**, porque a diferença de *peça* entre os cenários é
pequena perto da diferença de *preço* (ver o achado abaixo). Registrado como tabela da
casa em `referencias/ferragens.md`.

### ✅ D2 · Blum como linha — fora. D3 · Corrediça do cenário 3 — **Quadro**.

### ✅ D4 · Dobradiça do cenário 3 — **NOVISYS** [Jonathan 13/08]
Eu tinha recomendado Sensys; o Jonathan escolheu **Novisys R$ 10**. Decisão dele.

**Consequência, registrada uma vez:** entre os cenários 2 e 3 a ferragem quase não
muda — báscula **idêntica** (HK-xs nos dois), dobradiça 8 → 10 (**1,25×**), e só a
corrediça sobe de verdade (70 → 120, **1,7×**). No exemplo ilustrativo isso dá
**+R$ 830 de ferragem contra +R$ 10.705 de preço — 92% de margem** entre o 2º e o 3º.

⇒ **O 3º cenário se defende pela garantia (10 anos) e pela corrediça oculta Quadro**,
não pelo nome Hettich na dobradiça. Na conversa de venda, é a corrediça que ele tem de
abrir e fechar, e é a garantia que ele leva escrita.

### ❓ D5 · Puxadores entram nos cenários?
Cava usinada, perfil Rometal (RM195 R$ 250/3m · RM213 R$ 100/3m) ou aparente?
**Não está em nenhum dos três e pesa.**

### Preço atualizado na base
**Blum HK-xs: R$ 180 → R$ 250.** `dados/materiais.json` corrigido.

---

## ⚠️ DOIS ACHADOS DA ESCADA DE FERRAGEM

Exemplo ilustrativo — 40 dobradiças, 15 gavetas, 6 básculas, R$ 25.000 de custo direto
sem ferragem, igual nos três:

| Cenário | Ferragem | Preço | Δ | Garantia |
|---|--:|--:|--:|--:|
| 1 · Telescópica | R$ 960 | R$ 54.065 | — | 2 anos |
| 2 · Hardt | R$ 2.870 | R$ 64.790 | +20% | 5 anos |
| 3 · Hettich | R$ 3.700 | R$ 75.495 | **+40%** | 10 anos |

### 1 · **84% da diferença de preço é margem, 16% é peça a mais**
Do primeiro ao terceiro a ferragem sobe R$ 2.740 de custo e o preço sobe R$ 21.429
(**87% margem**). Entre o 2º e o 3º isoladamente, **92%**.
Não está errado — é a política de preço da casa. Mas o cliente que comparar as três
colunas vai sentir o salto de 45% e perguntar o que mudou, e **a resposta tem de ser a
garantia (2 · 5 · 10) e o mecanismo**, não o nome do fabricante. Com o HK-xs entrando
nos cenários 2 e 3, a parcela de peça subiu de 12% para 13% — ajudou pouco, e com a
Novisys no lugar da Sensys o desenho voltou a apertar.

### 2 · **A báscula virou a quantidade mais sensível do orçamento**

| | Cenário 1 | Cenário 2 | × | Cenário 3 | × |
|---|--:|--:|--:|--:|--:|
| Dobradiça | 6 | 8 | 1,3× | 10 | 1,2× |
| Corrediça | 40 | 70 | 1,8× | 120 | 1,7× |
| **Báscula** | **20** | **250** | **12,5×** | **250** | **1,0×** |

A báscula **salta 12,5× do 1º para o 2º e depois não muda**. Duas consequências:

- **Cenários 2 e 3 têm a MESMA báscula e quase a mesma dobradiça.** Entre eles sobra
  **só a corrediça** (oculta Hardt → oculta Quadro). É o único mecanismo que o cliente
  consegue sentir de um cenário para o outro.
- **Cada báscula vale mais que 30 dobradiças.** Ela pesa **52%** da ferragem do
  cenário 2 e **32%** do cenário 3. ⇒ **Contar báscula a báscula nas pranchas, nunca
  estimar.** Errar duas básculas custa R$ 500 de custo direto e ~R$ 1.300 de preço.

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
| 1 | ~~**Desenho raster.**~~ **ERA VETORIAL O TEMPO TODO** [17/08]. O texto é que foi convertido em curvas. Aferi a escala no próprio desenho (a porta 80×210 mediu 80,0 × 210,0) e medi o painel ripado na geometria: 570,6 × 287,5. | **Nunca concluir "raster" só porque não sai texto.** Abrir o PDF e contar os vetores: 25.703 traços na folha 01/08. |
| 1b | **Peça maior que a chapa.** A ripa de 288 cm não cabe em 275 × 185 — e o `nest` devolveu 111 chapas a 9% sem reclamar. | Guarda de peça fora de chapa **antes** de qualquer conta. Ver `quantitativo.md`. |
| 1c | **Nome de arquivo mente.** `PR 05_COZINHA` é a folha 08/08 (gourmet). | **Ler o carimbo, sempre.** Foi o que o Jonathan já tinha dito. |
| 2 | **Nesting subempacota.** | Dois empacotadores (faixa + best-fit) × 4 ordenações. Aproveitamento acima de ~75% numa chapa só → conferir à mão. |
| 3 | **Cor × espessura puxa chapa mínima.** | Testar consolidar espessura dentro da cor — no Honda economizou 2 chapas. |
| 4 | **Vidro/espelho por folha, não por m².** | Nunca usar os R$ da tabela como R$/m². |
| 5 | **Crédito de área ≠ crédito de chapa.** | Se um item sair do escopo, **re-rodar o nesting**, nunca estimar o delta por m². |
| 6 | **Visibilidade se decide por FACE, não por peça.** | A mesma chapa pode ter uma face contra a parede e a outra dentro de um nicho aberto. |
| 7 | **Sanidade: R$/m² de chapa.** | Faixa da casa: 626 (Rizzi) · 647 (aéreo cozinha) · 739 (SPE decorado) · 834 (Honda, job pequeno) · **846 (Eliuton)**. O Eliuton fica no topo da faixa apesar de ser job grande porque **logística (28%) e terceirizados (15%) pesam mais que a chapa (39%)** — é casa inteira, 3 pavimentos, 12 conjuntos. Se o Jonathan cravar menos dias de montagem, esse número cai. |
| 8 | **Ripado é gargalo de fita.** | Na Rizzi foi 42% de toda a fita. Contar ripa a ripa, não por área. |

---

## ~~O que ainda falta para eu começar o levantamento~~ — RESOLVIDO 17/08

Os 19 PDFs subiram no chat e o levantamento está feito: **169,93 m² de chapa ·
49 chapas · R$ 126.400 / 143.800 / 162.500** nos três cenários.

**A fila agora é outra**, e por ordem de dinheiro:

1. **Preço da chapa Arauco madeirada** (±R$ 58.100) — uma ligação ao fornecedor.
2. **A Valvic fornece o mármore?** — escopo inteiro à parte.
3. **RT para a arquiteta** (+24% a +30%).
4. **Dias de montagem** — R$ 17.200 são estimativa minha, 28% do custo direto.
5. **Folha 02/10** e o passo do ripado — os dois últimos buracos de desenho.
