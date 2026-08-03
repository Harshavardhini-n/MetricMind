from app.agent.metricmind_agent import MetricMindAgent


class AgentService:

    agent = MetricMindAgent()

    @classmethod
    def ask(cls, question: str):

        return cls.agent.run(question)