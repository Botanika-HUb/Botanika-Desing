// Gera os estáticos da Semana Rosa (feed 1080x1350 e story 1080x1920)
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs');
const path = require('path');

const D = __dirname;
const OUT = path.join(D, 'out');
fs.mkdirSync(OUT, { recursive: true });
const b64 = f => fs.readFileSync(path.join(D, f)).toString('base64');
const BOTTLE = 'data:image/png;base64,' + b64('rotulo1.png');
const FR = 'data:font/woff2;base64,' + b64('fr-normal.woff2');
const FRI = 'data:font/woff2;base64,' + b64('fr-italic.woff2');
const IS = w => 'data:font/ttf;base64,' + b64(`InstrumentSans-${w}.ttf`);

const ribbon = (size, color, opacity = 1) => `
<svg width="${size}" height="${size * 1.35}" viewBox="0 0 100 135" style="opacity:${opacity}">
  <path d="M50 8 C30 8 22 26 30 44 L62 118" fill="none" stroke="${color}" stroke-width="13" stroke-linecap="round"/>
  <path d="M50 8 C70 8 78 26 70 44 L38 118" fill="none" stroke="${color}" stroke-width="13" stroke-linecap="round"/>
</svg>`;

const seal = (txt1, txt2, size = 230) => `
<div class="seal" style="width:${size}px;height:${size}px">
  <div class="seal-in"><span class="s1">${txt1}</span><span class="s2">${txt2}</span></div>
</div>`;

const bottles = n => `<div class="bottles">${Array.from({ length: n }, (_, i) =>
  `<img src="${BOTTLE}" class="b${i === n - 1 ? ' last' : ''}">`).join('')}</div>`;

// Peças: texto da copy aprovada (Drive: "Semana Rosa Botanika — Copy dos criativos")
const PIECES = [
  { id: 'E01', momento: 'antecipacao', kicker: 'Semana Rosa Botanika', h: 'Outubro é sobre <em>você.</em>', sub: 'Começa segunda, 19/10', art: 'ribbon' },
  { id: 'E02', momento: 'antecipacao', kicker: 'Outubro Rosa', h: 'Cuidar de si não é luxo. <em>É rotina.</em>', sub: 'Exames em dia, rotina em dia.<br>Segunda tem novidade.', art: 'ribbon' },
  { id: 'E03', momento: 'antecipacao', kicker: 'Semana Rosa Botanika', h: 'Coloque <em>você</em> na agenda.', sub: '19 a 25/10', art: 'agenda' },
  { id: 'E04', momento: 'e-amanha', kicker: 'Semana Rosa Botanika', h: 'É <em>amanhã.</em>', sub: 'Abre segunda, 00h', art: 'ribbon', seal: ['100 primeiros', 'frete grátis'] },
  { id: 'E05', momento: 'e-amanha', kicker: 'Segunda, 00h', h: 'Meia-noite começa a <em>Semana Rosa.</em>', bullets: ['Frete grátis acima de R$ 199', 'Compre 4 suplementos, leve 5'], art: 'bottle' },
  { id: 'E06', momento: 'oferta', kicker: 'Semana Rosa Botanika', h: 'Frete grátis acima de <em>R$ 199.</em>', sub: 'Até domingo, 25/10', art: 'ribbon', seal: ['100 primeiros', 'frete grátis sem mínimo'] },
  { id: 'E07', momento: 'oferta', kicker: 'Semana Rosa', h: 'Compre 4. <em>Leve 5.</em>', sub: 'Escolha 4 suplementos: a Super Vitamina C é presente', art: 'five', seal: ['Frete grátis', 'acima de R$ 199'] },
  { id: 'E08', momento: 'oferta', kicker: 'Semana Rosa Botanika', h: 'Cuidar de você também é <em>rotina.</em>', bullets: ['Frete grátis acima de R$ 199', 'Compre 4 suplementos, leve 5'], art: 'bottle' },
  { id: 'E09', momento: 'oferta-remarketing', kicker: 'Semana Rosa Botanika', h: 'Seu carrinho ainda está <em>te esperando.</em>', sub: 'Na Semana Rosa, acima de R$ 199<br>o frete é por nossa conta.', art: 'cart' },
  { id: 'E10', momento: 'ultima-chance', kicker: 'Termina hoje, 23h59', h: 'Última <em>chance.</em>', bullets: ['Frete grátis acima de R$ 199', 'Compre 4 suplementos, leve 5'], art: 'bottle', urgent: true },
  { id: 'E11', momento: 'ultima-chance', kicker: 'Semana Rosa Botanika', h: 'Hoje à meia-noite volta tudo <em>ao normal.</em>', sub: 'Aproveite enquanto dá.', art: 'ribbon', urgent: true },
];

