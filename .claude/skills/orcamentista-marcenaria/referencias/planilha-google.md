# Planilhas da casa — a base e o orçamento

## ⭐⭐ DUAS PLANILHAS, NÃO UMA [Jonathan, 26/10/2026]

> *"quero que você crie uma planilha individual, que vai ser a base de
> informações... E já na planilha do orçamento do cliente, você vai puxar
> todas as informações dessa base e vai relacionar só as abas."*

| planilha | o que é | quantas |
|---|---|---|
| **Valvic · Base de Custos** | a fonte única de preço da casa | **uma só**, para sempre |
| **orçamento do cliente** | o levantamento de um projeto | uma por cliente |

⛔ **Preço não se digita dentro do orçamento do cliente.** Se falta um item,
ele entra na Base. Assim o preço muda num lugar só e todos os orçamentos
novos acompanham — e some o risco de dois orçamentos usarem preços
diferentes para a mesma dobradiça.

### A Base — seis abas

`https://docs.google.com/spreadsheets/d/13cZGej-AUTTyWZblqtraTBnc1HUECjT6fy3zy6R5mv4/edit`

| aba | o que guarda |
|---|---|
| **Instruções** | como usar, como ligar um orçamento, as regras de ferro |
| **MDF** | preço da chapa por padrão × espessura, medida, aproveitamento, fita, consumíveis |
| **Ferragens** | Blum, alma de aço, LED — e os itens **a cotar**, com a linha reservada |
| **Terceirizados** | provençal, usinagens, laminação, pedra, serralheria |
| **Vidro** | reflecta champagne, espelho, temperado |
| **Comissões** | a cascata inteira e a BASE calculada em cada condição |

⭐ Os itens **sem preço** ficam na Base com a linha criada e o valor vazio.
Assim o orçamento que os usa mostra zero e grita — em vez de esconder o
buraco.

### O orçamento do cliente

| aba | o que faz |
|---|---|
| **Painel** | o resumo geral: custo por ambiente, preço de venda, taxas de transação, comissões, MC |
| **Base (importada)** | `IMPORTRANGE` da Base, uma vez só; as outras abas fazem PROCV aqui |
| **uma por ambiente** | os **itens** do ambiente, e dentro de cada item os seus materiais |

⭐⭐ **O ambiente se organiza por ITEM, não por tipo de material.**
Cada móvel é um bloco fechado com o seu custo; o ambiente soma os blocos.
É como o Jonathan vende e como a fábrica produz — e conferir "a sapateira
custa X" é possível, conferir "o ambiente tem 104 m² de chapa" não é.

No fim da aba vai o **resumo de material do ambiente**: a soma de tudo que
os itens consumiram, consolidada.

⛔ `IMPORTRANGE` pede autorização na primeira vez: abrir a planilha do
cliente, clicar na célula e em **Permitir acesso**. Sem isso a aba
importada fica em `#REF!` e o orçamento inteiro zera.

### ⭐ O LAYOUT ESCOLHIDO — "Prancha" [Jonathan, 26/10/2026]

Três opções foram desenhadas e o Jonathan escolheu a **B · Prancha**:
branco puro, tipografia leve e grande, réguas finas, dourado em **um**
acento só. Parece uma prancha de arquitetura — e é o que a planilha deve
parecer quando a arquiteta do projeto abrir para conferir.

**O que faz o desenho**, e nenhuma dessas coisas é enfeite:

| recurso | para quê |
|---|---|
| **gridlines desligadas** | o desenho sai das réguas e do respiro, não da grade |
| **colunas de 36 px nas pontas** (A e J) | margem — o conteúdo não encosta na borda |
| **altura de linha variada** | 58 px no nome do ambiente, 46 no número do KPI, 30 na tabela, 10 nos respiros |
| **células mescladas** | o nome do ambiente atravessa C:G, a área da imagem ocupa B16:I30 |
| **borda inferior de 2 px preta** | a régua que separa cabeçalho de conteúdo |
| **borda de 3 px dourada** | só no custo direto do ambiente, e em mais nada |
| **`REPT("█"; …)`** | a barra de proporção do KPI, feita de caractere: sem gráfico, sem imagem |

⭐ **A área da imagem** é B16:I30 mesclada, fundo #FAFAFA, borda cinza.
A imagem vai **sobre** as células (Inserir › Imagem › Sobre as células) e
fica onde for solta.

⭐⭐ **O ambiente se organiza por ITEM.** Cada móvel é um bloco fechado:
faixa preta com o número e o nome, uma linha de conferência da cadeia de
cota, a tabela de materiais e o total do item. O ambiente soma os blocos.

