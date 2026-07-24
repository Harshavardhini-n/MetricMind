from app.catalog.metrics import METRICS
from app.models.semantic import MetricResponse


class SemanticTool:

    @classmethod
    def query_metric(cls, metric, dimension=None, period=None):

        metric = metric.lower()

        if metric not in METRICS:
            return None

        info = METRICS[metric]

        data = info["dimensions"]

        if dimension:

            dimension = dimension.lower()

            if dimension not in data:
                return None

            region = data[dimension]

            if period:

                period = period.lower()

                if period not in region:
                    return None

                value = region[period]

            else:

                value = sum(region.values())

        else:

            value = 0

            for region in data.values():
                value += sum(region.values())

        return MetricResponse(
            metric=metric,
            value=value,
            unit=info["unit"],
            description=info["description"],
            dimension=dimension,
            period=period,
        )