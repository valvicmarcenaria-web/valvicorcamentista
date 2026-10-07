# Proposta comercial — formato de saída ao cliente

Como a Valvic apresenta o orçamento ao cliente (referência:
`fontes/exemplo_proposta_lucas_e_ana_v2.pdf`). O quantitativo/custo interno
(planilha) vira uma proposta institucional com preço **por ambiente** em
**duas linhas: Gold e Silver**.

## ⛔ REGRAS DO QUE **NÃO** VAI NA PROPOSTA

Três coisas que o Jonathan já teve de pedir mais de uma vez. Se aparecerem numa
proposta, é erro — não é questão de gosto.

> ### ⚠️ ESCOPO DESTAS REGRAS: SÓ O TEXTO DA PROPOSTA
> [Jonathan 24/08]
>
> As três valem **exclusivamente para o que é escrito no documento que vai ao
> cliente**. Elas **não** tocam no método de trabalho.
>
> **O LEVANTAMENTO DE CUSTO CONTINUA COTADO AO MILÍMETRO.** Ler cada prancha,
> transcrever cada cota, lançar peça a peça, conferir se cabe na chapa, rodar o
> nesting por cor × espessura — nada disso muda. É de lá que sai o número.
>
> Se algum dia a leitura destas regras deixar o **levantamento** menos preciso,
> a regra foi mal lida. O que se esconde é a **cota na descrição de venda**,
> não a cota no motor.
>
> | Onde | Medida |
> |---|---|
> | `corte-*.py`, plano de corte, quadro de peças | **obrigatória, exata** |
> | dossiê do projeto (`projetos/*.md`) | **obrigatória** — é o registro técnico |
> | memorial de produção, ordem de corte, contrato | **obrigatória** |
> | **descrição de item na proposta ao cliente** | **⛔ nunca** |

### 1 · NUNCA cotar medida de móvel **na descrição da proposta**
[Jonathan 21/08 e 24/08 — pedido **duas vezes**]

Nada de `2,60 m`, `340 × 90`, `920 × 400 × 2450`, `prof. 65`, `altura 2,45 m`.
Nem no título do item, nem na descrição, nem entre parênteses.

**Isto é uma regra de REDAÇÃO.** O levantamento que gerou o preço usou todas
essas cotas, uma a uma — e tem de continuar usando. O que muda é só a forma de
**contar ao cliente** o que ele vai receber.

**Por quê.** Medida na proposta convida o cliente a conferir régua na parede
antes de a gente medir — e a prancha quase sempre manda "conferir em obra". Cota
divergente vira objeção antes da venda e discussão depois dela. Medida é
documento **técnico**, de produção, não de venda.

| Em vez de | Escreva |
|---|---|
| "Buffet suspenso 443,5 × 80 × 45 prof — seis gavetões" | "Buffet suspenso com seis gavetões" |
| "Armário de 2,60 m com quatro portas" | "Armário com quatro portas e gaveteiro central" |
| "Nicho contínuo de 1,77 m em MDF de 25 mm" | "Nicho contínuo, sem divisória, em MDF encorpado" |
| "Painel de 6,57 m sobre estrutura niveladora" | "Painel do piso ao forro sobre estrutura niveladora" |

