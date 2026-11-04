# ⭐ REGRAS DE QUANTITATIVO DA CASA — o que não se decide duas vezes

> **Cravadas pelo Jonathan em 28/10/2026**, na revisão do projeto ICA. Cada uma
> nasceu de um erro de levantamento real e cada uma vale para **todo projeto**,
> não só para aquele. ⛔ Onde outra referência divergir daqui, vale esta.
>
> Implementadas em `projetos/ica-michell/base.py` e conferidas por
> `projetos/ica-michell/auditor.py` — **regra da casa é do motor, não da lista.**
> O que o motor calcula sozinho ninguém esquece de declarar.

---

## 1 · ⛔⛔ PINUS ESTÁ PROIBIDO

> *"Não usamos peças de pinus para nada."*

O sarrafo de pinus era cômodo: R$ 8 o metro resolvia qualquer engradado sem
desenhar nada, e por isso ele aparecia como **metro linear invisível** em vez de
peça no plano de corte. Acabou. Onde ele segurava alguma coisa, entra uma de três:

| o sarrafo segurava… | agora é |
|---|---|
| engradado interno de painel ou tampo | **travessa de MDF**, tirada da própria chapa — `B.engradado()` |
| estrado de cama | **quadro de metalon** (ver 3) |
| móvel suspenso, estrutura de verdade | **serralheria estrutural**, valor fechado do serralheiro |

**O auditor quebra** se um ambiente declarar `SARRAFOS`.

---

## 2 · SUPORTE DE PRATELEIRA — R$ 6,50 por prateleira, não R$ 30 por par

> *"prateleiras internas dos armarios nao ultilizamos suporte oculto, mas
> precisamos considerar que toda prateleira interna existe a composição de 4
> suportes em um custo total de 6.50"*

- **A unidade é a PRATELEIRA**, não o par de pinos a cada 40 cm.
- Acabou o suporte oculto de R$ 30 em prateleira de armário.
- ⭐ **Não se declara.** Por ser "toda prateleira", a conta sai das peças, em
  `B.prateleiras()`. Quem **não** leva — prateleira que encaixa em rasgo, que
  pendura em haste, que é fixa cavilhada — escreve **`sem suporte`** na obs, e aí
  a exceção fica na linha do orçamento em vez de ficar na cabeça do orçamentista.

---

## 3 · ESTRADO EM METALON — R$ 250 o quadro, em TODA cama

> *"Todas as camas teremos a aplicação de estrado em metalom, tanto para a
> superior quanto para a inferior. o custo de cada quadro é de 250,00"*

⛔ O estrado **deixa de ser painel de MDF**. Um quadro por leito: beliche tem
dois, bicama tem dois, cama com bicama tem dois. Sai o painel de 15 mm **e** sai
o sarrafo que o apoiava.

---

## 4 · PRATELEIRA ACIMA DE 1,20 m PEDE ALMA DE AÇO

> *"prateleiras acima de 1.20mt vamos considerar alma de aço"*

É contra **flecha**, não contra empeno — 18 mm resolve o empeno e **não** resolve
o vão. Uma barra por prateleira. ⭐ Também **não se declara**: sai de
`B.almas_de_prateleira()`. A lista `ALMAS` fica só para coluna, montante e pé, e
o auditor quebra se alguém puser prateleira nela.

---

## 5 · CORREDIÇA TOUCH — R$ 500, e ela SUBSTITUI o pulsador

> *"no caso de corrediças com abertura por toque, considere a corrediça touch,
> não precisa de pulsador. a corrediça com toque considere o custo de 500,00"*

Quem abre é a própria corrediça. Declarar corrediça touch **e** pulsador na mesma
gaveta é pagar duas vezes pela mesma abertura — o auditor quebra.

---

## 6 · PERFIL DE PROTEÇÃO DE PISO — R$ 15 o metro linear

> *"Todos os paineis que estao em contado direto no piso terá aplicação de
> aluminio/perfil inox de proteção, calcule a extensao linear"*

Vale para **todo** painel que toca o chão. Mede-se a **extensão linear** da
frente do móvel, não o perímetro. Móvel suspenso não entra.

