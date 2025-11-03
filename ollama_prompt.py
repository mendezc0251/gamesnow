import subprocess, json

def call_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True, text=True
    )
    return result.stdout