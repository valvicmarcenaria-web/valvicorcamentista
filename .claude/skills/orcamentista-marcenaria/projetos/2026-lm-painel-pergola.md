# Orçamento — LM / SPE Nova Lima 1 (Painéis + Pérgola) — comercial

**Cliente:** SPE Nova Lima 1 · **Projeto:** arq. Lodi Motta / JBA Arquitetura · **Local:** Nova Lima–MG · **Etapa:** Executivo
**Pranchas:** MOB 01 (Painel Corretores/Pilar, R01) + MOB 02 (Painel/Pérgula Gourmet-Lounge, R00)
\+ **[07/08] MO 03 (Sala/Cozinha) · DET 05 (Quarto) · DET 06 (Suíte)** — o apartamento decorado.
**Acabamentos:** MDF Arauco Realce **Cravo Trend** (painéis/aparente) · **Moscada Matt** (móveis/caixa interna) · **MDF madeirado** (revestimento da pérgola + forro).

## Método
Cotas lidas do **vetor do CAD** (planta + elevações + cortes) — calcular, não estimar. Alturas de painel **2,62 m** (confirmado). `corte-lm.py`.

## PÉRGOLA (metalon #10×5) — exato
- Cadeia de cotas da planta: **28 faces de 8 cm** (17×12 + 9×13 + 1×14 de vão) → **28 ripas**; vão total 563 cm.
- Comprimento de cada ripa = projeção da pérgola = **309 cm**. 2×3,09 = 6,18 > 6 m → **1 barra por ripa**.
- **28 barras** de 6 m × R$ 150 + **R$ 150 frete dedicado** (1 entrega) = **R$ 4.350**.
- Revestimento das ripas em MDF madeirado (perfil acabado ~15×8): ~40 m².

## PAINÉIS (Cravo Trend) — parede a parede
**MOB 02:** E05 4,27 + Topo 2,946 + Copa 3,384 (2 portas + painel) + Corredor pérgola 5,63 + E03 1,42 + Hall 1,57 + IS frente 1,86 + retornos/faces IS 2,937 = **24,0 m × 2,62 = 62,9 m²**.
**MOB 01:** Corretor backdrop 8,175 × 3,85 (faixa 4×204,4 h=125 + STAND/caixa 260) ≈ 31,5 m² · Pilar 0,445 × 3,85 × ~2,5 faces ≈ 4,3 m².
\+ porta ripada (0,90×2,10) + armário gourmet exterior. **Total Cravo Trend ≈ 107,5 m² → 25 chapas (15 mm).**

## MÓVEIS (Moscada Matt)
- **Móvel Lounge:** 300 L × 60 A (40 corpo + 20 pé metálico) × 35 P — 2 nichos + 4 gavetas, sobre pés metálicos.
- **Armário Gourmet:** 97,5 L × 248 A × 42 P — ext. Cravo Trend, caixa/nicho Moscada; 2 portas 42,3 + nicho 85,5 + compart. 56.
→ Moscada ~6,2 m² (15) + 1,8 m² (6) → 3 chapas.

## RESUMO — chapas & custo
| Item | m² | Chapas | R$ |
|---|---|---|---|
| Cravo Trend 15 | 107,5 | 25 | 12.500 |
| Moscada 15 | 6,2 | 2 | 1.000 |
| Moscada 6 | 1,8 | 1 | 300 |
| MDF madeirado 15 | 45,8 | 11 | 5.500 |
| **Chapas** | | **39** | **19.300** |
| Metalon pérgola (28 barras + frete) | | | 4.350 |
| Terceiros (inox, pés, vidro jateado, sanca LED, moldura hidrante, poliestireno) | | | ~3.234 |
| Insumos (fita, cola/parafuso, usinagem) | | | ~6.660 |
| Visitas + logística | | | 1.350 |
| **CUSTO MATERIAL** | | | **≈ R$ 34.900** |

