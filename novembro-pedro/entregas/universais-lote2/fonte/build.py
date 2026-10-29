import json, sys, os
S = os.path.abspath('..')
H = {'sleep':0.80,'tri':1.0,'omega':1.04,'hair':1.0,'vitc':1.0,'coq10':1.0,'nac':1.0,'msm':1.0,'cran':1.0,'flexia':1.0,'whey':1.22,'crea':0.92,'tetra':0.86}
def page(p):
    n = len(p['prods'])
    base = {1:540,2:470,3:380,4:330,5:290,6:260}[min(n,6)]
    imgs = ''.join(f'<img src="file://{S}/cut/{k}.png" style="height:{int(base*H[k])}px">' for k in p['prods'])
    t1, t2 = p['title']
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:I;src:url(file://{S}/kit/InstrumentSans-Regular.woff2);font-weight:400}}
@font-face{{font-family:I;src:url(file://{S}/kit/InstrumentSans-Medium.woff2);font-weight:500}}
@font-face{{font-family:I;src:url(file://{S}/kit/InstrumentSans-SemiBold.woff2);font-weight:600 800}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1350px;background:#fff;font-family:I,sans-serif;color:#091b5d;overflow:hidden;position:relative}}
.bar{{background:#e3132b;color:#fff;text-align:center;font-weight:700;font-size:22px;letter-spacing:.14em;padding:16px 0;text-transform:uppercase}}
.bar i{{display:inline-block;width:11px;height:11px;border-radius:50%;background:#fff;margin-right:14px;vertical-align:2px}}
.top{{display:flex;justify-content:center;padding:34px 0 0}}
.top img{{height:46px}}
.wrap{{padding:0 70px;text-align:center}}
.chip{{display:inline-block;margin-top:28px;background:#ffe9ec;color:#b80d20;font-weight:700;font-size:22px;letter-spacing:.1em;padding:12px 24px;border-radius:99px;text-transform:uppercase}}
h1{{font-size:{p.get('fs',78)}px;line-height:1.02;letter-spacing:-.03em;font-weight:700;color:#0c298d;margin:24px 0 18px}}
h1 em{{font-style:normal;color:#e3132b}}
.sub{{font-size:30px;color:#55608a;font-weight:500}}
.sub b{{color:#091b5d;font-weight:700}}
.arch{{position:absolute;left:110px;right:110px;bottom:200px;height:{p.get('ah',560)}px;border-radius:430px 430px 36px 36px;background:radial-gradient(120% 90% at 50% 15%,#2e53df 0,#0c298d 62%,#091b5d 100%);overflow:hidden}}
.arch:after{{content:"";position:absolute;left:8%;right:8%;bottom:38px;height:70px;border-radius:50%;background:radial-gradient(closest-side,#c8f14b99,transparent)}}
.prods{{position:absolute;left:0;right:0;bottom:256px;display:flex;justify-content:center;align-items:flex-end;gap:{p.get('gap',8)}px;z-index:2}}
.prods img{{filter:drop-shadow(0 18px 22px rgba(0,0,0,.45))}}
.tag{{position:absolute;right:86px;bottom:{p.get('ah',560)+150}px;background:#e3132b;color:#fff;font-weight:800;font-size:22px;line-height:1.1;text-transform:uppercase;letter-spacing:.06em;padding:14px 20px;border-radius:16px;transform:rotate(6deg);box-shadow:0 14px 30px -10px #e3132b;text-align:center;z-index:3}}
.tag b{{display:block;font-size:34px;letter-spacing:-.01em}}
.cap{{position:absolute;left:0;right:0;bottom:150px;text-align:center;font-size:24px;color:#55608a;font-weight:500}}
.cap b{{color:#091b5d}}
.cta{{position:absolute;left:50%;transform:translateX(-50%);bottom:52px;background:#e3132b;color:#fff;font-weight:700;font-size:34px;padding:24px 64px;border-radius:99px;box-shadow:0 16px 34px -12px #e3132bcc;white-space:nowrap}}
</style></head><body>
<div class="bar"><i></i>Botanika November</div>
<div class="top"><img src="file://{S}/kit/logo-c.png"></div>
<div class="wrap">
<span class="chip">{p.get('chip','🔥 O mês da sua rotina')}</span>
<h1>{t1}<br><em>{t2}</em></h1>
<p class="sub">O maior desconto da <b>história da Botanika.</b></p>
</div>
<div class="arch"></div><div class="prods">{imgs}</div>
{('<div class="tag">'+p['tag'][0]+'<b>'+p['tag'][1]+'</b></div>') if p.get('tag') else ''}
<p class="cap">{p['cap']}</p>
<div class="cta">Aproveitar agora</div>
</body></html>'''
P = json.load(open('pecas.json'))
for p in P:
    open(f"{p['id']}.html",'w').write(page(p))
print('ok', len(P))
