# Semana do Cliente — 14/09 a 19/09 · estado da Shopify

Loja: botanikabrasil.com.br · plano Shopify (não-Plus) · BRL · UTC-3
Configurado em 12/09. Tudo **programado**, com data de fim. Nada depende de alguém ligar ou desligar na mão.

---

## 1. O que está no ar (agendado)

| Item | ID | Janela (BRT) | Combina (produto / pedido / frete) |
|---|---|---|---|
| **RECOMPRA10** — cupom 10% | `DiscountCodeNode/1580102287592` | 14/09 00h01 → 20/09 00h00 | SIM / **NÃO** / SIM |
| Frete grátis ≥ R$ 199,90 | `DiscountAutomaticNode/1580105302248` | 14/09 00h01 → 20/09 00h00 | SIM / SIM / NÃO |
| 100 primeiros — frete sem mínimo | `DiscountAutomaticNode/1580105335016` | 14/09 00h01 → **14/09 23h59** | SIM / SIM / NÃO |
| Compre 4, leve 5 — Super Vitamina C | `DiscountAutomaticNode/1580105367784` | 14/09 00h01 → 20/09 00h00 | SIM / SIM / SIM |
| ~~Escada Volume — 15% (5+ itens)~~ | `DiscountAutomaticNode/1577084682472` | **DESATIVADO em 13/09** | — |
| ~~Escada Volume — 20% (8+ itens)~~ | `DiscountAutomaticNode/1577084715240` | **DESATIVADO em 13/09** | — |

> **Escadas de volume — desativadas em 13/09, a pedido.** Elas nunca foram perpétuas: foram criadas
> em 02/09 já agendadas só para a janela da campanha (14/09 03:01Z → 20/09 03:00Z) e morreriam
> sozinhas em 20/09. Como os 15%/20% saíram de toda a comunicação (ajuste do Gabriel), desconto que
> ninguém anuncia só custava margem. **Não há nada a restaurar depois da campanha** — o estado
> perpétuo da loja (as escadas por produto, 5% em 2 un e 10% em 3 un, com `endsAt` nulo) é o mesmo
> com ou sem elas. Se um dia forem reaproveitadas: `discountAutomaticActivate` nos mesmos IDs, mas
> **o `startsAt`/`endsAt` original foi sobrescrito** pela desativação — tem que reagendar a janela.

**RECOMPRA10** é classe PRODUTO (aplicado sobre a coleção `[CUPONS] Todos os Produtos`, não sobre
"todos os produtos" — se fosse "todos os produtos" a Shopify o classificaria como classe PEDIDO e o
bloqueio contra o cupom de influenciadora deixaria de existir). Sem limite de uso, sem
"uma vez por cliente".

**Aberto a qualquer cliente** (decisão de 12/09). A restrição por segmento foi removida porque exigia
que a pessoa estivesse logada com o e-mail da compra anterior, o que gerava recusa no carrinho. Em
troca: **se o código vazar, funciona para cliente novo também** — somado à escada por produto chega a
~19% off (era 28% quando as escadas de volume existiam; foram desativadas em 13/09).
Por isso o código não pode aparecer em criativo público, só no disparo segmentado, e vale olhar a
contagem de uso na segunda e na terça.

### Cupons abertos pausados (12/09)

Todos acumulavam com as escadas e entregavam o mesmo desconto (ou mais) que a condição exclusiva da
base, esvaziando o argumento da campanha. Nenhum foi apagado; os históricos estão preservados.

| Cupom | ID | Usos | Fim |
|---|---|---|---|
| PALPITE12 (12%) | `1554738020584` | 3 | **encerrado em 12/09**, em definitivo |
| BRASIL10 (10%) | `1554185879784` | 0 | 14/09 00h01 |
| VOLTEI10 (10%) | `1552191848680` | 9 | 14/09 00h01 |
| RECUPERA10 (10%) | `1566943281384` | 5 | 14/09 00h01 |

⚠️ **RECUPERA10 pode estar plugado em automação de carrinho abandonado.** Se estiver, o fluxo de
recuperação fica sem oferta a partir de segunda. **RECUPERA10ZAP** e **RECUPERA10MAIL** seguem ativos,
também dão 10% e estão com "combina com" tudo desligado — não criam a brecha dos 28%. Trocar a
automação para um desses resolve. Conferir no ActiveCampaign antes de segunda.

