import ollama
import time

def query_ollama(prompt, model="llama3.2"):
    """Robust Ollama query with retries"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = ollama.chat(
                model=model,
                messages=[{
                    'role': 'user',
                    'content': prompt + "\n\nIMPORTANT: Only output the requested content with absolutely no additional text."
                }],
                options={
                    'temperature': 0,
                    'seed': 42,
                    'num_ctx': 8192
                }
            )
            return response['message']['content'].strip()
        except Exception as e:
            if attempt == max_retries - 1:
                raise RuntimeError(f"Ollama query failed after {max_retries} attempts: {str(e)}")
            time.sleep(1 * (attempt + 1))