# ICA · Jéssica e Michell — ferramenta de leitura do executivo

⛔⛔ **O PROBLEMA QUE ISTO RESOLVE.** O executivo tem **235 páginas A3** e
**111 MB**. Nada disso funciona:

| caminho | resultado |
|---|---|
| `curl` em `drive.google.com` | **403** — bloqueado por política no proxy |
| `read_file_content` no PDF inteiro (6,5 MB) | corta em **107 mil caracteres**, na página 80 |
| `read_file_content` no PDF inteiro (111 MB) | **string vazia** — o Drive não indexa |
| `download_file_content` no PDF inteiro | **derruba o servidor MCP** |

## ⭐⭐⭐ O CAMINHO BARATO — descoberto em 26/10/2026

`read_file_content` **numa página solta** devolve o **texto inteiro da
prancha** em ~1.200 caracteres: título do ambiente, conteúdo da folha,
chamadas de detalhe ("Ver Det. 06"), especificações de material, nomes de
móvel solto e **as cotas**. Sem download, sem base64, sem disco.

⚠ **O que ele perde: a POSIÇÃO.** As cotas saem soltas no meio do texto
(`37Prateleira inferior. Ver Det. 03. 294`), sem saber a que peça cada
número pertence. Serve para **mapear** o ambiente; não serve para **contar
gaveta** nem para amarrar cota a peça.

⭐ **A regra prática:** `read_file_content` em TODAS as páginas para montar
o mapa; `download_file_content` + `extrair.py` **só** nas folhas de
detalhamento onde é preciso contar frente, gaveta e porta.

⭐⭐ **O CAMINHO CARO, que continua valendo para a geometria** [Jonathan dividiu o PDF por página em 25/10]:
`download_file_content` numa **página solta** (300–800 KB) estoura o limite
de tokens, e **o harness salva o resultado em arquivo** em vez de jogar no
contexto. Daí é só decodificar o base64 — e sai o **PDF real da página,
com a geometria vetorial inteira**. Custo de contexto: a mensagem de erro.

## Como usar

1. **IDs** — `paginas.json` mapeia `nº do arquivo → fileId` das 235 páginas.
   ⚠⚠ **O ARQUIVO N É A PÁGINA N+1 DO DOCUMENTO.** `páginas-157` traz
   "158 PÁGINA" no carimbo. Para a página P do documento, baixe o arquivo
   P−1.
   ⚠ Os títulos vêm com acento **decomposto** (NFD): `re.search` com `á`
   literal não casa. Normalizar com `unicodedata.normalize('NFC', …)`.
2. **Baixar** — `download_file_content` com o fileId, **várias por bloco**
   (testado com 10 em paralelo).
3. **Colher** — `python3 -I colher.py` decodifica tudo que está em
   `tool-results/` para `pgs/pNNN.pdf` e **apaga o .txt** (cada um pesa
   ~1 MB; 235 páginas encheriam o disco).
4. **Ler** — `python3 -I extrair.py [nº …]` resume ambiente, conteúdo,
   linhas de especificação e cotas de cada página.

⚠ Para listar a pasta, usar **`list_recent_files`** com `pageSize=100`:
o `search_files` **ignora o pageSize e devolve 5 por chamada** (46 chamadas
para 235 arquivos).

## O Painel, e por que ele quebrava

O Painel (sheetId 0) **não é gerado por módulo** — ele é escrito à mão e
busca os números nas 19 abas. Cada regeração de uma aba move as linhas dela,
e foi assim que o Painel passou semanas somando errado.

⭐⭐ **A CORREÇÃO DE FUNDO [29/10]: o Painel busca por RÓTULO, não por
posição.** Toda fórmula é `SUMIF` sobre a faixa fixa `B$7:B$26` da aba,
casando o texto da coluna MATERIAL:

| coluna | o que traz | critério |
|---|---|---|
| D | itens | `COUNT` em `B{it0}:B{it1}` — a única que ainda usa posição |
| E | chapas | `SUMIFS` por UN `"chapas"` **e** material `"MDF *"` |
| F | MDF | `"MDF *"` sobre F |
| G | fita e filetagem | `"Fita*"` + `"Filetagem*"` sobre F |
| H | ferragem | `"Ferragem*"` sobre F |
| I | vidro e frete | `"Vidro*"` sobre F + `"CUSTO DIRETO*"` sobre G |
| J | corte, consum. e embal. | `"Corte*"` + `"Consumíveis"` + `"Embalagem"` sobre F |
| K | custo direto | `"CUSTO DIRETO*"` sobre H |

