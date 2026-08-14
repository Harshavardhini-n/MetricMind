from app.core.config import settings
from app.providers.snowflake_provider import SnowflakeProvider


class ProviderFactory:

    _provider = None

    @classmethod
    def get_provider(cls):

        provider = settings.DATA_PROVIDER.lower()

        if provider == "snowflake":

            if cls._provider is None:
                print(">>> INITIALIZING SNOWFLAKE PROVIDER")

                cls._provider = SnowflakeProvider()

            else:
                print(">>> REUSING SNOWFLAKE PROVIDER")

            return cls._provider

        raise ValueError(
            f"Unsupported data provider: {provider}"
        )