⚠️ **Código de cupom é único na Shopify — nenhum desses volta sozinho.** Diferente dos bumps, não dá
para recriá-los programados. Se BRASIL10, VOLTEI10 e RECUPERA10 tiverem que voltar depois da campanha,
é edição manual: abrir cada um e apagar a data de término.

## 2. Limite de 25 descontos automáticos — e o que foi feito

A loja estava em 25/25. A Shopify conta **períodos que se sobrepõem**, não o total
(confirmado na prática, e é o mesmo padrão que o Dia D usou em 09/09 com as 16 escadas).

Três bumps foram encerrados em **14/09 00h01** e **recriados já programados para voltar
em 20/09 00h00**, sem data de fim. A volta é automática — ninguém precisa religar nada.

| Bump | Encerra 14/09 00h01 | Volta 20/09 00h00 |
|---|---|---|
| Creatina → Whey 10% | `1574087000296` | `1580105433320` |
| Hair → Vitamina C 10% | `1572745773288` | `1580105466088` |
| Vit C / Ômega → TetraVit D 10% | `1573508743400` | `1580105498856` |

Continuam ativos e intocados: **Whey → Creatina**, **Tri[Mg] → TetraVit D**, **Sleep → Tri[Mg]**,
as 16 escadas por produto, os cupons de influenciadora e os cupons abertos.

⚠️ **Cota de automáticos: a loja está NO TETO. Não sobrou vaga.**

O teto é **25 automáticos** e a Shopify o aplica por sobreposição de período — a mensagem exata do
erro é `ACTIVE_PERIOD_OVERLAP: Limit of 25 automatic discounts reached.`

> **Não confie em contagem feita à mão aqui.** Em 13/09, depois de desativar as 2 escadas de volume,
> a contagem manual dos automáticos que se sobrepõem à janela deu **23** — e mesmo assim a tentativa
> de estender um bump foi recusada por limite. Ou seja, a Shopify conta algo que a listagem simples
> não mostra (provavelmente os instantes de fronteira, ou os 3 gêmeos `[retomada 20/09]`, que têm
> `endsAt` nulo). **A única contagem confiável é tentar a operação e ver se passa.** Já errei essa
> conta duas vezes; não repita o erro.

Cupom **não** entra nessa cota — só automáticos.

**Onde abre vaga sem custo:** no dia 1, ao desativar à mão o frete grátis sem mínimo dos 100
primeiros (`DiscountAutomaticNode/1580105335016`), libera-se uma vaga. É o momento natural para
trazer **um** bump de volta rodando de terça a sexta.

---

## 3. ⚠️ REGRAS PARA A ALTERAÇÃO DO TEMA

**O cliente nunca pode ver um preço que o checkout não vai confirmar.** Cada item abaixo é um
lugar onde a vitrine pode prometer o que a loja não entrega.

### Não anunciar durante 14–19/09
- **"Leve o 2º com 10% off" para Hair → Vitamina C, Creatina → Whey e Vit C/Ômega → TetraVit D.**
  Esses três bumps estão desligados na semana. Qualquer bloco de cross-sell que os mostre precisa
  sair no dia 14 e voltar no dia 20.
- **5% no PIX — CANCELADO.** Decisão de 12/09: sai da campanha, não vai mais existir. Tem que ser
  removido de **todos** os canais: site, criativos, CRM, WhatsApp, influenciadoras, lives. O plano
  oficial em PDF ainda menciona os 5% do PIX e o acúmulo deles com os 10% de recompra — **essa parte
  do documento está vencida**.
- **Qualquer percentual somado do tipo "até 25%".** Desde 13/09 a pergunta ficou sem objeto: as
  escadas de volume foram desativadas, o teto automático é 10% e não existe mais nenhuma soma de
  escadas para testar. O único empilhamento real é **RECOMPRA10 (10%) sobre a escada (10%)**,
  que dá ~19% efetivo em 3 unidades — e mesmo esse só se anuncia depois de visto num carrinho real.

### Anunciar com o texto certo
- **Compre 4, leve 5:** o BxGy da Shopify **não adiciona o item ao carrinho** — ele zera o preço de
  uma Vitamina C que já esteja lá. A copy tem que dizer, na PDP e no carrinho:
  *"adicione 1 Super Vitamina C e ela sai de graça"*. Sem isso o cliente com 4 itens não vê o brinde.
