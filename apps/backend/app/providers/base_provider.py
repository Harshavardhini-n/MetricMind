from abc import ABC, abstractmethod


class BaseProvider(ABC):

    # ==========================================================
    # SEMANTIC CATALOG
    # ==========================================================

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

    # ==========================================================
    # SINGLE METRIC
    # ==========================================================

    @abstractmethod
    def query_metric(
        self,
        metric,
        dimension=None,
        period=None,
    ):
        """
        Return a single metric.

        Supports optional:
        - region/dimension
        - quarter/period
        """
        pass

    # ==========================================================
    # REGIONAL COMPARISON
    # ==========================================================

    @abstractmethod
    def compare_metric(
        self,
        metric,
        period=None,
    ):
        """
        Return metric values across all regions.

        If period is provided, restrict the comparison
        to that quarter.
        """
        pass

    # ==========================================================
    # REGIONAL RANKING
    # ==========================================================

    @abstractmethod
    def rank_metric(
        self,
        metric,
        mode,
        period=None,
    ):
        """
        Return ordered regional ranking.

        mode:
        - max -> highest first
        - min -> lowest first

        period:
        - q1
        - q2
        - q3
        - q4
        - None -> full year
        """
        pass