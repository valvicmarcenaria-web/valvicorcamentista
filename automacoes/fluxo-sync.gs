/**
 * Valvic · espelho automático do fluxo de caixa em duas frentes:
 *
 *   1) Categoria que começa por "Nova Fábrica · "  →  aba "Nova Fábrica" da N.GESTAO 3
 *   2) Coluna Cliente + Categoria no projeto       →  livro de compras da ficha do
 *                                                     cliente, na N.GESTAO 2
 *
 * Instalar NA PLANILHA DE FLUXO DE CAIXA DO MÊS.
 * Extensões → Apps Script → substitua o conteúdo por este arquivo → salve.
 * Depois rode uma vez instalarGatilhos() e autorize.
 *
 * Mudanças em relação à versão anterior:
 *   · a primeira linha de dados do fluxo é descoberta sozinha (antes estava fixa em 2,
 *     e quebrou quando o painel de saldos foi para o topo da aba);
 *   · a coluna "ID (fixo, não editar)" passa a ser preenchida pelo script;
 *   · a chave de rastreio usa o ID, não o número da linha — mover linha não duplica nada;
 *   · a chave da ficha foi para a coluna P: em K a N ela caía dentro da célula mesclada
 *     do Status (I:O) e o Apps Script descartava a escrita sem acusar erro;
 *   · depois de gravar a chave o script confere se ela realmente ficou lá, e para com
 *     mensagem clara se não ficou — antes isso passava batido e duplicava na rodada seguinte.
 */

var FLUXO_ABA   = 'LANCAMENTOS';

// ── destino 1: nova fábrica ────────────────────────────────────────────────
var NF_ID       = '1-7XUrVso9oVKccQjM2m5Tgd9_-QIk-r1LZ8XZbDnGL0';
var NF_ABA      = 'Nova Fábrica';
var NF_PREFIXO  = 'Nova Fábrica · ';
var NF_PRIMEIRA = 31;
var NF_ULTIMA   = 600;
var NF_COL_CHAVE = 11;

// ── destino 2: fichas de cliente ───────────────────────────────────────────
var FICHA_ID     = '1tTJXG4w7lDvIcnd0dyr219-leOPwuURqrBk6lJIr18I';
var LIVRO_TITULO = 'Descrição / fornecedor';  // cabeçalho do bloco 8
var LIVRO_LINHAS = 60;                        // o bloco tem 60 linhas; as fórmulas da
                                              // ficha somam exatamente esse intervalo
var LIVRO_COL_CHAVE = 16;                     // coluna P da ficha.
                                              // NÃO usar K a N: na ficha o campo "Status"
                                              // é uma célula mesclada de I até O, e o
                                              // Apps Script DESCARTA EM SILÊNCIO qualquer
                                              // escrita numa célula que não seja a âncora
                                              // da mescla — sem erro no log. Foi por isso
                                              // que a primeira rodada gravou as compras
                                              // mas não gravou as chaves. P é a primeira
                                              // coluna livre depois da mescla.

// ── colunas do fluxo (1 = A) ───────────────────────────────────────────────
var C_DATA = 1, C_TIPO = 2, C_DESC = 3, C_CATEG = 4, C_CONTA = 5, C_VALOR = 6,
    C_OBS = 9, C_CLIENTE = 15, C_CATPROJ = 16, C_ID = 17;
var FLUXO_COLS = 17;

// ───────────────────────────────────────────────────────────────────────────
function onOpen() {
  SpreadsheetApp.getUi().createMenu('Valvic')
    .addItem('Sincronizar tudo agora', 'sincronizarTudo')
    .addItem('Sincronizar só a Nova Fábrica', 'sincronizarNovaFabrica')
    .addItem('Sincronizar só as fichas de cliente', 'sincronizarClientes')
    .addSeparator()
    .addItem('Instalar automação', 'instalarGatilhos')
    .addToUi();
}

function instalarGatilhos() {
  var id = SpreadsheetApp.getActive().getId();
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'aoEditar') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('aoEditar').forSpreadsheet(id).onEdit().create();
  sincronizarTudo();
  SpreadsheetApp.getActive().toast('Automação instalada e sincronizada.', 'Valvic', 8);
}

function aoEditar(e) {
  if (e && e.range && e.range.getSheet().getName() !== FLUXO_ABA) return;
  sincronizarTudo();
}

function sincronizarTudo() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(25000)) return;
  try {
    var dados = lerFluxo_();
    garantirIDs_(dados);
    sincronizarNovaFabrica_(dados);
    sincronizarClientes_(dados);
  } finally {
    lock.releaseLock();
  }
}

