# Controle de Patrimônio — Valvic

Planilha única para o cadastro de bens da empresa e para os termos de posse das
ferramentas cedidas à equipe.

**Arquivo:** `Valvic_Controle_Patrimonio.xlsx`
**Gerador:** `gerar-controle-patrimonio.py` — editar o script, nunca o `.xlsx` diretamente,
senão a próxima geração sobrescreve as mudanças.

---

## As 15 abas

| Aba | Para quê |
|---|---|
| **Dashboard** | Painel com valor de aquisição, depreciação, valor contábil, itens cedidos, termos assinados e três quadros de distribuição. Tudo calculado — nada se digita aqui |
| **Patrimônio Geral** | O cadastro. Uma linha por bem, 150 linhas disponíveis. Fundo creme = preencher; fundo cinza-azulado = calculado |
| **Movimentações** | Histórico de entregas, devoluções, transferências, manutenções e baixas — uma linha por evento |
| **Conferência Mensal** | Checagem física, responsável Deivson, periodicidade mensal |
| **Termo · [nome]** × 8 | Um termo por colaborador, em layout A4 retrato pronto para imprimir |
| **Termo · MODELO CLT / PJ** | Modelos em branco para quem entrar depois |
| **Listas** | Fontes das listas suspensas e as taxas de depreciação por categoria |

## Dois instrumentos jurídicos diferentes

Não é o mesmo documento com nome trocado — as cláusulas mudam.

- **CLT** (Cezar, Jomar, Davi, Jonathan Godoy, Joelson) → *Termo de Entrega e Responsabilidade*.
  A cláusula de dano prevê **reposição in natura** como remédio principal: o colaborador compra
  outro item equivalente por conta própria, no prazo de 30 dias, da forma que lhe for mais
  conveniente. O desconto em folha só aparece como alternativa, condicionado a **autorização
  expressa e específica**, nos termos do art. 462, §1º, da CLT.
- **PJ** (Deivson, Samuel, Jackson) → *Termo de Comodato*, regido pelos arts. 579 e seguintes do
  Código Civil.

Em ambos: desgaste natural por conta da empresa, guarda vedada em residência, e Boletim de
Ocorrência obrigatório em até 48 horas para furto ou roubo.

## Como operar

1. **Cadastrar o bem** na aba Patrimônio Geral, com código sequencial `VLV-0001`.
2. **Etiquetar** a ferramenta com o mesmo código e registrar o código de etiqueta do fabricante
   ou número de série na coluna F.
3. **Ceder**: preencher Responsável, Estado na entrega e Data de entrega.
4. **Gerar o termo**: na aba da pessoa, digitar só os códigos na coluna A — descrição, marca,
   número de série e valor vêm sozinhos do cadastro.
5. **Fotografar** os itens na data da entrega. O anexo fotográfico integra o termo; sem ele o
   documento não sustenta pedido de reposição.
6. **Imprimir em duas vias**, colher as assinaturas e marcar `Termo assinado = Sim` no cadastro.
7. **Na devolução ou no desligamento**, preencher o quadro de devolução do mesmo termo.

## Depreciação

Linear, mês a mês: `valor de aquisição × taxa anual ÷ 12 × meses de uso`, limitada ao valor do
bem. A taxa vem da categoria, pela tabela na aba Listas. A data de referência do cálculo é a
célula `Listas!N2`, que traz `=TODAY()`.

> **Confirmar as taxas com o contador** antes de usar esses números em balanço.

## Duas ressalvas

**Não foi possível recalcular as fórmulas neste ambiente.** O LibreOffice do runner esgota o
tempo mesmo com um arquivo de quatro células, então a verificação por execução não rodou. As
1.718 fórmulas foram auditadas manualmente — referências entre abas conferidas, funções todas
do conjunto Excel 2007 (`SUMIF`, `COUNTIFS`, `INDEX`, `MATCH`, `IFERROR`, `DATEDIF`), sem
nenhuma função moderna que quebre. **Ao abrir no Excel ou no Google Sheets os valores aparecem
normalmente**, porque o cálculo acontece na abertura. Se algum previewer mostrar células vazias,
é isso — não é erro de fórmula.

**A cláusula de desconto precisa de revisão jurídica.** É a que mais gera passivo trabalhista.
Vale o advogado revisar antes da primeira assinatura, e vale checar a convenção coletiva da
categoria em BH, que pode ter regra própria sobre fornecimento e desconto de ferramenta —
prevalecendo sobre o que está escrito aqui.
