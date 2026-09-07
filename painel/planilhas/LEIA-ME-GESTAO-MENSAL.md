# Valvic — Gestão Mensal 2026 (acompanhamento com o Walton)

**Arquivo:** `Valvic_Gestao_Mensal_2026.xlsx`
**Gerador:** `gerar-gestao-mensal-walton.py` — **edite o script, nunca o `.xlsx`**, senão a
próxima geração apaga a mudança.
**Testes:** `testar-gestao-mensal.py` — 81 checagens, e não são de fachada: o teste preenche
um exemplo, manda o **LibreOffice recalcular de verdade** e confere cada número contra a
conta feita na mão.
**Desenho:** `painel/esquema-planilha-walton.html` (lâmina A3 que foi aprovada antes de
construir).

---

## O que ela responde

O que aconteceu na empresa em cada mês, em **competência**: quanto se vendeu, quanto de
material virou móvel, quanto se fabricou, quanto se instalou e quanto se faturou — mais o
custo fixo do mês.

**O que ela não responde:** se o dinheiro entrou na conta. Isto não é caixa. As colunas de
**mês do recebimento** (Faturamento) e de **parcelas** (Compras) já existem para o dia em
que o Walton pedir a visão de caixa, e por isso ela não vai precisar ser refeita.

---

## As duas decisões que explicam a planilha inteira

**1 · A unidade de lançamento é o ambiente, não o projeto.**
Projeto nunca fica "fabricado" — fica fabricado aos pedaços. Se a unidade fosse o projeto,
seria preciso estimar percentual ("a cozinha está uns 60%"), e percentual estimado é onde o
número vira opinião. Ambiente fica pronto ou não fica.

**2 · Material entra pelo uso, não pela data da compra.**
A compra é lançada inteira, com o projeto. A planilha a **rateia entre os ambientes daquele
projeto, na proporção do valor de cada um**, e o material de cada ambiente conta **no mês em
que aquele ambiente foi fabricado**. É por isso que "material ÷ fabricado" é uma margem de
verdade, e não uma coincidência de calendário.

---

## As abas

| Aba | O que é |
|---|---|
| **Instruções** | As definições de quando cada coisa conta. É o que impede o número de mudar conforme quem preenche |
| **Projetos** | Um contrato por linha. Traz a conferência **Σ ambientes × valor do contrato** |
| **Ambientes** | **O coração.** Um ambiente por linha, com valor, mês fabricado e mês instalado |
| **Faturamento** | Uma nota por linha |
| **Compras** | Uma nota por linha. Sem projeto = material de uso geral |
| **Custo Fixo** | Um mês por linha: folha, estrutura e frota — as mesmas rubricas já apresentadas ao Walton |
| **Jan … Dez** | 12 lâminas, cada uma com o dashboard do mês. **Não se digita nelas** |
| **Ano 2026** | Os doze meses lado a lado. É onde se lê tendência |
| **Listas** | Alimenta o cálculo do nº do mês. Não apague nem reordene a coluna Meses |

**Fundo creme = você digita. Fundo azul-claro = calculado** — digitar por cima apaga a
fórmula.

---

## O dashboard de cada mês

**Seis números:** custo fixo · R$ vendido · material aplicado · R$ fabricado ·
R$ instalado · R$ faturado.

**Seis leituras** — é aqui que a planilha deixa de ser relatório:

| Leitura | A conta | O que responde |
|---|---|---|
| Material comprado | compras do mês | quanto de compromisso a empresa assumiu (com a parte de uso geral logo abaixo) |
| **Material em estoque** | comprado **de projeto** acum. − aplicado acum. | quanto está parado no galpão. **É o número que explica caixa curto com resultado bom** |
| Material sobre o fabricado | aplicado ÷ fabricado | o termômetro da margem bruta |
| Parado na fábrica | fabricado − instalado | móvel pronto esperando obra |
| A faturar | instalado − faturado | entregue e ainda sem nota |
| Carteira a produzir | vendido acum. − fabricado acum. | trabalho que a fábrica já tem contratado |

E, abaixo, a quebra por projeto: de onde saiu cada número do mês, para o Walton conferir sem
precisar perguntar.

---

## Três coisas que valem saber antes de usar

**O estoque só olha compra vinculada a projeto.** Material de uso geral — fita, cola,
parafuso, lixa, ferramenta — nunca é aplicado a ambiente nenhum. Se entrasse na conta do
estoque, ficaria acumulando mês a mês e fingiria estoque que não existe. Ele aparece à parte,
na linha do material comprado.

**Ambiente que atravessa o mês conta inteiro no mês em que ficou pronto.** Se um ambiente é
grande demais para caber num mês, o caminho certo é **quebrá-lo em dois ambientes** — e não
lançar percentual, que traria de volta a estimativa que o lançamento por ambiente veio
resolver.

**O rateio por valor é aproximação.** Cozinha consome mais material por real que um home com
prateleira simples, então o rateio erra um pouco para cada lado dentro do mesmo projeto; no
total do mês se compensa. Quando você souber o material real de um ambiente, informe na
coluna **Material apurado**: aquele ambiente passa a usar o valor informado e o rateio se
aplica só ao que sobrou. Se as compras do projeto passarem da soma dos valores apurados, a
diferença fica registrada como estoque — que é o comportamento certo, mas convém saber.

---

## Por que não existe menu suspenso no campo Projeto

A lista de projetos passaria dos **255 caracteres** que uma lista literal aceita, e cresce ao
longo do ano. E lista literal é o único formato que sobrevive à importação no Google Sheets —
intervalo de outra aba e nome definido são descartados, foi assim que a planilha de custos
saiu sem menu nenhum.

No lugar do menu há duas redes: a coluna **Aviso** na aba Ambientes acende quando o nome
digitado não está cadastrado em Projetos, e a conferência **Σ ambientes × contrato** pega o
mesmo erro por outro caminho.

---

## Rodar de novo

```bash
cd painel/planilhas
python3 gerar-gestao-mensal-walton.py     # regera o .xlsx do zero
python3 testar-gestao-mensal.py           # 81 checagens, com recálculo real
```

O teste exige o **LibreOffice Calc** instalado (`apt-get install libreoffice-calc`). Ele cria
um perfil próprio e liga o recálculo forçado — sem isso o LibreOffice abriria o arquivo sem
calcular nada e o teste passaria a testar coisa nenhuma.