A faixa `7:26` cobre o painel de material da aba mais longa (Cozinha, cujo
CUSTO DIRETO cai na linha 25). Nas abas curtas ela invade a tabela de itens,
onde a coluna B tem **números** — e critério de texto não casa número, então
não há contaminação.

⛔⛔ **CHAPAS DOBRAVA.** Somar toda linha com UN `"chapas"` conta também a
linha **"Corte · por chapa"**, cujo D é a soma de todas as chapas. O Living
marcava 56 onde são 28. Por isso a coluna E exige as DUAS condições.

⛔⛔ **O QUADRO ④ DA ABA DE PREÇO LIGA POR POSIÇÃO** a `Painel!B24:K43` —
vinte linhas, Living a Banho 03. Ele estava uma linha abaixo: pulava o
Living e contava a linha de TOTAL como ambiente, dobrando o custo direto.
⚠ Ao mexer nas linhas do Painel, **conferir `Preço e Comissões!B41:C60`**.

### O mapa de linhas do Painel

| linha | o que é |
|---|---|
| 6–7 | o conjunto: ambientes, itens, chapas, custo direto, preço |
| 9 | a nota do levantamento |
| 13–19 | ONDE ESTÁ O DINHEIRO · 1 cabeçalho + 5 linhas + total em 19 |
| 23 | cabeçalho da tabela por ambiente |
| 24–43 | os vinte ambientes, **nesta ordem**, com o Lavabo zerado em 28 |
| 44 | TOTAL DO QUE ESTÁ LEVANTADO |
| 47–61 | O PREÇO DO PROJETO · resumo da aba ao lado |
| 63–72 | ⭐ O LUCRO DO PROJETO · custo fixo da empresa × dias |
| 76–80 | o que não é marcenaria |
| 82–88 | o que ainda não tem preço |
| 90–103 | ⭐ AS REGRAS DA CASA · as doze regras, pedido do Jonathan |

### O LUCRO DO PROJETO, e o IMPORTRANGE da Gestão 3

[Jonathan, 29/10] *"insira no painel uma linha que informe o custo fixo mes
da empresa, quero que busque esse valor da planilha da gestao 3 de forma
automatica… e outro campo ao lado onde eu preencho a estimativa de gasto de
tempo para o projeto em dias e ela me mostrar o resultado em lucro"*

A cadeia, em `Painel!G66:G71`:

```
G66  margem de contribuição do projeto   = G58  (o quadro de preço acima)
G67  custo fixo da empresa, por mês      = IMPORTRANGE da N.GESTAO 3
G68  custo fixo por dia                  = G67/30   (dias de CALENDÁRIO)
G69  ⭐ DIAS DE PROJETO                   ← amarelo, o Jonathan digita
G70  custo fixo alocado                  = G68*G69
G71  ⭐ LUCRO DO PROJETO                  = G66-G70
```

A fonte é **N.GESTAO 3 · Direção · não compartilhar**,
`1-7XUrVso9oVKccQjM2m5Tgd9_-QIk-r1LZ8XZbDnGL0`, aba `O mês`, bloco CUSTO
FIXO VIGENTE em `B58:D62`. A busca é por RÓTULO — `VLOOKUP("Custo
operacional*")` — e não por célula, para sobreviver a mudança de layout lá.
⚠ É o custo OPERACIONAL (folha + estrutura, R$ 116.817,70), que é o mesmo
que o ponto de equilíbrio da Gestão 3 usa. O `Custo total · com
investimentos` (R$ 125.417,70) está na linha de baixo de lá, se um dia a
conta tiver de incluir investimento.

⛔⛔ **EM 29/10 A GESTÃO 3 FOI REORGANIZADA** e o bloco CUSTO FIXO VIGENTE
desceu de `B58` para `~B107`. O `IMPORTRANGE` fixo em `B58:D62` passou a
trazer a tabela ANO A ANO, e o VLOOKUP devolvia `#N/A`. ⭐ Corrigido para
importar **colunas inteiras**, `'O mês'!B:D`, de modo que o rótulo é achado
onde quer que o bloco esteja. Não voltar a cravar linha.

