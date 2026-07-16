# Orçamento — GRAÇA · Marcenaria (Despensa + Lavanderia + Armário-tanque)

**Cliente:** Graça · **Projeto/arquiteta:** Lais Teles (autor da prancha: Marcus Juan) · **Data:** 16/07/2026
**Caderno:** 25 páginas A4 (paisagem), "Detalhamento" — sem data/rev. nos carimbos ("XX").
**Nota geral do projeto (verbatim):** *"PROJETO TODO EM MDF AZUL PETRÓLEO GUARARAPES"* · *"ARMÁRIO EXISTENTE (REVESTIR EM AZUL PETRÓLEO)"* · rodapé em todas: *"CONFERIR MEDIDAS NO LOCAL. ADAPTAR DE ACORDO COM A NECESSIDADE DO CLIENTE."*

## Escopo (3 ambientes · 4 conjuntos de marcenaria — tudo MDF Azul Petróleo Guararapes)

**Despensa**
- **B1 — Armário superior (EXISTENTE → revestir).** 163 L × 247 A cm; prof 50 (principal) + 18 (rasa esq.). Novas frentes de giro (2× 42×124 + porta esq. + porta cheia dir. 245 da coluna), laterais aparentes, 4 prateleiras (vão 84), coluna-nicho 30×196 com **2 pistões a gás**. Escopo = revestimento sobre a caixa existente (não refaz a caixa).
- **B2 — Bancada inferior (nova, em "L").** 154 L × 73 A × 61 P (+ retorno ~50). 2 gavetões 71×34, nichos (39×50 / 39×14 / 2× 38×32), coluna de **3 cestos aramados** p/ frutas e legumes. **LED perfil de embutir 3000 K centralizado.**

**Lavanderia**
- **B3 — Torre da máquina de lavar.** 84 L × 152 A × 67 P (prof escalonada 42+25). Vão da máquina 69×87, bancada de apoio, gaveteiro de produtos, gavetão de roupas 79×47, apoio extraível. Puxador **cava/perfil passante**.

**Armário-tanque**
- **B4 — Balcão do tanque.** 50 L × 65 A (68 c/ tampo) × 48 P. 2 portas de giro 24×64, prateleira interna. **Tampo de pedra + cuba/tanque = terceiro (marmorista), não incluso.**

## Cálculo (CALCULAR, não estimar) — `corte-graca.py`
Peça a peça, cotas do caderno. Construção Valvic: face/portas/gavetões/tampo e prat. visíveis = **cor (Azul Petróleo)**; caixaria interna = **Branco TX 15mm**; fundos = **6mm**. Chapa 2,75×1,85 = 5,0875 m²; aprov. 0,82 (15/18) e 0,55 (6).

**59 peças lançadas → 11 chapas = R$ 3.750** (Azul 18: 1 · Azul 15: 3 · Azul 6: 1 · Branco 15: 3 · Branco 6: 3).
Insumos: fita R$825 · cola/parafuso/minifix/cavilha R$660 · usinagem (cava passante + furações) R$450 · LED 3000 K (perfil+fita+fonte) R$300 · acessórios (2 pistões a gás + 3 cestos aramados) R$370 · visitas R$500 · logística R$300.
Ferragens por linha: **Telescópica** 7 pares × R$40 + 18 dobradiças × R$6 = **R$388** · **Hardt** 7 pares × R$70 + 18 dob. × R$8 = **R$634**.

**fixedR** — Essencial (Telescópica) R$ 7.543 · Essencial Prime (Hardt) R$ 7.789.

## Motor (COM cartão — pagamento padrão · RT 10% líq. arq. Lais Teles)
`inv = fixedR / (1 − a − liqF·b − mc)` · a=0,18 (nf4+parc8+vend3+erro2+serra0,5+manut0,5) · liqF=0,88 · b=0,143 (prog0,8+coord1+marc2,5+**rt10**) → **denominador = 0,69416 − mc**.

| Linha | Ferragem / garantia | MC | Cálculo | **Cravado** |
|---|---|---|---|---|
| **Essencial** | Telescópica · **2 anos** | 35% | R$ 21.917 | **R$ 21.900** |
| **Essencial Prime** | Hardt (oculta alemã) · **5 anos** | 38% | R$ 24.793 | **R$ 24.800** |

**Alocação por ambiente** (proporcional ao material direto): Despensa 67,6% (14,8k/16,8k) · Lavanderia 26,4% (5,8k/6,5k) · Tanque 6,0% (1,3k/1,5k).

## Decisões & premissas (sinalizadas na proposta)
- **Diferenciação por modelo/garantia, não por marca** (regra da casa): Essencial = telescópica/2a; Essencial Prime = "oculta alemã"/5a (Hardt não é citado pelo nome ao cliente).
- **Cor interna:** base = caixaria interna Branco TX (padrão); a nota "todo em Azul Petróleo" vale p/ as superfícies aparentes. Interior integral em Azul Petróleo **sob consulta** (delta material ~R$1.050 → ~R$1.500 cliente).
- **B1 revestir:** novas frentes + laterais aparentes + prateleiras + nicho; **não** refaz a caixa existente.
- **Tampo da bancada da despensa:** considerado MDF; se pedra → sai p/ marmorista.
- **RT 10% líquido** embutido no preço (não aparece como linha ao cliente).
- **Pagamento:** escala padrão Valvic (30% até 10× · 50% até 8× −3% · 70% até 6× −5% · 70% + transf. −7%). **Prazo 60–90 dias corridos.** Validade 15 dias.

## Não inclusos (ditos na proposta)
Tampo/cuba de pedra e inox do armário-tanque (marmorista) · máquina de lavar (eletrodoméstico do cliente) · pontos hidráulicos/elétricos de alimentação.

## Flags a confirmar (do caderno)
1. Nº exato de folhas do armário superior da despensa (isométricas ~3, lateral ~4) — é existente a revestir.
2. Largura da bancada da despensa: 136 (raw_02) vs **154** (demais) — adotado 154.
3. Cestos vs nichos com perfil metálico na coluna direita da despensa.
4. Material do tampo da bancada da despensa (MDF vs pedra).
5. Modelo de puxador na despensa e no tanque (só a lavanderia especifica cava passante).

## Arquivos
`corte-graca.py` (cálculo) · `build-graca.py` (montagem) · `proposta-graca.html/.pdf` (3 págs) · `orcamento-graca.json` · imagens `img-graca-{despensa,lavanderia,tanque}.png` (renders do cliente recortados).
