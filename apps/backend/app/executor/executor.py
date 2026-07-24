from app.registry.tool_registry import ToolRegistry


class Executor:

    METRICS = {
        "revenue": "revenue",
        "margin": "margin",
        "profit": "profit",
        "cost": "cost",
    }

    DIMENSIONS = [
        "north america",
        "europe",
        "asia",
    ]

    PERIODS = [
        "q1",
        "q2",
        "q3",
        "q4",
    ]

    @classmethod
    def execute(cls, tool, question):

        tool_class = ToolRegistry.get_tool(tool)

        if not tool_class:
            return None

        question = question.lower()

        dimension = None
        period = None

        for d in cls.DIMENSIONS:
            if d in question:
                dimension = d
                break

        for p in cls.PERIODS:
            if p in question:
                period = p
                break

        for metric in cls.METRICS:
            if metric in question:
                return tool_class.query_metric(
                    metric,
                    dimension,
                    period,
                )

        return None

    @classmethod
    def compare(cls, tool, question):

        tool_class = ToolRegistry.get_tool(tool)

        if not tool_class:
            return None

        question = question.lower()

        for metric in cls.METRICS:
            if metric in question:
                return tool_class.compare_metric(metric)

        return None