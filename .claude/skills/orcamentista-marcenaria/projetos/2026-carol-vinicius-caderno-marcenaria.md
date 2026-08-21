# CAROL E VINÍCIUS — Caderno de Marcenaria

**Cliente:** Carol e Vinícius Ramalho
**Projeto:** Jéssica Sollero Design de Interiores — jessicasollerointeriores@gmail.com · 31-98406.0172
**Data da prancha:** 20 de julho de 2026 · escala 1:25 · **49 pranchas**
**Levantamento:** Lavinia, 18/08/2026 · `projetos/corte-vinicius.py`
**Entregáveis:**
`projetos/apresentacao-vinicius.pdf` — apresentação premium, A4 paisagem,
16 páginas, no padrão do caderno do Junior (Lagoa Santa), com as 15
perspectivas do projeto · `projetos/proposta-vinicius.pdf` — proposta A4
retrato, 8 páginas, versão técnica
**Carimbo em todas as folhas:** "CONFERIR MEDIDAS NO LOCAL"

---

## 🔁 21/08/2026 — REVISÃO DO JONATHAN

### O erro que ele pegou: a sala de estar, lida errada duas vezes

> *"o painel ripado não é do rodapé ao forro, segunda leitura errada no mesmo
> projeto, considere apenas a cota visível do projeto. Os armários tbm não têm
> frentes ripadas, as colunas tbm não são abertas."*

Eu tinha lançado o painel da elevação B como **quase tudo ripado**: o painel da
TV inteiro, as seis portas do armário superior e as colunas laterais abertas.
As duas perspectivas do próprio caderno desmentem as três coisas:

| Perspectiva | O que mostra |
|---|---|
| `img-vinicius/estar-3.jpg` — **fechada** | painel de MDF Areal **liso**; as linhas verticais são junta de porta, não ripa |
| `img-vinicius/estar-4.jpg` — **aberta** | as colunas **têm porta** — é a foto aberta que revela as prateleiras brancas |

O **único ripado do ambiente** é a faixa sob o televisor, na cota de 30 que a
elevação traz. Correção aplicada:

| | Antes | Depois |
|---|--:|--:|
| Ripado da sala de estar | 5,73 m² | **0,68 m²** |
| Ripado do projeto | 6,68 m² | **1,97 m²** |
| Dobradiças da sala de estar | 12 | **16** (as colunas ganharam porta) |

> 🧠 **A lição, para o moleskine.** Perspectiva **fechada** e perspectiva
> **aberta** do mesmo móvel são dois **estados**, não duas vistas complementares.
> Ler só a fechada faz junta de porta virar ripa; ler só a aberta faz porta
> virar nicho. **Quando existem as duas, as duas têm de ser lidas antes de
> lançar a geometria** — e é a fechada que define o que o cliente vê.

### As outras quatro correções

| # | O que mudou |
|--:|---|
| 1 | **Prazo**: de "90 a 120 dias" para **até 90 dias corridos**. |
| 2 | **Lavabo**: sai a frase "do teto à bancada" — o ripado não tem essa extensão. |
| 3 | **Varanda**: a bancada curva fica, agora com nota de **estruturação especial coordenada** (reforço embutido no tampo + pés em tubo champagne, dimensionados com a serralheria). |
| 4 | **Quarto Maria Luísa**: as portas de espelho prata do armário existente **saem do escopo**. Fica só o envelopamento em MDF Frapê — montantes, testeira e base. Saem 3 portas, 9 dobradiças e 3 folhas de espelho (R$ 855). |

### A Telescópica sai; entra um upgrade de projeto

> *"vamos tirar a telescópica de cena. em vez disso apresentar um upgrade de
> projeto mudando a cor da estrutura interna para a mesma cor da estrutura
> externa."*

O terceiro degrau da proposta **deixa de ser ferragem e passa a ser acabamento**.
Comercialmente é melhor: a Telescópica competia para baixo, e o upgrade compete
para cima.

