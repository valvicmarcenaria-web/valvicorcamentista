# HONDA · MINAS MOTOS SANTA EFIGÊNIA — marcenaria do showroom

**Data:** 07/08/2026 · **Script:** `corte-honda-minas-motos.py`
**Fonte:** `653_HON_EX_V1_AR18_R07.pdf` — prancha **AR-18**, projeto EXECUTIVO,
**Mímesis Arquitetura e Interiores** (CAU-MG PJ34.285-8), rev. **07 de 06/08/2026**
(*"ALTERAÇÃO SHOWROOM"* — emitida ontem, liberada para obra).
**Cliente:** Aliança Imobiliária Ltda. · **Obra:** Av. do Contorno, 3585 — Santa Efigênia, BH/MG.
**Responsável técnico:** Arq. Cleverson Sousa · **Desenhista:** Marina Assis.

---

## O escopo de marcenaria são DUAS peças — e só duas

A prancha traz **duas tabelas separadas**, e essa separação é o orçamento:

| Tabela | Conteúdo | É nosso? |
|---|---|:--:|
| **ESPECIFICAÇÃO DE MOBILIÁRIO** | MB01 a MB40 — padrão Honda, Home Office, Leroy Merlin, Madeira Madeira, Amazon | ❌ comprado |
| **ESPECIFICAÇÃO DE MARCENARIA** | **MA-01** e **MA-02** | ✅ |

Fora também: **BG07** (bancada — outra disciplina), a **cervejeira** e a **adega**
(projetadas em tracejado na VISTA 01, ficam nos 81,5 cm ao lado do móvel), o
**elevador de motocicleta**, os **displays Pro Honda** e o **balcão de peças** —
todos padrão Honda.

---

## Geometria — lida dos vetores do PDF, não do olho

Escala aferida **no próprio desenho**: 1,134 pt/cm (= 1/25 exato). Cada linha do
DWG foi extraída em coordenada e convertida. As cotas anotadas conferem com o
traçado em **todas** as cadeias — largura, altura e a planta.

### MA-01 — Armário superior · MDF **Amêndola Rústica** (Duratex) · prof. 30

```
Largura 315,5 = [2+2+2] + 69,5 + 70 + 70 + [2+2+2] + 88 + [2+2+2]
```

Os três grupos de `2+2+2` são as três **prumadas**: MDF 2 · **metalon 2** · MDF 2.
Foi o que revelou que o metalon não é enfeite — é a estrutura que carrega as
prateleiras abertas.

Alturas apuradas do piso acabado: topo **224** · fundo do caixote **184** ·
prateleira longa **154** · prateleira do vão direito **122** · bancada BG07 **90**.
Metalon esquerdo 225,9→150,0; do meio e da direita 225,9→118,0.

| | |
|---|---|
| Caixote A | 213 × 40 × 30 — **3 básculas** de 69,5 / 70 / 70 (vão livre 209,2) |
| Caixote B | 92 × 40 × 30 — **nicho aberto** 88 × 36, interior todo aparente |
| Prateleiras | 213 (alta) · 92 (alta) · 92 (baixa), apoiadas no metalon |

### MA-02 — Armário inferior em "L" · MDF **Palha** (Duratex) · alt. 84

Altura 84 = sóculo 10 + corpo 74 (tampo 2 + frentes 72).

**A VISTA 01 está espelhada em relação à planta.** Conferido por dois caminhos
independentes antes de aceitar:
1. o módulo hachurado de 55 na ponta **direita** da elevação é a perna B em corte,
   e na planta a perna B está à **esquerda**;
2. a sequência de módulos da planta (39,9 | 75,9 | 51,9) só fecha com as frentes
   da elevação (39 | 39+39 | gaveteiro 55) **lida ao contrário**.

Bate nos dois. E fecha a terceira ponta: a cervejeira e a adega, tracejadas à
esquerda da elevação, caem exatamente nos 81,5 cm que na planta sobram **à
direita** do móvel, até a parede.

| | |
|---|---|
| Perna A (VISTA 01) | corpo 173,9 × 57 prof — **3 portas de 39** + **gaveteiro de 55 com 4 gavetas de 16,5** |
| Perna B (VISTA 02) | corpo 141,5 × 60 prof — **portas de 46 / 46 / 45,5** + 60,8 de **canto cego** |

Extensão total: perna A **234** · perna B **202** — ambas incluem o canto, que é
contado **uma vez só** (na B). Frentes somadas 173,9 + 141,5 = 315,4.

**Puxador:** cava embutida usinada na própria frente — DT-01 (inferior, nas
básculas do MA-01) e DT-02 (superior com tampo, no MA-02). **Não é perfil comprado.**

---

## Quantitativo

| Material | Área | Chapas | Aprov. |
|---|--:|--:|--:|
| Amêndola Rústica 18 | 3,98 m² | 1 | 78% |
| Palha 18 | 5,32 m² | 2 | 52% |
| Branco 15 | 7,61 m² | 2 | 75% |
| Branco 18 | 1,41 m² | 1 | 28% |
| Branco 6 | 4,57 m² | 2 | 45% |
| **TOTAL** | **22,89 m²** | **8** | **56%** |

