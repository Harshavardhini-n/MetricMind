from app.catalog.catalog import SemanticCatalog
from app.providers.provider_factory import ProviderFactory
from app.models.semantic import (
    MetricResponse,
    ComparisonResponse,
)


class SemanticTool:

    @classmethod
    def query_metric(cls, metric, dimension=None, period=None):

        metric = metric.lower()

        if not SemanticCatalog.metric_exists(metric):
            return None

        provider = ProviderFactory.get_provider()

        info = provider.get_metric(metric)

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

    @classmethod
    def compare_metric(cls, metric):

        metric = metric.lower()

        if not SemanticCatalog.metric_exists(metric):
            return None

        provider = ProviderFactory.get_provider()
        info = provider.get_metric(metric)

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

    @classmethod
    def rank_metric(cls, metric, mode):

        metric = metric.lower()

        if not SemanticCatalog.metric_exists(metric):
            return None

        provider = ProviderFactory.get_provider()
        info = provider.get_metric(metric)

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

        if mode == "max":
            ranking = descending
        else:
            ranking = ascending

        return {
            "metric": metric,
            "unit": info["unit"],
            "ranking": ranking,
            "highest_region": descending[0][0],
            "highest_value": descending[0][1],
            "lowest_region": ascending[0][0],
            "lowest_value": ascending[0][1],
        }