## Portas (destacadas na proposta) — CORRIGIDO
2 portas de **giro** na copa (+ painel entre elas) · 2 portas do **armário gourmet** (42,3) · 1 porta de **acesso ao QG** embutida no painel.
**FORA (terceiros, correção do Jonathan):** a porta com lâminas horizontais da Elev.2 é **veneziana** (não marcenaria Valvic); a portinhola 30×20 do pilar (*"vidro temperado c/ película jateada"*, acesso hidrante) é **vidraceiro**. Ambas removidas do escopo/preço.

## Corretor & Inox (esclarecimentos)
- **Corretores** = Painel Corretor (MOB 01): backdrop 8,17×3,85 em Cravo Trend — faixa sup. 4×204,4 (h=125) + **caixa em marcenaria** central recuada (h=260). Não é balcão.
- **Inox** = rodapé em perfil de **inox escovado 5×0,5, h=5cm** (DET.02), na base dos painéis. Serralheria (incluso, coordenado pela Valvic).

## Fechamento (confirmado): chapa R$ 500 · sem RT · MC 40% → **R$ 88.200**
*(era R$ 91.300; −R$ 3.100 ao remover veneziana + vidro jateado, ambos terceiros.)* Material R$ 33.694.
Breakdown: Painéis R$ 45.700 · **Pérgola R$ 18.000** · **Portas (giro+acesso) R$ 5.500** · Móveis + complementos R$ 19.000. Pagto 40/40/20 · prazo 45–60 úteis · garantia 2 anos.

## Preço (motor comercial) — sensibilidade
denom = 1 − 0,18 − 0,88·b − MC. **MC 40% · sem RT → R$ 91.300** · **MC 40% · RT 10% → R$ 118.600** · MC 43%/RT10 → R$ 132.100.

## FLAGS p/ travar a proposta
1. **Preço da chapa Arauco Realce** — usei base R$ 500/chapa (cor). Realce é linha premium; se ~R$ 700–900, o material sobe.
2. **RT** — projeto de escritório de arquitetura (Lodi Motta). Tem RT (10%)? Muda ~R$ 27 mil.
3. **MC** — recomendo 40% (piso caixa Rodrigo é 37%).
4. **Forro em gypsum** — assumido por conta do gesseiro (fora do escopo Valvic). Confirmar.
5. Espessura do painel de parede: assumi 15 mm.


---

# ESCOPO NOVO — APARTAMENTO DECORADO [07/08/2026]

Chegaram três pranchas **executivas** do Lodi Motta, R00 de 05–06/08/2026:

| Prancha | Conteúdo | Formato |
|---|---|---|
| **MO 03** | Mobiliário Sala / Cozinha — 4 elevações + 2 plantas | A2 79,3×42 |
| **DET 05** | Quarto — 4 elevações + planta, 9,00 m² | A2 59,4×42 |
| **DET 06** | Suíte — 3 elevações + planta | A2 59,4×42 |

**Não há sobreposição com a proposta vigente.** Os R$ 88.200 cobrem MOB 01 + MOB 02 —
painéis, pérgola e móveis das **áreas comerciais do stand**. Isto é o **apartamento
decorado**. É escopo somado, não revisado.

## Acabamentos (legenda das pranchas)
- **Sala/Cozinha e Suíte:** MDF Arauco **Anis Matt** + **Frapé Matt**
- **Quarto:** MDF **Ciliegio Poro** + **laca brilhante Sayerlack M072**
- **Rodapé sala/cozinha:** perfil de **inox escovado 5×0,5, h=5** (DET.02)
- **Rodapé quarto/suíte:** h=7
- **Puxador da cozinha:** perfil embutido 1,5+1,5, prof. 8 (DET.03) — é **cava**

## Quantitativo — `corte-spe-decorado.py`

