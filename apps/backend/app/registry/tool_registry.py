from app.tools.semantic_tool import SemanticTool


class ToolRegistry:

    TOOLS = {
        "semantic": SemanticTool,
    }

    @classmethod
    def get_tool(cls, name):

        return cls.TOOLS.get(
            name
        )