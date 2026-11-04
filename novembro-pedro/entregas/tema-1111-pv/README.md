# Tema "11/11 — preto e vermelho (prévia 04/11)" (168318206184)

Duplicado do tema no ar "ESQUENTA PV — imagem 5 potes" (168272953576) em 04/11.
Prévia do dia 11 (abre a página com estes parâmetros): https://botanikabrasil.com.br/?preview_theme_id=168318206184&esquenta=0&onze=2
- `esquenta=0` desliga o Esquenta, que liga sozinho em tema não publicado.
- `onze=2` simula o dia 11 aberto. `onze=1` simula a madrugada (site fechado).

## Feito em 04/11
- `snippets/bk-pv-1111.liquid` (novo): coloca a classe `bk-pv` no html de 10/11 às 20h até 11/11 às 23h59. Com ela:
  - o preto e vermelho continua: botões, selos, Mais Vendidos, home preta, brilho nos cards, menu e rodapé;
  - a faixa azul "3x sem juros" some;
  - as barras "Faltam R$ X para o frete grátis" somem (no 11/11 o frete é grátis sem mínimo).
- `snippets/botanika-campaign-css.liquid`: passa a chamar `bk-pv-1111` depois do `bk-1111`.
- Testado com o relógio simulado em 11/11 às 12h:
  - home preta com a tarja e o banner do 11/11;
  - cards com brilho;
  - sem barra de frete e sem faixa azul.

## Falta
1. **Desconto do 11/11 (até 40%):** o Vitor precisa definir quais produtos e quanto em cada. Depois:
   - configurar na Shopify;
   - ajustar o seletor de potes, que hoje mostra a escada antiga (2 potes 5% / 3 potes 10%, que não existe);
   - ajustar os preços nos cards.
   - Testar se o brinde da Q10 continua funcionando junto com o desconto.
2. **Link do grupo VIP da Sarah** na tela de site fechado. Hoje está `sndflw.com/i/botanika11-11`. Mudar também o texto para "reabre quarta 11/11 às 08h".
3. Teste completo de madrugada e do dia 11 na quinta. O Pedro publica na sexta.
