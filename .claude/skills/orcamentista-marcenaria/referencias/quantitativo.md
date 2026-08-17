# Quantitativo de materiais — metodologia (em revisão)

> ⚠ **PRELIMINAR — aguardando explicação da Valvic.** Este documento registra
> os **artefatos reais** lidos (plano de corte e lista de materiais do projeto
> Maria – Vale dos Cristais). As **interpretações de metodologia** abaixo
> (especialmente "dois níveis" e a regra de estimativa) podem estar incorretas
> e serão corrigidas. Os *dados* são fiéis; as *conclusões*, não confirmadas.

## O cerne é a LISTA DE PEÇAS — extraída à mão (método tradicional)

> **Correção da Valvic:** a lista de peças **não sai de software**. Ela é tirada
> **manualmente**, do jeito tradicional da marcenaria — *"riscando na régua"*:
> olhando o projeto e **decompondo o móvel peça por peça**, definindo as
> dimensões (C × L) e a espessura de cada uma. **Essa é a habilidade central a
> destilar.** O software de plano de corte só entra **depois**, para encaixar
> (nesting) a lista já pronta nas chapas.

### Como a Valvic faz (a aprender em detalhe)

> 🟡 **A SER ENSINADO pela Valvic.** Registrar aqui o método de leitura do
> projeto e de quebra do móvel em peças (caixaria, fundos, frentes, prateleiras,
> gavetas...), as folgas, os critérios de dimensão e como se anota.

## Depois: o software faz o nesting (plano de corte)

Com a lista de peças pronta, o **otimizador de corte** encaixa as peças em
chapas de **2750 × 1850 mm** e devolve, por chapa:

- **Tipo / espessura / cor** (ex.: MDF Branco 15, Nuvem Matt 15mm, Nuvem Matt 6mm);
- **Qtd de peças** encaixadas e o layout do corte;
- **% utilizado** (aproveitamento) — varia de ~7% a ~92% por chapa;
- **Metros de filetamento** (fita de borda) daquela chapa.

O **nº de chapas** do projeto = nº de chapas que o nesting precisou. Exemplo
real (Maria – Vale dos Cristais, Ambiente 1, código 0ED321): **7 chapas MDF
Branco 15 + 4 chapas Nuvem Matt 15mm + 1 chapa Nuvem Matt 6mm = 12 chapas**.

### Taxonomia de peças (papel de cada peça no corte)

Cada peça carrega seu papel: `Função - Grupo - Módulo`. Vistos no plano de corte:

- **Estrutura:** Painel / Cabeceira, Lateral Direita/Esquerda, Base (passante),
  Batedor Topo (traseiro), Fundo.
- **Prateleiras:** Prateleira.
- **Gaveta:** Fundo interno, Contra-frente, Posterior, Lateral.

> Espessuras seguem o padrão Valvic (estrutura 15mm, fundos 6mm, etc. — ver
> `chapas.md`).

## Lista de materiais — auto-gerada a partir do corte

Do mesmo projeto sai a **lista de materiais/ferragens** (com códigos de SKU),
organizada por categoria. Exemplo real (Maria, Ambiente 1):

| Categoria        | Item                                           | Qtd      |
|------------------|------------------------------------------------|----------|
| MDF (chapas)     | MDF Branco 15                                  | 7 chapas |
|                  | Nuvem Matt 15mm                                | 4 chapas |
|                  | Nuvem Matt 6mm                                 | 1 chapa  |
| Fita             | Borda Branco TX 22×0,45 **+10% desperdício**   | 60 m     |
|                  | Fita Borda Nuvem Matt 22×0,45 **+10% desperdício** | 80 m |
| Corrediças       | Corrediça BLUM Invisível 500mm (amortecimento) | 6 pares  |
| Suporte prat.    | Suporte "queijinho" (PCT 100)                  | 1 pacote |
| Acessórios       | Cantoneira reforçada 3 furos c/ capa           | 16       |
| Parafusos        | 4×16mm / 4×40mm                                | 1 / 2 pct|
| Tapa-furo        | 12mm Branco Ártico TX / Nuvem Matt             | 7 / 4    |
| **Serviços**     | Filetamento                                    | 120,90 m |
|                  | Furação                                        | 388 furos|
|                  | Marcação                                       | 80       |
|                  | Rasgo                                          | 5,95 m   |
|                  | Peças cortadas                                 | 85       |
|                  | Embalagem                                      | 12       |

### Regras que isso revela

- **Fita de borda = metros de filetamento do nesting + 10% de desperdício**,
  na bitola **22 × 0,45 mm**, por cor de chapa.
