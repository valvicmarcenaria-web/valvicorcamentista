# Levantamento — Portas + painéis do vão da escada (contato: Flávia Moacir)

> **Status:** 🟢 **REV.06** (`proposta-flavia-portas.pdf`, 2 págs) — entrou o nicho de
> escaninhos e o desconto foi para **R$ 1.950**. **R$ 15.000** fechado.

## ➕ REV.06 — nicho de escaninhos [Jonathan 07/08/2026]

**6 nichos** em **MDF Itapuã**, cada um com **porta e fechadura individuais** e
**usinagem para recebimento de correspondência**. Preço de venda **R$ 2.450**.

| | |
|---|--:|
| Portas e painéis do vão da escada | 14.500 |
| **Nicho de escaninhos** | **2.450** |
| Subtotal | 16.950 |
| ~~Desconto especial de 10%~~ | ~~−1.695~~ |
| **Desconto especial (11,5%)** | **−1.950** |
| **TOTAL** | **R$ 15.000** |

> **Fechado em R$ 15.000 [Jonathan 07/08].** Apresentei o desconto como **valor**
> (R$ 1.950) e não como percentual, porque 11,504% não fecha em número redondo — desse
> jeito a conta da página bate exatamente e o total sai limpo.

> **O desconto foi aplicado também sobre o escaninho.** É a leitura consistente com a
> mesa da Juliana, e é a única que deixa a matemática da página fechar à vista do
> cliente — a proposta mostra a composição inteira: dois itens, subtotal, desconto, total.
> **Se o escaninho não devia entrar no desconto**, o total é **R$ 15.500** (13.050 + 2.450)
> e a página precisa de outro arranjo. Diferença de R$ 245.

> ⚠️ **Sem levantamento.** O R$ 2.450 é preço de venda ditado, como a mesa da Juliana.
> Não apurei chapa, fechadura nem usinagem. Por ordem de grandeza — ~1 chapa de Itapuã,
> 6 fechaduras, 12 dobradiças, fita e a usinagem das 6 fendas — o custo deve ficar perto
> de **R$ 1.200**, o que daria MC próxima dos **27%** sobre os R$ 2.205 recebidos.
> Fica na mesma faixa apertada do restante do job.

> ⚠️ **A descida para R$ 15.000 cruza o piso.** Com o custo estimado do conjunto
> (6.659 apurado + ~1.200 do escaninho ≈ **7.859**), a MC sai de **~28,5%** a R$ 15.255
> para **~27,6%** a R$ 15.000. Os R$ 255 a mais de desconto custam **0,9 ponto** e põem o
> job **logo abaixo do piso de 28%** da casa. Não é queda grande, mas é uma linha
> cruzada — e como o custo do escaninho é estimativa, a margem real pode estar um pouco
> pior. Decisão comercial, registrada.

Na proposta o escaninho ganhou **bloco de destaque próprio**: *seis escaninhos, seis
chaves* — a correspondência de um morador não fica acessível ao outro, e a fenda usinada
na porta recebe carta com o nicho fechado. É o argumento que justifica fechadura
individual em vez de um nicho aberto.

## Histórico — REV.05

## 🔴 REV.05 — RETIFICAÇÃO [Jonathan 04/08/2026]

| | REV.04 (entregue) | REV.05 |
|---|---|---|
| Aberturas | **2 portas de giro** | **1 pivotante + 1 de correr** |
| Painel | 1 painel de complemento (241 cm) | **2 painéis fixos** (120,5 cada) |
| Pivotante | — | dobradiça invisível · cava · **com fechadura** |
| Correr | — | **RO82 duplo amortecimento** · cava · **sem fechadura** |
| Base | perfil de alumínio, só nas portas | **rodapé de alumínio fosco 30 mm**, portas **e** painéis |
| Material | MDF Ultra amadeirado fosco | **MDF Itapuã Ultra** |
| Prazo | 50 dias **úteis** | **até 45 dias corridos** |
| Preço | R$ 14.500 | **R$ 13.050** (−10% especial) |

Pagamento segue **50% + 50%**. Motor em `corte-flavia-portas-rev05.py`.

### Os 2 painéis já estavam lá — só não eram painéis