O motor ganhou o mecanismo: a caixaria interna passa a ser lançada como
`I:AR` / `I:FR` — *interior de um módulo Areal ou Frapê*. Com `INTERNO_COR=False`
resolve para Branco TX (o que a prancha pede); com `True`, resolve para a cor do
próprio módulo. **Muda também o nesting**: o interior deixa de dividir chapa
branca com todo mundo e passa a dividir chapa colorida com a frente do seu móvel.

⚠ A **caixa da gaveta fica em Branco TX nos dois casos**. Interior na cor é o que
se vê ao *abrir a porta*; caixa de gaveta em branco é padrão mesmo em projeto
premium, e trocá-la encareceria sem aparecer. Está escrito na proposta.

### Os números novos — COM RT, escada 35/38

| | 5 anos (Hardt) | 10 anos (Hettich) |
|---|--:|--:|
| Investimento | **R$ 170.200** | **R$ 191.700** |
| + Upgrade · interior na cor | + R$ 9.800 | + R$ 10.800 |
| **Com o upgrade** | **R$ 180.000** | **R$ 202.500** |

Sem RT, referência interna: R$ 136.900 e R$ 151.600.
Área de chapa: **210,02 m²** (era 214,23) em 58 chapas.
O upgrade custa R$ 3.360 de chapa a mais e **não acrescenta uma única chapa** ao
plano de corte — o interior colorido ocupa a sobra das chapas de cor que já
seriam compradas. É por isso que ele é barato para o que entrega.

### ⚠ O caderno original se perdeu

O container foi recriado e o PDF de origem sumiu de `/root/.claude/uploads/`.
A correção da sala de estar foi possível **só porque as 30 perspectivas ficaram
versionadas** em `projetos/img-vinicius/`. Para reconferir cota de elevação é
preciso subir o caderno de novo.

---

## 1 · Como o PDF foi lido

Caso **B** da taxonomia de `referencias/quantitativo.md`: **0 palavras de texto,
331 imagens, 337.884 vetores** — o texto está **em curvas**. O conector do Drive
não devolve nada; a leitura foi visual, sobre render a 2,9× com rotação de +90°
(as pranchas estão deitadas no PDF).

Como o desenho é vetorial e **cotado**, as medidas abaixo saíram das **cotas
escritas na prancha**, não de medição em pixel. Isso põe este job no mesmo
patamar de confiança do Eliuton — e acima da Luciana, que foi por módulo.

**Mapa das pranchas**

| Folhas | Ambiente |
|---|---|
| 01 | capa |
| 02–03 | Lavabo |
| 04–11 | Sala de jantar |
| 12–17 | Sala de estar |
| 18–21 | Varanda |
| 22–31 | Quarto Rafael e Miguel |
| 32–37 | Quarto Maria Luísa |
| 38–40 | Banho social |
| 41–46 | Quarto casal |
| 47–49 | Banho casal |

---

## 2 · Materiais do projeto

| Sigla | Material | Onde |
|---|---|---|
| **AR** | MDF **Areal** — ARAUCO | painéis, ripados, prateleiras orgânicas, mezanino, escada, bancada da varanda, cristaleira do casal |
| **FR** | MDF **Frapê** — ARAUCO | armários, racks, bancadas, portas, envelopamentos |
| **BT** | MDF **Branco TX** | interno de armário fechado |
| **TV** | MDF **Trevi** — DURATEX | nicho da sala de jantar |
| **CR** | MDF **Cru** | base do espelho do lavabo |

Nota que se repete em **todas** as pranchas:

> "ATENÇÃO AO PADRÃO DE VEIOS DOS MDF AMADEIRADOS — SEGUIR VEIOS NOS ENCONTROS
> EM TODOS OS DETALHES."

Isso **encarece o nesting**: peça com veio orientado não gira 90° para caber.
Está quantificado na sensibilidade (item 3).

---

## 3 · O que foi orçado, ambiente a ambiente

