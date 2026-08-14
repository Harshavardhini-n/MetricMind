from app.agent.metricmind_agent import MetricMindAgent


class AgentService:

    agent = MetricMindAgent()

    @classmethod
    def ask(cls, question: str):

        if not question or not question.strip():

            return (
                "Please enter a business question."
            )

        question = question.strip()

        try:

            return cls.agent.run(
                question
            )

        except Exception as exc:

            print("\n========================================")
            print("AGENT SERVICE ERROR")
            print("Question:", question)
            print("Error:", repr(exc))
            print("========================================\n")

            return (
                "I could not process your request "
                "because an internal data or processing "
                "error occurred."
            )