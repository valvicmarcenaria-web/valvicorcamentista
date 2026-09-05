# O Núcleo Informacional da Valvic — escopo de referência

Este é o **mapa mestre** de tudo que a Valvic precisa ter escrito para deixar de depender da
cabeça das pessoas. É o documento de escopo da Academy: diz **o que existe**, **o que falta**,
**quem é dono de cada buraco** e **em que ordem se produz**.

> Escopo definido com o Jonathan em setembro/2026. Substitui a discussão de "vamos fazer uma
> apostila". Complementa `curriculo-marcenaria.md`, que segue valendo como a narrativa dos
> módulos técnicos — mas **os IDs e o escopo fechado são aqui**.

---

## 1 · A decisão de arquitetura

O pedido original era uma apostila única, com todo o conhecimento, para todo mundo que entra.
**Não vamos fazer assim**, e a razão é o próprio aluno da casa: adulto, aprendeu fazendo, lê
em pé, com pressa (`metodo-didatico.md`). Apostila de 300 páginas para todos é apostila que
ninguém termina — e quando ninguém termina, o conhecimento continua na cabeça de quem sabe.

Cinco decisões substituem a apostila única:

### 1.1 · Ficha atômica, não capítulo
A unidade do núcleo é a **ficha**: 1 a 6 folhas A4, **um assunto só**, com ID estável. Um
módulo é um conjunto de fichas; uma apostila impressa é uma seleção de fichas com capa e
sumário. Nada se escreve "dentro do capítulo tal" — se escreve como ficha, e a ficha entra em
quantas apostilas precisar.

**Por que:** é o que permite imprimir a apostila do montador e a do programador da mesma
fonte, sem manter dois textos. E é o que permite corrigir uma ferragem sem reabrir 40 páginas.

### 1.2 · ID estável — e para sempre
Cada ficha nasce com um ID: `FER-03`, `QUI-02`, `FIX-02`. O ID **nunca muda e nunca se
reaproveita**, mesmo se a ficha for reescrita ou aposentada.

**Por que:** o POP vai citar "ver FER-03", o desenho vai citar, o checklist vai citar, o
formador vai citar. Sem ID, na terceira revisão ninguém sabe mais do que se está falando —
e é exatamente aí que a documentação morre nas empresas.

### 1.3 · Três camadas dentro de cada ficha, sempre separadas
Este é o ponto que mais economiza retrabalho no futuro:

| Camada | O que é | Muda quando |
|---|---|---|
| **SABER** | O ofício. O que é um caneco de 35 mm, o que é cola de contato base água | Quase nunca |
| **PADRÃO VALVIC** | A decisão da casa. "Corrediça oculta Hardt soft-close é o padrão Gold" | Muda com fornecedor, preço, garantia |
| **FAZER** | A execução com critério de aceite. Vira POP quando é tarefa | Muda com máquina e processo |

**Por que:** no dia em que a Valvic subir de Hardt para Blum — que é meta declarada — troca-se
a camada PADRÃO VALVIC de meia dúzia de fichas. Se as três camadas estiverem misturadas no
texto, reescreve-se a apostila inteira. Empresa nenhuma faz isso duas vezes; na segunda, o
material é abandonado.

### 1.4 · Nível profissional resolvido **dentro** da ficha
Não haverá apostila de iniciante e apostila de avançado — isso dobra o trabalho e desatualiza
metade. Cada ficha tem profundidade em camadas, na estrutura de 7 blocos do
`metodo-didatico.md`:

- **Folha 1 — o essencial.** O que qualquer pessoa da Valvic precisa saber, inclusive quem
  não é da produção. É o que entra no kit de integração.
- **Miolo — o técnico.** Números, especificações, tabelas. Para quem executa.
- **Erro comum + custo.** Para quem já executa e ainda erra. É a parte mais lida.
- **Como conferir.** O critério de "está bom". Para quem cobra o padrão.

Novato lê a folha 1 e o erro comum. Marceneiro vive no técnico e no critério. Mesma ficha.

