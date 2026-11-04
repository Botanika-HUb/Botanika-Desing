# Tema "ESQUENTA BOTANIKA WEEK (publicar 11/11 23h59)" (168321417448)

Duplicado em 04/11 do tema no ar "ESQUENTA PV — imagem 5 potes" (168272953576). A oferta da Week é igual à do Esquenta 11/11 (ficha v3):
- 8% em 1 item, 10% em 3+ e 12% em 5+, valendo misturando os produtos;
- frete grátis acima de R$ 249;
- cranberry acima de R$ 400 (2 para clientes recorrentes).

Preview: https://botanikabrasil.com.br/?preview_theme_id=168321417448

Janela: 12/11 00h → 20/11 23h59 (Brasília) = 1794452400 → 1795230000.

| Arquivo | Mudança | Status |
|---|---|---|
| `botanika-campaign-css` | Janela do R$349→R$249 nas novas datas; saem o `bk-1111` e o script de frete do 11/11 | ✅ no tema |
| `botanika-freeship-weekend` | Frete acima de R$ 249 nas novas datas; sai o frete do 11/11 | ✅ no tema |
| `bk-bf-merge` | Junta "Esquenta Botanika Week · 8% + 2% + 2%" numa linha só | ✅ no tema |
| `bk-bf-skin` | Novas datas; "Esquenta 11/11" vira "Esquenta Botanika Week" (tarja, banner, textos, brinde); banners novos | ✅ no tema |
| `bk-bf-pv` | Textos "Esquenta Botanika Week" e banners pretos novos | ✅ no tema |

Banners: `banners/` (gerados em 04/11 só trocando o texto dos aprovados: "ESQUENTA BOTANIKA WEEK" e "SÓ ATÉ 20/11"). Aprovados pelo Pedro em 04/11 e enviados para a Shopify (esquenta-week-preto-hero-mobile/desktop.png e esquenta-week-preto-colecao.png).

## Descontos na Shopify (criados em 04/11, com OK do Pedro)
Todos programados de 12/11 00h a 20/11 23h59 (Brasília). São cópias dos descontos do Esquenta 11/11, com as mesmas regras de combinação:
| Desconto | ID |
|---|---|
| Esquenta Botanika Week · 8% OFF (1+ un.) | 1595622326504 |
| Esquenta Botanika Week · +2% (3+ un.) | 1595622359272 |
| Esquenta Botanika Week · +2% (5+ un.) | 1595622392040 |
| Esquenta Botanika Week · Frete grátis acima de R$ 249 | 1595622424808 |
| Esquenta Botanika Week · Brinde cranberry acima de R$ 400 | 1595622260968 |
| Esquenta Botanika Week · 2 cranberries (clientes recorrentes) | 1595622293736 |

Não há sobreposição com o 11/11, que termina em 12/11 02:59:59Z. O estoque do cranberry era de 1.205 em 04/11.

## Teste (04/11, relógio simulado em 14/11)
- Home: tarja "Esquenta Botanika Week · termina em 6d", banner novo, "Tá rolando o Esquenta Botanika Week" e nenhum "11/11" na página.
- Coleção: banner novo.
- Página de produto (Hair): 5 potes 12%, 3 potes 10% e 1 pote 8%, com a faixa da Week.

## Último dia (20/11)
O snippet `bk-week-ultimo` (renderizado no `botanika-campaign-css`) faz a troca sozinho na sexta 20/11 às 00h:
- banners da home e das coleções passam a ser os de "ÚLTIMO DIA · ACABA HOJE 23H59" (esquenta-week-ultimo-*.png, aprovados pelo Pedro em 04/11);
- entra o selo "⏳ ÚLTIMO DIA" na tarja do topo (no celular fica numa linha própria), na faixa da página de produto e na caixa do carrinho.

Testado com o relógio em 19/11 (sem troca) e em 20/11 (com troca).

Falta o Pedro programar a publicação deste tema para 11/11 às 23h59 (logo depois do tema exclusivo do 11/11).