function sincronizarNovaFabrica() { sincronizarNovaFabrica_(lerFluxo_()); }
function sincronizarClientes()    { var d = lerFluxo_(); garantirIDs_(d); sincronizarClientes_(d); }

// ── leitura do fluxo ───────────────────────────────────────────────────────

/** Acha a linha do cabeçalho ("Data" na coluna A) e devolve a primeira de dados. */
function primeiraLinhaDados_(aba) {
  var col = aba.getRange(1, 1, Math.min(aba.getLastRow(), 40), 1).getValues();
  for (var i = 0; i < col.length; i++) {
    if (String(col[i][0]).trim() === 'Data') return i + 2;
  }
  throw new Error('Não achei o cabeçalho "Data" na coluna A da aba ' + FLUXO_ABA + '.');
}

function lerFluxo_() {
  var ss  = SpreadsheetApp.getActive();
  var aba = ss.getSheetByName(FLUXO_ABA);
  if (!aba) throw new Error('Aba ' + FLUXO_ABA + ' não encontrada.');

  var ini = primeiraLinhaDados_(aba);
  var n   = Math.max(aba.getLastRow() - ini + 1, 0);
  var vals = n ? aba.getRange(ini, 1, n, FLUXO_COLS).getValues() : [];

  return { ss: ss, aba: aba, ini: ini, vals: vals, marca: 'FLUXO:' + ss.getId() + ':' };
}

/** Preenche a coluna de ID onde estiver vazia, mantendo a numeração. */
function garantirIDs_(d) {
  var maior = 0, faltam = false;
  d.vals.forEach(function (l) {
    var id = String(l[C_ID - 1] || '').trim();
    var m = id.match(/^L-(\d+)$/);
    if (m) maior = Math.max(maior, Number(m[1]));
    else if (temConteudo_(l)) faltam = true;
  });
  if (!faltam) return;

  var col = d.vals.map(function (l) {
    var id = String(l[C_ID - 1] || '').trim();
    if (id || !temConteudo_(l)) return [id];
    maior += 1;
    id = 'L-' + ('0000' + maior).slice(-4);
    l[C_ID - 1] = id;
    return [id];
  });
  d.aba.getRange(d.ini, C_ID, col.length, 1).setValues(col);
}

function temConteudo_(l) {
  return l[C_DATA - 1] !== '' && l[C_VALOR - 1] !== '';
}

// ── destino 1 · Nova Fábrica ───────────────────────────────────────────────
function sincronizarNovaFabrica_(d) {
  var novas = [];
  d.vals.forEach(function (l, i) {
    var categoria = String(l[C_CATEG - 1] || '').trim();
    if (categoria.indexOf(NF_PREFIXO) !== 0) return;
    if (String(l[C_TIPO - 1] || '').trim() !== 'Despesa') return;
    var valor = Number(l[C_VALOR - 1]) || 0;
    if (!valor) return;

    var id  = String(l[C_ID - 1] || '').trim() || ('lin' + (i + d.ini));
    var obs = String(l[C_OBS - 1] || '').trim();
    var org = 'Do fluxo de caixa · ' + d.ss.getName() + ' · ' + id;
    novas.push({
      chave: d.marca + id,
      linha: [l[C_DATA - 1], String(l[C_DESC - 1] || '').trim(),
              categoria.substring(NF_PREFIXO.length), '', 'Fábrica', 'Pago',
              Math.abs(valor), obs ? org + ' · ' + obs : org]
    });
  });

  var destino = SpreadsheetApp.openById(NF_ID).getSheetByName(NF_ABA);
  if (!destino) throw new Error('Aba ' + NF_ABA + ' não encontrada no destino.');
  escreverBloco_(destino, NF_PRIMEIRA, NF_ULTIMA - NF_PRIMEIRA + 1, 2, 8,
                 NF_COL_CHAVE, d.marca, novas);
}

