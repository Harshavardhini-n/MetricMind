import snowflake.connector

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

        print("SnowflakeProvider initialized")

    # ==========================================================
    # GENERIC SQL EXECUTION
    # ==========================================================

    def execute(self, query, params=None):

        cursor = self.conn.cursor()

        try:

            print("\n========== SNOWFLAKE QUERY ==========")
            print(query)
            print("PARAMS:", params)
            print("=====================================\n")

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            return cursor.fetchall()

        finally:

            cursor.close()

    # ==========================================================
    # SEMANTIC CATALOG
    # ==========================================================

    def metric_exists(self, metric):

        return metric.lower() in {
            "revenue",
            "profit",
            "margin",
            "cost",
        }

    def get_metric(self, metric):

        metric = metric.lower()

        if not self.metric_exists(metric):
            return None

        return {
            "metric": metric
        }

    def list_metrics(self):

        return [
            "revenue",
            "profit",
            "margin",
            "cost",
        ]

    # ==========================================================
    # METRIC SQL EXPRESSION
    # ==========================================================

    def _get_metric_expression(self, metric):

        metric = metric.lower()

        metric_map = {

            # Revenue = SALES
            "revenue": "SUM(SALES)",

            # Profit is directly available
            "profit": "SUM(PROFIT)",

            # Profit margin = Profit / Sales
            "margin": """
                CASE
                    WHEN SUM(SALES) = 0 THEN 0
                    ELSE (SUM(PROFIT) / SUM(SALES)) * 100
                END
            """,

            # Cost = Sales - Profit
            "cost": "SUM(SALES) - SUM(PROFIT)",
        }

        return metric_map.get(metric)

    # ==========================================================
    # METRIC UNIT
    # ==========================================================

    def _get_metric_unit(self, metric):

        if metric.lower() == "margin":
            return "%"

        return "USD"

    # ==========================================================
    # SINGLE METRIC
    # ==========================================================

    def query_metric(
        self,
        metric,
        dimension=None,
        period=None
    ):

        metric = metric.lower()

        print("\n========================================")
        print("SnowflakeProvider.query_metric()")
        print("Metric:", metric)
        print("Dimension:", dimension)
        print("Period:", period)
        print("========================================")

        expression = self._get_metric_expression(metric)

        if not expression:

            print("Unknown metric:", metric)

            return None

        sql = f"""
            SELECT
                COALESCE(
                    {expression},
                    0
                )
            FROM SALES_ORDERS
        """

        params = []

        conditions = []

        # ------------------------------------------------------
        # REGION
        # ------------------------------------------------------

        if dimension:

            conditions.append(
                "LOWER(REGION) = LOWER(%s)"
            )

            params.append(dimension)

        # ------------------------------------------------------
        # QUARTER
        # ------------------------------------------------------

        if period:

            quarter_map = {
                "q1": 1,
                "q2": 2,
                "q3": 3,
                "q4": 4,
            }

            quarter = quarter_map.get(
                period.lower()
            )

            if quarter:

                conditions.append(
                    "QUARTER(TO_DATE(ORDER_DATE)) = %s"
                )

                params.append(quarter)

        # ------------------------------------------------------
        # WHERE
        # ------------------------------------------------------

        if conditions:

            sql += (
                " WHERE "
                + " AND ".join(conditions)
            )

        # ------------------------------------------------------
        # EXECUTE
        # ------------------------------------------------------

        rows = self.execute(
            sql,
            params
        )

        if not rows:

            value = 0.0

        else:

            value = rows[0][0]

            if value is None:
                value = 0.0

        value = float(value)

        unit = self._get_metric_unit(metric)

        print("SQL Result =", value)

        return {
            "metric": metric,
            "value": value,
            "unit": unit,
            "description": self._get_description(metric),
            "dimension": dimension,
            "period": period,
        }

    # ==========================================================
    # DESCRIPTION
    # ==========================================================

    def _get_description(self, metric):

        descriptions = {

            "revenue":
                "Total business revenue",

            "profit":
                "Total business profit",

            "margin":
                "Profit margin",

            "cost":
                "Total business cost",
        }

        return descriptions.get(
            metric,
            f"Total {metric.title()}"
        )

    # ==========================================================
    # COMPARE ACROSS REGIONS
    # ==========================================================

    def compare_metric(self, metric):

        metric = metric.lower()

        expression = self._get_metric_expression(metric)

        if not expression:
            return None

        sql = f"""
            SELECT
                REGION,
                COALESCE(
                    {expression},
                    0
                ) AS VALUE
            FROM SALES_ORDERS
            GROUP BY REGION
            ORDER BY REGION
        """

        rows = self.execute(sql)

        values = {}

        for region, value in rows:

            if value is None:
                value = 0.0

            values[str(region)] = float(value)

        if not values:
            return None

        return {
            "metric": metric,
            "unit": self._get_metric_unit(metric),
            "values": values,
        }

    # ==========================================================
    # RANK ACROSS REGIONS
    # ==========================================================

    def rank_metric(self, metric, mode):

        metric = metric.lower()

        expression = self._get_metric_expression(metric)

        if not expression:
            return None

        direction = "DESC"

        if mode == "min":
            direction = "ASC"

        sql = f"""
            SELECT
                REGION,
                COALESCE(
                    {expression},
                    0
                ) AS VALUE
            FROM SALES_ORDERS
            GROUP BY REGION
            ORDER BY VALUE {direction}
        """

        rows = self.execute(sql)

        ranking = []

        for region, value in rows:

            if value is None:
                value = 0.0

            ranking.append(
                (
                    str(region),
                    float(value)
                )
            )

        if not ranking:
            return None

        return {
            "metric": metric,
            "unit": self._get_metric_unit(metric),
            "ranking": ranking,

            "highest_region": ranking[0][0],
            "highest_value": ranking[0][1],

            "lowest_region": ranking[-1][0],
            "lowest_value": ranking[-1][1],
        }