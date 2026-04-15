import os
import requests

class LLMService:
    @staticmethod
    def generate_text(prompt: str) -> str:
        try:
            url = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
            response = requests.post(
                f"{url}/api/generate",
                json={"model": "llama3.1:8b", "prompt": prompt, "stream": False},
                timeout=300
            )
            return response.json().get("response", "AI summary unavailable.")
        except Exception as e:
            return f"LLM Error: {str(e)}"

llm_service = LLMService()
