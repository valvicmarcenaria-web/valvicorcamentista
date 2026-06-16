# Parâmetros do orçamento (regras fixas)

Definições do fundador para o motor operar com agilidade.

## Profundidades padrão (quando não vêm no projeto)

| Móvel              | Profundidade |
|--------------------|--------------|
| Cozinha — inferior | 60 cm        |
| Cozinha — superior | 35 cm        |
| Roupeiro           | 65 cm        |
| Bancada            | 50 cm        |

## Móveis com CURVA — regra do fundador (perda + margem)

Todo móvel que tem **curva** (recorte orgânico, raio, painel curvo, lateral
arredondada) carrega muito mais **trabalho operacional** — recorte, lixamento,
fita acompanhando o raio, encaixe. Regra fixa, registrada para todo o time:

- **Perda de material:** considerar **+15%** (aprox.) sobre a peça/área curva —
  além do desperdício normal de aproveitamento. O raio "come" chapa.
- **Margem de lucro:** subir a MC em **+5%** (pelo menos) sobre o piso do projeto
  — a curva é mão de obra embutida que não aparece no material.

> **Propagar:** vale para a **Lavinia** (quantitativo + piso de MC), para o
> **Rodrigo** (margem/saúde financeira — curva puxa o piso pra cima) e para o
> **Vitor** (descrição da proposta — registrar que a peça é curva e por que custa
> mais). Em treinamento contínuo: calibrar o fator a cada projeto com curva.

## LED da marcenaria — padrão (incluir por default)

Todo LED **da marcenaria** (cabeceira, nicho, prateleira, sob bancada) é
**fornecimento Valvic** e entra **por padrão** no orçamento — fita + perfil +
usinagem (lib "Iluminação", ~R$150/m) + sensor/interruptor quando houver.
**Só remover se o cliente pedir** (ou sob exceção sinalizada pelo fundador). Não
confundir com LED de teto/sanca/espelho comprado, que é da elétrica/decoração.

## Tampo de vidro / penteadeira

Tampo de vidro (ex.: sobre penteadeira) = **item de vidro** (lib "Vidros e
espelhos", por m²) **+ logística dedicada de R$ 150** (lib "Especiais ¦ Logística
específica") — o vidro vem de terceirizado e exige entrega/manuseio próprios.

## O que o orçamentista informa vs. o que vem do projeto (Bloco A)

- **Marcos só informa a LINHA de ferragem** (dobradiça/corrediça/sistema).
- Todo o resto (medidas, ambientes, itens, acabamento) **vem no projeto**.

## Bloco B — fixadores e consumíveis (especulação)

Parafuso, cavilha, cola, tapa-furo e afins **não são catalogados**. Entram como
**~2% do custo total** do orçamento.

## Blocos C e D — JÁ EXISTEM no motor do Valvic OS

O motor já dispõe destes (não recriar; apenas referenciar/usar):

- **Comissões:** venda, parceiro (RT), coordenador, programador, marceneiros.
- **Custo de chapa** (comissão de corte por chapa).
- **Logística** (carreto + equipe) e setup/visitas.

> Percentuais de referência (padrão 06/2026): NF **5%** · parcelamento 7–8% ·
> comissão vendedor 5% (**0 quando o lead vem de parceiro**) · comissão produção
> **~7,2%** (marc 5%) · RT 10% do líquido (quando há parceiro) · margem de erro 2% ·
> visita R$250. Meta **MC 35–40%**. Detalhe e divisor de preço em
> `validacao-orcamento.md`.
