# GUSTAVO RAPOSO — casa completa

**Projeto:** **Luiza Pacheco Arquitetura** · CAU **A69992-6** ·
(31) 98885-1403 · `luiza@luizapacheco.com.br`
⚠ O Drive é da conta `larissasales.arquiteta@gmail.com` — **a dona da pasta
não é a autora do projeto.** O carimbo das pranchas é da Luiza Pacheco.
**Cliente:** Gustavo Raposo · **Obra:** Condomínio Vale dos Pinhais, Nova
Lima/MG · **Etapa:** Executivo, Revisão 00, março/2026 · **75 pranchas A0**
**Executivo:** `Executivo_Gustavo Raposo_Rev.00_.dwg` — ⛔ **869 MB**, não abre aqui
**Pranchas:** pasta `PDF`, uma folha por arquivo, **01 a 75**, formato A0
**Drive:** `1Bb8tprrT32D3GtWGbvhpWzkaBFgzSUrb` · PDF: `1ViO7-Ugz0vEuvzr_oQjkNj8PX0TYpic0`
**Aberto em:** 29/10/2026

## ⭐ O FORMATO É O MELHOR POSSÍVEL

Ao contrário do ICA — 235 páginas num PDF de 111 MB —, aqui a arquiteta já
entregou **uma prancha por arquivo**, com o ambiente no nome. Isso dispensa
a divisão manual e o `paginas.json`: dá para ler ambiente a ambiente direto.

⚠ O DWG de 869 MB não serve de fonte neste ambiente. A geometria vetorial,
se precisar, sai do PDF da prancha, como no ICA.

## ⭐ OS AMBIENTES, PELA PLANTA DE LAYOUT (prancha 03)

A planta 03 nomeia o programa inteiro — e ele é **maior** do que a primeira
listagem do Drive sugeria:

**Social e serviço:** Sala de estar · Conversação · Jantar · Sala de TV ·
Varanda · Cozinha · Despensa · Despejo · Lavanderia · Lavabo · Circulação ·
Jardim de inverno · Bicicletário · Abrigo de gás · Garagem coberta

**Íntimo:** Suíte Master + closet + banho · Suíte 01 Filhos + closet + banho ·
Suíte 02 Filhas + closet + banho · Suíte Hóspedes + banho · Hóspedes/Office ·
Home School · Salão de jogos

**Externo:** Jardim · Deck · SPA · área coberta com pergolado

⛔ **SPA e pergolado estão FORA** por decisão do Jonathan.

⚠ A planta 07 (acabamentos) mostra **muita pedra** — mármore Bege Bahia em
soleira, filete e peitoril, granito Marrom Imperial, ecogranito de sóculo.
**Nada disso é nosso**, pela regra da fronteira do escopo.

## Os ambientes mapeados na primeira listagem do Drive

| folhas | ambiente |
|---|---|
| 02–10 | plantas gerais: cobertura, layout, demolir/construir, hidráulica, acabamentos, elétrica, luminotécnica |
| 12, 15, 16 | Pergolado |
| 17, 18 | SPA |
| 19, 20 | Varanda |
| 23, 24 | Sala de estar |
| 28, 30 | Cozinha |
| 31 | Despensa |
| 33, 34 | Lavanderia |
| 38 | Hóspedes Office |
| 39–41 | Suíte Master |
| 42, 44 | Closet Suíte Master |
| 45–47 | Banheiro Suíte Master |
| 48–53 | Suíte 01 Filhos |
| 54 | Banheiro Suíte 01 Filhos |
| 57–60 | Suíte 02 Filhas |
| 61, 62 | Closet Suíte 02 Filhas |
| 63–65 | Banheiro Suíte 02 Filhas |
| 66–68 | Suíte Hóspedes |
| 69, 70 | Anexo Banheiro Suíte Hóspedes |
| 71 | Anexo Banheiro Social |
| 72–75 | Home Schooling |

⚠ **O índice ainda não está completo** — a listagem do Drive vem paginada e
faltam folhas intermediárias. Fechar antes de começar o levantamento.

## O que já dá para dizer

