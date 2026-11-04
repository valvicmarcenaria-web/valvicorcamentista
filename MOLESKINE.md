# Moleskine Digital — Valvic

Arquivo de tarefas e recados entre sessões. Qualquer agente (Lavinia, Rodrigo, Vitor…)
pode ler e escrever aqui. Formato livre — marcar data e agente responsável.

---

## Tarefas abertas

### [2026-11-04] Attos · Costa Laguna — A CABECEIRA ESTOFADA, MEDIDA NO VETOR — Lavinia
**Solicitante:** Jonathan · **Agente:** Lavinia · **Status:** 🟡 Suíte master orçada · suíte 01 BLOQUEADA por falta de prancha

> *"olhe as duas cabeceiras estofadas no pdf dos 3ds e faça o orcamento das
> cabeceiras e mesas de cabeceiras tbm"* · depois, com dois prints:
> *"tenhos esses prints, pelas plantas vc consegue ter uma projeção de medidas"*

**A resposta foi SIM — e por MEDIÇÃO, não por semelhança.** A prancha da suíte é
export vetorial de CAD: as cotas estão em curva (só "A3" é texto de verdade),
mas a geometria é exata. Tirei a escala da cota de 467 (529,68 pt →
**0,88166 cm/pt**) e ela fecha em oito outras cotas da prancha antes de eu medir
qualquer coisa não cotada.

| peça | medida | como sei que não é chute |
|---|---|---|
| **cabeceira estofada** | **240 × 5** | centro em 642,0 · centro da cama em 642,15 → **centrada** |
| **mesa de cabeceira esq.** | **80 × 50** | fica **10,0 cm** da cama |
| **mesa de cabeceira dir.** | **90 × 50** | fica **10,0 cm** da cama |
| (a cabeceira passa **20,2 e 19,8 cm** por trás das mesas — o que o 3D mostra) | | |

⭐ **A espessura desenhada confirma a receita sozinha:** 5,0 cm é 15 mm de MDF +
30 mm de espuma + tecido. O 3D disse O QUE É; a planta disse QUANTO.

**O que entrou:** cabeceira R$ 2.169,08 · mesa de 80 R$ 1.061,10 · mesa de 90
R$ 1.108,48. Custo direto do projeto **R$ 70.767,00 → R$ 75.681,91**; preço
Hettich MC 35% **R$ 189.551,29** com frete. Duas chaves novas na Base:
**Estofado R$ 600/m²** (de face estofada) e **Pé metálico R$ 300/jogo**
(serralheria, mínimo por serviço).

**⚠ TRÊS PERGUNTAS PARA O JONATHAN** (dúvidas 9, 10 e 11 da aba 07 Suíte):

1. ⚠⚠ **A ALTURA DA CABECEIRA É PREMISSA MINHA, 120 cm** — o único número dela
   que não saiu do desenho. ⛔ **Não há elevação da parede da cabeceira em
   prancha nenhuma:** a ELEV.01 é o ripado (200 × 272) e a ELEV.02 é a parede da
   TV (467 × 275). Cada 10 cm a mais custam R$ 144 de estofado mais a chapa.
2. ⚠⚠ **As duas mesas são DIFERENTES na planta, 80 e 90.** Não é erro de
   leitura — e a planta explica (sobram 53,7 cm de parede à esquerda e só 18,4 à
   direita). Se foi desenho no olho, é trocar um número; a de 90 custa R$ 47 a
   mais.
3. ⛔⛔ **DUAS SUÍTES INTEIRAS APARECEM NO 3D E NÃO TÊM PRANCHA.** O executivo
   tem onze: cozinha (3), escritório (2), hall (3), sala/TV (1), suíte MASTER
   (2). O 3D mostra SUÍTE 01, SUÍTE 02 e PRINCIPAL. **A segunda cabeceira que o
   senhor pediu é da suíte 01 e NÃO foi orçada** — não há desenho para medir, e
   fazer por analogia seria pôr número inventado num orçamento todo medido.
   ⚠ A pergunta maior: **faltam AMBIENTES nesta conta, não uma cabeceira?**

**⛔ E A DIVERGÊNCIA QUE NÃO DEU ERRO, DE NOVO — DUAS, NO PAINEL:**
Quando a aba 07 cresceu de 94 para 148 linhas, a conferência do Painel
continuou apontando para o endereço VELHO: `'07 Suíte'!$I$32` passou a ler o
*arredondamento de chapa* (R$ 481,21) em vez do zero da conferência. E a linha
"A PLANILHA CONTRA O MOTOR" seguia com **R$ 70.767,00 digitado à mão** na
fórmula e na frase, acusando R$ 4.914,89 de erro onde não havia erro nenhum.
⭐ **Corrigido na raiz:** a fórmula agora **PROCURA a linha pelo rótulo**
(`INDEX/MATCH("⭐ CONFERÊNCIA*")`) em vez de apontar para endereço fixo — e o
`painel.py` passou a IMPRIMIR, a cada rodada, o número que precisa ir à mão
para a G37. ⛔ Endereço fixo e número digitado envelhecem calados; os dois já
me pegaram hoje.

**⭐ E DEPOIS, NO MESMO DIA:** *"as mesas de cabeceira pode ser um item unico
no orcamento"*. Eram os itens 04 e 05; viraram **UM**, com cada peça dizendo
de qual mesa é e uma linha só por família de ferragem. ⛔ **O custo não mudou
um centavo** — R$ 75.681,91 antes e depois. Mudou a apresentação: 22 itens →
**21**, e a Suíte de 5 para **4**.
⚠ E a pergunta do pé metálico fica de pé: **juntar numa linha de orçamento não
é o mesmo que o serralheiro fazer os dois jogos numa ida só.** A primeira
coisa é apresentação; a segunda é preço. Seguem dois jogos, R$ 600.

**Hoje:** conferência interna das 7 abas **R$ 0,00** · planilha contra o motor
**−R$ 0,06** · linhas a preço zero **0** · 21 itens · 57 chapas.

**⚠ E DOIS NÚMEROS QUE O JONATHAN MEXEU NA PLANILHA ENQUANTO EU TRABALHAVA**,
que eu NÃO toquei porque são células dele:
- **MC alvo do projeto está em 50%**, não nos 35% combinados. O preço no
  Painel saiu **R$ 300.074,19** em vez dos R$ 189.551 de 35%. ⚠ E a nota ao
  lado da célula segue contando a história dos 35% — **o rótulo voltou a
  divergir do valor**, que é exatamente o que aquela nota foi escrita para
  denunciar.
