# Botanika — repositório de Landing Pages

Este repositório contém as **landing pages premium da Botanika** (marca brasileira de suplementos).
Cada produto tem sua **própria pasta** e sua **própria identidade visual** — nunca clonar uma LP para outro produto.

## ⚠️ LEIA ANTES DE CRIAR OU EDITAR QUALQUER LP

Sempre que a tarefa envolver **criar ou editar uma landing page**, leia primeiro, nesta ordem:

1. **`PAGINAS.md`** — mapa de todas as LPs (pasta, link, VARIANT_ID, preço, identidade, status). Confirme com o usuário qual pasta vai mexer antes de começar.
2. **`botanika-lp-superprompt.md`** — guia de construção: design system, interações, regras de commerce, publicação.
3. **`botanika-lp-kit/`** — base de conhecimento para criação:
   - `botanika-lp-kit/prompts/` — repertório de referência (recreações getlayers e outros prompts). **Use só como inspiração de técnica** (shaders, canvas de partículas, reveals, grids em rem, springs). **NUNCA copiar** um desses direto para uma LP da Botanika — cada produto precisa de identidade própria.
   - `botanika-lp-kit/zips/` — arquivos `.zip` que o usuário deixa como base de conhecimento (assets, referências, exports). Se houver zips relevantes ao produto, descompacte/leia antes de construir.

## Convenções fixas (não quebrar)

- **Uma pasta por produto:** `landing-<slug>/index.html` — HTML **autocontido** (CSS+JS inline, sem build).
- Deve funcionar no **Safari mobile via URL ao vivo**. `html{overflow-x:hidden}` na raiz (não só no body).
- Validar antes de commitar: `node --check` nos blocos `<script>` não-módulo + checagem de balanço de tags.
- **Branch de publicação:** `lp`. Link fixo: `https://raw.githack.com/BotanikaHub/Botanika-Desing/lp/landing-<slug>/index.html`.
- **Checkout Shopify:** `https://botanikabrasil.com.br/cart/<VARIANT_ID>:<QTD>`. Cupom `BOTANIKA` 5% OFF. Frete grátis > R$349.
- **Fonte da verdade do produto:** Shopify (variant/preço) + Google Drive (rótulo/caixa/depoimentos). Cada produto DEVE ter identidade própria (paleta/fundo/fonte/assinatura).
- **Nunca** colocar o identificador do modelo em commits, PRs ou código.

## Como o usuário edita uma LP específica (comando pra colar em chat novo)

> "Leia o `PAGINAS.md`, o `botanika-lp-superprompt.md` e a pasta `botanika-lp-kit/` no repo `botanikahub/botanika-desing`. Vou editar a LP do **[produto]**. Me confirma qual pasta/arquivo você vai mexer antes de começar."

## 🎬 Edição de vídeo — skills instaladas (`.claude/skills/`)

Pacote de skills de edição de vídeo, carregado automaticamente em toda sessão do Claude Code neste repo.
Sempre que a tarefa envolver **edição de vídeo** (criativos, anúncios, Reels/TikTok, Remotion), use a skill que corresponde ao pedido:

| Skill | Quando usar |
| --- | --- |
| `cp-extratora-de-referencia` | Analisar um vídeo de referência e gerar o pacote (relatório, CSV de cenas, receita JSON, prompt de recriação) |
| `cp-estilo-por-referencia` | Aplicar a linguagem de uma referência ao vídeo próprio da Botanika, sem copiar conteúdo de terceiros |
| `cp-direcao-de-edicao` | Decidir o que mostrar, quando cortar, alternar apresentador / demonstração / apoio visual |
| `cp-motion-explicativo` | Motion graphics que explicam processos, causa e efeito, comparações (inclui 3D com fallback) |
| `cp-apresentador-em-cena` | Enquadramento, moldura, tracking e recorte alfa do apresentador |
| `cp-lettering-com-hierarquia` | Tipografia animada, títulos cinéticos, chamadas e CTA |
| `cp-variacoes-controladas` | Variações de um criativo aprovado (abertura, título, CTA) com matriz rastreável |

Regras para vídeos da Botanika: usar a identidade visual do produto (mesma fonte da verdade das LPs: Shopify + Google Drive), nunca inventar resultados, depoimentos ou ofertas, e não usar serviços pagos sem autorização.
Para editar ou adicionar uma skill: altere o `SKILL.md` na pasta correspondente em `.claude/skills/` e faça commit.
