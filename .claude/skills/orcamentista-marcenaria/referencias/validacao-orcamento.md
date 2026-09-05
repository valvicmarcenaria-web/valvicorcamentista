# Validação de orçamento — base real da Valvic (planilha atual)

> **Esta é a base de orçamento que a Valvic usa hoje** — a planilha
> `fontes/validacao_de_orcamentos.xlsx` ("Validação de orçamentos"). É a
> **fonte de verdade dos custos e percentuais atuais**. O app Valvic OS
> (ver `custos.md`/`estrutura-orcamento.md`) é o sistema em construção que
> formaliza esta lógica.

Cada aba = um projeto/ambiente orçado (cliente, projeto, versão). Exemplos na
planilha: roupeiros, cristaleiras, painéis, cozinhas, closets, escritórios.

## Modelo de validação

```
Investimento R$        = preço de venda ao cliente
Custo total R$         = Operacional + Terceirizados + Venda + Material + Margem de erro
MC R$                  = Investimento − Custo total
MC %                   = MC / Investimento          → IDEAL 35–40%
```

A planilha valida o orçamento **de trás para frente**: dado um Investimento
(preço), soma-se todo o custo e verifica-se se a MC% cai na faixa ideal.

### Blocos do custo (todos abatem da MC)

**1. Custo operacional**
- Comissão produção · Logística (carretos/materiais · uber · equipe) ·
  Alimentação · Hora extra · Desgaste de serra/fresa · Manutenção de máquinas.

**2. Terceirizados**
- Vidraceiro · Serralheiro · Pintor · Estofador · Laqueamento · Montagem.

**3. Custos de venda**
- Comissão vendedor · RT · Nota fiscal · Visitas · Impressão ·
  Parcelamento máquina · Brindes · Projeto.

**4. Custo material** (ver catálogo abaixo).

**5. Margem de erro** — contingência.

## Percentuais reais (sobre o Investimento) — padrão atualizado 06/2026

> Padrão revisado pelo fundador em 06/2026 (projeto Samara). Mudou: NF 7→**5%**,
> comissão produção ~5→**7,2%** (marceneiro 5%), e **vendedor = 0 quando o lead vem
> de parceiro**.

| Encargo                  | % do Investimento        | Observação                         |
|--------------------------|--------------------------|------------------------------------|
| Nota fiscal              | **5%** (era 7%)          | padrão atual 06/2026               |
| Parcelamento de máquina  | **7%** (às vezes 8%)     | taxa da maquininha/cartão; vira desconto à vista |
| Comissão vendedor        | **5%** · **0** c/ parceiro | quem "vende" é a RT do parceiro  |
| Comissão produção        | **~7,2%**                | prog 0,8 + coord 1 + **marc 5** + serra 0,2 + manut 0,2 |
| RT (parceiro/arquiteto)  | **10% do líquido** (≈8,8% do bruto) | 0 quando não há parceiro; ver `proposta-comercial.md` |
| Margem de erro           | **2%**                   |                                    |
| Visitas                  | **R$ 250** (fixo)        | valor por visita                   |

> **Meta de margem:** MC% entre **35% e 40%** é o ideal. Abaixo disso, revisar
> preço ou enxugar custos; isso difere do markup bruto do app (CX 52–68%),
> que é *antes* dos encargos.

## Fórmula de preço (markup divisor) — validada

> Atalho para chegar ao **preço** a partir do **custo direto** e da **MC alvo**,
> sem ir e voltar no app. Validado contra projetos reais (Camila, Samara 06/2026).

Componentes do encargo (padrão 06/2026), **% sobre o investimento**:

| Bloco | % do inv |
|-------|---------:|
| NF | 5% |
| Parcelamento de máquina | 7% |
| Comissão vendedor | 5% (**0** c/ parceiro) |
| Comissão produção (prog 0,8 + coord 1 + **marc 5** + serra 0,2 + manut 0,2) | 7,2% |
| Margem de erro | 2% |
| RT 10% do líquido (líquido = inv − NF − cartão ≈ 0,88·inv) | ≈ 8,8% do bruto (0 sem parceiro) |

**Dois cenários** (definem o divisor):