⛔ **Formato condicional NÃO aceita tamanho de fonte** — só negrito,
itálico, tachado e as duas cores. A faixa de bloco e o fundo saem por
regra (`=ESQUERDA($B56;5)="ITEM "`), mas o corpo 12 de cada título tem
que ir por `repeatCell`, linha por linha.

⭐ **`repeatCell` replica fórmula ajustando as referências relativas.**
Noventa e uma fórmulas de custo entraram em **um** request, em vez de
noventa e uma linhas de JSON — depois só as oito linhas de `SOMA` foram
reescritas por cima.

⛔ **`update_values` reclama quando o array tem mais linhas que o range.**
Dimensionar o range pelo tamanho do array, sempre com folga: errei isso
quatro vezes seguidas e cada erro custou uma chamada.

### A chave de preço

A aba de ambiente **não digita preço**. Cada linha de material carrega uma
**chave** numa coluna oculta (K), e o `R$ un` é
`=SEERRO(PROCV($K61;precos;2;FALSO);"")`. `precos` é o intervalo nomeado
na aba `Base (importada)`, que por sua vez espelha a planilha-base com
`IMPORTRANGE`.

⭐ São **três camadas**: a Base guarda o preço, a aba importada traduz para
as chaves que o orçamento usa, e o ambiente consome a chave. Mudar o preço
de uma dobradiça atravessa as três sem ninguém digitar nada.

⛔⛔ **`IMPORTRANGE` fica em `#REF!` até alguém autorizar**, clicando na
célula e em **Permitir acesso**. Enquanto isso toda a cadeia dá
`#DIV/0!` — por isso as fórmulas de custo vão dentro de `SEERRO`, para que
a planilha fique limpa, e não quebrada, no estado intermediário.

## ⛔⛔ ENTREGUEI SEM REVISAR, E O JONATHAN ACHOU OITO [28/10/2026]

> *"sempre revise antes de entregar os resultados."*

Oito correções numa rodada só. Quase todas eram coisas que uma conferência
**mecânica** teria pegado antes de a aba existir: frente sem dobradiça,
gaveta sem corrediça, peça de largura que não existe, duas linhas em que
uma somava e a outra subtraía a mesma área.

⭐ A revisão não pode depender de eu lembrar — tem de **quebrar**.
`projetos/ica-michell/auditor.py` confere o levantamento antes de ele virar
planilha, e depois confere a planilha contra o levantamento:

| regra | o que pega |
|---|---|
| peça cabe na chapa | emenda que ninguém decidiu |
| quantidade negativa | linha que subtrai área fingindo ser peça |
| gaveta ↔ corrediça | caixa sem par, par sem caixa |
| frente com cava ↔ metro de cava | usinagem prometida e não orçada |
| porta ↔ dobradiça | **o furo do item 1** |
| dobradiça de vidro ↔ folha de vidro | ferragem sem o que ela segura |
| alma onde a regra manda | estrutura que some numa reescrita |
| peça sem fita sem justificativa | esquecimento disfarçado de decisão |
| chave fora da Base | preço que nunca vai resolver |
| totais da aba × totais do script | a aba divergindo em silêncio |

⛔ **E o auditor foi testado pela violação, 8/8** — porque auditor que nunca
falhou não está provado. ⚠ Uma das dez regras nasceu **vazia**: conferia um
atributo que não existia e passava sempre. Foi o teste negativo que viu.

## ⛔⛔ TRÊS ARMADILHAS DE ESCRITA QUE ENGOLEM EM SILÊNCIO

1. **Merge órfão engole a escrita.** A linha do MDF 6 mm saía vazia, e a API
   devolvia `updatedCells: 6` toda vez. ⭐ Sobrara um `merge` B:I daquela
   linha de quando o resumo morava ali. **Mesclagem sobrevive a
   `batchClear`** — limpar valor não desfaz merge. Antes de reescrever uma
   faixa, conferir `merges` na estrutura da planilha.
2. **Nunca escrever valores e fórmulas em faixas sobrepostas na mesma leva
   paralela.** As duas chamadas não têm ordem garantida: a de valores
   chegou depois e apagou as fórmulas. Em faixa sobreposta, uma de cada vez.
3. **Padrão numérico é em convenção americana, mas o ponto não é decimal em
   pt_BR.** `0.##` renderizou `65` como **"65,"** — o ponto virou separador
   de milhar. ⭐ Para número livre, **não definir padrão nenhum** e deixar o
   formato Geral.

## ⭐⭐ LER A PRANCHA POR VISTA, NÃO POR CADEIA

> *"analise todas as visoes, como vista superior e vista frontal"*

