// Renderiza um HTML em PDF A4 sem margem, com o Chromium do container.
//
// ⛔ ESTE ARQUIVO MORAVA EM /tmp/r.js, E /tmp NÃO SOBREVIVE AO CONTAINER
//   [30/10/2026]. Numa sessão nova o build da proposta da Eliza morria no
//   `node: cannot find module`. ⭐ Entrada de build é arquivo do repositório.
//
// ⭐ E AGORA OS CAMINHOS SÃO ARGUMENTO, não constante: a versão de /tmp
//   lia `file:///tmp/in.html` cravado dentro do código, então dois builds
//   na mesma sessão disputavam o mesmo arquivo temporário.
//
//   uso:  NODE_PATH=/opt/node22/lib/node_modules node render-pdf.js ent.html sai.pdf
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [ent, sai] = process.argv.slice(2);
  if (!ent || !sai) { console.error('uso: render-pdf.js <entrada.html> <saida.pdf>'); process.exit(1); }
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(ent), { waitUntil: 'networkidle' });
  await p.waitForTimeout(2500);
  await p.pdf({ path: sai, format: 'A4', printBackground: true,
                margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await b.close();
})();
