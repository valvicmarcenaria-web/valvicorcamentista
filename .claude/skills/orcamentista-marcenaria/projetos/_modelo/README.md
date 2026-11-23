# A PLANILHA BASE DA VALVIC — o modelo de onde todo orçamento sai

**Modelo:** `11IgmtI5Xd8pshHvYpYvejzas0OemHbyw9Jqwd5SPN38`
https://docs.google.com/spreadsheets/d/11IgmtI5Xd8pshHvYpYvejzas0OemHbyw9Jqwd5SPN38/edit
Mora em **Orçamentos Valvic**, ao lado dos orçamentos.

## ⛔⛔ Por que ela existe

Porque eu comecei o orçamento do Gustavo **copiando a planilha do Michell**, e isso
estava errado por dois motivos [Jonathan, 29/10/2026]:

> *"não pode haver informações relacionadas ao orçamento do michell, é outro cliente.
> crie uma planilha base (vazia apenas com uma aba de ambiente para ser replicada
> quando necessário)."*

1. **Dado de outro cliente.** Não se copia orçamento de cliente para começar outro.
2. **Erro em cadeia.** Copiar planilha com `IMPORTRANGE` quebra o vínculo, e a
   planilha inteira vira `#DIV/0!`.

## ⛔⛔ O PRIMEIRO PASSO DE TODA CÓPIA, SEMPRE

Abrir a aba `Base (importada)` e clicar no **`#REF!` da célula D3**, depois em
**Permitir acesso**. Um clique. ⭐ O aviso está escrito ali ao lado, em vermelho, e
no topo do Painel. ⛔ Nenhum script pode dar essa autorização — é trava de segurança
do Google, por par (origem, destino). **Vale para toda cópia nova.**

## As quatro abas

| aba | o que é |
|---|---|
| **Painel** | o resumo do projeto · ensina a sequência de trabalho no topo |
| **Preço e Comissões** | a cascata de encargos em três degraus, a MC e o preço por ambiente |
| **00 Ambiente (modelo)** | ⭐ a aba que se DUPLICA, uma por ambiente |
| **Base (importada)** | as 70 chaves da casa, com preço vindo da Base de Custos |

## ⭐⭐ O que mudou em relação à planilha do ICA

**O preço vem por NOME, não por posição.** Na do ICA a célula escrevia `=I19` e
torcia para que a linha 19 do bloco importado continuasse sendo o Melamínico Fosco
de 18 mm; a própria aba avisava *"LINHA NOVA VAI NO FIM, NUNCA NO MEIO"*. Isso é
bomba-relógio: basta alguém inserir uma linha na Base de Custos e todo orçamento
passa a somar errado, **calado**.

Aqui cada chave declara, nas colunas E e F, **o produto como ele se chama na Base** e
a espessura quando é chapa; a fórmula busca por esses dois critérios. Inserir,
remover ou reordenar linha na Base deixou de quebrar qualquer coisa. É a mesma lição
que o Painel já tinha aprendido — buscar por rótulo, não por posição.

⛔ **A cascata de encargos está completa**, e a do ICA não estava. A aba Comissões da
Base de Custos fecha a BASE em **84,88%** sem RT e sem vendedor; a planilha do ICA
mostra **92,50%**, porque nota fiscal, margem de erro, serra e manutenção ficaram em
branco. São 7,6 pontos de encargo que não entraram naquela conta.

## Os arquivos daqui

| arquivo | o que faz |
|---|---|
| `base_importada.py` | a tabela de 70 chaves e as fórmulas de busca por nome |
| `formatar.py` | ⭐ a paleta e os helpers da identidade visual, copiados do `aba.py` |
| `painel.py` | ⭐ o CONTEÚDO do Painel, os oito blocos, linha por linha |
| `regras.py` | as dezessete regras da casa, que fecham o Painel |
| `preco.py` | a nota de piso do ⑤ e o bloco ⑥ da aba Preço e Comissões |
| `fmt_painel.py` | ⭐ o FORMATO do Painel · 129 requests · é ele que manda, não o `gerar_formato.py` |
| `gerar_formato.py` | emite o formato das outras três abas fixas |

