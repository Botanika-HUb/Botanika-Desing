"""Criativo da creator Anna Luiza (Esquenta 11/11), no estilo aprovado da v3 dos vídeos do Esquenta.
Bruto: "Creator Anna Luiza | Esquenta Botanika.mov" (Otávio, 05/11), 28,5 s, 4K SDR.
A fala foi medida na onda do áudio (-42 dB, janelas de 10 ms). O texto foi reconstruído da transcrição.
Uso: python3 build_anna.py <pasta de trabalho>  (precisa de anna_mid.mp4, fontes, png e wav na pasta)
"""
import json, subprocess, sys, os
D = os.path.dirname(os.path.abspath(__file__)); W = sys.argv[1]
def run(c): subprocess.run(c, check=True)
# trechos mantidos no bruto: tiram as pausas de 0,3 s ou mais
KEEPS = [(0.18, 4.90), (5.18, 13.50), (13.80, 15.70), (16.00, 18.48), (18.70, 27.95)]
# (trechos de fala no bruto, frase) — a palavra cai proporcional ao tamanho falado, dentro da fala
FRASES = [
 ([(0.24, 0.60), (0.72, 1.61)], "Montei meu kit de suplementos"),
 ([(1.91, 3.06)], "com 12% de desconto"),
 ([(3.22, 3.95)], "e o melhor:"),
 ([(4.30, 4.81)], "sem pagar frete."),
 ([(5.26, 5.96), (6.15, 6.30), (6.43, 6.60), (6.80, 7.15), (7.34, 8.35)], "Eu comprava um pote por mês e pagava frete toda vez."),
 ([(8.49, 8.64), (8.77, 9.37), (9.53, 11.18)], "No fim do mês, já tinha gastado mais do que devia."),
 ([(11.35, 12.38), (12.62, 12.70), (13.00, 13.11), (13.24, 13.39)], "Agora a Botanika tá dando desconto por quantidade."),
 ([(13.88, 15.40)], "Quanto mais você leva, maior o desconto."),
 ([(16.08, 16.25), (16.40, 16.80), (16.95, 17.19), (17.32, 17.47), (17.63, 17.80), (17.97, 18.39)], "Até 12% a partir de 5 unidades."),
 ([(18.77, 19.32), (19.44, 20.18), (20.40, 21.12), (21.39, 22.39)], "Montei meu kit com o Hair, a Creatina e o Super Ômega 3,"),
 ([(22.74, 23.61), (23.83, 25.81)], "o frete saiu grátis e ainda ganhei um cranberry porque passou de 400."),
 ([(26.27, 27.81)], "Monte o seu agora clicando aqui embaixo."),
]
FALADO = {'12%': 'dozeporcento', '5': 'cinco', '3': 'três', '400': 'quatrocentos'}
END = 2.4
def remap(t):
    acc = 0
    for a, b in KEEPS:
        if t < a: return acc
        if t <= b: return acc + t - a
        acc += b - a
    return acc
R = lambda t: round(remap(t), 3)
words = []
for sp, tx in FRASES:
    ws = tx.split(); wt = [len(FALADO.get(w.strip('.,:'), w)) + 2 for w in ws]; sw = sum(wt); tot = sum(b - a for a, b in sp)
    def at(f):
        x = f * tot
        for a, b in sp:
            if x <= b - a: return a + x
            x -= b - a
        return sp[-1][1]
    c = 0
    for w, q in zip(ws, wt):
        words.append(dict(t=R(at(c / sw)), w=w, src=at(c / sw))); c += q
main = round(sum(b - a for a, b in KEEPS), 3); dur = round(main + END, 2)
src = lambda w0: next(x['src'] for x in words if x['w'].startswith(w0))
cran = src('cranberry')
scenes = [dict(kind='pct', a=R(16.02), b=R(18.45)),          # "Até 12% a partir de 5 unidades"
          dict(kind='gift', a=R(cran - 0.1), b=R(25.85))]    # "ganhei um cranberry porque passou de 400"
