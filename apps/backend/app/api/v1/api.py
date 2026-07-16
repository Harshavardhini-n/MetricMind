from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get(
    "/health",
    tags=["Health"],
    summary="Health Check",
    description="Returns application health status.",
)
async def health():
    return {
        "success": True,
        "data": {
            "status": "healthy",
            "environment": settings.ENVIRONMENT,
            "version": settings.APP_VERSION,
        },
        "message": "MetricMind API is running",
    }