⛔ **A aba não se formata, ela se GERA.** A regra é a mesma que o `aba.py` aprendeu
em 28/10, quando o Living e a Cozinha saíram diferentes em quinze pontos: duas mãos,
dois resultados.

⚠ **`fontSize` da API é INTEIRO.** Um 9,5 derruba o lote inteiro com "Internal
error", e o erro não diz qual request falhou.

## ⛔⛔ LAYOUT NÃO É COR — a lição de 30/10/2026

Jonathan pediu *"quero a planilha com a mesma formatação e layout que fizemos com a
do michell"*. Eu copiei a **paleta** do `aba.py` — o preto do título, o cinza do
subtítulo, a régua, o teto dourado — e **inventei o layout**. A resposta veio em uma
linha:

> *"esta muuuuuito diferente"*

Estava. O Painel do Michell tem **OITO blocos** e o meu tinha **três**. Faltavam a
tabela por ambiente de dez colunas, o resumo de preço, **o quadro de lucro contra o
custo fixo dos dias**, o que não é marcenaria, o que ainda não tem preço e as
dezessete regras da casa. A aba Preço tem **SEIS** blocos e a minha tinha cinco:
faltava o ⑥, que declara o que a aba **não** faz.

⭐ **O conserto não foi estético, foi de método:** exportei o Painel do ICA em CSV
(`download_file_content` devolve `text/csv` da primeira aba), leio as linhas e
reproduzo o mapa. O layout agora é **lido de uma referência**, não lembrado.

⭐ **O mapa de linhas do Painel**, para quem for mexer:

| linha | bloco |
|---|---|
| 1–2 | título e subtítulo do projeto |
| 4–9 | ① O CONJUNTO · cinco indicadores + a nota do primeiro clique |
| 11–19 | ② ONDE ESTÁ O DINHEIRO · cinco linhas de custo e as barras █ |
| 23–44 | ③ a tabela por ambiente, dez colunas, vinte linhas reservadas |
| 48–59 | ④ O PREÇO DO PROJETO · o resumo do que a aba ao lado calcula |
| 61–70 | ⑤ O LUCRO DO PROJETO · ⚠ custo fixo da empresa · **esconder do cliente** |
| 74–79 | ⑥ O QUE NÃO É MARCENARIA |
| 81–82 | ⑦ O QUE AINDA NÃO TEM PREÇO |
| 85–103 | ⑧ AS REGRAS DA CASA, as dezessete |

⚠ **O bloco 61–70 traz o custo fixo mensal da empresa.** Antes de abrir a planilha a
um cliente ou a um parceiro, **esconder essas linhas**.

---

## ⛔⛔ DOIS DEFEITOS NO MODELO, achados em projeto real

Os dois são da pior espécie: **não quebram nada, não acusam erro, e continuam
somando.** Toda cópia nova do MODELO nasce com eles, então **corrigir na cópia é
obrigatório** — e corrigir no MODELO, melhor ainda.

### 1 · `Preço e Comissões!E41` · a tabela de dificuldade não alcança "Complexo"

A fórmula da MC APLICADA busca os pontos da dificuldade num intervalo curto:

```
=IF($C41=0;0;$D$7+IFERROR(VLOOKUP($D41;$B$66:$D$68;3;FALSE);0))
                                       ↑↑↑↑↑↑↑↑↑↑↑↑
```

A tabela do quadro ⑤ tem **cabeçalho na 66** e os três níveis nas linhas
**67 (Médio), 68 (Difícil) e 69 (Complexo)**. O intervalo `$B$66:$D$68` cobre o
cabeçalho e dois níveis — **"Complexo" fica de fora**. O VLOOKUP falha, o
`IFERROR` devolve 0 e a MC sai igual à alvo, sem os 20 pontos.

⛔ No Centurion isso significava **MC de 35% em vez de 55%** e um preço
R$ 157 mil mais baixo, sem um único aviso na tela.