- **Frete:** R$ 199,90 vale **só** de 14/09 00h01 a 20/09 00h00. Fora dessa janela o mínimo volta a ser
  R$ 349,00 sozinho (é regra da taxa de envio, não desconto — não foi tocada).
- **100 primeiros:** o desconto expira **14/09 às 23h59 BRT**. O aviso no site tem que sair no mesmo
  minuto, senão o site promete frete grátis depois que a loja parou de dar.
- **RECOMPRA10:** só funciona para quem já tem pedido anterior. Não pode ser anunciado como cupom
  aberto — cliente novo tenta, é recusado, e abandona.

### Comunicar o que existe e ninguém está comunicando
- ~~As escadas de 15% (5+ itens) e 20% (8+ itens)~~ — **resolvido de outra forma em 13/09.** O Gabriel
  pediu para tirar os 15%/20% da comunicação e enfatizar o "compre 4, leve 5". Como ninguém ia
  anunciá-las, foram desativadas. A mecânica visível voltou a ser exatamente a de sempre
  (5% em 2 un, 10% em 3 un) mais o brinde — que é o que a mensagem oficial descreve.
- **"Os 100 primeiros pedidos" não é contagem, é horário** (segunda 14/09 até 23h59). Comunicar como
  contagem gera reclamação de quem comprar na terça.
- **RECOMPRA10 é cupom e exige login** com o e-mail que tem pedido anterior. O código precisa
  aparecer na copy, junto com a instrução de entrar na conta.

### Contradição comercial — resolvida
PALPITE12, BRASIL10, VOLTEI10 e RECUPERA10 foram pausados (ver seção 2). Durante a campanha, nenhum
cupom aberto empata ou supera a condição da base. Os que continuam no ar — JOINGLE, ELAINE, LUCCA
(5%), BOTANIKA (5%, não acumula com nada), ALUNO10, ALUNONOVA15, VOLTA5, VOLTA10, RECUPERA10ZAP e
RECUPERA10MAIL — ficam abaixo do teto da semana e não criam conflito.

### Tema: de onde vem o número na tela
O seletor de potes da página de produto é **por produto** (2 un 5%, 3 un 10%) e é a única escada que
existe desde 13/09 — as escadas por carrinho (15% em 5+, 20% em 8+) foram desativadas. O seletor
deriva o percentual da lista de handles com escada real (`botanika-escada-handles`), então kit
aparece como preço regular sem ninguém precisar lembrar disso.

**Regra que continua valendo:** o percentual e o preço exibidos têm que vir do cálculo real, nunca de
tabela fixa no JavaScript do tema. A barra de progresso ("faltam 2 itens para o brinde") pode ser
tabela fixa, porque só conta itens. O desconto exibido, não.

### Não acumula (se a copy disser que acumula, está errado)
- RECOMPRA10 **não** soma com cupom de influenciadora (os dois são classe PRODUTO — a Shopify
  aceita um cupom por classe). É intencional, está no plano oficial.
- RECOMPRA10 **não** soma com PALPITE12, BRASIL10, VOLTEI10, JOINGLE nem BOTANIKA (classe PEDIDO,
  bloqueados por `pedido = NÃO`).
- **Cupom de influenciadora agora acumula com a escada** (corrigido em 12/09, conforme o plano
  oficial). Consequência de margem: cliente com 8 itens e cupom de influenciadora paga
  0,80 × 0,95 = **24% off**. É o que o plano manda, mas o número é esse.
- **BOTANIKA** está com "combina com" tudo desligado: quem usa BOTANIKA perde a escada e o frete
  da semana. Estado pré-existente. As LPs anunciam esse cupom — vale revisar a copy.

---

## 4. Pendências

