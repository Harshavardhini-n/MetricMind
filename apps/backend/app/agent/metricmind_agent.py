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
        unit,
    ):

        value = float(value)

        if unit == "USD":

            return f"${value:,.2f}"

        if unit == "%":

            return f"{value:.2f}%"

        return str(value)

    # ==========================================================
    # PERIOD FORMATTER
    # ==========================================================

    @staticmethod
    def _format_period(period):

        if not period:
            return "FULL YEAR"

        return period.upper()

    # ==========================================================
    # RUN
    # ==========================================================

    def run(
        self,
        question: str,
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
                    question,
                )

            # ==================================================
            # COMPARISON
            # ==================================================

            elif comparison:

                result = Executor.compare(
                    tool,
                    question,
                )

            # ==================================================
            # SINGLE METRIC
            # ==================================================

            else:

                result = Executor.execute(
                    tool,
                    question,
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
                        value,
                    ) in enumerate(
                        result["ranking"],
                        start=1,
                    ):

                        formatted = (
                            self._format_value(
                                value,
                                result["unit"],
                            )
                        )

                        lines.append(
                            f"{index}. "
                            f"{region}: "
                            f"{formatted}"
                        )

                    # ----------------------------------------------
                    # REQUESTED WINNER
                    # ----------------------------------------------

                    mode = result.get(
                        "mode",
                        "max",
                    )

                    if mode == "min":

                        selected_region = (
                            result["lowest_region"]
                        )

                        selected_value = (
                            result["lowest_value"]
                        )

                        ranking_type = "LOWEST"

                    else:

                        selected_region = (
                            result["highest_region"]
                        )

                        selected_value = (
                            result["highest_value"]
                        )

                        ranking_type = "HIGHEST"

                    selected_value = (
                        self._format_value(
                            selected_value,
                            result["unit"],
                        )
                    )

                    period = self._format_period(
                        result.get("period")
                    )

                    context = f"""
BUSINESS DATA FROM SNOWFLAKE

Type:
Regional Ranking

Metric:
{result["metric"]}

Period:
{period}

Requested ranking:
{ranking_type}

Selected region:
{selected_region}

Selected value:
{selected_value}

Full ranking:
{chr(10).join(lines)}

Unit:
{result["unit"]}

IMPORTANT:
These values were retrieved directly from Snowflake.

Use these exact values as the source of truth.

The requested ranking is:
{ranking_type}

The selected region is:
{selected_region}

The selected value is:
{selected_value}

Do not invent numerical values.

Do not replace period-specific values with full-year values.

Do not claim that regional data is unavailable.
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
                                result["unit"],
                            )
                        )

                        lines.append(
                            f"{region}: "
                            f"{formatted}"
                        )

                    period = self._format_period(
                        result.get("period")
                    )

                    context = f"""
BUSINESS DATA FROM SNOWFLAKE

Type:
Regional Comparison

Metric:
{result["metric"]}

Period:
{period}

Regional values:
{chr(10).join(lines)}

Unit:
{result["unit"]}

IMPORTANT:
The regional values above were retrieved directly
from Snowflake.

Use these exact regional values to answer the user.

The requested period is:
{period}

Do NOT say that regional data is unavailable.

Do NOT say that additional regional data is required.

Do NOT replace these values with a full-year total.

Do NOT invent values.

Do NOT use values from another period.
"""

                # ==================================================
                # SINGLE METRIC CONTEXT
                # ==================================================

                else:

                    formatted = (
                        self._format_value(
                            result["value"],
                            result["unit"],
                        )
                    )

                    dimension = (
                        result.get("dimension")
                        or "All Regions"
                    )

                    period = self._format_period(
                        result.get("period")
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
{period}

Value:
{formatted}

Unit:
{result["unit"]}

IMPORTANT:
Use this value as the source of truth.

Do not invent another value.

Do not replace a period-specific value with a full-year value.

Do not claim that the requested metric is unavailable
when a value is present.
"""

        # ======================================================
        # NO RESULT
        # ======================================================

        if not context:

            context = """
No business data was retrieved from Snowflake.

Do not invent a numerical answer.

Clearly state that the requested metric could not
be retrieved from the available business data.
"""

        # ======================================================
        # DEBUG
        # ======================================================

        print(
            "\n========== CONTEXT SENT TO LLM =========="
        )

        print(context)

        print(
            "==========================================\n"
        )

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

        print(
            "========================================\n"
        )

        return response.content