- **Serviços de produção são quantificados** (filetamento em m, furação em
  nº de furos, marcação, rasgo, peças cortadas, embalagem) — alimentam o custo
  operacional / tempo de máquina.
- Ferragens vêm da **especificação do item** (no escopo), não do nesting.

## Dois níveis de quantitativo

| Momento     | Como conta as chapas                              | Onde            |
|-------------|---------------------------------------------------|-----------------|
| **Orçamento** | Estimativa (inclui frações: 0,5 chapa) p/ precificar rápido | `validacao-orcamento.md` (planilha) |
| **Produção**  | Exato, via plano de corte (nesting) em chapas inteiras + aproveitamento + filetamento | software de corte |

> O agente orçamentista deve produzir a **lista de peças** (cut list) a partir
> do projeto; o nesting converte em chapas. Para orçar rápido, estima por área/
> aproveitamento (a confirmar a regra de estimativa com a Valvic).

## Fluxo de documentos por projeto (Google Drive → CLIENTES VALVIC)

`Escopo de venda → Projeto 3D → Plano de corte → Lista de materiais →
Etiquetas → Registros de entrega`. Apps internos em `sistema_valvic/apps/`
(ex.: `Valvic_Escopo_Venda_App.html`) geram esses documentos.

## Calibração com projetos reais (Marcenária Diferente)

Aprendido com 2 projetos completos (`projetos/treino/`): modelo maior (cozinha,
17 chapas, cliente luiz) e modelo menor (aéreos+balcão, 6 chapas, cliente aline).

### Regras de estimativa de chapas

1. **Chapa = 2750 × 1850 mm** (área útil ~5,09 m²), sempre.
2. **Agrupar peças por cor × espessura.** Cada combinação consome suas próprias
   chapas.
3. **Aproveitamento real:** chapas "principais" de uma cor rendem **85–92%**.
   Mas há chapas de **cauda** (sobra de uma cor com poucas peças) que rendem
   **2–35%**.
4. **Cada cor distinta puxa ≥ 1 chapa**, mesmo para 1 peça só. ⇒ Projetos com
   **muitas cores** gastam mais chapa do que a área pura sugere.
5. **Estimativa prática:** por cor/espessura,
   `chapas ≈ arredonda_para_cima( Σ área das peças ÷ (5,09 m² × 0,85) )`,
   com **mínimo de 1 chapa por cor**. Para a chapa de cauda, não esperar bom
   aproveitamento.

### Fita de borda
- Calcular o **filetamento** (metros das faces que levam fita — regras em
  `laminacao-e-construcao.md`), por cor.
- A **fita-material é arredondada pra cima por cor** (ex.: 40/60/140 m), acima
  do filetamento e além dos +10% — margem de estoque. Usar múltiplos
  generosos por cor.

### Ferragens — proporções observadas
- **Corrediça oculta = 1 par por gaveta** (Hardt Invisível P-10, no comprimento
  da profundidade: 400/450/550mm).
- **Dobradiças:** ~2 por porta de giro; mix Reta/Curva c/ amortecedor + Reta
  comum (interno). Cozinha grande: 59; conjunto pequeno: 24.
- **Pistão a gás** (60–100N) por báscula/aéreo basculante.
- **Sistema Dominus** (correr): kit + trilho inferior RM-265 + superior RM-264
  (barras de 3m) + amortecedores.
- **Puxador cava:** medido em **metro** (usinado), pela extensão das frentes.
- **Suporte de prateleira:** VB Zamac Uniblock (furo 18mm), ~4 por prateleira.
- **Cantoneira reforçada 3 furos c/ capa** e **parafusos** (4×16/25/40mm) por
  módulo/montagem; **tapa-furo por cor**.

### Serviços de produção (sempre quantificados)
Filetamento (m), **Rasgo (m)** — sulco do fundo por encaixe —, Furação (nº de
furos), Marcação, Peças Cortadas, Embalagem. Úteis para dimensionar tempo de
máquina/operação.

> **Próximo passo de calibração:** comparar a estimativa manual do Marcos
> (a partir de medidas/render) com esses números reais e ajustar os fatores
> (aproveitamento por tipo, fita por gaveta/porta, furação por módulo).

---

## ⚠️ O empacotador guloso depende da ORDEM de entrada [07/08/2026]

O `nest()` que usamos nos scripts de corte é um empacotador **por faixas**
(shelf packing). Ele é guloso: a ordem em que as peças entram decide quantas
chapas saem. Ordenar só por **largura decrescente** — que era o padrão — pode
gastar uma chapa inteira à toa.

