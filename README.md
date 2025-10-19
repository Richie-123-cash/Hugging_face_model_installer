# 🤖 HuggingFace Model Installer (HFMI)

A lightweight CLI tool to **download, organize, and test Hugging Face models** locally.

## 🧭 Features
- Easy one-command model installation.
- Automatic folder management (`AI_models/`).
- Optional interactive text generation.
- Metadata logging for every model.

## 🚀 Usage
```bash
python -m hfmi --model meta-llama/Llama-3-8b --generate
```
Or, run without flags for interactive prompts: 
```bash 
python -m hfmi
```
All downloaded models are stored under AI_models/<model_id>/ .

##Installation 
```bash 
bash install.sh 
```