- **01 Hall com 2 viagens de frete**, R$ 400. O frete do projeto passou de
  R$ 2.200 para R$ 2.600.

**⭐⭐ E AS TRÊS RESPOSTAS DO JONATHAN, no mesmo dia:**

1. *"120 esta otimo"* — a altura da cabeceira está fechada.
2. *"considere tbm o painel de mdf que esta atras"* — ⛔⛔ **ELE ESTAVA
   FALTANDO, E A PLANTA JÁ DIZIA.** A parede da cabeceira é cotada
   **200 + 267 = 467**. Os 200 são o ripado, que eu orcei. **Ninguém cota 267
   de nada** — os 267 são o outro painel, o liso, e eu li a cota como "o
   resto da parede" em vez de como um ITEM. ⭐ A cabeceira de 240 prova a
   leitura: ela pisa 86,5 cm de ripado e 153,5 cm do liso, e atravessar a
   junta entre dois acabamentos só faz sentido se os dois forem acabamento.
   ⭐⭐ E a emenda se resolve sozinha: 267 pede 2 faixas de 133,5, e a junta
   cai **debaixo da cabeceira**, com 20 cm de folga. +R$ 1.268 no projeto.
3. *"pode considerar ambas de 90cm"* — a planta desenhava 80 e 90; medir não
   é decidir, e ele decidiu. +R$ 47.

**Custo direto R$ 75.681,91 → R$ 76.996,72** · 22 itens · 59 chapas ·
conferência **R$ 0,00** · linhas a preço zero **0**.

**⚠ E O PEDIDO QUE NÃO TEM UMA RESPOSTA SÓ:** *"considere um investimento no
orcamento 20% a menos"*. ⛔⛔ **20% A MENOS DE QUÊ?** A planilha não está nos
35% combinados — a célula da MC alvo está em **50%**, posta à mão. São duas
contas completamente diferentes, e isso está medido em `economia.py`:

| leitura | preço hoje | −20% | como se chega |
|---|---|---|---|
| ① da planilha, MC 50% | R$ 305.114 | **R$ 244.091** | ⭐ a MC vai de 50% para **43,5%** · zero mudança de produto, e 8,5 pontos acima do piso |
| ② do combinado, MC 35% | R$ 193.724 | **R$ 154.979** | ⛔ por margem NÃO DÁ (pediria MC 24,7%) · tem de sair produto |

⭐ **E a alavanca que não toca no projeto: SEM VENDEDOR.** BASE sobe de
76,09% para 84,88% e o preço cai **17,6%** com a mesma MC e o mesmo móvel.
Com ripa de 3 em vez de 2 (passo 4,5), chega a **−23,5%**.
⛔ A ripa é a maior alavanca de produto do orçamento, e agora sai por
variável de ambiente: `RIPA_L=3 VAO=1.5 python3 levantamento.py`.

**⛔ E UM ERRO MEU, DE FERRAMENTA, NÃO DE CONTA:** pus um `git stash` dentro
de um script de diagnóstico "por segurança" e ele engoliu TODAS as alterações
não commitadas no meio da cirurgia da planilha. Recuperado com `git stash
pop`, nada se perdeu. ⭐ A lição: **script de leitura não escreve.** Comando
que muda estado não entra em ferramenta de diagnóstico, nem com boa intenção.

**⭐⭐ E DEPOIS, A CONDIÇÃO COMERCIAL** [Jonathan, 04/11/2026]: *"nao
considere cartao de credito, considere custo de comissao de vendedor de 5%.
parcelamento sero o mesmo proposto para o michel e o gustavo"*.

**⛔⛔ E A COMISSÃO DE 5% CORRIGE UMA CORREÇÃO MINHA.** A célula NASCEU em 5%
e eu a troquei para 10% em 03/11, apoiada na frase daquele dia — *"tem
comissão do vendedor (10%)"* — tratando os 5% como erro do modelo. **Não
eram.** As duas frases ficam registradas na planilha, com data: apagar a de
03/11 faria o próximo leitor achar que a de hoje sempre esteve ali.
⭐ **BASE 76,09% → 80,48%**, e na MC de 35% o preço cai **9,7%**, de
R$ 187.397 para **R$ 169.293**. Comissão de vendedor não sai da margem: sai
do preço, nos dois sentidos.

**⭐ O PARCELAMENTO: fui ler a PROPOSTA ENTREGUE, não o orçamento.** O que se
copia de outro cliente é a CONDIÇÃO COMERCIAL da casa, nunca o número dele.
A proposta do Gustavo Raposo traz **30% na assinatura · 20% em 30 dias · 20%
em 60 dias · 30% em 90 dias, todas por transferência bancária**, e a do
Michel traz a mesma regra de fundo, "entrada e saldo por transferência, sem
cartão".
⛔ E isso expôs uma divergência na própria skill: a tabela de formas de
pagamento do `proposta-comercial.md` é **toda baseada em cartão**, de 6× a
10× — nenhuma das quatro linhas serve. A escada real foi gravada lá.

**Preço no Painel: R$ 305.114 → R$ 261.133** (MC 50%, com frete).

**⭐⭐ E A SEGUNDA CABECEIRA DESTRAVOU — por regra, não por desenho.**
*"20 a menos que a cabeceira da suite de casal"*: a da SUÍTE 01 sai por 80%
da master. Perguntei em vez de adivinhar, porque a frase tinha três leituras
e uma delas era remover ripado de um projeto de cliente.

⛔⛔ **E ISSO INVERTE O MÉTODO DA CASA, com o dono sabendo.** No projeto
inteiro a medida vem primeiro e o preço depois. Ali não há desenho para
medir, então o dono deu o PREÇO e eu derivei a medida: **192 × 120** é o que
faz o custo cair exatamente 20% (R$ 1.735,26 contra R$ 2.169,08) a 120 de
altura, porque o custo da cabeceira é quase todo linear na largura.
⭐ Está escrito assim em toda linha onde aparece: **estimativa comercial
declarada, não cota.**

⚠ **E O AMBIENTE NOVO COMPRA CHAPA INTEIRA:** 2,61 m² de MDF 15 num ambiente
de um móvel só são UMA chapa de R$ 550 contra R$ 352,86 de rateio. Então o
**ITEM** cai os 20% pedidos, mas o **AMBIENTE** sai em R$ 2.014. A diferença
some assim que o resto da suíte 01 entrar.

