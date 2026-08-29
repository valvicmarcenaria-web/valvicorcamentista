# Chapas e acabamentos

Material base padrão da Valvic: **MDF melamínico**. Catálogo e preços de
referência extraídos da biblioteca do **Valvic OS** (`fontes/valvic_os.html` →
objeto `biblioteca`, a *fonte única de verdade* do sistema).

> Preços = **custo de compra** (referência 2026), usados como base de
> precificação interna. Não são preço de venda — o preço ao cliente sai do
> motor de custo (ver `custos.md`).

> **Dimensão padrão da chapa: 2750 × 1850 mm** (~5,09 m²), confirmada nos
> planos de corte reais. O consumo é apurado por nesting — ver `quantitativo.md`.

## Categoria `Chapas` — unidade: **chapa**

| Produto                     | Espessuras e preço (R$/chapa)                          |
|-----------------------------|--------------------------------------------------------|
| MDF Melamínico Fosco        | 6mm 85 · 15mm 110 · 18mm 125                            |
| MDF Branco Ártico Ultra     | 6mm 78 · 9mm 92 · 15mm 108 · 18mm 122 · 25mm 162        |
| MDF Melamínico Brilhante    | 15mm 132 · 18mm 148                                     |
| MDF Cru                     | 6mm 62 · 15mm 82 · 18mm 95 · 25mm 128                  |

### Padrão de espessuras Valvic (confirmado na proposta ao cliente)

| Aplicação            | Espessura padrão            |
|----------------------|-----------------------------|
| Estrutura (caixaria) | **15 mm**                   |
| Fundos               | **6 mm** (duplo revestimento) |
| Prateleiras          | **18 / 25 mm**              |
| Portas               | **15 mm**                   |
| Portas de passagem   | **42 mm**                   |

- **MDF Cru** — quando a peça recebe laca/pintura ou não fica aparente.
- **branco TX Ultra** — interno de áreas úmidas (mais resistente à umidade).

### Linhas de melamínico usadas em projeto (nomes comerciais reais)

Vistas na proposta Lucas e Ana e na planilha — a classificação
"branco / cor / especial" da planilha mapeia para estas linhas:

- **Branco:** Branco TX · Branco TX Ultra · Branco Diamante · Branco Diamante Essencial.
- **Cor:** Areia Guararapes · Cinza Fóssil · Carvalho Guararapes.
- **Especial / nobre:** Freijó Puro Duratex · lâmina natural (carvalho,
  nogueira) · com acabamento curvo/ripado/laca.

## Categoria `Portas de Vidro` — unidade: **folha**

| Produto                | Variações e preço (R$/folha)                              |
|------------------------|-----------------------------------------------------------|
| Vidro Reflecta Bronze  | Sem perfil 380 · Perfil champanhe 450 · Preto 460 · Inox 470 |
| Vidro Reflecta Prata   | Sem perfil 340 · Perfil champanhe 410 · Perfil preto 420  |
| Vidro Fumê             | Sem perfil 290 · Perfil champanhe 360                     |
| Espelho Prata          | Colado 220 · Com perfil 285                               |
| Vidro Canelado         | Sem perfil 310 · Com perfil 375                           |

## Categoria `Portas de Passagem` — unidade: **un**

| Produto         | Variações e preço (R$/un)                       |
|-----------------|-------------------------------------------------|
| Porta Pivô      | 60cm 680 · 70cm 720 · 80cm 780 · 90cm 840       |
| Porta de Correr | 2 folhas 920 · 3 folhas 1240 · 4 folhas 1560    |
| Porta de Giro   | 70cm 490 · 80cm 530 · 90cm 570                  |

## Categoria `Acabamentos` — unidade: **m** (metro linear)

| Produto             | Variações e preço (R$/m)                                   |
|---------------------|------------------------------------------------------------|
| LED Fita            | Branco frio 28 · Branco quente 28 · RGB 45                 |
| Perfil de Alumínio  | Bronze 38 · Preto 38 · Prata 32 · Dourado 44               |
| Rodapé Inox         | 10cm 52 · 15cm 68                                          |
| Fita de Bordo       | Branco 22mm 2,8 · Branco 45mm 4,2 · Colorida 22mm 3,4      |

### Fita de bordo
- Padrão Valvic: **fita de borda extra fina 0,4 mm** (laminação refinada,
  argumento de acabamento na proposta).
- Cobrada por **metro linear**, na largura que acompanha a espessura da chapa
  (22mm para peças de 15/18mm; 45mm para peças mais espessas).
- Somar apenas as **bordas aparentes** de cada peça.

> TODO Valvic: confirmar critério de bordas por tipo de peça e a perda/folga
> de fita considerada.

## Regra de quantitativo de chapas

No Valvic OS, a chapa é lançada como **componente com quantidade em nº de
chapas** (unidade `chapa`) dentro de cada item. Ou seja: o consumo é informado
em **chapas inteiras (ou frações)** consumidas por ambiente/item — não por m²
peça a peça.

> TODO Valvic: registrar como você chega ao número de chapas a partir das
> peças (plano de corte mental? fator de aproveitamento? arredondamento para
> cima?). É a regra que vamos destilar com os projetos resolvidos.

---

## Branco de banheiro é o ULTRA — [Jonathan 29/08/2026]

> *"Cite que os MDF branco a ser utilizados serão da linha ultra premium,
> inclusive o da nova porta."*

Nos banheiros da Dani Rosaria eu tinha orçado tudo em **Branco TX**. O branco
que a casa usa nesses jobs é o **MDF Branco Ártico Ultra** — este arquivo já o
descrevia como *"interno de áreas úmidas, mais resistente à umidade"*, que é
exatamente o caso. Também resolveu uma dúvida que estava aberta: a prancha da
Giza dizia "MDF BRANCO ÁRTICO" na nota de furo.

**Na proposta**, a linha é benefício técnico, não nome comercial:

> MDF branco da linha **ultra premium** — chapa de área úmida, mais resistente
> à umidade que o MDF branco comum.

### ★ Como o preço foi adotado

O `materiais.json` **não tem** o Ártico Ultra. A tabela deste arquivo tem, mas
numa base de preços diferente (aqui o Melamínico Fosco 18 mm é 125; no
`materiais.json` é 600). O que se aproveita daqui é a **posição relativa**:

| | 6 mm | 15 mm | 18 mm |
|---|--:|--:|--:|
| Ártico Ultra (tabela deste arquivo) | 78 | 108 | 122 |
| Melamínico Fosco (mesma tabela) | 85 | 110 | 125 |
| **razão** | 0,918 | 0,982 | 0,976 |
| **aplicada à base de hoje** | **275** | **490** | **585** |

Ou seja: **o branco ultra sai praticamente no preço de um melamínico
colorido** — coerente com um MDF de área úmida. Os motores calculam a razão em
código, não o número, para que a conta fique auditável.

> ⚠ **CONFERIR o preço de compra com o Jonathan.** É a adoção ★ de maior peso
> destes dois jobs: nos banheiros da Giza, que são 100% brancos, ela sozinha
> move o material de R$ 1.230 para R$ 1.530 mesmo depois de o job perder uma
> chapa inteira.
