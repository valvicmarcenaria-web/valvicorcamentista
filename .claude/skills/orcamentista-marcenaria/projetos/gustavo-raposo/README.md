# Gustavo Raposo · casa inteira · Condomínio Vale dos Pinhais, Nova Lima (MG)

Arquiteta **Luiza Pacheco** (CAU A69992-6) · executivo Rev.00, março/2026 · **75 pranchas**.
⛔ Pergolado (11–16) e SPA (17–18) **não entram** [Jonathan].

**Planilha:** `1HovPv64ISuL-cnRUNyKpxoPdZqvkzMQyiAYBNYiexE8`
https://docs.google.com/spreadsheets/d/1HovPv64ISuL-cnRUNyKpxoPdZqvkzMQyiAYBNYiexE8/edit

**Planilha BASE da casa, de onde ela saiu:** `1slBElrHqfJDgZ67NrVW1DMLfJ5ioiB4LyMlVXvqoD8E`
https://docs.google.com/spreadsheets/d/1slBElrHqfJDgZ67NrVW1DMLfJ5ioiB4LyMlVXvqoD8E/edit

⭐ **As duas moram na pasta `Orçamentos Valvic`** (`1liWjdBNktz6C4087YhbJq0gufVwcYSBx`),
ao lado das outras — é lá que se procura quando se vai começar um orçamento, e é de
lá que se copia o modelo. ⛔ A planilha do cliente **não** fica na pasta do projeto
do arquiteto: aquela é a pasta das pranchas, que vêm de fora.

⛔⛔ **O QUE DEU ERRADO ANTES, para não se repetir.** A primeira planilha do Gustavo
foi uma **cópia da planilha do ICA**, e isso estava errado por dois motivos, não um:

1. **Dado de outro cliente.** [Jonathan, 29/10] *"não pode haver informações
   relacionadas ao orçamento do michell, é outro cliente."* A cópia trazia as
   dezenove abas da Jéssica e do Michell, com as medidas e os preços deles dentro
   de um arquivo com o nome do Gustavo. ⛔ Não se copia orçamento de cliente para
   começar outro. Copia-se **modelo**.
2. **Erro em cadeia.** Copiar uma planilha com `IMPORTRANGE` **quebra o vínculo**:
   o Google exige uma autorização nova em toda cópia, e ela só pode ser dada por
   uma pessoa, clicando. Sem o clique, a `Base (importada)` volta vazia, todo
   `PROCV` em `precos` não acha nada e a planilha inteira vira `#DIV/0!`. Era o
   que o Jonathan estava vendo.

⭐ **A planilha BASE resolve os dois.** É um modelo vazio, sem cliente nenhum, com
a infraestrutura pronta: a `Base (importada)`, a `Preço e Comissões` com a cascata
de encargos, o `precos` nomeado, o Painel e **uma aba de ambiente para duplicar**.

⛔⛔ **EM TODA CÓPIA NOVA, O PRIMEIRO PASSO É O CLIQUE.** Abrir a aba
`Base (importada)`, achar o `#REF!` na célula **N1** e clicar em **Permitir acesso**.
Nenhum script pode dar essa autorização — é trava de segurança do Google, não
defeito do arquivo. O aviso está escrito no topo do Painel das duas planilhas.

⭐ **A BUSCA DE PREÇO MUDOU, e para melhor.** Na planilha do ICA o preço vinha por
POSIÇÃO — a célula escrevia `=I19` e torcia para que a linha 19 do bloco importado
continuasse sendo o Melamínico Fosco de 18 mm; a própria aba avisava *"LINHA NOVA
VAI NO FIM, NUNCA NO MEIO"*. Aqui o preço vem por **NOME DE PRODUTO** (e pela
espessura, quando é chapa). Inserir, remover ou reordenar linha na Base de Custos
deixou de quebrar qualquer coisa.

## Como se trabalha aqui

