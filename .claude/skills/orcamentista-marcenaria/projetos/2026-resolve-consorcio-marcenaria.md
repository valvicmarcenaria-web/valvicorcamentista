# Resolve Consórcio — Marcenaria completa (escritório comercial)

**Cliente:** Resolve Consórcio · **Decoradora/parceira:** Jéssica Sollero · **Engenharia:** Corsino Soares
**Caderno:** 11/06/2026 (54 pranchas) · **Perfil:** comercial (corporativo) · **Escopo:** orçar **só o que está descrito**
**Status (v3):** 🟢 **CHAPAS CALCULADAS peça-a-peça** (`corte-resolve-consorcio.py`, 257 peças) — **79 chapas · R$ 29.770**.
Ripado = produto Eucatex (calculado por área/rendimento). **Custo de material Valvic ≈ R$ 56.700 (base Hardt) · R$ 62.600 (Hettich)**, sem fechaduras.
**Unidade:** CHAPAS (plano de corte real) + ripado como produto Eucatex.

> **Histórico:** v1 estimativa 106 chapas (alta) · v2 estimativa 49 (baixa) · **v3 CÁLCULO 79** (o número real).
> Lição cravada na skill: **calcular, nunca estimar.** Fechaduras dos lockers = **NÃO inclusas** (fornecimento à parte).

## Escopo (14 ambientes descritos)
Recepção · Sala Reunião · Convivência · Coffe Point · Descompressão · Refeitório · Jurídico (planta "Gestão") ·
Compliance · **Circulação (63 lockers)** · Comercial · Sala Reunião Colab · Sala CEO · CALL · **Cabines CALL (7 acústicas)**.

**Paleta MDF:** **Grafito Chess** (Arauco) — dominante · **Freijó Brasil** (Eucatex) — ripado (produto) + painéis lisos ·
**Carvalho Americano** (Arauco) — básculas refeitório · **Azul Austral / Azul Secreto** (Duratex) + **Azul Petróleo**
(Guararapes) — portas dos lockers/CALL · interno **Branco TX**. Tudo em **½ esquadria**; "puxador chanfrado" = **cava usinada**.

## ① RIPADO — produto Eucatex (referência de custo real, da internet)
**Painel Ripado Eucatex RU Freijó Brasil** = caixa de **6 barras de encaixe**, barra **55 × 2.700 × 12 mm**,
**rende 0,75 m²/caixa**, **R$ 166,50/caixa** (Estilo Home Center; faixa R$ 158–183). É produto **pronto e pré-acabado**
(obra seca, encaixe macho-fêmea) — **não leva chapa de fundo nem fita**; só acabamento em **perfil L** nas bordas aparentes.
- **Paredes ripadas (Freijó Brasil):** Recepção ~8,4 m² · Convivência 7,4 m² · Sala Reunião Colab 7,9 m² ·
  Compliance ~5 m² ⚠️ · Comercial ~5 m² ⚠️ → **≈ 34 m²** (larguras de Compliance/Comercial a confirmar).
- **34 m² ÷ 0,75 = ~46 caixas × R$ 166,50 = R$ 7.660** + perfis L (~R$ 600) → **≈ R$ 8.300.**

## ② CHAPAS MDF — **CALCULADO peça-a-peça** (não estimado)
**Método:** `corte-resolve-consorcio.py` — **257 peças** decompostas (cada L×A), área somada por cor×espessura,
chapas = área ÷ (5,0875 m² × aproveitamento **0,82** p/ 15-18mm · **0,55** p/ 6mm — fatores da skill). **Conta aberta e auditável.**
Premissas de construção explícitas: face/portas/gavetões = cor 18mm · tampo/prateleira visível/jardineira/banco = cor 15mm ·
caixaria interna + lat/contrafrente de gaveta = Branco TX 15mm · fundos = 6mm · banco suspenso (sem encosto/base MDF) ·
prateleira "esp 5" = painel 15mm + fascia (vão 347 leva reforço) · mesa de cabine = só tampo (pé é tubo metálico, fora).

| Cor · esp | área (m²) | chapas | R$/ch | R$ |
|---|--:|--:|--:|--:|
| **Grafito 15** | 68,0 | 17 | 500 | 8.500 |
| **Grafito 18** | 12,0 | 3 | 600 | 1.800 |
| **Branco TX 15** | 84,8 | 21 | 260 | 5.460 |
| **Branco TX 6** | 51,1 | 19 | 190 | 3.610 |
| **Freijó liso 15** | 31,5 | 8 | 500 | 4.000 |
| **Azul Petróleo 18** | 8,5 | 3 | 600 | 1.800 |
| **Azul Austral 18** | 6,8 | 2 | 600 | 1.200 |
| **Azul Secreto 18** | 4,5 | 2 | 600 | 1.200 |
| **Carvalho Am. 15+18** | 3,2 | 2 | — | 1.100 |
| **"Similar" 15+18** | 2,4 | 2 | — | 1.100 |
| **TOTAL (calculado)** | | **79 chapas** | | **R$ 29.770** |

