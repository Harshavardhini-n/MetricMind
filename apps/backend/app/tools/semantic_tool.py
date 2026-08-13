from app.providers.provider_factory import ProviderFactory


class SemanticTool:

    @classmethod
    def query_metric(
        cls,
        metric,
        dimension=None,
        period=None,
    ):

        provider = ProviderFactory.get_provider()

        return provider.query_metric(
            metric=metric,
            dimension=dimension,
            period=period,
        )

    @classmethod
    def compare_metric(
        cls,
        metric,
        period=None,
    ):

        provider = ProviderFactory.get_provider()

        return provider.compare_metric(
            metric=metric,
            period=period,
        )

    @classmethod
    def rank_metric(
        cls,
        metric,
        mode,
        period=None,
    ):

        provider = ProviderFactory.get_provider()

        return provider.rank_metric(
            metric=metric,
            mode=mode,
            period=period,
        )