O `geo.py` agrupa cotas em cadeias e acha a que fecha — mas joga **todas as
vistas no mesmo saco**. Quando a folha traz três vistas do mesmo móvel, a
cota da superior entra na cadeia da frontal e o móvel sai errado.

⛔ Foi assim que inventei **quatro módulos de 65 de largura** na cristaleira.
O 65 é a **profundidade** — a vista superior fecha `16 + 2 + 15 + 16 + 16 =
65` — e reaparece como **vão** na cadeia vertical. Não existe peça de 65 de
largura no móvel, e eu tinha criado três montantes que não existem.

⭐ `projetos/ica-michell/vistas.py` faz cada rótulo de VISTA virar um centro
e manda cada cota para a vista mais próxima. Daí dá para ler *"o que a
superior diz"* separado de *"o que a frontal diz"* — que é como um
marceneiro lê a prancha.

## ⛔⛔ A CHAVE DE PREÇO DESLIZOU DE LINHA — e ninguém via [27/10/2026]

O Jonathan apontou que *"não puxou o custo da corrediça"*. A linha **estava**
na planilha; o que não estava era o preço. A chave `Corrediça` devolvia
**vazio**, e a investigação mostrou que não era uma chave só:

| chave | puxava | devia puxar |
|---|--:|--:|
| Corrediça | *(vazio)* | **R$ 300** |
| Dobradiça | R$ 70 | **R$ 50** |
| Báscula HK-XS | R$ 100 | **R$ 250** |
| Puxador slim | R$ 6 | **R$ 35** |

⭐⭐ **Cada uma pegou a linha SEGUINTE à certa na Base.** O vazio gritou; os
outros três mentiram caladinhos, com um número plausível na célula. ⛔ **Um
preço errado é pior que um preço faltando** — o faltando a gente vê.

⭐ **O conserto é buscar por NOME, não por posição:**
```
=SEERRO(PROCV("Corrediça Blum";IMPORTRANGE(id;"Ferragens!A:D");4;FALSO);"")
```
Assim inserir uma linha na Base não desloca mais nada. ⚠ Só serve onde o
nome é único: as chapas de MDF repetem o nome em 6/15/18 mm e continuam
por posição.

## ⭐⭐ A REGRA DE FERRO PRECISA DE UMA LINHA PRÓPRIA NO FECHAMENTO

O bloco por item **rateia a chapa em fração** — tem de ratear, senão cada
móvel puxaria uma chapa inteira. Mas a compra é em número cheio. Os dois
não podem viver na mesma linha.

⭐ A saída: o **RESUMO DE MATERIAL DO AMBIENTE** no fim da aba soma a área
por cor × espessura, arredonda para cima, e mostra as duas colunas lado a
lado — `CUSTO CHEIO` e `NOS ITENS`. A diferença vira uma linha explícita no
fechamento: *"Arredondamento de chapa para número cheio"*. No Living deu
**R$ 333,49**, e agora dá para ver de onde vem.

## ⛔⛔ O PAINEL MISTURAVA NÚMERO VIVO COM NÚMERO MORTO

Pior que `#REF!`. Três ambientes estavam no formato antigo e devolviam
`#REF!` em quase tudo — **menos** nas colunas de Ferragem e Terceirizados,
onde sobraram valores fixos digitados numa rodada anterior. O `TOTAL`
somava o Living vivo com três mortos e dava **R$ 25.108** de ferragem, que
não é número de lugar nenhum.

⭐ `#REF!` é honesto: grita. Número velho fixo é o contrário — parece certo.
Hoje o TOTAL usa `SOMARPRODUTO(SEERRO(faixa;0))` e soma só o que existe,
com a nota dizendo em voz alta o que ainda não entrou.

## ⚠ TRÊS DETALHES DA API QUE CUSTARAM CHAMADA

1. **Número vai como número.** Mandar `"131.4"` como texto numa planilha
   pt_BR vira texto ou 1314. O JSON leva `131.4` sem aspas e o Sheets
   grava número, seja qual for o locale.
2. **`fields` com vírgula é recusado.** `userEnteredFormat(wrapStrategy,textFormat)`
   voltou `Invalid field`. Usar `userEnteredFormat` inteiro, ou um campo só.
3. **Padrão de `TEXT` é sempre em convenção americana.** `TEXT(x;"R$ #.##0")`
   em pt_BR sai `R$ 19600,0`. O certo é `"R$ #,##0"` — a vírgula é milhar no
   padrão, e o Sheets traduz para o ponto na tela.

## ⭐ A PLANILHA NÃO SE DIGITA — ELA SAI DO SCRIPT

