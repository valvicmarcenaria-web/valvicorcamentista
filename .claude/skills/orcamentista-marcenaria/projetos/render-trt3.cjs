const {chromium}=require('/opt/node22/lib/node_modules/playwright');
const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+path.join(__dirname,'proposta-trt3.html'),{waitUntil:'networkidle'});
await p.pdf({path:path.join(__dirname,'proposta-trt3.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close();console.log('ok');})();
