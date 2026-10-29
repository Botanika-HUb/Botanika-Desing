# PÁGINAS — mapa das landing pages Botanika

> **Leia este arquivo primeiro** ao editar qualquer LP. Cada produto é uma **pasta isolada** — mexer numa nunca afeta a outra. Confirme com o usuário qual pasta vai editar antes de começar.

## Convenção
- **Repositório:** `botanikahub/botanika-desing`
- **Uma pasta por produto:** `landing-<slug>/index.html` (arquivo único, HTML autocontido).
- **Branch de publicação:** `lp` (todas as páginas ficam nela). O link muda só pela pasta.
- **Link fixo de cada página:** `https://raw.githack.com/BotanikaHub/Botanika-Desing/lp/landing-<slug>/index.html`
- **Preview instantâneo (sem cache):** troque `lp` pelo SHA do commit → `.../<sha>/landing-<slug>/index.html`
- **Guia de construção/design:** `botanika-lp-superprompt.md` (design system, interações, regras).
- **Checkout Shopify:** `https://botanikabrasil.com.br/cart/<VARIANT_ID>:<QTD>` (kit 1 nos botões soltos; a oferta muda por kit).
- Ao terminar uma edição: validar (`node --check` nos scripts), commit, e push para a branch `lp`.

## Páginas

### 1. Super Ômega 3 + CoQ10
- **Pasta:** `landing-omega/`
- **Link:** https://raw.githack.com/BotanikaHub/Botanika-Desing/lp/landing-omega/index.html
- **Shopify:** produto `super-omega-3-coq10` · **VARIANT_ID `48115368034536`**
- **Preço:** 3x de R$ 54,37 · ou R$ 163,12 à vista · kits 2 (5% OFF) e 3 (10% OFF)
- **Identidade:** oceano profundo azul-marinho + dourado · fundo WebGL (ondas + koi + cápsulas) · Playfair Display
- **Fotos de depoimento:** `landing-omega/proof/` (também usadas pelo Tri)
- **Status:** ✅ pronta

### 2. Tri[Mg] Complex — Magnésio 3 em 1
- **Pasta:** `landing-tri/`
- **Link:** https://raw.githack.com/BotanikaHub/Botanika-Desing/lp/landing-tri/index.html
- **Shopify:** produto `tri-mg-complex` · **VARIANT_ID `48115368558824`**
- **Preço:** 3x de R$ 29,17 · ou R$ 87,50 à vista · kits 2 (5% OFF) e 3 (10% OFF) — *confirmar preços de kit na loja*
- **Identidade:** meia-noite índigo + menta/violeta/champagne · fundo constelação mineral interativa (muda de cor por seção) · molécula "3 em 1" orbitando · Fraunces
- **Imagem do pote:** `landing-tri/bottle-tri.png` (transparente)
- **Status:** ✅ pronta

### 3. Hair Botanika — Cabelos, Unhas e Pele
- **Pasta:** `landing-hair/`
- **Link:** https://raw.githack.com/BotanikaHub/Botanika-Desing/lp/landing-hair/index.html
- **Shopify:** produto `hair-botanika` (confirmar handle) · **VARIANT_ID `HAIR_VARIANT_ID` (⚠️ placeholder — trocar pelo real)**
- **Preço:** *placeholder* 3x de R$ 32,33 · ou R$ 97,00 · kits 2 (5% OFF) e 3 (10% OFF + frete grátis) — *confirmar preços/variant na loja*
- **Produto:** 12 ativos (Biotina, Silício Orgânico, Zinco, Ferro, Cisteína, Metionina, Iodo, Vit A/E/B1/B2/B5) · 60 cápsulas · 38g · sem açúcar/glúten
- **Identidade:** "Seiva & Raiz" — verde-botânico profundo + rosé-champagne + dourado · fundo canvas "cascata de fios luminosos" (reage ao mouse) · Italiana + Outfit
- **Pote:** render SVG estilizado (trocar por PNG transparente quando disponível)
- **Status:** ✅ pronta (pendente: VARIANT_ID + preços reais da loja)

### 4. Captação · Grupo VIP 11/11 (Black Friday)
- **Pasta:** `landing-grupo-vip-11-11/`
- **Link (no ar, Shopify):** https://botanikabrasil.com.br/pages/grupo-vip-11-11
- **Como está publicada:** página `grupo-vip-11-11` na Shopify. O tema mostra um iframe em tela cheia, e o HTML vem do arquivo `lp-grupo-vip-1111-v4.txt` (em base64) em Conteúdo › Arquivos. Para atualizar: gerar a versão nova, subir um .txt novo e trocar a URL no corpo da página.
- **Tipo:** captação para o grupo VIP do 11/11 (sem preço, desconto ou checkout). Tarefa no Alliance OS: `mcp-1793219208869-17-9fa23`.
- **Destino:** `GRUPO_URL` no script, `https://sndflw.com/i/botanika11-11` (campanha "Black Friday 11/11" no SendFlow, recebida em 29/10). UTMs repassadas + `utm_source=lp_grupo_vip_1111`.
- **Rastreio:** GA4 (GT-P8RLSDHK / G-2JFV5TGHCV) + Meta Pixel 828186133708463. Evento `Lead` e `generate_lead` no clique.
  - Na versão da Shopify, os pixels rodam na **página da loja** (endereço real, com UTMs e fbclid), e não dentro do quadro. O Meta Pixel (PageView) está no corpo da página. O GA4 vem do Google da loja. Os cliques chamam `window.top` (Lead, generate_lead e dataLayer `grupo_vip_click`).
  - O HTML publicado está em `novembro-pedro/entregas/lp-grupo-vip-1111-shopify.html`.
- **Identidade:** formato da LP da Revita adaptado à Botanika: fundo branco, azul #0c298d, urgência em vermelho #e3132b e Instrument Sans. Topo com contador, cartão de oferta secreta, comparação entre quem fica de fora e quem está no grupo, e carrossel de vídeos UGC do site.
- **Status:** ✅ no ar com o link definitivo do grupo

<!-- PRÓXIMOS PRODUTOS (modelo — copiar ao criar):
### N. <Nome do produto>
- **Pasta:** `landing-<slug>/`
- **Link:** https://raw.githack.com/BotanikaHub/Botanika-Desing/lp/landing-<slug>/index.html
- **Shopify:** produto `<handle>` · **VARIANT_ID `<id>`**
- **Preço:** ...
- **Identidade:** <paleta / fundo / assinatura / fonte — DEVE ser própria, não clonar outra LP>
- **Status:** em construção
-->

## Como editar uma página específica (comando pra colar num chat novo)
> "Leia o `PAGINAS.md`, o `botanika-lp-superprompt.md` e a pasta `botanika-lp-kit/` no repo `botanikahub/botanika-desing`. Vou editar a LP do **[produto]**. Me confirma qual pasta/arquivo você vai mexer antes de começar."
