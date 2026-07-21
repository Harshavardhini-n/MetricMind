from app.tools.semantic_tool import SemanticTool


class Executor:

    @staticmethod
    def execute(tool: str, question: str):

        if tool == "semantic":

            if "revenue" in question.lower():
                return SemanticTool.query_metric("revenue")

            if "margin" in question.lower():
                return SemanticTool.query_metric("margin")

            if "profit" in question.lower():
                return SemanticTool.query_metric("profit")

        return None