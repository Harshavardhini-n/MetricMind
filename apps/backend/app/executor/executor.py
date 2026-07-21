from app.tools.semantic_tool import SemanticTool


class Executor:

    METRICS = {
        "revenue": "revenue",
        "margin": "margin",
        "profit": "profit",
        "cost": "cost",
    }

    @classmethod
    def execute(cls, tool: str, question: str):

        if tool != "semantic":
            return None

        question = question.lower()

        for keyword, metric in cls.METRICS.items():
            if keyword in question:
                return SemanticTool.query_metric(metric)

        return None