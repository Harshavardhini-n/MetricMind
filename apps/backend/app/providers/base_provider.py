from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def metric_exists(self, metric: str):
        """Check whether a metric exists."""
        pass

    @abstractmethod
    def get_metric(self, metric: str):
        """Return raw metric metadata."""
        pass

    @abstractmethod
    def list_metrics(self):
        """Return all supported metrics."""
        pass

    @abstractmethod
    def query_metric(self, metric, dimension=None, period=None):
        """Return a single metric."""
        pass

    @abstractmethod
    def compare_metric(self, metric):
        """Return values for all regions."""
        pass

    @abstractmethod
    def rank_metric(self, metric, mode):
        """Return ordered ranking."""
        pass