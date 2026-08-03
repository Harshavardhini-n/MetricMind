from pydantic import BaseModel


class RankingResponse(BaseModel):
    metric: str
    unit: str

    values: dict[str, float]

    highest_region: str
    highest_value: float

    lowest_region: str
    lowest_value: float