#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

REQUIRED_DIRS=(
  "Drawings"
  "Data_Raw"
  "Schedules"
  "Specs"
  "Code_Research"
)

for rel_dir in "${REQUIRED_DIRS[@]}"; do
  mkdir -p "$ROOT_DIR/$rel_dir"
done

TEMPLATE_PATH="$ROOT_DIR/Templates/agent.template.md"
AGENT_PATH="$ROOT_DIR/agent.md"

if [[ ! -f "$TEMPLATE_PATH" ]]; then
  echo "ERROR: missing template at $TEMPLATE_PATH" >&2
  exit 1
fi

if [[ ! -f "$AGENT_PATH" ]]; then
  cp "$TEMPLATE_PATH" "$AGENT_PATH"
  echo "Created $AGENT_PATH"
else
  echo "Preserved existing $AGENT_PATH"
fi

echo "Project workspace bootstrap complete in: $ROOT_DIR"
