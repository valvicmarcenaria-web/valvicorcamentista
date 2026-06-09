# Chapas e acabamentos

Material base padrão da Valvic: **MDF melamínico**. Catálogo e preços de
referência extraídos da biblioteca do **Valvic OS** (`fontes/valvic_os.html` →
objeto `biblioteca`, a *fonte única de verdade* do sistema).

> Preços = **custo de compra** (referência 2026), usados como base de
> precificação interna. Não são preço de venda — o preço ao cliente sai do
> motor de custo (ver `custos.md`).

## Categoria `Chapas` — unidade: **chapa**

| Produto                     | Espessuras e preço (R$/chapa)                          |
|-----------------------------|--------------------------------------------------------|
| MDF Melamínico Fosco        | 6mm 85 · 15mm 110 · 18mm 125                            |
| MDF Branco Ártico Ultra     | 6mm 78 · 9mm 92 · 15mm 108 · 18mm 122 · 25mm 162        |
| MDF Melamínico Brilhante    | 15mm 132 · 18mm 148                                     |
| MDF Cru                     | 6mm 62 · 15mm 82 · 18mm 95 · 25mm 128                  |

**Leitura de uso por espessura (padrão de marcenaria):**
- **18 mm** — estrutura: laterais, bases, tampos, prateleiras, portas.
- **15 mm** — estrutura alternativa / portas e fundos estruturais.
- **6 mm** — fundos de armário e de gaveta.
- **25 mm** — tampos reforçados, peças de destaque.
- **MDF Cru** — quando a peça recebe laca/pintura ou não fica aparente
  (ex.: armário de área de serviço, caixaria interna).

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
