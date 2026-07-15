from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Agentic Semantic BI Backend",
)


@app.on_event("startup")
async def startup_event():
    logger.info("MetricMind API started successfully")


@app.get("/")
async def root():
    return {"message": "Welcome to MetricMind API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}