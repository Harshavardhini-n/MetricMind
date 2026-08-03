from langchain_ollama import ChatOllama

from app.agent.prompts import build_prompt
from app.core.config import settings


def create_chain():
    llm = ChatOllama(
        model=settings.OLLAMA_MODEL,
        base_url=settings.OLLAMA_HOST,
        temperature=0,
    )

    prompt = build_prompt()

    return prompt | llm