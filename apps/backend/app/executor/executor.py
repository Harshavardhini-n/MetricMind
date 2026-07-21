from app.registry.tool_registry import ToolRegistry


class Executor:
    
    METRICS = {
        "revenue": "revenue",
        "margin": "margin",
        "profit": "profit",
        "cost": "cost",
    }

    @classmethod
    def execute(cls, tool_name: str, question: str):

        tool = ToolRegistry.get_tool(tool_name)

        if tool is None:
            return None

        question = question.lower()

        for keyword, metric in cls.METRICS.items():

            if keyword in question:
                return tool.query_metric(metric)

        return None