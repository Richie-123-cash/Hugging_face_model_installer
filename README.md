# Hugging Face Model Installer & Runner

A simple Python script to download any Hugging Face model and optionally generate text locally.

## Requirements
- Python 3.10+  
- Pip

## Installation

1. Clone the repo:
```bash
git clone https://github.com/yourusername/hugging_face_model_installer.git
cd hugging_face_model_installer
``` 
2. Install dependencies: 
```bash 
pip install -r requirements.txt
```
Usage: 
```bash 
python run_model.py
```
   1.  Paste the Hugging Face model ID (e.g., gpt2).

   2.  Wait for download & loading.

   3.  Optional: generate text interactively.

Notes: 
    Models are stored in AI_models/<model_name>/.

    Works with CPU or GPU automatically.

    Works with any Transformers model.