**Caso real** (armário superior de cozinha, 07/08): as 3 verticais de 50×50
ocupavam a primeira faixa e empurravam os tampos de 230 para outra chapa →
**3 chapas com 47%**. Empacotado à mão, tudo cabia em **2 chapas com 71%**.
R$ 250 de custo e R$ 555 de preço em cima de um artefato do algoritmo.

**Correção:** varrer várias ordens e ficar com a menor contagem.

```python
ordens = [lambda p: -p[1],            # largura decrescente
          lambda p: (-p[1], -p[0]),   # largura, depois comprimento
          lambda p: -p[0],            # comprimento decrescente
          lambda p: -p[0]*p[1]]       # área decrescente
chapas = min(_pack(sorted(base, key=k)) for k in ordens)
```

**Como ler o aproveitamento:**

| Sintoma | Leitura |
|---|---|
| < 50% com **muita área** | suspeitar do algoritmo — conferir à mão antes de aceitar |
| < 50% com **pouca área** | piso de 1 chapa por cor × espessura. Normal, não é desperdício |
| < 50% em **peça única multi-material** | pode ser o chão real (cristaleira: 36% verificado peça a peça) |

> A regra continua: **sub-50% é sintoma a investigar**, nunca resultado a aceitar.
> Mas a investigação agora começa pelo empacotador, não pelo móvel.

---

## ⚠️ Varrer ordens não bastou — o packer só olhava a ÚLTIMA faixa [Honda 07/08/2026]

A varredura de quatro ordens acima **não é suficiente**. O `_pack` por faixas só
tenta encaixar a peça na **última faixa aberta**. Quando entra uma peça larga no
meio da fila, ele abre faixa nova e **abandona toda a sobra das faixas
anteriores** — e nenhuma das quatro ordens conserta isso.

**Caso real** (Honda Minas Motos, MA-01): 3,98 m² de Amêndola 18 — **78% de UMA
chapa** — saía em 2 chapas nas quatro ordens. Empacotado à mão fecha em **1**,
usando 166 dos 185 cm:

```
faixa h=30 : 213×30 + 40×30           = 253 de 275
faixa h=30 : 213×30 + 40×30           = 253
faixa h=40 : 92×40 + 70×36 + 70×36    = 232
faixa h=36 : 92×30 + 92×30 + 69,5×36  = 253,5
faixa h=30 : 92×30 + 92×30 + 40×30×2  = 264      → 166 de 185 ✓
```

**Correção:** segundo empacotador **best-fit** — procura a melhor faixa já aberta
em **qualquer** chapa, não só a última. Rodar os dois, nas quatro ordens, e ficar
com o mínimo. Qualquer resultado continua sendo um plano de corte real (faixa
guilhotinada é como a serra opera), então baixar a contagem nunca é otimismo.

```python
def _pack_bf(pcs):
    ch = []                    # ch[i] = [altura_usada, [[alt_faixa, sobra_larg], ...]]
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch.append([CH_L, []]); continue
        best = None
        for s in ch:
            for fx in s[1]:
                if fx[0] >= l and fx[1] >= c and (best is None or fx[1] < best[1]):
                    best = fx
        if best is not None: best[1] -= c; continue
        for s in ch:
            if s[0] + l <= CH_L:
                s[0] += l; s[1].append([l, CH_C - c]); break
        else:
            ch.append([l, [[l, CH_C - c]]])
    return len(ch)

chapas = min(pk(sorted(base, key=k))
             for pk in (_pack_faixa, _pack_bf) for k in ordens)
```

No mesmo job o best-fit ainda derrubou o Branco 15 de 3 para 2 chapas (50% → 75%).
**Efeito total: 11 → 8 chapas, R$ 4.290 → R$ 3.030.**

### E o teste de sanidade que fecha a conta
Antes de aceitar qualquer contagem, olhar o **aproveitamento por cor × espessura**.
Acima de ~75% numa chapa só, desconfie de que o packer inventou a segunda —
empacote à mão. É rápido e já pegou dois casos.

---

## 💡 Consolidar espessura dentro da cor [Honda 07/08/2026]

Cada **cor × espessura** puxa no mínimo 1 chapa. Um móvel com 15 e 18 na mesma
cor paga **duas** chapas mínimas. Quando a área da cor é pequena, jogar tudo na
espessura maior costuma sair mais barato — e às vezes é tecnicamente melhor.

No Honda: Amêndola 15 (1,67 m², 33%) + Amêndola 18 (2,31 m², 45%) = 2 chapas,
R$ 1.100. Tudo em 18 → **1 chapa, R$ 600**. Mesma coisa no Palha (−R$ 500).
E no MA-01, caixaria de 18 mm ainda é **ganho estrutural** — é um aéreo de 3,15 m
em balanço com fixação invisível.