| Cenário | Vendedor | RT | Encargos | Divisor |
|---------|:-------:|:--:|:--------:|:-------:|
| **Venda direta** (sem parceiro) | 5% | 0 | **26,2%** | `0,738 − MC%` |
| **Lead de parceiro** (decorador/arquiteto) | 0 | 8,8% | **30,0%** | `0,70 − MC%` |

```
preço (inv) = (custo_material_direto + visita) / (divisor − MC%)
```

- Ex. parceiro: material R$ 10.866 + visita 250, MC 40% → inv = 11.116 / (0,70 − 0,40)
  = **R$ 37.055** (Samara/Luana 06/2026).
- **Atenção:** estimar encargos "no olho" subprecifica MC — usar o divisor do
  cenário certo. (Aprendizado Samara: R$40,6k "a 40%" com encargo errado dava 38,8%.)

## Subestimar custo = preço travado = MARGEM VIRA PREJUÍZO

> Lição cara (clínica Dermato-Nutro 06/2026). O preço é **travado com o cliente**; se o
> levantamento subestima o custo, **o erro sai inteiro da MC** — a empresa financia a obra.

Os encargos (~30%) são **% do preço** (fixos). Quem absorve um custo direto maior é só a
MC. Exemplo real (custo direto subestimado em R$ 8.740, real ~R$ 14.300):

| Preço enviado | Custo real | MC real | vs alvo 42% |
|---|---:|:---:|---|
| R$ 32.500 (errado) | R$ 14.300 | **25,3%** | −17 pts · ~R$ 14 mil de MC perdida |
| R$ 52.900 (correto) | R$ 14.300 | 42,6% | ✅ |

**Regra:** isto **não** quer dizer "na dúvida erra o custo pra cima" — padding é muleta
(encarece e perde venda, ou esconde levantamento mal feito). **Lidamos com matemática: dá
para medir.** Na dúvida, **pergunta, alinha e aprende a fazer certo** — e **mede** (cotas
do projeto, ou **escalímetro** usando a medida de um móvel conhecido como referência para
achar portas/paredes). Conferir omissões clássicas antes de fechar: painel com portas (3
partes), curva (+15%/+5%), sistemas de porta, terceirizados, fita de ripado.

## Situação de caixa — perguntar em TODA nova demanda

> **Antes de fechar o preço, perguntar ao Jonathan como está o caixa.** Com caixa
> baixo aceita-se uma MC menor para gerar fluxo; com caixa folgado, segura-se a
> margem. A MC mínima aceitável muda conforme a situação.

| Situação        | MC          | Leitura                                   |
|-----------------|-------------|-------------------------------------------|
| **Crítico**     | até **25%** | só para gerar caixa urgente               |
| **Ruim**        | até **30%** | aperta, mas passa                         |
| **Normal**      | **30–37%**  | faixa de trabalho saudável                |
| **Bom**         | **37–45%**  | margem confortável                        |
| **Ótimo**       | **acima de 45%** | excelente                            |

> No projeto da Camila o Jonathan fechou com MC propositalmente menor (caixa
> baixo, precisando de recursos). Variável embutida no app `validacao-orcamento.html`
> (seletor "Situação de caixa" + sinalização de piso na MC).

## Custo FIXO vs VARIÁVEL — o que entra (e o que NÃO entra) no orçamento

> **Conceito-chave.** O orçamento contém **apenas custos variáveis** (incidem
> por projeto). A **produção é custo FIXO** e **NÃO entra no orçamento**.

- **Variáveis (entram no orçamento):** material e insumos; **comissões**
  (vendedor, produção, programador, coordenador, marceneiro/montador); corte de
  chapa; NF; RT; logística (carreto + equipe); máquina/parcelamento; embalagem;
  visitas/setup; margem de erro.
- **Fixos (NÃO entram no orçamento):** **salários de toda a equipe** (7
  profissionais — marceneiros, montadores, etc.), galpão ~500 m², máquinas
  (CNC, coladeira automática), administrativo. A produção é **fixa, não por
  demanda**.

