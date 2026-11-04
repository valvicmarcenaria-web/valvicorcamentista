const path=require('path');
const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.join(__dirname,'proposta-porto-verde-v2.html'),{waitUntil:'networkidle'});
await p.pdf({path:path.join(__dirname,'proposta-porto-verde-v2.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close();console.log('ok');})();