---

## 7 · PALHINHA NATURAL — R$ 650 o m², e é TAPECEIRO, não chapa

> *"na cabeceira vc nao considerou a palha indiana (650,00) o metro quadrado"*

⛔ **O erro que isso corrigiu foi de cinco vezes.** A palha estava orçada como
chapa melamínica "Palha Indiana Sextavada" — R$ 700 a chapa, uns **R$ 137 o m²**
depois do aproveitamento — e ela custa **R$ 650 o m²**.

A frente fica assim: **moldura em MDF** (régua, quando a moldura é de outra cor) +
**substrato de MDF estrutural** (a palhinha precisa de fundo em que se fixar) +
**palhinha natural por m²**, na linha de terceirizado.

---

## 8 · ESTOFADO — R$ 600 o m²

> *"considere o metro quadrado do estofado em 600,00"*

Deixa de ser linha a zero. É estofador, terceirizado, por m² de face estofada.

---

## 9 · BRANCO DIAMANTE É COR

> *"sao materiais de cor (branco diamante tem o mesmo preço de amadeirado)"*

**R$ 700 / 550 / 350**, como qualquer padrão de cor — e não R$ 400 / 350 / 250
como o Branco TX. Era a pergunta mais cara do ICA e está fechada.

---

## 10 · CORTE — R$ 2,00 por chapa e R$ 2,50 por peça, em CADA ambiente

> *"Em cada ambiente considere o custo de corte por chapa de 2.00 e corte por
> peça de 2.50"*

São **serviço do ambiente**, não material rateado por item: entram depois do
material, junto de consumíveis e embalagem, e por isso ficam **fora da
conferência** que compara o rateio dos itens com o painel de material.
⛔ A contagem de peça é por **PEÇA**, não por linha: uma linha de 4 prateleiras
são 4 peças.

---

## 11 · UNIFICAR O PREÇO NÃO É UNIFICAR A LEITURA

Quando o preço de vários detalhamentos vira um item só, **cada peça continua
carregando o DET de origem no nome** — senão o plano de corte fica com quatro
"Fundo" de medidas diferentes. E um item unificado pode ter **mais de um modo de
abrir** (a bicama por cava, o baú por puxador): isso se declara em `ABRE_MISTO`,
para que a exceção fique escrita e não implícita.

---

## 12 · SERRALHERIA ENTRA NA CONTA PELO VALOR DO AMBIENTE

Valor fechado do serralheiro, por móvel — ⛔ **não** se busca preço na Base. Até
28/10/2026 a linha procurava uma chave que nunca existiu e os R$ 2.500 do banco
suspenso do Living saíam **zero** nos dois lados da conferência, que por isso
fechava sem gritar. É o tipo de erro que só aparece quando se soma à mão o que a
planilha já somou.

---

## 13 · "m²" TEM DOIS SENTIDOS, E CONFUNDI-LOS ZERA UMA LINHA INTEIRA

Peça de MDF em m² se paga **por CHAPA**: a área entra dividida pela área útil da
chapa e multiplicada pelo preço da chapa. Palhinha, espelho, vidro, estofado e
malha de cordas se pagam **POR m²**: a área entra inteira.

⛔ Enquanto o discriminador da planilha foi a UNIDADE, os dois caíram na mesma
conta — e a palhinha da cabeceira da Suíte Hóspedes somou **ZERO**. Eram
R$ 2.645,50 numa linha que estava escrita certa, com a quantidade certa e o
preço certo na Base: a fórmula pedia comprimento e largura, a palhinha não tem,
e o produto deu zero sem erro nenhum na tela.

⭐ **O discriminador honesto é a CHAVE**: só `MDF …` se paga por chapa.

---

## 14 · MALHA DE CORDAS NÁUTICAS — R$ 250 o m²

> *"na base da cama superior, inferior e bicama considere a estrutura de
> serralheria, considere a malha de cordas naulticas a 250,00 mt²"*

Na Suíte 03 ela **substitui** o estrado em metalon das três bases: quadro de
serralheria com a malha tecida dentro. ⛔ Quadro de metalon **mais** malha seria
cobrar duas bases para o mesmo colchão.

