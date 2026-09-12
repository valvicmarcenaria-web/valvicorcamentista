# ⭐ MODELO DE CUSTO E MARGEM DE CONTRIBUIÇÃO — FONTE ÚNICA

> **Cravado pelo Jonathan em 12/09/2026.** Este arquivo é a **fonte de verdade**
> do método. Onde `validacao-orcamento.md` e `notas-marcos-planilha.md`
> divergirem daqui, vale este. Implementado em **`projetos/motor_mc.py`** —
> nenhum motor redefine coeficiente de encargo, todos importam de lá.

> *"Nossa metodologia consiste em levantar todos os custos relacionados a um
> projeto a fim de se obter uma Margem de Contribuição específica que lhe é
> direcionada a cada projeto e nível de complexidade do projeto todo ou de um
> item específico do projeto."*

Duas consequências do enunciado, e as duas importam:

1. **A MC é escolhida, não descoberta.** Ela é *direcionada* ao projeto conforme
   a complexidade. O motor calcula o preço que entrega a MC escolhida.
2. **A MC pode ser por ITEM, não só por projeto.** "do projeto todo ou de um
   item específico" — um item mais complexo carrega MC maior que o vizinho.

---

## 1 · A cascata de encargos

Tudo abaixo é **percentual sobre o preço de venda**, em três degraus. A ordem
importa: cada degrau incide sobre o que sobrou do anterior.

### Degrau 1 — sobre o BRUTO (o preço cheio)

| Encargo | % | Quando |
|---|--:|---|
| **Nota fiscal** | **5,0%** | sempre |
| **Taxa de máquina de cartão** | **1,2% × nº de parcelas** | só quando a condição de pagamento oferece cartão |
| **Margem de erro** | **2,0%** | sempre |
| **Desgaste de serra e fresa** | **0,5%** | sempre |
| **Manutenção de máquinas** | **0,5%** | sempre |

> ⛔ **A taxa de cartão ACUMULA por parcela.** 1,2% é o custo de *cada* parcela
> sobre o valor total: em 6× são **7,2%**, em 10× são **12,0%**. Não é 1,2% uma
> vez. É o encargo mais pesado do modelo depois das comissões, e é o único que
> muda com a **condição de pagamento** — logo **preço de tabela com cartão não é
> o mesmo preço de tabela à vista**.

### Degrau 2 — sobre o LÍQUIDO

**LÍQUIDO = bruto − nota fiscal − taxa de cartão.** Só esses dois saem.

| Encargo | % do líquido | Quando |
|---|--:|---|
| **RT** (arquiteto/parceiro) | **10%** | quando há parceiro indicando |
| **Comissão de vendedor** | **10%** | quando há vendedor na venda |

> As duas dividem a **mesma base**. [Jonathan 12/09] — não é cascata entre elas.

### Degrau 3 — sobre o LÍQUIDO 2

**LÍQUIDO 2 = líquido − RT − comissão de vendedor.**

| Comissão de produção | % do líquido 2 |
|---|--:|
| Coordenação | 1,0% |
| Programação | 1,0% |
| Fabricação | 2,5% |
| Montagem | 2,5% |
| **total** | **7,0%** |

> ⛔ **Montagem e fabricação entram aqui, como COMISSÃO — nunca como dia de
> marceneiro no custo direto.** A equipe é salário fixo; lançar dia de montador
> conta a mesma mão de obra duas vezes. Ver `validacao-orcamento.md`.

### A base

```
BASE = 1 − (todos os encargos acima, como fração do preço)

PREÇO para uma MC alvo  =  custo_direto / (BASE − MC)
MC conferida de um preço =  BASE − custo_direto / preço
```

| Condição | BASE | MC máxima teórica |
|---|--:|--:|
| à vista · com RT e vendedor | **67,68%** | 67,7% |
| à vista · sem RT | **76,52%** | 76,5% |
| à vista · sem RT e sem vendedor | **85,35%** | 85,4% |
| cartão 6× · com RT e vendedor | **62,32%** | 62,3% |
| cartão 10× · com RT e vendedor | **58,75%** | 58,8% |
| cartão 10× · sem RT | **66,47%** | 66,5% |