### 1.5 · O núcleo é a mesma fonte que alimenta os agentes
As fichas moram em Markdown no repositório. Delas saem o HTML/PDF do `painel/`, o guia de
parede, o quiz — **e o conhecimento que a Lavinia, o Vitor e a Helena consultam**. Hoje
`orcamentista-marcenaria/referencias/ferragens.md` já é 70% da ficha de ferragens.

**Por que importa:** se a apostila virar um documento paralelo, em seis meses a Valvic terá
duas verdades sobre a mesma corrediça — a da apostila e a do orçamento. Uma fonte, várias
saídas. Sem exceção.

---

## 2 · Anatomia da ficha

```
ID · TÍTULO                                    [SABER | PADRÃO | FAZER]
─────────────────────────────────────────────────────────────────────
Por que isto importa      o custo do erro, em uma frase
Você vai saber            objetivo em verbo de ação
O essencial               folha 1 — o mínimo que todos precisam
O técnico                 números, tabelas, especificação
Como se faz aqui          o padrão Valvic, passo a passo
Erro comum e custo        o que dá errado, como se percebe antes, quanto custa
Como conferir             o critério de "está bom"
Verificação               pergunta, tarefa prática ou checklist
─────────────────────────────────────────────────────────────────────
Fonte · Dono do conteúdo · Revisão · Fichas relacionadas
```

Toda ficha declara **dono do conteúdo** (quem valida tecnicamente) e **data de revisão**.
Ficha sem dono é ficha que ninguém corrige quando a fábrica muda.

---

## 3 · O mapa — 14 blocos

**Legenda de estado:**
`✅` pronto · `🟡` a fonte existe, falta virar material · `🔴` não existe em lugar nenhum ·
`🧠` só na cabeça de alguém — exige sessão de extração

### Bloco 0 · A CASA — institucional `INST`
O que dá sentido a todo o resto. Hoje é o bloco mais vazio do núcleo.

| ID | Ficha | Estado | Fonte / dono |
|---|---|---|---|
| INST-01 | História da Valvic e os sócios — de onde viemos | 🧠 | Jonathan |
| INST-02 | O que a Valvic vende — Linha Gold, garantia de 10 anos, o padrão prometido | 🟡 | `closer-vendas/referencias/valor-do-produto.md`, `garantia.md`, `identidade-marca.md` |
| INST-03 | Quem é quem — organograma e o que cada cargo entrega | 🟡 | `painel/apostila-escopos-funcao.html` (10 cargos) |
| INST-04 | **Fluxograma mestre — da venda à entrega** | 🔴 | existe só na versão investidor (`walton-fluxo-trabalho.html`, restrito). Precisa de versão de chão de fábrica |
| INST-05 | Fluxos de apoio — compras, recebimento, assistência, não-conformidade | 🔴 | fichas existem, o fluxo não |
| INST-06 | As regras da casa — conduta, comunicação com cliente e arquiteto | 🟡 | espalhado em 5 documentos; `politicas-internas.md` |
| INST-07 | Kit de integração — o primeiro dia | 🔴 | receita em `trilhas-e-avaliacao.md` §Integração |

### Bloco 1 · A LINGUAGEM `LING`
Pré-requisito de tudo. Sem isso, nenhuma outra ficha é legível por quem chegou ontem.

| ID | Ficha | Estado | Fonte / dono |
|---|---|---|---|
| LING-01 | Anatomia do móvel — o nome de cada peça (lateral, base, tampo, costa, testeira, montante, frente) | 🔴 | Paulo / Deivison |
| LING-02 | Glossário técnico e o jargão da casa | 🟡 | Guia Técnico Mód. I (Drive) — ampliar |
| LING-03 | Medida, cota, tolerância e folga — como a Valvic mede | 🧠 | Paulo |

### Bloco 2 · MATERIAL `MAT`
Hoje comprimido no "Módulo I" junto com ferragens e glossário. Vira bloco próprio.

