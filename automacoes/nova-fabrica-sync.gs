/**
 * Valvic · espelho automático do fluxo de caixa na aba "Nova Fábrica".
 *
 * Instalar NA PLANILHA DE FLUXO DE CAIXA DO MÊS (a da pasta da Kelly).
 * Extensões → Apps Script → cole este arquivo → salve.
 * Depois rode uma vez a função instalarGatilhos() e autorize.
 *
 * O que faz: toda linha de LANCAMENTOS cuja Categoria comece por
 * "Nova Fábrica · " é copiada para a aba "Nova Fábrica" da planilha
 * N.GESTAO 3. Editou a linha no fluxo, a linha de lá se atualiza.
 * Apagou ou trocou a categoria, a linha de lá some. Não duplica:
 * cada linha carrega uma chave de origem na coluna K.
 */

var DESTINO_ID   = '1-7XUrVso9oVKccQjM2m5Tgd9_-QIk-r1LZ8XZbDnGL0';
var DESTINO_ABA  = 'Nova Fábrica';
var ORIGEM_ABA   = 'LANCAMENTOS';
var PREFIXO      = 'Nova Fábrica · ';
var PRIMEIRA_LIN = 31;   // primeira linha da tabela de compras no destino
var ULTIMA_LIN   = 600;  // última linha coberta pelas fórmulas dos quadros
var COL_CHAVE    = 11;   // coluna K do destino, fora dos quadros

function instalarGatilhos() {
  var id = SpreadsheetApp.getActive().getId();
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'aoEditar') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('aoEditar').forSpreadsheet(id).onEdit().create();
  sincronizarTudo();
  SpreadsheetApp.getActive().toast('Automação instalada e sincronizada.', 'Nova Fábrica', 8);
}

function aoEditar(e) {
  if (!e || !e.range) return sincronizarTudo();
  if (e.range.getSheet().getName() !== ORIGEM_ABA) return;
  sincronizarTudo();
}

/** Menu manual, para rodar à mão quando quiser. */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Valvic')
    .addItem('Sincronizar Nova Fábrica agora', 'sincronizarTudo')
    .addItem('Instalar automação', 'instalarGatilhos')
    .addToUi();
}

function sincronizarTudo() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) return;
  try {
    var origem  = SpreadsheetApp.getActive();
    var abaOrig = origem.getSheetByName(ORIGEM_ABA);
    if (!abaOrig) throw new Error('Aba ' + ORIGEM_ABA + ' não encontrada.');

    var dados = abaOrig.getRange(2, 1, Math.max(abaOrig.getLastRow() - 1, 1), 9).getValues();
    var marca = 'FLUXO:' + origem.getId() + ':';

    // Linhas do fluxo que pertencem à nova fábrica, na ordem em que estão.
    var novas = [];
    for (var i = 0; i < dados.length; i++) {
      var l = dados[i];
      var categoria = String(l[3] || '').trim();
      if (categoria.indexOf(PREFIXO) !== 0) continue;
      if (String(l[1] || '').trim() !== 'Despesa') continue;
      var valor = Number(l[5]) || 0;
      if (!valor) continue;

      var obs = String(l[8] || '').trim();
      var origemTxt = 'Do fluxo de caixa · ' + origem.getName() + ' · linha ' + (i + 2);
      novas.push({
        chave: marca + (i + 2),
        linha: [
          l[0],                                 // B Data
          String(l[2] || '').trim(),            // C Item / material
          categoria.substring(PREFIXO.length),  // D Categoria
          '',                                   // E Fornecedor
          'Fábrica',                            // F Quem paga
          'Pago',                               // G Situação
          Math.abs(valor),                      // H Valor
          obs ? origemTxt + ' · ' + obs : origemTxt // I Observação
        ]
      });
    }

    var destino = SpreadsheetApp.openById(DESTINO_ID).getSheetByName(DESTINO_ABA);
    if (!destino) throw new Error('Aba ' + DESTINO_ABA + ' não encontrada no destino.');

    var total   = ULTIMA_LIN - PRIMEIRA_LIN + 1;
    var chaves  = destino.getRange(PRIMEIRA_LIN, COL_CHAVE, total, 1).getValues();
    var corpo   = destino.getRange(PRIMEIRA_LIN, 2, total, 8).getValues();

    // Mantém intactas as linhas digitadas à mão (sem chave desta origem).
    var manuais = [];
    for (var r = 0; r < total; r++) {
      var ch = String(chaves[r][0] || '');
      if (ch.indexOf(marca) === 0) continue;          // linha nossa: será reescrita
      if (ch === '' && corpo[r].join('') === '') continue; // linha vazia
      manuais.push({ chave: ch, linha: corpo[r] });
    }

    var saida = manuais.concat(novas);
    if (saida.length > total) throw new Error('Mais linhas do que a tabela comporta.');

    var corpoNovo  = [];
    var chaveNova  = [];
    for (var k = 0; k < total; k++) {
      corpoNovo.push(k < saida.length ? saida[k].linha : ['', '', '', '', '', '', '', '']);
      chaveNova.push([k < saida.length ? saida[k].chave : '']);
    }

    destino.getRange(PRIMEIRA_LIN, 2, total, 8).setValues(corpoNovo);
    destino.getRange(PRIMEIRA_LIN, COL_CHAVE, total, 1).setValues(chaveNova);
    destino.getRange(PRIMEIRA_LIN, COL_CHAVE, total, 1).setNote(
      'Chave de origem — preenchida pela automação. Não editar.');
  } finally {
    lock.releaseLock();
  }
}