MA-01 5,69 m² · MA-02 17,20 m². Fita **73,13 m** (50,47 cor + 22,66 branco).

Ferragens: 12 dobradiças Sensys c/ amortecimento · 6 pistões a gás · 4 corrediças
ocultas Hardt · 6,84 m de cava usinada · 8 pontos de fixação invisível.
Terceirizado: **serralheria do metalon R$ 1.200** ⚠ estimado.

**CUSTO DIRETO: R$ 9.199,01**

---

## 🔧 O nesting errou de novo — e desta vez a varredura de ordens não salvou

O Amêndola consolidado dá 3,98 m² = **78% de UMA chapa**, e o packer insistia em 2
nas quatro ordens. Empacotado à mão fecha em 1, com 166 dos 185 cm usados.

**Causa:** o `_pack` por faixas só tenta a **última faixa aberta** — quando entra
uma peça larga no meio da fila, ele abre faixa nova e abandona a sobra de todas as
anteriores. Nenhuma ordenação conserta isso.

**Correção:** segundo empacotador **best-fit**, que procura a melhor faixa já
aberta em qualquer chapa. Registrado em `referencias/quantitativo.md` como padrão
da casa. No mesmo job ele ainda derrubou o Branco 15 de 3 para 2 chapas.

Somado à **consolidação de espessura dentro da cor** (Amêndola 15+18 → só 18;
Palha 15+18 → só 18), o efeito foi:

| | Chapas | Custo de chapa |
|---|--:|--:|
| Antes | 11 | R$ 4.290 |
| **Depois** | **8** | **R$ 3.030** |

Ordem importa: consolidar o Amêndola **antes** de corrigir o packer custava R$ 100
a mais. Testar, não supor.

---

## Preço — MC 35% · sem RT · divisor 0,45016

| | Custo direto | Investimento |
|---|--:|--:|
| **MA-01** — Armário superior | 3.454,11 | **R$ 7.700** |
| **MA-02** — Armário inferior em "L" | 5.744,90 | **R$ 12.800** |
| **TOTAL** | **9.199,01** | **R$ 20.500** |

MC conferida **35,1%**. Escada: −3% 19.900 · −5% 19.500 · −7% **19.100**
(no pior degrau a MC ainda fica em **31,9%**, acima do piso de 28%).

Base MC 35% sem RT segue o precedente do **SPE Nova Lima** — também comercial,
também executivo de escritório de arquitetura.

### Sensibilidade — a RT continua pesando mais que a MC

| | sem RT | com RT 10% |
|---|--:|--:|
| MC 30% | 18.400 | 22.300 |
| **MC 35%** | **20.400** | 25.400 |
| MC 40% | 23.000 | 29.500 |

### Sanidade — R$ por m² de chapa

| Job | R$/m² |
|---|--:|
| Cozinha Rizzi (residencial) | 626 |
| Armário superior de cozinha | 647 |
| SPE decorado (comercial) | 739 |
| **→ Honda showroom** | **895** |

Acima da faixa **por ser job pequeno com custo fixo alto**: serralheria, fixação
invisível e 3 dias de instalação somam **49% do custo direto** (R$ 4.500 de
R$ 9.199). Não é levantamento inflado — é o piso de custo de mobilizar uma equipe
para dois móveis num canteiro comercial no Contorno.

---

## ⚠️ Aberto — precisa da palavra do Jonathan

1. **RT.** O executivo é da Mímesis. Tem RT de 10%? É a maior alavanca daqui
   (R$ 20.500 → R$ 25.400 na mesma MC).
2. **Preço de compra da chapa Duratex Amêndola Rústica e Palha.** Usei a linha
   Fosco (18 mm R$ 600). Rústica texturizada costuma custar acima disso.
3. **Serralheria do metalon — R$ 1.200 é estimativa minha.** A casa não tem tabela
   para metalon 20×20 com pintura eletrostática. Cotar.
4. **Tampo do MA-02.** O DT-02 chama de *"bancada/tampo do móvel"*. Orcei em MDF
   Palha 18. Se for pedra (a prancha tem BG07 = bancada, outra disciplina), sai do
   escopo e o custo cai.
5. **Parede de fixação do MA-01.** 3,15 m de aéreo em balanço com **fixação
   invisível**. A nota 2 da prancha manda conferir se é drywall — se for, exige
   reforço estrutural que não está no preço.

## Premissas assumidas (não estão na prancha)

- **Interno branco**, exceto o nicho do MA-01, que é aberto e vai todo na cor.
- **2 divisórias internas** no caixote A do MA-01 — a prancha desenha um vão de
  209 cm sem apoio, que empenaria tampo e base. Caem atrás das básculas fechadas.
- **1 prateleira por módulo de porta** no MA-02 (4 no total) — a prancha não desenha.
- **Travessa de metalon** sob a prateleira longa de 213 cm do MA-01, já dentro do
  pacote de serralheria. Em 18 mm com vão livre de 213 ela flexiona.
