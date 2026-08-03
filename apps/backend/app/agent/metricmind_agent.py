from app.agent.chain import create_chain
from app.planner.planner import Planner
from app.executor.executor import Executor


class MetricMindAgent:

    def __init__(self):
        self.chain = create_chain()

    def run(self, question: str):

        tool = Planner.choose_tool(question)
        comparison = Planner.is_comparison(question)
        ranking = Planner.is_ranking(question)

        context = ""

        if tool:

            if ranking:
                result = Executor.rank(tool, question)

            elif comparison:
                result = Executor.compare(tool, question)

            else:
                result = Executor.execute(tool, question)

            if result:

                # ====================================
                # BUSINESS RANKING
                # ====================================

                if ranking:
    
                    lines = []

                    for i, (region, value) in enumerate(result["ranking"], start=1):

                        if result["unit"] == "USD":
                            formatted = f"${value:,.2f}"
                        elif result["unit"] == "%":
                            formatted = f"{value}%"
                        else:
                            formatted = str(value)

                        lines.append(f"{i}. {region} — {formatted}")

                    if result["unit"] == "USD":
                        highest = f"${result['highest_value']:,.2f}"
                        lowest = f"${result['lowest_value']:,.2f}"
                    elif result["unit"] == "%":
                        highest = f"{result['highest_value']}%"
                        lowest = f"{result['lowest_value']}%"
                    else:
                        highest = str(result["highest_value"])
                        lowest = str(result["lowest_value"])

                    context = f"""
Business Ranking

Metric:
{result["metric"]}

Ranking:
{chr(10).join(lines)}

Highest Region:
{result["highest_region"]}

Highest Value:
{highest}

Lowest Region:
{result["lowest_region"]}

Lowest Value:
{lowest}
"""

                # ====================================
                # BUSINESS COMPARISON
                # ====================================

                elif comparison:

                    lines = []

                    for region, value in result.values.items():

                        if result.unit == "USD":
                            formatted = f"${value:,.2f}"
                        elif result.unit == "%":
                            formatted = f"{value}%"
                        else:
                            formatted = str(value)

                        lines.append(f"{region}: {formatted}")

                    context = f"""
Business Comparison

Metric:
{result.metric}

Values:

{chr(10).join(lines)}
"""

                # ====================================
                # SINGLE METRIC
                # ====================================

                else:

                    if result.unit == "USD":
                        formatted = f"${result.value:,.2f}"
                    elif result.unit == "%":
                        formatted = f"{result.value}%"
                    else:
                        formatted = str(result.value)

                    context = f"""
Business Metric

Metric:
{result.metric}

Description:
{result.description}

Dimension:
{result.dimension or "All Regions"}

Period:
{result.period or "Full Year"}

Value:
{formatted}

Unit:
{result.unit}
"""

        print("\n========== CONTEXT SENT TO LLM ==========")
        print(context)
        print("=========================================\n")

        response = self.chain.invoke(
            {
                "question": question,
                "context": context,
            }
        )

        return response.content