**Nasceu a aba 08 Suíte 01**, e com ela a primeira aba do projeto cujo
ambiente não tem prancha — o subtítulo gerado dizia "executivo vetorizado,
11 pranchas A3" ali também, e agora ele pergunta antes de afirmar.

**Projeto: 8 ambientes · 23 itens · 60 chapas · custo direto R$ 81.611,05 ·
preço R$ 267.741,81** (MC 50%, com frete). Conferências: material R$ 0,00 ·
8 internas R$ 0,00 · contra o motor −R$ 0,06 · Preço e Comissões R$ 0,00 ·
linhas a preço zero **0**.

**⚠ E O `economia.py` NASCEU DE UM MAL-ENTENDIDO MEU.** Eu li "20% a menos"
como desconto no PROJETO, montei a análise inteira e perguntei "de quê" —
quando ele falava da cabeceira. ⭐ O arquivo fica, porque o que ele mede
segue valendo: quanto cada alavanca de preço realmente devolve, com o motor
rodando em cada cenário. ⛔ A lição está escrita no topo dele: "20% a menos"
sem sujeito tem pelo menos três leituras, e eu escolhi a mais trabalhosa
antes de perguntar.

**⭐⭐ E A ESCADA DE TRÊS LINHAS** [Jonathan, 04/11/2026]: *"35 telescopica
(basica) 38 hettich e 43 blum — lembrando que so tem alteração de valores os
itens que levam as respectivas ferragens. os demais pode manter a mc de 38%
fixo."*

⛔⛔ **A SEGUNDA FRASE É MAIS IMPORTANTE QUE A PRIMEIRA.** A MC da linha não
é a MC do projeto: vale só para os itens que carregam a ferragem que muda.
⭐ É a regra que ele mesmo cravou em 09/09/2026 — *"a cabeceira estofada deve
custar o mesmo valor para o cliente em ambos os contextos"* — e agora ela
virou **aritmética com trava**: `linhas.py` explode se um item sem corrediça
e sem sistema de correr mudar de preço entre as colunas.

| | **BÁSICA** 35% | **HETTICH** 38% | **BLUM** 43% |
|---|--:|--:|--:|
| **A CASA** | **179.785** | **185.991** | **201.353** |
| da anterior | — | +3,5% | +8,3% |

**7 itens de 23 mudam.** Os outros **16 têm preço idêntico nas três colunas**.
⭐ A básica usa a **Corrediça Hardt, R$ 80/par**, que já estava na Base — não
inventei tier nenhum.

⚠⚠ **E UM ACHADO QUE VALE DECISÃO:** as duas portas de correr ripadas têm
**custo idêntico na básica e na Hettich** (o sistema de correr custa R$ 600
nas duas, porque a Base não tem um mais barato) e mesmo assim o preço sobe
**R$ 539 cada** — três pontos de MC sem ferragem diferente nenhuma. Ou a
básica leva um sistema mais simples (e falta o preço dele na Base), ou esses
dois itens ficam em 35% também.

**Gravado em:** `referencias/quantitativo.md` (MEDIR O VETOR DA PRANCHA) ·
`referencias/laminacao-e-construcao.md` (a cabeceira e a mesa, camada a
camada) · `referencias/base-de-custos.md` (as duas chaves novas) · Base
(importada) linhas 94 e 95 · aba 07 Suíte, itens 03 a 05.

### [2026-11-04] Attos · Costa Laguna — o MÉTODO DA PORTA DE PASSAGEM — Lavinia
**Solicitante:** Jonathan · **Agente:** Lavinia · **Status:** 🟡 Aplicado, com 3 perguntas abertas

**O que o Jonathan cravou nesta sessão** (cada uma virou regra de casa, não
só número do Attos):

| decisão | palavras dele | onde foi parar |
|---|---|---|
| **A folha da porta é FEITA** | *"sanduiche com duas chapas de 6mm ... com um miolo de chapa Gdoor ... reguas de 15cm em torno da extençao"* | `referencias/laminacao-e-construcao.md`, seção PORTA DE PASSAGEM |
| **Metalon na ripada** | *"adicionais dois perfis de metalom ... a barra de 3mt custa 100,00"* | idem + `base-de-custos.md` |
| **A ripa vai à coladeira** | *"a filetagem das reguas pode considerar automatica"* + *"todo o ripado do projeto"* | `base-de-custos.md` · R$ 5,00 → R$ 2,50 |
| **Dobradiça de porta de vidro é comum** | *"as dobradiças do item 3, sao normais"* | a folha é vidro COM PERFIL: parafusa no perfil |
| **Reflecta é por m², a R$ 650** | *"é 420 o mt quadrado"* → *"atualize ... para 650 o mt²"* | `base-de-custos.md` · era lido como preço de FOLHA |

**⛔ O QUE ISSO DESFEZ:** a linha "porta pronta" não existe. Eu tinha duas
portas paradas num orçamento à espera de decisão (R$ 530 e R$ 840) porque não
sabia se a casa compra ou fabrica. Fabrica.

**⚠ TRÊS PERGUNTAS SEGUEM ABERTAS, e a primeira é a que me incomoda:**
1. ⛔⛔ **A FITA DA ARESTA DA PORTA ESTÁ ERRADA E EU SEI.** A folha fica com
   41,2 mm (29,2 de G-Door + 2 × 6) e a fita da Base é de 22. A de 45 não
   existe lá; na ripada seriam 59,2 mm e pediria 60. Lancei com a de 22 e
   gritei na aba. **Ou entra o preço da fita de 45/60, ou a aresta fecha com
   sarrafo — e isso é outra conta.**
2. As réguas de 15 do miolo: só o perímetro, ou há travessa no meio e bloco
   de fechadura? (~R$ 12 cada)
3. O metalon por barra (R$ 200) ou por metro (R$ 181,33)?

**⛔ E UMA COISA QUE EU NÃO CONSEGUI FAZER:** o Jonathan pediu o orçamento das
**duas cabeceiras estofadas e das mesas de cabeceira**, que estão no
*"Anteprojeto - Attos 2.pdf"* do Drive. **O arquivo tem 7,96 MB e não passa
pelo conector do Drive** — a leitura devolve só os rótulos das 24 páginas, sem
uma cota. ⚠ E ele revelou uma coisa maior: os 3Ds têm **SUÍTE 01, SUÍTE 02 e
SUÍTE PRINCIPAL**, e o executivo de 11 pranchas só cobre a PRINCIPAL. As duas
outras suítes não têm prancha executiva nenhuma.

