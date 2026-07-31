from app.agent.chain import create_chain
from app.planner.planner import Planner
from app.executor.executor import Executor


class MetricMindAgent:

    def __init__(self):
        self.chain = create_chain()

    def run(self, question: str):

        tool = Planner.choose_tool(question)
        comparison = Planner.is_comparison(question)

        context = ""

        if tool:

            if comparison:
                result = Executor.compare(tool, question)
            else:
                result = Executor.execute(tool, question)

            if result:

                # ==========================
                # Comparison Context
                # ==========================
                if comparison:

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

                # ==========================
                # Single Metric Context
                # ==========================
                else:

                    if result.unit == "USD":
                        formatted_value = f"${result.value:,.2f}"
                    elif result.unit == "%":
                        formatted_value = f"{result.value}%"
                    else:
                        formatted_value = str(result.value)

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
{formatted_value}

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