A REV.04 cortava o painel de 241 cm em **duas tiras de 120,5** porque 241 não cabe na
chapa em nenhuma orientação. Agora que o projeto pede **dois painéis fixos**, a emenda
central deixou de ser emenda: virou a junta entre duas peças. **Mesma área, mesmas 6
chapas** — e um problema de fabricação a menos.

### O que a retificação fez com o custo

| | REV.04 | REV.05 |
|---|--:|--:|
| Ferragens | 7 × IN600 + 2 fecho rolete = 1.900 | 4 × IN600 + fechadura + RO82 top + trilho = **1.850** |
| Rodapé de alumínio | 40 | **228** |
| Cava usinada (4,4 m) | — | **220** |
| Fita e sarrafo | 319 | 381 |
| **Custo direto** | **6.239** | **6.659** |

Trocar 3 dobradiças IN600 (R$ 750) pelo conjunto RO82 top + trilho (R$ 600) **baratearia**
— mas a fechadura, a cava e o rodapé de 30 mm devolvem tudo e mais um pouco: **+R$ 420**.

> ⚠️ **A MC cai de 37% para 29,0%.** O escopo cresceu R$ 420 e o desconto de 10% vem por
> cima. O motor, no escopo novo, pediria **R$ 15.500** de tabela — e com os mesmos 10%
> daria R$ 13.950. A R$ 13.050 estamos **R$ 900 abaixo** disso. Está acima do piso de 28%
> da casa, mas por pouco. Foi decisão comercial, registrada.

### ⚠️ Três preços que não vêm da base

| Item | Adotado | Origem |
|---|--:|---|
| Fechadura da pivotante | R$ 250 | **estimativa** — `ferragens.md` lista fechaduras como TODO |
| RO82 com duplo amortecimento | R$ 400 + R$ 200 de trilho | li como o **RO82 "top"** da base; se for RO82 padrão + kit de amortecedor, o número é próximo |
| Rodapé de alumínio fosco 30 mm | R$ 38/m | referência de perfil de alumínio de `chapas.md` (preto/bronze 38) |

---

## Histórico — REV.04 (substituída)

> **Status anterior:** proposta entregue com 2 portas de giro, R$ 14.500.
> Origem: WhatsApp (atendimento Jonathan), fotos do local (escada em concreto + hall de elevadores amadeirado) e medidas passadas em texto.

## REV.04 — fechamento
- **Dobradiça Häfele IN600 = R$ 250,00/un** (valor do anúncio, confirmado pelo cliente — substitui a
  estimativa de R$138,51 da pesquisa de mercado).
- **Valores arredondados para números cheios** na proposta final: Portas R$ 9.100 + Painel R$ 5.400 =
  **Total R$ 14.500** (cálculo bruto do motor: R$ 14.505,54 — MC efetiva ~37,0% mantida no arredondamento).
- **Pagamento 50% + 50%** (entrada na assinatura + saldo na entrega). **Prazo: 50 dias úteis.**
- Puxadores em cava nas 2 portas (sem ferragem aparente) — destacado na proposta.
- Destaques da proposta: **dobradiças Häfele IN600** (7 un, 4 na porta maior) e **proteção de
  alumínio na base** das portas.

## Leitura da conversa
- 14/07: foto da escada (vão subindo/descendo). Escopo: **porta no vão da escada subindo E porta no vão da escada descendo** — confirmado.
- 17/07: foto do hall de elevadores (referência estética amadeirada do prédio).
- "Vão de passagem da escada": **4,45×2,20** (medida do vão total, passada pela Flávia).
- 3 larguras de porta foram mencionadas (88/116/103); **confirmado nesta rodada: 116cm e 88cm**.

## Decisões confirmadas (REV.03)
1. **2 portas: 116cm e 88cm.**
2. **+ Painéis de complemento** — o vão de passagem (4,45m) menos as 2 portas (204cm) sobra
   **241cm de painel** (revestimento de parede, 1 face só — não é porta de giro) completando a composição.
3. **MDF Ultra amadeirado fosco 15mm.**
4. **Dobradiça Häfele IN600** (produto indicado pelo cliente) — regulagem 3D, até 60kg, espessura
   mín. porta 35mm, ângulo 180°, acabamento preto. Vendida por unidade.
