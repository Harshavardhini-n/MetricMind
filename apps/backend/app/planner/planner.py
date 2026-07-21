class Planner:
    
    TOOL_KEYWORDS = {
        "semantic": [
            "revenue",
            "margin",
            "profit",
            "cost",
        ]
    }

    @classmethod
    def choose_tool(cls, question: str):

        question = question.lower()

        for tool, keywords in cls.TOOL_KEYWORDS.items():

            for keyword in keywords:

                if keyword in question:
                    return tool

        return None