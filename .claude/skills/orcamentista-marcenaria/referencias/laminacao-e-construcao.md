# Regras de laminação (fita de borda) e construção

Regras **gerais** do método Valvic, válidas para todos os móveis. A laminação é
ponto crítico de precisão — **subestimar fita já gerou prejuízo** (ver painel
ripado em `processo-orcamento.md`).

## Fita de borda — qual face leva fita, por tipo de peça

| Peça                        | Faces que recebem fita                                  |
|-----------------------------|---------------------------------------------------------|
| **Gaveta — laterais**       | os **dois lados maiores** (cima e embaixo)              |
| **Gaveta — frente e contra-frente** | **um lado maior só** (só o de cima)             |
| **Frente de gaveta** (face visível) | **4 lados** — *exceto* puxador de cava (usinagem, outra regra) |
| **Porta**                   | **4 lados**                                             |
| **Estrutura** (laterais/verticais, base, teto) | **um lado maior** (a borda frontal aparente) |
| **Fundo**                   | **não recebe fita**                                     |
| **Tamponamento**            | frente / lado maior (cima e embaixo) — proteção e transporte |

> Ao quantificar a fita: somar os **metros lineares reais** das faces acima,
> peça por peça, e aplicar **+10% de desperdício** (ver `quantitativo.md`).
> Bitola usual **22 × 0,45 mm**, na cor da chapa.

## Regras construtivas

- **Fundo por encaixe (não parafusado).** Faz-se um **rasgo** nas laterais e no
  pé de base, e o fundo **encaixa**. Padrão em praticamente todos os armários.
  - **Exceção:** armários de banheiro **superiores** (fininhos) — fundo
    **parafusado**.
- **Gaveteiro = módulo independente.** Tem caixaria própria (laterais, teto,
  base); **o módulo do gaveteiro não tem fundo** (o fundo do armário serve),
  mas **as gavetas têm fundo**. Depois encaixa-se o módulo na estrutura.
- **Tamponamento** = peça de acabamento nas laterais do armário. Geralmente
  **18 mm** (às vezes 15 mm), laminado na frente / lado maior.

> Espessuras seguem o padrão Valvic (estrutura e gavetas 15 mm; portas 18 mm no
> caso de correr/Dominus; fundos 6 mm) — ver `chapas.md`. Confirmar caso a caso.

## Ripado — o maior gargalo de fita (onde mais se perde dinheiro)

> **Regra de ouro:** ripado consome **muito mais fita** do que parece. Calcular
> régua a régua, sempre. Subestimar aqui = prejuízo na certa. São **três
> construções** distintas — identificar qual é antes de quantificar.

**Geometria comum:** cada régua tem **largura** (ex. 3 cm) + **espaçamento**
entre réguas (ex. 1–2 cm). O **passo = largura + espaçamento**.
→ **nº de réguas ≈ largura útil do vão ÷ passo.**

### Tipo 1 — ripado de PORTA (vazado), MDF 15 mm laminado nas 2 faces
- Quadro de marcenaria em **MDF 15 mm**, usinado tirando o miolo, deixando
  **borda ~5 cm**; o quadro é laminado **por fora e por dentro** (fica acabado).
- Preenchido com **réguas de MDF 15 mm laminadas nas 2 faces**.
- Régua usual **3 cm de largura + 2 cm de espaçamento** (passo 5 cm); altura da
  régua = altura útil do vão (ex. faixa de ar-condicionado = **33 cm**).
- **Fita por régua = perímetro das bordas ≈ 2 × (altura + largura)**
  (ex. 2 × (33 + 3) = **72 cm ≈ 0,70 m por régua**).
- **Fita total da porta = nº réguas × ~0,70 m + fita do quadro.**
  > Ex.: porta de 88 cm → ~17–18 réguas → **~12,5 m de fita só nas réguas**, por
  > porta. Multiplicar pelo nº de portas ripadas.
- Filetagem na **máquina** (réguas de 15 mm passam na coladeira automática).

### Tipo 2 — PAINEL ripado, MDF 18 mm fitado em **uma face** só
- Mais comum em **painel** (raramente porta). MDF **18 mm**, **fita em 1 face**;
  a **face fitada fica para a frente** (é o que aparece); o **topo cola no
  painel** de fundo.
- Espaçamento varia por projeto (**geralmente ~1 cm**).
- **Fita = a régua inteira fitada de um lado só** → **um custo de fita por
  régua** (comprimento da régua) + **um custo de filetagem** (máquina). Bem mais
  econômico em fita que o Tipo 1.

### Tipo 3 — ripa fina, MDF 6 mm (filetagem **manual**)
- Réguas de **6 mm** **não passam na coladeira automática** → filetagem
  **manual**, processo mais lento.
- Mesmo na régua de 6 mm, **considerar fita de 22 mm** (há mais perda de
  largura, mas usa-se a bitola padrão) e **~1 m de fita por régua**.
- **Custo de aplicação é maior** (ver tabela abaixo).

## Custo de filetagem (APLICAÇÃO) — separado do custo da fita-material

> A fita tem **dois custos**: o **insumo** (a fita em si — ver `materiais.json`:
> Branco ~R$2/m, Cor ~R$3/m) **e** a **aplicação/filetagem** (mão de obra +
> coladeira). No orçamento, somar os dois.

| Filetagem        | Custo aprox. | Quando                                   |
|------------------|--------------|------------------------------------------|
| **Máquina** (coladeira automática) | **~R$ 2,50 / m** | padrão (15/18 mm, réguas que passam na máquina) |
| **Manual**       | **~R$ 4,00 / m** | ripa de 6 mm e casos que não entram na máquina |

> Valores da planilha de validação da Valvic (a confirmar na versão que o
> Jonathan vai enviar). O diferencial máquina × manual existe porque o trabalho
> manual leva mais tempo.
