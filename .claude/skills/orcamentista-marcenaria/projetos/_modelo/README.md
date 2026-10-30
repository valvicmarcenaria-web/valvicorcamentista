# A PLANILHA BASE DA VALVIC — o modelo de onde todo orçamento sai

**Modelo:** `1Wl5j1HgBiakn6HiRm0WFRFakDq_jtmAFSjKK2YNjpkc`
https://docs.google.com/spreadsheets/d/1Wl5j1HgBiakn6HiRm0WFRFakDq_jtmAFSjKK2YNjpkc/edit
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
| `gerar_formato.py` | emite o lote de requests de formato das quatro abas fixas |

⛔ **A aba não se formata, ela se GERA.** A regra é a mesma que o `aba.py` aprendeu
em 28/10, quando o Living e a Cozinha saíram diferentes em quinze pontos: duas mãos,
dois resultados.

⚠ **`fontSize` da API é INTEIRO.** Um 9,5 derruba o lote inteiro com "Internal
error", e o erro não diz qual request falhou.