> Sempre testar a consolidação quando uma cor tiver **duas espessuras com pouca
> área**. Não vale quando isso empurra a chapa consolidada para uma chapa a mais —
> testar, não supor (no Honda, consolidar o Amêndola **antes** de corrigir o packer
> custava R$ 100 a mais).

---

## ⛔ Peça que não cabe na chapa [Eliuton 17/08/2026]

> **O empacotador não avisa. Ele obedece.** Se a peça é maior que 275 × 185, o
> `nest` abre **uma chapa por peça** e devolve um número que passa por plano de
> corte válido. Verificar SEMPRE antes de somar custo.

No Eliuton o painel ripado do estar/jantar tem **288 cm de altura** e a ripa
saiu inteira. 288 > 275: não cabe deitada nem em pé. O motor devolveu
**111 chapas de Nogueira Persa com 9% de aproveitamento** — e o relatório
imprimiu isso sem reclamar, como se fosse um plano de corte.

Depois de emendar a ripa em 2 trechos de 144 (a emenda cai na horizontal do
acabamento sobre a porta de correr): **10 chapas, 69% de aproveitamento**.
Diferença de R$ 60.600 no custo de chapa.

**Peça fora de chapa não é problema de empacotamento — é decisão de marcenaria:**
ou emenda, ou muda o desenho. Quem decide onde a emenda cai é quem desenha o
móvel, não o algoritmo.

### A guarda (copiar em todo motor novo)
```python
_fora = [(m, e, a, d, c, l) for m, e, a, d, c, l, q, r in P
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('PEÇAS QUE NÃO CABEM NA CHAPA DE 275 × 185 — corrigir antes de orçar')
    for m, e, a, d, c, l in _fora:
        print(f'  {m} {e} mm · {a} · {d}: {c:.0f} × {l:.0f} cm')
```
Roda **antes** de qualquer conta e imprime em destaque. No Eliuton pegou uma
segunda peça que eu não tinha visto: o rodapé da área de serviço, 359 cm.

### Onde isso morde
Altura de pé-direito. Painel de forro a piso, lateral de torre alta, costas de
armário até o teto — tudo que passa de 2,75 m. Num apartamento com pé-direito
de 2,60 nunca aparece; numa casa com forro a 2,88 aparece em todo painel.

---

## Quatro peças que NÃO existem [Eliuton 17/08/2026]

Auditoria depois que o Jonathan disse "os valores ficaram altos demais". Nove
erros; quatro eram chapa lançada a mais. Todos são erros de *desenho de móvel*,
não de conta — e todos passam despercebidos porque a peça "faz sentido".

### 1. Nicho de eletrodoméstico não leva fundo
Geladeira, forno, micro-ondas, cervejeira, máquina de lavar, secadora, lava-louças:
**o fundo é a alvenaria.** O aparelho precisa de ventilação, de folga de
dissipação e de tomada atrás. Fechar com MDF é erro de execução, não só de
orçamento.

No Eliuton eu tinha lançado fundo atrás da geladeira (2,81 m²), da torre de
cocção (1,93) e da cervejeira (1,49): **6,2 m² que não existem.**

### 2. O tampo de um módulo é a base do módulo de cima
Torre com nicho embaixo e armário em cima: a horizontal entre os dois é **uma
peça só**. Lançar "tampo do nicho" + "base do armário" duplica.

### 3. Onde a bancada é de PEDRA não há tampo de MDF
Bancada em mármore/granito/quartzo apoia em **base + travessa**, não em tampo
inteiro. Quem faz o tampo é a marmoraria. Vale para gabinete de banheiro,
lavabo, bancada de cozinha e de área de serviço.

> Sinal de alerta: se a prancha diz "BANCADA E RODABANCA EM MÁRMORE" e a lista
> de peças tem um tampo de MDF do mesmo tamanho, um dos dois está sobrando.

### 4. Fundo lançado duas vezes em caixote com face de vidro
Acontece quando a linha diz "laterais e fundo, 3 peças" e depois vem uma linha
"fundo" separada.

### O teste que pega os quatro
Somar a área do item e dividir pela **área frontal** do móvel. Faixa normal:
- móvel raso (aéreo, espelheira, 15–40 cm): **2 a 3×**
- móvel fundo (torre, bancada, roupeiro, 50–70 cm): **3 a 4,5×**

Acima de 4,5× num móvel fundo, procurar fundo de nicho de eletro e tampo
duplicado — foi exatamente onde estavam.