| ID | Ficha | Estado | Fonte / dono |
|---|---|---|---|
| MAT-01 | Substratos — MDF, MDP, compensado, chapa dura: o que é e onde entra | 🟡 | `orcamentista/referencias/chapas.md` |
| MAT-02 | Dimensão, espessura e rendimento — 2.750 × 1.840; 6, 9, 15, 18, 25 mm; peso | 🟡 | `chapas.md` |
| MAT-03 | Acabamentos de superfície — BP/melamínico, laminado (fórmica), lâmina natural, laca | 🟡 | `chapas.md` + `laminacao-e-construcao.md`; laca é 🧠 |
| MAT-04 | Comportamento do material — umidade, área molhada, direção do padrão, flecha e vão máximo | 🔴 | Paulo |
| MAT-05 | Recebimento e armazenagem — o defeito que se recusa na entrega | 🟡 | `painel/ficha-recebimento-material.html` |

### Bloco 3 · BORDAS `BOR`

| ID | Ficha | Estado | Fonte / dono |
|---|---|---|---|
| BOR-01 | Fitas — PVC, ABS, PP; 0,45 / 1 / 2 mm; largura; **a regra de cor bater com a chapa** | 🟡 | `chapas.md`, `laminacao-e-construcao.md` |
| BOR-02 | Colagem — coladeira, EVA × PUR, pré-fusionada; **a SCM ME25 não finaliza 100%** | 🟡🧠 | `curriculo-marcenaria.md` Mód. III; técnica com Deivison |
| BOR-03 | Refile, raspagem e acabamento de topo | 🧠 | Deivison |
| BOR-04 | Onde entra fita e onde não entra — a regra peça a peça | ✅🟡 | `laminacao-e-construcao.md` (fita por peça) |
| BOR-05 | Defeitos de borda — descolamento, folga, filete de cola | 🟡 | `painel/feedback-deivison-obra.html` |

### Bloco 4 · COLAS E QUÍMICOS `QUI`
**Buraco total.** Não existe uma linha escrita sobre isso em lugar nenhum do repositório.

| ID | Ficha | Estado | Fonte / dono |
|---|---|---|---|
| QUI-01 | Cola de contato — base solvente × base água, tempo aberto, aplicação nas duas faces | 🔴🧠 | Paulo |
| QUI-02 | Cola branca PVA e cola PUR — onde cada uma, tempo de prensa | 🔴🧠 | Paulo |
| QUI-03 | Silicones — **acético × neutro** (espelho e pedra exigem neutro), cor, aplicação | 🔴🧠 | Samuel (obra) |
| QUI-04 | PU, espuma expansiva, calafetador e rejunte — onde entram no acabamento | 🔴🧠 | Samuel |
| QUI-05 | Segurança e guarda — ventilação, inflamável, validade, descarte | 🔴 | — |

### Bloco 5 · FERRAGENS `FER`
O maior bloco do núcleo, e o que tem mais matéria-prima pronta.

| ID | Ficha | Estado | Fonte / dono |
|---|---|---|---|
| FER-01 | Dobradiças — caneco 35 mm, reta / curva / super-curva, amortecimento, calço, regulagem 3D | 🟡 | `ferragens.md` |
| FER-02 | Corrediças telescópicas — roldana × esfera, comprimento, capacidade (Linha Silver) | 🟡 | `ferragens.md` |
| FER-03 | Corrediças ocultas — soft-close, Hardt Invisível P-10 400/450/550, folga e regra de gaveta | 🟡 | `ferragens.md` |
| FER-04 | Elevação e báscula — pistão a gás força inversa 60N / 100N, articulador | 🟡 | `ferragens.md` |
| FER-05 | Deslizante de roupeiro — Dominus, trilhos RM-264 / RM-265, capacidade, exigência de vão | 🟡 | `ferragens.md`, `roupeiros.md` |
| FER-06 | Deslizante de porta de passagem — RO82, embutir × aparente, o que a obra tem de deixar pronto | 🟡🧠 | `ferragens.md` (citado, sem técnica) |
| FER-07 | Puxadores e perfis — SP7000, perfil slim, gola, touch/pulsador Blum | 🟡 | `ferragens.md` |
| FER-08 | Suportes e montagem — VB Zamac, pino pitão, cantoneira, tapa-furo | 🟡 | `ferragens.md` |
| FER-09 | Iluminação — fita LED 240 leds, perfil com difusor, fonte, sensor, dimensionamento | 🟡 | `ferragens.md` |
| FER-10 | Homologadas Valvic — Hardt, Hettich, Häfele, Rometal, Blum: e o que a garantia de 10 anos obriga | 🟡 | `ferragens.md`, `garantia.md` |