O que **pode** ficar: o **material**, a **ferragem**, o **acabamento**, a
**função** e o **diferencial construtivo**. Onde a dimensão for o próprio
argumento de venda ("do piso ao forro", "parede inteira", "sem emenda
aparente"), diga isso **em palavras**, não em número.

Onde as medidas VÃO, e onde são obrigatórias: **motor de levantamento**
(`corte-*.py`), **plano de corte**, **quadro de peças**, **dossiê do projeto**,
**memorial de produção**, **ordem de corte** e **contrato de execução**.

### 2 · NUNCA explicar a formação do preço
[Jonathan 24/08]

Nada de nesting, aproveitamento de chapa, "acrescenta duas chapas ao plano de
corte", "cor nenhuma divide chapa com outra", custo de material, MC ou rateio.

**Por quê.** Explicar por que algo custa o que custa é abrir a planilha para
negociação. O cliente não compra chapa: compra o móvel pronto. Justificar preço
por dentro convida a discutir por dentro — e transforma um diferencial em
"então dá para tirar isso e baixar".

**Fale só de BENEFÍCIO.** O que ele ganha, vê, sente e usa.

| Em vez de | Escreva |
|---|---|
| "São duas chapas a mais no plano de corte" | "O armário fica inteiro na mesma cor, por dentro e por fora" |
| "O interior deixa de dividir chapa branca" | "Abrir a porta deixa de mostrar branco" |
| "Cor nenhuma divide chapa com outra" | *(nada — apagar a frase)* |

### 3 · Imagens do projeto entram na composição
[Jonathan 21/08 e 24/08]

Sempre que a pasta do cliente tiver perspectiva, render ou apresentação, as
imagens **do projeto dele** entram no layout. Proposta premium é conduzida por
imagem (ver `projetos/build-vinicius-premium.py` e o padrão do caderno do
Junior/Lagoa Santa).

⚠ **Imagem de referência estética fornecida pelo cliente** (as que as pranchas
rotulam assim) **não** serve: é inspiração de terceiro, não é o projeto dele, e
usar na nossa proposta é risco de direito de imagem. Só render ou perspectiva do
projeto em questão.

Se a pasta não tiver render acessível, **peça** — não entregue proposta premium
sem imagem alegando que não deu.

---

## Estrutura da proposta

1. **Capa** — "Proposta especial para [Cliente]".
2. **Apresentação institucional** — diferenciais, materiais premium.
3. **Configuração técnica dos móveis** — padrão de ferragens, espessuras e
   acabamentos (ver `ferragens.md` e `chapas.md`).
4. **Cases** — 3 projetos de destaque (storytelling de complexidade técnica).
5. **Linha do tempo do projeto** — Análise técnica → Apresentação → Contrato e
   financeiro → Produção e controle de qualidade → Entrega/montagem/pós-venda.
6. **Tabela de preços por ambiente** — colunas **Linha Gold** e **Linha Silver**.
7. **Totais, garantia, prazo, validade e formas de pagamento.**

## Tabela de preços por ambiente

Cada linha = um móvel/ambiente: `Serviço | Descrição técnica | Gold R$ | Silver R$`.
A descrição cita material (linha de melamínico), ferragens e acabamentos.
A coluna Silver pode ficar vazia quando o item não admite versão econômica
(ex.: por carga de peso, "não recomendo mudar").

## Linha Gold vs Linha Silver

| Aspecto      | Linha Gold                          | Linha Silver                         |
|--------------|-------------------------------------|--------------------------------------|
| Corrediças   | Ocultas, slow motion                | Telescópicas                         |
| Garantia     | 10 anos                             | 10 anos / **2 anos** nas corrediças  |
| Preço        | Cheio                               | ~6–7% menor                          |

Exemplo Lucas e Ana: **Gold R$ 181.800** · **Silver R$ 169.950**.

## Garantia (Linha Gold) — `fontes/valvic_garantia_comercial.pdf`

Cobertura **por componente**, documentada e assinada na entrega:

| Componente                        | Garantia              |
|-----------------------------------|-----------------------|
| Estrutura & Ferragens             | **10 anos**           |
| Lâmina natural                    | 10 anos* (restrições sol/calor) |
| Fechaduras & regulagens           | 2 anos                |
| Laca & pinturas / Estofados       | Vistoria assinada na entrega |

Atendimento: **24h** para retorno · **3 dias úteis** para visita técnica ·
custo zero ao cliente dentro do prazo. Marcas: Hardt, Häfele, Hettich, Rometal.

## Prazo e condições

- **Entrega:** 45 a 60 dias úteis (projeto completo).
- **Validade da proposta:** 2 dias úteis.

## Formas de pagamento

| Condição                                              | Desconto |
|-------------------------------------------------------|----------|
| Entrada 30% à vista + restante em até 10× no cartão   | —        |
| Entrada 50% à vista + restante em até 8× no cartão    | 3%       |
| Entrada 70% à vista + restante em até 6× no cartão    | 5%       |
| Entrada 70% à vista + restante via transferência      | 7%       |

> O custo do parcelamento no cartão (≈7–8%) é o mesmo "Parcelamento de máquina"
> da planilha de validação — por isso o pagamento via transferência ganha 7%
> de desconto (a Valvic devolve a taxa que economiza).

## Parceria com arquitetos/decoradores — RT

`fontes/valvic_parceria_rt_arquitetos.pdf` — Programa de Parceria Profissional
(Política de Responsabilidade Técnica).

- **RT = 10% sobre o valor líquido do projeto.**
- **Líquido** = valor bruto do contrato − custos de NF (~7,5%) − taxa
  financeira (se cartão).
- Exemplo: contrato R$100k à vista → NF −R$7.500 → **RT ≈ R$9.250**.
- A RT já entra **de forma transparente na proposta** e é **repassada
  conforme cronograma** acordado.
- Fluxo da parceria: Briefing → Proposta (com RT) → Produção (CNC próprio) →
  Entrega (montagem conjunta) → Repasse.

> Na planilha, "RT" aparece como ~7–8% do investimento (= 10% do líquido após
> deduções) e zero quando não há parceiro indicando o projeto.

---

## ⛔ GARANTIA — números corrigidos pelo Jonathan [07/08/2026]

A tabela "Linha Gold vs Linha Silver" acima traz **10 anos / 10 anos com 2 nas
corrediças**. **Não é o que a Valvic pratica.** Os números reais, por linha de
corrediça:

| Corrediça | Garantia |
|---|---|
| **Telescópica** | **2 anos**, geral |
| **Oculta Hardt** | **5 anos** |

> **E não abrir por componente na proposta.** O Jonathan pediu o número, não a
> composição: *"não precisa entrar em detalhes da garantia"*. Escrever a abertura
> (estrutura X, ferragem Y, corrediça Z) cria compromissos que a gente não emite —
> o mesmo motivo pelo qual a garantia vitalícia da Sensys saiu das propostas
> (ver `ferragens.md`).

Aplicado em `build-cozinha-elena-v4.py`. As propostas anteriores que imprimiram
**10 anos** estão desatualizadas nesse ponto.


---

## ⛔⛔ Se está no TEXTO, tem de estar na CONTA [Jonathan 02/09/2026]

Regra completa em `validacao-orcamento.md`, seção **FALHA GRAVÍSSIMA**. O
resumo, porque é aqui que o erro nasce:

> A proposta da Juliana descreveu *"cômoda em **laca vermelha**"* e o orçamento
> pagou **melamínico vermelho**, com `laq = R$ 0`. A proposta é o contrato:
> assinada, a casa deve a laca e não tem o dinheiro dela na conta.

**Antes de fechar qualquer proposta**, ler a descrição de cada item **palavra
por palavra** contra a lista de materiais do motor — não contra a memória do
levantamento. Palavras que obrigam linha no orçamento: **laca · espelho · vidro
· estofado · marca de ferragem · LED · inox/dourado · serralheria · pedra ·
ripado · cava usinada**.


---

# ⛔⛔ NUNCA PÔR METRAGEM NEM QUANTITATIVO NA PROPOSTA

**[Jonathan 12/09/2026]** *"Não precisa ficar colocando metragem de nada na
proposta. Eu já pedi isso pra você várias vezes, mas você está esquecendo.
Então grave essa regra na skill."*

Ele pediu no SPE Nova Lima (10/09) — *"não fale sobre quantitativo de material
nem metragem de nada"* — e eu tratei como decisão daquele job. **Não era.
É regra da casa, vale para toda proposta.**

## A regra

> **A proposta descreve o MÓVEL e o BENEFÍCIO. Nunca a medida, nunca a
> quantidade.** Sai tudo: cota em metro e centímetro, m², contagem de portas,
> gavetas, prateleiras, ripas, chapas, metros de fita, metros de LED, número de
> dobradiças, corrediças ou pistões.

| ⛔ Não escrever | ✅ Escrever |
|---|---|
| "Cabeceira estofada de 3,10 × 1,10 m" | "Cabeceira estofada em tecido Bouclé" |
| "Painel de 3,975 × 1,00 m" | "Painel de TV com iluminação nas bordas" |
| "vassoureiro de 2,50 m com três prateleiras" | "vassoureiro do piso ao teto, com vassoureiro deslizante" |
| "armário inferior de 4,30 m com quatro gavetas" | "armário inferior com gavetões, gavetas e porta de temperos" |
| "roupeiro de 1,54 m com duas portas de correr" | "roupeiro com portas de correr espelhadas" |
| "6 m de LED com sensor" | "iluminação em LED embutida, com sensor" |
| "28 ripas em perfil metálico" | "pérgola em perfil metálico revestido em MDF" |

## Por quê

1. **Medida é levantamento, não venda.** O cliente não compra metro quadrado,
   compra o móvel pronto. Cota na proposta convida a comparar preço por metro
   com quem orça por metro — e a casa não orça assim.
2. **Cota vira contrato.** "3,10 m" escrito numa proposta é uma medida que a
   obra pode desmentir. A proposta já diz que a medida é conferida no local
   antes do corte; escrever a cota briga com a própria cláusula.
3. **Quantitativo expõe a conta.** Número de dobradiças e metros de fita é
   informação de custo, não de benefício — e abre flanco para negociar item.

## O que PODE ficar

- O **material e o acabamento**: MDF Carvalho, Grafito Chess, Branco TX no
  interno, vidro temperado, espelho prata, Bouclé.
- A **ferragem por marca e linha**: Hettich Sensys, corrediça telescópica,
  Dominus, RO65.
- A **função**: gavetão, báscula, porta de temperos, nicho ventilado, cava
  usinada, meia esquadria, LED embutido.
- **Prazo, garantia, condição de pagamento e o preço.**
- Especificação técnica de durabilidade (ciclos de uma dobradiça, norma) — não
  é metragem do móvel.

> **O auditor de proposta passa a rodar isto:** regex atrás de
> `\d+[.,]?\d*\s*(m|cm|mm|m²)` e de contagem de peça no PDF final.
> **Qualquer ocorrência é erro.**

---

## ⛔⛔ O AUDITOR DE TRANSBORDO NÃO VÊ O QUE FOI CORTADO [30/09/2026]

No Marcelo Tolentino a **escada de pagamento inteira sumiu da proposta** e o
auditor de transbordo disse **"ok"**. A página tinha estourado, o
`overflow:hidden` da `.page` cortou o bloco, e o auditor — que mede a posição
do último bloco **que renderizou** — não tinha o que medir.

**Medir o que saiu não prova que saiu tudo.** O auditor de posição só pega
conteúdo que vazou *visivelmente* para cima do rodapé. Conteúdo que a página
engoliu é invisível para ele.

### O auditor certo compara HTML → PDF

```python
def norm(t):
    t = unicodedata.normalize('NFKD', t)
    return re.sub(r'[^0-9a-zA-Z%]', '', t).lower()   # tira espaço e acento

pdf = norm(texto_extraido_do_pdf)
txt = html.unescape(re.sub(r'<[^>]+>', ' ', html_do_corpo))
perdidos = [f for f in re.split(r'[.·—\n]', txt)
            if len(f.strip()) >= 25 and norm(f) not in pdf]
assert not perdidos
```

⚠ **A normalização tem de tirar o espaço todo**, não só colapsar. O PDF quebra
linha no meio da frase e insere `\n` onde o HTML não tem nada — comparar com
`\s+ → ' '` dá dezenas de falsos positivos.

**Os três auditores rodam juntos em toda proposta, nesta ordem:**

| | o que pega |
|---|---|
| 1 · conteúdo perdido (HTML → PDF) | bloco que a página engoliu |
| 2 · transbordo (posição **e rodapé ausente**) | bloco que invadiu o rodapé |
| 3 · metragem e quantitativo | o que não pode estar escrito |

### ⛔⛔ A causa raiz, achada em 30/09: `flex-shrink` + `overflow:hidden`

`.pad` é **coluna flex**. Uma caixa filha com `overflow:hidden` e
`flex-shrink` no padrão (1) **encolhe** quando a coluna estoura — e o
conteúdo que sobra é cortado **sem empurrar nada para baixo**. O rodapé fica
no lugar, o auditor de posição mede "folga 27 pt" e responde ok.

> **Toda caixa de conteúdo fechado — escada de pagamento, tabela de
> condições, cartões de linha — leva `flex:none`.** Assim o estouro vira
> transbordo visível, que o auditor 2 pega, em vez de sumiço silencioso.

```css
.escP{ ...; overflow:hidden; flex:none; }
```

Sem isso a escada de pagamento sumiu **quatro vezes** na mesma proposta.

### ⛔ Numeração de item NÃO é contagem de peça [01/10/2026]

O auditor 3 usava `\s*` entre o número e o substantivo, e `\s` come a quebra
de linha. No United SP a numeração de item ("03" numa linha, "Prateleiras
suspensas" na seguinte) virou `03 prateleiras` no texto extraído e foi
acusada como quantitativo.

> O número e o substantivo têm de estar **na mesma linha**: `[\t ]*`, nunca
> `\s*`. E, já que se mexe nele, a lista de substantivos cresce — faltavam
> `painel`, `fechamento` e `suporte`. **Estreitar o falso positivo é motivo
> para apertar o regex, nunca para afrouxá-lo.**

```python
(r'\b\d{1,2}[\t ]*(portas?|gavetas?|prateleiras?|nichos?|módulos?|'
 r'ripas?|dobradiças?|corrediças?|folhas?|peças?|chapas?|pulsadores?|'
 r'painéis|paineis|painel|fechamentos?|suportes?)\b', 'contagem'),
```

### ⛔ E rodapé ausente É transbordo

O auditor 2 usava o rodapé como régua e caía em `pg.rect.y1` quando não o
achava. Só que **o rodapé some justamente quando a página estoura** — foi o
que aconteceu na página do estande do Marcelo Tolentino, com duas linhas de
texto escritas por cima de onde o rodapé deveria estar, e o auditor
respondendo "folga 28 pt".

```python
fb = [b for b in bl if 'valvicmarcenaria' in norm(b[4])]
if not fb and pagina > 1:            # a capa não tem rodapé
    print('⛔ RODAPÉ PERDIDO — a página estourou')
foot_y = max([b[1] for b in fb] or [pg.rect.y1])   # ⛔ max, nunca min
ult    = max(b[3] for b in bl if b[1] < foot_y - 1)
```

#### ⛔ E `min()` pega o CABEÇALHO, não o rodapé

Na folha única do Douglas a marca aparece **duas vezes**: no cabeçalho
(y = 51,7) e no rodapé (y = 820,7). O `min()` escolheu o cabeçalho e o
auditor anunciou *"último bloco 0.0 · rodapé 51.7 · folga 51.7 pt"* — um
número sem significado, numa página que naquele momento **estava mesmo
estourando** e só foi pega pelo passe 1.

A régua é a ocorrência **mais baixa** da marca, e o conteúdo é só o que está
acima dela. Enquanto todo layout tinha a marca apenas no rodapé, `min()` e
`max()` davam o mesmo resultado e o erro ficou latente — apareceu no dia em
que um layout novo pôs a marca no topo.

⭐ A lição não é sobre `min`: **toda régua que se procura por conteúdo pode
achar o pedaço errado.** Quando o passe 2 der um número estranho, é o passe 2
que está errado, não a página.

#### ⛔⛔ E `i > 1` NUNCA dispara em documento de UMA página

No mesmo dia, a folha do pórtico **perdeu o rodapé inteiro** e os três passes
disseram "tudo ok". Duas falhas somadas:

* O passe 2 só avisava `if not fb and i > 1`, porque a **capa** não tem
  rodapé. Só que numa folha única `i` é sempre 1 — justamente o caso em que
  a página 1 **tem** rodapé. O guarda calava o único alarme que importava.
* O passe 1 não pegou porque procurava **presença**, e "Valvic Marcenaria"
  sobreviveu no cabeçalho.

Os dois consertos são o mesmo conserto: **contar, não procurar.**

```python
quer_foot = html.count('class="foot"')    # quantos o HTML manda imprimir
tem_foot  = 0
for i, pg in enumerate(doc, 1):
    fb = [b for b in bl if 'valvicmarcenaria' in norm(b[4])
          and b[1] > pg.rect.y1*0.80]     # só o terço de baixo é rodapé
    tem_foot += 1 if fb else 0
if tem_foot < quer_foot:
    print('⛔ RODAPÉ PERDIDO — alguma página estourou')
```

E no passe 1, `Counter` em vez de `in`:

```python
quer = Counter(norm(f) for f in frags)
if npdf.count(n) < quer[n]:               # 2× no HTML e 1× no PDF = perdeu
    perdidos.append(f)
```

⭐ **Presença não é contagem.** Todo trecho que o layout repete — marca,
data, nome do cliente — some sem alarme enquanto o auditor só perguntar
"está aí?".

⭐ O auditor **saiu do `/tmp`**: mora em `ferramentas/auditor-proposta.py`.
Três vezes ele foi reescrito de memória depois que o container reiniciou.

### Exceções autorizadas à regra de metragem

| medida | quando | por quê |
|---|---|---|
| `15 mm` · `18 mm` | 30/09 | espessura de chapa — separa as duas linhas |
| `2,73 m` | 01/10 | altura do pano ripado do hall (United) |
| `50 mm` | 07/10 | largura da régua do ripado (pórtico) |

⭐ O critério não é o tamanho do número: é **especificação × quantitativo**.
O passo do ripado — régua de 50, vão de 15 — **é o produto**: sem ele o
cliente não sabe o que está comprando, do mesmo jeito que não saberia sem a
espessura. Já "quantos metros de ripado" é quantitativo e continua proibido.

---

## ⛔ COLISÃO DE CLASSE COM O `css-proposta.css` — a segunda vez

`css-proposta.css` já define `.inv`, `.pay`, `.esc` e `.cnd`, e o `.inv td`
dele força `text-align:right`. Redefinir essas classes no build **não
sobrescreve** — o navegador soma as duas regras e a última vence por
especificidade, não por ordem de arquivo.

Sintoma: na Luiza e Raphael (12/09) os nomes dos itens saíram alinhados à
direita; no Marcelo Tolentino (30/09) aconteceu **de novo**, e junto a escada
de pagamento sumiu.

> **Toda classe nova de um build leva sufixo do job ou um `P`:**
> `.invA`, `.escP`, `.cndP`. Nunca reutilizar um nome que já está no CSS base.
> Antes de estilizar, `grep -n "^\.nome" css-proposta*.css`.