**Piso da casa: MC 35%. Faixa ideal: 35–40%.** Abaixo do piso é decisão de
preço do Jonathan, declarada — nunca resultado de conta.

### ⛔ O acréscimo do cartão segura a MC em REAIS, nunca em percentual

**Corrigido pelo Jonathan em 12/09/2026:** *"por que o parcelamento no cartão
está ficando tão alto, 17% e 30%, se é apenas 1,2% por parcela? Em 10 parcelas
aumentaria só 12%. O cálculo está errado."*

Estava. Eu calculava o preço parcelado **segurando a MC percentual**:

```python
P = CD / (base(parcelas) − mc_pct)          # ⛔ +31% em 10×
```

Isso faz a **margem em reais SUBIR junto com o preço** — de R$ 17.755 para
R$ 23.271 no job da Luiza. Ou seja, **marca up o custo da operadora em vez de
repassá-lo**, e contradiz o que a própria proposta diz ao cliente.

```python
mc_rs = preco_avista * mc(preco_avista, CD)
P = (mc_rs + CD) / base(parcelas)           # ✅ +15% em 10×
```

| | à vista | 6× | 10× |
|---|--:|--:|--:|
| taxa nominal do cartão | — | 7,2% | 12,0% |
| **acréscimo correto** | — | **+8,5%** | **+15,2%** |
| MC em reais | 17.755 | **17.755** | **17.755** |
| ~~acréscimo errado (MC % constante)~~ | — | ~~+16,6%~~ | ~~+31,1%~~ |
| ~~MC em reais que isso gerava~~ | — | ~~20.699~~ | ~~23.271~~ |

**Por que o acréscimo (15,2%) é maior que a taxa nominal (12%)?** Porque a taxa
incide sobre o preço **já acrescido**, e porque nota fiscal, margem de erro,
serra, manutenção, RT e comissões também correm sobre o acréscimo. No exemplo:
a operadora leva R$ 7.183 e o preço sobe R$ 7.857 — os R$ 674 de diferença são
os demais encargos sobre o próprio acréscimo. É **gross-up, não margem**, e dá
para explicar isso ao cliente sem constrangimento.

Implementado em `motor_mc.preco_repasse()`.

---

## 2 · O levantamento do custo direto

Daqui para baixo é **por demanda de projeto** — nada é percentual, tudo é
levantado peça a peça.

### Custos logísticos — variáveis, por projeto OU por ambiente

- **Frete de compra de material**
- **Frete de entrega na obra**
- **Logística da equipe de montagem**

> São três linhas, não uma. Um job de três ambientes num apartamento e um job de
> um ambiente em três endereços têm logísticas opostas.

### Matéria-prima

| Linha | O que entra |
|---|---|
| **Material bruto** | MDF, compensado, lâminas, fórmicas |
| **Ferragens** | dobradiças, corrediças, articuladores, sistemas deslizantes, puxadores |
| **Dispositivos de montagem e insumos de fixação** | cavilha, cantoneira, VB, tambor, parafuso estrutural |
| **Consumíveis** | cola instantânea, parafusos, limpeza, acabamentos |
| **Embalagem** | **2% do custo direto do projeto** — ver nota |
| **Vidros e espelhos** | |
| **Material elétrico** | fita de LED, perfil, driver, sensor, cabo |
| **Acessórios** | escorredor de prato, divisor de acrílico, cabideiro, sapateira deslizante |

> ⛔ **[Jonathan 12/09] A EMBALAGEM SOMA, NÃO SUBSTITUI os consumíveis.** São
> coisas diferentes: consumível é cola, parafuso, limpeza e acabamento aplicados
> **no móvel** (os motores usam 6% de chapa + fita); embalagem é caixa, plástico
> e canto de proteção **para transportar** o móvel, 2% do custo direto. As duas
> linhas convivem.

