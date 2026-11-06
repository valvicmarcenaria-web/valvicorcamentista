# A Base de Custos — o que ela tem e de onde veio

> **Jonathan, 26/10/2026:** *"faça uma busca profunda em todo histórico de
> orçamentos bem como no motor de orçamentos, dentro do moleskine e dentro
> de todo repositório. existe mais itens registrados para compor a base.
> complemente a base toda."*

`https://docs.google.com/spreadsheets/d/13cZGej-AUTTyWZblqtraTBnc1HUECjT6fy3zy6R5mv4/edit`

## De onde cada preço veio

A varredura passou por **sete fontes**, e elas não concordam entre si:

| fonte | o que tem | quanto confiar |
|---|---|---|
| **`dados/materiais.json`** | 16 categorias, ~120 itens, de 11/06/2026 | ⭐ a base estruturada da casa |
| **`fontes/valvic_painel_ferragens.html`** | Bigfer e Hettich com preço, ciclos, carga e garantia | ⭐ catálogo comercial, preço de compra |
| **`fontes/valvic_os.html`** | a biblioteca do motor de orçamento | ⚠ conflita com o materiais.json em vários itens |
| **`referencias/chapas.md`** | vidro, portas prontas, LED, perfis, rodapé | ⭐ para esses; ⛔ a tabela de CHAPA está em outra escala |
| **`referencias/ferragens.md`** | a escada de linhas, garantia por linha, regras de contagem | ⭐ é onde mora o método |
| **os ~120 scripts `corte-*.py`** | 130 constantes de preço usadas na prática | ⭐ é o que foi cobrado de verdade |
| **falas do Jonathan datadas** | o que ele cravou | ⭐⭐ sempre vence |

⛔ **As ferramentas HTML** (`base-materiais.html`, `tabela-de-valores.html`)
**não têm preço**: são renderizadores que leem o `materiais.json`. Procurar
preço nelas é perder tempo.

## ⭐⭐ O QUE A VARREDURA CORRIGIU NA MINHA CABEÇA

Eu havia montado a Base com **cinco linhas de ferragem Blum**, como se a
casa tivesse uma linha só. **Tem cinco níveis**, e a escolha do nível é o
que move o preço de um cenário para outro:

| nível | dobradiça | corrediça | garantia Valvic |
|---|---|---|--:|
| Silver, econômico | Bigfer Slow Click 2,05 | Telescópica 8,92 | 2 anos |
| **Padrão · 70% dos casos** | **Hardt** | **Hardt Invisível P-10 · 70/par** | **5 anos** |
| Gold | Hettich Novisys 7,90 · Sensys 17,80 | Quadro V6 83 | 10 anos |
| Máximo | Sensys Onix 27,05 | Actro 5D 245 | 10 anos |
| Blum | 50 | 250 | — |

⭐ A garantia **dobra a cada degrau** — 2 · 5 · 10 — e é isso que sustenta
comercialmente uma escada de três cenários, porque a diferença de **peça**
entre eles é pequena perto da diferença de **preço**.

⛔ **Telescópica não é especificação, é rebaixamento de preço** [Jonathan
29/08/2026]. Toda gaveta sai em oculta com amortecimento.

## ⚠ OS CONFLITOS QUE A BASE AGORA REGISTRA EM VEZ DE ESCONDER

**1 · Dobradiça: 12 ou 50?** O Jonathan disse *"nossa dobradiça custa
12,00"* em 14/10 e *"valor de dobradiça, R$ 50"* em 26/10. Não é
contradição: **R$ 12 é a dobradiça da casa, R$ 50 é a Blum.** As duas estão
na Base, em linhas separadas.

**2 · Corrediça Blum: 145–178 ou 250?** A biblioteca do motor traz a
Tandembox a 145 (350 mm), 162 (450) e 178 (500). O Jonathan cravou **250
por gaveta** em 26/10. O valor dele é o que vale; os outros ficam como
histórico de SKU.

**3 · Dominus: 700 ou 1.840?** O `materiais.json` traz 2 portas a 700 e 3 a
850. A biblioteca do motor traz 1.840, 2.450 e 3.060. ⚠ Um dos dois é venda
e o outro é compra — **a conferir com o Jonathan**. Está anotado na própria
aba.

**4 · LED instalado: de 66 a 150 por metro.** Nos jobs o metro de LED
aparece em toda essa faixa, porque às vezes é só o perfil e às vezes é o
conjunto com fita, fonte, usinagem e instalação. A Base lista os
componentes separados **e** o conjunto, para que quem orça escolha
sabendo.

**5 · Chapa: duas escalas de preço.** No `chapas.md` o Melamínico Fosco
18 mm é **R$ 125**; no `materiais.json` é **R$ 600**. A tabela antiga serve
só para **posição relativa entre padrões** — foi assim que o Branco Ártico
Ultra entrou a 275/490/585, por razão e não por valor.

## O que estava faltando e entrou agora

**MDF:** Cristallo e Acetinato (as linhas de brilho e acetinado, até 1.500 a
chapa) · lâmina natural de uma e duas faces (700 a 1.600) · compensado em
seis espessuras, com a ressalva de que a chapa é 1600 × 2200 e não
2750 × 1850 · Branco TX em 9 e 25 mm · Branco Ártico Ultra para área úmida
· espessura padrão por aplicação · filetagem na máquina (2,50/m) contra
manual (4,00/m).