### Lavabo — 2,40 m² de chapa
Painel ripado em MDF Areal, 126 × 148, ripas de 3 × 2 cm com espaçamento de 3 cm
(passo 6 cm), espelho prata 126 × 98 colado em MDF Cru no miolo, LED 4000 K
superior e inferior.

### Sala de jantar — 39,23 m² · 19 dobradiças · 4 gavetas
- **Cristaleira** MDF Frapê 230 × 114,5 × 35,5 — 4 portas de vidro reflecta
  bronze com alumínio bronze e puxador Sotille, 4 prateleiras de vidro incolor
  temperado, LED 3000 K posterior.
- **Nicho** MDF Trevi Duratex 230 × 66 × 35,5 com LED superior.
- **Armário inferior** MDF Frapê 230 × 82 × 50 — 4 gavetas + 4 portas,
  **puxador em mármore travertino 6 × 6 (04 unidades)**.
- **Elevação B** — painel 120 × 262,5 com porta de giro 76 × 210; marco do vão
  140 × 150 em MDF Areal; painel 140 × 262,5 e porta de correr 140 × 242,5 com
  trilho embutido no gesso.
- **Elevação C** — painel 120 × 262,5 e porta de correr 72 × 230.
- **Sapateira** MDF Areal 52,5 × 105 × 25, 4 prateleiras inclinadas.

### Sala de estar — 42,68 m² · 12 dobradiças · 9 gavetas · **ripado 5,73 m²**
- **Buffet suspenso** MDF Frapê 443,5 × 80 × 45 — 6 gavetões, LED 3000 K
  superior e inferior, **puxador travertino (06 unidades)**.
- **Painel da TV** 228 × 262,5 em MDF Areal ripado: armário superior de 6 portas
  ripadas (228 × 59), painel ripado central 152 × 118,5, faixa ripada 228 × 30,
  8 prateleiras laterais de 34 e LED inferior.
- **Rack** MDF Frapê 228 × 50 × 61 — 3 gavetões, **puxador travertino (03 un)**.

### Varanda — 7,13 m² · 2 dobradiças
- **Armário superior** MDF Areal 73 × 168 × 22, **sem fundo**, 3 prateleiras de
  vidro incolor temperado, acabamento em tubinho champagne.
- **Armário inferior** MDF Frapê 90 × 80 × 50 — nicho de 30 × 68 e porta de 56,
  **puxador travertino (01 un)**.
- **Bancada curva** MDF Areal 300 × 40 × 5 cm, bordas arredondadas, fixação
  invisível, **pés chumbados em tubo champagne**.

### Quarto Rafael e Miguel — 37,68 m² · 19 dobradiças · 6 gavetas
- **Mezanino / cama suspensa** MDF Areal, estrado 203 × 150, **estruturado com
  metalon**, vão com porta de acesso, **guarda-corpo de corda**, LED 4000 K
  inferior.
- **Escada** MDF Areal — 9 degraus de 17, altura 170.
- **Cama inferior** 203 × 105 com 2 gavetões em MDF Frapê.
- **2 cabeceiras** 146 × 35 com LED 3000 K e **2 nichos** 146 × 23 com suporte
  em MDF Frapê.
- **Bancada/escrivaninha** MDF Frapê 113 × 46, 2 gavetas.
- **Armário** MDF Frapê 104,5 × 170 × 40 — 4 portas, 2 gavetas, prateleiras.
- **Armário existente ENVELOPADO** em MDF Frapê, 204 × 280, **3 portas novas de
  espelho prata**.

### Quarto Maria Luísa — 37,94 m² · 11 dobradiças · 5 gavetas · 2 básculas
- **Fechamento de cortineiro** MDF Frapê — 318,5 e 214,5, LED 3000 K inferior.
- **Painel e teto** em MDF Areal, 60 × 266 e 169,5 × 60.
- **3 prateleiras orgânicas** MDF Areal de 5 cm de espessura (duas lâminas de
  18 mm), fixação invisível, LED inferior — 170, 170 e 125, com retorno de canto.
