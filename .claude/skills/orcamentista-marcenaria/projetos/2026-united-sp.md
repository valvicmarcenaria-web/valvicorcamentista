# UNITED SP — pavimentos 8 e 9

Obra **2504 United SP**, projeto executivo **R08** de 29/07/26.
Arquitetura **VD Arquitetura — Glauco Vitor Dias**. Fit-out corporativo:
contact center, salas de reunião, lounges, copas e halls de elevador.

Levantamento: `levantamento-united-sp.md` · motor: `corte-united-sp.py` ·
proposta: `build-united-sp.py` · pranchas: `pranchas-united-sp/`.

---

## 30/09/2026 — o caderno

> *"vamos orçar um projeto novo / vou enviar mais arquivos"*

Chegaram **8 folhas**: 3 e 4 (layouts dos dois pavimentos), 11 (cozinha do
9°), 12 e 13 (cozinha do 8°, em dois módulos, mais a bancada alta), 14
(painéis do hall, que se repetem nos dois pavimentos), 15 (prateleiras 01 a
05) e 19.1 (fechamento dos quadros de energia).

⭐ **Primeiro caderno deste histórico com camada de texto.** As cotas e
legendas saem por extração, não por rasterização. Ainda assim cada folha foi
aberta e conferida no desenho — texto extraído dá o número, não diz a qual
peça ele pertence.

⚠ **Faltam as folhas 1, 2, 5 a 10 e 16 a 20.** As 16 a 20 caem no meio da
sequência de detalhamento de marcenaria e podem trazer mais escopo.

---

## 01/10/2026 — as definições, e o orçamento

> *"1 - não · 2 - Nao são nossas · 3 - isso é suporte oculto de 40 em 40cm
> aprox. custo unitario de 30,00 · 4 - Sera um puxador em uma das ripas ·
> 5 - pode considerar a profundidade com 83cm. obs, se atente para os
> montantes encorpados, deve ser 5cm de espessura. considere a construção com
> dois chapas de 6mm prenchida para dar a espessura correspondente."*
> *"esse projeto é em Sao Paulo, capital. Considere os seguintes custos:
> carreto para entrega 8k · logistica equipe 2,5k · estadia e alimentacao
> equipe 4k · hora extra 1.5k. considere RT tbm."*

### O que saiu do escopo

**Granito São Gabriel escovado** e as **52 estações do contact center**.
As estações estavam cotadas no layout (5,31 × 1,78 × 0,90) e **sem folha de
detalhe** — era exatamente o tipo de coisa que, descoberta depois, vira
briga de escopo no meio da obra.

### ⭐ Montante encorpado: a instrução que mudou o plano de corte

O projeto desenha laterais, travessas e prateleiras com **5 cm de corpo**.
Não existe chapa melamínica de 5 cm. A instrução do Jonathan define a
construção: **duas faces de 6 mm sobre miolo**, mais a testeira que fecha
os 5 cm de topo.

O motor ganhou `enc()`, que lança as três peças de uma vez e acumula o m² de
miolo à parte:

```python
def enc(mov, cor, desc, c, l, q=1):
    a(mov, cor+'6', desc+' · face',     c, l, q*2)
    a(mov, cor+'6', desc+' · testeira', (c+l)*2, 5, q)
    ENCA[mov] += c*l*q/10000
```

Efeito: **58,5 m² de Tauari de 6 mm** no plano de corte — mais que o Tauari
de 18. Encorpado não é detalhe de acabamento, é metade da chapa clara do
projeto.

### ⛔⛔ O painel do hall tem 2,80 e a chapa tem 2,75

O achado da rodada, e ele apareceu no plano de corte, não na leitura.

A primeira passada emendou os painéis de 2,80 em dois módulos — porque é o
que o nesting faz com peça maior que a chapa. Uma emenda horizontal
**atravessando o ripado do hall do elevador, na altura dos olhos**.

