# Guia de Apps e Ferramentas — Valvic

Consultar antes de qualquer modificação nas ferramentas HTML. Documenta padrões,
armadilhas já encontradas e regras de entrega.

---

## Regra nº 0 — toda ferramenta é um ARTEFATO autocontido

Decisão do Jonathan (jun/2026): **toda ferramenta que criamos é um artefato.**
Na prática isso significa **dois entregáveis para o mesmo arquivo**:

1. **Fonte de verdade no repositório** — o `.html` versionado em `ferramentas/`.
   É onde editamos, testamos e commitamos.
2. **Artefato pronto para rodar** — o mesmo arquivo entregue ao Jonathan para
   abrir na hora (enviado no chat / colável como Artifact no Claude.ai).

Requisitos que tornam isso possível (NUNCA quebrar):
- **HTML único e autocontido**: tudo em um arquivo `.html` — CSS e JS inline.
- **Sem build, sem dependências locais, sem backend.** Fontes via CDN (Google
  Fonts) são aceitas; a ferramenta funciona offline mesmo sem elas.
- **Persistência só com `localStorage`** + import/export JSON. Nada de servidor.
- **Abre com duplo-clique** no navegador e funciona igual em qualquer máquina.

> Ao concluir/atualizar uma ferramenta: commitar no repo **e** enviar o arquivo
> ao Jonathan (SendUserFile) para ele ter o artefato em mãos.

---

## Ferramentas existentes

| Arquivo | Skill | Função |
|---|---|---|
| `orcamentista-marcenaria/ferramentas/validacao-orcamento.html` | Lavinia | Orçamento de projeto: material × MC% × KPIs |
| `estrategia-financeira-precificacao/ferramentas/custo-operacao.html` | Rodrigo | Levantamento de custo da operação (centro de custo → ponto de equilíbrio) |

---

## Padrão de render: NUNCA rebuildar o DOM em `oninput`

### O problema

Qualquer input que dispara `render()` / `renderLib()` / `renderTree()` no `oninput`
**destrói o campo que o usuário está digitando**: o DOM é reconstruído, o elemento
some, o foco é perdido. O usuário não consegue digitar nada.

### A solução: split render

Separar a renderização em duas responsabilidades:

1. **`renderDash()` / `recalcDash()`** — atualiza apenas KPIs, barras, fechamento,
   totais globais. **Não toca na tabela/árvore.**
2. **`renderTree()` / `renderLib()`** — reconstrói a tabela/árvore inteira.
   Chamado **apenas em mudanças estruturais**: adicionar/remover item, recolher
   categoria, trocar de ambiente, import, reset.

Para atualizar totais de linha e categoria sem rebuildar, usar **IDs nos elementos
de texto** e uma função de atualização pontual:

```javascript
// IDs nos elementos de total em renderLib/renderTree:
// <span id="cttot-${ci}">...</span>   ← total da categoria
// <td id="rtot-${ci}-${ii}">...</td>  ← total da linha
// <tr id="row-${ci}-${ii}" class="...">  ← classe has/zero da linha

function refreshLibTotals(){
  const amb = S.ambientes[S.ativo];
  S.lib.forEach((cat, ci) => {
    let ctot = 0;
    cat[1].forEach((it, ii) => {
      const q = amb.q[key(cat[0], it[0])] || 0;
      const tot = q * it[1];
      ctot += tot;
      const rtEl = document.getElementById('rtot-' + ci + '-' + ii);
      if (rtEl) rtEl.textContent = tot > 0 ? fmt(tot) : '—';
      const rowEl = document.getElementById('row-' + ci + '-' + ii);
      if (rowEl) rowEl.className = q > 0 ? 'has' : 'zero';
    });
    const ctEl = document.getElementById('cttot-' + ci);
    if (ctEl) ctEl.textContent = ctot > 0 ? fmt(ctot) : '';
  });
}

// setQ e setU chamam refreshLibTotals + recalcDash, NÃO renderLib:
function setQ(ci, ii, val) {
  /* atualiza estado */
  refreshLibTotals();
  recalcDash();
}
```

**Regra:** `oninput` em campos de valor → `refreshTotals + recalcDash`.
`renderLib/renderTree` só em ações estruturais (add, remove, toggle collapse, import).

---

## Modal in-page (substitui `prompt` / `confirm` / `alert` do navegador)

### O problema

`prompt()`, `confirm()` e `alert()` abrem uma janela nativa do browser com o texto
"Essa página diz…". Parece inseguro, é feio e quebra a experiência.