### Bloco 6 · FIXAÇÃO E MONTAGEM `FIX`
Pedido explícito do Jonathan, e hoje inexistente.

| ID | Ficha | Estado | Fonte / dono |
|---|---|---|---|
| FIX-01 | Parafuso — como se lê a medida (Ø × comprimento), cabeça, ponta, rosca | 🔴 | — |
| FIX-02 | **Tabela de aplicação e risco de atravessamento** — 4×16, 3,5×20, 4×25, 4×40 contra cada espessura | 🔴🧠 | Paulo / Deivison |
| FIX-03 | Montagem desmontável — cavilha M8×30, minifix / excêntrico, tambor | 🟡 | `ferragens.md` |
| FIX-04 | Furação sistema 32 e gabaritos | 🔴 | previsto no Mód. III |
| FIX-05 | Fixação em parede — drywall, gesso, alvenaria, concreto: a bucha certa para cada uma | 🔴🧠 | Samuel |
| FIX-06 | Dispositivos, gabaritos e ferramenta de montagem | 🟡 | `painel/checklist-insumos-ferramentas.html` |

> **FIX-02 é, na minha leitura, a ficha de maior retorno do núcleo inteiro.** É um erro que
> atravessa a porta do cliente, é irreversível, acontece com quem tem pressa, e cabe numa
> folha. Deve nascer já como **guia de parede** além de ficha.

### Bloco 7 · CONSTRUÇÃO DO MÓVEL `CON`

| ID | Ficha | Estado | Fonte / dono |
|---|---|---|---|
| CON-01 | Caixaria — esquadro, prumo, sequência de montagem | 🟡 | Mód. IV previsto |
| CON-02 | Gaveta — as 6 peças, dimensionamento e folga | ✅🟡 | `laminacao-e-construcao.md` |
| CON-03 | Portas e frentes — folga, alinhamento, regulagem | 🧠 | Deivison |
| CON-04 | **Tipos de cava** — usinada 45°, cava perfil, cava em L, gola, cava de embutir: quando cada uma, profundidade, custo | 🔴🧠 | Jonathan / programador |
| CON-05 | Ripado, filetagem e curvos | 🟡 | `laminacao-e-construcao.md` |
| CON-06 | Tipologias — roupeiro/closet, cozinha, banheiro, rack/painel, home | 🟡 | `roupeiros.md`, `movel-roupeiro.md` |

### Bloco 8 · LEITURA DE PROJETO `PRJ`
Prioridade declarada — é a causa direta do gargalo da casa.

| ID | Ficha | Estado | Fonte / dono |
|---|---|---|---|
| PRJ-01 | Anatomia do executivo — prancha, legenda, escala, revisão R01/R02 | 🔴 | caso real: Lucas & Ana, 84 pranchas |
| PRJ-02 | Planta, vista, corte e detalhe — o que cada desenho responde | 🔴 | — |
| PRJ-03 | Ler a cota e virar peça | 🔴 | — |
| PRJ-04 | Lista de materiais — e onde o projeto diz qual ferragem vai | 🟡 | `quantitativo.md` |
| PRJ-05 | Plano de corte e nesting — ler e conferir antes de cortar | 🟡 | `quantitativo.md` |
| PRJ-06 | **O que fazer quando o projeto não diz** — a regra de perguntar antes de assumir | 🔴 | `MOLESKINE.md` (aprendizados Lavinia) |