| Material | Área | Chapas |
|---|--:|--:|
| Branco 15 · 18 · 6 (caixaria e fundos) | 100,9 m² | 29 |
| Anis Matt 15 · 18 | 25,6 m² | 8 |
| Frapé Matt 15 · 18 | 6,9 m² | 3 |
| Ciliegio Poro 15 · 18 | 12,6 m² | 5 |
| **Total** | **145,85 m²** | **45** · 64% |

Terceirizados **R$ 5.950,69** — espelho prata 5,34 m², laca Sayerlack 3,16 m²,
cabeceiras estofadas 3,64 m², rodapé inox 10,6 m, LED 9,9 m.
Ferragens **R$ 2.860,50** — 22 dobradiças, 8 articuladores, 3 conjuntos de correr,
8,95 m de cava.

**CUSTO DIRETO: R$ 37.808,82**

## Preço

### FECHADO [Jonathan 07/08]: **sem RT · MC 35%** · *"sem mexer nos valores na proposta inicial"*

Divisor 0,45016. Rateio por ambiente — chapa por área dentro de cada material,
fita e filetagem por área, **terceiros e ferragens atribuídos exatos**.

| Ambiente | Área | Custo direto | Investimento |
|---|--:|--:|--:|
| Cozinha | 54,5 m² | 11.671,12 | **25.900** |
| Sala | 19,2 m² | 6.306,83 | **14.000** |
| Quarto | 29,9 m² | 9.178,30 | **20.400** |
| Suíte | 42,2 m² | 10.652,57 | **23.700** |
| **Decorado** | **145,9 m²** | **37.808,82** | **84.000** |

MC conferida **35,0%**.

| | |
|---|--:|
| Stand — MOB 01 + MOB 02 · **inalterado** | R$ 88.200 |
| Decorado — MO 03 + DET 05 + DET 06 | R$ 84.000 |
| **TOTAL** | **R$ 172.200** |

Escada: −3% 167.000 · −5% 163.600 · −7% **160.100**.

> ⚠️ **O contrato passa a ter duas margens.** O stand fechou a **40%**, o decorado
> sai a **35%**. A MC combinada fica em **~37,6%** — ainda na faixa boa. Mas se a
> negociação puxar desconto sobre o total, ela corrói a etapa nova, não a antiga.

O decorado quase empata com o stand — quatro ambientes mobiliados contra
painelaria e pérgola.

## Proposta — `build-spe-nova-lima.py` → `proposta-spe-nova-lima.pdf`

4 páginas no layout premium da casa: capa · **o que muda** (duas caixas opondo
contratado × entra agora, mais o decorado em números) · os quatro ambientes ·
investimento com o stand em faixa cinza marcado *"valor inalterado"*.

Condições: **60 a 75 dias úteis** para o decorado, a alinhar com a inauguração do
stand · garantia **2 anos** (mesma da etapa contratada) · validade 7 dias.
⚠️ O prazo é assumido por mim, não ditado.

## ⚠️ Flags
1. **Chapa Arauco MATT** — usei a base "cor" (R$ 500/580). Matt é linha premium;
   a R$ 800/chapa o custo sobe ~R$ 11.250 e o preço ~R$ 28.100. **É o maior risco
   aberto**, e é o mesmo flag que ficou pendente na proposta vigente.
2. **RT** — projeto do Lodi Motta. Se houver, o decorado vai de 94.500 para 121.100.
3. **Interno branco assumido** — as pranchas só especificam o acabamento aparente.
4. **Fita pelo fator 2,6 m/m²**, não apurada peça a peça.
5. **Divisão interna dos módulos** lida das elevações; as plantas cotam o
   desenvolvimento, não a divisão de gavetas.
6. **Fora do escopo:** caixa de gypsum, pintura, cortinas, tapetes, eletros,
   bancadas de pedra.


---

# ⚠️ AUDITORIA DO DECORADO — o Jonathan achou os valores baixos [07/08]

> *"estou achando os valores bem abaixo do real. vc considerou tudo, estofados,
> portas de espelho, sistema etc?"*

Estava. Quatro furos, e o primeiro é grosseiro.

