import os
from llama_cpp import Llama

# ✅ Path to locally stored LLaMA 2 GGUF model
MODEL_PATH = "../simple_code_summary/models/llama-2-7b-chat.gguf"

# ✅ Load the LLaMA 2 model with GPU acceleration
llm = Llama(model_path=MODEL_PATH, n_ctx=4096, n_gpu_layers=50, verbose=True)

# ✅ Load the Markdown documentation file
MD_FILE_PATH = "project_documentation.md"
if not os.path.exists(MD_FILE_PATH):
    raise FileNotFoundError(f"Markdown file '{MD_FILE_PATH}' not found!")

with open(MD_FILE_PATH, "r", encoding="utf-8") as file:
    md_content = file.read()

# ✅ Truncate input to fit within 4096 tokens
MAX_INPUT_CHARS = 3000  # Adjust based on model capacity
truncated_content = md_content[:MAX_INPUT_CHARS]

# ✅ Construct the prompt for summarization & function descriptions
prompt = f"""
You are an expert technical writer. Given the structured documentation below, generate:
1. A **concise file-level summary** for each file.
2. **Conversational function descriptions** in plain English.

---
### Extracted Documentation (Truncated to fit model):
{truncated_content}

---
### Instructions:
- Summarize each file in **2-3 sentences**.
- Rewrite function descriptions in a **natural, conversational tone**.
- Keep a **structured, Markdown-friendly format**.

Now, generate the improved documentation:
"""

# ✅ Run the model to generate improved documentation
print("🔄 Generating improved documentation, please wait...")
output = llm(prompt, max_tokens=1024, temperature=0.7, top_p=0.9)  # Reduce max_tokens

# ✅ Extract the generated text
generated_text = output["choices"][0]["text"]

# ✅ Save the improved documentation to a new file
IMPROVED_MD_FILE = "improved_project_documentation.md"
with open(IMPROVED_MD_FILE, "w", encoding="utf-8") as file:
    file.write(generated_text)

print(f"✔ Documentation saved as '{IMPROVED_MD_FILE}'")
