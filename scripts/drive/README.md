# Como o Claude sobe vídeos editados para o Google Drive

Guia para outro Claude (ex.: Botanika) fazer o mesmo que o Claude da Revita: editar e **subir o vídeo
pronto direto numa pasta do Drive**, a partir de um link de pasta.

## Por que "só mandar o link da pasta" não funciona

- O conector do Google Drive do Claude **lê e procura** arquivos, mas **não sobe vídeo** (não envia
  arquivos binários grandes). Por isso o Claude diz que não consegue.
- O container do Claude Code na nuvem não tem login do Google. Ele precisa de um "receptor" do lado
  do Google que aceite o arquivo e grave na pasta.

A solução: um **App da Web no Google Apps Script** (roda com a conta Google de vocês e grava no Drive)
+ um script `sobe-drive.sh` que manda o vídeo para ele com `curl`.

## Configuração única (feita por uma pessoa, ~10 min)

### 1. Criar o receptor no Apps Script
1. Com a conta Google que tem acesso às pastas da Botanika, abra https://script.google.com → **Novo projeto**.
   Nome sugerido: "Botanika Upload Claude".
2. Apague o conteúdo e cole o código abaixo.
3. Troque `TOKEN` por uma senha longa (só letras e números, sem espaços) e `FOLDER_ID` pelo ID da pasta
   padrão de entrega (o ID é o trecho depois de `/folders/` no link da pasta).
4. **Implantar → Nova implantação → tipo "App da Web"**:
   - Executar como: **Eu**
   - Quem pode acessar: **Qualquer pessoa**
   - Autorize o acesso ao Drive quando pedir.
5. Copie a **URL do App da Web** (termina em `/exec`).

```javascript
/**
 * Receptor de uploads do Claude -> Google Drive.
 * Publicado como App da Web: "Executar como: eu" / "Quem pode acessar: qualquer pessoa".
 * Só aceita envios que tragam o TOKEN abaixo.
 */
const FOLDER_ID = 'ID-DA-PASTA-PADRAO';            // pasta de entrega padrão
const TOKEN = 'TROQUE-POR-UMA-SENHA-LONGA';        // a mesma de DRIVE_UPLOAD_TOKEN

function doPost(e) {
  const p = e.parameter || {};
  if (p.token !== TOKEN) return out({ ok: false, error: 'token invalido' });
  if (!p.name) return out({ ok: false, error: 'falta o nome do arquivo' });
  const folder = DriveApp.getFolderById(p.folder || FOLDER_ID);
  if (p.replace === '1') {                          // --replace: manda a versão antiga para a lixeira
    const old = folder.getFilesByName(p.name);
    while (old.hasNext()) old.next().setTrashed(true);
  }
  const bytes = Utilities.base64Decode(e.postData.contents);
  const file = folder.createFile(Utilities.newBlob(bytes, p.mime || 'video/mp4', p.name));
  return out({ ok: true, id: file.getId(), url: file.getUrl(), size: file.getSize() });
}

function doGet(e) {                                 // teste: ?token=...[&folder=ID]
  const p = (e && e.parameter) || {};
  if (p.token !== TOKEN) return out({ ok: false, error: 'token invalido' });
  return out({ ok: true, folder: DriveApp.getFolderById(p.folder || FOLDER_ID).getName() });
}

function out(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
```

> Se mudar o código depois, é preciso **Implantar → Gerenciar implantações → editar → Nova versão**,
> senão a URL continua rodando a versão antiga.

### 2. Dar acesso às pastas
A conta Google que publicou o script grava os arquivos. Ela precisa ser **Editor** de toda pasta para onde
o Claude vai subir (em Drive compartilhado: "Administrador de conteúdo" ou acima). Pasta de outra conta que
não foi compartilhada com ela dá erro de acesso.

### 3. Configurar o ambiente do Claude Code (claude.ai/code → ambiente da Botanika → configurações)
- **Variáveis de ambiente**:
  - `DRIVE_UPLOAD_URL` = a URL `/exec` do passo 1
  - `DRIVE_UPLOAD_TOKEN` = a senha do `TOKEN`
- **Rede (domínios liberados)**: `script.google.com`, `script.googleusercontent.com`
  (o upload) e, para baixar os brutos do Drive, `drive.google.com`, `drive.usercontent.google.com`.
  Para transcrever com whisper: `huggingface.co`, `*.huggingface.co`, `*.hf.co`.
- **Abra uma sessão nova** depois de salvar: as variáveis só entram em sessões criadas depois.

## O script de envio (`scripts/drive/sobe-drive.sh`)

Salve no repositório da Botanika e dê permissão de execução (`chmod +x`).

