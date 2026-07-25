# Levantamento — Portas do vão da escada (contato: Flávia Moacir)

> **Status:** 🟢 REV.02 — escopo e material confirmados. Aguardando aprovação da tabela de cálculo para virar proposta.
> Origem: WhatsApp (atendimento Jonathan), fotos do local (escada em concreto + hall de elevadores amadeirado) e medidas passadas em texto.

## Leitura da conversa
- 14/07: foto da escada (vão subindo/descendo). Jonathan confirmou escopo: **porta no vão da escada subindo E porta no vão da escada descendo** — Flávia confirmou ("Isso").
- 17/07: foto do hall de elevadores (portas de madeira, acabamento amadeirado — referência estética do prédio).
- Jonathan perguntou a largura do **vão de passagem da escada**: Flávia respondeu **4,45×2,20** (medida do vão/patamar, não de uma porta individual).
- Pergunta "Só o vão da escada?" → resposta "Tudo kkk" + 3 medidas: **2,20×88 / 2,20×116 / 2,20×103**.

## Decisões confirmadas (REV.02)
1. **2 portas** (não 3) — o combinado original (subindo/descendo).
2. **MDF Ultra amadeirado fosco 15mm** (Duratex, linha reforçada/hidrófuga) — casa com o acabamento do hall dos elevadores.
3. **MC 37%, sem RT.**

## ⚠️ Ponto ainda assumido — confirmar antes de fabricar
- **Qual medida é qual porta:** das 3 recebidas (88/116/103cm), usei as **2 maiores (116 e 103)** como o par
  subindo/descendo — a de 88cm foi descartada por ser a mais estreita, provável abertura secundária.
  **Confirmar com a Flávia** qual largura é a "subindo" e qual é a "descendo" antes da produção.
- **Preços de dobradiça/fechadura/perfil/MDF Ultra são estimativa de mercado** (sem fornecedor cadastrado
  na base Valvic para esses itens específicos) — cotar com fornecedor (Häfele Brasil / Metalferco /
  Simonswerk / Duratex) antes de fechar.
- **Nome do prédio/síndico não identificado** — só temos o contato Flávia Moacir via Jonathan.

## Especificação técnica
- **Construção:** porta de giro lisa — miolo em sarrafo de pinus (estrutura) + MDF **frente e verso**
  (15mm cada face, ~35mm de espessura total).
- **Dobradiças invisíveis — pesquisa de mercado:** linha **Simonswerk Tectus**, referência técnica do
  setor para dobradiça 100% oculta.
  - TE.240.3D → até 60 kg · TE.340.3D → até 80 kg (espessura mín. porta 35mm) · TE.540.3D → até 120 kg.
  - Peso calculado por porta (MDF 2 faces + 15% estrutura/ferragem): **Porta 1 (116cm) 66,0 kg** ·
    **Porta 2 (103cm) 58,6 kg**.
  - Porta 1 já exige TE.340.3D (>60kg). Decisão: **padronizar TE.340.3D nas 2 portas** (margem + peça única).
  - Altura 2,20m > referência de catálogo (2,00m/2 dobradiças) → **3 dobradiças por porta**.
  - **Total: 6 unidades TE.340.3D.**
- **Fechadura de fecho rolete:** 1 unidade por porta (2 un) — padrão porta pivotante 30–35mm (Stam/Pado/Imab).
- **Perfil de alumínio na base:** 116+103=219cm > barra de 2m → **1 barra de 2m por porta** (2 barras).

## Quantitativo (plano de corte real — não por m²)
> Chapa 275×185cm. Cada peça é 220×largura — o lado de 220cm sempre corre no eixo de 275cm.
> 116+103=219cm / 116+116=232cm / 103+103=206cm — **nenhuma combinação cabe** dentro dos 185cm de largura
> da chapa → cada face ocupa uma chapa inteira. **4 chapas**, não as 3 que a conta ingênua por
> m²/aproveitamento sugeriria.

| Porta | Vão (AxL) | Área MDF (frente+verso) | Peso | Chapas dedicadas |
|---|---|---:|---:|---|
| 1 (subindo) | 220×116 | 5,104 m² | 66,0 kg | 2 chapas (1 por face) |
| 2 (descendo) | 220×103 | 4,532 m² | 58,6 kg | 2 chapas (1 por face) |
| **Total** | | **9,636 m²** | | **4 chapas MDF Ultra amadeirado fosco 15mm** |

Fita de borda: 13,18 m perímetro × 1,10 (perda) = **14,5 m**.
Estrutura interna (sarrafo pinus, perímetro + reforço): **17,1 m**.

## Custo de material (compra)

| Item | Qtd | Preço unit. | Total |
|---|--:|--:|--:|
| MDF Ultra amadeirado fosco 15mm | 4 chapas | R$ 580 | R$ 2.320 |
| Fita de borda (amadeirado) | 14,5 m | R$ 4,00/m | R$ 58 |
| Dobradiça Tectus TE.340.3D *(estimativa)* | 6 un | R$ 650 | R$ 3.900 |
| Fecho rolete *(estimativa)* | 2 un | R$ 75 | R$ 150 |
| Perfil alumínio base *(estimativa)* | 4 m (2 barras) | R$ 50/m | R$ 200 |
| Estrutura interna (sarrafo) | 17,1 m | R$ 8/m | R$ 137 |
| **Subtotal material** | | | **R$ 6.765** |
| Logística | | | R$ 300 |
| Visita técnica | | | R$ 200 |
| **Custo direto (fixedR)** | | | **R$ 7.265** |

## Precificação — MC 37%, sem RT
Motor oficial do validador: `inv = fixedR / (1 − a − liqF·b − mc)`, com **a**=16,2% (nf4+parc8+vend3+erro0,5+serra0,2+manut0,5),
**liqF**=0,88, **b**=4,3% (prog0,8+coord1+marc2,5+rt0), **mc**=37% → divisor **0,43016**.

| | Valor |
|---|--:|
| **INVESTIMENTO TOTAL (2 portas)** | **R$ 16.889** |
| Porta 1 — vão subindo (220×116) — 53,0% | R$ 8.946 |
| Porta 2 — vão descendo (220×103) — 47,0% | R$ 7.943 |

> Alocação proporcional por área de MDF — referencial. MC verificada = 37,0% em todas as linhas. RT = 0%. Sem desconto.

## Entregáveis
- `corte-flavia-portas.py` — script de cálculo (quantitativo + plano de corte + peso + motor), reproduzível/auditável.

## Próximo passo
Tabela de cálculo apresentada para aprovação (Jonathan). Após OK: cotar os 4 itens sinalizados como estimativa
com fornecedor real, confirmar qual largura é qual porta, e montar a proposta (padrão visual das comerciais Valvic).
