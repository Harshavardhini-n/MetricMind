import snowflake.connector
from app.models.semantic import MetricResponse
from app.core.config import settings
from app.providers.base_provider import BaseProvider


class SnowflakeProvider(BaseProvider):

    def __init__(self):
        self.conn = snowflake.connector.connect(
            account=settings.SNOWFLAKE_ACCOUNT,
            user=settings.SNOWFLAKE_USER,
            password=settings.SNOWFLAKE_PASSWORD,
            warehouse=settings.SNOWFLAKE_WAREHOUSE,
            database=settings.SNOWFLAKE_DATABASE,
            schema=settings.SNOWFLAKE_SCHEMA,
        )

    def execute(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def metric_exists(self, metric):
        return metric.lower() in [
            "revenue",
            "profit",
            "margin",
            "cost",
        ]

    def get_metric(self, metric):
        return {"metric": metric}

    def list_metrics(self):
        return [
            "revenue",
            "profit",
            "margin",
            "cost",
        ]

    

    def query_metric(self, metric, dimension=None, period=None):

        metric = metric.lower()

        if metric != "revenue":
            return None

        sql = """
        SELECT SUM(SALES)
        FROM SALES_ORDERS
        """

        value = self.execute(sql)[0][0]

        return MetricResponse(
            metric="revenue",
            value=float(value),
            unit="USD",
            description="Total Revenue",
            dimension=dimension,
            period=period,
        )

    def compare_metric(self, metric):
        raise NotImplementedError

    def rank_metric(self, metric, mode):
        raise NotImplementedError