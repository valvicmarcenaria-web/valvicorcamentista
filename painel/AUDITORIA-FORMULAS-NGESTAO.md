# Auditoria de fórmulas · N.GESTAO 1, 2 e 3

Leitura de 23/11/2026. **Somente leitura — nenhum lançamento foi alterado.**
A N.GESTAO 2 está como somente-leitura para mim, o que torna impossível tocá-la.

Método: puxei a fórmula de cada célula das três planilhas pela API, não o valor
exibido, e processei por script. Comparei as 22 fichas, célula por célula, contra
a Ficha Modelo. Recalculei à mão as somas de folha, estrutura, aporte e os
divisores de mês de quatro anos de pagamentos.

---

## O achado que organiza todos os outros

**Das 44 abas das três planilhas, 12 não têm uma única fórmula.** São valores
fixos gravados pelo script `atualizarTudo`. Não existe fórmula para revisar
nelas, e elas não recalculam quando a fonte muda — só quando o script roda.

| Planilha | Abas com fórmula | Abas sem nenhuma fórmula |
|---|---|---|
| N.GESTAO 1 | 4 (as quatro Pagamentos) | 7 — Clientes, Projetos, Análise mensal, Listas, **Conferência**, **O mês**, Notas de migração |
| N.GESTAO 2 | 25 (Painel Geral, Ficha Modelo, 22 fichas, Base) | 2 — Instruções, Listas |
| N.GESTAO 3 | 2 (Custo Fixo, Aporte) | 3 — **O mês**, **Resultado**, **Operação** |

As três abas que o Walton lê são fotografia. E **a última foto é de 21/11 às
05:21** (carimbo em `Operação!B2`). Hoje é 23/11: a atualização automática não
rodou em 22 nem em 23.

---

## ERROS CONFIRMADOS — número errado na tela hoje

### E-1 · Outubro soma 4 de 6 projetos · R$ 196.468 fora
`Pagamentos 2026`, linha 74. O bloco de outubro vai da linha 75 à 80.

| Célula | Fórmula | Cobre |
|---|---|---|
| C74 vendido | `=SUM(C75:C78)` | 4 linhas |
| E74 recebido | `=SUM(E75:E78)` | 4 linhas |
| F74 a receber | `=SUM(F75:F80)` | **6 linhas** |
| H74 contagem | `=COUNT(C75:C78)` | 4 linhas |

Ficam fora **Sandra R$ 10.980** e **Gustavo e Eliza R$ 185.488**. A linha é
internamente inconsistente: alguém corrigiu só o F74, então "a receber" conta
seis projetos e "vendido" conta quatro.

A própria planilha avisa, em R7: *"DIVERGE em −R$ 196.468,00"*. Eu levantei isso
em 30/10. São 24 dias no ar.

### E-2 · Novembro é número digitado, não fórmula
`C82 = 166460`, um valor cravado, enquanto `E82`, `F82`, `G82` e `H82` somam a
faixa 83:85. Hoje coincide com a única linha do bloco (Attos). No dia em que a
Carla digitar o segundo projeto de novembro na linha 84, o recebido e a contagem
sobem e o vendido não — sem aviso.

### E-3 · Custo fixo do painel do Walton está R$ 7.875 acima do real
- `Custo Fixo!H82`, vivo e calculado: **R$ 108.942,70**
- `O mês`, foto: **R$ 116.817,70**

Contamina o ponto de equilíbrio, o "Resultado do mês" (−R$ 107.293,56) e a
"Entrega necessária / mês" (R$ 223.453,70). O break-even publicado ao sócio está
superestimado em R$ 7.875 por mês.

### E-4 · Bloco Aporte de `O mês` voltou para valores revogados
Mostra Entradas 583.460 e Saldo 3.500. A aba `Aporte` viva diz **602.886** e
**R$ 0,85**. Em 04/11 eu liguei `C68:C71` por fórmula à aba Aporte; a rodada de
21/11 sobrescreveu com valores. Erro de R$ 19.426 nas entradas.

### E-5 · Vendido no ano, no painel do Walton, está R$ 371.815 abaixo
`O mês` diz R$ 1.650.462. `Pagamentos 2026!A7`, vivo, diz **R$ 2.022.277**.

### E-6 · Comissão de coordenação congelada na ficha da Ana Carolina
`D65 = 883,93`, valor cravado. O modelo tem `=IF($B65="";"";ROUND($B65*$D$45;2))`.
Com `B65 = 1,0%` e a receita líquida de R$ 87.466 (provada por `D66 = 437,33 =
0,5% × 87.466`), o certo é **R$ 874,66**. Erro de R$ 9,27.

