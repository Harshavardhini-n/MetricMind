from app.catalog.metrics import METRICS
from app.providers.base_provider import BaseProvider


class CatalogProvider(BaseProvider):

    def metric_exists(self, metric):

        return metric.lower() in METRICS

    def get_metric(self, metric):

        return METRICS.get(
            metric.lower()
        )

    def list_metrics(self):

        return list(
            METRICS.keys()
        )

    def query_metric(
        self,
        metric,
        dimension=None,
        period=None,
    ):

        metric = metric.lower()

        data = METRICS.get(metric)

        if not data:

            return None

        return data

    def compare_metric(self, metric):

        raise NotImplementedError(
            "Comparison is not supported "
            "by CatalogProvider."
        )

    def rank_metric(
        self,
        metric,
        mode,
    ):

        raise NotImplementedError(
            "Ranking is not supported "
            "by CatalogProvider."
        )