> ⚠️ **v1 (106) e v2 (49) eram ESTIMATIVAS — as duas erradas** (uma alta, uma baixa). Este **79 é cálculo**.
> Sensibilidade: o **Branco 6mm** usa o fator conservador da skill (0,55); com nesting apertado cai p/ ~13 chapas (−6). Confirmar no app.

## ③ Fita, ferragens, LED, insumos, terceirizados
- **Fita + filetagem ≈ R$ 5.000** (só as chapas; ripado não leva fita; muita ½ esquadria = + mão de obra, − fita).
- **Ferragens (CONTADAS do levantamento):** **87 portas · 23 gavetões** →
  - Dobradiças c/ amortecedor **176** + corrediças oculta **23 pares** → **base Hardt = 176×8 + 23×70 = R$ 3.018** · (Hettich = 176×35 + 23×120 = **R$ 8.920**).
  - Pistões a gás (básculas Refeitório) ~R$ 120.
  - **Usinagem** do "puxador chanfrado" (cava) nos armários + alça preta 70 cm (CALL) ≈ **R$ 2.000** (usinagem, não ferragem comprada).
  - 🚫 **FECHADURAS DIGITAIS (63× Papaiz M1602) — NÃO INCLUSAS** no escopo Valvic (fornecimento à parte, por conta do cliente). Ref. de mercado ~R$ 196,90/un = ~R$ 12.400 caso queiram incluir depois.
- **LED** (prateleiras Sala Reunião + Jurídico 3000K · básculas Refeitório 4000K · Colab) ~15–18 m + sensores ≈ **R$ 2.700**.
- **Insumos** (cola/PUR, parafusos/minifix/cantoneira, limpeza + embalagem — obra grande) ≈ **R$ 4.000**.

### Custo de MATERIAL Valvic (base Hardt) — SEM fechaduras
`chapas 29.770 (CALCULADO) + ripado 8.300 + fita ~6.000 + dobr./corr. Hardt 3.018 + pistões 120 + usinagem 2.000 + LED ~3.000 + insumos ~4.500`
→ **≈ R$ 56.700** (base Hardt) · com **Hettich** no lugar da variável: **≈ R$ 62.600**.
> **Fechaduras digitais FORA** (não inclusas). Se o cliente quiser incluir: +~R$ 12.400.
> **Chapas e ripado = CALCULADOS.** Fita, LED e insumos ainda a fechar por perímetro/metro linear (próximo passo do rigor).

### Terceirizados (à parte — não são material Valvic)
- **Blindex** das 7 cabines (4 giro + 3 correr) ≈ R$ 7.000 · **estofado** dos 7 bancos (tecido acústico) ≈ R$ 2.100 ·
  **pés de mesa em tubo metálico** (7) ≈ R$ 1.000 · escorredor metálico Refeitório ≈ R$ 200.
- ⛔ **CABINE ACÚSTICA (caixa + carpete + espuma acústica) = ESPECIALIDADE — cotar à parte.** Não dá pra estimar por chapa
  com o que o caderno traz; orcei só o **banco + mesa** (marcenaria) de cada cabine. A construção acústica da caixa é item próprio.

## Flags — o que NÃO está descrito / a confirmar
1. **Ripado — larguras de Compliance e Comercial** não claras nas elevações → área de ripado pode subir (mais caixas).
2. **Cabines acústicas:** caixa + carpete + espuma = especialidade, fora deste material (só banco/mesa entraram).
3. **Fechaduras digitais dos lockers = NÃO INCLUSAS** (fornecimento à parte). Fora do custo de material.
4. **Mesas orgânicas das cabines = tampo MDF + pé em tubo metálico** → só o tampo é marcenaria; o pé é serralheria (fora).
5. **Nº de chapas (~49) = ESTIMATIVA por área, não plano de corte fechado.** Para cravar, levantar peça-a-peça no app.
4. **Bancadas/tampos** (Refeitório, Coffe Point) **não especificados** → fora. **Jardineiras** só como caixa MDF (sem impermeabilização).
5. **Frigobares** (93L/45L) = eletrodoméstico, fora (o nicho é marcenaria).
6. **Materiais conflitantes:** jardineira Descompressão (Freijó × Grafito); **Jurídico × "Gestão"** (mesmo ambiente?).
7. **Elevações faltando:** Recepção Elev. C e Coffe Point Elev. B referenciadas e não desenhadas.
8. **"Similar ao existente"** (Refeitório) — cor/linha depende de amostra do local.
9. **Preços de compra:** ripado e fechadura vêm de **varejo web** (Valvic pode ter preço melhor no fornecedor). Chapas/ferragens = base da skill.
10. **Preço final / MC:** ainda **não** calculado — aguardando a Lavinia/Rodrigo definir margem, linhas e RT do comercial.

**Fontes de custo (web):** Ripado — estilohomecenter.com.br / leomadeiras.com.br / eucatex.com.br · Fechadura — loja.papaiz.com.br / amazon.com.br.
**Arquivos:** `orcamento-resolve-consorcio.json` · este `.md`. Caderno-fonte no upload da sessão.
