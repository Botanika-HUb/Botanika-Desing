const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});
for(const id of process.argv.slice(2)){await p.goto('file://'+process.cwd()+'/'+id+'.html');await p.waitForTimeout(500);await p.screenshot({path:id+'.png'});console.log(id);}
await b.close()})();
