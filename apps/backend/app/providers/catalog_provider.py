from app.catalog.metrics import METRICS
from app.providers.base_provider import BaseProvider


class CatalogProvider(BaseProvider):

    def metric_exists(self, metric):
        return metric.lower() in METRICS

    def get_metric(self, metric):
        return METRICS.get(metric.lower())

    def list_metrics(self):
        return list(METRICS.keys())