**Arquivos:** `projetos/attos-costa-laguna/` (base.py, levantamento.py,
chaves.py, planilha.py, _portas.py) · planilha
`1eNEzHVhPF2HvKJ7MYGRZSkw9l-0aMMfij1ZXHMEcg0c`

---

### [2026-06-16] Novo layout de proposta — Vitor
**Solicitante:** Jonathan  
**Agente:** Vitor  
**Status:** 🔴 Pendente

**O que foi pedido:**  
Criar um novo layout/template de proposta para o Vitor — diferente dos modelos atuais
no Canva (MODELO e MODELO ENXUTO). Jonathan quer um design novo com:
- Nova linha do tempo visual
- Links para Instagram e YouTube da Valvic
- (outros detalhes a confirmar com Jonathan na próxima sessão)

**Contexto:**  
A demanda surgiu na sessão de 2026-06-16 mas foi interrompida antes de Jonathan
especificar o design completo. Retomar perguntando: "Quais seções quer no novo
layout? Referência visual? Links exatos do IG e YouTube?"

**Arquivos relacionados:**  
- Templates atuais: MODELO `DAHMsJxsuhE` · MODELO ENXUTO `DAHMsEfQNas`  
- Referência de identidade: `.claude/skills/closer-vendas/referencias/identidade-marca.md`

---

## Tarefas concluídas

*(mover aqui quando feito, com data de conclusão)*

### [2026-06-19] Orçamento + Proposta — Halls Ed. Luxemburgo — Lavinia + Vitor
**Solicitante:** Jonathan · **Status:** 🟢 Concluído

Orçamento e proposta dos halls do **Condomínio Ed. Luxemburgo** (Arq. Rosana Miraglia).
Escopo Valvic = revestimento em **MDF amadeirado** (painéis dos halls de 2 e 4 apt +
molduras de espelho no hall social). Fora: granito, gesso, portas prontas, papel,
pintura, porcelanato, rodapé poliestireno, blindex, arandelas e **madeira de demolição**.
- Fechado: **versão única Hardt** (garantia 5 anos), **sem RT**, espelhos em linha
  separada, **MC 37%**, preço **unitário** (1 hall de cada).
- Preços: 2 apt **R$ 9.070** · 4 apt **R$ 12.710** · social A+B **R$ 4.780** ·
  espelhos **R$ 8.730** · total 1-de-cada **R$ 35.295**.
- Prazo 100–120 dias úteis · pagamento 40% entrada + 30% entrega + 30% boleto 30d ·
  validade 7 dias · cliente: Condomínio Ed. Luxemburgo (Igor, 31 98814-4127).
- **Arquivos:** `projetos/2026-ed-luxemburgo-halls.md` · `orcamento-ed-luxemburgo-halls.json` ·
  `proposta-ed-luxemburgo.html`/`.pdf`. Proposta subida ao Drive (pasta do cliente).
- **Pendências:** confirmar prazo do boleto (assumido 30 dias); ver recado p/ Rodrigo.

### [2026-07-17] Orçamento + Proposta — LM / SPE Nova Lima 1 (comercial: painéis + pérgola) — Lavinia
**Solicitante:** Jonathan · **Projeto:** arq. **Lodi Motta / JBA** · **Status:** 🟢 Proposta entregue
Stand de vendas comercial (2 pranchas executivas CAD): **MOB 01** Painel Corretores/Pilar + **MOB 02** Painel/Pérgula Gourmet-Lounge.
- **Leitura do VETOR do CAD** (não OCR/olho): cotas exatas de planta/elevações. Alturas painel 2,62 m.
- **PÉRGOLA cravada:** cadeia de cotas = **28 faces de 8** → **28 ripas** de metalon #10×5 × **3,09 m** (projeção). Barra 6 m, 2×3,09>6 → **1 ripa/barra = 28 barras** × R$150 + R$150 frete dedicado = **R$ 4.350**. (Cliente já sabia que não dá 2 numa barra — bateu.)
- **Painéis Cravo Trend** parede a parede: MOB02 62,9 m² + MOB01 ~35,8 m² + porta ripada + armário ext = **107,5 m² → 25 chapas**. Móveis Moscada Matt (móvel lounge 300×60×35 + armário gourmet 97,5×248×42). MDF madeirado (pérgola+forro) 11 chapas. **39 chapas**, custo material **~R$ 34.900**.
- **Preço:** chapa Arauco Realce R$ 500 · **sem RT** · **MC 40%** → **R$ 91.300**. Pagto 40/40/20, prazo 45–60 úteis, garantia 2a. Proposta comercial config única (sem linhas de ferragem), capa tipográfica (sem render, é CAD).
- **Não inclusos:** forro gypsum (gesseiro), pontos elétr./hidr., obra civil.
- **Rev. (Jonathan revisou):** tirei **veneziana** (a "porta ripada" da Elev.2 = veneziana, terceiro) e **vidro jateado** do pilar (vidraceiro) → **R$ 91.300 → R$ 88.200**. Corretor **não é balcão** — é backdrop + **caixa em marcenaria** (nicho recuado). **Inox** = rodapé perfil inox escovado 5cm (DET.02, serralheria). ⚠️ Lição: não rotular "ripado/balcão" no olho — conferir se é veneziana/nicho; e itens escritos na prancha (vidro) podem ser terceiro/existente, sempre confirmar escopo.
- **Aprendizado:** ler cota do vetor (`get_text('words')`) é o método exato pra prancha CAD — clusterizar cadeias horizontais/verticais dá comprimento de parede e contagem de ripas sem erro. Coordenada do vetor = pt; imagem 2,2x = ×2,2.
- **Arquivos:** `2026-lm-painel-pergola.md` · `corte-lm.py` · `build-lm.py` · `proposta-lm.html/.pdf`.

