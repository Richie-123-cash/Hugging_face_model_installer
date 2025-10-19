#!/usr/bin/env bash
# run.sh — launch HFMI easily from repo root
# Usage:
#   ./run.sh --model meta-llama/Llama-3-8b --generate
#   ./run.sh meta-llama/Llama-3-8b           # positional model id (legacy)
#
# The script runs python -m hfmi with whatever flags you pass.

set -euo pipefail

# Resolve script dir (so you can run from anywhere)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$SCRIPT_DIR"

# If first arg doesn't start with -- and looks like a model id (contains a slash),
# allow short form: ./run.sh meta-llama/Llama-3-8b -> translate to --model <id>
if [[ $# -ge 1 && "$1" != --* && "$1" == */* ]]; then
  MODEL_ID="$1"
  shift
  set -- --model "$MODEL_ID" "$@"
fi

exec python -m hfmi "$@"