**Margem de Contribuição (MC) = Preço − Custos Variáveis.** A soma das MCs de
todos os projetos é o que **cobre os custos fixos e gera o lucro**. Por isso a
meta de **MC 35–40%** é crítica: com a estrutura fixa que cresceu (sócio,
galpão, CNC, coladeira, 7 fixos), a MC precisa ser robusta o bastante para
pagar tudo isso e ainda manter caixa saudável.

> ⚠ Cuidado para **não confundir**: o marceneiro tem **salário (fixo, fora do
> orçamento)** e pode ter **comissão (variável, dentro do orçamento)**. Só a
> comissão entra na cotação.

## Catálogo de material — preços de compra reais (R$ unitário)

Organizado como na planilha. Onde há faixa, são valores vistos em projetos
diferentes (variam por linha/fornecedor).

### MDF e chapas (R$/chapa)
| Item                          | R$ unit. |
|-------------------------------|----------|
| mdf branco 6                  | 190 (200)|
| mdf branco 15                 | 230 (250)|
| mdf branco 15 Ultra           | 320      |
| mdf branco 18                 | 290      |
| mdf branco 25                 | 420      |
| mdf cor 6                     | 250 (300)|
| mdf cor 15                    | 500      |
| mdf cor 18                    | 580      |
| mdf especial 6                | 800      |
| mdf especial 15               | 950      |
| mdf especial 18               | 1200     |
| mdf com lâmina prensada +acab.| 2200     |
| Palha sintética               | 600      |
| Compensado flexível           | 400      |

> "branco / cor / especial" classifica o melamínico por linha de preço, e a
> espessura (6/15/18/25) define o uso (fundos / estrutura / tampos).

### Cola e fita
Cola **80** · Fita de borda **100** (por rolo).

### Ferragens
| Item                       | R$ unit.            |
|----------------------------|---------------------|
| Dobradiças                 | 10 (9–12)           |
| Dobradiças especiais       | 30                  |
| Corrediças telescópicas    | 30 /par             |
| Corrediças                 | 100 (25–350) /par   |
| Rodízio                    | 8 (30)              |
| Articuladores              | 150                 |
| Sistema roupeiro           | 250                 |
| Sistema porta passagem     | 150                 |
| Puxadores                  | 40 (25–200)         |
| Puxador cava               | 30–80               |
| Puxador topo de porta      | 80                  |
| Portas de vidro            | 850 (600–1000)      |
| Desempenador de portas     | 60                  |
| Sistema RO82 + trilho      | 700                 |
| Cabideiros                 | 150 (100)           |
| Suporte de prateleira      | 12                  |
| Prateleira de vidro        | 35                  |

### Parafusos, dispositivos e montagem
Parafusos **25** · Conj. parafuso e bucha **1,8** (2,5) · Sup. prateleiras
**1,5** · Sist. montagem (mini fix etc.) **0,8** · kit Teck bond **35** ·
PUR/PU **50** · Silicone acabamento **30**.

### Iluminação
Led – Fita + perfil (metro linear) **130** (100) · Sensor **50** (150).

### Diversos
Metalom **80** · Vidros **30** · Escorredor **500** · Material de pintura
**300** · Palinha **600**.

### Limpeza / embalagem
Tinner (litro) **12** · Estopa (pacote) **10** · Strech **4** · Cantoneira
**0,5** · Embalagem **50**.

### Material informacional
Etiqueta **20** · Impressão externa **1,5** · Impressão interna **1,0**.

---

> Cada item de material tem **Quant × R$ unit. = R$ total**. O quantitativo
> (a coluna Quant) é justamente a metodologia que vamos destilar com os
> projetos resolvidos: como se chega ao nº de chapas e às quantidades de
> ferragem a partir das peças.

---

## Unidades: quatro linhas em que a casa cobra numa unidade e eu cobrei noutra
### [Eliuton 17/08/2026 — depois de "os valores ficaram altos demais"]

> **Antes de multiplicar, olhar a UNIDADE da linha.** `materiais.json` e
> `chapas.md` não usam sempre a mesma, e há linhas com duas origens e dois
> preços. Quando houver conflito, vale a que já foi usada num job real.

