from app.catalog.metrics import METRICS
from app.models.semantic import MetricResponse, ComparisonResponse
from app.providers.base_provider import BaseProvider


class CatalogProvider(BaseProvider):

    def metric_exists(self, metric):
        return metric.lower() in METRICS

    def get_metric(self, metric):
        return METRICS.get(metric.lower())

    def list_metrics(self):
        return list(METRICS.keys())

    def query_metric(self, metric, dimension=None, period=None):

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

            if isinstance(region, dict):

                if period:

                    period = period.lower()

                    if period not in region:
                        return None

                    value = region[period]

                else:
                    value = sum(region.values())

            else:
                value = region

        else:

            value = 0

            for region in data.values():

                if isinstance(region, dict):

                    if period:
                        if period in region:
                            value += region[period]
                    else:
                        value += sum(region.values())

                else:
                    value += region

        return MetricResponse(
            metric=metric,
            value=value,
            unit=info["unit"],
            description=info["description"],
            dimension=dimension,
            period=period,
        )

    def compare_metric(self, metric):

        metric = metric.lower()

        if metric not in METRICS:
            return None

        info = METRICS[metric]

        values = {}

        for region, data in info["dimensions"].items():

            if isinstance(data, dict):
                values[region] = sum(data.values())
            else:
                values[region] = data

        return ComparisonResponse(
            metric=metric,
            unit=info["unit"],
            values=values,
        )

    def rank_metric(self, metric, mode):

        metric = metric.lower()

        if metric not in METRICS:
            return None

        info = METRICS[metric]

        values = {}

        for region, data in info["dimensions"].items():

            if isinstance(data, dict):
                values[region] = sum(data.values())
            else:
                values[region] = data

        descending = sorted(
            values.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        ascending = sorted(
            values.items(),
            key=lambda x: x[1],
        )

        ranking = descending if mode == "max" else ascending

        return {
            "metric": metric,
            "unit": info["unit"],
            "ranking": ranking,
            "highest_region": descending[0][0],
            "highest_value": descending[0][1],
            "lowest_region": ascending[0][0],
            "lowest_value": ascending[0][1],
        }