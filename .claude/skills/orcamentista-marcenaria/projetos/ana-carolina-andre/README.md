# Ana Carolina e André · projeto [35] de Ana Maria

Quatro ambientes com marcenaria: roupeiro da Suíte master, closet da Suíte master,
roupeiro do Quarto Gabriel e closet da Isabella. **Ferragem Blum · RT 10% · sem
vendedor** [Jonathan, 05/11/2026]. ⭐ Closet da suíte master com **até dez gavetas e
sapateiras**: são três sapateiras no módulo 1 da E1, quatro gavetas no módulo 3 e
três sapateiras no módulo A da E2.

**Planilha:** `1GT83X1kSwGQ83xXuHJfQ-NvUJAC41WBaP350l06oZT4`
https://docs.google.com/spreadsheets/d/1GT83X1kSwGQ83xXuHJfQ-NvUJAC41WBaP350l06oZT4/edit
Copiada da BASE da casa (`11IgmtI5…`), na pasta `Orçamentos Valvic`.

⛔ **Primeiro passo:** aba `Base (importada)`, clicar no `#REF!` da D3 e escolher
**Permitir acesso**. Sem o clique, MDF e ferragem Blum saem a zero.

## Os arquivos

- `levantamento.py` · as peças, item por item, com a chave da Base na coluna K.
- `planilha.py` · monta as abas no layout do Gustavo e grava `_abas.json`. Também
  calcula o que a planilha **tem de mostrar** depois do clique.
- `_abas.json` · as linhas exatamente como foram gravadas, aba por aba.

## O que a planilha tem de mostrar depois do clique (MC 45% = 40% + Médio)

| Ambiente | Custo direto | Preço (base 76,09%) |
|---|---:|---:|
| 01 Suíte master | R$ 6.519,94 | R$ 20.972,88 |
| 02 Closet suíte master | R$ 12.622,54 | R$ 40.603,26 |
| 03 Quarto Gabriel | R$ 9.409,49 | R$ 30.267,76 |
| 04 Closet Isabella | R$ 11.988,74 | R$ 38.564,52 |
| **Total** | **R$ 40.540,72** | **R$ 130.408,41** |

✅ Conferido em 05/11/2026, antes do clique e só com os preços locais (fita,
filetagem, suporte, perfil de piso, corte, frete, consumíveis e embalagem). Painel
e Python bateram centavo a centavo nas quatro abas: R$ 570,28 · 1.356,64 · 817,01 ·
1.239,98. Os preços que chegam pelo IMPORTRANGE (Fosco 350/550/700, Branco TX
250/350/400, Corrediça Blum 300, Dominus 800, Trilho 350, Desempenador 100,
Cabideiro 120, Cava 50) foram lidos direto na Base de Custos: são os mesmos do
`planilha.py`.

## ⛔ Dois defeitos da planilha BASE, achados aqui (corrigidos SÓ nesta cópia)

1. **Células mescladas na aba `00 Ambiente (modelo)`:** B:K nas linhas 15, 22, 30,
   37 e 41. Tudo que se grava em C:K de uma linha mesclada **some sem erro**. Aqui
   isso apagou a linha de Ferragem, a de Corte por chapa e o Arredondamento de
   chapa. ⭐ Na cópia, primeiro desmesclar de 5 a 160 e só depois gravar.
2. **`Preço e Comissões` aponta para a célula vazia.** E14:E27 multiplicam por
   `$D$33` e D34/E35 leem `$D$31`/`$D$33`, mas o custo e o preço moram na coluna
   **E**, em E31 e E33. Na Planilha do Gustavo já está `$E$33`. E o quadro ④ procura
   a dificuldade em `$B$66:$D$68`, mas a tabela está em **B67:D69**: assim o
   "Complexo" nunca seria achado.
