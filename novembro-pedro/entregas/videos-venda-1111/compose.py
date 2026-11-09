"""Edição v4 (motion): vídeo da Mafe + telas animadas (motion.html, Playwright) + Mafe em janelinha (PiP) nas telas cheias.
Uso: python3 compose.py specs.json motion.json R1 saida_dir
- specs.json: cortes (os trechos já cortados em saida_dir/_R1 pelo build.py)
- motion.json: cenas por trecho: {"R1": [{"i":2,"type":"clock",...,"full":true}, ...]}
"""
import json, os, subprocess, sys
spec_f, mot_f, key, out = sys.argv[1:5]
S = json.load(open(spec_f))[key]; M = json.load(open(mot_f))[key]
PAD_IN, PAD_OUT, END = 0.06, 0.12, 3.0
segs = [(max(0, a - PAD_IN), b + PAD_OUT) for a, b in S['segs']]
st, t = [], 0.0
for a, b in segs: st.append(t); t += b - a
total = t; dur = total + END
here = os.path.dirname(os.path.abspath(__file__))
tmp = os.path.join(out, '_' + key)
# 1) base: junta os trechos (já cortados) e congela o último quadro no fim
base = os.path.join(tmp, 'base.mp4')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', os.path.join(tmp, 'list.txt'),
                '-vf', 'tpad=stop_mode=clone:stop_duration=%.2f' % END, '-af', 'apad=pad_dur=%.2f' % END,
                '-c:v', 'libx264', '-preset', 'fast', '-crf', '16', '-c:a', 'aac', '-b:a', '192k', '-t', '%.3f' % dur, base], check=True)
# 2) cenas na linha do tempo final
scenes, pip = [], []
for m in M:
    i = m.pop('i'); a = st[i] + m.pop('at', 0.0); j = m.pop('until', i)
    b = st[j] + (segs[j][1] - segs[j][0])
    m['t0'], m['t1'] = round(a, 3), round(b, 3)
    if m.get('full'): m['bg'] = m.get('bg', 'card'); pip.append((a, b))
    scenes.append(m)
scenes.append({'type': 'end', 'img': 'coq10', 'bg': 'card', 't0': round(total, 3), 't1': round(dur, 3), 'fade': False, 'full': True})
scenes.sort(key=lambda m: m['t0'])
fulls = [m for m in scenes if m.get('full')]
for k, m in enumerate(fulls):
    m['fin'] = not (k > 0 and abs(fulls[k - 1]['t1'] - m['t0']) < 0.06)
    m['fout'] = not (k + 1 < len(fulls) and abs(fulls[k + 1]['t0'] - m['t1']) < 0.06)
if False: scenes.append({'type': 'end', 'img': 'coq10', 'bg': 'card', 't0': round(total, 3), 't1': round(dur, 3), 'fade': False})
cfg = {'scenes': scenes, 'img': os.environ.get('CUT_DIR', '/tmp/claude-0/-home-user-Botanika-Desing/939e42b8-9d13-56a4-bbfb-1c809580e4f3/scratchpad/cut'), 'dur': dur}
cfgp = os.path.join(tmp, 'motion_cfg.json'); json.dump(cfg, open(cfgp, 'w'))
fr = os.path.join(tmp, 'mframes'); os.makedirs(fr, exist_ok=True)
subprocess.run(['node', os.path.join(here, 'render_motion.js'), cfgp, fr, os.path.join(here, 'motion.html')], check=True)
# 3) composição: base + telas + PiP (Mafe numa janelinha com borda branca) nas telas cheias
pip.sort(); mg = []
for a, b in pip:
    if mg and a - mg[-1][1] < 0.06: mg[-1][1] = max(mg[-1][1], b)
    else: mg.append([a, b])
pip = mg
en = '+'.join('between(t,%.3f,%.3f)' % (a + 0.1, b - 0.05) for a, b in pip) or '0'
fc = ('[0:v]split[b0][b1];'
      '[b1]scale=300:534,pad=312:546:6:6:white[pip];'
      '[b0][1:v]overlay=0:0:format=auto[m];'
      "[m][pip]overlay=x=W-w-44:y=H-h-60:enable='%s'[v]" % en)
outp = os.path.join(out, '%s.mp4' % S.get('name', key).replace('.mp4', '') + '')
outp = os.path.join(out, S.get('name', key) + '_v4.mp4')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', base, '-framerate', '30', '-i', os.path.join(fr, 'f%05d.png'),
                '-filter_complex', fc, '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '19',
                '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-t', '%.3f' % dur, '-movflags', '+faststart', outp], check=True)
print(outp, round(dur, 2))