| # | Erro | Delta |
|---|---|--:|
| 1 | **Portas de espelho orçadas como painel de MDF.** Os roupeiros do quarto e da suíte têm portas de correr com hachura de espelho na elevação — e o render do quarto mostra o reflexo. `ferragens.md` é explícito: terceirizadas, ~R$ 1.200 + R$ 200 de frete. Eu tinha R$ 1.012 de chapa onde vão R$ 5.200. | **+4.188** |
| 2 | **Sistema de correr a R$ 250.** Peguei "Sistema roupeiro 250" da planilha em vez do **Dominus** (R$ 1.840 o kit de 2 portas), que é o padrão da casa. | **+3.630** |
| 3 | **LED curto** — contei 9,9 m; são **16,7 m** (dois cortineiros, torre de 5 nichos da suíte, nichos do quarto, fita da cozinha). | **+888** |
| 4 | Estofado a R$ 450/m² — **Jonathan cravou: mantém 450**, é o custo da base. | 0 |
| — | Chapa Arauco Matt — **Jonathan confirmou: o preço está certo.** Flag fechado. | 0 |

**Custo direto: R$ 37.808,82 → R$ 46.515,04.**
Decorado a MC 35% sem RT: **R$ 84.000 → R$ 103.300.** Total **R$ 191.500**.

## O teste que faltou

**R$ por chapa** — a métrica que denuncia orçamento raso:

| | R$/chapa |
|---|--:|
| Decorado (1ª versão) | 1.867 |
| Cozinha Rizzi (residencial) | 2.005 |
| Stand SPE (fechado) | 2.262 |
| **Decorado corrigido** | **2.296** |

Um decorado com espelhos, laca, estofado e quatro acabamentos saindo **mais barato
por chapa que uma cozinha residencial** não fechava. Rodar essa razão contra jobs
comparáveis antes de entregar teria pego os quatro furos.

## ⚠️ ABERTO — espelho da ELEVAÇÃO 03

Painel de 1,90 × 2,40 (4,56 m²) + 4 nichos de 0,39 × 0,50 = **5,34 m²**.
Estão no orçamento a **R$ 285/m²** — mas os 285 vêm da tabela *"Espelho Prata ·
com perfil"* de `chapas.md`, onde **a unidade é FOLHA**, não metro quadrado.

| R$/m² | Custo direto | Decorado | Total |
|--:|--:|--:|--:|
| 285 *(hoje)* | 46.515 | 103.300 | 191.500 |
| 450 | 47.396 | 105.300 | 193.500 |
| 630 | 48.357 | 107.400 | 195.600 |
| 800 | 49.265 | 109.400 | 197.600 |

### ✅ FECHADO em R$ 191.500 [Jonathan 07/08]

> ⛔ **NADA FOI CONTRATADO AINDA.** [Jonathan 07/08] A primeira versão de 17/07
> foi *apresentada*, não assinada. A moldura "contratado + adição" que eu tinha
> usado estava errada — não existe etapa fechada. É **uma proposta só**, com oito
> frentes. Corrigido em `build-spe-nova-lima.py`.

> **Layout:** o mesmo da primeira versão (`build-lm.py`, 17/07) — editorial claro,
> capa creme com moldura dourada, blocos com filete, tabela de frentes, hero do
> investimento. O build **lê o CSS direto do `build-lm.py`**, então os dois nunca
> divergem. 4 páginas: capa · escopo do stand · escopo do decorado · investimento.

Espelho da E03 **mantido a R$ 285/m²**. Emitida `proposta-spe-nova-lima.pdf`.

| Etapa | Custo direto | Investimento |
|---|--:|--:|
| Stand — MOB 01 + MOB 02 · *inalterado* | — | **88.200** |
| Cozinha | 11.379,56 | 25.800 |
| Sala | 6.971,85 | 15.800 |
| Quarto | 13.230,71 | 30.000 |
| Suíte | 13.971,37 | 31.700 |
| **Decorado** | **45.553,49** | **103.300** |
| **TOTAL** | | **R$ 191.500** |