`projetos/ica-michell/planilha-living.py` lê `living.py` e monta as linhas
da aba. Quando os dois divergem, é bug — e divergiram: faltava a **fonte de
LED**, que serve o ambiente e não um item só, e a aba saiu R$ 240 mais
barata que a conta. ⭐ Os dois números batendo é a única prova de que a aba
está certa.

## ⛔⛔ A ARMADILHA QUE QUEIMOU UMA RODADA INTEIRA — locale pt_BR

As planilhas da casa nascem em **pt_BR**. Nesse locale o separador de
argumento de função é **`;`**, não `,`. A API grava a fórmula do jeito que
chega, e **toda** fórmula escrita com vírgula vira `#ERROR!` na célula:

```
=IF(C17="","",C17*D17)     →  #ERROR!      ⛔ vírgula
=IF(C17="";"";C17*D17)     →  calcula ✓    ✅ ponto e vírgula
```

⚠ Pega `IF`, `IFERROR`, `ROUND`, `ROUNDUP`, `CEILING`, `SUMIF` — tudo que
tem mais de um argumento. **`SUM(A1:A9)` não pega**, porque é argumento
único: por isso a planilha parece meio funcionando e engana.

⭐ **Nome de função pode ser em inglês** (`IF`, `SUM`, `CEILING`): o Sheets
traduz sozinho na tela. O que não se traduz é o separador.

⭐ **Decimal dentro de fórmula também muda** (`0,80` e não `0.80`). A saída
limpa é **não escrever decimal dentro de fórmula nenhuma**: todo percentual
e todo preço mora numa célula da aba `Base de Preços`, e a fórmula aponta
para a célula. Quem quiser mudar o aproveitamento muda num lugar só.

⭐ Conferir **sempre** com `get_values` depois de gravar. `update_formulas`
devolve `status: success` mesmo quando as 284 células viraram `#ERROR!` —
ele confirma que escreveu, não que calculou.

## A forma da planilha

| aba | para quê |
|---|---|
| **Resumo Geral** | uma linha por ambiente; as colunas puxam das abas. Nada é digitado aqui. |
| **Custos** | o preço entra, a cascata inteira se abre em financeiro e operacional, e a MC sai. |
| **Base de Preços** | **toda** entrada da casa: chapa, fita, ferragem, percentuais da cascata. Azul = mexer aqui. |
| **NN Ambiente** | uma por ambiente, todas com o mesmo esqueleto. |

O esqueleto do ambiente, na ordem: móveis do ambiente · chapa · fita ·
ferragem · alma de aço · iluminação e terceirizados · o que **não** é
marcenaria · custo direto. O último bloco é o que a `Resumo Geral` lê.

⭐ **Azul é entrada, verde é fórmula.** O Jonathan abre a planilha e sabe
onde pode digitar sem quebrar nada.

⭐ **Pôr uma linha de conferência.** No fim do `Resumo Geral`:

```
=IF(ROUND(B38;2)=ROUND($K$27;2);"confere com a soma dos ambientes";"DIVERGE")
```

Ela compara o custo direto montado por material com o custo direto somado
por ambiente. São dois caminhos independentes para o mesmo número — se
divergirem, tem erro de fórmula em algum lugar.

## ⛔ Upload de `.xlsx` pelo Drive não funciona

