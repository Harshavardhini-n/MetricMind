from pydantic import BaseModel


class MetricRequest(BaseModel):
    metric: str
    dimension: str | None = None
    filters: dict | None = None


class MetricResponse(BaseModel):
    metric: str
    value: float
    unit: str
    dimension: str | None = None