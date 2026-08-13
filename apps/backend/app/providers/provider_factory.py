from app.core.config import settings
from app.providers.snowflake_provider import SnowflakeProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        provider = settings.DATA_PROVIDER.lower()

        if provider == "snowflake":

            print(">>> USING SNOWFLAKE PROVIDER")

            return SnowflakeProvider()

        raise ValueError(
            f"Unsupported data provider: {provider}"
        )