# Razão das planilhas · o que existe e onde vai parar

Leitura célula a célula feita em **26/10/2026**, com o conector do Google Sheets,
depois que a "Analise anual" foi restaurada da lixeira. Não é resumo de dump: é
leitura de intervalo, com os totais refeitos à mão e conferidos contra os
divisores que a própria planilha calcula.

O que esta página responde: **se alguma coisa digitada pode se perder na
mudança**. A resposta curta é não, e abaixo está o porquê, linha a linha.

---

## 1 · Analise anual — o arquivo que sai de cena

15 abas. É daqui que tudo migra, **por cópia**, e nada é apagado na origem pelo
script.

| Aba | O que é | Confere |
|---|---|---|
| **2026** | 47 projetos · R$ 1.650.462 | os 10 divisores de mês somam o total |
| **2025** | 55 projetos · R$ 1.566.491 | 12 divisores · Set é o maior mês, R$ 572.850 |
| **2024** | 51 projetos · R$ 1.072.980 | 12 divisores · Monte Negro recebeu R$ 20.000 a mais |
| **2023** | 54 projetos · R$ 710.884 | 12 divisores **+ bloco "Anterior (2022)" com 12 contratos e R$ 274.600, fora do total de propósito** |
| **Custo Fixo** | 19 pessoas · 23 itens de estrutura · 3 de investimento | folha R$ 86.067,70 + estrutura R$ 30.750 = **R$ 116.817,70** · com investimentos R$ 125.417,70 |
| **Aporte Walton** | 5 entradas · 10 saídas · 9 investimentos · 2 serviços | 579.960 − 163.378 − 374.582 − 42.000 = **R$ 0,00** |
| **Listas** | 13 divisores + 12 formas de pagamento | load-bearing: o total de cada ano depende dela |
| **Notas de migração** | 67 datas corrigidas, o −R$ 20.000 do Monte Negro | explicação que não existe em outro lugar |
| Painel · Produção e Entrega · Painel de Competência · Análise & Sazonalidade · Base · Projetos · Base · Recebimentos · Base · Custo Fixo | **derivadas** | nada digitado, todas se refazem |

**Migram:** Listas, as quatro abas de ano (viram `Pagamentos 2026`…`2023`),
Custo Fixo, Aporte Walton (vira `Aporte`), Notas de migração.
**Não migram:** as sete derivadas. Morrem com o arquivo.

---

## 2 · O 2026 já está salvo

A cópia na `N.GESTAO 1 · Gestão` foi lida linha por linha contra o original:

* **mesmos 47 projetos, na mesma ordem, com os mesmos nomes e projetos**;
* única diferença: a **Maria**, de R$ 117.738 para **R$ 99.978** — edição sua,
  de 25/10. Por isso a cópia fecha em R$ 1.632.702 e o original em R$ 1.650.462.

A cópia está **à frente** do original. Quando a Analise anual for para a lixeira,
o 2026 não perde nada.

### Um contrato de R$ 87.000 que saiu antes disso

O `BACKUP - Valvic_Controle_Pagamentos`, de 23/10 16:43, fecha 2026 em
**R$ 1.737.462**. O original hoje fecha em R$ 1.650.462. A diferença, R$ 87.000,
é a linha **"Andre alphavillie - APIA / casa"**, de Abril: no backup ela tem
valor, hoje tem a palavra *"investimento - 87k"* escrita na coluna de forma de
pagamento e **nenhum valor**. Saiu entre 23 e 24 de outubro, antes de a cópia
existir — então as duas estão iguais nisso.

Se foi de propósito, está certo. Se não foi, **o valor está no backup**.

---

## 3 · Custo por Projeto — não se mexe

22 abas: Instruções, Painel Geral, Ficha Modelo, **17 fichas**, Base · Comissões,
Listas. **Onze fichas têm espaço no fim do nome** (`Juliana `, `Ana Carolina `,
`Andrea `, `EPE Formas `, `Flavia `, `Graciene `, `Larissa `, `Leonardo `,
`Luiz `, `Maria `, `Nadia `) e o código lê o nome **cru**, sem trim, porque é com
ele que se abre a aba.