| arquivo | o que faz |
|---|---|
| `paginas.json` | nº da prancha → fileId no Drive, as 75 |
| `colher.py` | decodifica os `download_file_content` em `pr/<NN>-<nome>.pdf` |
| `geo.py` | lê a prancha vetorial **com posição**: agrupa cota em cadeia e confere se a cadeia fecha na cota total |
| `zoom.py` | recorta um pedaço da folha em alta resolução — ⭐ é olhando que se **conta frente** |
| `base.py` | a chapa, a peça, a gaveta e os preços desta casa |
| `<ambiente>.py` | o levantamento peça por peça, com as listas de ferragem |
| `planilha.py` | transforma o ambiente nas linhas da aba |
| `auditor.py` | ⛔ **roda até ficar limpo ANTES de gerar a aba** |
| `aba.py` | gera o lote de requests de formato para o Sheets |

## ⭐⭐ O que esta casa tem de diferente do ICA

1. **FERRAGEM HETTICH NA CASA TODA**, 10 anos uniformes. O executivo vem misto —
   invisível em dez ambientes e telescópica em cinco — e onde pede telescópica
   nós **subimos**. Preço pela razão **0,71** sobre a Blum, apurada no ICA.
2. **NOVE PADRÕES** de MDF Duratex, todos de cor.
3. ⛔ **A COZINHA É LACA** M048 Sayerlack: MDF **cru** mais pintura em cabine,
   com **moldura provençal de 5 cm** em toda frente.
4. **Dobradiça de porta de vidro com modelo**: GV48 1011, inox, 90°.
5. ⛔ **PEDRA NÃO ENTRA** — nem granito, nem quartzito, nem Nanoglass, nem sóculo
   de alvenaria, nem nicho revestido, nem box. ⭐ Mas **espelho, vidro e
   serralheria que estão NA marcenaria são nossos**.

## Estado do levantamento

| # | ambiente | arquivo | situação |
|---|---|---|---|
| 1 | Varanda | `varanda.py` | ✅ auditor limpo |
| 2 | Lavabo | `lavabo.py` | ✅ auditor limpo |
| 3 | Cozinha | `cozinha.py` | ✅ auditor limpo |
| 4 | Despensa | `despensa.py` | ✅ auditor limpo |
| 5 | Lavanderia | `lavanderia.py` | ✅ auditor limpo |
| 6 | Circulação / Rouparia | `rouparia.py` | ✅ auditor limpo |
| 7 | Hóspedes / Office | `office.py` | ✅ auditor limpo |
| 8 | Suíte Master | — | a levantar (pranchas 39–41) |
| 9 | Closet Suíte Master | — | a levantar (42–44) |
| 10 | Banheiro Suíte Master | — | a levantar (45–47) |
| 11 | Suíte 01 · Filhos | — | a levantar (48–53) |
| 12 | Banheiro Suíte 01 | — | a levantar (54–56) |
| 13 | Suíte 02 · Filhas | — | a levantar (57–60) ⚠ o mais complexo |
| 14 | Closet Suíte 02 | — | a levantar (61–62) |
| 15 | Banheiro Suíte 02 | — | a levantar (63–65) |
| 16 | Suíte Hóspedes | — | a levantar (66–68) |
| 17 | Banheiro Suíte Hóspedes | — | a levantar (69–70) |
| 18 | Banheiro Social | — | a levantar (71) |
| 19 | Homeschooling | — | a levantar (72–75) |

⛔ **Sala de Estar (23–24) não tem marcenaria**: só perfil de LED e o aparador de
quartzito, que é do marmorista. Não vira aba.

## ⚠ As perguntas abertas, por ordem de dinheiro

1. **Os 531 metros de usinagem do muxarabi saem ZERO** — a Base não tem linha de
   corte de router por metro. Cronometrar uma peça na fábrica resolve e dá à casa
   uma linha que serve em todo projeto com vazado daqui para frente.
2. **O preço do MDF cru é derivado, não lido** (razão 0,76 da Base antiga). É a
   chapa de toda a cozinha.
3. **R$ 650/m² é o preço da laca em peça LISA** e toda frente da cozinha tem
   relevo de router. Perguntar o acréscimo ao pintor.
4. **A cristaleira da varanda é curva?** A planta desenha R72, a elevação cotada
   desenha plana. Porta de vidro temperado não curva.
5. **O painel muxarabi se segura?** 43% vira vazio e o que sobra são ripas de 2 cm
   num painel de 4,44 × 2,71 m. A prancha não diz como ele fixa.
6. **O puxador dourado da cozinha** (catorze) e o **NEO32 Bronze** não têm modelo
   nem preço.
