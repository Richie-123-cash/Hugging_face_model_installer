#!/usr/bin/env bash
echo "🔧 Installing HuggingFace Model Installer dependencies..."
pip install -r requirements.txt
echo "✅ Done. Run it with: python -m hfmi --model <model_id> --generate"