Escada: −3% 185.800 · −5% 181.900 · −7% **178.100**.

> ⚠️ **A MC do decorado ficou em 35,9%, não 35,0%.** Ao tirar as portas de espelho
> da lista de MDF, o re-nesting caiu de 145,9 para **137,0 m²** e derrubaram
> chapas inteiras — o custo caiu **R$ 962** a mais do que meu crédito à mão previa.
> A MC 35% exata daria R$ 101.200 (total 189.400). Segurando o valor autorizado,
> ganhamos 0,9 ponto. **MC combinada do contrato: ~38,1%.**

### APRENDIZADO — crédito de área ≠ crédito de chapa
Quando um item sai do plano de corte, creditar só a **área** subestima a economia:
o nesting pode derrubar **chapas inteiras**. Vale para os dois lados — foi o mesmo
efeito que fez a bancada da cozinha Rizzi economizar menos do que a linha rateada
sugeria. **Sempre re-rodar o nesting, nunca estimar o delta por m².**

---

# ✅ VERSÃO FINAL — MC 35% exata no decorado · garantia 5 anos [07/08/2026]

> *"vamos elevar a MC para 35% e dar 5 anos de garantia."* — Jonathan
> *"sempre mantendo os valores do orçamento inicial do Stand de vendas"* — Jonathan

## A ambiguidade que a segunda mensagem resolveu

"Elevar a MC para 35%" não podia significar *elevar* nada: o stand estava em **40%**
e o decorado em **35,9%**. Aplicar 35% no contrato inteiro **derrubaria** o total em
R$ 11.900. A segunda mensagem travou a leitura correta: **stand congelado, MC 35% só
no decorado.**

## Preço

| Frente | Custo direto | Investimento |
|---|--:|--:|
| Painéis — Cravo Trend (Gourmet/Lounge + Corretores + Pilar) | — | 45.700 |
| Pérgola — 28 ripas metalon #10×5 revestido | — | 18.000 |
| Portas — giro (copa + armário) + acesso ao QG | — | 5.500 |
| Móveis + complementos — armário gourmet, móvel lounge, sanca, inox | — | 19.000 |
| **Stand — MOB 01 + MOB 02 · MC 40% · congelado** | **33.694** | **88.200** |
| Cozinha do decorado | 11.379,56 | 25.300 |
| Sala do decorado | 6.971,85 | 15.500 |
| Quarto do decorado | 13.230,71 | 29.400 |
| Suíte do decorado | 13.971,37 | 31.000 |
| **Decorado — MC 35,0% exata** | **45.553,49** | **101.200** |
| **TOTAL** | **79.247** | **R$ 189.400** |

**MC combinada do contrato: 37,3%** *(média ponderada por receita: 88.200 a 40% +
101.200 a 35%)*. Bem acima do piso de caixa do Rodrigo (37%) e no meio da faixa
saudável.

Escada: −3% 183.700 · −5% 179.900 · −7% **176.100**. No pior degrau a MC do decorado
ainda fica em **31,6%** — acima do piso de 28%.

> **R$ 2.100 abaixo dos R$ 191.500 antes autorizados.** Não é perda: os 103.300
> nunca foram alvo, eram o **resíduo de segurar o número redondo**, o que deixava a
> MC em 35,9%. Pedida a MC 35% exata, o decorado é 101.200 por construção.

## Garantia — 5 anos

Coerente com a tabela corrigida da casa (`proposta-comercial.md`): **corrediça oculta
Hardt = 5 anos**. O decorado usa oculta. O stand é painelaria e pérgola — quase não
tem ferragem móvel, então 5 anos não cria exposição nova ali.

