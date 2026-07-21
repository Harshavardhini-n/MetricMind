from app.agent.chain import create_chain


class OllamaService:

    @staticmethod
    def generate_response(prompt: str) -> str:

        chain = create_chain()

        response = chain.invoke(
            {
                "question": prompt
            }
        )

        return response.content