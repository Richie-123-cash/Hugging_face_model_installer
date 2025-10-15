#!/usr/bin/env python3
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
from pathlib import Path

# 1️⃣ Ask user for model ID
model_id = input("Paste the Hugging Face model ID: ").strip()

# 2️⃣ Set dedicated folder for this model
base_dir = Path.cwd() / "AI_models" / model_id.replace("/", "_")
base_dir.mkdir(parents=True, exist_ok=True)

# 3️⃣ Load tokenizer and model
print(f"Downloading and loading {model_id} into {base_dir}...")
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=base_dir)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16,
    cache_dir=base_dir
)

# 4️⃣ Confirm ready
print(f"Model {model_id} loaded on {model.device}.")

# 5️⃣ Optional: interactive text generation
use_generation = input("Do you want to generate text now? (y/n): ").strip().lower()
if use_generation == "y":
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
    while True:
        prompt = input("\nEnter prompt (or 'exit' to quit): ")
        if prompt.lower() in ["exit", "quit"]:
            break
        output = generator(prompt, max_new_tokens=100)
        print("\nGenerated Text:\n", output[0]["generated_text"])
