# Ana Carolina e André · projeto [35] de Ana Maria

Três ambientes com marcenaria: closet da Suíte master, roupeiro do Quarto Gabriel e
closet da Isabella. **Ferragem Blum · RT 10% · sem vendedor** [Jonathan, 05/11/2026].

**Decisões [Jonathan, 06/11/2026]:**
- "não tem roupeiro na suíte master, apenas o closet": a aba saiu;
- roupeiro do Gabriel com **duas portas de correr no SI Forma, uma de espelho prata**.
  A folha de espelho é a "porta de espelho em alumínio" da Base (R$ 700/m²);
- "os demais serão **portas de giro com puxador em cava**": os dois closets;
- "todos os MDFs serão no padrão **Nude Vel Guararapes**": nem o miolo fica em Branco TX.
  As chaves `MDF Nude Velluto 18/15/6` estão no fim da Base (importada), com o preço
  da linha Melamínico Fosco;
- **três viagens de frete** no closet da suíte, digitadas por ele na célula amarela.

⭐ Closet da suíte master com **dez gavetas e sapateiras**: três sapateiras no módulo 1
da E1, quatro gavetas no módulo 3 e três sapateiras no módulo A da E2.

**Planilha:** `1GT83X1kSwGQ83xXuHJfQ-NvUJAC41WBaP350l06oZT4`
https://docs.google.com/spreadsheets/d/1GT83X1kSwGQ83xXuHJfQ-NvUJAC41WBaP350l06oZT4/edit
Copiada da BASE da casa (`11IgmtI5…`), na pasta `Orçamentos Valvic`.

**Pasta das pranchas:** `Orçamentos Valvic / Ana Carolina e André - [35] Apto Funcionários`
(`1ZBIwyOh_Bv8DtudizomUfXwfAEEdqlJN`) · https://drive.google.com/drive/folders/1ZBIwyOh_Bv8DtudizomUfXwfAEEdqlJN
⚠ Os PDFs (35_.1 SUITE MASTER, QUARTO GABRIEL, CLOSET ISABELLA) entram nela à mão:
o conector do Drive só sobe arquivo com o conteúdo inteiro dentro do comando, e
1,5 MB de PDF vetorial não cabe [06/11/2026].

✅ IMPORTRANGE autorizado pelo Jonathan em 06/11/2026: a Base chega inteira.

## Os arquivos

- `levantamento.py` · as peças, item por item, com a chave da Base na coluna K.
- `planilha.py` · monta as abas no layout do Gustavo e grava `_abas.json`. Também
  calcula o que a planilha **tem de mostrar** depois do clique.
- `_abas.json` · as linhas exatamente como foram gravadas, aba por aba.

## O que a planilha mostra (MC 45% = 40% + Médio) · versão de 06/11/2026

| Ambiente | Folhas | Gavetas | Custo direto | Preço (base 76,09%) |
|---|---:|---:|---:|---:|
| 01 Closet suíte master | 13 de giro | 10 | R$ 19.664,53 | R$ 63.255,42 |
| 02 Quarto Gabriel | 2 de correr (1 espelho) | 8 | R$ 10.870,03 | R$ 34.965,91 |
| 03 Closet Isabella | 12 de giro | 14 | R$ 17.896,10 | R$ 57.566,86 |
| **Total** | | | **R$ 48.430,65** | **R$ 155.788,19** |

✅ Conferido em 06/11/2026, já com a Base autorizada. Painel, item a item e o total
batem centavo a centavo com o `planilha.py`. As três conferências internas e a do
Painel dão zero, e nenhuma linha fica sem preço.

## ⛔ Dois defeitos da planilha BASE, achados aqui (corrigidos SÓ nesta cópia)

1. **Células mescladas na aba `00 Ambiente (modelo)`:** B:K nas linhas 15, 22, 30,
   37 e 41. Tudo que se grava em C:K de uma linha mesclada **some sem erro**. Aqui
   isso apagou a linha de Ferragem, a de Corte por chapa e o Arredondamento de
   chapa. ⭐ Na cópia, primeiro desmesclar de 5 a 160 e só depois gravar.
   ⭐ E texto longo pede `OVERFLOW_CELL`: com `CLIP` ele é cortado na borda da coluna B.
2. **`Preço e Comissões` aponta para a célula vazia.** E14:E27 multiplicam por
   `$D$33` e D34/E35 leem `$D$31`/`$D$33`, mas o custo e o preço moram na coluna
   **E**, em E31 e E33. Na Planilha do Gustavo já está `$E$33`. E o quadro ④ procura
   a dificuldade em `$B$66:$D$68`, mas a tabela está em **B67:D69**: assim o
   "Complexo" nunca seria achado.
