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
| Escada Volume — 15% (5+ itens) | `DiscountAutomaticNode/1577084682472` | 14/09 00h01 → 20/09 00h00 | SIM / SIM / SIM |
| Escada Volume — 20% (8+ itens) | `DiscountAutomaticNode/1577084715240` | 14/09 00h01 → 20/09 00h00 | SIM / SIM / SIM |

**RECOMPRA10** é classe PRODUTO (aplicado sobre a coleção `[CUPONS] Todos os Produtos`, não sobre
"todos os produtos" — se fosse "todos os produtos" a Shopify o classificaria como classe PEDIDO e o
bloqueio contra o cupom de influenciadora deixaria de existir). Sem limite de uso, sem
"uma vez por cliente".

**Aberto a qualquer cliente** (decisão de 12/09). A restrição por segmento foi removida porque exigia
que a pessoa estivesse logada com o e-mail da compra anterior, o que gerava recusa no carrinho. Em
troca: **se o código vazar, funciona para cliente novo também** — com a escada de 20% chega a 28% off.
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

⚠️ **Não sobrou vaga.** Durante a campanha a loja volta a 25/25 automáticos: 16 escadas por produto +
3 bumps + Upsell.com + 2 escadas de volume + 3 da campanha. Qualquer desconto automático novo durante
a semana (relâmpago, kit, coleção) exige pausar outro antes. Cupom não entra nessa cota.

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
- **Qualquer percentual somado do tipo "até 25%".** A soma da escada por produto com a escada de
  volume não foi testada. Só anunciar número que tenha sido visto num carrinho real.

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
- **As escadas de 15% (5+ itens) e 20% (8+ itens) são novas da semana** e não estão na mensagem
  oficial, que fala em "seguir a mecânica que já temos atualmente". É o maior gancho de ticket da
  campanha. O tema precisa mostrar os degraus.
- **"Os 100 primeiros pedidos" não é contagem, é horário** (segunda 14/09 até 23h59). Comunicar como
  contagem gera reclamação de quem comprar na terça.
- **RECOMPRA10 é cupom e exige login** com o e-mail que tem pedido anterior. O código precisa
  aparecer na copy, junto com a instrução de entrar na conta.

### Contradição comercial — resolvida
PALPITE12, BRASIL10, VOLTEI10 e RECUPERA10 foram pausados (ver seção 2). Durante a campanha, nenhum
cupom aberto empata ou supera a condição da base. Os que continuam no ar — JOINGLE, ELAINE, LUCCA
(5%), BOTANIKA (5%, não acumula com nada), ALUNO10, ALUNONOVA15, VOLTA5, VOLTA10, RECUPERA10ZAP e
RECUPERA10MAIL — ficam abaixo dos 28% da recompra e não criam conflito.

### Tema: de onde vem o número na tela
O seletor de potes da página de produto é **por produto** (2 un 5%, 3 un 10%). As escadas de 15% e 20%
são **por carrinho** (5+ e 8+ itens de qualquer produto). Quem leva 3 Hair + 2 Creatina tem 5 itens e
entra em 15% — e o tema hoje não conta isso em lugar nenhum.

**Regra:** o percentual e o preço exibidos têm que vir do cálculo real do carrinho da Shopify, nunca
de tabela fixa no JavaScript do tema. Enquanto não soubermos se a escada por produto soma com a de
volume, qualquer conta hardcoded pode mostrar um número que o checkout não confirma. A barra de
progresso ("faltam 2 itens para 15% OFF") pode ser tabela fixa, porque só conta itens. O desconto
exibido, não.

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
| Escada por produto + escada de volume: soma ou pega a melhor? | **Em aberto.** Sem teste. Enquanto não for verificado num carrinho real, não anunciar percentual somado. |
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
| 5 un | **15%** (volume, só na semana) | **15%** (volume, só na semana) |
| 8 un | **20%** (volume, só na semana) | **20%** (volume, só na semana) |

Handles com escada própria: `tetravit-d`, `super-omega-3-coq10`, `hair-botanika`,
`super-vitamina-c`, `tri-mg-complex`, `whey-balance-chocolate`,
`whey-balance-sem-sabor`, `sleep-inositol`, `creatina-l-carnitina`.

A janela do volume está fixa no código como epoch (`1789354860` a `1789873200`,
= 14/09 03:01Z → 20/09 03:00Z). **Depois de 20/09 o card volta sozinho** para os
10% da escada por produto — e para "preço regular" nos kits. Nada a reverter à mão.

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
