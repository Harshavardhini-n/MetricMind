from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def get_metric(self, metric: str):
        pass