**Correto:** `$B$67:$D$69` — e aplicar nas vinte linhas de ambiente, `E41:E60`,
não só na primeira.

### 2 · `Preço e Comissões` · a coluna EM R$ da cascata aponta para `$D$33`

Deveria apontar para `$E$33`, onde está o preço de venda. Com `$D$33` a cascata
multiplica pela célula errada e a conferência acusa valores que não existem.
Corrigido nas cópias do Painel da Sala e do Centurion; **o MODELO segue com o
defeito.**

### 3 · a nota fiscal do MODELO ainda está em 5%

O Jonathan fixou **9%** em 19/11/2026 (`D14`). Nota fiscal é alíquota da
empresa, não varia por projeto — então o lugar dela é o MODELO, não a cópia.

---

## ⚠ Ao renomear uma coluna do quadro ③, renomear também o rótulo do bloco ②

O bloco ② ONDE ESTÁ O DINHEIRO **espelha as colunas F..K** do quadro por
ambiente, na ordem, por `=SUM($F$24:$F$43)` e irmãs. Os rótulos são texto solto:
renomear a coluna e esquecer o rótulo faz **cada linha do bloco exibir o número
da coluna seguinte**, somando certo e dizendo errado.

⛔ Já aconteceu duas vezes — no Painel da Sala e no Centurion. No Centurion,
"Frete do projeto · R$ 200 a viagem" exibia R$ 9.953,57 de laca e concluía
"49,76785 viagens", porque `I17` guarda a fórmula de frete do MODELO
(`$G17/VLOOKUP("Frete";precos;2;FALSE)`) em vez da barra `REPT("█";…)` das
vizinhas. **Rótulo e fórmula se escrevem na mesma passada.**

---

## ⛔⛔⛔ CÉLULA MESCLADA ENGOLE A LINHA, E A API RESPONDE `success`

**Esta seção corrige um diagnóstico errado que esteve aqui.** Ela dizia que
"gravação em bloco perde linha" e mandava quebrar as escritas em pedaços cada
vez menores. Isso nunca resolveria, porque a causa era outra.

O sintoma, visto três vezes: depois de gravar, uma linha aparece **só com o
primeiro campo**, ou inteiramente vazia. A resposta diz `status: success` e
conta as células como gravadas. O Python tem o dado certo.

A causa, descoberta em 23/11/2026 ao listar os merges da aba: **a aba tinha
células mescladas de B a K, sobradas de um layout anterior**, em linhas que no
layout novo são de dado. Uma célula mesclada aceita valor só na âncora (a
primeira coluna) e **descarta o resto da linha em silêncio**.

⭐ **A cura** é desmesclar a aba inteira e mesclar de volta só o que é texto
corrido — título, subtítulo e seção:

```
unmergeCells  A1:K<fim>
mergeCells    B..K  em cada linha de título, subtítulo e seção
```

⛔ **E a regra que evita o problema:** regravar uma aba num layout novo
**começa por desmesclar**. Merge é formato, e formato sobrevive ao `clear`
de valores — por isso ele volta a morder depois de a aba parecer limpa.

⚠ Conferir o motor contra si mesmo não pega nada disso: o que falha é a
gravação. A conferência tem de rodar **na planilha**.

⭐ **As conferências que pegam isso rodam NA PLANILHA, por fórmula:**

```
=SUMPRODUCT((D63:D88<>"")*(I63:I88=""))     linha com medida e sem custo → 0
=SUMPRODUCT((C94:C109<>"")*1)               quantas notas chegaram
=SUM(F7:F28)-F29                            a coluna soma o total → 0
=F29-Painel!K24                              a aba bate com o Painel → 0
```

⭐⭐ **E a mais forte de todas é a DUPLA CONFERÊNCIA**, que fica na aba para
sempre e não precisa ser apagada: somar os itens (cada peça pagando a FRAÇÃO
de chapa que ocupa), somar o arredondamento para chapa cheia, e comparar com
o painel do ambiente. As duas contas saem dos mesmos lançamentos por caminhos
diferentes, então **a diferença tem de ser zero**:

```
Soma dos itens · chapa rateada em fração      =SUM(I<itens>)
Arredondamento para número cheio              =SUM(F<chapas>)-SUMPRODUCT(SUMIF(K;B<chapas>;I))
MATERIAL E FERRAGEM, PELO RATEIO DOS ITENS    =soma + arredondamento
Material e ferragem, pelo painel do ambiente  =SUM(F<chapas até insumos>)
⭐ CONFERÊNCIA                                 =a diferença, e ela é ZERO
```

Ela pegou, em 23/11/2026: uma fita de R$ 393,13 que ficou fora do total de um
item, e R$ 418,20 de fita que existiam no motor e não na planilha. Nenhuma
das duas quebrava nada.

As conferências descartáveis escreva numa coluna livre (a **A** serve: é
estreita e não tem merge), leia, e **apague**. ⛔ Antes de usar uma região "vazia" para isso, confira o
que mora lá: na aba `Preço e Comissões` a tabela de dificuldade vive em
`B66:D68`, escondida bem abaixo do conteúdo visível.

## ⭐ A COLUNA DE DINHEIRO TEM DE SOMAR O TOTAL; A DE PERCENTUAL, NÃO

Exibir cada linha arredondada a dois centavos e o total pelo valor exato faz
a coluna somar um centavo a menos. Quem confere soma a coluna, então **a
última linha absorve a diferença** — a embalagem no bloco de material, o
último móvel no bloco de itens.

⛔ Mas a regra **não** se aplica ao percentual: cada célula ali é a razão da
sua própria linha, e forçar a última a fechar faria ela mentir sobre si
mesma. Lá a solução é **mais precisão** — guardar seis casas em vez de
quatro, e deixar o formato exibir uma.

## ⛔⛔⛔ O PADRÃO: CADA ITEM É UM BLOCO AUTOSSUFICIENTE

Vem de uma correção do Jonathan em 23/11/2026: *"vc nao esta seguindo o padrao
que estabelecemos na planilha. os itens nao estao separados. quero poder
alterar o quantitativo de material de cada item sem comprometer o
funcionamento da planilha."*

⛔ **O que estava errado:** um painel agregado em cima e todas as peças soltas
embaixo, agrupadas por um marcador, com a fita, a laca, o LED e a ferragem num
painel único e o custo de cada item saído de um **rateio**. Assim o item é só
uma etiqueta: mexer no quantitativo de um móvel contamina os outros.

⭐ **O padrão certo** — na seção `AS PEÇAS, ITEM POR ITEM`, cada item traz o
seu próprio cabeçalho, as suas peças, os **seus** insumos e o seu total:

```
ITEM 01 · nome do móvel                                    medida geral
a observação do item
MATERIAL | ESPECIFICAÇÃO | C | L | QTD | UN | R$ UN | CUSTO || chave na Base
   as peças de chapa dele .........................................
   a fita dele, a laca dele, o LED dele, a ferragem dele ..........
TOTAL DO ITEM 01                               =SUM(OFFSET(...)) ⭐ ver abaixo
```

E então:

- o **painel do ambiente** é DERIVADO: cada linha soma as peças **pela chave**
  (coluna K), com `SUMPRODUCT` para área de chapa e `SUMIF` para insumo.
  Ninguém digita o painel;
- o **custo do item**, no bloco `OS ITENS`, **puxa o TOTAL DO ITEM**. Não há
  rateio: o item custa o que as peças dele custam;
- só `OS PARÂMETROS` se digita, e toda fórmula procura preço e rendimento
  **pela chave**, nunca por posição.

⭐ **O TOTAL DO ITEM usa `OFFSET`, não `SUM` de range fixo.** `SUM($I$97:$I$103)`
parece certo e falha no caso que mais importa: inserir linha **dentro** do
range faz o Sheets estender a fórmula, mas inserir **no fim do bloco** — logo
acima do total, que é onde a pessoa naturalmente acrescenta — deixa a linha
nova fora da soma, sem erro nenhum. Com