| Item | Errado | Certo | Por quê |
|---|---|---|---|
| **Cava usinada** | R$ 50 **por peça** (`materiais.json`) | **R$ 25 por metro** linear (Honda 07/08) | A CNC cobra tempo de percurso, e percurso é metro. Uma frente de 20 cm e uma de 1,45 m não custam o mesmo. |
| **Espelho e vidro** | R$ 600/m² (`materiais.json`) | **R$ 285 por folha** com perfil (`chapas.md`) | Já estava escrito como armadilha e caí nela mesmo assim. |
| **LED** | R$ 150/m ("LED COB fita + perfil") | **R$ 66/m** = fita 28 + perfil de alumínio 38 (`chapas.md`) | A decomposta é rastreável; a agregada não diz que perfil é. |
| **Sistema de correr** | SS150 R$ 500–600 + trilho | **RO65 Rometal R$ 60/porta + trilho R$ 60** | SS150 é sistema de **roupeiro**: folha pesada, 65 cm de profundidade. Porta de espelho num armário de banheiro de **15 cm** não é o mesmo produto. |

Somadas, essas quatro linhas valiam **R$ 4.237 de custo** e ~R$ 9.850 de preço
num job de R$ 118.800 — 8% do orçamento em erro de unidade.

---

## ⛔ MONTAGEM NÃO ENTRA NA PROPOSTA [Jonathan 17/08/2026]

> **"Nunca consideramos montagem na proposta."** — Jonathan, 17/08.
> Já estava escrito nesta mesma página, na lista de custos fixos. Eu lancei
> assim mesmo, duas vezes: 22 dias de dupla e depois 13. **A linha não existe.**

**Por quê.** Montador e marceneiro são **salário fixo** — a estrutura da Valvic
tem 7 profissionais que recebem todo mês, com ou sem obra. A produção é fixa,
não por demanda. O que é variável e entra no orçamento é a **comissão**, e a
comissão **já está dentro do motor**, nos coeficientes `a = 0,162` e
`liqF·b = 0,0378`.

Lançar dia de montador como custo direto conta a mesma mão de obra **duas
vezes**: uma no salário que a empresa paga de qualquer jeito, outra na comissão
que o divisor já cobra. E ainda infla o preço, porque o custo direto passa pelo
divisor.

### O que fica na logística
| Entra | Não entra |
|---|---|
| **Carreto** (frete do móvel até a obra) | Dia de montador |
| **Visita técnica** (~R$ 250 cada) | Dia de marceneiro |
| Embalagem | Qualquer "instalação" em dias |
| Terceirizado de verdade: serralheiro, vidraceiro, marmorista, laqueador | |

No Eliuton isso derrubou R$ 13.200 de custo direto — de R$ 17.200 de "logística
e instalação" sobraram **R$ 3.150** de 4 carretos e 3 visitas.

### ⚠ Rever a Honda
`corte-honda-minas-motos.py` tem `INSTAL = 1800.0` ("3 dias de dupla") dentro do
custo direto. Pela regra, não deveria estar lá. Consequência para um job **já
entregue a R$ 19.100**: o custo direto real é R$ 6.799, não R$ 8.599, e a
**MC foi 44,4%, não os 35% que a proposta declarou**. O job é mais lucrativo do
que está registrado. Não mexi no arquivo entregue — fica a nota para o Jonathan
decidir se corrige o histórico.

### O teste
Se uma linha do custo direto tem a palavra **dia**, **hora**, **equipe**,
**montagem** ou **instalação** e o serviço é feito por gente da casa, ela está
errada. Só entra o que a Valvic **compra de terceiro** ou **paga por evento**.

### ⚠ Não confundir CUSTO com ESCOPO [Jonathan 17/08]
Montagem **não entra no custo** — e **entra no escopo**. São duas coisas
diferentes e é fácil derrubar a segunda junto com a primeira.

| | Custo (planilha) | Escopo (proposta) |
|---|---|---|
| Instalação e montagem | **não entra** — equipe é salário fixo | **entra, e é diferencial**: "instalação e montagem por equipe própria da Valvic; não terceirizamos a montagem" |

A Valvic **não terceiriza a montagem**, e isso é argumento de venda: quem
instala é quem produziu. Toda proposta tem de dizer isso na lista do que está
dentro do valor. Tirar a linha da planilha e esquecer de escrever no papel é
entregar de graça um diferencial que a concorrência não tem.