### [2026-07-16] Orçamento + Proposta — Graça (despensa + lavanderia + tanque) — Lavinia
**Solicitante:** Jonathan · **Projeto:** arq. **Lais Teles** (RT 10% líq.) · **Status:** 🟢 Proposta entregue
3 ambientes, 4 conjuntos de marcenaria, **projeto 100% MDF Azul Petróleo Guararapes** (25 pranchas, "Detalhamento").
- **CÁLCULO peça-a-peça** (`corte-graca.py`, 57 peças) → **9 chapas R$ 4.000**. Despensa = armário superior **revestido** (existente) + bancada em L (2 gavetões, nichos, **3 cestos aramados**, LED 3000 K). Lavanderia = torre da máq. de lavar (puxador cava passante). Tanque = balcão 2 portas. **Tampos (bancada despensa + tanque) = pedra/marmorista, fora.**
- **Preço (motor COM cartão, RT 10%):** **Essencial (telescópica/2a, MC 32%) R$ 20.100** · **Essencial Prime (oculta alemã Hardt/5a, MC 37%) R$ 24.000.** Alocação: Despensa 64,4% · Lavanderia 29,1% · Tanque 6,5%.
- **Rev. 16/07 (tarde) — ajustes do Jonathan:** (1) **100% Azul** (nada de Branco TX na caixaria); (2) **tampo é pedra** (fora); (3) **nesting unificado** (tudo uma cor → pilhas somadas), efeito **11→9 chapas** (unificar cor −1, tampo pedra −1); (4) **2ª linha +5% de MC** (32→37%) → gap ~R$ 3.900. ⚠️ Essencial a 32% abaixo do piso do Rodrigo (exceção 37%) — decisão do Jonathan.
- **Layout:** 1ª versão ficou "pesada" (blocos sólidos empilhados) → refeita **leve/editorial** (fios finos, tinta petróleo suave na Prime, pill "Recomendada"). **Bug pego:** `min-height:297mm` no WeasyPrint não enche a folha → rodapé `absolute` colava no conteúdo; corrigido com **`height:297mm`**.
- **Aprendizado:** projeto de cor única otimiza chapa (sem pilha Branca vs cor com sobra separada). Diferenciação por modelo/garantia, não por marca (regra da casa). **Pagto:** escala padrão. **Prazo 60–90 dias.** Proposta **enxuta (3 págs)**.
- **Flags:** nº de folhas do armário existente · larg. bancada 136 vs 154 (adotado 154) · puxador despensa/tanque.
- **Arquivos:** `2026-graca-marcenaria.md` · `orcamento-graca.json` · `corte-graca.py` · `build-graca.py` · `proposta-graca.html/.pdf` · `img-graca-*.png`.

### [2026-07-16] Orçamento + Proposta — Resolve Consórcio (comercial, 14 amb.) — Lavinia + Vitor
**Solicitante:** Jonathan · **Parceira:** Jéssica Sollero (RT 10%) · **Eng.:** Corsino Soares · **Status:** 🟢 Proposta entregue
Escritório corporativo completo (14 ambientes, 54 pranchas) — recepção, salas, convivência, coffe point, refeitório,
jurídico, compliance, **63 lockers**, comercial, CEO, CALL + **7 cabines**. **Refeito do zero** (v1/v2 estimativas erradas).
- **CÁLCULO peça-a-peça** (`corte-resolve-consorcio.py`, 257 peças) → **79 chapas R$ 29.770** (v1 estimava 106, v2 49 — as duas erradas).
  **Ripado = produto Eucatex RU Freijó Brasil** (0,75 m²/cx, R$ 166,50/cx, ref. web). Material Valvic ~R$ 61k (Hardt).
- **Preço (motor sem cartão, RT 10%):** **Essencial (Hardt/5a/MC35%) R$ 147.800** · **Essencial Prime (Hettich/10a/MC38%) R$ 174.800.**
  Alocação por ambiente **proporcional ao material** (lockers 16,9%). Pagto **40/40/20**, prazo **90–100 dias corridos**.
- **Escopo:** inclui estofado dos bancos + pés metálicos + escorredor cromado. **FORA:** blindex, espuma acústica, fechaduras dos lockers.
- **Lição cravada na skill:** *CALCULAR, nunca ESTIMAR* (princípio nº 1). ⚠️ MC 35/38% abaixo do piso 40% do Rodrigo p/ >R$80k — decisão do Jonathan.
- **Arquivos:** `2026-resolve-consorcio-marcenaria.md` · `orcamento-resolve-consorcio.json` · `corte-resolve-consorcio.py` · `proposta-resolve-consorcio.html/.pdf`.

### [2026-07-14] Orçamento + Proposta — Jairo Samuel (apto completo) — Lavinia + Vitor
**Solicitante:** Jonathan · **Parceira:** Jéssica Sollero (RT 10%) · **Status:** 🟢 Proposta entregue (v002)
Marcenaria completa do apto (projeto Jéssica Sollero, 27 pranchas). **9 móveis MDF:** cristaleira (Sala,
Carvalho Hanover) · cozinha completa (superiores Cinza Cristal Chess + inferiores Lord + prateleiras) ·
cabeceira + roupeiro (Hóspede, Beige Matt) · roupeiro + painel/prateleiras + mesa (Suíte, Lord).
- **2 linhas pela ferragem, nomeadas pelo MODELO Valvic** (a pedido — sem citar marca):
  **"Essencial"** (Hardt · 5 anos · MC **32%** · **R$ 70.400**) · **"Essencial Prime"** (Hettich Sensys+Quadro ·
  10 anos · MC **35%** · **R$ 83.900**). Premium evidencia **engenharia alemã** (ciclagem 100k, ajuste 3D) e garantia superior.
  (nomes v1 "Assinatura/Assinatura Alemã" trocados por Essencial/Essencial Prime a pedido do Jonathan.)
- **Quantitativo com PLANO DE CORTE** (premissa nova da skill) → ~34 chapas · fita+filetagem · ~64 dobr. + 16 corr.
  ocultas · LED 9 m · terceirizados (vidros cristaleira + espelho + estofado cabeceira) · **insumos** (cola, parafusos,
  limpeza/embalagem) não esquecidos. Cliente **criterioso** → proposta puxa acabamento, garantia, pós-venda e a
  **parceria de anos com a Jéssica**. Prazo **60–70 dias úteis**.
- 🚫 **DIVISÓRIA de TV (Metalon + cachepots) FORA** (confirmado cliente) · toda serralheria/marmoraria fora do escopo
  (por fornecedor parceiro) — só a marcenaria MDF entrou.
- **Margens:** v001 era 37/42% (R$81k/105k); revistas p/ **32/35%** a pedido do Jonathan.
- **Arquivos:** `projetos/2026-jairo-samuel-marcenaria.md` · `orcamento-jairo-samuel.json` · `proposta-jairo-samuel.html`/`.pdf`.
- **Pendências:** ① confirmar coordenação da **serralheria** (Valvic gerencia ou fica com o serralheiro?) · ② **ripado dos
  banhos** sem cota · ③ cota "113" da cristaleira não fecha (conferir DWG p/ porta de vidro) · ④ prof. do roupeiro da suíte
  (adotei 55) · ⑤ refinar quantitativo no app após **medição no local** · ⑥ subir a proposta ao Drive (pasta do cliente).