const css = (W, H) => `
@font-face{font-family:Fr;src:url(${FR}) format('woff2');font-weight:100 900;font-style:normal}
@font-face{font-family:Fr;src:url(${FRI}) format('woff2');font-weight:100 900;font-style:italic}
@font-face{font-family:IS;src:url(${IS('Regular')});font-weight:400}
@font-face{font-family:IS;src:url(${IS('SemiBold')});font-weight:600}
@font-face{font-family:IS;src:url(${IS('Bold')});font-weight:700}
:root{--rose:#C23B6B;--deep:#6E1A3D;--blush:#F8E6E8;--blush2:#F1C9D2;--cream:#FFF9F6;--navy:#14235F}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:${W}px;height:${H}px;overflow:hidden}
body{font-family:IS,sans-serif;color:var(--deep);
  background:radial-gradient(120% 80% at 85% 10%,#fff 0%,var(--blush) 45%,var(--blush2) 100%);position:relative}
body.urgent{background:radial-gradient(120% 80% at 85% 10%,#E35A88 0%,var(--rose) 40%,var(--deep) 100%);color:var(--cream)}
.grain{position:absolute;inset:0;opacity:.06;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence baseFrequency='.9' numOctaves='2'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.arc{position:absolute;border-radius:50%;border:2px solid rgba(194,59,107,.18)}
body.urgent .arc{border-color:rgba(255,255,255,.18)}
.wrap{position:absolute;inset:0;padding:${H > 1500 ? '210px 90px 230px' : '90px 90px 80px'};display:flex;flex-direction:column}
.kicker{font-weight:600;letter-spacing:.22em;text-transform:uppercase;font-size:26px;color:var(--rose);display:flex;align-items:center;gap:16px}
.kicker:before{content:"";width:46px;height:3px;background:currentColor;border-radius:2px}
body.urgent .kicker{color:#FFD3E0}
h1{font-family:Fr,serif;font-weight:560;font-variation-settings:"opsz" 144;font-size:${H > 1500 ? 112 : 100}px;line-height:1.02;letter-spacing:-.02em;margin-top:34px;max-width:${W - 180}px}
h1 em{font-style:italic;font-weight:500;color:var(--rose)}
body.urgent h1 em{color:#FFD3E0}
.sub{font-size:38px;line-height:1.3;margin-top:30px;opacity:.85}
ul{list-style:none;margin-top:34px;display:flex;flex-direction:column;gap:16px}
li{font-size:34px;font-weight:600;display:flex;align-items:center;gap:18px}
li:before{content:"";width:16px;height:16px;border-radius:50%;background:var(--rose);flex:none}
body.urgent li:before{background:#FFD3E0}
.art{flex:1;position:relative;display:flex;align-items:flex-end;justify-content:center;min-height:0}
.art img.bottle{height:100%;max-height:${H > 1500 ? 820 : 560}px;object-fit:contain;filter:drop-shadow(0 40px 50px rgba(110,26,61,.35))}
.bottles{display:flex;align-items:flex-end;justify-content:center;height:100%;max-height:${H > 1500 ? 560 : 420}px}
.bottles img{height:${H > 1500 ? 320 : 280}px;margin:0 -26px;filter:drop-shadow(0 26px 30px rgba(110,26,61,.3))}
.bottles img.last{height:${H > 1500 ? 370 : 330}px;outline:0;filter:drop-shadow(0 0 0 #fff) drop-shadow(0 30px 34px rgba(194,59,107,.55))}
.plus{position:absolute;right:90px;bottom:${H > 1500 ? 400 : 350}px;background:var(--rose);color:#fff;font-weight:700;font-size:30px;padding:12px 24px;border-radius:40px;letter-spacing:.04em}
.seal{position:absolute;right:0;top:${H > 1500 ? 40 : 10}px;z-index:2;border-radius:50%;background:var(--rose);color:#fff;display:flex;align-items:center;justify-content:center;transform:rotate(8deg);box-shadow:0 18px 40px rgba(110,26,61,.3)}
.seal:after{content:"";position:absolute;inset:10px;border:2px dashed rgba(255,255,255,.6);border-radius:50%}
.seal-in{text-align:center;display:flex;flex-direction:column;padding:0 26px}
.s1{font-family:Fr,serif;font-size:36px;font-weight:600;line-height:1}
.s2{font-size:21px;font-weight:600;text-transform:uppercase;letter-spacing:.08em;margin-top:8px;line-height:1.2}
.foot{display:flex;justify-content:space-between;align-items:center;margin-top:36px;font-size:24px;letter-spacing:.14em;text-transform:uppercase;font-weight:600}
.logo{font-family:IS;font-weight:700;font-size:40px;letter-spacing:-.01em;text-transform:none;color:var(--navy)}
body.urgent .logo{color:#fff}
.agenda{width:460px;background:var(--cream);border-radius:28px;box-shadow:0 30px 60px rgba(110,26,61,.2);overflow:hidden;font-family:IS}
.agenda .top{background:var(--rose);color:#fff;padding:20px 30px;font-weight:700;font-size:28px;letter-spacing:.12em;text-transform:uppercase}
.agenda .row{display:flex;gap:20px;padding:20px 30px;border-bottom:1px solid #f0d9de;font-size:28px;align-items:center}
.agenda .row b{color:var(--rose);width:70px}
.agenda .row.me{background:#FCE9EE;font-weight:700}
.cart{width:420px;background:var(--cream);border-radius:28px;padding:34px;box-shadow:0 30px 60px rgba(110,26,61,.2);display:flex;gap:26px;align-items:center}
.cart img{height:170px}
.cart .t{font-size:28px;font-weight:700;color:var(--deep)}
.cart .f{margin-top:12px;font-size:24px;color:var(--rose);font-weight:700}
`;

