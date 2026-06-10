# Custo logístico

## A virada: de "por projeto" para "por ambiente"

**Antigamente (errado):** calculava a logística do **projeto inteiro**, no olho.
Ex. Lucas: "acho que uns 5 carretos de material (trazer pra fábrica + levar pra
casa) + uns R$500 de combustível da equipe na montagem". Resultado: número
**genérico e subestimado** — o orçamento saía **abaixo do que deveria**.

**Hoje (refinado):** a logística é medida **por ambiente** — coerente com a
separação Ambiente → Itens do Valvic OS (campos `logMat`, `logEquipe`,
`descarga`). Cada ambiente carrega a sua própria logística.

## Como estimar a logística de um ambiente

### 1. Carreto (transporte)
Pensar **quantos móveis cabem por carreto**. Ex.: a **sala do Lucas** tem
cristaleira + rack → **dá pra levar os dois num carreto só**.

- **1 carreto de ida** (fábrica → casa do cliente, móveis prontos)
- **+ 1 carreto** (vinda do material → fábrica)
- ≈ **R$ 300 os dois carretos** (~R$ 150 cada).

### 2. Equipe de montagem (era esquecido — causava subprecificação)
O montador (ex.: Samuel) **+ um ajudante** gastam **2 a 3 dias** para montar
aquele ambiente, indo à casa do cliente **~3 vezes**. Esse custo de equipe
(diárias + deslocamentos do montador e ajudante) **tem que entrar no ambiente**
— antes era ignorado ou jogado num número geral, e o orçamento ficava baixo.

> Regra prática: logística do ambiente = **carretos** (material + entrega) **+
> equipe de montagem** (montador + ajudante × dias × deslocamentos). O fator
> `descarga` do Valvic OS é um multiplicador sobre essa base.

## Setup / visita técnica (também era especulação solta)

Após o cliente fechar, agenda-se a **visita técnica total** para medir. Na
prática, gasta **2 a 3 visitas**, porque em obra um ambiente às vezes **não pode
ser medido** e o Paulo precisa **voltar para remedir**. Isso entra como **setup**
no motor de orçamento (Valvic OS: `setup` do ambiente / setup por pessoa).

- Visitas têm custo (na planilha: validação R$250 / conferência R$300).
- Antes era estimado "no ar", com pouca precisão.

## Arredondamento de consumíveis (margem de segurança)

Mede-se e **arredonda para cima** no orçamento. Ex.: deu **5,5 m de LED** →
lança **6 m de LED**, **6 m de perfil**, **1 m de cabo**. Pequenas folgas que
evitam faltar — coerente com a "margem de erro" (2%) da planilha.

## A continuar (variância produção × orçamento)

> 🟡 O fundador estava explicando o que acontece **depois** que a produção
> começa: às vezes gasta **mais/menos carreto**, às vezes **falta chapa**…
> Registrar aqui como a realização se compara ao orçado e o que isso ensina
> para calibrar a estimativa. (Continuar com a explicação.)