**Carteira: R$ 866.043** em 17 obras. **Cinco entregues** (têm competência):

| Obra | Competência | Venda | Custo | MC | Atraso | Faturado |
|---|---|---|---|---|---|---|
| Carla Dresller | Set/2026 | 27.000 | 15.455,34 | 42,8% | — | **27.000** |
| Luiz | Set/2026 | 20.000 | 7.086,34 | 64,6% | 2 dias | 0 |
| Flavia | Out/2026 | 15.000 | 5.869,14 | 60,9% | 13 dias | 0 |
| Simony | Out/2026 | 34.850 | 20.056,47 | 42,4% | 15 dias | 0 |
| Maria | Out/2026 | 117.738 | 29.262,36 | 75,1% | 14 dias | 48.174 |

As outras doze estão em produção e **não têm MC publicada em lugar nenhum**.

---

## 4 · As catorze individuais — 9 células digitadas no total

Lidas uma a uma. O que a pessoa digita (Pagamento combinado, Status, Repassado
em NF, Observação) **não existe a montante**: é acordo com gente, não cálculo.

| Pessoa | A receber | Células digitadas |
|---|---|---|
| Deivison | R$ 5.826,52 | 0 |
| Jhon | R$ 3.795,59 | **2** — Larissa, 25/09, "Pago" sobre R$ 0,00 |
| Samuel | R$ 2.428,76 | 0 |
| Cesar | R$ 2.421,63 | 0 |
| Lorrane | R$ 1.211,77 | **7** — 3 "Pago" em 10/10, 3 "Em aberto" em 30/10 |
| Bruna | R$ 421,80 | 0 — só a Larissa tem gestor técnico preenchido |
| Joelson | R$ 61,74 | 0 |
| Lucas · Ronald · Davi · Jomar · Bruno · Wallace · Douglas | R$ 0,00 | 0 |

**Ronald não aparece em ambiente nenhum** e por isso recebe zero. O script
guarda essas 9 células antes de reescrever a aba e devolve depois, casando pelo
nome do projeto — conferido no código e na simulação.

---

## 5 · O que a leitura achou de errado

| | |
|---|---|
| **Dias de atraso é texto** | está escrito "13 dias", "2 dias", "14 dias", "15 dias". `Number()` disso é NaN e virava zero: obra atrasada aparecia no prazo. **Corrigido.** |
| **Status do RT com a dica dentro** | nas 17 fichas, a célula E43 guarda a frase "% sobre o líquido: venda menos impostos, máquina e taxas" em vez do status. RT nenhum consegue ser marcado como pago. **Corrigido** — defeito meu, da conversão do orçado. |
| **"Ainda a faturar" congelado** | virou texto fixo no dia da conversão. Na Maria anuncia R$ 117.738 a faturar com R$ 48.174 já faturados. **Corrigido.** |
| **Linha sem nome de cliente sumia** | "Pergolado Banheiro", R$ 5.500, Dezembro/2023. **Corrigido.** |
| **Saldo do aporte** | eu ia publicar que não fechava. Fecha: faltava o bloco "Saídas Walton", R$ 42.000 de serviços tomados. **Conclusão minha desfeita pela leitura.** |
| Ambiente sem valor | a "Lavanderia" da Maria tem montador e data e **nenhum valor** |
| Ambientes que não fecham | Leonardo −29.300 · Cristiane −29.000 · Andrea −27.000 · Maria −24.080 · Jairo +7.300 · Ana Carolina +10 |
| Gestão técnica | **16 das 17 fichas** cobram 0,5% sem nome de gestor |
| Richard | sem coordenador e sem vendedor |
| Flavia | data de entrada **07/08/2016** |
| Faturamento | **uma nota em 17 fichas** — R$ 48.174 de R$ 866.043 |
| Venda divergente | Maria: ficha 117.738 × contrato 99.978 · Leonardo: ficha 55.800 × contrato 55.000 |

Tudo isso vira linha na aba **Conferência**, ordenado por dinheiro em risco.
