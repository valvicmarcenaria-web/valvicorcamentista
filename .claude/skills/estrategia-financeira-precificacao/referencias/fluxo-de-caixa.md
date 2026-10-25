# Fluxo de caixa — realizado, projetado e capital de giro

O fluxo de caixa é o pilar 3 do Rodrigo ("preço e caixa são as sementes"). Na
Valvic ele é **o** problema: a empresa cresce e opera acima do break-even
operacional, mas o caixa fica negativo em 7 de 12 meses.

## 1. Três visões — escolher pela pergunta

| Visão | Horizonte | Pergunta que responde | Granularidade |
|---|---|---|---|
| **Fluxo realizado** | passado | "para onde foi o dinheiro?" | por lançamento → mês |
| **Fluxo projetado 13 semanas** | próximos 3 meses | "vou conseguir pagar a folha e os fornecedores?" | semanal |
| **Fluxo projetado 12 meses** | ano | "preciso vender quanto, e quando, para não faltar caixa?" | mensal |

Para caixa crítico (situação atual), **a visão de 13 semanas manda**: é ela que
mostra a semana exata em que o saldo fica negativo e dá tempo de agir (cobrar,
renegociar, antecipar, segurar compra).

## 2. Estrutura (método direto, categorias da marcenaria)

```
SALDO INICIAL (bancos + caixa, conferido com extrato)

ENTRADAS OPERACIONAIS
  Entradas/sinais de contratos novos
  Parcelas de produção / entrega / saldo final (por projeto)
  Recebimento de cartão (líquido de taxa) / antecipação
  Outras (venda de sobra, assistência cobrada)

SAÍDAS OPERACIONAIS VARIÁVEIS
  Chapas e fita · Ferragens · Iluminação · Vidros
  Terceirizados (vidro, serralheria, laca, estofado, pedra)
  Comissões (vendedor, produção, montagem) · RT arquitetos
  Impostos sobre faturamento (DAS) · Frete/carreto · Embalagem

SAÍDAS OPERACIONAIS FIXAS
  Folha + encargos + benefícios · Pró-labore
  Aluguel galpão · Energia · Internet/sistemas · Contador
  Manutenção de máquinas · Marketing · Outras administrativas

= FLUXO OPERACIONAL

INVESTIMENTOS (máquinas, ferramental, veículos)
FINANCIAMENTOS (parcelas de máquinas, devolução ao Paulo, empréstimos,
                 entrada de novo empréstimo)

= VARIAÇÃO DO CAIXA
SALDO FINAL  → comparar com o SALDO MÍNIMO (reserva-alvo: R$ 70k ≈ 45 dias de fixo)
```

Manter **entradas por projeto/cliente** em linhas próprias (ou num anexo) — é o
que permite saber quem atrasou e projetar o recebimento real.

## 3. Como projetar uma marcenaria

**Entradas** — montar a partir de três fontes:
1. **Contratos assinados**: cronograma de parcelas do contrato (entrada, etapas,
   entrega, saldo). Ajustar pela realidade: se o cliente costuma pagar a
   parcela de entrega 10 dias depois, projetar 10 dias depois.
2. **Recebíveis vencidos**: não projetar 100% na próxima semana. Classificar
   (atraso < 30 d: 80% em 2 semanas; 30–90 d: 50%; > 90 d: tratar como
   cobrança, 0% até acordo). Os % são ponto de partida — calibrar com histórico.
3. **Pipeline (vendas futuras)**: só no fluxo de 12 meses e **em cenário
   separado**. Valor × probabilidade × política de entrada (40% em D0). Nunca
   misturar pipeline com contratado no cenário base.

**Saídas variáveis** — derivar da produção, não do faturamento:
- Para cada projeto contratado, aplicar a curva de desembolso do ciclo
  (ver `marcenaria-financeira.md`): material ≈ 30–40% do preço entre D+10 e
  D+30 (respeitando o prazo do fornecedor), terceirizados entre D+30 e D+60,
  comissões conforme a regra de pagamento, DAS no mês seguinte à NF.
- Na falta do orçamento detalhado, usar as % da validação: NF 7%, maquininha
  7–8%, comissão vendedor 3–5%, comissão produção 5%, RT ≈ 7–8% do bruto.

**Saídas fixas** — médias dos últimos 3–6 meses, corrigidas por eventos
conhecidos (13º em nov/dez, férias coletivas, reajuste de aluguel, dissídio).

**Dívidas** — tabela de parcelas por contrato (máquinas, Paulo, capital de giro).

Sempre entregar **3 cenários**: base (contratado + recebíveis ajustados),
pessimista (atraso dos 3 maiores devedores + pipeline zero) e otimista
(pipeline com probabilidade). Mostrar o **mês/semana do pior saldo** em cada um.

## 4. Ciclo financeiro e capital de giro

```
PMR  = prazo médio de recebimento  (da entrega/NF até o dinheiro entrar)
       — na marcenaria, pode ser NEGATIVO se a entrada é forte (cliente paga antes)
PME  = prazo médio de "estoque"     (da compra de chapa até a entrega do móvel)
PMP  = prazo médio de pagamento     (da compra até pagar o fornecedor)

Ciclo financeiro = PME + PMR − PMP   (em dias)
Necessidade de capital de giro ≈ (custo variável + fixo diário) × ciclo financeiro
```

Exemplo Valvic típico: compra chapa em D+15 pagando em 28 dd (paga em D+43),
entrega em D+60, cliente quita o saldo em D+75. Sem entrada forte, o dinheiro
fica fora ~30–45 dias por projeto. Com **entrada de 40% em D0**, o ciclo fica
negativo — o cliente financia o material. **A política de entrada é a alavanca
de caixa mais barata que existe** (não custa juros, não exige vender mais).

## 5. Break-even de caixa

```
Break-even de caixa (faturamento/mês) =
   (custo fixo mensal + parcelas de dívidas + investimentos planejados) ÷ MC%
```

Ele é **maior** que o break-even operacional porque inclui o serviço da dívida.
Exemplo com a régua do orçamento (MC 43,5%): fixo R$ 47,2k + dívidas R$ X →
(47,2 + X) ÷ 0,435. Quando X não é conhecido, dizer isso e mostrar a fórmula —
**não inventar o valor das parcelas**.

## 6. Sinais de "fluxo de caixa doente" (diagnóstico)

- Meses com **recebimento zero** enquanto há produção → contratos sem entrada.
- Saldo negativo recorrente mesmo com DRE positiva → ciclo de caixa / dívida /
  investimento, não preço.
- **Pagamento de fornecedor atrasado** para pagar folha → já é capital de giro
  negativo; projetar 13 semanas imediatamente.
- Investimento em máquina durante saldo negativo (R$ 35k em 2026) → decisão de
  investimento descolada do caixa.
- Pico de saídas no fim do ano (13º + férias + compras) sem reserva.
- Dependência de **um contrato grande** para fechar o mês.
- Pipeline futuro zerado (H2/2026) → o caixa de daqui a 60–90 dias já está
  comprometido; o fluxo de 12 meses tem que mostrar isso em vermelho.