### [2026-06-25] Orçamento + Proposta — Camila (Closet) — Lavinia + Vitor · rev. 10/07
**Solicitante:** Jonathan · **Status:** 🟢 Concluído
Closet = **Roupeiro em L (piso-teto) + Ilha**. Fechou em **config única** (evoluiu de 2
versões — correr ripado × básculas — que foram descartadas). **R$ 24.900** ·
RT **10%** embutido · ferragem **Hardt** → garantia 5 anos.
- **Roupeiro** (piso-teto, 2 cores cinza + Cumaru **USINADO**, não ripado): 3 portas de
  correr **RO-65 piso-teto** (trilho 3 m + desempenadores) + 2 portas menores (43 cm) de
  **giro** (dobradiças Hardt). Gavetas em corrediça oculta Hardt + puxador SP7000. LED +
  sensor. **Eliminados:** módulo superior, báscula/Multi, tábua de passar.
- **Ilha (rev. 10/07):** agora **marcenaria** — **estrutura com 4 gavetas** (corrediça oculta
  Hardt + puxador Enlevo), **base SEM serralheria**. Saiu a serralheria da base e o tampo de
  vidro. **R$ 4.200** (era R$ 6.800). Repreço a pedido do Jonathan.
- **Alocação:** Roupeiro **R$ 20.700** · Ilha **R$ 4.200** → **total R$ 24.900**.
- **Pagamento (rev. 10/07):** condição única **50% entrada + 50% na entrega** (transferência)
  com **8% de desconto → R$ 22.908**. (Saíram as opções de cartão/parcelamento.)
- **Arquivos:** `orcamento-camila-v3-mc32.json`, `orcamento-camila-closet.html/.pdf`,
  `proposta-camila.html/.pdf` (proposta de config única, **atualizada 10/07**).
- **Drive (pasta "Camila"):** Docs **ATUAL** (proposta + orçamento interno v3). ⚠️ Subir a
  proposta rev. 10/07 no lugar. Há **2 Docs antigos** (das versões 2-cenários) a **apagar**
  pelo Jonathan — o Drive MCP não deleta.
- **Pendências:** ① atualizar o **orçamento interno v3** (linha da ilha ainda com serralheria/vidro
  → recalcular MC com o novo custo da ilha em marcenaria); ② confirmar prazo (usei 60–70 dias
  úteis); ③ trocar render da capa por foto real.

### [2026-06-27] Orçamento + Proposta — Raquel (Roupeiro Branco TX) — Lavinia + Vitor
**Solicitante:** Jonathan · **Status:** 🟢 Concluído
Roupeiro piso-teto de **6,30 m**, todo em **MDF Branco TX 15 mm**, **portas de giro** com
puxador **Liveri IL955 192 mm** (Italy Line), interior completo (cabideiros, prateleiras e
**até 25 gavetas/sapateiras deslizantes** — puxadores espaçados, sem cava). **Sem LED.**
- **Duas linhas de ferragem** (mesma estrutura/portas): **Premium** (corrediça oculta Hardt
  + dobradiça Hardt → 5 anos) **R$ 30.000** (MC **35,2%** — ÂNCORA) × **Essencial**
  (telescópica + dobradiça padrão → 2 anos) **R$ 25.000** (MC **30%**). RT 0. Gap = R$ 5.000.
- **Arquivos:** `orcamento-roupeiro-branco-tx.json` (v003), `proposta-roupeiro-branco-tx.html/.pdf`.
- **Proposta:** 5 páginas, 2 opções lado a lado · prazo **60 dias corridos** · validade
  **30/06/2026**. Drive: pasta **"Raquel"** criada + **Doc nativo** da proposta; PDF visual no chat.
- **Pendências:** confirmar custo de compra do **Liveri IL955** (usei R$ 40/un); confirmar
  nº de chapas na **elevação das portas** (~14 portas de giro; ±2-3 chapas no nesting).

---

## Painel de orçamentos (dashboard)

### [2026-07-16] Painel fixo de orçamentos — Lavinia
**Artifact (link fixo):** https://claude.ai/code/artifact/19b63c82-17d8-4b8c-a5b7-b95c63abb71d
**Fonte no repo:** `painel-orcamentos.html` (raiz) = **versão COMPACTA/widget** (o que está publicado — feito p/ ficar
fixo no painel lateral: hero de valor total, ticket, nº fechados, lista enxuta + status dot). A **versão detalhada**
(KPIs + gráfico de barras + tabela completa) está preservada em `painel-orcamentos-detalhado.html`.
- **Dados:** array `ORCAMENTOS` no `<script>` (KPIs recalculam sozinhos ao adicionar item). Também `PARADOS`.
  Atualizar `DATA_ATUALIZADA` a cada mudança. `dp` = pendências Drive (conta ausente+desatualizado).
- **Como atualizar:** editar `painel-orcamentos.html`, e republicar com a ferramenta Artifact **passando
  `url:` = o link acima** (senão cria um artifact novo). Na mesma conversa que publicou, basta republicar o mesmo caminho.
- Regra: **preencher o painel a cada orçamento que a Lavinia finaliza.**

## Aprendizados

### [2026-06-19] Método e ferramentas (projeto Luxemburgo) — Lavinia/Vitor
- **Medir revestimento por PIXEL nas elevações 1:20.** Isolar a cor do MDF amadeirado
  na imagem e converter px→m² (fator linear = 2,54/dpi × escala; área = fator²).
  Ótimo p/ revestimento de parede sem cotas item-a-item; conferir contra 1 cálculo
  manual. (Halls: ~10,2 m² no 2 apt; ~14 m² no 4 apt.)
- **Escopo de hall de arquitetura:** separar SEMPRE a marcenaria (MDF amadeirado) do
  resto (granito, gesso/sanca, portas prontas, papel, pintura, porcelanato, rodapé
  poliestireno, blindex, arandelas). **Madeira de demolição = maciça → fora** quando
  o cliente pede "sem maciça".
- **Condomínio:** orçar por HALL (unitário) × nº de pavimentos; hall social é único (A+B).
- **Ferragem muda preço E garantia:** Hardt = 5 anos (dobradiça ~R$8) · Hettich Sensys
  = 10 anos (~R$35). Trocar ferragem → reprecificar e reajustar a garantia. Upsell de
  garantia = subir p/ Hettich (+R$264 no 2 apt, +R$393 no 4 apt).
