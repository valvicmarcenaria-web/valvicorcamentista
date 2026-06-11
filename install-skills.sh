#!/usr/bin/env bash
# Instala as skills da Valvic (Marcos + Lavinia) na BASE GERAL do Claude Code
# (~/.claude/skills), deixando-as disponíveis em todos os seus projetos.
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
    cp -r "$SRC/$s" "$DEST/$s"
    echo "  ✓ $s"
  else
    echo "  ✗ não encontrada: $SRC/$s"
  fi
done
echo "Concluído. Se não aparecerem no menu, reinicie o Claude Code (nova pasta de skills)."
