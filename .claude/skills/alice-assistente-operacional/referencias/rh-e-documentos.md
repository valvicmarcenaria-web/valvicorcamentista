# RH, documentos e o Drive

## Triagem de currículo

A Karla faz a **primeira peneira** e agenda. Ela não avalia técnica — quem avalia é o Paulo
(fábrica e CNC) ou o Deivison (marcenaria e montagem).

O que ela confere no currículo, nesta ordem:
1. **Mora perto o suficiente** para chegar às 7h todo dia. Este é o filtro que mais elimina
   e o que mais causa desistência no primeiro mês.
2. **Experiência no que a vaga pede** — marcenaria, CNC, montagem, ajudante.
3. **Tempo médio de casa** nos empregos anteriores. Três empregos de dois meses conta uma
   história.
4. **Contato que funciona.**

O que ela **não** filtra: idade, aparência, estado civil, filhos, bairro por preconceito.
Além de errado, é risco jurídico real.

### Mensagem de agendamento
> Olá, [nome]! Aqui é a Karla, da Valvic Marcenaria. Recebemos seu currículo para a vaga de
> [cargo] e gostaríamos de conversar.
>
> Você consegue vir até nossa fábrica em [endereço] no dia [data], às [hora]?
> A conversa dura cerca de 30 minutos. Me confirma por aqui, por favor 🙂

### Mensagem de retorno negativo — sempre mandar
> [nome], obrigada pelo seu tempo e pelo interesse na Valvic. Neste momento seguimos com
> outro perfil para a vaga, mas guardamos seu contato para as próximas oportunidades.
> Desejo sucesso!

Retorno negativo é barato e a cidade é pequena. Quem não recebe resposta fala mal; quem
recebe, volta quando você precisar.

## Admissão — o que tem de estar assinado antes de começar

| Documento | Onde está | Quando |
|---|---|---|
| **Escopo de função** | `painel/apostila-escopos-funcao.html` e os `escopo-*.html` | Na admissão, lido junto, não só entregue |
| **Termo de responsabilidade de veículo** | `painel/controle-veiculos-termo.html` (em branco) e `gerar-termo-veiculo.py` | Antes de dirigir qualquer carro da empresa |
| **Termo de ferramenta** | `painel/planilhas/Valvic_Controle_Patrimonio.xlsx` | Antes de receber kit |
| **Checklist de insumos e ferramentas** | `painel/checklist-insumos-ferramentas.html` | Na entrega do kit |

**Os termos de veículo e ferramenta mudam conforme o vínculo** — CLT e prestador de serviço
têm cláusulas diferentes, porque a base legal do ressarcimento é outra. Não trocar um pelo
outro. O gerador `painel/gerar-termo-veiculo.py` preenche o termo por pessoa a partir de uma
lista — **editar o script, nunca o HTML já gerado**.

## O Drive — a pasta do cliente em 24 horas

Promessa do escopo: fechou contrato, a pasta está montada em **24 horas**. Não é
organização por gosto — é o que permite qualquer pessoa achar o contrato sem perguntar.

Estrutura padrão da pasta de cliente:
```
[Ano] — [Nome do cliente]/
├── 01 Contrato e propostas
├── 02 Projeto (executivo, render, SketchUp)
├── 03 Medições
├── 04 Financeiro (notas, boletos, comprovantes)
├── 05 Produção (plano de corte, listas)
├── 06 Obra (fotos, ocorrências, ficha de conferência)
└── 07 Entrega (termo, garantia, fotos finais)
```

Nomenclatura de arquivo: `AAAA-MM-DD_assunto_versao.ext` — a data primeiro faz o Drive
ordenar sozinho. Nunca "final", "final2", "FINAL definitivo": use `v1`, `v2`, `v3`.

## Sigilo — a norma de conduta

Vários documentos da pasta `painel/` são **restritos**: folha de pagamento nominal, passivo
trabalhista, remuneração individual, documentos do investidor (os `walton-*`), o caderno
empresarial e o modelo econômico.

A regra: **a Karla pode consultar o que precisa para trabalhar, mas não compartilha
documento restrito com ninguém — dentro ou fora da empresa — sem autorização do Jonathan.**
Se alguém da equipe pedir para ver algo assim, a resposta é "isso é com o Jonathan", e
pronto. Não é desconfiança dela; é o que a protege de virar a fonte de um vazamento que ela
não causou.

A Alice, quando for usar um documento restrito para responder algo, **avisa que é restrito**
e não o reproduz por inteiro em mensagem que vai sair da empresa.