> **Fita de borda e filetagem** entram no material bruto, em duas linhas
> separadas: a fita é insumo (R$/m) e a filetagem é aplicação (R$/m de máquina).
> **Usinagem** (cava, chanfro, meia esquadria, curva) é serviço de CNC por metro,
> também no material bruto.

### Mão de obra terceirizada

- **Acabamento** (laca, pintura, laqueamento)
- **Serralheiro**
- **Vidraceiro**

> Estofador e marmorista, quando entram, seguem a mesma lógica de terceirizado.
> **Pedra é quase sempre FORA do escopo** — conferir em cada job.

---

## 3 · ⛔ O que este modelo corrigiu (12/09/2026)

Os motores carregavam, cada um a sua cópia, `A_ = 0,162 · LIQF_ = 0,88 ·
B_ = 0,043`, com `BASE = 0,80016` e o RT descontado à parte. Decodificado:
NF 4% + cartão **8% fixo** + vendedor **3%** sobre o bruto, produção **4,3%**
sobre o líquido. **Não é o método.**

| Encargo | Motores até 11/09 | Método correto |
|---|--:|--:|
| Nota fiscal | 4% | **5%** |
| Cartão | 8% fixo, **sempre** | **1,2% × parcelas**, só com cartão |
| Comissão de vendedor | 3% | **10%** |
| Comissão de produção | 4,3% agregada | **7%**, aberta em quatro |
| Base da produção | líquido de NF e cartão | **líquido de NF, cartão, RT e vendedor** |
| Embalagem | não existia | **2% do custo direto** |

### O erro que isso produziu na MC reportada

| Job | preço | CD | tabela | MC que reportei | **MC real** | delta |
|---|--:|--:|---|--:|--:|--:|
| SPE Nova Lima 1 | 168.000 | 81.022 | à vista | 30,5% | **28,3%** | −2,2 |
| Eliuton 2ª fase | 141.800 | 45.640 | à vista | 39,0% | **35,5%** | −3,5 |
| Luiza e Raphael · Telescópica | 54.200 | 21.248 | à vista | 32,0% | **28,5%** | −3,5 |
| Luiza e Raphael · Hettich | 71.700 | 23.659 | à vista | 38,2% | **34,7%** | −3,5 |
| **Juliana · Gold** | 71.904 | 29.624 | **10× no cartão** | 38,8% | **25,3%** | **−13,5** |
| **Juliana · Essencial** | 60.921 | 27.844 | **10× no cartão** | 34,3% | **20,8%** | **−13,5** |

**À vista o erro é de 2 a 3,5 pontos.** Com **cartão em 10× como preço de
tabela é de 13,5 pontos** — e as propostas da casa lideram justamente com
"entrada 30% + até 10× no cartão" como valor de tabela. O motor nunca soube que
o cartão era variável, então cobrava 8% onde a realidade é 12%.

> ⛔ **A LIÇÃO:** a escada de pagamento não é desconto comercial, é **encargo
> diferente em cada degrau**. Cada linha da escada tem a sua BASE e, no mesmo
> preço, a sua MC. Se o cartão em 10× é o preço de tabela, ele tem de ser
> precificado como tal — ou o cartão entra como **acréscimo ao cliente**, que é
> o que a Lídia fez (+10% para 6×) e por isso ela não tem o problema.

---

## 4 · Como usar

```python
import motor_mc as M

CD = material + ferragens + terceirizados + logistica + acessorios
CD = M.com_embalagem(CD)                       # + 2% de embalagem

pv = M.preco(CD, mc=0.38, parcelas=0, rt=True)      # preço para MC alvo
mc = M.mc(168000, CD, parcelas=10, rt=False)        # MC de um preço fechado

for n, v in M.encargos(parcelas=10, rt=True).items():
    print(n, f'{v:.2%}')                            # abre a cascata
```

**Em toda proposta com escada de pagamento, rodar `M.mc()` em cada degrau** e
conferir se o degrau mais barato para a casa ainda passa do piso.
