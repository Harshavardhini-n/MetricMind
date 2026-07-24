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

                if comparison:

                    lines = []

                    for region, value in result.values.items():
                        lines.append(f"{region}: {value} {result.unit}")

                    context = f"""
Business Comparison

Metric:
{result.metric}

Values:
{chr(10).join(lines)}
"""

                else:

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
{result.value}

Unit:
{result.unit}
"""

        response = self.chain.invoke(
            {
                "question": question,
                "context": context,
            }
        )

        return response.content