```
=ROUND(SUM(OFFSET($I$<primeira peça>;0;0;MAX(1;ROW()-<primeira peça>);1));2)
```

o total soma até a linha imediatamente acima de si mesmo, calculada por
`ROW()` na hora, e nenhuma inserção escapa.

## ⛔⛔⛔ O APROVEITAMENTO DE 80% É UMA MÉDIA — E MÉDIA SÓ VALE PARA PEÇA QUE REPETE

Os 80% da casa descrevem o desperdício **médio** de um plano de corte com
peças que se repetem e encaixam. Para uma peça **grande que não repete na
chapa**, a média mente nas duas direções, e as duas custam dinheiro:

- **para cima:** lançar o forro como peças do tamanho da chapa aplica o
  aproveitamento DUAS VEZES (o motor já divide por rendimento) e compra
  chapas do nada. ⭐ **Quem lança área lança ÁREA**; o rendimento é do motor;
- **para baixo:** o fundo de nicho de 104,1 × 193 numa chapa de 275 × 185
  cabe **uma vez só** — os 193 cm entram apenas no lado de 275, e a sobra de
  82 cm não comporta o segundo. O aproveitamento real é de 39,5%, e com 80%
  a planilha compra menos chapa do que o marceneiro precisa.

⭐ **A cura é dizer a verdade do rendimento na tabela de parâmetros**, por
chave `(padrão, espessura)` — não somar chapas na mão. Melhor ainda: deixar o
aproveitamento ser **fórmula** derivada da própria peça, para que mudar a cota
refaça o número de chapas sozinho.

⭐ **E a coluna `APROV.` é a que denuncia** peça que não encaixa: 39,5% grita,
80% engana. Ela tem de estar visível na tabela.

⛔ **E a tolerância no arredondamento não é enfeite:** guardar o aproveitamento
com 4 casas fez uma divisão dar `6,000090`, o `ROUNDUP` cobrou 7 chapas e R$ 350
apareceram do nada. A planilha tem de fazer `ROUNDUP(ROUND(x;6);0)` — a mesma
tolerância que o motor em Python já usava com `math.ceil(round(x, 6))`.

## ⛔⛔ DUAS ARMADILHAS DE LOCALE pt-BR, E ELAS SÃO OPOSTAS

Nenhuma das duas aparece no Python: só na célula, depois de gravar.

1. **Na fórmula, o decimal é VÍRGULA.** `IFERROR(...;0.8)` faz a célula inteira
   virar `#ERROR!`, porque `0.8` não é número em pt-BR. É a mesma regra do
   separador de argumento (`;` e não `,`), aplicada ao decimal.
2. **No padrão do `TEXT()`, o decimal é PONTO.** O padrão usa símbolos
   neutros, então `TEXT(22,4;"0,00")` lê a vírgula como separador de **milhar**
   e exibe `022`. O certo é `"0.00"`, que em pt-BR **exibe** `22,40`.

⭐ Número literal dentro de fórmula passa por uma função que troca `.` por `,`;
padrão de formato é sempre o neutro. Nunca escrever decimal solto.

## ⭐ NÚMERO CALCULADO DENTRO DE TEXTO FIXO É MENTIRA ESPERANDO A PRÓXIMA MUDANÇA

Escrever "área líquida de 22,30 m²" ou "4 folhas" numa observação funciona no
dia em que se escreve e mente na mudança seguinte — e ninguém percebe, porque
texto não quebra.

⭐ **Número vive em CÉLULA, com formato; texto explica o porquê.** Quando o
número precisa mesmo aparecer no meio da frase, a frase inteira vira
**fórmula**:

```
="Melamínico Fosco · "&TEXT(<a soma das peças>;"0.00")&" m² de peças"
```

Assim o número está dentro do texto e **nunca mente**.

⚠ A exceção é o **registro histórico**: "o Jonathan fixou R$ 650 em 23/11/2026"
ou "eram 18 mm, a R$ 700" são fatos datados, e fato datado não muda. O que não
pode ficar cravado é o **estado atual**.