**Ferragens:** as cinco linhas de dobradiça e as cinco de corrediça, com
ciclos e carga · a regra de quantas dobradiças por altura de porta · pistões
de 20, 30 e 35 · Aventos HK e HF · três sistemas deslizantes de roupeiro
com os trilhos separados · **desempenador de porta, R$ 60, padrão em toda
porta deslizante** · quatro sistemas de porta de passagem e as portas
prontas · **suporte oculto de prateleira, R$ 30, de 40 em 40 cm** (preço do
Jonathan) · perfis de puxador RM195, RM213 e SP7000.

**Terceirizados:** mão de obra de marceneiro a R$ 36/h **com encargos** (o
R$ 65 que eu já tinha visto é venda) · serralheria em quatro patamares, de
12 a 180 por metro · laca e pintura · laminação de HPL separada em material
(96/m²) e mão de obra (190/m²) · palha natural, corda em cinco bitolas,
malha, linho, acolchoado e tela · perfis e rodapés metálicos.

**Vidro:** nove tipos por m² · treze combinações de porta de vidro por
folha · **duas referências confirmadas em obra** (Kenia e Fábio, 12/06/2026)
· o multiplicador **1,80 do corte orgânico** · a peça mínima de espelharia.

## ⭐ A regra de ouro desta base

**Linha com R$ vazio é buraco conhecido, não item esquecido.** O item existe,
a unidade está definida, e o preço falta. O orçamento que o usa mostra zero
e denuncia — o que é infinitamente melhor que o item não existir e o
orçamento fechar errado sem ninguém ver.

Hoje são **quinze linhas vazias**, e cada uma tem o nome de quem coteja:
Zen Designer, marmoraria, vidraceiro, e a própria fábrica para a moldura
provençal.

---

## ⭐ LINHAS NOVAS — porta de passagem feita na casa [04/11/2026]

| chave | preço | un | de onde vem |
|---|--:|---|---|
| **Miolo G-Door** | R$ 600,00 | chapa | ⭐ [Jonathan, 04/11/2026] · Guararapes, MDF de baixíssima densidade (360 kg/m³) para enchimento de porta · chapa **2.750 × 2.055 × 29,2 mm** |
| **Miolo G-Door em régua** | R$ 132,71 | m² | derivado: R$ 600 ÷ (5,65125 m² × 80%) · ⛔ a área é a DELE, não os 275 × 185 da casa |
| **Perfil de metalon** | R$ 100,00 | barra de 3 m | ⭐ [Jonathan, 04/11/2026] · 2 por folha RIPADA, contra empeno |
| **Filetagem de ripa** | R$ 2,50 | m | ⭐ [Jonathan, 04/11/2026] "a filetagem das reguas pode considerar automatica ... todo o ripado do projeto" |

⛔⛔ **A FILETAGEM DE RIPA MUDOU DE PREÇO, E NÃO ERA POUCO.** Este arquivo e o
`laminacao-e-construcao.md` diziam *"ripa de 2 cm não entra na coladeira: vai
à mão, a R$ 5,00"*, e a própria Base repete isso na linha "Filetagem manual".
**Entra.** No Attos eram 2.595,5 m — **91% da fita do projeto** —, de
R$ 12.977,30 para R$ 6.488,65.

⚠ **A parte da chapa de 6 mm daquela nota NÃO foi perguntada** e segue
valendo: o que mudou foi a ripa.

⭐ E a linha ganhou **chave própria** em vez de cair dentro da "Filetagem
automática". As duas custam R$ 2,50 hoje, mas o metro de ripa é o maior metro
de qualquer orçamento com painel ripado: dentro da outra linha ele some.

## ⭐ VIDRO REFLECTA É POR METRO QUADRADO [Jonathan, 04/11/2026]

> *"a portas de vidro como por exemplo a da cristaleira do item 3 é calculada
> pelo mt² ou seja, é 420 o mt quadrado"* — e depois: *"atualize o preço da
> porta em reflecta para **650 o mt²**"*.

⛔ **O erro não era de conta, era de UNIDADE** — e unidade errada não dá erro,
dá um número. Lido como preço de FOLHA, ele errava nos DOIS sentidos: folha
grande saía barata, folha pequena saía cara, e o total ficava perto o
bastante para não chamar atenção.

⭐ **A trava contra a reincidência é de ASSINATURA, não de comentário:** o
lançamento de vidro passou a EXIGIR as medidas da folha. Antes dava para
lançar vidro sem dizer o tamanho dele — e foi por isso que a unidade errada
passou.

---

## ⭐ ESTOFADO e PÉ METÁLICO — duas chaves novas [04/11/2026]

| chave | valor | unidade | de onde vem |
|---|---|---|---|
| **Estofado** | R$ 600,00 | **m²** | ⭐ [Jonathan] *"considere o metro quadrado do estofado em 600,00"* — regra 8 do quantitativo, não premissa deste projeto |
| **Pé metálico** | R$ 300,00 | **jogo** | ⚠ PREMISSA · é o "Serralheiro, mínimo por serviço" da Base, aplicado por mesa |

⛔ **O ESTOFADO É POR m² DE FACE ESTOFADA**, não por m² de painel: conta só a
cara que recebe espuma e tecido. A diferença é de 2× num painel estofado dos
dois lados — e esse é exatamente o tipo de erro de UNIDADE que não dá erro,
como o vidro reflecta que eu li por folha quando era por m².

⚠ **O PÉ METÁLICO É A LINHA MAIS FRÁGIL DA SUÍTE.** O 3D mostra pé metálico
fino; o executivo não desenha mesa de cabeceira em lugar nenhum. Sem seção, sem
perfil, sem acabamento. O mínimo de serralheria é a régua mais honesta que
existe para isso — e, por ser mínimo, é **conservador**: dois jogos na mesma ida
são um serviço só.