### A solução: modal Promise-based

```html
<!-- HTML — overlay fixo, z-index alto -->
<div id="modal">
  <div class="md-box">
    <div class="md-title" id="mdTitle"></div>
    <input id="mdInp" onkeydown="if(event.key==='Enter')closeModal(true);
                                  if(event.key==='Escape')closeModal(false)">
    <div class="md-row">
      <button onclick="closeModal(false)" id="mdCancel">Cancelar</button>
      <button onclick="closeModal(true)"  id="mdOk">OK</button>
    </div>
  </div>
</div>
```

```javascript
let _resolve = null;

function openModal(title, withInput, def) {
  return new Promise(r => {
    _resolve = r;
    document.getElementById('mdTitle').textContent = title;
    const inp = document.getElementById('mdInp');
    inp.style.display = withInput ? '' : 'none';
    inp.value = def || '';
    document.getElementById('modal').classList.add('show');
    if (withInput) setTimeout(() => inp.focus(), 40);
  });
}
function closeModal(ok) {
  const val = ok ? document.getElementById('mdInp').value : null;
  document.getElementById('modal').classList.remove('show');
  if (_resolve) { _resolve(val); _resolve = null; }
}
function askText(t, d)   { return openModal(t, true,  d); }
function askConfirm(t)   { return openModal(t, false);    }
```

**Uso:** funções que precisam de input do usuário viram `async`:

```javascript
async function addCat() {
  const nm = await askText('Nome da nova categoria:', '');
  if (!nm) return;
  // ...
}
async function rmLine(ci, ii) {
  const ok = await askConfirm('Remover "' + nm + '" da biblioteca?');
  if (!ok) return;
  // ...
}
```

**Regra de revisão:** após qualquer migração, fazer grep por `prompt(`, `confirm(`
e `alert(` para garantir que nenhum sobrou:

```bash
grep -n "prompt(\|confirm(\|alert(" ferramentas/nome-do-app.html
```

---

## Schema normalize — prevenção de tela branca

Sempre que o estado é carregado do `localStorage` ou de um JSON importado, validar
antes de renderizar. Caso o esquema esteja corrompido ou seja de uma versão antiga,
usar `defaultData()` como fallback.

```javascript
function normalize() {
  if (!D || !Array.isArray(D.centros)) D = defaultData();
  D.centros.forEach(c => {
    c.cats = Array.isArray(c.cats) ? c.cats : [];
    c.cats.forEach(k => { k.itens = Array.isArray(k.itens) ? k.itens : []; });
  });
}

function load() {
  try { const r = localStorage.getItem('chave'); if (r) D = JSON.parse(r); }
  catch (e) {}
  if (!D) D = defaultData();
  normalize();  // ← sempre depois do parse
}

function importJSON(e) {
  // ...
  rd.onload = () => {
    try { D = JSON.parse(rd.result); normalize(); boot(); }  // ← normalize antes de boot
    catch (err) { askConfirm('JSON inválido.'); }
  };
}
```

---

## Regra de entrega — testar antes de entregar

**Antes de qualquer entrega de app HTML, rodar teste Node.js** simulando o DOM
para verificar que as funções críticas não travam. Padrão mínimo:

```bash
node - << 'EOF'
# mock de document.getElementById, localStorage, etc.
# eval do bloco <script> do HTML
# chamar: load(), boot(), recalcDash(), setQ(), setU(), setTerc(), suggest(), compute()
# conferir que nenhum lança exceção
EOF
```

O mock de `getElementById` precisa retornar objeto com: `value`, `textContent`,
`innerHTML`, `className`, `style.display`, `classList.add/remove/toggle`.

---

## Persistência e export

- **localStorage**: chave única por app (`'valvic_orc'`, `'valvic_custos'`).
- **Export JSON**: `JSON.stringify(S, null, 2)` — download via `<a>.click()`.
- **Import JSON**: `FileReader.readAsText` → parse → `normalize()` → `boot()`.
- O estado completo (incluindo preços da biblioteca editados) vai no JSON.
  Importar em outra máquina restaura tudo.

---

## Tema claro / escuro

Padrão: variáveis CSS no `:root` para tema escuro. Tema claro via `body.light`
que sobrescreve as variáveis. `S.theme = 'light' | 'dark'` persistido no estado.

```javascript
function applyTheme() {
  const light = S.theme === 'light';
  document.body.classList.toggle('light', light);
}
function toggleTheme() {
  S.theme = (S.theme === 'light') ? 'dark' : 'light';
  applyTheme(); save();
}
```
