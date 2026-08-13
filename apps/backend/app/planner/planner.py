class Planner:
    
    TOOL_KEYWORDS = {
        "semantic": [
            "revenue",
            "margin",
            "profit",
            "cost",
        ]
    }

    COMPARISON_KEYWORDS = [
        "compare",
        "comparison",
        "across regions",
        "by region",
        "per region",
        "each region",
        "every region",
        "regions",
        "versus",
        "vs",
        "between",
    ]
    

    @classmethod
    def choose_tool(cls, question: str):

        question = question.lower()

        for tool, keywords in cls.TOOL_KEYWORDS.items():

            for keyword in keywords:

                if keyword in question:
                    return tool

        return None

    @classmethod
    def is_comparison(cls, question: str):

        question = question.lower()

        return any(keyword in question for keyword in cls.COMPARISON_KEYWORDS)

    @classmethod
    def is_ranking(cls, question: str):

        keywords = [
            "highest",
            "lowest",
            "maximum",
            "minimum",
            "best",
            "worst",
            "top",
            "bottom",
            "max",
            "min",
            "largest",
            "smallest",
        ]

        question = question.lower()

        return any(k in question for k in keywords)

    @classmethod
    def ranking_type(cls, question: str):

        question = question.lower()

        if any(word in question for word in ["highest", "maximum", "best", "top"]):
            return "max"

        if any(word in question for word in ["lowest", "minimum", "worst", "bottom"]):
            return "min"

        return None