- **Proposta HTML→PDF (weasyprint) — armadilhas:** (1) NÃO renderiza `background`
  multi-camada nem `var()` dentro de gradiente → o painel "some". Usar **divs sólidos**
  (slats) p/ o painel amadeirado/frisos; gradiente ÚNICO funciona (usei no LED).
  (2) `min-height:297mm` + página cheia estoura p/ uma página extra — deixar folga.
- **Canva:** brand-template **autofill exige plano pago** (bloqueado nesta conta).
  Fallback oficial = **HTML→PDF** (precedente K&F). A API do Canva **não adiciona/remove
  linhas de tabela** — limita reaproveitar os masters p/ nº de itens diferente.

### [2026-06-25] Proposta — clareza para o cliente (Vitor) — regra do Jonathan
- **Quanto mais conta o cliente tem que fazer sozinho, pior; quanto mais claro,
  organizado e objetivo, melhor.** Na proposta, mostrar SEMPRE o total que o cliente
  paga, pronto — nada de "some o roupeiro + a ilha". Cada cenário/opção já traz o
  conjunto COMPLETO num total único + o valor à vista.
- **Comparativo de versões na proposta:** quando há duas formas de executar (ex. módulo
  superior em correr ripado × báscula — closet da Camila), apresentar as duas como
  CENÁRIOS COMPLETOS lado a lado (roupeiro + ilha em cada), com a economia explícita —
  não só o item que muda.

### [2026-06-27] Ancoragem de preço por MC, não só por custo (Vitor/Lavinia) — Raquel
- **Diferenciar as versões pela MARGEM, não apenas pelo custo da ferragem.** No roupeiro da
  Raquel as duas linhas usam a mesma estrutura; a Premium custa só **+R$ 880** de ferragem
  (oculta Hardt vs telescópica). Precificada na mesma MC, o gap fica pequeno (~R$ 1.800).
  Subindo a **Premium para 35% de MC** (× Essencial 30%), o gap vira **R$ 5.000** — âncora
  forte que faz a Essencial parecer o "negócio certo".
- **Usar números redondos como âncora** (R$ 30.000 × R$ 25.000): mais memorável e o salto de
  qualidade (telescópica/2 anos → oculta Hardt/5 anos) fica nítido. Fechar o investimento na
  MC alvo e arredondar pra cima (motor confirma a MC realizada — Premium 35,2%).

---

## Aprendizados (Lavinia)

### [2026-06-30] Orçar por render — 2 regras
1. **Item arquitetônico ambíguo** (forro/revestimento de madeira, painéis colados na parede) →
   **PERGUNTAR antes de incluir**, nunca assumir que é marcenaria nossa. (Erro no orç. Juliana:
   inventei "aparador ripado curvo" e "divisória curva" que eram revestimento / vinham de outro projeto.)
2. **Isolar renders por cliente/data** antes de ler — misturar pastas gera **móveis fantasma**
   (renders da Kênia & Fábio contaminaram a leitura da Juliana).
3. **Nunca orçar por m²** — sempre plano de corte (peça a peça por cor×espessura). Diretriz do Jonathan.

### [2026-06-30] Orçamento Juliana (Kairon & Juliana) — em proposta
4 ambientes (Cozinha, Área serviço, Lavabo, Sala). Anteprojeto Caio Oliveira. Caixa normal, sem RT, vend 3%.
**Gold R$ 55.800 (MC 42%) · Essencial R$ 49.200 (MC 37%).** Registro: `projetos/2026-kairon-juliana.md`.
Falta: definir pagamento/validade e montar a proposta 2 linhas.

### ⛔⛔ [2026-09-02] FALHA GRAVÍSSIMA — descrever na proposta o que não foi orçado

**Jonathan, sobre o orçamento da Juliana:** *"Ponto crítico: você não orçou a
laca da cômoda mas descreveu na proposta. Registre esse erro como falha
gravíssima. Nunca mais podemos errar isso. O custo desse erro é gigante."*

A proposta v2 da Juliana diz **"cômoda em laca vermelha com tampo de vidro"**.
O orçamento lançou **MDF Vermelho melamínico** e `laq = R$ 0` em todos os 8
ambientes, nas duas linhas. Laca é MDF **cru** + pintura em cabine a R$ 650/m²;
melamínico já vem revestido. Não são o mesmo produto.

**Por que o custo é gigante:** a proposta é o contrato. Assinada, a Valvic deve
uma cômoda lacada e tem no orçamento uma melamínica. Ou come o prejuízo
(R$ 1.500–2.000 só nesta peça), ou entrega diferente do escrito, ou renegocia
depois de assinado — a pior das três. Numa casa com laca em vários ambientes,
escala para dezenas de milhares.

**A regra, registrada em `referencias/validacao-orcamento.md`:** toda palavra de
acabamento, ferragem ou material escrita na proposta tem de ter linha
correspondente no orçamento. **Se está no texto, tem de estar na conta.** Há
uma tabela de palavras-gatilho lá — laca, espelho, vidro, estofado, marca de
ferragem, LED, inox, serralheria, pedra, ripado — e o auditor de cada
`build-*.py` passa a falhar quando uma delas aparecer no PDF sem a linha no
motor.

É o gêmeo da regra de 17/08 sobre montagem: lá o risco era **tirar da proposta**
algo que a casa entrega; aqui é **colocar na proposta** algo que a casa não
orçou. Mesma origem — texto e conta escritos em momentos diferentes, sem
ninguém cruzar os dois no fim.

### [2026-10-29] Orçamento + Caderno de proposta — Jéssica e Michell / ICA — Lavinia
**Solicitante:** Jonathan · **Projeto:** **IARA CEZAR Arquitetura e Interiores**, Lagoa Santa/MG · **Status:** 🟢 Caderno entregue, com pendências nomeadas

O maior job já orçado pela casa: **executivo de 235 páginas A3 · 20 ambientes · 19 levantados**.
Entregue em **dois cenários de ferragem**, com caderno A4 deitado de **35 folhas** e PDF.

**Os números.** Custo direto **R$ 311.541,90** (Blum) e **R$ 297.795,90** (Hettich).
Fechado em **MC 55% Blum → R$ 1.042.818,08** e **MC 52% Hettich → R$ 905.843,04**.
Lucro do período (90 dias, custo fixo lido ao vivo da Gestão 3): **R$ 223.096,84** e
**R$ 120.585,28**. A margem Blum paga **147 dias** de empresa com uma obra de 90.
Pagamento **30 / 20 / 20 / 30** (assinatura, 30, 60 e 90 dias), por transferência.

