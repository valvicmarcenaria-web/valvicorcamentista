# Planilha no Google — como montar sem apanhar

Quando o Jonathan pede uma planilha **para o cliente conferir o levantamento**,
ela vai para o Google Sheets, na pasta `Orçamentos Valvic`, e não para um
`.xlsx` local. O cliente abre no celular; o Jonathan edita junto; e a projeção
versus realizado só existe se a planilha for **viva**, com fórmula, não com
número colado.

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
