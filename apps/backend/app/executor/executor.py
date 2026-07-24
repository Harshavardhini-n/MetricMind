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

    @classmethod
    def execute(cls, tool, question):

        question = question.lower()

        dimension = None

        for d in cls.DIMENSIONS:
            if d in question:
                dimension = d
                break

        tool_class = ToolRegistry.get_tool(tool)

        if not tool_class:
            return None

        for metric in cls.METRICS:
            if metric in question:
                return tool_class.query_metric(
                    metric,
                    dimension
                )

        return None