## Layout
O mesmo da primeira versão (`build-lm.py`, 17/07). O build **lê o CSS direto do
`build-lm.py`** via regex, então os dois nunca divergem. 4 páginas: capa · escopo do
stand · escopo do decorado · investimento. Prazo 60–75 dias úteis · 40/40/20 ·
validade 15 dias.

Emitida `proposta-spe-nova-lima.pdf` (4 páginas, verificada).

### APRENDIZADO — unidade de tabela
`chapas.md` cota vidro e espelho **por folha**; `validacao-orcamento.md` cota
**por unidade**. Nenhuma das duas é por m². Usar esses números como R$/m² em
painelaria subestima sempre.

---

## 🔁 21/08/2026 — DUAS PRANCHAS NOVAS NO DECORADO

O Jonathan mandou acrescentar dois ambientes ao escopo:

| Prancha | Ambiente | Emissão | Acabamento |
|---|---|---|---|
| **DET 07** | Armário 1 — **COPA** | R00 · 07/08/2026 | MDF Arauco **Frapé Matt** (cravado) |
| **DET 02** | **ILHA GOURMET** | R00 · 22/07/2026 | ⚠ não legendado — adotei Frapé |

As duas são **caso A** (têm camada de texto: 175 e 311 palavras). Lidas pelo
conector e conferidas no render.

### ⛔ Não foi somar duas linhas

Rodei o motor inteiro com `EXCLUIR` desligado e os dois ambientes novos dentro.
**Os quatro ambientes que já existiam mudaram de preço:**

| Ambiente | Antes | Depois |
|---|--:|--:|
| Cozinha | 25.300 | **24.700** |
| Sala | 15.500 | **15.800** |
| Quarto | 29.400 | **29.800** |
| Suíte | 31.000 | **30.300** |
| Copa *(novo)* | — | **6.200** |
| Ilha gourmet *(novo)* | — | **9.000** |
| **DECORADO** | 101.200 | **115.800** |
| Stand *(intocado)* | 88.200 | 88.200 |
| **TOTAL** | 189.400 | **R$ 204.000** |

**A cozinha CAIU.** Duas forças em sentidos opostos: a chapa Frapé passou a
render mais — a copa e a ilha preenchem sobra que a cozinha pagava sozinha — e a
logística subiu com a área (137,0 → 167,5 m² de chapa, 4 → 6 ambientes). Na
cozinha o ganho de nesting venceu; nos outros três, a logística.

MC do decorado mantida em **35,0% exata**. MC combinada do contrato: **37,2%**.

### ⛔ Dívida técnica que NÃO corrigi — e que o Jonathan precisa decidir

Este motor é de 07/08 e ainda lança **INSTALAÇÃO como custo direto**
(R$ 7.947 no escopo novo). A regra da casa, cravada em 17/08 no Eliuton, é que
**montagem não entra no custo** — a equipe é salário fixo e a comissão já está
no divisor.

Mantive a convenção do motor por duas razões: não misturar dois critérios dentro
do **mesmo** orçamento, e porque a proposta vigente de R$ 189.400 já foi entregue
nela.

> **Se aplicar a regra, o decorado cai de R$ 115.800 para ~R$ 98.100** — R$ 17.700
> a menos. E a parte do stand também teria de ser refeita, porque saiu na mesma
> convenção. É a mesma correção que pegou a Honda.

### O que ficou fora dos dois ambientes novos

- **Bancada e rodabanca da copa** — pedra, marmoraria.
- **Bancada da ilha** — "pedra a definir", marmoraria.
- **Cuba 50×40×20 e torneira monocomando Tramontina** — louça e metal do cliente.
- **Adega Duo Maxi Crissair** (770 × 870 × 575) — equipamento do cliente; fazemos
  o nicho ventilado.

### Uma nota de leitura sobre a ilha

Móvel de ilha **aparece pelos quatro lados**: não existe face de fundo barata,
tudo é frente. São 18,4 m² de chapa para 3,40 × 0,90 m — proporcionalmente mais
que qualquer armário encostado na parede do projeto. Está no preço.
