#!/usr/bin/env bash
# Instala as skills da Valvic (Marcos + Lavinia) na BASE GERAL do Claude Code
# (~/.claude/skills), deixando-as disponíveis em todos os seus projetos.
#
# Copia apenas o essencial — exclui fontes/ (arquivos pesados de referência
# que ficam no repositório, não precisam ir para a base pessoal).
#
# Uso (na SUA máquina, dentro do repositório):
#   bash install-skills.sh
#
# Depois, reinicie o Claude Code se as skills não aparecerem de imediato.
set -euo pipefail

DEST="$HOME/.claude/skills"
SRC="$(cd "$(dirname "$0")" && pwd)/.claude/skills"
SKILLS=("orcamentista-marcenaria" "leitor-projetos-marcenaria")

mkdir -p "$DEST"
echo "Instalando skills da Valvic em: $DEST"

for s in "${SKILLS[@]}"; do
  if [ -d "$SRC/$s" ]; then
    rm -rf "${DEST:?}/$s"
    mkdir -p "$DEST/$s"

    # Copia tudo exceto fontes/ (PDFs/HTML pesados — ficam só no repo)
    if command -v rsync &>/dev/null; then
      rsync -a --exclude='fontes/' "$SRC/$s/" "$DEST/$s/"
    else
      # fallback sem rsync: copia subdiretórios um a um, pulando fontes/
      cp "$SRC/$s/SKILL.md" "$DEST/$s/" 2>/dev/null || true
      for sub in referencias dados ferramentas projetos; do
        [ -d "$SRC/$s/$sub" ] && cp -r "$SRC/$s/$sub" "$DEST/$s/$sub"
      done
    fi

    echo "  ✓ $s"
  else
    echo "  ✗ não encontrada: $SRC/$s"
  fi
done

echo "Concluído. Se não aparecerem no menu, reinicie o Claude Code (nova pasta de skills)."
