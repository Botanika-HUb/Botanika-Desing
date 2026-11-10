const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const [h,f] of [['oferta','banner-live_oferta_08h-20h.png'],['uc','banner-live_ultima-chance_20h-00h.png']]){await p.goto('file://'+__dirname+'/banner.html#'+h);await p.reload();await p.waitForTimeout(600);await p.screenshot({path:__dirname+'/'+f});}
await b.close();})();
