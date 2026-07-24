from app.catalog.metrics import METRICS
from app.models.semantic import (
    MetricResponse,
    ComparisonResponse,
)

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
    @classmethod
    def compare_metric(cls, metric):

        metric = metric.lower()

        if metric not in METRICS:
            return None

        info = METRICS[metric]

        values = {}

        for region, data in info["dimensions"].items():

            # Quarterly structure
            if isinstance(data, dict):
                values[region] = sum(data.values())

            # Single yearly value
            else:
                values[region] = data

        return ComparisonResponse(
            metric=metric,
            unit=info["unit"],
            values=values,
        )