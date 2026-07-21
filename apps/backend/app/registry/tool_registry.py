from app.tools.semantic_tool import SemanticTool


class ToolRegistry:

    _TOOLS = {
        "semantic": SemanticTool,
    }

    @classmethod
    def get_tool(cls, tool_name: str):
        return cls._TOOLS.get(tool_name)

    @classmethod
    def available_tools(cls):
        return list(cls._TOOLS.keys())