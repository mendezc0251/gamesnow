import subprocess, json

def call_llm(prompt):
    
    result = subprocess.run([
    r"C:\Users\Cris\AppData\Local\Programs\Ollama\ollama.exe",
    "run", "llama3", prompt
], capture_output=True, text=True)
    
    return result.stdout