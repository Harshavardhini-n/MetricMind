from app.catalog.dimensions import DIMENSIONS
from app.providers.provider_factory import ProviderFactory


class SemanticCatalog:

    provider = ProviderFactory.get_provider()

    @classmethod
    def metric_exists(cls, metric):
        return cls.provider.metric_exists(metric)

    @classmethod
    def get_metric(cls, metric):
        return cls.provider.get_metric(metric)

    @classmethod
    def list_metrics(cls):
        return cls.provider.list_metrics()

    @classmethod
    def get_dimensions(cls):
        return DIMENSIONS