| Item | Situação |
|---|---|
| 5% no PIX | **Cancelado em 12/09.** Não entra na campanha. Retirar de toda a copy. |
| Brinde dos 200 primeiros (Manual + Guia da Imunidade) | **Resolvido.** Entrega via ActiveCampaign, fora da Shopify. |
| VICTORIA, JULIACOLARES e FESTEVES não acumulavam com a escada | **Corrigido em 12/09.** Os três agora combinam com desconto de produto, conforme o plano oficial. Históricos preservados (566, 70 e 20 usos). |
| "Cupom de quantidade exclusivo para cliente" | **Resolvido.** Segue a tabela atual, como o briefing manda. Nenhuma tabela nova criada. |
| Escada por produto + escada de volume: soma ou pega a melhor? | **Sem objeto desde 13/09.** As escadas de volume foram desativadas; sobrou só a escada por produto (teto 10%). Nada a testar. |
| Cupom **ANAAMARAL** | **Corrigido em 12/09.** Estava aplicando só no Hair Botanika (1 produto de 12); passou para a coleção `[CUPONS] Todos os Produtos`, igual aos outros 20. Os 2 usos foram preservados. |
| "4 suplementos participantes" (Compre 4, leve 5) | Na configuração **qualquer produto conta**, inclusive kits. Não existe lista de participantes. Ou a copy tira "participantes", ou alguém define a lista e a mecânica é reconfigurada. |
| Acesso antecipado 23/09 com 5% OFF | **Nada configurado.** É pós-semana. Vai precisar de um segmento de quem comprou entre 14 e 19/09 + cupom com "combina com" tudo desligado. |

## 5. Reversão — dia 20/09 a loja volta sozinha

Frete grátis ≥ R$ 349 · 16 escadas por produto com teto de 10% · 6 bumps (3 deles pelos IDs
`[retomada 20/09]`) · cupons de influenciadora · cupons abertos. Nada da Semana do Cliente sobrando.

### 5.1 Reversão do tema — os cards do bump da gaveta

A loja volta sozinha nos descontos, mas **o tema não**. Os três `[BUMP]` que foram encerrados
em 14/09 03:01Z para liberar slots (Hair→Vit C, Vit C/Ômega→TetraVit, Creatina→Whey)
alimentavam **quatro** cards do bump da gaveta. Enquanto não existirem, esses cards mostram
preço cheio e botão "Adicionar ao carrinho", sem prometer desconto.

Depois que as retomadas agendadas entrarem (20/09 03:00Z), abrir
`snippets/botanika-order-bump.liquid` e devolver `deal` aos índices **2, 5, 6 e 8**:

```liquid
assign ob_modes = 'msg,msg,msg,deal,msg,msg,msg,deal,msg' | split: ','
                          ↑2        ↑3       ↑5  ↑6  ↑7  ↑8
```

| # | Gatilho no carrinho | Card oferece | Hoje | Após 20/09 |
|---|---|---|---|---|
| 0 | Whey Chocolate | Creatina | `msg` | `msg` (proposital — brigaria com a escada dos 2 wheys) |
| 1 | Whey Sem Sabor | Creatina | `msg` | `msg` (idem) |
| 2 | Hair | Super Vit C | `msg` | **`deal`** |
| 3 | Tri[Mg] | TetraVit D | `deal` | `deal` (BxGy sem data de fim) |
| 4 | TetraVit D | Ômega 3 | `msg` | `msg` (BxGy desativado em 31/08) |
| 5 | Super Vit C | TetraVit D | `msg` | **`deal`** |
| 6 | Ômega 3 | TetraVit D | `msg` | **`deal`** |
| 7 | Sleep | Tri[Mg] | `deal` | `deal` (BxGy sem data de fim) |
| 8 | Creatina | Whey Chocolate | `msg` | **`deal`** |

**Regra que não se quebra:** um card só pode dizer "−10% só aqui" se o `[BUMP]` BxGy
correspondente estiver ATIVO naquela data. Antes de trocar `msg` por `deal`, conferir o
status no Shopify — não confiar nesta tabela.

### 5.2 Seletor de quantidade da PDP — reverte sozinho

O bloco `blocks/_product-quantity-cards.liquid` passou a **derivar** o percentual
do que existe de desconto automático, em vez de ler o campo "Desconto %" do editor
(que ficou como legado). Regra, sempre a melhor das duas:

| Quantidade | Com escada própria (9 handles) | Sem escada (os 3 kits) |
|---|---|---|
| 2 un | 5% | preço regular |
| 3 un | 10% | preço regular |
| 5 un | 10% (teto) | preço regular |
| 8 un | 10% (teto) | preço regular |

> As linhas de 5 un e 8 un valiam **15%/20%** enquanto as escadas de volume existiam. Elas foram
> **desativadas em 13/09** — hoje o teto é 10% em qualquer quantidade.

