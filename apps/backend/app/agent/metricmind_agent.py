from app.agent.chain import create_chain
from app.planner.planner import Planner
from app.executor.executor import Executor


class MetricMindAgent:

    def __init__(self):
        self.chain = create_chain()

    def run(self, question: str):

        tool = Planner.choose_tool(question)

        context = ""

        if tool:

            result = Executor.execute(tool, question)

            if result:

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