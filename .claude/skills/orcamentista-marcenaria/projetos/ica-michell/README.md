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
| 64–68 | o que não é marcenaria |
| 70–76 | o que ainda não tem preço |
| 78–91 | ⭐ AS REGRAS DA CASA · as doze regras, pedido do Jonathan |

⚠ `Painel!B6:K7` e `B9` são **texto escrito**, não fórmula de aba: o número
de itens e de chapas aparece em prosa e envelhece. Reescrever junto.