Handles com escada própria: `tetravit-d`, `super-omega-3-coq10`, `hair-botanika`,
`super-vitamina-c`, `tri-mg-complex`, `whey-balance-chocolate`,
`whey-balance-sem-sabor`, `sleep-inositol`, `creatina-l-carnitina`.

O bloco ainda tem os ramos `qc_vol` (15% em 5+, 20% em 8+) presos à janela em epoch
(`1789354860` a `1789873200` = 14/09 03:01Z → 20/09 03:00Z). **Hoje são código morto**:
os três cards são 1/2/3 unidades, então `q` nunca passa de 3 e o ramo nunca roda.
Ficaram no lugar de propósito na véspera do lançamento — mexer num arquivo de 25 KB
horas antes de publicar valia menos que o risco. **Limpeza pós-campanha:** remover os
ramos `qc_vol`, senão quem um dia configurar um card de 5 unidades no editor volta a
ver 15% na vitrine sem desconto nenhum atrás. Nada a reverter à mão em 20/09.

> Se um dia os kits ganharem escada própria, basta acrescentar o handle em
> `qc_ladder`, dentro do bloco. Sem isso, card de kit em 2 ou 3 unidades **tem**
> que aparecer como preço regular — era exatamente o que estava errado antes.

### 5.3 Onde ficam os arquivos do tema no repo

O repo **espelha os caminhos da Shopify**: `blocks/`, `sections/`, `snippets/`,
`templates/`, `config/`, `assets/`, `layout/`. É daí que os arquivos sobem para o
tema, e é onde se edita.

Existia também uma pasta `theme-semana/` com cópias achatadas dos mesmos arquivos.
Em **sete** deles as duas versões tinham divergido, e a cópia publicada era sempre
a de `theme-semana/` — quem abrisse o caminho espelhado estaria editando arquivo
morto. A pasta foi consolidada nos caminhos espelhados (cada arquivo conferido
contra o tema antes de mover) e removida.

**Regra:** um arquivo do tema mora num lugar só, no caminho igual ao da Shopify.
Não recriar pasta paralela.

### 4.1 Frete — a única troca manual da campanha

| Desconto | Janela | Mínimo |
|---|---|---|
| `[SEMANA DO CLIENTE] Frete grátis sem mínimo — DESATIVAR À MÃO ao bater 100 pedidos` | 14/09 03:01Z → **20/09 03:00Z** | nenhum |
| `[SEMANA DO CLIENTE] Frete grátis acima de R$ 199,90` | 14/09 03:01Z → 20/09 03:00Z | R$ 199,90 |

Os dois rodam juntos desde a virada. Enquanto o sem-mínimo estiver ativo, **ele ganha**
— a Shopify aplica o melhor frete para o cliente, então no começo é frete grátis para
qualquer valor. No instante em que alguém **desativar o sem-mínimo no admin**, o de
R$199,90 assume sozinho, sem buraco e sem precisar mexer em mais nada.

**Por que o fim mudou.** Ele terminava às 23:59 de 14/09. Com ticket médio de R$299 e a
meta de R$130 mil em 6 dias (~72 pedidos/dia), o pedido nº 100 cairia no meio do dia 2 —
o corte automático quebraria a promessa dos "100 primeiros" sem ninguém ver. O fim foi
estendido até o encerramento da campanha e o controle passou a ser manual, como o
planejamento oficial descreve.

⚠️ **O risco virou o oposto:** se ninguém desativar, é frete grátis sem mínimo a semana
inteira. O título do desconto foi renomeado para gritar isso no admin.

**Bônus dessa desativação: abre 1 vaga na cota de automáticos.** A loja está no teto de 25
(ver a seção da cota). Tentar reativar os bumps encerrados em 13/09 foi recusado com
`ACTIVE_PERIOD_OVERLAP`. Assim que o sem-mínimo sair do ar, dá para trazer **um** bump de volta.

Operação (estende o original até o instante em que o gêmeo `[retomada 20/09]` começa — sem
criar nada novo, sem sobreposição e sem alterar o estado pós-campanha):

```graphql
mutation { discountAutomaticBxgyUpdate(
  id: "gid://shopify/DiscountAutomaticNode/<ID>",
  automaticBxgyDiscount: { endsAt: "2026-09-20T03:00:00Z" }
) { userErrors { field code message } } }
```

Ordem de prioridade, por uso real medido em 13/09:

