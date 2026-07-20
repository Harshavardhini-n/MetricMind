from ollama import chat
from app.core.config import settings

class OllamaService:from app.core.config import settings

    @staticmethod
    def generate_response(prompt: str) -> str:
        response = chat(
            model=settings.OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]