# Cláudia — quarto do Matheus e painel livreiro

**Refazimento de layout**, não orçamento novo. [Jonathan 31/08]

> *"Preciso que refaça o layout dessa proposta adicionando 10% a mais em cada
> valor para pagamento em até 5 vezes sem juros no cartão, ou nesses valores
> atuais para pagamento à vista — entrada de 70% + restante na entrega. Prazo de
> entrega em 60 dias corridos, garantia de 5 anos, validade da proposta 5 dias
> úteis."*

Entrada: `fontes` — não; o original é o `proposta_claudia.pdf` enviado na
conversa. Uma página: tabela de três linhas, quatro renders e um rodapé escuro.
Saída: `build-claudia.py` → `proposta-claudia.pdf`, 5 páginas.

## ⚠ Este job NÃO tem levantamento próprio

Não existe `corte-claudia.py`. Os valores vieram prontos da proposta original e
foram **transportados**, não recalculados. Consequência prática: **não dá para
conferir MC, R$/m² nem plano de corte** neste job. Se em algum momento for
preciso mexer no preço — desconto, revisão de escopo, troca de ferragem — o
levantamento tem de ser feito antes.

## A leitura de escopo que mudou a proposta

A tabela original tinha três linhas: *Quarto Matheus opção 1*, *Quarto Matheus
opção 2* e *Painel livreiro*. **As duas primeiras são alternativas**, não itens
somáveis:

- **opção 1** — armário aéreo com báscula + prateleira + ganchos
- **opção 2** — só duas prateleiras + ganchos, sem armário

Os renders confirmam: o par de imagens do quarto é **a mesma parede com e sem o
aéreo**. O segundo par é o quarto da menina, com e sem o painel livreiro.

A proposta antiga deixava o cliente montar essa conta sozinho. A nova fecha
**por conjunto**:

| Conjunto | À vista | 5 × sem juros |
|---|--:|--:|
| Opção 1 + painel livreiro | **R$ 8.150** | R$ 8.965 · 5 × R$ 1.793 |
| Opção 2 + painel livreiro | **R$ 6.100** | R$ 6.710 · 5 × R$ 1.342 |

Por item:

| Item | À vista | 5 × sem juros |
|---|--:|--:|
| Quarto do Matheus · opção 1 | R$ 3.500 | R$ 3.850 · 5 × R$ 770 |
| Quarto do Matheus · opção 2 | R$ 1.450 | R$ 1.595 · 5 × R$ 319 |
| Painel livreiro | R$ 4.650 | R$ 5.115 · 5 × R$ 1.023 |

> Os 10% são **derivados em código**, não digitados, e o build tem `assert` de
> que a parcela fecha redonda em todos os itens e de que 10% no item equivale a
> 10% no conjunto. Deu certo por sorte da aritmética: todos os valores são
> múltiplos de 50, então +10% dá múltiplo de 5 e a divisão por 5 é exata.

## Condições — o que mudou

| | antes | agora |
|---|---|---|
| Prazo | 30 a 45 dias úteis | **60 dias corridos** |
| Validade | 2 dias úteis | **5 dias úteis** |
| Garantia | não constava | **5 anos** |
| Pagamento | não constava | à vista 70% + entrega · ou 5× sem juros |

## Imagens

As quatro do PDF original, recortadas dos dois pares embutidos. Trazem a marca
d'água **"IMAGEM ILUSTRATIVA"** do próprio fornecedor — **mantida como está**,
que é o mais honesto: a imagem se identifica sozinha, sem que a proposta
precise escrever a frase que a casa proíbe.

> **Armadilha técnica:** `Pixmap.copy()` do pymupdf copia na **interseção das
> coordenadas**, não relativo à origem. Recortar a metade direita com
> `IRect(394,0,783,292)` para um destino de 389 px dá interseção vazia — e o
> arquivo sai com **lixo de memória**, ruído RGB puro. O jeito certo é criar o
> destino já nas coordenadas da origem e só depois `set_origin(0,0)`. Passou na
> primeira rodada e só apareceu no render da página.

## Em aberto

1. **Confirmar que as opções 1 e 2 são mesmo alternativas.** É a leitura que os
   renders sustentam, mas quem escreveu a proposta original foi a casa — vale
   um "sim" antes de enviar.
2. **Cláudia é a cliente?** O nome saiu do arquivo (`proposta_claudia.pdf`) e o
   quarto é do Matheus. Se o contrato for em outro nome, é uma constante.
3. **A cor do MDF** segue "a definir", como no original.
