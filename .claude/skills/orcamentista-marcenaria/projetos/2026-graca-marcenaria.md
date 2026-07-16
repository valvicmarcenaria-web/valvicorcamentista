# Orçamento — GRAÇA · Marcenaria (Despensa + Lavanderia + Armário-tanque)

**Cliente:** Graça · **Projeto/arquiteta:** Lais Teles (autor da prancha: Marcus Juan) · **Data:** 16/07/2026
**Caderno:** 25 páginas A4 (paisagem), "Detalhamento" — sem data/rev. nos carimbos ("XX").
**Nota geral do projeto (verbatim):** *"PROJETO TODO EM MDF AZUL PETRÓLEO GUARARAPES"* · *"ARMÁRIO EXISTENTE (REVESTIR EM AZUL PETRÓLEO)"* · rodapé em todas: *"CONFERIR MEDIDAS NO LOCAL. ADAPTAR DE ACORDO COM A NECESSIDADE DO CLIENTE."*

> **Rev. 16/07 (tarde) — 3 ajustes do Jonathan:** (1) **projeto 100% Azul Petróleo** — nada de Branco TX na caixaria/fundos; (2) **tampo da bancada da despensa é pedra** (marmorista, fora), como o do tanque; (3) **margem 32%** e **nesting unificado do projeto inteiro** (tudo uma cor → pilhas somadas → menos chapa).

## Escopo (3 ambientes · 4 conjuntos de marcenaria — tudo MDF Azul Petróleo Guararapes)

**Despensa**
- **B1 — Armário superior (EXISTENTE → revestir).** 163 L × 247 A cm; prof 50 (principal) + 18 (rasa esq.). Novas frentes de giro (2× 42×124 + porta esq. + porta cheia dir. 245 da coluna), laterais aparentes, 4 prateleiras (vão 84), coluna-nicho 30×196 com **2 pistões a gás**. Escopo = revestimento sobre a caixa existente.
- **B2 — Bancada inferior (nova, em "L").** 154 L × 73 A × 61 P (+ retorno ~50). 2 gavetões 71×34, nichos (39×50 / 39×14 / 2× 38×32), coluna de **3 cestos aramados** p/ frutas e legumes. **LED perfil de embutir 3000 K centralizado.** **Tampo = pedra (marmorista, fora).**

**Lavanderia**
- **B3 — Torre da máquina de lavar.** 84 L × 152 A × 67 P (prof escalonada 42+25). Vão da máquina 69×87, bancada de apoio, gaveteiro de produtos, gavetão de roupas 79×47, apoio extraível. Puxador **cava/perfil passante**.

**Armário-tanque**
- **B4 — Balcão do tanque.** 50 L × 65 A (68 c/ tampo) × 48 P. 2 portas de giro 24×64, prateleira interna. **Tampo de pedra + cuba/tanque = terceiro (marmorista), não incluso.**

## Cálculo (CALCULAR, não estimar) — `corte-graca.py`
Peça a peça, cotas do caderno. **Projeto 100% Azul Petróleo** (aparente e caixaria); fundos 6mm. Como tudo é a mesma cor, o **nesting é unificado** (pilhas de 15 e de 6 mm somadas no projeto inteiro → menos rounding de chapa). Chapa 2,75×1,85 = 5,0875 m²; aprov. 0,82 (15/18) e 0,55 (6).

**57 peças lançadas → 9 chapas = R$ 4.000** (Azul 15: 5 · Azul 18: 1 · Azul 6: 3). *(Antes, com caixaria Branca + tampo MDF: 11 chapas R$ 3.750. A unificação de cor tirou 1 chapa, o tampo em pedra tirou outra → 9. Custo sobe ~R$ 250 porque tudo é Azul, mais cara que a Branca.)*
Insumos: fita R$675 · cola/parafuso/minifix/cavilha R$540 · usinagem (cava passante + furações) R$450 · LED 3000 K (perfil+fita+fonte) R$300 · acessórios (2 pistões a gás + 3 cestos aramados) R$370 · visitas R$500 · logística R$300.
Ferragens por linha: **Telescópica** 7 pares × R$40 + 18 dobradiças × R$6 = **R$388** · **Hardt** 7 pares × R$70 + 18 dob. × R$8 = **R$634**.

**fixedR** — Essencial (Telescópica) R$ 7.523 · Essencial Prime (Hardt) R$ 7.769.

## Motor (COM cartão — pagamento padrão · RT 10% líq. arq. Lais Teles)
`inv = fixedR / (1 − a − liqF·b − mc)` · a=0,18 · liqF=0,88 · b=0,143 (rt10) → **denominador = 0,69416 − mc**.

| Linha | Ferragem / garantia | MC | Cálculo | **Cravado** |
|---|---|---|---|---|
| **Essencial** | Telescópica · **2 anos** | 32% | R$ 20.106 | **R$ 20.100** |
| **Essencial Prime** | Hardt (oculta alemã) · **5 anos** | 32% | R$ 20.764 | **R$ 20.800** |

Margem unificada 32% → as linhas diferem só pela ferragem (gap ~R$ 700). **⚠️ 32% está abaixo do piso de caixa do Rodrigo** (exceção 37%, ideal 43%+) — decisão do Jonathan.
**Alocação por ambiente** (proporcional ao material direto): Despensa 64,4% (12,9k/13,4k) · Lavanderia 29,1% (5,9k/6,1k) · Tanque 6,5% (1,3k/1,3k).

## Decisões & premissas (sinalizadas na proposta)
- **Diferenciação por modelo/garantia, não por marca:** Essencial = telescópica/2a; Essencial Prime = "oculta alemã"/5a.
- **Cor:** projeto **100% Azul Petróleo** (aparente + caixaria + fundos). Sem Branco TX.
- **B1 revestir:** novas frentes + laterais aparentes + prateleiras + nicho; não refaz a caixa existente.
- **Tampos de pedra** (bancada da despensa + tanque) = marmorista, **fora**.
- **RT 10% líquido** embutido no preço (não aparece como linha ao cliente).
- **Pagamento:** escala padrão Valvic (30% até 10× · 50% até 8× −3% · 70% até 6× −5% · 70% + transf. −7%). **Prazo 60–90 dias.** Validade 15 dias.

## Não inclusos (ditos na proposta)
Tampos de pedra e cuba/inox (bancada da despensa + armário-tanque, marmorista) · máquina de lavar (eletrodoméstico do cliente) · pontos hidráulicos/elétricos de alimentação.

## Flags a confirmar (do caderno)
1. Nº exato de folhas do armário superior da despensa (isométricas ~3, lateral ~4) — é existente a revestir.
2. Largura da bancada da despensa: 136 (raw_02) vs **154** (demais) — adotado 154.
3. Cestos vs nichos com perfil metálico na coluna direita da despensa.
4. Modelo de puxador na despensa e no tanque (só a lavanderia especifica cava passante).

## Arquivos
`corte-graca.py` (cálculo) · `build-graca.py` (montagem) · `proposta-graca.html/.pdf` (3 págs) · `orcamento-graca.json` · imagens `img-graca-{despensa,lavanderia,tanque}.png` (renders do cliente recortados).
