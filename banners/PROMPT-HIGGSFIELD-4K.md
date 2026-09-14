# Prompt Higgsfield — arte fotorrealista do banner "Compre 4, leve 5"

Conceito aprovado em 14/09. A arte da Higgsfield entra como **fundo**; a
tipografia continua vindo de `banners/semana-do-cliente-v2.html`, porque texto
gerado por IA erra acento e quebra de palavra em português — e a headline é
exatamente onde não pode ter erro.

## Configuração (não usar os padrões!)

| Parâmetro | Valor | Observação |
|---|---|---|
| `model` | `gpt_image_2_5` | tem 21:9 e 4:5 nativos |
| `variant` | `flare` | padrão, melhor para fotorrealismo |
| `quality` | **`max`** | o padrão é `low` — foi o erro da 1ª tentativa |
| `resolution` | **`4k`** | o padrão é `1k` |
| `aspect_ratio` | `21:9` desktop · `4:5` mobile | |

Custo aferido: **16 créditos** por geração em 4k/max.

⚠️ O plano está em período de carência, com teto de ~5 gerações por dia,
**contado por imagem** (`count: 2` gasta 2). O teto é da conta inteira — trocar
de modelo ou de provedor não contorna.

---

## Prompt — DESKTOP (21:9)

Ultra-premium commercial product photograph for a wellness brand's hero banner. Medium-format quality, 100mm macro lens, f/8, razor-sharp detail throughout, high dynamic range, immaculate retouching.

THE SUBJECT — a precise row of five supplement jars standing on a seamless surface, occupying only the RIGHT 45% of the wide frame:
• Four IDENTICAL jars, evenly spaced: matte deep-navy-blue cylindrical supplement jars (colour #323C91), each with a glossy navy screw-top lid slightly wider than the body, a subtle shoulder curve, and a clean blank cream-white label band wrapping the middle. The labels are COMPLETELY BLANK — no writing, no logos, no symbols, just smooth cream paper stock with a faint emboss.
• Then a small gap, and a FIFTH jar of the exact same size and shape, but visually distinct: a warm cream off-white matte body with a glossy TEAL screw-top lid (colour #0D9488) and a blank white label. This one is lit slightly brighter, as the hero of the group.
• Beside the fifth jar, one fresh halved orange and a couple of small glossy green leaves resting on the surface — subtle, not cluttered — signalling vitamin C.

BACKGROUND: a seamless studio backdrop in a smooth warm citrus gradient — deep burnt orange at the far left, flowing through vivid orange, into golden yellow at the right edge. Behind the jars, a soft wide radial sun-glow warms the backdrop. No graphic rays, no starburst, no patterns — only smooth light falloff.

LIGHTING: high-end studio setup. Large soft key light from the upper left, a warm golden rim light raking the right edges of the jars, delicate specular highlights along the glossy lids, soft gradient reflections down the curved bodies. Soft realistic contact shadows pooling under each jar and a faint glossy reflection on the surface beneath them.

COMPOSITION: the LEFT 55% of the frame must be completely empty, clean gradient backdrop — pure negative space reserved for typography added later. Nothing intrudes there. Keep the top 15% of the frame calm and uncluttered. The jars are bottom-weighted, standing on a surface line in the lower portion of the frame.

MOOD: warm, generous, premium, calm confidence. The feeling of a high-end pharmacy or a luxury wellness campaign — expensive, clean, appetising.

ABSOLUTELY NO: text, letters, numbers, words, typography, logos, brand marks or writing of any kind anywhere in the image; no red tones; no navy or blue in the background; no people, hands or body parts; no price badges, starbursts, stickers or sale graphics; no clutter; no harsh shadows; no visible studio equipment.

---

## Prompt — MOBILE (4:5)

Mesmo texto do desktop, trocando o bloco COMPOSITION por:

COMPOSITION: vertical portrait framing. The row of five jars sits as a horizontal band across the LOWER THIRD of the frame, standing on a surface line. The UPPER TWO-THIRDS must be completely empty, clean gradient backdrop — pure negative space reserved for typography added later. Keep the bottom 8% calm as well, for carousel dots.

---

## Depois de gerar

1. Conferir olhando (`Read` no PNG) — principalmente se não entrou nenhum texto.
2. Baixar a arte e apontar como `background-image` das artboards em
   `banners/semana-do-cliente-v2.html`, no lugar do gradiente CSS, mantendo a
   camada `.layer` com a tipografia por cima.
3. Re-renderizar com `scratchpad/shot.mjs` para sair nos 2200×933 e 1400×1737.
