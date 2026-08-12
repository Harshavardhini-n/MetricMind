from app.agent.chain import create_chain
from app.planner.planner import Planner
from app.executor.executor import Executor


class MetricMindAgent:

    def __init__(self):

        self.chain = create_chain()

    # ==========================================================
    # VALUE FORMATTER
    # ==========================================================

    @staticmethod
    def _format_value(
        value,
        unit
    ):

        value = float(value)

        if unit == "USD":

            return f"${value:,.2f}"

        if unit == "%":

            return f"{value:.2f}%"

        return str(value)

    # ==========================================================
    # RUN
    # ==========================================================

    def run(
        self,
        question: str
    ):

        print("\n========================================")
        print("METRICMIND AGENT")
        print("Question:", question)

        # ======================================================
        # PLANNING
        # ======================================================

        tool = Planner.choose_tool(
            question
        )

        comparison = Planner.is_comparison(
            question
        )

        ranking = Planner.is_ranking(
            question
        )

        print("Tool:", tool)
        print("Comparison:", comparison)
        print("Ranking:", ranking)

        context = ""

        # ======================================================
        # EXECUTION
        # ======================================================

        if tool:

            # ==================================================
            # RANKING
            # ==================================================

            if ranking:

                result = Executor.rank(
                    tool,
                    question
                )

            # ==================================================
            # COMPARISON
            # ==================================================

            elif comparison:

                result = Executor.compare(
                    tool,
                    question
                )

            # ==================================================
            # SINGLE METRIC
            # ==================================================

            else:

                result = Executor.execute(
                    tool,
                    question
                )

            print("Backend result:", result)

            # ==================================================
            # RESULT EXISTS
            # ==================================================

            if result:

                # ==================================================
                # RANKING CONTEXT
                # ==================================================

                if ranking:

                    lines = []

                    for index, (
                        region,
                        value
                    ) in enumerate(
                        result["ranking"],
                        start=1
                    ):

                        formatted = (
                            self._format_value(
                                value,
                                result["unit"]
                            )
                        )

                        lines.append(
                            f"{index}. "
                            f"{region}: "
                            f"{formatted}"
                        )

                    highest = (
                        self._format_value(
                            result["highest_value"],
                            result["unit"]
                        )
                    )

                    lowest = (
                        self._format_value(
                            result["lowest_value"],
                            result["unit"]
                        )
                    )

                    context = f"""
BUSINESS DATA FROM SNOWFLAKE

Type:
Ranking

Metric:
{result["metric"]}

Ranking order:
{chr(10).join(lines)}

Highest region:
{result["highest_region"]}

Highest value:
{highest}

Lowest region:
{result["lowest_region"]}

Lowest value:
{lowest}

Unit:
{result["unit"]}

IMPORTANT:
These values were retrieved directly from Snowflake.
Use these values as the source of truth.
Do not claim that regional data is unavailable.
Do not invent other values.
"""

                # ==================================================
                # COMPARISON CONTEXT
                # ==================================================

                elif comparison:

                    lines = []

                    for region, value in (
                        result["values"].items()
                    ):

                        formatted = (
                            self._format_value(
                                value,
                                result["unit"]
                            )
                        )

                        lines.append(
                            f"{region}: "
                            f"{formatted}"
                        )

                    context = f"""
BUSINESS DATA FROM SNOWFLAKE

Type:
Regional Comparison

Metric:
{result["metric"]}

Regional values:
{chr(10).join(lines)}

Unit:
{result["unit"]}

IMPORTANT:
The regional values above were retrieved directly
from Snowflake.

Use these exact regional values to answer the user.

Do NOT say that regional data is unavailable.
Do NOT say that additional regional data is required.
Do NOT replace these values with a total.
Do NOT invent values.
"""

                # ==================================================
                # SINGLE METRIC CONTEXT
                # ==================================================

                else:

                    formatted = (
                        self._format_value(
                            result["value"],
                            result["unit"]
                        )
                    )

                    dimension = (
                        result.get("dimension")
                        or "All Regions"
                    )

                    period = (
                        result.get("period")
                        or "Full Year"
                    )

                    context = f"""
BUSINESS DATA FROM SNOWFLAKE

Type:
Single Metric

Metric:
{result["metric"]}

Description:
{result["description"]}

Dimension:
{dimension}

Period:
{period.upper() if result.get("period") else "FULL YEAR"}

Value:
{formatted}

Unit:
{result["unit"]}

IMPORTANT:
Use this value as the source of truth.
Do not invent another value.
"""

        # ======================================================
        # NO RESULT
        # ======================================================

        if not context:

            context = """
No business data was retrieved from Snowflake.

Do not invent a numerical answer.
Clearly state that the requested metric could not
be retrieved.
"""

        # ======================================================
        # DEBUG
        # ======================================================

        print("\n========== CONTEXT SENT TO LLM ==========")
        print(context)
        print("==========================================\n")

        # ======================================================
        # LLM
        # ======================================================

        response = self.chain.invoke(
            {
                "question": question,
                "context": context,
            }
        )

        print("LLM RESPONSE:")
        print(response.content)
        print("========================================\n")

        return response.content