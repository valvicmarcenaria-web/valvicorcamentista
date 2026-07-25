# Levantamento — Portas do vão da escada (contato: Flávia Moacir)

> **Status:** 🟡 Levantamento de material concluído (custo). Falta confirmação de escopo/cor antes de virar proposta.
> Origem: WhatsApp (atendimento Jonathan), fotos do local (escada em concreto + hall de elevadores amadeirado) e medidas passadas em texto.

## Leitura da conversa
- 14/07: foto da escada (vão subindo/descendo). Jonathan confirmou escopo: **porta no vão da escada subindo E porta no vão da escada descendo** — Flávia confirmou ("Isso").
- 17/07: foto do hall de elevadores (portas de madeira, acabamento amadeirado — referência estética do prédio, não necessariamente da cor das portas técnicas da escada).
- Jonathan perguntou a largura do **vão de passagem da escada**: Flávia respondeu **4,45×2,20** (medida do vão/patamar, não de uma porta individual).
- Pergunta "Só o vão da escada?" → resposta "Tudo kkk" + 3 medidas: **2,20×88 / 2,20×116 / 2,20×103**.

## ⚠️ Pontos assumidos — confirmar antes de fechar
1. **3 portas, não 2.** O combinado inicial foi 2 portas (subindo/descendo); vieram 3 medidas ("tudo"). Orcei as 3 — se for só 2, é só remover a de menor prioridade (ver alocação por porta abaixo, é proporcional e direto de ajustar).
2. **Cor do MDF não informada.** Assumi **Branco TX 15mm** (porta técnica/utilitária, acesso de serviço) — se for para casar com o amadeirado do hall dos elevadores, o custo de chapa sobe (cor ~R$500/chapa vs branco R$260/chapa → +R$1.200 no material, +~R$2.790 no investimento final).
3. **Preços de dobradiça/fechadura/perfil são estimativa de mercado** (não há fornecedor cadastrado na base Valvic para esses itens específicos) — cotar com fornecedor (Häfele Brasil / Metalferco / Simonswerk) antes de fechar.
4. **Nome do prédio/síndico não identificado** — só temos o contato Flávia Moacir via Jonathan.

## Especificação técnica (conforme solicitado)
- **Construção:** porta de giro lisa — miolo em sarrafo de pinus (estrutura) + MDF **frente e verso** (15mm cada face, ~35mm de espessura total), conforme instruído.
- **Dobradiças invisíveis — pesquisa de mercado:** linha **Simonswerk Tectus** é a referência técnica do setor para dobradiça 100% oculta.
  - TE.240.3D → até 60 kg · TE.340.3D → até 80 kg (espessura mín. porta 35mm) · TE.540.3D → até 120 kg.
  - Peso calculado por porta (MDF 2 faces + 15% estrutura/ferragem): Porta A 50,1 kg · Porta B 66,0 kg · Porta C 58,6 kg.
  - **Porta B (66 kg) já exige o TE.340.3D.** Decisão: **padronizar TE.340.3D nas 3 portas** (margem de segurança + peça única em estoque).
  - Altura 2,20 m > referência de catálogo (2,00 m/2 dobradiças) → **3 dobradiças por porta** (evita empeno no uso intenso de escada de serviço).
  - **Total: 9 unidades TE.340.3D.**
- **Fechadura de fecho rolete:** 1 unidade por porta (3 un) — padrão porta pivotante 30–35mm (Stam/Pado/Imab).
- **Perfil de alumínio na base:** protege o rodapé da porta contra impacto/umidade — 1 corte por porta, barras de 2m (Porta A+C dividem 1 barra: 88+103=191cm ≤200cm; Porta B usa a 2ª barra).

## Quantitativo (plano de corte real — não por m²)
> Chapa 275×185cm. Cada peça é 220×largura — o lado de 220cm sempre corre no eixo de 275cm.
> Larguras só combinam 2 a 2 numa chapa se a soma ≤185cm: **só 88+88 cabe** (176cm); 88+103=191, 103+103=206,
> 88+116=204 e 116+116=232 **não cabem**. Resultado: **5 chapas**, não as 4 que a conta ingênua por m²/aproveitamento sugeriria.

| Porta | Vão (AxL) | Área MDF (frente+verso) | Peso | Chapas dedicadas |
|---|---|---:|---:|---|
| A | 220×88 | 3,872 m² | 50,1 kg | 1 chapa (as 2 faces juntas) |
| B | 220×116 | 5,104 m² | 66,0 kg | 2 chapas (1 por face) |
| C | 220×103 | 4,532 m² | 58,6 kg | 2 chapas (1 por face) |
| **Total** | | **13,508 m²** | | **5 chapas MDF Branco 15mm** |

Fita de borda: 19,34 m perímetro × 1,10 (perda) = **21,3 m**.
Estrutura interna (sarrafo pinus, perímetro + reforço): **25,1 m**.

## Custo de material (compra)

| Item | Qtd | Preço unit. | Total |
|---|--:|--:|--:|
| MDF Branco TX 15mm | 5 chapas | R$ 260 | R$ 1.300 |
| Fita de borda | 21,3 m | R$ 2,50/m | R$ 53 |
| Dobradiça Tectus TE.340.3D *(estimativa)* | 9 un | R$ 650 | R$ 5.850 |
| Fecho rolete *(estimativa)* | 3 un | R$ 75 | R$ 225 |
| Perfil alumínio base *(estimativa)* | 4 m (2 barras) | R$ 50/m | R$ 200 |
| Estrutura interna (sarrafo) | 25,1 m | R$ 8/m | R$ 201 |
| **Subtotal material** | | | **R$ 7.829** |
| Logística | | | R$ 300 |
| Visita técnica | | | R$ 200 |
| **Custo direto (fixedR)** | | | **R$ 8.329** |

## Precificação — MC 37%, sem RT
Motor oficial do validador: `inv = fixedR / (1 − a − liqF·b − mc)`, com **a**=16,2% (nf4+parc8+vend3+erro0,5+serra0,2+manut0,5),
**liqF**=0,88, **b**=4,3% (prog0,8+coord1+marc2,5+rt0), **mc**=37% → divisor **0,43016**.

| | Valor |
|---|--:|
| **INVESTIMENTO TOTAL (3 portas)** | **R$ 19.363** |
| Porta A (220×88) — 28,7% | R$ 5.550 |
| Porta B (220×116) — 37,8% | R$ 7.316 |
| Porta C (220×103) — 33,6% | R$ 6.496 |

> Alocação proporcional por área de MDF — referencial, para facilitar aprovação parcial (ex.: só as 2 do combinado original).
> MC verificada = 37,0% em todas as linhas. RT = 0%. Sem desconto.

## Entregáveis
- `corte-flavia-portas.py` — script de cálculo (quantitativo + plano de corte + peso + motor), reproduzível/auditável.

## Próximo passo
Confirmar com Jonathan/Flávia: (1) 2 ou 3 portas, (2) cor do MDF, (3) nome do prédio/cliente formal — daí monto a proposta
(mesmo padrão visual das comerciais) e cotamos os 3 itens de ferragem/perfil com fornecedor antes de fechar o número final.