| Bump | ID do original | Usos | Por dia | Cards da gaveta que destrava |
|---|---|---|---|---|
| Vit C / Ômega → TetraVit D | `1573508743400` | 48 em 23 d | **2,1** | **2** (índices 5 e 6) |
| Hair → Vitamina C | `1572745773288` | 46 em 28 d | 1,6 | 1 (índice 2) |
| Creatina → Whey | `1574087000296` | 21 em 21 d | 1,0 | 1 (índice 8) |

⚠️ **Ao reativar, virar o `ob_modes` correspondente para `deal`** em
`snippets/botanika-order-bump.liquid` — senão a gaveta segue mostrando preço cheio e o
desconto existe sem ninguém saber. O caminho inverso (virar para `deal` sem o desconto
existir) é quebra da regra de ouro: nunca faça isso antes de a mutation passar.

---

## 17/09 — Correção definitiva do brinde (causa raiz encontrada)

### O que estava acontecendo

`snippets/botanika-semana-gift-sync.liquid` roda no navegador e, quando o
carrinho chega a 4 unidades elegíveis, **adiciona sozinho** um pote de Super
Vitamina C (variante 48115368460520, R$ 89,52) via `/cart/add.js`, marcado com
a propriedade `_semana_cliente_brinde`. Na tela ele escreve:

> 🎁 Super Vitamina C adicionada automaticamente
> "O desconto de 100% da promoção será aplicado automaticamente."

Só que o desconto era um **BxGy**, e BxGy **consome** as 4 unidades de
pré-requisito. Quando as escadas por produto já tinham pego essas unidades
(o caso normal, porque só um desconto se aplica por unidade), o BxGy não
podia disparar — e o pote ficava no carrinho **cobrado**.

Ou seja: a loja colocava um produto pago no carrinho da cliente por conta
própria, prometia que era grátis, e cobrava. Três clientes reclamaram
(14–17/09). Não era "desconto que não aplicou": era cobrança indevida.

Agravante: a lista `eligible` do script inclui `9558490448104`
(Kit da Imunidade), que **não estava** na lista do BxGy. Dava para bater as
4 unidades com um produto que o desconto nem aceitava.

### A correção

Trocado o mecanismo do brinde:

| | antes | depois |
|---|---|---|
| tipo | BxGy "compre 4, leve 5" | desconto de produto, valor fixo |
| valor | 100% em 1 Super Vitamina C | **R$ 89,52** na Super Vitamina C |
| condição | 4 unidades de pré-requisito | **subtotal ≥ R$ 300** |
| consome unidades? | **sim** — matava as escadas | **não** |

`gid://shopify/DiscountAutomaticNode/1581910425832` — ACTIVE até 20/09 03:00Z,
`combinesWith` produto/pedido/frete todos `true`, `appliesOnEachItem: false`
(aplica uma vez por pedido).

O BxGy `1580105367784` foi encerrado (`endsAt` = 2026-09-17T13:55:00Z,
33 usos no total).

**Por que R$ 300:** o pior caso de "4 unidades" é 4× Tri[Mg] (o mais barato,
R$ 87,50) = R$ 350, que com os 10% da escada vira **R$ 315**. Qualquer teto
acima disso deixaria de entregar o brinde para quem cumpriu a regra. R$ 300
nunca sub-entrega.

**Vazamento conhecido, aceito:** um carrinho de 3 unidades acima de R$ 300
que contenha uma Super Vitamina C também ganha o desconto (ex.: 2 Ômega +
1 Vit C). Sobre-entrega, nunca sub-entrega — e a regra do projeto é que o
cliente nunca veja um preço que o checkout não honra. Se incomodar, o número
é um campo só.

### Ainda pendente (não autorizado)

- `blocks/_product-quantity-cards.liquid`, `snippets/botanika-semana-cart.liquid`
  e `snippets/botanika-semana-gift-sync.liquid` anunciam **"+5% OFF adicional
  no PIX"**. Esse desconto **não existe** na Shopify — varredura completa em
  automáticos e cupons ativos não achou nada de PIX. É promessa sem lastro,
  em três lugares.
- O painel de confiança diz "Frete grátis acima de R$349" enquanto a caixa da
  campanha diz "a partir de R$ 199,90", na mesma página.
- Escrita em tema publicado é bloqueada pela política do servidor MCP; essas
  correções têm que sair pelo admin ou num tema duplicado.