```bash
#!/usr/bin/env bash
# Sobe arquivos para o Drive pelo receptor do Apps Script.
# Requer DRIVE_UPLOAD_URL e DRIVE_UPLOAD_TOKEN no ambiente.
# Uso: scripts/drive/sobe-drive.sh [--replace] [--folder ID] arquivo1.mp4 [arquivo2.mp4 ...]
#      scripts/drive/sobe-drive.sh --check
set -euo pipefail
: "${DRIVE_UPLOAD_URL:?defina DRIVE_UPLOAD_URL}"; : "${DRIVE_UPLOAD_TOKEN:?defina DRIVE_UPLOAD_TOKEN}"
replace=0; folder=""; falhas=0
if [[ "${1:-}" == "--check" ]]; then
  curl -sSL --get "$DRIVE_UPLOAD_URL" --data-urlencode "token=$DRIVE_UPLOAD_TOKEN"; echo; exit 0
fi
while [[ "${1:-}" == --* ]]; do
  case "$1" in --replace) replace=1; shift;; --folder) folder="$2"; shift 2;; *) echo "opção desconhecida $1"; exit 2;; esac
done
for f in "$@"; do
  size=$(stat -c%s "$f")
  if (( size > 36000000 )); then echo "ERRO: $f tem $((size/1000000)) MB (limite ~36 MB do Apps Script)"; falhas=$((falhas+1)); continue; fi
  tmp=$(mktemp); base64 -w0 "$f" > "$tmp"
  echo -n "subindo $(basename "$f") ($((size/1000000)) MB)... "
  # sem -X POST: o Apps Script responde 302 e o curl precisa seguir o redirecionamento com GET
  resp=$(curl -sSL "$DRIVE_UPLOAD_URL?$(python3 -c 'import sys,urllib.parse as u; print(u.urlencode({k:v for k,v in [("token",sys.argv[1]),("name",sys.argv[2]),("replace",sys.argv[3]),("folder",sys.argv[4])] if v}))' "$DRIVE_UPLOAD_TOKEN" "$(basename "$f")" "$replace" "$folder")" \
       -H "Content-Type: text/plain" --data-binary @"$tmp") || resp="falha no curl"
  rm -f "$tmp"
  if [[ "$resp" == *'"ok":true'* ]]; then echo "$resp"; else echo "ERRO: ${resp:0:200}"; falhas=$((falhas+1)); fi
done
(( falhas == 0 ))
```

## Como o Claude usa (no dia a dia)

1. Testar: `scripts/drive/sobe-drive.sh --check` → deve responder `{"ok":true,"folder":"<nome da pasta padrão>"}`.
2. Receber o link da pasta do usuário, ex. `https://drive.google.com/drive/folders/1Mjh0SMx...`
   → o **ID** é o trecho depois de `/folders/` (sem `?usp=...`).
3. Subir: `scripts/drive/sobe-drive.sh --folder <ID> "Nome - Tema - Botanika 9x16.mp4" ...`
   - cada arquivo responde `{"ok":true,"id":...,"url":...}` → mandar o `url` ao usuário;
   - versão nova de um arquivo já enviado: `--replace` (a antiga vai para a lixeira).
4. Conferir com o conector do Drive (`search_files` com `parentId = '<ID>'`) que os arquivos estão lá.

**Arquivos:** até ~36 MB cada (o vídeo vai em base64 e o Apps Script aceita ~50 MB por envio).
Na prática, entregar vídeos com **menos de 30 MB** (H.264, 2 passadas com a taxa calculada pela duração).

## Erros comuns

| Mensagem | Causa | Como resolver |
|---|---|---|
| `defina DRIVE_UPLOAD_URL` / variáveis vazias | sessão aberta antes de criar as variáveis | abrir uma sessão nova |
| `CONNECT tunnel failed, response 403` | domínio fora da lista de rede do ambiente | liberar `script.google.com` e `script.googleusercontent.com` |
| `token invalido` | `TOKEN` do script diferente de `DRIVE_UPLOAD_TOKEN` | igualar os dois (e reimplantar se mudou o código) |
| erro de acesso / "Exception: ... getFolderById" | a conta do script não é Editor da pasta | compartilhar a pasta com essa conta como Editor |
| resposta em HTML de login do Google | implantação com acesso restrito | reimplantar com "Quem pode acessar: Qualquer pessoa" |
| `ERRO: ... limite ~36 MB` | arquivo grande demais | recomprimir abaixo de 30 MB |
| resposta antiga / sem efeito depois de mudar o código | URL ainda na versão anterior | Gerenciar implantações → editar → Nova versão |

## Segurança
- O token é a "senha" do receptor: guardar só nas variáveis do ambiente, nunca no repositório nem em mensagens.
- Quem tem URL + token consegue gravar nas pastas que a conta do script acessa. Se vazar, troque o `TOKEN`
  no script (nova versão) e na variável do ambiente.