### E-7 · Data de entrada da Flavia com ano errado
`Painel Geral`: 07/08/**2016**. Deveria ser 2026.

---

## FRAGILIDADES — certo hoje, errado amanhã

### F-1 · Valor de venda digitado em A13 nas fichas da Juliana e do Orlando
Nas duas, `A13` é número cravado (15.700 e 12.000) e **`D28` está vazio**. O
modelo tem `A13 = IF($D$28="";0;$D$28)`. Funciona porque tudo lê A13, mas:
restaurar a fórmula do modelo zera as duas fichas. É a mesma causa do
desencontro da Maria que você relatou em 30/10.

### F-2 · A Ficha Modelo ainda carrega as colunas de orçado e desvio
Elas foram removidas das fichas, mas não do modelo. Resultado: **7 fichas
nasceram com elas de volta** — Attos, Daniel, Gustavo, Leonardo Henrique,
Sandra, Juliana e Orlando. Existem duas gerações de ficha convivendo: 8 com 307
ou 308 fórmulas e 14 com 281 a 283.

### F-3 · Percentuais de comissão congelados em algumas fichas
`B67` em 6 fichas, `B68` em 5, `B69` em 2. Mostram um percentual que parou de
acompanhar o valor.

### F-4 · A ficha do Jairo não tem linha de conferência
`E194` e `G194` estão vazias. `G194` é o aviso *"ATENÇÃO: N lançamento(s) sem
categoria"*. Nessa ficha ele nunca vai disparar.

### F-5 · Painel Geral usa INDIRECT 430 vezes, dentro de IFERROR
`=IF($B11="";"";IFERROR(INDIRECT("'"&$B11&"'!A7");""))`. Se o nome da aba mudar,
a referência quebra **em silêncio** e devolve branco, que soma como zero. E 12
das 22 abas têm espaço no fim do nome. Hoje as 22 resolvem.

### F-6 · O Painel puxa a venda de C61, a soma dos ambientes
Não de A13, o valor do contrato. Hoje as 22 fichas fecham, então não há dano —
mas quem manda no painel e em tudo a jusante é a soma dos ambientes.

### F-7 · Base · Comissões tem data em linha sem ambiente
A coluna R dispara nas 12 linhas alocadas por projeto, inclusive nas vazias.
Gera linhas em que só a data está preenchida.

### F-8 · Faixas do Aporte encolheram de 500 para 499
Ao excluir a linha de R$ 533, todas as faixas `$C$21:$C$500` viraram `$C$21:$C$499`.

### F-9 · Teto de 5 parcelas por projeto
`E11 = ROUND(SUM(I11;L11;O11;R11;U11);2)`. Projeto com mais de cinco pagamentos
não cabe na linha.

### F-10 · Base do vendedor e da RT deixa D42 de fora
`D41` e `D43` incidem sobre `A13 − SUM(D38:D40)`. Se D42 for custo de venda sobre
o bruto, a base de vendedor e RT fica inconsistente com a dos outros encargos.
Decisão de desenho a confirmar, não defeito provado.

---

## FALTA DIGITAR — não é fórmula

- **Linha 31 de `Pagamentos 2026`** — "Andre alphavillie - APIA" sem valor de
  investimento, com "investimento - 87k" escrito na forma de pagamento. Cerca de
  R$ 87.000 fora de qualquer total.
- **A atualização automática não roda desde 21/11 05:21.**

---

## O QUE ESTÁ CORRETO

- **Zero células de erro.** Nenhum `#REF!`, `#DIV/0!`, `#VALUE!` ou `#N/A` em
  nenhuma das três planilhas. Varri todas.
- **As 22 fichas fecham.** Em todas: ambientes = valor de venda, e custo +
  margem = venda. As 22 conferências internas `D61` dizem *"OK · os ambientes
  somam o valor de venda"*.
- **Custo Fixo** — recalculei as três somas célula a célula: folha R$ 78.192,70,
  estrutura R$ 30.750, investimentos R$ 8.600. Encargos de 33% incidem só sobre o
  fixo e só quando o vínculo é CLT, nunca sobre VT e VR. Correto.
- **Aporte** — SUMIF e COUNTIF por categoria corretos, saldo = entradas menos
  aplicado, e a linha de conferência detecta valor lançado sem categoria.
  Resíduo de R$ 0,85 é centavo de arredondamento dos lançamentos reconciliados
  por extrato, não erro de fórmula.
- **Pagamentos 2025, 2024 e 2023** — os 35 divisores de mês têm faixa correta e
  com folga. Nenhum problema.
- **O A13 circular que eu causei em outubro está corrigido** no modelo:
  `=IF($D$28="";0;$D$28)`.
- **"Ainda a faturar"** (`E34`) e o status da RT seguem como fórmula viva.
- **A cascata de encargos da ficha confere com a política da casa**: imposto e
  taxa de máquina sobre o bruto; vendedor e RT sobre o líquido; comissões de
  produção, montagem e projeto sobre a receita líquida do ambiente.
- **Base · Comissões** usa referência direta entre abas, não INDIRECT — quebra
  visível em vez de silenciosa. Melhor que o Painel Geral.

---

## Ordem de correção que eu recomendo

1. `C74`, `E74` e `H74` para a faixa 75:80 — R$ 196.468, e a planilha já avisa.
2. `C82` volta a ser fórmula, `=SUM(C83:C85)`.
3. Custo fixo e aporte de `O mês`: decidir se viram fórmula viva ou se o script
   passa a ler a fonte certa. Enquanto não, o painel do sócio está errado.
4. Descobrir por que a atualização parou em 21/11.
5. Limpar o orçado/desvio da Ficha Modelo, senão cada ficha nova repõe.
6. `D65` da Ana Carolina volta a ser fórmula.
7. `D28` das fichas da Juliana e do Orlando — com cuidado: mexer em A13 antes
   zera as duas.
8. Valor do contrato da linha 31 e o ano da Flavia.