A saída estava no próprio desenho: a prancha pede *"iluminação indireta sob
painéis em marcenaria"*. Então o pano ripado para em 2,70 e os 10 de cima
viram a **sanca que recebe a luz**. O painel sobe inteiro.

| | chapas | aproveitamento | custo de chapa |
|---|--:|--:|--:|
| com o painel emendado | 78 | 57% | 32.970 |
| **com a sanca** | **69** | **66%** | **28.250** |

**R$ 4.720 de chapa e 9 chapas a menos** — e some a emenda. Vale para os dois
painéis nos dois pavimentos.

### O ripado, medido

Passo extraído dos vetores da prancha: **5,0 cm**, linha simples, sem par
ripa/vão. Isso é **friso usinado na própria chapa**, não ripa aplicada. Ripa
de 5 cm justaposta num painel desse tamanho custaria mais em fita do que em
chapa, e não é o que o desenho mostra. Lancei usinagem + selagem do canal por
m² de painel.

### ⚠ A logística de São Paulo é 22% do custo direto

| | |
|---|--:|
| carreto para entrega | 8.000 |
| logística de equipe | 2.500 |
| estadia e alimentação | 4.000 |
| hora extra | 1.500 |
| **total** | **16.000** |

⛔ **O modelo regional de `logistica.md` não se aplica** — é outra praça.
Os valores são fechados, do Jonathan, e entram como linha única rateada pela
área de chapa.

Sobre R$ 71.558 de custo direto, são **22% do custo**. No preço, com a
BASE e a MC desta proposta, a logística sozinha responde por cerca de
**R$ 42.200 dos R$ 188.500**. Não é despesa de rodapé: é o quarto maior item
do orçamento, atrás só de chapa, serviços e ferragem.

### O modelo

`RT_ON = True`, sem comissão de venda → **BASE 76,52%**.
MC direcionada por complexidade, nos alvos padrão da casa: **35%** painelaria
· **38%** armários e fechamentos · **40%** ripado, prateleiras suspensas e
bancada alta.

### Abertura do custo direto

| | R$ |
|---|--:|
| chapa (69 chapas, aproveitamento 66%) | 28.250 |
| fita de borda | 3.454 |
| miolo encorpado | 2.677 |
| consumíveis | 2.063 |
| **logística São Paulo** | **16.000** |
| ferragem | 6.932 |
| serviços e usinagem (ripado, LED, puxadores) | 10.780 |
| embalagem | 1.403 |
| **CUSTO DIRETO** | **71.558** |

Ferragem: **88 dobradiças**, **12 pares de corrediça**,
**74 suportes ocultos** de prateleira a R$ 30 (preço do Jonathan).

### O fechamento

| item | m² de chapa | custo | **venda** | MC |
|---|--:|--:|--:|--:|
| Cozinha 8° | 67.2 | 15.281 | **40.010** | 38.3% |
| Hall 8° | 40.5 | 16.371 | **43.220** | 38.6% |
| Prateleiras 8° | 10.7 | 3.707 | **10.150** | 40.0% |
| Quadros de energia 8° | 9.2 | 3.035 | **7.880** | 38.0% |
| **8° pavimento** | **127.5** | **38.393** | **101.260** | **38.6%** |
| Cozinha 9° | 45.7 | 10.815 | **28.080** | 38.0% |
| Hall 9° | 40.5 | 16.371 | **43.220** | 38.6% |
| Prateleiras 9° | 8.4 | 2.945 | **8.060** | 40.0% |
| Quadros de energia 9° | 9.2 | 3.035 | **7.880** | 38.0% |
| **9° pavimento** | **103.8** | **33.165** | **87.240** | **38.5%** |
| **TOTAL** | **231.4** | **71.558** | **R$ 188.500** | **38.6%** |

**R$ 188.500**, MC **38.6%** — dentro da faixa ideal da casa (35–40%).

O **hall é o maior item do contrato**: R$ 86.440 somando os dois
pavimentos, mais que as três copas juntas. É painelaria grande, ripada e com
duas portas mimetizadas — e ela se repete idêntica.