### Bloco 9 · DA FÁBRICA `FAB`
| ID | Ficha | Estado |
|---|---|---|
| FAB-01 | Corte e nesting | 🟡 |
| FAB-02 | Coladeira e filetagem — incluindo o acabamento manual que a ME25 exige | 🟡🧠 |
| FAB-03 | Usinagem e CNC — a consequência do erro de programação | 🧠 |
| FAB-04 | Pré-montagem e embalagem | 🔴 |
| FAB-05 | O que é uma peça aprovada | ✅ | `POP-01` + Módulo VI |

### Bloco 10 · OBRA E ACABAMENTO `OBR`
| ID | Ficha | Estado | Fonte |
|---|---|---|---|
| OBR-01 | Conduta na casa do cliente — proteção, limpeza, o que se fala e o que não se fala | 🟡 | `kit-montador-relatorios.html` |
| OBR-02 | Sequência de montagem em obra | 🧠 | Samuel |
| OBR-03 | Instalação de LED em obra | 🟡 | FER-09 |
| OBR-04 | **Acabamento e o padrão Valvic** | ✅ | `painel/academy-modulo-06-acabamento.html` — 37 pontos reais |
| OBR-05 | Vistoria e entrega ao cliente | 🟡 | `matriz-conferencia.html` |

### Bloco 11 · SEGURANÇA E ORGANIZAÇÃO `SEG` / `ORG`
| ID | Ficha | Estado |
|---|---|---|
| SEG-01 | Máquina segura — serra, coladeira, furadeira, CNC | 🔴 |
| SEG-02 | EPI — o que se usa em cada tarefa | 🔴 |
| SEG-03 | Carga e transporte — o acidente do RJ como caso de abertura | 🧠 |
| SEG-04 | O que fazer em caso de acidente | 🔴 |
| ORG-01 | Layout do galpão e onde fica cada coisa | 🟡 `layout-fase1-galpao-atual.html` |
| ORG-02 | Ferramenta — devolução, termo e responsabilidade | 🟡 `controle-veiculos-termo.html` (modelo) |

### Bloco 12 · POP `POP`
O Doc 12 do Valvic OS. Cada POP nasce **atrelado à ficha que o explica**.

| ID | POP | Estado | Ficha-mãe |
|---|---|---|---|
| POP-01 | Conferência de peça antes de sair da fábrica | ✅ aguarda aprovação da Direção | FAB-05 |
| POP-02 | Friso e perfil de alumínio — a técnica | 🧠 perguntas já escritas no Mód. VI | OBR-04 |
| POP-03 | Recebimento de material | 🔴 ficha existe, procedimento não | MAT-05 |
| POP-04 | Medição em obra | 🔴 `ficha-medicao.html` existe | LING-03 |
| POP-05 | Conferência de programação (pré-CNC) | 🔴 | PRJ-05 |
| POP-06 | Montagem em obra e entrega | 🔴 | OBR-02 |
| POP-07 | Assistência técnica e não-conformidade | 🔴 | INST-05 |

### Bloco 13 · TRILHAS E AVALIAÇÃO `TRI`
| ID | Trilha | Estado |
|---|---|---|
| TRI-01 | Ajudante → Marceneiro | ✅ `trilha-formacao-marceneiro.html` — é o modelo da casa |
| TRI-02 | Montador | 🔴 |
| TRI-03 | Programador CNC | 🔴 — o conhecimento mais concentrado e de maior risco |
| TRI-04 | Operador de máquinas | 🔴 |
| TRI-05 | Assistente operacional | 🟡 base na skill da Alice |
| TRI-06 | Projetos / arquitetura | 🟡 Plano de Estágio |

---

## 4 · Contagem e realidade do escopo

**77 fichas mapeadas.** Delas: **4 prontas**, **31 com fonte pronta faltando virar material**,
**42 inexistentes** — e **24 dependem de extração** da cabeça do Jonathan, Paulo, Deivison ou
Samuel.

