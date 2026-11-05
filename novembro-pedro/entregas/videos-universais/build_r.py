"""Vídeos universais da Black · roteiros completos (05/11), todos com a Mafe.
Ordem de cada roteiro: gancho (IMG_9671) → identificação (IMG_9673) → frase da Black (IMG_9667) → chamada final do roteiro (IMG_9674, cenário roxo).
O roteiro 2 (Sleep) usa o corpo inteiro do IMG_9668. O roteiro 5 não tem gancho gravado: abre na identificação.
Na frase da Black saiu o trecho "e não é só ele", que só fazia sentido no vídeo do Tri-Magnésio.
Brutos HDR (HLG) → SDR com tone mapping (hable); trechos já convertidos em <dupla>/mids (clips.json diz de onde vem cada um).
Uso: python3 build_r.py <roteiro> <pasta uni> <pasta dupla>
"""
import json, subprocess, sys, os
import numpy as np
D = os.path.dirname(os.path.abspath(__file__))
k = sys.argv[1]; W = sys.argv[2]; DU = sys.argv[3]; BR = W + '/../brutos'
def run(c): subprocess.run(c, check=True)
CL = json.load(open(DU + '/clips.json'))
OFF = 3.9  # body_mid.mp4 começa em 3,9 s do IMG_9667
HOOK = {  # IMG_9671 (hooks_mid, mesmo tempo): fala, texto, gancho na tela
 '3': (28.22, 31.37, "Você dorme rápido e acorda às 3 da manhã sem motivo nenhum?", ['Acorda às 3h', 'sem motivo?'], ['3h']),
 '4': (38.27, 41.24, "Você entra no trabalho de dia e só sai quando o sol já foi embora?", ['Sai do trabalho', 'já de noite?'], ['noite?']),
 '6': (49.08, 52.45, "O site inteiro da Botanika tá em promoção. Inteiro mesmo!", ['O site inteiro', 'em promoção'], ['inteiro']),
 '7': (67.56, 71.77, "Os suplementos que o médico integrativo Dr. William indica estão todos em promoção.", ['A linha que o', 'Dr. William indica'], ['William']),
 '8': (78.38, 81.51, "Se você já é cliente da Botanika, para tudo e escuta isso aqui!", ['Já é cliente?', 'Para tudo'], ['cliente?']),
 '9': (88.73, 92.32, "Se você nunca comprou na Botanika, essa é a hora de conhecer!", ['Nunca comprou', 'na Botanika?'], ['Nunca']),
 '10': (105.51, 108.86, "Black Friday de suplemento vale mais que qualquer outra!", ['Black de', 'suplemento'], ['suplemento']),
 '11': (115.78, 119.11, "Essa é a última chance do ano de montar seu kit de suplementos!", ['Última chance', 'do ano'], ['ano']),
 '12': (124.61, 126.81, "Olha o seu potinho aí. Já tá no fim?", ['Seu pote', 'tá no fim?'], ['fim?']),
 '13': (134.97, 138.78, "Se você já entrou no site da Botanika e saiu sem comprar, essa é a sua hora!", ['Entrou e saiu', 'sem comprar?'], ['comprar?']),
 '14': (145.44, 148.02, "Você já conhece os novos produtos que a Botanika lançou?", ['Já conhece os', 'lançamentos?'], ['lançamentos?']),
 '15': (154.59, 157.39, "Todos os suplementos da Botanika acabaram de baixar de preço!", ['Tudo', 'baixou de preço'], ['preço']),
 '16': (164.69, 168.48, "Se você tava adiando sua compra por causa do preço, acabou a sua desculpa!", ['Acabou a', 'desculpa'], ['desculpa']),
}
IDENT = {  # IMG_9673 (textos conferidos pela transcrição de 05/11)
 '3': "Eu acordava, ficava calculando quantas horas faltavam e aí piorava.",
 '4': "Eu não lembrava a última vez que tinha tomado sol de verdade.",
 '5': "Gastei uma fortuna em ampola, salão, shampoo caro, sempre achando que o próximo ia ser o certo.",
 '6': "Se você toma suplemento ou tava pensando em começar, essa notícia é pra você.",
 '7': "Se você acompanha ele, já viu ele falando de magnésio, ômega ou vitamina D, ou falando sobre montar uma suplementação que faça sentido.",
 '8': "Você que já tem o seu favorito, já sabe o que funciona pra você e sempre repõe um de cada vez?",
 '9': "Eu sei que trocar de marca de suplemento dá uma insegurança, porque você nunca sabe se vai valer tanto quanto custa.",
 '10': "Sabe por quê? Porque não é uma coisa que você compra por impulso, é uma coisa que você já usa, vai acabar e você vai ter que repor de todo jeito.",
 '11': "E eu digo última porque com um valor desse não vai aparecer de novo tão cedo.",
 '12': "Se tá, não compra ainda, espera eu te contar uma coisa.",
 '13': "Eu sei que você olhou, achou interessante, mas deixou pra depois. Todo mundo faz isso.",
 '14': "Pouca gente viu, porque lançamento sempre passa batido no meio do feed.",
 '15': "Todos mesmo! Não é uma seleção de dois ou três produtos, é o site inteiro!",
 '16': "Eu já esperei condição boa aparecer e já deixei passar algumas que eu devia ter pego.",
}
CTA = json.load(open(DU + '/cta.json'))  # IMG_9674: texto da chamada de cada roteiro
# v2 (05/11): a frase vai inteira. Cortar o "e não é só ele" deixava o corte no meio da fala (o Otávio apontou).
BLACK = [((78.42, 83.45), "E agora a Black da Botanika tá rolando, e não é só ele: o site inteiro tá com condição especial o mês todo.")]
SLEEP = [('s1', "Tá exausta e a cabeça continua ligada?"), ('s2', "Celular longe, chá, horário fixo, fiz a lista toda da internet e nada funcionou."),
         ('s3', "Desacelerar à noite é algo que o seu corpo já faz, mas pra fazer isso com excelência, ele precisa de algo."),
         ('s4', "Nenhum chá entrega isso."), ('s5', "Comecei a usar o Sleep da Botanika e tem me ajudado muito nessa parte.")]
