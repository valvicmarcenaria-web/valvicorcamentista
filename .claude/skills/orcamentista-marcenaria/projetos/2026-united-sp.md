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