Isso é a medida honesta do gargalo: **um terço do núcleo da empresa só existe como conversa.**

---

## 5 · Ordem de produção

A ordem não é a numérica. É esta, e o critério de cada onda está dito:

### Onda 1 — o que só existe na cabeça e sai barato
*Critério: buraco total + alto custo do erro + cabe numa sessão de extração.*
1. **FIX-02** — tabela de parafuso e atravessamento (ficha + guia de parede)
2. **QUI-01 a QUI-05** — o bloco de colas inteiro; hoje é zero e é usado todo dia
3. **LING-01** — anatomia do móvel (destrava a leitura de todo o resto)
4. **CON-04** — tipos de cava

### Onda 2 — o gargalo declarado
*Critério: ataca diretamente "executou sem saber ler o que já estava definido".*
5. **PRJ-01 a PRJ-06** — o bloco de leitura de projeto, com o executivo do Lucas & Ana
   (84 pranchas) como caso real
6. **POP-05** — conferência de programação pré-CNC

### Onda 3 — a integração
*Critério: para de perder gente na primeira semana.*
7. **INST-01 a INST-07** — a casa, o organograma, os fluxogramas e o kit de integração

### Onda 4 — a colheita
*Critério: 70% do texto já existe; é trabalho de conversão, rápido e de alto volume.*
8. **FER-01 a FER-10** — todo o bloco de ferragens a partir do `ferragens.md`
9. **MAT + BOR** — material e bordas a partir de `chapas.md` e `laminacao-e-construcao.md`

### Onda 5 — fechar o cerco
10. **POP-03, POP-04, POP-06, POP-07** · **SEG** · **CON** · **FAB** · **TRI-02 a TRI-04**

---

## 6 · As sessões de extração

24 fichas dependem de conhecimento que só existe falado. Isso não se resolve pedindo à pessoa
que escreva — se resolve com **sessão curta, pergunta dirigida e rascunho para corrigir**
(`metodo-didatico.md` §Extrair). Agrupadas por dono, para não picar a agenda de ninguém:

| Dono | Sessões | Fichas cobertas |
|---|---|---|
| **Jonathan** | 2 | INST-01, INST-02, INST-06, CON-04 |
| **Paulo** | 3 | LING-01, LING-03, MAT-04, MAT-03 (laca), QUI-01, QUI-02, FIX-02 |
| **Deivison** (fábrica) | 3 | BOR-02, BOR-03, CON-03, FAB-02, FAB-03, FIX-02 |
| **Samuel** (obra) | 2 | QUI-03, QUI-04, FIX-05, OBR-02, SEG-03 |

**10 sessões de 40 minutos destravam um terço do núcleo.** É o melhor investimento de tempo
disponível neste projeto.

---

## 7 · Regras de manutenção

1. **Uma fonte.** A ficha em Markdown é a verdade. HTML, PDF e guia de parede são saídas.
   Correção entra na ficha, nunca no PDF.
2. **ID não se reaproveita.** Ficha aposentada vira `FER-03 · APOSENTADA — ver FER-11`.
3. **Toda ficha tem dono e data de revisão.** Sem dono, não publica.
4. **Nada se inventa.** Ficha sem fonte e sem extração não é escrita — é marcada 🧠 e vira
   pergunta na próxima sessão. POP inventado destrói a confiança em todo o resto.
5. **Documento restrito não vira aula.** Folha, passivo trabalhista, investidor, caderno
   empresarial e todos os `walton-*` ficam fora — inclusive como fonte citada.
6. **Caso real: o erro e a consequência, nunca a pessoa.**
7. **A cada ficha publicada**, atualizar o estado aqui e no `dados/estado-da-academy.md`.

---

## 8 · Como se mede se isto funcionou

Não pelo número de fichas. Pelas três medidas do `trilhas-e-avaliacao.md`:
**retrabalho**, **tempo até a autonomia** e — a que mede o gargalo-raiz —
**quantas perguntas ainda sobem para o Jonathan e o Paulo.**
