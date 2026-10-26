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
