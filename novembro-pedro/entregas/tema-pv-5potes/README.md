# Tema "ESQUENTA PV — imagem 5 potes" (168272953576)

Duplicado do tema publicado "ESQUENTA PV — preço c/ desconto 03/11" (168270889192) em 04/11, porque o Gabriel pediu no grupo para ajustar a imagem dos 5 potes.
Preview: https://botanikabrasil.com.br/?preview_theme_id=168272953576

- `snippets/bk-pv-5potes.liquid` (novo): o cartão "5 potes" usava a foto de 3 potes. Agora a imagem é montada com a foto de 1 pote do próprio produto, com 3 potes atrás e 2 na frente. Vale para todos os produtos, sem foto nova.
- `snippets/botanika-campaign-css.liquid`: passa a chamar o `bk-pv-5potes`.
- Testados os 21 produtos: os 17 com cartão de 5 potes montaram certo. Os 4 kits não têm cartão de 5 potes.