5. **Perfil de alumínio na base: R$ 10,00/m** (valor passado pelo cliente).
6. **Porta maior (116cm) reforçada com 4 dobradiças** (peso calculado 66kg, acima dos 60kg nominais
   do IN600 — decisão do cliente de reforçar em vez de trocar de linha). Porta 88cm: 3 dobradiças (padrão).
7. **MC 37%, sem RT.**

## ⚠️ Premissa ainda aberta
- **Leitura do painel:** assumi que "os painéis" = a sobra do vão de 4,45m depois das 2 portas
  (241cm, 1 face). Se for outra coisa (ex.: painéis em outro ambiente, ou frente+verso), o número muda —
  confirmar antes de fabricar.
- **Fecho rolete** segue estimativa de mercado (sem link/produto do cliente ainda).
- **Nome do prédio/síndico não identificado.**

## Quantitativo (plano de corte real — não por m²)
> Chapa 275×185cm. Portas: peça 220×largura (o lado de 220cm corre no eixo de 275cm) — 116+88=204cm
> não cabe numa chapa (>185cm) → 1 chapa por face. Painel 220×241cm **excede as duas dimensões úteis**
> da chapa em qualquer orientação → dividido em 2 tiras de ~120,5cm (emenda central).

| Item | Dimensão | Área MDF | Peso | Chapas |
|---|---|--:|--:|---|
| Porta 1 | 220×116 (frente+verso) | 5,104 m² | 66,0 kg | 2 (1 por face) |
| Porta 2 | 220×88 (frente+verso) | 3,872 m² | 50,1 kg | 2 (1 por face) |
| Painel complemento | 220×241 (1 face) | 5,302 m² | — | 2 (2 tiras ~120,5cm) |
| **Total** | | **14,278 m²** | | **6 chapas MDF Ultra amadeirado fosco** |

Fita de borda: 22,10 m perímetro × 1,10 (perda) = **24,3 m**. Estrutura interna (sarrafo): **27,8 m**.
*(Nesting real pede 6 chapas — a conta ingênua por m²/aproveitamento indicaria só 4.)*

## Ferragem — dobradiça Häfele IN600
| Porta | Peso | Dobradiças | Observação |
|---|--:|--:|---|
| 1 (116cm) | 66,0 kg | **4 un** | Excede 60kg nominal do IN600 — reforçada (decisão cliente) |
| 2 (88cm) | 50,1 kg | 3 un | Dentro da capacidade nominal |
| **Total** | | **7 un** | |

## Custo de material (compra)

| Item | Qtd | Preço unit. | Total |
|---|--:|--:|--:|
| MDF Ultra amadeirado fosco 15mm | 6 chapas | R$ 580 | R$ 3.480 |
| Fita de borda | 24,3 m | R$ 4,00/m | R$ 97 |
| Dobradiça Häfele IN600 | 7 un | R$ 138,51 | R$ 970 |
| Fecho rolete *(estimativa)* | 2 un | R$ 75 | R$ 150 |
| Perfil alumínio base | 4 m (2 barras) | R$ 10/m | R$ 40 |
| Estrutura interna (sarrafo) | 27,8 m | R$ 8/m | R$ 222 |
| **Subtotal material** | | | **R$ 4.959** |
| Logística | | | R$ 300 |
| Visita técnica | | | R$ 200 |
| **Custo direto (fixedR)** | | | **R$ 5.459** |

## Precificação — MC 37%, sem RT
Motor oficial do validador: `inv = fixedR / (1 − a − liqF·b − mc)`, a=16,2%, liqF=0,88, b=4,3% (RT=0), mc=37% → divisor **0,43016**.

| | Valor |
|---|--:|
| **INVESTIMENTO TOTAL (2 portas + painel)** | **R$ 12.691** |
| Porta 1 (116cm) — 35,7% | R$ 4.537 |
| Porta 2 (88cm) — 27,1% | R$ 3.442 |
| Painel de complemento (241cm) — 37,1% | R$ 4.713 |

> Alocação proporcional por área de MDF — referencial. MC verificada = 37,0%. RT = 0%. Sem desconto.

## Entregáveis
- `corte-flavia-portas.py` — script de cálculo (quantitativo + plano de corte + peso + motor), reproduzível/auditável.

## Próximo passo
Tabela apresentada para aprovação. Após OK: cotar fecho rolete com fornecedor real, confirmar leitura
do painel (241cm) e montar a proposta visual (padrão comerciais Valvic).
