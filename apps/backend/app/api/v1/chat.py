from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent_service import AgentService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
    summary="Chat with MetricMind",
)
async def chat(
    request: ChatRequest,
):

    answer = AgentService.ask(
        request.message
    )

    return ChatResponse(
        response=answer
    )