**O que este projeto ensinou — está registrado, não aqui:**
- `referencias/ferragens.md` — como **contar** ferragem de marca pelo motor (errei duas
  vezes antes de acertar), a **razão Hettich/Blum de 0,70–0,72** apurada no mercado, os
  ciclos de ensaio das duas marcas, e duas correções técnicas: **articulador é de molas,
  não a gás** e **gaveta não leva pulsador**.
- `referencias/proposta-comercial.md` — **a LEI DA VOZ**: nem "sob nossa coordenação",
  que entrega que não executamos, nem "a nossa serralheria", que seria mentira. Mais o
  **refrão é tempero** (no máximo 3 ambientes), a folha de ambiente **sem medida, sem
  marca e sem preço**, a ordem **valor antes de valores**, e a mecânica do caderno.
- `referencias/estrutura-orcamento.md` — ⛔ **PEDRA NÃO É ESCOPO DA VALVIC.**
- `closer-vendas/referencias/garantia.md` — **Blum 30 anos, Hettich 10**, decisão do
  Jonathan, com a ressalva de que o termo de 30 anos ainda não existe em papel.
- `referencias/planilha-google.md` — o **Painel por rótulo**, a auditoria de fórmula
  morta com `FORMULATEXT`, `IMPORTRANGE` por coluna inteira, e o truque da linha única.
- `projetos/ica-michell/README.md` — a leitura do executivo de 111 MB, os **renders em
  1760 × 1328 nas folhas de FOTO**, e as duas rodadas de correção.
- **Planilha do cliente, Painel, bloco AS REGRAS DA CASA:** entraram as regras **13 a 17**
  (pedra fora, frete como linha do ambiente, como contar ferragem, articulador de molas,
  garantia escalonada).

**Arquivos:** `projetos/build-caderno-ica.py` (o caderno) · `build-previa-ica.py` (a prévia) ·
`projetos/ica-michell/` (motor, 19 módulos, `wf.json` e `wf2.json` com a apuração e o texto) ·
planilha `10G12W-0rZUu4c0hAdXmuz-ClgeUluR5vIuTU7pjqLOw`.

⚠ **Vale para o Vitor:** o caderno do ICA é, na prática, o **novo layout premium de
proposta** que está aberto como tarefa desde 16/06. Vale olhar antes de começar do zero.

---

## Recados rápidos

*(notas passageiras — podem ser apagadas após lidas)*

### [2026-06-16] Rodrigo → Lavinia
**CAIXA CRÍTICO.** Piso de exceção: 37%. Ideal: 43%+.
Projetos grandes (>R$ 80k): mínimo 40%, ENTRADA de 40% antes de iniciar produção.
Não fechar nenhum projeto sem entrada real. H2 está zerado — cada venda conta.

### [2026-06-16] Rodrigo → Vitor
**Pipeline H2/2026 zerado — emergência comercial.**
Prioridade 1: fechar Kênia & Fábio (casa completa, MC ≥ 40%, entrada 40%).
Prioridade 2: reativar orçamentos parados nos últimos 90 dias.
Sem margem para desconto de preço. Sem desconto = sem negociação de preço.
Cobrar Andre Alphaville (R$ 70.800 em aberto) e Marcelo e Simony (R$ 34.850).

### [2026-06-19] Vitor → Rodrigo / Jonathan
Luxemburgo fechou a **MC 37%** (seu piso de exceção do caixa crítico) com **entrada de
40%** — atende sua regra de entrada. ⚠️ **Atenção:** o preço é por hall; se o total do
prédio passar de **R$ 80k** (vários pavimentos), sua regra pede **MC mínima 40%**.
Avaliar subir a margem no fechamento do prédio inteiro ou manter 37% como exceção.

### [2026-10-29] Lavinia → Jonathan · ICA, o que trava a impressão
Três coisas, em ordem de risco:

1. ⛔ **O termo de garantia de 30 anos não existe em papel.** `garantia.md` registra que
   só o de 10 anos está desenhado. A folha 30 do caderno promete 30 anos no cenário Blum
   e a arquiteta vai pedir o documento.
2. ⛔ **Serralheria, espelho e vidro estão a R$ 0,00** em sete ambientes. O caderno diz
   que tudo sai no mesmo contrato — a frase é verdadeira, mas o **preço não a cobre**.
   Ou cotamos, ou esses itens vão nomeados na folha "o que não está nesta proposta".
   Pela regra dos dois estados: ou é nosso com valor, ou está escrito como fora.
3. ⚠ **Cozinha e Closet master estão com desenho axonométrico, não render.** As folhas
   de foto do executivo pesam 6,8 e 7,4 MB e não passam pelo Drive. Duas imagens no chat
   resolvem em cinco minutos.

⚠ Menor, mas fica: o **Lavabo** é o 20º ambiente do executivo e não foi levantado. O
caderno foi montado com **19** e o Lavabo está nomeado como escopo à parte.

### [2026-10-29] Jonathan → todos os agentes · A FRONTEIRA DO ESCOPO, DEFINITIVA
> *"grave DEFINITIVAMENTE NA SKILL: pedra nao é escopo da marcenaria.
> espelhos, vidros e serralheria que estiverem na marcenaria é nosso."*

⛔ **PEDRA NUNCA.** Granito, quartzito, mármore, silestone — bancada, sóculo,
frontão, tampo, soleira, peitoril. Fora do custo e fora da proposta, e não se
lança a linha nem a zero. Vai nomeada em "o que não está nesta proposta".
⚠ O executivo desenhar a pedra junto do armário não a torna nossa.

⭐ **ESPELHO, VIDRO E SERRALHERIA, SIM — quando fazem parte do móvel.** Espelho
de porta de roupeiro, vidro de cristaleira, estrado de cama, alma de aço, haste
de prateleira, quadro de leito. ⛔ Box, janela, guarda-corpo, portão, grade,
pergolado e escada metálica, não.

⭐ **O teste:** sai no mesmo caminhão e é instalado pela mesma equipe? É nosso.
Existe sem o móvel? Não é.

**Gravado em:** `orcamentista-marcenaria/SKILL.md` (bloco próprio e regra 19) ·
`referencias/regras-de-quantitativo.md` · `referencias/estrutura-orcamento.md` ·
Base de Custos, aba Instruções · Painel do ICA, regra 13.
