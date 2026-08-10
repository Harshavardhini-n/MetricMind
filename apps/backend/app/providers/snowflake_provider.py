import snowflake.connector
from app.models.semantic import MetricResponse,ComparisonResponse
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

    def execute(self, query, params=None):
        cursor = self.conn.cursor()

        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        finally:
            cursor.close()

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
    
        print("SnowflakeProvider.query_metric() called")
        print("Metric:", metric)
        print("Dimension:", dimension)
        print("Period:", period)

        metric = metric.lower()

        metric_columns = {
            "revenue": "SALES",
            "profit": "PROFIT",
        }

        if metric not in metric_columns:
            return None

        column = metric_columns[metric]

        sql = f"""
            SELECT SUM({column})
            FROM METRICMIND_DB.RAW.SALES_ORDERS
        """

        params = []

        conditions = []

        if dimension:
            conditions.append("LOWER(REGION) = LOWER(%s)")
            params.append(dimension)

        if period:
            # Only add this once we implement the actual date logic.
            pass

        if conditions:
            sql += " WHERE " + " AND ".join(conditions)

        rows = self.execute(sql, params)

        value = rows[0][0] or 0

        print("SQL Result =", value)

        return MetricResponse(
            metric=metric,
            value=float(value),
            unit="USD",
            description=f"Total {metric}",
            dimension=dimension,
            period=period,
        )
    def compare_metric(self, metric):
    
        metric = metric.lower()

        if metric == "revenue":

            sql = """
            SELECT
                REGION,
                SUM(SALES) AS REVENUE
            FROM SALES_ORDERS
            GROUP BY REGION
            ORDER BY REVENUE DESC
            """

            rows = self.execute(sql)

            values = {
                str(region): float(value or 0)
                for region, value in rows
            }

            return ComparisonResponse(
                metric="revenue",
                unit="USD",
                values=values,
            )

        return None

    def rank_metric(self, metric, mode):
        raise NotImplementedError