---

## 15 · MOLDURA DE MESMA COR É PROVENÇAL; DE OUTRA COR É RÉGUA

É a mesma regra lida dos dois lados:

- **mesma cor** → duas **chapas inteiras**, a base lisa e a de cima usinada na
  router. Vale para frente de armário **e** para moldura de espelho em arco: no
  Banho Mariana a moldura estava quebrada em quatro réguas de 3 cm, e régua
  emenda — numa moldura de cor única a emenda aparece.
- **outra cor** → **régua**, porque peça inteira cobriria o material de baixo.
  É o caso da moldura de Sal Rosa sobre a palha indiana, e do Oásis sobre a
  palha no aparador da Suíte Hóspedes.

⭐ A auditoria confere o par: a peça usinada tem de ter o **mesmo tamanho e a
mesma quantidade** da base, e uma linha de mão de obra por folha.

---

## 16 · NICHO COM INTERIOR DE OUTRA COR É MATERIAL DUPLO

> *"observe que são materiais duplos, ou seja, o dobro de material"*

Em melamínico **uma chapa não tem duas cores**. Se a caixa é de uma cor por fora
e o nicho é de outra por dentro, cada face é **duas peças coladas** — pele
externa e pele interna. Era o furo da mesa lateral da Suíte Mariana: eu contava
uma só.

---

## 17 · NÃO EXISTE "MDF PALHA INDIANA SEXTAVADA"

> *"não existe mdf palha indiana sextavada, isso é a palha indiana (650,00 mt²)"*

É a palha do **tapeceiro**, R$ 650 o m². O que a marcenaria faz é o **fundo em
que ela se fixa** — e esse fundo sai em MDF estrutural, ⛔ sem fita, porque as
arestas morrem sob a moldura.

---

## 18 · ⛔ NEM TODA PEÇA COM "PRATELEIRA" NO NOME É PRATELEIRA

O motor conta suporte e alma pelo **nome**, e o nome mente. Não levam suporte
nem alma:

- **painel** que se chama "painel das prateleiras" — é painel;
- **divisória** vertical, mesmo numa sapateira;
- **horizontal fixa** cavilhada, que é o teto de um bloco e a base do outro;
- a **camada de baixo** de uma prateleira duplada — é a MESMA prateleira;
- prateleira **pendurada em haste** de metal, sem armário;
- as horizontais que **fazem** os nichos de uma torre embutida;
- **sapateira corrediça**, que já tem par de corrediça orçado.

⭐ A exceção se escreve na `obs` da peça — `sem suporte`, `sem alma` — e aí fica
na linha do orçamento, não na memória de quem levantou. Foram **nove** peças
assim no projeto ICA, e cada uma cobrava um jogo de suportes que não existe.

---

## ⛔⛔⛔ REGRA 19 — A FRONTEIRA DO ESCOPO [Jonathan, 29/10/2026]

> *"pedra nao é escopo da marcenaria. espelhos, vidros e serralheria que
> estiverem na marcenaria é nosso."*

**PEDRA NUNCA.** Granito, quartzito, mármore, silestone: bancada, sóculo,
frontão, tampo, soleira e peitoril ficam fora do custo e fora da proposta.
Não se lança a linha nem a zero. Vai para "o que não está nesta proposta".
⚠ O executivo desenhar a pedra junto do armário não a torna nossa.

**ESPELHO, VIDRO E SERRALHERIA, SIM — quando fazem parte do móvel.** Espelho
de porta de roupeiro, vidro de cristaleira, estrado de cama, alma de aço,
haste de prateleira, quadro de leito: medimos, fornecemos e instalamos.
⛔ Box, janela, guarda-corpo, portão, grade, pergolado e escada metálica não.

⭐ **O teste:** sai no mesmo caminhão e é instalado pela mesma equipe? É
nosso. Existe sem o móvel? Não é.

⛔ **Dois estados, só dois:** ou é nosso COM VALOR na linha, ou está nomeado
na proposta como fora. Linha a zero com promessa de fornecimento é prometer
com o dinheiro do lucro.
