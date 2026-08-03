from app.catalog.catalog import SemanticCatalog
from app.providers.base_provider import BaseProvider


class CatalogProvider(BaseProvider):

    def get_metric(self, metric: str):

        return SemanticCatalog.get_metric(metric)