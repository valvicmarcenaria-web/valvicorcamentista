# ICA · Jéssica e Michell — ferramenta de leitura do executivo

⛔⛔ **O PROBLEMA QUE ISTO RESOLVE.** O executivo tem **235 páginas A3** e
**111 MB**. Nada disso funciona:

| caminho | resultado |
|---|---|
| `curl` em `drive.google.com` | **403** — bloqueado por política no proxy |
| `read_file_content` no PDF inteiro (6,5 MB) | corta em **107 mil caracteres**, na página 80 |
| `read_file_content` no PDF inteiro (111 MB) | **string vazia** — o Drive não indexa |
| `download_file_content` no PDF inteiro | **derruba o servidor MCP** |

⭐⭐ **O QUE FUNCIONA** [Jonathan dividiu o PDF por página em 25/10]:
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
