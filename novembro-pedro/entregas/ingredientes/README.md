# Seção "Ingredientes" nas páginas de produto (07/11)

- **Fonte:** PDF "BOTANIKA_COMPLETO" (catálogo GSA), recebido pelo Pedro em 07/11. Texto copiado do campo INGREDIENTES de cada página.
- **Onde fica o texto:** no campo do produto `custom.ingredientes` (definição "Ingredientes (rótulo)"), que também pode ser editado no admin.
  - Formato: uma linha por cartão, `Título|texto`.
  - Uma linha `selo|texto` vira etiqueta (por exemplo, "Não contém glúten").
  - Gravado em 21 produtos: 17 avulsos e 4 kits. Nos kits há um cartão por produto.
- **Seção:** `sections/bk-pdp.liquid`, renderizada logo abaixo do "O que diz o rótulo" (dentro do bloco `specs`).
  - Título "Ingredientes · Do que é feito".
  - Fórmula e cápsula em lista; selos no fim.
- **Temas com a seção:**
  - Cópia do tema no ar (168436498664);
  - OFICIAL (168106000616), que volta em 01/12;
  - 11/11 (168318599400).
  - Tema da Week (168321417448): seção aplicada em 09/11, com o ok do Pedro, e testada na prévia.
  - O tema antigo do Esquenta (168360411368, agora 🗑️ APAGAR) não foi alterado.
- **Fora do PDF:** Ômega 3 (60 cápsulas) e Vitamina B12+B9 estão no catálogo, mas não estão ativos na loja.
- `ingredientes.py` gera os valores (`python3 ingredientes.py ids.json`).
