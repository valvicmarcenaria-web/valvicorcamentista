# Conciliação — painel × repositório × Drive  [04/08/2026]

Auditoria de **todos** os orçamentos: o que está no painel, o que está no repositório
(`projetos/*.md`) e o que está no Drive (`valvicmarcenaria@gmail.com`).

> **A conta do Drive mudou.** Nas sessões anteriores o conector apontava para
> `clubedoplanejado@gmail.com` e nada da Valvic aparecia. Agora está em
> `valvicmarcenaria@gmail.com` e o acervo inteiro está acessível — foi o que permitiu
> esta conciliação.

## Estrutura do Drive

```
Orçamentos Valvic/
  └── Em aberto/          leonardo_mirante · romulo · Nura · hotel_ibis · juliana
                          junior - Lagoa santa · carla_dresller · projeto_fabio
CLIENTES VALVIC/          (compartilhada por producaovalvic@gmail.com)
  └── Tania · Cristiane · Ana Carolina · Alexandrina · Bernardo
      Carla dressler · Simony - Buritis
sistema_valvic/           apps · financeiro · fluxograma
```

## ✅ Adicionados ao painel — 7 orçamentos que existiam e não estavam lá

| Cliente | Ref. | Máx. | Onde estava | Observação |
|---|--:|--:|---|---|
| **Júnior — Lagoa Santa** | 370.000 | 395.000 | Drive (doc 18/06) | Casa completa, 9 ambientes, Res. Bouganville. **2º maior da carteira** |
| **Quartos Mateus & Manuela** | 93.800 | 104.200 | repo (fechado hoje) | A Urbanística · 11 móveis |
| **Clínica Nura** | 85.150 | 92.550 | Drive (PDF 08/07) | Comercial · arq. Jessyca Santos |
| **Rômulo** | 39.000 | 58.400 | Drive (PDF 09/07) | Apto 4 amb · 3 níveis de ferragem |
| **Simony — Buritis** | 34.850 | — | Drive (contrato) | **Contrato assinado** — não era orçamento, era venda fechada |
| **Karina Ramos** | 17.500 | 21.500 | repo + Drive | Estava em PARADOS "a consultar", mas a proposta Gold/Silver está fechada |
| **Regina Godinho** | 13.100 | — | Drive (doc 16/06) | Escritório · cliente recorrente, 3º projeto |

**Impacto:** 19 → **26 orçamentos** · R$ 1.641.166 → **R$ 2.294.566** (+R$ 653.400,
+40%). Ticket médio R$ 86.377 → **R$ 88.253**.

## 🔁 PARADOS reconstruído

Antes trazia só "Karina Ramos — a consultar", que na verdade tinha proposta fechada.
Agora lista os leads com **escopo de venda registrado no Drive e sem orçamento fechado**:

`Cristiane · Ana Carolina · Tania · Bernardo · Carla Dressler · Marina · Alexandrina`

São 7 pastas com projeto ou escopo recebido e nenhum número. É a fila real de trabalho.

## ✔️ Já existia e foi mantido — 19 entradas

Kênia & Fábio · Casa L&M · Resolve Consórcio · Lilian Lee · Kairon & Juliana ·
SPE Nova Lima 1 · Aline Sanches · Apto CJ · TRT 3ª Região · Jairo Samuel ·
Porto Verde · Ed. Luxemburgo · Raquel · Camila · Graça · Hotel Ibis ·
Flávia Moacir · Lirriet Libório · Maria.

## ⚠️ Achados que precisam de decisão

1. **O HANDOFF do Juninho estava errado.** `HANDOFF-juninho-lagoa-santa.md` diz que
   *"o orçamento do Juninho não foi encontrado neste repositório"* e manda localizá-lo.
   Ele **existe no Drive desde 18/06** — R$ 395.000, com breakdown por ambiente,
   condições fechadas e proposta em 6 páginas. As três instruções pendentes do handoff
   (serralheria da cozinha ~R$ 900, ferragens Hettich, sem versão Hardt) **já estão
   aplicadas** no documento do Drive. O handoff pode ser encerrado.

2. **Lucas e Ana — Apto 101 (2025), R$ 181.800 Gold.** Não foi adicionado. O material
   está em `fontes/` com prefixo `exemplo_` e o dossiê o descreve como o caso que ensina
   o método. Se for cliente real e não material de treino, entra e move o total para
   R$ 2.476.366. **A confirmar.**

3. **Rômulo tem três colunas de preço** (43.300 / 48.300 / 58.400, e −10% no fechamento
   dos 4 ambientes: 39.000 / 43.500 / 52.600). Lancei o piso à vista (39.000) e o teto
   de tabela (58.400). Se ele fechou numa coluna específica, corrigir.

4. **Coluna `drive`.** Marquei `ok` para tudo que tem pasta com proposta no Drive.
   Os quartos Mateus & Manuela e os demais projetos recentes do repositório seguem
   `ausente` — os PDFs estão só no Git.
