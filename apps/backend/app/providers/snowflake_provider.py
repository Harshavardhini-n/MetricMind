from app.providers.base_provider import BaseProvider


class SnowflakeProvider(BaseProvider):

    def metric_exists(self, metric):
        raise NotImplementedError

    def get_metric(self, metric):
        raise NotImplementedError

    def list_metrics(self):
        raise NotImplementedError