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