É **outra casa completa**, do porte do ICA: área externa (pergolado, SPA,
varanda), social (sala, cozinha, despensa, lavanderia), quatro suítes com
closet e banheiro, home schooling e um anexo. ⛔ Pergolado e SPA **ficaram de fora** por decisão do Jonathan.

## ⭐ O ESCOPO, FECHADO [Jonathan, 29/10/2026]

> *"casa toda · pergolado e spa nao entram"*

✅ **DENTRO:** a casa inteira — varanda, sala de estar, cozinha, despensa,
lavanderia, as quatro suítes com closet e banheiro, hóspedes office, home
schooling e o anexo de banheiro social.

⛔ **FORA:** **Pergolado** (folhas 12, 15, 16) e **SPA** (folhas 17, 18).
Não entram no levantamento nem na proposta. Vão nomeados na folha "o que
não está nesta proposta".

⛔ **FORA por regra da casa:** toda **pedra** — bancada, sóculo, frontão,
tampo, soleira e peitoril. Ver a fronteira do escopo na `SKILL.md`.

✅ **DENTRO por regra da casa:** **espelho, vidro e serralheria que fazem
parte do móvel** — espelho de porta de roupeiro, vidro de cristaleira,
estrado de cama, alma de aço, haste de prateleira. E com **linha de valor**,
nunca a zero.

## ⭐⭐ O CAMINHO DE LEITURA — `read_file_content`, uma chamada por prancha

Testado na prancha 41 (Suíte Master, elevação do armário): devolve o **texto
inteiro da folha em ~1.500 caracteres**, sem download e sem base64.

O que vem: o **material** com padrão, linha e fabricante · o **interno** ·
o **puxador** · a **ferragem** · o **conteúdo do móvel** (maleiro, três
prateleiras, quatro gavetas, duas portas de giro) · as **cotas soltas** · e o
carimbo, que diz qual ambiente e qual elevação é.

⚠ **O que ele perde é a POSIÇÃO.** As cotas saem soltas (`131`, `4`, `510`,
`5`, `10`) sem dizer a que peça cada número pertence. Serve para **mapear** o
ambiente e cravar material e ferragem; **não serve** para amarrar cota a peça.
Para isso, o PDF da prancha — `download_file_content` + poppler.

⭐ É o mesmo padrão do ICA, e aqui sai mais barato: lá eram 235 folhas num PDF
de 111 MB; aqui cada folha já é um arquivo.

### O que a prancha 41 já entregou

| | |
|---|---|
| externo | **MDF Nogueira Caiena**, Linha Design, Duratex |
| interno | **MDF Off-White Suave**, Linha Sense, Duratex |
| puxador | **cava quadrada**, usinada na marcenaria |
| ferragem | ⚠ **corrediças telescópicas** |
| conteúdo | maleiro, 3 prateleiras, 4 gavetas, 2 portas de giro |

⛔⛔ **A ARQUITETA ESPECIFICOU TELESCÓPICA.** Pela tabela da casa
(`closer-vendas/referencias/garantia.md`), telescópica é o tier mais baixo:
**2 anos de garantia**. Pela regra do elo mais fraco, UMA telescópica no
projeto derruba a garantia da casa inteira para 2 anos.

⚠ **Isto é decisão do Jonathan, antes de eu levantar peça:** seguir a prancha
e orçar telescópica, ou subir para oculta — Hettich (10 anos) ou Blum
(30 anos) — como fizemos no ICA e na Eliza. A diferença é de preço E de
garantia, e muda o discurso inteiro da proposta.

## Próximos passos

1. Fechar o índice de pranchas (paginar a listagem do Drive até o fim).
2. Ler as plantas gerais 03 (layout) e 07 (acabamentos) — elas dão o mapa
   dos ambientes e a tabela de materiais da casa inteira.
3. ⭐ **Decidir a ferragem** (ver acima) — trava a garantia e o preço.
4. Ler as ~55 pranchas de ambiente com `read_file_content`, uma chamada cada,
   e montar o mapa de material, ferragem e conteúdo por móvel.
5. Montar a planilha no mesmo motor do ICA, já com a linha de frete na coluna
   de custo e o seletor de dificuldade por ambiente.
