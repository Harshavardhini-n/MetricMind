import snowflake.connector
from app.core.config import settings


print(settings.SNOWFLAKE_ACCOUNT)
conn = snowflake.connector.connect(
    account=settings.SNOWFLAKE_ACCOUNT,
    user=settings.SNOWFLAKE_USER,
    password=settings.SNOWFLAKE_PASSWORD,
    warehouse=settings.SNOWFLAKE_WAREHOUSE,
    database=settings.SNOWFLAKE_DATABASE,
    schema=settings.SNOWFLAKE_SCHEMA,
)

cur = conn.cursor()

cur.execute("SELECT CURRENT_VERSION();")
print("Snowflake Version:", cur.fetchone())

cur.execute("SELECT COUNT(*) FROM SALES_ORDERS;")
print("Rows:", cur.fetchone())

cur.close()
conn.close()