function html(p, W, H) {
  let art = '';
  if (p.art === 'ribbon') art = `<div class="art" style="align-items:center">${ribbon(H > 1500 ? 380 : 260, p.urgent ? '#FFD3E0' : '#C23B6B', p.urgent ? .9 : 1)}</div>`;
  if (p.art === 'bottle') art = `<div class="art"><img class="bottle" src="${BOTTLE}"></div>`;
  if (p.art === 'five') art = `<div class="art">${bottles(5)}<div class="plus">+1 de presente</div></div>`;
  if (p.art === 'agenda') art = `<div class="art" style="align-items:center"><div class="agenda"><div class="top">Outubro</div>
    <div class="row"><b>09h</b>Reunião</div><div class="row"><b>12h</b>Mercado</div>
    <div class="row me"><b>19h</b>Eu 🎀</div><div class="row"><b>20h</b>Exame em dia ✓</div></div></div>`;
  if (p.art === 'cart') art = `<div class="art" style="align-items:center"><div class="cart"><img src="${BOTTLE}"><div>
    <div class="t">Super Vitamina C</div><div class="t" style="font-weight:400;font-size:24px;margin-top:6px">no seu carrinho</div>
    <div class="f">Frete: R$ 0,00</div></div></div></div>`;
  const body = `
  <div class="grain"></div>
  <div class="arc" style="width:${W * 1.2}px;height:${W * 1.2}px;right:-${W * .55}px;top:-${W * .5}px"></div>
  <div class="arc" style="width:${W * .9}px;height:${W * .9}px;left:-${W * .5}px;bottom:-${W * .35}px"></div>
  <div class="wrap">
    <div class="kicker">${p.kicker}</div>
    <h1>${p.h}</h1>
    ${p.sub ? `<div class="sub">${p.sub}</div>` : ''}
    ${p.bullets ? `<ul>${p.bullets.map(b => `<li>${b}</li>`).join('')}</ul>` : ''}
    ${art.replace(/<\/div>$/, (p.seal ? seal(p.seal[0], p.seal[1], H > 1500 ? 250 : 210) : '') + '</div>')}
    <div class="foot"><span class="logo">botanika</span><span>${p.urgent ? 'Até hoje, 23h59' : (p.momento.startsWith('oferta') ? 'Até 25/10' : 'Semana Rosa · 19 a 25/10')}</span></div>
  </div>`;
  return `<!doctype html><html><head><meta charset="utf-8"><style>${css(W, H)}</style></head><body class="${p.urgent ? 'urgent' : ''}">${body}</body></html>`;
}

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const only = process.argv[2];
  for (const p of PIECES) {
    if (only && !p.id.startsWith(only)) continue;
    for (const [fmt, W, H] of [['feed', 1080, 1350], ['story', 1080, 1920]]) {
      const page = await browser.newPage({ viewport: { width: W, height: H } });
      await page.setContent(html(p, W, H), { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      const file = path.join(OUT, `SemanaRosa_${p.id}_${p.momento}_${fmt}.png`);
      await page.screenshot({ path: file });
      await page.close();
      console.log(path.basename(file));
    }
  }
  await browser.close();
})();
