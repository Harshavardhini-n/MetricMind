from app.core.config import settings

from app.providers.catalog_provider import CatalogProvider
from app.providers.snowflake_provider import SnowflakeProvider


class ProviderFactory:

    @classmethod
    def get_provider(cls):

        if settings.DATA_PROVIDER.lower() == "snowflake":
            return SnowflakeProvider()

        return CatalogProvider()