- **Cabeceira estofada em gomos**, tecido facto branco, 4,14 m em duas paredes,
  vão posterior para persiana, LED 3000 K superior.
- **Bancada/penteadeira em L** MDF Frapê 172 + 167,5 × 50 × 80 — 2 gavetões,
  2 gavetas, báscula a gás e báscula com espelho prata colado, divisória em
  acrílico, LED 4000 K do espelho.
- **Banco-armário** 50 × 80 × 50 com assento estofado.
- **Armário existente ENVELOPADO** em MDF Frapê, 188,5 × 266, 3 portas de espelho.

### Banho social — 11,20 m² · 3 gavetas · 1 báscula
- **Armário superior** 140 × 120,5 × 15 — 3 portas de correr em espelho prata,
  12 prateleiras.
- **Armário inferior** 140 × 91 × 35 — báscula com pistão a gás, 2 gavetões
  tulha e 1 gavetão.

### Quarto casal — 25,46 m² · 9 dobradiças · 10 gavetas · 2 básculas
- **Painel da cabeceira** MDF Areal 272,5 × 256, instalado acima do rodapé.
- **Cabeceira estofada** em Tecido Bouclé Elba Cor Branco Bruma, 177,5.
- **Penteadeira** MDF Frapê 52 × 50 × 80 — báscula a gás, báscula com espelho
  prata colado, divisória em acrílico, LED 4000 K.
- **Mesa de cabeceira** MDF Frapê 45 × 50, **puxador travertino (01 un)**.
- **Cristaleira** MDF Areal 100,5 × 181 × 30 — 2 portas de vidro reflecta bronze,
  4 prateleiras de vidro, LED 3000 K posterior.
- **Armário inferior** MDF Frapê 100,5 × 85 × 30 — 8 gavetas.
- **2 portas** em MDF Areal (giro 97,5 × 242 e correr 59 × 242), puxador cava,
  perfil de alumínio na base.

### Banho casal — 10,51 m² · 2 gavetas · 1 báscula
- **Armário superior** 112 × 120,5 × 15 — 2 portas de correr em espelho prata,
  4 prateleiras, **iluminação frontal em LED 4000 K**.
- **Armário inferior** 112 × 91 × 51,5 — báscula a gás, gavetão tulha e gavetão.

---

## 4 · Números

| | |
|---|---|
| Área de chapa | **214,23 m²** |
| Chapas | **59** (aproveitamento médio 71 %) |
| Fita de borda | 435,20 m |
| Cava / chanfro usinado | 27,3 m |
| LED | 49,91 m |
| Ferragem | 72 dobradiças · 39 gavetas · 6 básculas · 54 prateleiras |
| Custo direto | R$ 60.683 a R$ 65.471 conforme a linha |

**Composição do custo direto** — chapas R$ 24.060 · terceirizados R$ 22.407 ·
LED R$ 3.294 · logística R$ 3.750 · consumíveis R$ 1.530 · fita R$ 1.436 ·
filetagem R$ 1.088 · cava R$ 682 · suportes R$ 324 · ferragem R$ 2.112 a 6.900.

> **O terceirizado pesa 37 % do custo direto** — espelhos, portas de vidro,
> estofador, serralheria do mezanino, tubo champagne e puxadores de travertino.
> É o job com maior fração de não-marcenaria que a casa já orçou.

### Preço — **COM RT de 10 %** [Jonathan 19/08]

Escada de MC 30/35/38, confirmada.

| Cenário | MC | Investimento | R$/m² de chapa | Garantia |
|---|---|---|---|---|
| I · Telescópica | 30 % | **R$ 148.000** | 691 | 2 anos |
| II · Hardt | 35 % | **R$ 175.400** | 819 | 5 anos |
| III · Hettich | 38 % | **R$ 197.300** | 921 | 10 anos |

