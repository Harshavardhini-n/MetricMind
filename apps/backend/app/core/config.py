from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "MetricMind API"
    APP_VERSION: str = "1.0.0"


settings = Settings()