// ── destino 2 · fichas de cliente ──────────────────────────────────────────
function sincronizarClientes_(d) {
  var porCliente = {};
  d.vals.forEach(function (l, i) {
    if (String(l[C_TIPO - 1] || '').trim() !== 'Despesa') return;
    var cliente = String(l[C_CLIENTE - 1] || '').trim();
    var catProj = String(l[C_CATPROJ - 1] || '').trim();
    if (!cliente || !catProj) return;
    var valor = Number(l[C_VALOR - 1]) || 0;
    if (!valor) return;

    var id = String(l[C_ID - 1] || '').trim() || ('lin' + (i + d.ini));
    (porCliente[cliente] = porCliente[cliente] || []).push({
      chave: d.marca + id,
      linha: [String(l[C_DESC - 1] || '').trim() + ' · fluxo ' + id,  // A
              catProj,                                                // B
              '',                                                     // C
              l[C_DATA - 1],                                          // D
              Math.abs(valor),                                        // E
              '',                                                     // F
              formaDePagamento_(l),                                   // G
              '',                                                     // H
              'Pago']                                                 // I
    });
  });

  var ss = SpreadsheetApp.openById(FICHA_ID);
  var abas = {};
  ss.getSheets().forEach(function (a) { abas[a.getName().trim()] = a; });

  var faltando = [];
  Object.keys(porCliente).forEach(function (cliente) {
    var aba = abas[cliente.trim()];
    if (!aba) { faltando.push(cliente); return; }
    var cab = linhaDoLivro_(aba);
    if (!cab) { faltando.push(cliente + ' (sem livro de compras)'); return; }
    escreverBloco_(aba, cab + 1, LIVRO_LINHAS, 1, 9, LIVRO_COL_CHAVE,
                   d.marca, porCliente[cliente]);
  });

  if (faltando.length) {
    d.ss.toast('Sem ficha na Gestão 2: ' + faltando.join(', '), 'Valvic', 10);
  }
}

/** O fluxo não tem coluna de forma de pagamento; deduz o que dá pela conta. */
function formaDePagamento_(l) {
  var conta = String(l[C_CONTA - 1] || '').trim();
  if (conta === 'Dinheiro (espécie)') return 'Dinheiro';
  var desc = String(l[C_DESC - 1] || '').toLowerCase();
  if (desc.indexOf('boleto') !== -1) return 'Boleto';
  if (desc.indexOf('cartão') !== -1 || desc.indexOf('fatura') !== -1) return 'Cartão de crédito';
  return 'PIX';
}

/** Acha a linha do cabeçalho do bloco 8 na ficha. */
function linhaDoLivro_(aba) {
  var col = aba.getRange(1, 1, aba.getMaxRows(), 1).getValues();
  for (var i = 0; i < col.length; i++) {
    if (String(col[i][0]).trim() === LIVRO_TITULO) return i + 1;
  }
  return 0;
}

// ── escrita comum: mantém as linhas manuais e reescreve só as nossas ───────
function escreverBloco_(aba, primeira, total, colIni, nCols, colChave, marca, novas) {
  var chaves = aba.getRange(primeira, colChave, total, 1).getValues();
  var corpo  = aba.getRange(primeira, colIni, total, nCols).getValues();

  var manuais = [];
  for (var r = 0; r < total; r++) {
    var ch = String(chaves[r][0] || '');
    if (ch.indexOf(marca) === 0) continue;               // linha nossa: será reescrita
    if (ch === '' && corpo[r].join('') === '') continue; // linha vazia
    manuais.push({ chave: ch, linha: corpo[r] });
  }

  var saida = manuais.concat(novas);
  if (saida.length > total) {
    throw new Error('O bloco de ' + aba.getName() + ' comporta ' + total +
                    ' linhas e precisaria de ' + saida.length + '.');
  }

  var vazia = [];
  for (var c = 0; c < nCols; c++) vazia.push('');

  var corpoNovo = [], chaveNova = [];
  for (var k = 0; k < total; k++) {
    corpoNovo.push(k < saida.length ? saida[k].linha : vazia.slice());
    chaveNova.push([k < saida.length ? saida[k].chave : '']);
  }

  aba.getRange(primeira, colIni, total, nCols).setValues(corpoNovo);

  var colunaChave = aba.getRange(primeira, colChave, total, 1);
  colunaChave.setValues(chaveNova);
  colunaChave.setNote('Chave de origem — preenchida pela automação. Não editar.');

  // Rede de segurança: se a coluna da chave cair dentro de uma célula mesclada, o
  // Apps Script engole a escrita sem erro e na rodada seguinte tudo duplica. Confere.
  var gravou = colunaChave.getValues();
  for (var v = 0; v < total; v++) {
    if (String(gravou[v][0] || '') !== String(chaveNova[v][0] || '')) {
      throw new Error('A chave de controle não gravou em ' + aba.getName() +
                      ', coluna ' + colChave + ' (linha ' + (primeira + v) + '). ' +
                      'Quase sempre é célula mesclada: escolha uma coluna livre.');
    }
  }
}
