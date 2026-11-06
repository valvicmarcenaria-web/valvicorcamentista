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

## O que a planilha mostra · versão de 06/11/2026, a da proposta

O Jonathan mexeu na planilha em 06/11/2026, e vale o que ele deixou:
- **margem de erro de 1%** em vez dos 2% da casa: BASE 77,09%;
- **sem acréscimo de dificuldade**, com MC 40% direto na D7;
- **frete de 3, 2 e 3 viagens**.

| Ambiente | Custo direto | Preço a MC 40% | Na proposta |
|---|---:|---:|---:|
| 01 Closet suíte master | R$ 19.664,53 | R$ 53.021,98 | 53.022 |
| 02 Quarto Gabriel | R$ 11.070,03 | R$ 29.848,40 | 29.848 |
| 03 Closet Isabella | R$ 18.296,10 | R$ 49.332,25 | 49.332 |
| **Total** | **R$ 49.030,65** | **R$ 132.202,64** | **132.202** |

`precos.py` refaz a cascata e trava o build se a conta deixar de bater com a planilha.
A proposta mostra cada ambiente em real cheio, e o total é a soma do que se lê.

## A proposta · `proposta-ana-carolina-andre.pdf` (14 folhas)

`build-ana-carolina-andre.py` monta o caderno do Michell e do Gustavo:
- **só a linha Blum**, com uma folha "Por que Blum" e uma folha dedicada às ferragens;
- **ferragens:** CLIP top BLUMOTION, TANDEM com BLUMOTION e o SI Ocean 80 da Siforma,
  com as imagens que o Jonathan mandou;
- **Nude Vel:** uma folha só para o padrão, por fora e por dentro;
- **sem render no projeto:** as folhas de ambiente usam as elevações do executivo,
  recortadas sem cota e multiplicadas sobre o campo Nude.

⚠ O texto da Blum e da Siforma veio das páginas indexadas na busca, porque o acesso
direto a blum.com e a siforma.com.br está bloqueado na rede da sessão.
⚠ Para confirmar:
- o preço do kit **SI Ocean 80**, orçado pelo "Sistema deslizante SI Forma" da Base
  (R$ 1.200);
- se ele recebe a folha de espelho em alumínio;
- o prazo de **60 dias** corridos.

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
