from app.catalog.metrics import METRICS
from app.catalog.dimensions import DIMENSIONS


class SemanticCatalog:

    @classmethod
    def metric_exists(cls, metric):

        return metric.lower() in METRICS

    @classmethod
    def get_metric(cls, metric):

        return METRICS.get(
            metric.lower()
        )

    @classmethod
    def list_metrics(cls):

        return list(
            METRICS.keys()
        )

    @classmethod
    def get_dimensions(cls):

        return DIMENSIONS