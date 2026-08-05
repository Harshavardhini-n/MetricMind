from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def metric_exists(self, metric):
        pass

    @abstractmethod
    def get_metric(self, metric):
        pass

    @abstractmethod
    def list_metrics(self):
        pass