---

# ⛔⛔ FALHA GRAVÍSSIMA — DESCREVER NA PROPOSTA O QUE NÃO FOI ORÇADO

**[Jonathan 02/09/2026, sobre o orçamento da Juliana]**

> *"Ponto crítico: você não orçou a laca da cômoda mas descreveu na proposta.
> Registre esse erro como falha gravíssima. Nunca mais podemos errar isso.
> O custo desse erro é gigante."*

## O que aconteceu

A proposta v2 da Juliana descreve, com todas as letras:

> *"cômoda em **laca vermelha** com tampo de vidro"*

E o orçamento lançou:

| O que a proposta promete | O que o orçamento pagou |
|---|---|
| Cômoda em **laca vermelha** | **MDF Vermelho melamínico** — 2 chapas de 15 mm + 1 de 6 mm = R$ 1.300 |
| — | `terc.laq` = **R$ 0** em **todos** os 8 ambientes, nas **duas** linhas |

**Laca e melamínico não são o mesmo produto.** Laca é MDF **cru** + pintura em
cabine, a R$ 650/m² de peça lisa na base da casa. Melamínico já vem revestido de
fábrica. A conta correta da cômoda troca a chapa (cor → cru) e **soma a laca**.

## Por que o custo do erro é gigante

O erro não é a diferença de preço. É que **a proposta é o contrato**. Assinada,
a Valvic deve uma cômoda lacada e tem no orçamento uma cômoda melamínica. As
saídas são todas ruins:

1. **Executar laca e comer o prejuízo** — sai do bolso, e numa cômoda de porte
   médio é da ordem de **R$ 1.500 a 2.000** só nesta peça.
2. **Executar melamínico** — entrega diferente do que foi escrito. É quebra de
   contrato e destrói a confiança, que custa muito mais que a laca.
3. **Renegociar depois de assinado** — a pior das três: o cliente já decidiu com
   base num número, e a casa aparece pedindo mais.

E é um erro que **escala silenciosamente**: se acontecer numa casa inteira com
laca em vários ambientes, são dezenas de milhares.

## ⛔ A REGRA — o auditor de TODA proposta passa a checar isso

> **Toda palavra de acabamento, ferragem ou material escrita na proposta tem de
> ter uma linha correspondente no orçamento. Se está no texto, tem de estar na
> conta. Se não está na conta, não pode estar no texto.**

Palavras que **obrigam** linha no orçamento — nunca escrever sem conferir:

| Palavra na proposta | Linha que TEM de existir |
|---|---|
| **laca**, lacado, pintado, laqueado | `Laca / Pintura` R$ 650/m² **e** chapa em **MDF cru**, não melamínico |
| **espelho**, espelhado | `Espelho prata/bronze` por m² |
| **vidro**, cristaleira, reflecta | `Vidro`/`Porta de vidro` por m² ou folha |
| **estofado**, capitonê | `Estofado (terceiro)` |
| marca de ferragem (**Blum**, Hettich, Hardt, Rometal, Häfele) | a linha daquela marca, não a genérica |
| **LED**, iluminação, fita | `LED fita + perfil` por metro **e** driver/sensor |
| **inox**, alumínio, latão, dourado | o perfil ou o puxador daquele acabamento |
| **serralheria**, estrutura metálica | `Estrutura de serralheria` |
| **mármore**, granito, pedra | ou está fora do escopo **e a proposta diz isso** |
| **ripado**, cava usinada, meia esquadria | usinagem por metro |

### Como conferir, na prática

O caminho que pegou este erro é o certo e passa a ser obrigatório:
**ler a descrição da proposta palavra por palavra contra a lista de materiais do
orçamento** — não contra a memória do que foi levantado. O auditor de cada
`build-*.py` tem de falhar quando uma dessas palavras aparecer no PDF sem a
linha correspondente no motor.

> Este é o gêmeo da regra de 17/08 sobre montagem: lá o risco era **tirar da
> proposta** algo que a casa entrega. Aqui é **colocar na proposta** algo que a
> casa não orçou. Os dois erros nascem do mesmo lugar — texto e conta escritos
> em momentos diferentes, sem ninguém cruzar os dois no fim.