END = 2.4
HOT = ['black', 'inteiro', 'especial', 'promoção', 'botão', 'sleep', 'magnésio', 'suplementação']

def speech(path, a, b):
    """trechos de fala (-42 dB, janelas de 10 ms) dentro de [a, b] do arquivo"""
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{a:.3f}', '-t', f'{b - a:.3f}', '-i', path, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(float) / 32768; w = 160; n = len(x) // w
    e = 20 * np.log10(np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(1)) + 1e-9); on = e > -42
    segs = []; s = None
    for i, v in enumerate(on):
        if v and s is None: s = i
        if not v and s is not None: segs.append([s, i]); s = None
    if s is not None: segs.append([s, n])
    m = []
    for p, q in segs:
        if m and p - m[-1][1] < 12: m[-1][1] = q
        else: m.append([p, q])
    m = [(a + p / 100, a + q / 100) for p, q in m if q - p > 5]
    return m or [(a, b)]

def refine(path, a, b, lo=0.0):
    """leva o início e o fim até o silêncio de verdade (-50 dB por 80 ms), com no máximo 0,35 s a mais de cada lado"""
    s0 = max(lo, a - 0.4)
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{s0:.3f}', '-t', f'{b - s0 + 0.5:.3f}', '-i', path, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(float) / 32768; w = 160; n = len(x) // w
    e = 20 * np.log10(np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(1)) + 1e-9)
    ia = int(round((a - s0) * 100)); ib = int(round((b - s0) * 100))
    i = ia
    while i > 0 and ia - i < 35 and e[i - 1] > -50: i -= 1
    j = ib; quiet = 0
    while j < n and j - ib < 35:
        quiet = quiet + 1 if e[j] < -50 else 0
        if quiet >= 8: j -= 7; break
        j += 1
    return s0 + i / 100 - 0.04, s0 + j / 100 + 0.06

def mid(key):  # trecho convertido: arquivo, onde começa a fala, onde termina
    src, a, b = CL[key]; s = max(0, a - 0.5)
    return f'{DU}/mids/{key}.mp4', a - s, b - s

SEGS = []  # (arquivo, (corte_a, corte_b), texto)
if k == '2':
    for key, tx in SLEEP:
        f, a, b = mid(key); SEGS.append((f, refine(f, a, b), tx))
    hook = dict(lines=['A cabeça', 'não desliga?'], em=['desliga?'])
else:
    if k in HOOK:
        a, b, tx, l, em = HOOK[k]; SEGS.append((f'{BR}/hooks_mid.mp4', (a - 0.06, b + 0.10), tx)); hook = dict(lines=l, em=em)
    else:
        hook = dict(lines=['Gastou uma fortuna', 'em ampola?'], em=['fortuna'])
    f, a, b = mid('i' + k); SEGS.append((f, refine(f, a, b), IDENT[k]))
for (a, b), tx in BLACK: SEGS.append((f'{BR}/body_mid.mp4', refine(f'{BR}/body_mid.mp4', a - OFF, b - OFF), tx))
f, a, b = mid('c' + k); ca, cb, ctx = CTA[k]; SEGS.append((f, refine(f, a + ca, a + cb) if ca is not None else refine(f, a, b), ctx))

