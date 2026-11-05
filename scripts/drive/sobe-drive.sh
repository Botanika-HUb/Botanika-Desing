#!/usr/bin/env bash
# Sobe arquivos para o Drive pelo receptor do Apps Script (guia: scripts/drive/README.md).
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
