# SPE NOVA LIMA 1 — stand de vendas e apartamento decorado

Projeto arq. **Lodi Motta**. Motor do decorado: `corte-spe-decorado.py` ·
proposta: `build-spe-nova-lima.py` → `proposta-spe-nova-lima.pdf`.

| Data | | |
|---|---|--:|
| 17/07/2026 | 1ª proposta, só o stand | 88.200 |
| 07/08/2026 | + decorado (4 ambientes), MC 35% | 189.400 |
| 21/08/2026 | + copa (DET 07) e ilha gourmet (DET 02) | 204.000 |
| **10/09/2026** | **fechamento com ferragem rebaixada** | **168.000** |

---

## Rodada de 10/09 — fechamento em R$ 168.000

> *"Vamos retornar ao orçamento do SPE Nova Lima 1 e fechar um valor de
> investimento de 168k. Descreva dobradiças Hettich Novisys, corrediças
> telescópicas sem amortecimento, articuladores simples, sistema de roupeiro
> RO65 Rometal. Não fale sobre quantitativo de material nem metragem de nada.
> Não precisa desmembrar os ambientes também não, apenas cite todos."*

### A proposta mudou de forma

| | antes | agora |
|---|---|---|
| Investimento | tabela com **10 frentes** e valor em cada | **um número só** |
| Descritivo | com cotas, m², contagem de ripas e portas | **sem uma medida sequer** |
| Ferragem | citada de passagem no meio do escopo | **página própria**, item por item |
| Páginas | 4 | **3** |

Auditei o PDF por regex atrás de cota, m², contagem de peça: **nenhuma sobrou.**
O escopo continua completo — o que saiu foi a régua, não o móvel.

### ⚠ A garantia caiu de 5 para 2 anos

`ferragens.md`: *"a Linha Silver troca corrediças ocultas por telescópicas
(garantia 2 anos nas corrediças)"*. Os 5 anos da versão anterior estavam
ancorados justamente na **corrediça oculta**. Com telescópica sem amortecimento
não dá para sustentá-los. A proposta agora diz **2 anos**, e a página da
ferragem explica de onde vem: *"é a linha que define a garantia de 2 anos desta
proposta"*.

### ⚠⚠ O que os R$ 36.000 de corte são

O rebaixamento de ferragem vale, de custo direto:

| | de | para | economia |
|---|---|---|--:|
| Corrediças (7 pares) | Oculta Hardt R$ 70 | Telescópica R$ 40 | 210 |
| Articuladores (8 un) | R$ 150 | ★ simples R$ 60 | 720 |
| Roupeiros (2 kits) | Dominus R$ 1.840/kit | RO65 4 portas + 2 trilhos | 3.280 |
| Dobradiças | **já eram Novisys** | sem mudança | 0 |
| | | | **R$ 4.210** |

Custo direto do contrato: **R$ 87.403 → R$ 83.193**.

| Preço | MC |
|---|--:|
| R$ 204.000 (com a ferragem nova) | 39,2% |
| **R$ 194.300** — mantém os 37,2% combinados de antes | 37,2% |
| R$ 184.800 — piso de 35% da casa | 35,0% |
| **R$ 168.000** ← fechado | **30,5%** |

**A ferragem justifica cair para R$ 194.300. Os outros R$ 26.300 são margem
entregue.** A MC de 30,5% fica **abaixo do piso de 35%** e no fundo da faixa
"Normal" da tabela de caixa. É decisão de preço do Jonathan, não consequência
técnica — fica registrado.

### ⚠ RO65 em roupeiro

`validacao-orcamento.md` registra a correção inversa: *"SS150 é sistema de
roupeiro: folha pesada, 65 cm de profundidade. Porta de espelho num armário de
banheiro de 15 cm não é o mesmo produto"* — ou seja, RO65 estava catalogado
como o sistema do armário **raso**, e o roupeiro pedia SS150/Dominus. Aqui as
folhas são **espelhadas em esquadria de alumínio**, que é o caso pesado.
**Conferir com a Rometal se o RO65 sustenta essa folha** antes de assinar.

### Em aberto

1. **A MC de 30,5%** — abaixo do piso, por decisão de preço.
2. **RO65 no roupeiro espelhado** — conferir carga com a Rometal.
3. **★ Articulador simples a R$ 60** — adoção minha; a base só tem Blum HK-xs
   (R$ 250) e Aventos (R$ 600), e o motor usava R$ 150 sem referência.
4. O motor `corte-spe-decorado.py` **não foi rodado de novo** com a ferragem
   nova: o preço agora é cravado, então o motor só serve de referência de custo.
   Se o escopo mudar, rodar antes.

### 2º ajuste de 10/09 — interno em Branco TX e LED do cliente

> *"Informe que o interno dos armários será em MDF Branco TX. Que os LEDs serão
> fornecidos pelo cliente."*

**Interno.** A nota de acabamentos dizia "caixaria interna em branco", vago.
Agora diz com todas as letras: **"O interno de todos os armários é MDF Branco
TX — caixaria, prateleiras, fundos e caixas de gaveta."**

**LED.** Saiu do escopo Valvic. Três lugares mudaram:

| Onde | Antes | Agora |
|---|---|---|
| Acabamentos | "espelhos, laca, estofados e **iluminação em LED** coordenados pela Valvic e entregues instalados" | o LED sai da lista |
| Puxadores e iluminação | "iluminação em fita de LED com perfil de alumínio, embutida na própria peça" | "**a iluminação em LED é fornecida pelo cliente** — fita, perfil e drivers. A Valvic entrega os nichos, a sanca e o cortineiro com o **rasgo e o embutimento usinados, prontos para receber a fita**" |
| Não inclusos | — | abre com **"Iluminação em LED — fita, perfil e drivers, fornecidos pelo cliente"** |

⛔ **E onde o descritivo prometia luz, passou a prometer o preparo.** "Sanca
iluminada" virou "sanca preparada para iluminação"; "módulo de nichos
iluminados" e "torre de nichos iluminados" viraram "preparado para iluminação".
Móvel que promete luz sem entregar a fita é a falha de 02/09 outra vez, agora
pelo lado do que sai do escopo. Auditei o PDF: **nenhum "iluminado" sobrou.**

### O que o LED faz com a margem

| | custo direto | MC em R$ 168.000 |
|---|--:|--:|
| escopo original | 87.403 | 28,0% |
| − rebaixamento de ferragem (R$ 4.210) | 83.193 | 30,5% |
| **− LED do decorado (16,7 m × R$ 130 = R$ 2.171)** | **81.022** | **31,8%** |

A MC sobe **1,3 ponto** e o número do cliente não muda. Segue abaixo do piso de
35% — para chegar lá o preço seria R$ 180.000, e para manter os 37,2%
combinados de antes, R$ 189.200.

⚠ A **sanca do pilar do stand** também perde o LED, mas o stand está com preço
travado desde 17/07 e o custo dele não está aberto neste motor — a economia real
é um pouco maior que os R$ 2.171.
