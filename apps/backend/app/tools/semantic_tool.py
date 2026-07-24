from app.catalog.metrics import METRICS
from app.models.semantic import MetricResponse


class SemanticTool:

    @classmethod
    def query_metric(cls, metric, dimension=None):

        metric = metric.lower()

        if metric not in METRICS:
            return None

        info = METRICS[metric]

        if dimension:

            dimension = dimension.lower()

            if dimension not in info["dimensions"]:
                return None

            value = info["dimensions"][dimension]

        else:

            value = sum(info["dimensions"].values())

        return MetricResponse(
            metric=metric,
            value=value,
            unit=info["unit"],
            description=info["description"],
            dimension=dimension,
        )