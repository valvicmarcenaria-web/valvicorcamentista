const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage();
  await p.goto('file://' + __dirname + '/comunicado-comissoes-projeto.html', { waitUntil:'networkidle', timeout:60000 });
  try { await p.evaluate(() => document.fonts.ready); } catch(e) {}
  const m = await p.evaluate(() => [...document.querySelectorAll('.body')].map((b,i) =>
    ({ folha:i+1, altura:b.clientHeight, conteudo:b.scrollHeight, transborda:b.scrollHeight-b.clientHeight })));
  m.forEach(x => console.log('folha '+x.folha+': '+(x.transborda>1 ? ('TRANSBORDA '+x.transborda+'px') : 'cabe')+'  ('+x.conteudo+'/'+x.altura+'px)'));
  await p.pdf({ path: __dirname + '/Valvic_Comunicado_Comissoes_Projeto.pdf', format:'A4', printBackground:true, margin:{top:0,right:0,bottom:0,left:0} });
  await b.close();
})();
