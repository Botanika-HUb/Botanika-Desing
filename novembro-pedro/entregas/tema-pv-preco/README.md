# Tema "ESQUENTA PV — preço c/ desconto 03/11" (168270889192)

Duplicado do tema publicado preto e vermelho (168242708712) em 03/11, a pedido do Pedro.
Preview: https://botanikabrasil.com.br/?preview_theme_id=168270889192

Arquivos alterados (só valem com a classe `bk-bf` no html, ou seja, na janela do Esquenta ou no preview):
- `snippets/installment-price.liquid`: a página de produto, os cards e o sticky mostram o preço com 8% (parcela grande em vermelho e a cheia riscada).
- `snippets/bk-custo-dia.liquid`: o custo por dia já sai com 8%.
- `snippets/bk-gaveta-card.liquid`: a vitrine da gaveta mostra o preço do Esquenta, acompanhando o % da escada.
- `snippets/bk-bf-pv.liquid`:
  - preço cheio riscado em todos os cartões de pote;
  - na gaveta, o preço de cada linha sai com o % (8/10/12) e a parcela aparece no subtotal;
  - a vitrine volta, mas sem a barra da escada antiga;
  - botões e selo de desconto em vermelho;
  - o selo do card não fica mais em cima do selo do tema.

Conferido em 03/11:
- Hair 1 un. = R$ 91,45.
- 2 Hair: −8%, subtotal R$ 182,90.
- 2 Hair + TetraVit: −10%, subtotal R$ 284,34. A soma das linhas dá R$ 284,35, diferença de 1 centavo.

03/11, mais tarde:
- Brilho vermelho pulsando em volta dos cards de produto (desliga para quem pede menos movimento).
- Escondida a contagem "10 avaliações" na página de produto (no topo, nos potes e no resumo das avaliações). A nota 5,0 e as estrelas continuam.
- Home preta e vermelha da faixa "Mais vendidos" para baixo (snippet novo `bk-pv-home.liquid`, chamado no `botanika-campaign-css.liquid`). Também some a faixa branca depois dos produtos.
- Removido o contador "Os produtos são limitados…" da gaveta e do carrinho.
- Temas sinalizados na loja: 4 com "🗑️ APAGAR —" e o OFICIAL com avaliações (168106000616) com "✅ MANTER".