for w in words: w.pop('src')
cuts = []; c = 0
for a, b in KEEPS: c += b - a; cuts.append(round(c, 3))
cfg = dict(hook=dict(lines=['12% OFF e', 'sem pagar frete'], em=['12%', 'OFF'], a=0.0, b=2.9), words=words, cuts=cuts, scenes=scenes,
           hot=['12%', 'grátis', 'desconto', 'cranberry'], cta=dict(a=R(26.2), b=main), end=main, dur=dur)
json.dump(cfg, open(f'{W}/cfg_anna.json', 'w'), ensure_ascii=False)
fr = f'{W}/frames_anna'
if not os.path.exists(fr + '/f00000.png'): run(['node', D + '/render_w.js', f'{W}/cfg_anna.json', fr, W])
# zoom: empurrões nas frases fortes + alterna 0/7% a cada corte (esconde o pulo)
terms = []
for a, b, amp in [(1.95, 3.0, .14), (11.4, 12.3, .10), (13.9, 15.3, .12), (22.75, 23.6, .12), (26.3, 27.3, .14)]:
    a, b = R(a), R(b); terms.append(f"{amp}*clip((it-{a - 0.12})/0.12,0,1)*clip(({b + 0.25}-it)/0.25,0,1)")
acc = 0
for i, (a, b) in enumerate(KEEPS):
    if i % 2: terms.append(f"0.07*between(it,{acc:.3f},{acc + b - a:.3f})")
    acc += b - a
z = '1+' + '+'.join(terms)
mid = f'{W}/anna_mid.mp4'; inp = []; fc = []; n = len(KEEPS)
for i, (a, b) in enumerate(KEEPS):
    inp += ['-ss', f'{a:.3f}', '-t', f'{b - a:.3f}', '-i', mid]
    fc.append(f"[{i}:v]setsar=1,setpts=PTS-STARTPTS[v{i}];[{i}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={b - a - 0.03:.3f}:d=0.03[a{i}];")
fc.append(''.join(f'[v{i}][a{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=1[vc0][ac0];')
fc.append(f"[vc0]zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih*0.4-(ih/zoom*0.4)':d=1:s=1080x1920:fps=30,setsar=1[vz];")
fc.append(f"color=c=0x0c298d:s=1080x1920:r=30:d={END},setsar=1[vend];anullsrc=r=48000:cl=stereo,atrim=0:{END}[aend];[vz][ac0][vend][aend]concat=n=2:v=1:a=1[vc][ac];")
o = n; inp += ['-reinit_filter', '0', '-framerate', '30', '-i', fr + '/f%05d.png']
fc.append(f"[{o}:v]format=rgba[ov];[vc][ov]overlay=0:0:format=auto,format=yuv420p[vout];")
sfx = [('whoosh', s['a'] - 0.08) for s in scenes] + [('pop', scenes[1]['a'] + 0.35), ('pop', cfg['cta']['a']), ('whoosh', main - 0.1)]
labs = []
for q, (nm, t) in enumerate(sfx):
    idx = o + 1 + q; inp += ['-i', f'{W}/{nm}.wav']; ms = int(max(0, t) * 1000)
    fc.append(f"[{idx}:a]adelay={ms}|{ms},volume={0.22 if nm == 'pop' else 0.3}[s{q}];"); labs.append(f'[s{q}]')
fc.append(f"[ac]loudnorm=I=-15:TP=-2:LRA=11,aresample=48000[voz];[voz]{''.join(labs)}amix=inputs={len(labs) + 1}:normalize=0:duration=first,alimiter=limit=0.89[aout]")
out = f'{W}/Creator-AnnaLuiza-Esquenta.mp4'
run(['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', ''.join(fc), '-map', '[vout]', '-map', '[aout]', '-r', '30', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out])
print(out, dur, scenes)