### ★ A ferragem que eu adotei, e o que custa

A linha não foi especificada. Adotei **Hettich Sensys + corrediça oculta
Quadro** — é obra corporativa, a copa abre e fecha o dia inteiro, e é a linha
que sustenta a garantia de 10 anos da casa.

Com **Novisys + telescópica** o custo direto cai R$ 3.160
(≈ R$ 8.205 de venda) e **a garantia cai para 2 anos**
(`ferragens.md`). A decisão é comercial, não técnica.

### A proposta

`proposta-united-sp.pdf`, **4 páginas** — capa, escopo, como é feito,
investimento. Pagamento **40% na assinatura · 30% no início das montagens ·
30% após a finalização**, como pedido.

Três passes de auditoria limpos.

⚠ **O auditor de contagem ganhou duas correções nesta rodada.** O regex de
contagem usava `\s*` entre o número e o substantivo, e atravessava a quebra
de linha: a numeração de item ("03" / "Prateleiras suspensas") era acusada
como quantitativo. Passou a exigir **mesma linha** (`[\t ]*`). E, de quebra,
a lista de substantivos ganhou `painel`, `fechamento` e `suporte`, que
faltavam — o auditor saiu mais estrito, não mais frouxo.

---

## Em aberto

1. ⚠ **Faltam as folhas 16 a 20.**
2. ★ **Iluminação indireta do hall**: lancei por nossa conta (a prancha manda
   o LED sob os painéis, mas não ficou dito de quem é o fornecimento).
   São os dois painéis × dois pavimentos.
3. ★ **Linha de ferragem** — ver o comparativo acima.
4. ★ **Painel de letreiro do hall** lido como comunicação visual do cliente,
   não como marcenaria.
5. **Prazo de 75 dias corridos** é proposta minha; não foi dado.
6. ⚠ **As portas mimetizadas são rota de fuga e acesso a hidrante.** O
   puxador na ripa resolve a abertura. A **sinalização** continua sendo da
   obra, e precisa existir — porta de escada que não se identifica é
   problema de vistoria, não de marcenaria.

---

## 01/10/2026 (2º) — painel a 2,73 e a logística como bloco próprio

> *"refaça com o custo do painel considerando 273 de altura e mencione na
> proposta essa informação. coloque esses custos [a logística] de forma
> estratégica na proposta, mais separada do valor dos móveis. pense em uma
> nomenclatura profissional para esse bloco de custos."*

### O pano ripado fecha em 2,73

A rodada anterior tinha parado o ripado em 2,70 por conta própria. O Jonathan
fixou **2,73** — sobram 7 até o teto para a sanca da luz indireta, e o painel
continua saindo de chapa inteira (a chapa tem 2,75).

⭐ **E a informação vai EXPLÍCITA na proposta.** É exceção autorizada à regra
de metragem, pelo mesmo motivo que a espessura entrou no Marcelo Tolentino:
é a informação que explica por que o painel não encosta no teto. Dito na
proposta, vira decisão combinada; omitido, vira reclamação na entrega. O
auditor passou a liberar `2,73 m` e só ela.

### Mobilização e logística de obra

A logística saiu do rateio por item e virou **bloco próprio, com nome**:

> **OBRA FORA DE SEDE · Mobilização e logística de obra**
> Equipe própria da Valvic em São Paulo: transporte e carreto de entrega,
> deslocamento da equipe, hospedagem e alimentação durante toda a permanência
> e jornada estendida para cumprir o prazo nos dois pavimentos.

Na proposta aparecem **o escopo do bloco e um preço só** — não os quatro
valores de custo. Bloco de mobilização em proposta B2B se cota por verba
fechada; abrir R$ 8.000 de carreto é publicar a nossa base de custo sem
necessidade.

### ⚠ A decisão que a separação obrigou

Separar não é descontar. Repassar o bloco a custo seco custaria
**R$ 27.100** — está registrado em `modelo-de-custo.md`, seção 3.1, com a
escada inteira. Entreguei o bloco **na MC do conjunto**, para que a mudança
seja de apresentação e não um corte de preço silencioso. Se for para
descontar, que seja escolha.

