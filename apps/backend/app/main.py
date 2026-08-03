from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import router as api_router
from app.core.config import settings
from app.core.logging import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Agentic Semantic BI Backend",
    contact={
        "name": "MetricMind Team",
        "email": "team@metricmind.dev"
    },
    license_info={
        "name": "MIT"
    },
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("MetricMind API started successfully")


@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }


app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX,
)