`create_file` com `base64Content` recusa um `.xlsx` ("The file content is
not a valid base64 string") mesmo com base64 válido — testado a 20.892 e a
23.616 caracteres. **Usar o conector do Google Sheets**, que cria e escreve
direto.

## ⭐ O MAPA DE LINHAS DA ABA DE AMBIENTE

Todas as abas de ambiente repetem este esqueleto. Decorar o mapa é o que
permite montar as vinte abas sem reabrir cada uma — e é o que o
`Resumo Geral` referencia célula por célula.

| linha | o que vai |
|--:|---|
| 1–2 | nome do ambiente · páginas, nº de detalhamentos, padrões de MDF |
| 4–5 | `MÓVEIS DO AMBIENTE` + cabeçalho |
| 6–17 | um móvel por linha · coluna H traz **a cadeia de cota que fecha** |
| 19–20 | `CHAPA` + cabeçalho |
| 21–70 | uma peça por linha: comprimento · largura · qtd · espessura |
| **71** | **área total (m²)** |
| **72** | **chapas, com aproveitamento** |
| **73** | **custo de chapa** |
| 75–76 | `FITA DE BORDA` + cabeçalho · 77–85 as linhas |
| **86** | **custo de fita** |
| 88–89 | `FERRAGEM BLUM` + cabeçalho · 90–104 as linhas |
| **105** | **custo de ferragem** |
| 107–108 | `ALMA DE AÇO` + cabeçalho · 109–115 as linhas |
| **116** | **custo de alma de aço** |
| 118–119 | `ILUMINAÇÃO E TERCEIRIZADOS` + cabeçalho · 120–129 as linhas |
| **130** | **custo de iluminação e terceirizados** |
| 132–133 | `NÃO É MARCENARIA` + cabeçalho · 134–144 os itens |
| 145–153 | `CUSTO DIRETO DO AMBIENTE`, linha a linha |
| **154** | **CUSTO DIRETO** — é o que o `Resumo Geral` lê |

⭐ **A aba `01 Living` é a exceção**: nasceu antes do padrão, num layout
compacto (área em G31, chapas G32, chapa G33, fita G43, ferragem G57, alma
G66, terceiros G76, custo direto **G96**). Como o `Resumo Geral` aponta
célula por célula, conviver com as duas não quebra nada.

⛔ **Linha vazia tem que ir como `[""]`, nunca como `[]`.** O `update_values`
colapsa a linha vazia do fim do bloco e **desloca tudo que vem depois** —
um erro que não aparece no `status: success` e só se vê relendo.

⭐ **Custo de chapa respeita a espessura.** Não é área ÷ aproveitamento ×
preço único: cada espessura tem o seu preço, e a fórmula separa com `SUMIF`
sobre a coluna de espessura:

```
=(SUMIF($F$21:$F$70;18;$G$21:$G$70)*'Base de Preços'!$B$6
 +SUMIF($F$21:$F$70;15;$G$21:$G$70)*'Base de Preços'!$B$7
 +SUMIF($F$21:$F$70; 6;$G$21:$G$70)*'Base de Preços'!$B$8)
 /('Base de Preços'!$B$57*'Base de Preços'!$B$27)
```

⭐ **Conferir a aba contra um script.** O `quantitativo.py` declara as
mesmas peças em Python e soma a área por espessura. Se a planilha e o
script derem o mesmo número, a leitura da prancha foi transcrita certo —
a Cozinha fechou em 80,27 m² nos dois caminhos.

## ⭐ O VISUAL — padrão Valvic aplicado à planilha

A paleta é a da marca (`closer-vendas/referencias/identidade-marca.md`), a
mesma das propostas. Uma planilha que o cliente abre é peça da marca, não
rascunho interno.

| uso | cor |
|---|---|
| faixa de bloco: fundo | **#1A1A1A** quase-preto |
| faixa de bloco: texto | **#E0A521** dourado da marca |
| cabeçalho de coluna: fundo | **#FDF6E3** creme |
| cabeçalho de coluna: texto | #1A1A1A, negrito |
| linha de total: fundo | **#F6E8C8** creme dourado |
| título da aba | #1A1A1A, 14 pt, negrito |
| número de entrada | **#0000CC** azul |
| número de fórmula | **#00732E** verde |
| borda de bloco | #D4C9A8 dourado claro, fina |

⭐ **Gridlines desligadas.** O desenho sai das faixas e das bordas, não da
grade. É o que dá o respiro das propostas.

⭐ **Azul é entrada, verde é fórmula** — a convenção fica escrita na linha 3
de cada aba, para quem abre pela primeira vez.

⭐ **A faixa de bloco é mesclada** (`mergeCells`) de A até a última coluna.
Assim o título do bloco atravessa a largura e separa de verdade.

## ⛔⛔ CHAPA EM NÚMERO CHEIO — como a planilha faz

> **Regra de ferro da casa** (`quantitativo.md`): não existe 2,7 chapas.

Cada aba de ambiente tem uma **coluna de padrão de MDF** (F) ao lado da
espessura (G), e um **bloco de compra** à direita (K:O) com uma linha por
**padrão × espessura**:

```
L = área   =SUMIFS($H$21:$H$70;$F$21:$F$70;$K22;$G$21:$G$70;$L22)
M = chapas =MAX(1;ROUNDUP(L22/('Base de Preços'!$B$57*'Base de Preços'!$B$27);0))
O = custo  =M22*N22
```

⭐ O `MAX(1; …)` é o "mínimo de uma chapa por cor": uma peça só de um padrão
já obriga a comprar a chapa inteira.

⭐ Os totais do ambiente (H71 área · H72 chapas · H73 custo) **somam esse
bloco**, não a fração. Antes de mudar isso, a Cozinha dava 19,72 chapas num
total só; com a regra, dá **21 chapas** em três compras separadas — e o custo
sobe, porque é o que sai do caixa de verdade.
