from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama_service import OllamaService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
    summary="Chat with MetricMind",
)
async def chat(request: ChatRequest):

    answer = OllamaService.generate_response(request.message)

    return ChatResponse(response=answer)