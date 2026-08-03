from app.providers.catalog_provider import CatalogProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        return CatalogProvider()