### O fechamento

| | |
|---|--:|
| **Marcenaria** | **R$ 144.230** |
| **Mobilização e logística de obra** | **R$ 43.100** |
| **Investimento total** | **R$ 187.330** |

MC **38,7%**. Caiu R$ 1.170 contra a rodada anterior — efeito do painel a
2,73 e do arredondamento do bloco separado.

### ⛔ A página de investimento estourou, e os dois auditores pegaram

O bloco novo não cabia. O auditor de conteúdo acusou a perda do "Não
inclusos" e o de transbordo acusou **rodapé perdido** — a checagem criada
ontem, no Marcelo Tolentino, ganhou o dia na primeira proposta seguinte.
Resolvido tirando os subtotais por andar (o agrupamento já se lê pela
etiqueta da esquerda) e pondo as condições em quatro colunas.

---

## 01/10/2026 (3º) — mobilização em 25k e ferragem Hettich fechada

> *"vamos colocar a mobilização e logística de obra em 25k, faça as
> compensações. especifique ferragens Hettich."*

### A compensação

O bloco fecha em **R$ 25.000** e os R$ 18.100 de diferença voltam para o
móvel. **O total não se mexe** — o que se mexe é onde a margem está.

| | móveis | mobilização | TOTAL |
|---|--:|--:|--:|
| bloco na MC do conjunto | 162.330 | 43.100 | 187.330 |
| **bloco fechado em 25k** ← entregue | **162.310** | **25.000** | **187.310** |
| MC de cada parte, agora | **42.9%** | **11.2%** | **38.7%** |

A compensação **desloca a escada inteira de MC por um mesmo delta**
(**+4.2 pontos**), resolvido por bisseção, em vez de somar um
acréscimo linear no preço. Assim painelaria (35), armário (38) e item
especial (40) mantêm a distância entre si — é a mesma régua, deslocada:

```python
def _mov_total(d):
    return sum(round(CD_AMB[am]/(BASE - (MC_ALVO[am] + d))/10)*10 for am in AMBS)
lo, hi = 0.0, 0.35
for _ in range(80):
    mid = (lo+hi)/2
    if _mov_total(mid) < ALVO_MOV: lo = mid
    else: hi = mid
```

### ⚠ O que a compensação custa, e onde ela aparece

O móvel passa a ler **42.9% de MC — acima da faixa 35–40 da casa**.
A margem não sumiu; mudou de linha. A consequência é de exposição comercial,
não de saúde financeira:

> **Se o cliente comparar o preço do MÓVEL com outra marcenaria, ele está
> 12,5% acima da versão em que a logística carregava a própria parte.**

E a mobilização passa a rodar a **11.2%**, bem abaixo do piso — ou seja,
a ida a São Paulo quase não paga margem, e quem paga é o armário. É escolha
comercial legítima (o bloco de logística fica num valor que o cliente aceita
sem discutir), mas precisa estar registrada como escolha.

### Ferragem Hettich, especificada

| | | |
|---|--:|--:|
| Dobradiça **Hettich Sensys** — amortecimento integrado, regulagem nos 3 eixos | 88 un | R$ 3.080 |
| Corrediça **Hettich Quadro** oculta — extração total, Silent System | 12 par | R$ 1.440 |
| Suporte oculto de prateleira | 74 un | R$ 2.220 |
| Fechadura com chave | 4 un | R$ 180 |

Confirma o que já estava precificado desde a primeira rodada — **o número não
muda por causa da ferragem**. O que muda é que deixa de ser adoção minha e
passa a ser especificação, e a proposta agora **nomeia a Hettich** no escopo
das copas, na página de execução e na linha de garantia.
A referência exata de modelo sai na cotação; a linha está fechada.

### O fechamento

