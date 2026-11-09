# Haverson Soares · Cozinha e Gourmet

Projeto de **Luiza Pacheco Arquitetura**, a mesma arquiteta do Gustavo Raposo. Rev.00,
de outubro de 2026. Rua Jatobás, 125, Residencial Árvores, Alphaville, Nova Lima/MG.

**Planilha:** `1m5Hq9Yd_KxXJy9lEe5CUHbrQNHdDTDo6gFQbNKxg8NE`
https://docs.google.com/spreadsheets/d/1m5Hq9Yd_KxXJy9lEe5CUHbrQNHdDTDo6gFQbNKxg8NE/edit
Copiada da BASE da casa (`11IgmtI5…`), na pasta `Orçamentos Valvic`.

⛔ **O IMPORTRANGE precisa ser autorizado:** na aba "Base (importada)", clique no
`#REF!` da célula D3 e depois em PERMITIR ACESSO. Até lá, o MDF e parte da
ferragem saem a zero.

⭐ Na cópia, antes de gravar, foram corrigidos os três defeitos da BASE:
- as células mescladas da aba-modelo foram desmescladas;
- as linhas E14 a E27, D34 e E35 da "Preço e Comissões" passaram a ler a coluna E;
- o quadro ④ passou a procurar a dificuldade em `$B$67:$D$69`.

## Os arquivos

- `levantamento.py` · as peças, item por item, com a chave da Base.
- `planilha.py` · monta as abas no layout da casa, com a formatação, e grava `_abas.json`.
- `precos.py` · a cascata e o preço a MC 35, 38 e 40.

## As três linhas · 06/11/2026

⭐ [Jonathan] "vamos trabalhar com as nossas três linhas": Telescópica, Hettich e
Blum no lugar da Häfele da prancha. A planilha mostra a **Hettich**, a de referência;
`precos.py` calcula as três.

A cascata usa nota 5%, margem de erro 2%, RT 10% (⚠ a confirmar), sem vendedor e sem
cartão. A base fica em **76,09%**, a mesma do Attos.
- **Item sem corrediça nem dobradiça da linha:** MC **38%** nas três linhas, com o
  mesmo preço em todas.
- **Item com ferragem de linha:** a escada do Attos, com **35 / 38 / 43**.
- **O que muda de uma linha para outra:**
  - Telescópica: corrediça R$ 15 e dobradiça R$ 4.
  - Hettich: corrediça R$ 150 e dobradiça R$ 50.
  - Blum: corrediça R$ 300 e dobradiça R$ 50.

⭐ [Jonathan, 09/11/2026] "no geral vamos reduzir a mc em 4% · em específico no rack vamos
reduzir em 10%". São pontos de MC: os itens sem ferragem da linha saem a 34%, e a escada
fica em 31 / 34 / 39. No rack, o corte é de 10 pontos no lugar dos 4, e a escada dele
fica em 25 / 28 / 33. A cozinha existente é preço fechado e não se move.
⚠ Tudo isso fica abaixo do piso da casa (35%), menos a Blum.

| Ambiente | Telescópica | Hettich | Blum |
|---|---:|---:|---:|
| Cozinha | 26.405 | 36.144 | 47.095 |
| Gourmet | 25.570 | 31.229 | 38.318 |
| Sala · rack com a torre de nichos | 11.027 | 12.300 | 13.727 |
| Sala · portas com sistema mão amiga | 11.386 | 11.386 | 11.386 |
| Cozinha existente (preço fechado) | 2.500 | 2.500 | 2.500 |
| **Total** | **76.887** | **93.559** | **113.027** |
| Antes do corte de MC | 85.950 | 105.060 | 128.440 |
| MC efetiva do levantado | 31,2% | 33,2% | 37,0% |

## As pranchas (`pranchas/`)

| Folha | O que é |
|---|---|
| 01 | Cozinha · planta de layout, 1/25 |
| 02 | Cozinha · elevação A (pia e cooktop) |
| 03 | Cozinha · elevação B (geladeira) |
| 04 | Cozinha · elevações C (torre quente e bancada) e D (colmeia na ilha) |
| 05 | Gourmet · planta de layout |
| 06 | Gourmet · elevação A, vistas externa e interna da cristaleira |
| 07 | Gourmet · elevação B (torre quente) |

## O que já foi lido

### Materiais e ferragens

- **MDF Azul a definir** (melamínico de cor) nas frentes. Interno em **MDF Branco**.
- No gourmet: **MDF Freijó Puro, linha Essencial Wood, Duratex** na torre, nos
  superiores, na cristaleira e na colmeia.
- Puxador cava na marcenaria.
- **Ferragens Häfele**, com corrediça oculta.
  - ⚠ Häfele não está na Base de Custos: cotar.

### Cozinha

- **Inferiores sob a bancada de pedra existente:** 415 de frente na pia e 174 na
  parede da geladeira, com frente de 68, sobre o sóculo existente.
  - **Pia:** módulos 52,5 · 52,5 · 25 (porta-temperos) · 77 · 3 × 69,33.
    - 8 gavetões e 2 gavetas.
    - 3 básculas que abrem para baixo, sob as cubas.
  - **Geladeira:** 2 módulos de 87, com 4 gavetões.
- **Máscara da geladeira:** 2 × 59 × 195.
- **Armário sobre a geladeira:** 88 × 49 × 59, com 2 portas de giro.
- **Torre quente:** 80 × 249 × 60.
  - Superior de 74 com 2 portas e prateleira.
  - Nichos do micro-ondas de 34 L (39 de altura) e do forno de 80 L (60).
  - Gavetão de 29.
- **Superiores sobre a bancada:** 157 × 74 com 4 portas de giro e 1 prateleira.
  ⚠ O corte B mostra os superiores com 60 de profundidade.
- **Bancada em MDF Azul:** 157 × 60 × 3.
  - Nicho de 55 para a adega Brastemp de 33 garrafas.
  - Armário de 102 com 2 portas de giro.
- **Painel fixo do piso ao teto:** 72 × 249. Mais a lateral fixa de 60 × 80.
- **Colmeia de vinhos** em Freijó, na ilha de pedra existente.
  - 91 × 64, com 7 × 5 nichos e divisórias de 2.
  - ⚠ Profundidade não cotada.

### Gourmet

- **Cristaleira em Freijó:** 51 × 254 × 60.
  - 1 porta de giro em vidro reflecta bronze com perfil bronze.
  - 3 prateleiras, com perfil de LED com abas.
  - Nicho de 78 para a adega existente.
- **Inferiores em Azul:** 246 (4 × 61,5) com 3 básculas, 4 gavetões e 2 gavetas.
  Mais 132 (2 × 66) com 4 gavetões, 42 de profundidade.
- **Superior em Freijó:** 192 × 89 × 30. É um nicho de 60 mais um armário de 132 com
  4 básculas que abrem para cima.
- **Torre quente em Freijó:** 95 × 254 × 60.
  - Superior de 75 com 2 portas.
  - Micro-ondas e forno com requadros de 17,5.
  - Gavetão de 35.

### Fora do escopo

- ⛔ **Pedra não é nossa:** bancadas, complemento de bancada, frente dos sóculos
  ("frente no mesmo material da bancada"), frontão e ilha.
- Eletrodomésticos, cooktop, coifa, cubas e churrasqueira.
- O sóculo em marcenaria é nosso, só a estrutura.