⛔⛔ **O IMPORTRANGE MOSTRA `#REF!` ATÉ ALGUÉM AUTORIZAR.** É uma vez só, na
célula, e é de propósito que **não** há `IFERROR`: com ele o custo fixo
ficaria em ZERO e o LUCRO apareceria igual à margem inteira — lucro inflado
e silencioso. `H67` detecta o erro com `ISERROR` e escreve o que fazer.

⚠⚠ **A CONTA ALOCA O CUSTO FIXO INTEIRO A UM PROJETO**, como se ele fosse o
único na fábrica nos dias digitados. É a leitura conservadora e responde
"enquanto este projeto está aqui, ele paga a casa?". Com três projetos em
paralelo o custo fixo se divide e o lucro real é MAIOR — o número é piso.

⚠ **ESTE BLOCO EXPÕE O CUSTO FIXO DA EMPRESA DENTRO DO ORÇAMENTO**, e a
planilha de origem se chama "não compartilhar". Se este arquivo for algum
dia aberto para o cliente, esconder ou apagar as linhas 63–72 antes.

⚠ `Painel!B6:K7` e `B9` são **texto escrito**, não fórmula de aba: o número
de itens e de chapas aparece em prosa e envelhece. Reescrever junto.

## A cascata de encargos, e a célula que sumiu

A aba **Preço e Comissões** calcula o preço em `③`, mas quem manda é a
cascata de `②`, em `D15:D26`. Cada linha é uma fórmula, e as quatro
amarelas de `①` (`D7` MC, `D8` parcelas, `D9` RT, `D10` vendedor) são as
únicas que se digitam.

| célula | o que é | fórmula |
|---|---|---|
| D15 | nota fiscal | `VLOOKUP("Nota fiscal";precos;2;FALSE)` |
| D16 | cartão | `VLOOKUP("Cartão por parcela";…)*$D$8` |
| D17–D19 | erro, serra, manutenção | VLOOKUP na Base |
| D20 | RT | `=(1-$D$15-$D$16)*$D$9` |
| **D21** | **comissão de vendedor** | **`=(1-$D$15-$D$16)*$D$10`** |
| D22–D26 | as cinco comissões internas | `=((1-$D$15-$D$16)-$D$20-$D$21)*n/1000` |
| D27 | SOMA | `=SUM(D15:D26)` |

⛔⛔ **EM 29/10 A `D21` APARECEU SEM FÓRMULA**, como valor vazio. O vendedor
saía 0,00% e R$ 0,00 mesmo com `D10` em 5%. O estrago não é só a linha dele:
`D22:D26` usam `-$D$21` para achar o LÍQUIDO 2, então com ela vazia o
líquido 2 inchava e as cinco comissões internas saíam grandes demais.

Com os valores daquele dia — MC 55%, RT 5%, vendedor 5% — o efeito era:

```
quebrado    encargos 19,52%   base 80,48%   preço R$ 1.274.692,83
consertado  encargos 23,91%   base 76,09%   preço R$ 1.557.466,55
                                            diferença R$ 282.773,71
```

⚠ O preço saía **R$ 282 mil mais barato**, e a comissão do vendedor sairia
da margem em vez de estar no preço.

⭐ **COMO ACHAR ISSO DE NOVO:** `FORMULATEXT` devolve `#N/A` para célula que
não é fórmula. Para auditar a cascata inteira de uma vez, escreva numa
coluna de rascunho:

```
=IFNA(FORMULATEXT('Preço e Comissões'!D15);"⛔ SEM FÓRMULA")
```

e arraste por `D15:E27`. Vale a mesma varredura sempre que um número da
aba de preço parecer baixo demais.

⚠ A CONFERÊNCIA de `③` tem DUAS colunas e elas não querem dizer a mesma
coisa: a de R$ é o fechamento do dinheiro e tem de ser `R$ 0,00` sempre; a
de % é `MC realizada − MC alvo`, e ela é diferente de zero **de propósito**
quando algum ambiente leva AJUSTE DE MC no quadro `④`. Não é erro.
