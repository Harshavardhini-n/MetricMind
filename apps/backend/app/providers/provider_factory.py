from app.core.config import settings

from app.providers.catalog_provider import CatalogProvider
from app.providers.snowflake_provider import SnowflakeProvider


class ProviderFactory:

    @classmethod
    def get_provider(cls):

        print("DATA_PROVIDER =", settings.DATA_PROVIDER)

        if settings.DATA_PROVIDER.lower() == "snowflake":
            print(">>> USING SNOWFLAKE PROVIDER")
            return SnowflakeProvider()

        print(">>> USING CATALOG PROVIDER")
        return CatalogProvider()