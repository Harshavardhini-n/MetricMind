from app.models.semantic import MetricResponse


class SemanticTool:

    MOCK_DATA = {
        "revenue": 1850000,
        "margin": 32.4,
        "cost": 1250000,
        "profit": 600000,
    }

    @classmethod
    def query_metric(cls, metric: str):

        value = cls.MOCK_DATA.get(metric.lower())

        if value is None:
            return None

        return MetricResponse(
            metric=metric,
            value=value,
            unit="USD"
        )