words = []; acc = 0; cuts = []
for f, (a, b), tx in SEGS:
    sp = [(max(p, a) - a + acc, min(q, b) - a + acc) for p, q in speech(f, a, b)]
    ws = tx.split(); wt = [len(w) + 2 for w in ws]; sw = sum(wt); tot = sum(q - p for p, q in sp)
    def at(x):
        x *= tot
        for p, q in sp:
            if x <= q - p: return p + x
            x -= q - p
        return sp[-1][1]
    c = 0
    for w, q in zip(ws, wt): words.append(dict(t=round(at(c / sw), 3), w=w)); c += q
    acc += b - a; cuts.append(round(acc, 3))
main = round(acc, 3); dur = round(main + END, 2)
first = SEGS[0][1]; hook_end = first[1] - first[0]
blk = next(x['t'] for x in words if x['w'] == 'Black' and x['t'] >= cuts[-3] - 0.01)
scenes = [dict(kind='black', a=round(blk - 0.15, 3), b=round(blk + 1.9, 3))]
if k == '2':
    sl = next(x['t'] for x in words if x['w'] == 'Sleep')
    scenes.insert(0, dict(kind='prod', a=round(sl - 0.1, 3), b=round(sl + 1.5, 3), name='SLEEP<br>BOTANIKA', sub='pra desacelerar à noite', img='sleep.png'))
cta_a = cuts[-2]
hk = dict(hook, a=0.0, b=round(min(3.2, hook_end), 2))
cfg = dict(hook=hk, words=words, cuts=cuts, scenes=scenes, hot=HOT, cta=dict(a=cta_a, b=main), end=main, dur=dur)
json.dump(cfg, open(f'{W}/cfg_r{k}.json', 'w'), ensure_ascii=False)
fr = f'{W}/frames_r{k}'
if not os.path.exists(fr + '/f00000.png'): run(['node', D + '/render_u.js', f'{W}/cfg_r{k}.json', fr, W])
terms = []; acc = 0
for i, (f, (a, b), _) in enumerate(SEGS):
    if i % 2: terms.append(f"0.07*between(it,{acc:.3f},{acc + b - a:.3f})")
    acc += b - a
for t0 in [0.3, blk - 0.1, cta_a + 0.1]:
    terms.append(f"0.12*clip((it-{t0 - 0.12:.3f})/0.12,0,1)*clip(({t0 + 1.0:.3f}-it)/0.25,0,1)")
z = '1+' + '+'.join(terms)
inp = []; fc = []; n = len(SEGS)
for i, (f, (a, b), _) in enumerate(SEGS):
    inp += ['-ss', f'{a:.3f}', '-t', f'{b - a:.3f}', '-i', f]
    fc.append(f"[{i}:v]scale=1080:1920,setsar=1,fps=30,setpts=PTS-STARTPTS[v{i}];[{i}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={b - a - 0.03:.3f}:d=0.03[a{i}];")
fc.append(''.join(f'[v{i}][a{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=1[vc0][ac0];')
fc.append(f"[vc0]zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih*0.4-(ih/zoom*0.4)':d=1:s=1080x1920:fps=30,setsar=1[vz];")
fc.append(f"color=c=0x0b0b0f:s=1080x1920:r=30:d={END},setsar=1[vend];anullsrc=r=48000:cl=stereo,atrim=0:{END}[aend];[vz][ac0][vend][aend]concat=n=2:v=1:a=1[vc][ac];")
o = n; inp += ['-reinit_filter', '0', '-framerate', '30', '-i', fr + '/f%05d.png']
fc.append(f"[{o}:v]format=rgba[ov];[vc][ov]overlay=0:0:format=auto,format=yuv420p[vout];")
sfx = [('whoosh', s['a'] - 0.08) for s in scenes] + [('pop', cta_a), ('whoosh', main - 0.1)]
labs = []
for q, (nm, t) in enumerate(sfx):
    idx = o + 1 + q; inp += ['-i', f'{W}/{nm}.wav']; ms = int(max(0, t) * 1000)
    fc.append(f"[{idx}:a]adelay={ms}|{ms},volume={0.22 if nm == 'pop' else 0.3}[s{q}];"); labs.append(f'[s{q}]')
fc.append(f"[ac]loudnorm=I=-15:TP=-2:LRA=11,aresample=48000[voz];[voz]{''.join(labs)}amix=inputs={len(labs) + 1}:normalize=0:duration=first,alimiter=limit=0.89[aout]")
out = f'{W}/Roteiro{int(k):02d}.mp4'
run(['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', ''.join(fc), '-map', '[vout]', '-map', '[aout]', '-r', '30', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out])
print(out, dur)
