class Planner:
    
    @staticmethod
    def choose_tool(question: str):

        question = question.lower()

        if "revenue" in question:
            return "semantic"

        if "margin" in question:
            return "semantic"

        if "profit" in question:
            return "semantic"

        return "chat"