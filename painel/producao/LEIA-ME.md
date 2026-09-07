# Abertura de Produção — gerar os checklists de um projeto

**Script:** `gerar-abertura.py` · **Uso:**

```bash
cd painel/producao
python3 gerar-abertura.py projeto.json  [saida.pdf]
```

Sai um **HTML** e um **PDF** com as sete folhas do projeto já preenchidas: escopo de venda,
ficha de medição, matriz do marceneiro, conferência de saída, insumos e kit por ambiente,
kit da obra, kit do montador (entrada, diário e vistoria) e a conferência final da direção.

---

## Por que existe, se já há a ferramenta web

A ferramenta em `claude.ai/code/artifact/8ef2c8dd-bbcc-4b36-86f1-ca012bba0b47` lê o contrato e
valida os dados, e isso ela faz bem. Mas **o painel onde ela roda bloqueia impressão e
download** — é regra da plataforma, não falha de código, e nenhum ajuste no código contorna.

Então o caminho do papel é este script: a Karla descreve o projeto na conversa com o Claude,
o Claude escreve o JSON, roda o script e **devolve o PDF como arquivo no chat** — que ela
baixa como qualquer anexo, sem popup e sem copiar nada.

---

## O JSON

```json
{
  "cliente": "Lucas e Ana",
  "op": "P-2026-058",
  "versao": "v2",
  "endereco": "Rua Ouro Preto, 1240 — Belvedere",
  "arquiteto": "Isabella Biancardine",
  "vendedor": "Jonathan",
  "prazo": "30/10/2026",
  "aberto": "07/09/2026",
  "condominio": "Ed. Vista — 8º andar, elevador de serviço",
  "acesso": "Carga e descarga só até as 17h",
  "caixaria": "Branco Diamante",
  "dobradica": "Hettich Sensys ônix",
  "corredica": "Oculta soft-close",
  "puxador": "Passante e em cava",
  "iluminacao": "Fita de LED 240 leds com perfil e difusor",
  "ambientes": [
    { "nome": "Living jantar", "itens": ["Cristaleira"], "descricao": "…" }
  ]
}
```

**`cliente` e `op` são obrigatórios** — sem eles o script para, porque folha sem cabeçalho
circula pela fábrica sem dono.

Para gerar só parte, some `"checklists": ["escopo","matriz","saida"]`. As chaves são
`escopo · medicao · matriz · saida · ferramentas · montador · final`.

---

## As marcas de atenção — o que o script deduz sozinho

Da descrição de cada ambiente ele detecta **led · vidro · serralheria · pedra · correr ·
validar**, e é isso que faz as folhas se adaptarem ao projeto:

- ambiente com **LED** ganha a coluna LED na matriz e o perfil, a fita e a fonte no kit;
- ambiente com **vidro** ganha a linha de vidro embalado;
- ambiente com **"obs. a se validar"** no contrato faz aparecer a **tarja vermelha** na matriz:
  não programe nem corte antes de o comercial fechar o que está em aberto.

Onde o insumo não se aplica ao ambiente, a folha traz um **traço** em vez de caixa — é assim
que ela diz que o LED vai só na suíte e no office.

Qualquer uma dessas marcas pode ser forçada no JSON: `"led": true`, `"validar": false`.

---

## Regras da geração

- **Vários ambientes por folha.** A coluna de ambiente ocupa as linhas dele e um filete
  dourado separa um do outro. Um ambiente só se divide entre folhas quando sozinho não cabe —
  e aí o nome se repete com "(continua)".
- Cada ambiente ganha **duas linhas em branco**, para a fábrica quebrar em mais módulos.
- **Sem valores em R$** nas folhas.
- O PDF sai por `.claude/skills/alice-assistente-operacional/ferramentas/gerar-pdf.py`, que
  confere se algum conteúdo estourou a página. `over_sheet` tem de dar **0**.

## Para mudar o conteúdo das folhas

Edite este script. As folhas da ferramenta web estão no artefato e precisam ser ajustadas lá
também, senão as duas versões divergem — o script é a fonte do que vai para o papel.
