# Tema "11/11 · TEMA EXCLUSIVO (publicar 10/11 20h)" (168318599400)

Duplicado da prévia "11/11 — preto e vermelho" (168318206184) em 04/11. O Pedro programa a publicação para 10/11 às 20h.
Nele fica tudo do 11/11 ligado sem depender de data, e nada do Esquenta.

## Banners (04/11, aguardando aprovação)
| Arquivo | Job Higgsfield |
|---|---|
| 1111-hero-mobile.png (4:5) | 09f38dbb-e786-4de5-9201-614147827ad8 |
| 1111-hero-desktop.png (21:9) | 35f4052d-b876-468a-9c1e-020f8d780ffc |
| 1111-colecao.png (21:9) | b4560f71-6628-4aa4-ab42-3964ddb853c1 |
Referência da linha de produtos: media 5a1c90ea (a mesma dos banners do Esquenta).

## Aplicado no tema (04/11) · tudo do 11/11 sempre ligado, sem Esquenta
- Prévia: https://botanikabrasil.com.br/?preview_theme_id=168318599400. Para ver a madrugada com o site fechado, acrescente `&onze=1`; para voltar, `&onze=0`.
- `botanika-campaign-css.liquid`: sem os snippets do Esquenta (`bk-bf-*`, `bk-pv-home`, `bk-pv-5potes`). O texto "acima de R$349" vira "em todos os pedidos" sempre. Chama `bk-1111`, `bk-pv-1111` e `bk-1111-x`.
- `bk-1111.liquid`: tarja, aviso na página de produto e Q10 sempre ligados até 11/11 às 23h59. O site fechado só vale de 10/11 às 20h até 11/11 às 08h.
- `bk-pv-1111.liquid`: preto e vermelho sempre ligado. Esconde a faixa azul e as barras de frete. Parcela em vermelho.
- `bk-1111-x.liquid` (novo):
  - banner de imagem na home (celular e desktop, no lugar do slideshow);
  - banner nas coleções;
  - tarja maior;
  - faixa da página de produto;
  - caixa da gaveta: frete grátis, quanto falta para a Q10 e o cashback;
  - vitrine e "−10% só aqui" da gaveta escondidos;
  - contador falso escondido;
  - botões da gaveta em vermelho.
- `botanika-freeship-weekend.liquid`: frete do 11/11 (mínimo 0) sempre.
- Arquivos na Shopify: `onze-1111-hero-mobile.png`, `onze-1111-hero-desktop.png` e `onze-1111-colecao.png`.

## Pendente
- Vitor: o "até 40%" por produto. Com isso entram o desconto na Shopify, o selo "-X%" nos cards, os preços e o seletor de potes. Até lá (04/11), o seletor mostra 2 e 3 potes a preço cheio com o selo "🔥 11/11 · frete grátis" (função `offers()` do `bk-1111-x`), sem a frase do "desconto por volume" e sem o contador "produtos limitados" no carrinho.
- Sarah: link do grupo VIP para a tela de site fechado.
- Na página de produto, o bloco "Complete sua rotina" fala em "desconto por volume automático". Rever depois do % do Vitor.
- A contagem mostra as horas até 11/11 às 23h59. Hoje aparece "180h"; no dia aparece o tempo certo.

## Últimas horas (04/11)
- Banners da home: `onze-1111-ultimas-mobile.png` (job bb0c22b1) e `onze-1111-ultimas-desktop.png` (job e62139ba). Trocam sozinhos às 18h do dia 11.
- Testado com o relógio em 11/11 às 19h: banner "ÚLTIMAS HORAS", tarja "11/11 · últimas horas" e contagem de 04h59m.

## 09/11 · Desconto por produto do 11/11 (PDF do Vitor, curva ABC), com ok do Pedro

**Shopify:** 7 descontos automáticos de produto, de 10/11 às 20h a 11/11 às 23h59. Combinam com descontos de pedido e de frete, mas não com outros descontos de produto.

| Desconto | ID | Produtos |
|---|---|---|
| 11/11 · 12% OFF | 1596747055336 | Hair, TetraVit D, Ômega 3, Whey 455 g Chocolate |
| 11/11 · 15% OFF | 1596747088104 | Tri[Mg], Vitamina C |
| 11/11 · 20% OFF | 1596747120872 | Creatina, Whey 910 g, NAC, Kit Imunidade |
| 11/11 · 25% OFF | 1596747153640 | Sleep, Whey Sem Sabor, Flexia, Kit Sono, Kit Whey + Creatina |
| 11/11 · 30% OFF | 1596747186408 | MSM, Whey Cappuccino |
| 11/11 · 35% OFF | 1596747219176 | Cranberry, Kit Completo |
| 11/11 · 40% OFF | 1596747251944 | Coenzima Q10, Xarope |

- **Cupom de influenciadora** (desconto de produto): no 11/11, não soma com o desconto do dia. A Shopify aplica o maior. Decisão do Pedro.
- **Whey 455 g Chocolate:** o produto e a variante Chocolate do kit passaram a vender sem estoque (pedido do Pedro, vai ter reposição).
- **Esquenta 11/11:** os 4 descontos acabam em 10/11 às 20h. Não há sobreposição.

**Tema:**
- `bk-1111-off` (novo): mapa produto → %. Nos cards e na página de produto, mostra "3x cheio" riscado, o "-X%", a parcela e o valor à vista com desconto, e o custo por dia. Some depois de 11/11 às 23h59.
- `bk-1111-x`: o seletor de potes (1, 3 e 5) usa o % do produto, com a faixa "11/11 · X% OFF + frete grátis". Na página de kit, o cartão do kit também leva o %.
- `botanika-campaign-css`: chama o `bk-1111-off`.

**Teste na prévia** (relógio em 11/11): os preços batem com o PDF.
- Hair: R$ 87,47.
- Vitamina C: R$ 76,09.
- Coenzima Q10: R$ 44,76.
- Kit Imunidade: R$ 289,37.
- Whey Chocolate: R$ 129,62.
- Hair, 5 potes: R$ 437,36.

O seletor de potes arredonda para baixo, então pode dar 1 centavo de diferença na parcela. O valor final é o do carrinho da Shopify.

**Conferir em 10/11 às 20h:** o carrinho real com os descontos.
