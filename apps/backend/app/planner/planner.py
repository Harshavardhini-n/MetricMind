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
    @classmethod
    def is_comparison(cls, question):

        question = question.lower()

        comparison_words = [
            "compare",
            "highest",
            "lowest",
            "by region",
        ]

        return any(word in question for word in comparison_words)