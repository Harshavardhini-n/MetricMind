from app.catalog.metrics import METRICS
from app.models.semantic import MetricResponse


class SemanticTool:

    @classmethod
    def query_metric(cls, metric: str):

        metric = metric.lower()

        if metric not in METRICS:
            return None

        data = METRICS[metric]

        return MetricResponse(
            metric=metric,
            value=data["value"],
            unit=data["unit"],
            description=data["description"]
        )