# Produzir documentos, fichas, painéis e planilhas no padrão Valvic

A Karla precisa de artefatos o tempo todo: ficha, checklist, painel, folha de campanha,
comparativo de cotação. A Alice **produz o arquivo**, não descreve como seria.

## O caminho, sempre o mesmo

1. **Ver se já existe.** `ls painel/` e `ls painel/planilhas/`. Metade dos pedidos já tem
   um documento pronto ou um parecido a copiar. Refazer o que existe é desperdício e cria
   duas versões da verdade.
2. **Copiar o modelo.** `ferramentas/modelo-folha-a4.html` para documento;
   `ferramentas/gerar-planilha.py` para planilha; `painel/painel-producao-a3.html` para
   quadro de parede.
3. **Escrever o conteúdo.**
4. **Gerar e conferir:** `python3 ferramentas/gerar-pdf.py painel/arquivo.html`
5. **Salvar em `painel/`** com nome descritivo, e o PDF com o padrão `Valvic_Nome_Do_Doc.pdf`.

## As regras de página que evitam retrabalho

- **Uma `<div class="sheet">` = uma folha.** A4 retrato é 210×297 mm; A3 paisagem é
  420×297 mm.
- **`over_sheet` e `over_body` têm de dar 0.** Se der estouro, o caminho é **reduzir o
  preenchimento das caixas e encurtar o texto** — nunca diminuir a fonte, que é o que
  estraga a leitura na fábrica.
- **Cuidado com `flex:1` em tabela:** reduzir a altura das linhas **não** reduz a altura
  total, porque a tabela cresce para preencher. O que manda é o conteúdo mínimo mais os
  blocos de altura fixa ao lado.
- **Um aviso por folha, dois no máximo.** Aviso demais vira paisagem.

## O que faz um documento da Valvic ser bom

Todo documento da casa serve a **uma decisão ou a uma cobrança**. Antes de montar, responder:
**quem lê, onde lê e o que faz depois de ler?**

- Documento lido **em pé, na fábrica** → frase curta, fonte maior, coluna para marcar.
- Documento lido **numa reunião** → número em destaque, comparação, uma conclusão por bloco.
- Documento que **alguém assina** → linguagem sem adjetivo, obrigação clara, data e assinatura.

E a marca do padrão da casa: **coluna para marcar**. Checklist sem lugar de riscar não é
checklist, é lembrete.

## Artefatos que a Karla mais pede — e o que já existe

| Precisa de… | Existe / como fazer |
|---|---|
| Quadro semanal de produção | `painel/painel-producao-a3.html` — ver `producao-e-painel.md` |
| Ficha de conferência de peça | `painel/ficha-conferencia-producao.html` |
| Checklist de insumo e ferramenta | `painel/checklist-insumos-ferramentas.html` |
| Ficha de medição | `painel/ficha-medicao.html` |
| Ficha de veículo | `painel/controle-veiculos-ficha-*.html` (uma por carro) |
| Termo de veículo por pessoa | `painel/gerar-termo-veiculo.py` — editar o script |
| Comparativo de cotação | `painel/planilhas/Valvic_Cotacao_Fornecedores.xlsx` |
| Cadastro de fornecedor | `painel/planilhas/Valvic_Gestao_Fornecedores.xlsx` |
| Folha de cobrança da equipe | `painel/folha-cobranca-karla.html` |
| Registro de ocorrência em obra | `painel/ocorrencia-reparo-maria-valdenir.html` (modelo) |
| Folha de campanha | Montar do modelo — ver `campanhas.md` |

## Nomear e guardar

- HTML em `painel/`, nome minúsculo com hífen: `folha-campanha-cafe-parceiras.html`
- PDF ao lado, com maiúsculas: `Valvic_Folha_Campanha_Cafe_Parceiras.pdf`
- Planilha em `painel/planilhas/`, com o gerador `gerar-*.py` e um `LEIA-ME-*.md` explicando
  o que cada aba faz. **Editar sempre o gerador, nunca o arquivo final.**
