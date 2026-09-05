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