| item | custo | **venda** | MC |
|---|--:|--:|--:|
| Cozinha 8° | 10.434 | **30.710** | 42.5% |
| Hall 8° | 13.263 | **39.610** | 43.0% |
| Prateleiras 8° | 2.955 | **9.150** | 44.2% |
| Quadros de energia 8° | 2.395 | **6.980** | 42.2% |
| Cozinha 9° | 7.542 | **21.990** | 42.2% |
| Hall 9° | 13.263 | **39.610** | 43.0% |
| Prateleiras 9° | 2.350 | **7.280** | 44.2% |
| Quadros de energia 9° | 2.395 | **6.980** | 42.2% |
| **Marcenaria** | **54.597** | **162.310** | **42.9%** |
| **Mobilização e logística de obra** | **16.320** | **25.000** | **11.2%** |
| **TOTAL** | **70.917** | **R$ 187.310** | **38.7%** |

---

## 01/10/2026 (4º) — três divisórias, a R$ 13.300 de venda

> *"preciso que vc adicione 3 divisórias, sendo 2 em L e 1 reta com um custo
> total delas de 13.300"* · *"é no orçamento da united essa alteração"* ·
> *"mas o valor de venda é o valor informado"*

⚠ Entraram primeiro no Suzi e Guilherme, por erro meu de atribuição, e lidas
como **custo**. As duas coisas foram corrigidas: são do **United**, e
R$ 13.300 é **venda**.

### ⚠ Preço fechado, custo ainda não levantado

**Não há prancha das divisórias.** Provavelmente estão nas **folhas 16 a 20**,
que nunca chegaram. Sem medida, material nem pavimento.

Como o que está fechado é o **preço**, o que falta é o **custo** — e é ele que
decide se o negócio é bom. Lancei o custo implícito pela MC padrão da casa
para o item não distorcer a MC do conjunto, e deixei no motor o **teto de
custo** que esse preço suporta:

| | teto de custo das três |
|---|--:|
| segurando a MC padrão de 38% | **R$ 5.122** |
| no piso da casa, MC 35% | R$ 5.521 |
| ponto de equilíbrio, MC zero | R$ 10.176 |

⛔ **Quando a prancha chegar, é contra o teto de R$ 5.122 que o
levantamento tem de bater.** Acima disso, R$ 13.300 deixa de pagar a margem
da casa; acima de R$ 10.176, deixa de pagar o próprio custo.

Na proposta a linha diz só o que se sabe: *"duas divisórias em L e uma reta,
no mesmo padrão construtivo e na mesma paleta do restante do fit-out.
**Medidas, posição e acabamento a confirmar em projeto** antes do corte."*

### A divisória fica FORA da compensação

A mobilização continua fechada em R$ 25.000 e a compensação continua
segurando o total dos móveis desenhados. **A divisória entra por fora, com
preço próprio**, porque o preço dela já veio fechado — pô-la dentro da
bisseção faria o deslocamento de MC dos outros itens mudar para acomodar um
número que não se move.

### O fechamento

| | |
|---|--:|
| 8º andar | 86.430 |
| 9º andar | 75.840 |
| **Divisórias** | **13.300** |
| **Marcenaria** | **175.570** |
| **Mobilização e logística de obra** | **25.000** |
| **TOTAL** | **R$ 200.570** · MC 38.6% |

### ⛔ E uma correção no meu próprio relatório

O quadro da compensação estava imprimindo o **valor compensado nos dois
lados** — mostrava R$ 175.570 de móveis tanto na linha "bloco na MC do
conjunto" quanto na linha entregue, o que fazia a comparação não comparar
nada. Eu imprimia `ALVO_MOV` (que já é o alvo compensado) onde devia estar o
total dos móveis **antes** da compensação. Guardei `TOT_MOV0` e o quadro
voltou a dizer o que promete:

| | móveis | mobilização | TOTAL |
|---|--:|--:|--:|
| bloco na MC do conjunto | 157.530 | 43.040 | 200.570 |
| **bloco fechado em 25k** ← entregue | **175.570** | **25.000** | **200.570** |

