"""Vídeos universais da Black Botanika · 1º lote (04/11).
Corpo: IMG_9667 (Tri[Mg] Complex, 2ª tomada de cada frase). Ganchos: IMG_9671 (16 ganchos).
Os brutos são HDR (HLG) do iPhone: viram SDR com tone mapping (hable) em body_mid.mp4 / hooks_mid.mp4.
Uso: python3 build_u.py 1   (gera Universal01-v1.mp4)
"""
import json, subprocess, sys, os
D = os.path.dirname(os.path.abspath(__file__))
W = sys.argv[2] if len(sys.argv) > 2 else D  # pasta de trabalho (fontes, sons, frames)
BR = W + '/../brutos'
def run(c): subprocess.run(c, check=True)

OFF = 3.9  # body_mid.mp4 começa em 3,9 s do IMG_9667
# (início, fim) no IMG_9667 · (início, fim) da fala · texto
BODY = [
 # v2 (04/11): bordas medidas na onda do áudio (fala -42 dB, 0,06 s antes e 0,10 s depois).
 # Saíram as tentativas que duplicavam palavras: 55,4-56,6 ("Comecei a tomar...") e 91,4-93,9 ("Então esse é o melhor momento pra montar não...").
 ((4.43, 7.75),   [(4.49, 7.65)],   "Se nem café te levanta mais, não é de café que você tá precisando."),
 ((17.70, 22.51), [(17.76, 22.41)], "Eu tentei dormir mais cedo, tentei vitamina de farmácia, tentei cortar açúcar e nada resolveu."),
 ((28.06, 31.05), [(28.12, 30.95)], "O que me faltava não era descanso. Era magnésio."),
 ((40.37, 44.42), [(40.43, 44.32)], "Ele participa de várias reações no corpo, inclusive as que geram energia."),
 ((57.14, 60.89), [(57.20, 60.79)], "Comecei a tomar o Tri-Magnésio da Botanika e ele virou parte fixa do meu dia."),
 ((78.41, 83.90), [(78.47, 83.80)], "E agora a Black da Botanika tá rolando, e não é só ele: o site inteiro tá com condição especial o mês todo."),
 ((94.53, 99.35), [(94.59, 99.25)], "Então esse é o melhor momento pra você garantir não só o seu Tri-Magnésio, mas toda a sua suplementação."),
 ((116.16, 118.46), [(116.22, 118.36)], "Clica no botão aqui embaixo e garanta o seu."),
]
JOBS = {
 '1': dict(hook=dict(lines=['Nem café', 'resolve?'], em=['café'])),
}
END = 2.4
HOT = ['magnésio', 'tri-magnésio', 'black', 'inteiro', 'energia', 'botão', 'suplementação']

def build(k):
    j = JOBS[k]
    keeps, spans, texts = [], [], []
    for i, (kp, sp, tx) in enumerate(BODY):
        keeps.append(kp); spans.append(sp)
        texts.append(tx)
    # texto que atravessa um corte (None = continua no próximo trecho)
    words = []; acc = 0; pend = []
    for i, (kp, sp, tx) in enumerate(BODY):
        a, b = kp
        seg = [(s0 - a + acc, s1 - a + acc) for s0, s1 in sp]
        pend += seg
        if tx:
            ws = tx.split(); tot = sum(e - s for s, e in pend); wt = [len(w) + 2 for w in ws]; sw = sum(wt)
            # posição de cada palavra proporcional ao tamanho, dentro dos trechos de fala
            def at(f):
                x = f * tot
                for s, e in pend:
                    if x <= e - s: return s + x
                    x -= e - s
                return pend[-1][1]
            c = 0
            for w, q in zip(ws, wt):
                words.append(dict(t=round(at(c / sw), 3), w=w)); c += q
            pend = []
        acc += b - a
    main = round(acc, 3); dur = round(main + END, 2)
    def wt_(w): return next(x['t'] for x in words if x['w'].lower().startswith(w))
    tri = wt_('tri-magnésio'); blk = next(x['t'] for x in words if x['w'] == 'Black')
    scenes = [dict(kind='prod', a=round(tri - 0.1, 3), b=round(tri + 1.5, 3), name='TRI[MG]<br>COMPLEX', sub='magnésio 3 em 1', img='trimg.png'),
              dict(kind='black', a=round(blk - 0.15, 3), b=round(blk + 1.9, 3))]
    last = BODY[-1][0]; cta_a = round(main - (last[1] - last[0]), 3)
    hk = dict(j['hook'], a=0.0, b=round(min(3.0, BODY[0][0][1] - BODY[0][0][0]), 2))
    cfg = dict(hook=hk, words=words, scenes=scenes, hot=HOT, cta=dict(a=cta_a, b=main), end=main, dur=dur)
    json.dump(cfg, open(f'{W}/cfg_u{k}.json', 'w'), ensure_ascii=False)
    fr = f'{W}/frames_u{k}'
    if not os.path.exists(fr + '/f00000.png'): run(['node', D + '/render_u.js', f'{W}/cfg_u{k}.json', fr, W])
    # zoom: alterna 0/7% a cada corte (esconde o pulo) + empurrão nas frases fortes
    terms = []; acc = 0
    for i, (a, b) in enumerate(keeps):
        if i % 2: terms.append(f"0.07*between(it,{acc:.3f},{acc + b - a:.3f})")
        acc += b - a
    for t0 in [0.3, blk - 0.1, cta_a + 0.1]:
        terms.append(f"0.12*clip((it-{t0 - 0.12:.3f})/0.12,0,1)*clip(({t0 + 1.0:.3f}-it)/0.25,0,1)")
    if os.environ.get('SO_FRAMES'): print('frames ok', fr); return
    z = '1+' + '+'.join(terms)
    mid = f'{BR}/body_mid.mp4'; inp = []; fc = []; n = len(keeps)
    for i, (a, b) in enumerate(keeps):
        inp += ['-ss', f'{a - OFF:.3f}', '-t', f'{b - a:.3f}', '-i', mid]
        fc.append(f"[{i}:v]setsar=1,setpts=PTS-STARTPTS[v{i}];[{i}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={b - a - 0.03:.3f}:d=0.03[a{i}];")
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
    out = f'{W}/Universal{int(k):02d}-v2.mp4'
    run(['ffmpeg', '-v', 'error', '-y'] + inp + ['-filter_complex', ''.join(fc), '-map', '[vout]', '-map', '[aout]', '-r', '30', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out])
    print(out, dur)

build(sys.argv[1])