Sem RT, para referência interna: R$ 121.800 · R$ 141.100 · R$ 155.900.
O RT vale ~R$ 17.500 no cenário II — 22 a 27 % sobre o preço sem RT, porque
sai de dentro do divisor, não por cima do preço.

Faixa de sanidade da casa **sem RT**: 626 (Rizzi) · 647 · 739 (SPE) ·
834 (Honda) · 624 (Eliuton). Sem RT o cenário II cai em **659** — meio da
faixa. Com RT sobe para 819, o que é esperado: o RT é comissão, não material.

O **ripado** (6,68 m², 3 % do projeto) sai à parte, a MC 40 %, como manda a
regra da casa.

---

## 5 · Sensibilidade

1. **Areal e Frapê como chapa ESPECIAL** (950/1200/800) em vez de COR
   (500/600/300): **+R$ 17.850 de custo ⇒ +R$ 39.653 de preço.**
   ⚠ É a maior incerteza do orçamento — a base da casa não tem preço nominal de
   Arauco amadeirado (mesmo buraco do Eliuton).
2. Interno na cor em vez de Branco TX (101,5 m²): +R$ 5.230 de chapa.
3. **Veio travado** no nesting: aproveitamento cai ~8 pontos ⇒ ~6 chapas a mais.
4. Terceirizados **sem preço na base**: R$ 7.210 — metalon do mezanino (2.500),
   pés e tubinho champagne (1.300), guarda-corpo de corda (800), 15 puxadores de
   travertino (2.250), 2 divisórias de acrílico (360).

---

## 6 · Dúvidas e itens a confirmar

**Fechado pelo Jonathan em 19/08** ✅

1. ✅ **Escada de MC: 30/35/38.**
2. ✅ **Chapa em COR** (500/600/300) — Areal e Frapê na faixa padrão.
3. ✅ **COM RT de 10 %** para a Jéssica Sollero.
4. ✅ **As estimativas dos terceirizados sem preço na base** — 15 puxadores de
   travertino a R$ 150/un, metalon do mezanino a R$ 2.500, guarda-corpo de corda
   a R$ 800, tubo champagne a R$ 900 + R$ 400 e acrílico a R$ 180.
5. ✅ **Estofador por peça**: duas peças "completo" para a cabeceira em gomos do
   quarto Maria Luísa (4,14 m em duas paredes) + uma "cabeceira" no quarto casal
   + uma no assento do banco.

**Para a arquiteta / conferir no local**

6. A **bancada e o nicho do lavabo**, as **bancadas dos dois banheiros** e a
   bancada da cuba aparecem em pedra nas perspectivas — não entraram no escopo
   de marcenaria.
7. A **sapateira** tem 52,5 de largura na elevação D e a planta traz 94 e 62 na
   mesma região. Adotei a cota da elevação.
8. A região de **140 × 100 abaixo do vão** da elevação B da sala de jantar está
   com hachura de parede e rodapé, não de marcenaria — não entrou.
9. A **bancada da varanda é curva** (R40/R46, arcos de 210,7 e 301,1). Adotei
    300 × 40 de projeção; o raio consome mais chapa.
10. Os **armários existentes** dos quartos Rafael/Miguel e Maria Luísa serão
    envelopados: as portas de espelho são novas, mas a caixaria é a que já está
    lá. Conferir se o corpo aceita a ferragem nova.
11. Na elevação D do quarto Maria Luísa o espelho tem 188,5 de vão e 266 de
    altura, mas a prancha não divide as folhas. Adotei 3 portas de 62,8.

---

## 7 · O que este levantamento **não** inclui

- Pedras (bancadas, cubas, rodabancas) — fora do escopo da casa.
- Persianas e cortinas (há vão previsto para persiana em duas cabeceiras).
- Eletrodomésticos: adega/frigobar da varanda, TV, pontos elétricos.
- Papel de parede, revestimento e pintura.
- **Montagem não entra no custo** (montador é salário fixo) — mas entra no
  escopo da proposta, feita por equipe própria.