---

## 07/10/2026 — segunda linha de divisórias

> *"acrescentar o seguinte item: divisórias de estações de trabalho
> existentes feitas em mdf melamínico fosco com 40mm de espessura na
> extensão referenciada no projeto na altura de 300mm seguido de acoplamento
> de vidro na extensão em mais 300mm de altura. Sendo vidro temperado de
> 10mm comum com lapidação reta. R$ 6.800"*

Lançada como as primeiras: **R$ 6.800 de VENDA**, pela convenção que o
Jonathan fixou em 01/10 (*"o valor de venda é o valor informado"*). Ambiente
próprio, para aparecer em linha separada no quadro de investimento.

| | antes | agora |
|---|--:|--:|
| Marcenaria | 175.570 | **182.340** |
| Mobilização | 25.000 | 25.000 |
| **TOTAL** | **200.570** | **R$ 207.340** |
| MC | 38,6% | 38,6% |

### ⚠ Por que +6.770 e não +6.800

Os R$ 30 que faltam **não são arredondamento**. A compensação da mobilização
mira `ALVO_MOV = TOT_MOV0 + PV_NEUT − 25.000`, e `PV_NEUT` é o preço que o
bloco teria carregando a **MC média do job**. O item novo entra a 38%, que é
um pouco abaixo da média que o job tinha — a média cai, o preço neutro da
mobilização cai de 43.040 para 43.010, e o total acompanha.

⭐ É consequência fiel do modelo, não defeito: o bloco de logística é
indexado à MC do conjunto, então mexer no conjunto mexe nele.

### ⚠ O teto de custo da linha nova

| | |
|---|--:|
| venda fechada | R$ 6.800 |
| custo implícito à MC de 38% | **R$ 2.619** |
| teto no piso da casa, MC 35% | R$ 2.823 |
| ponto de equilíbrio | R$ 5.203 |

⛔ **Escopo aberto dentro de preço fechado, pela segunda vez.** *"Na extensão
referenciada no projeto"* — a extensão não veio, como não vieram as folhas
16 a 20 das três primeiras divisórias.

Dois custos que somem dentro de um preço fechado:

* **40 mm não é chapa.** Melamínico vem em 15/18/25 — a faixa é construída,
  duas faces mais miolo, como o montante encorpado do hall. É custo de
  **montagem**, que não aparece no metro quadrado.
* **O vidro é terceiro.** Temperado de 10 mm com lapidação reta corre por
  R$ 350 a 550/m² em São Paulo, mais a ferragem de fixação. Dentro de
  R$ 2.619 sobram poucos metros quadrados de vidro **depois** de pagar a
  faixa de MDF.

### ⛔ A contradição que o item novo criou no documento

A linha de "não inclusos" da página 4 dizia **"vidros e esquadrias"** e
**"as estações de trabalho do contact center"** — e o item novo é
exatamente vidro temperado sobre as divisórias dessas estações. O mesmo
documento vendia e excluía a mesma coisa.

Reescrita: *"esquadrias e os demais vidros da obra — **o vidro temperado das
divisórias é nosso** —, o **mobiliário** das estações de trabalho do contact
center"*.

⭐ **Todo item novo tem de ser lido contra a lista de exclusões.** O escopo
cresce por onde se adiciona; a exclusão continua onde estava.

### ⛔ E o rodapé escorregou

Com o card 04 maior e a tabela com mais uma linha, os rodapés das páginas 2
e 4 desceram para **2,1 mm e 4,4 mm da borda** — e os três passes disseram
"tudo ok", porque a folga é medida *até o rodapé* e o rodapé desceu junto.
Nova checagem de margem mínima de 12 mm em
`referencias/proposta-comercial.md`. Depois de compactar: 793,0 e 797,5.

### Em aberto

★ Confirmar se os **300 mm de cada faixa** (MDF e vidro) são medidos a
partir do topo da divisória existente, e qual a **extensão total** — é ela
que decide se R$ 6.800 fecha.
