from langchain_core.prompts import ChatPromptTemplate


def build_prompt():

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are MetricMind.

You answer business questions.

If context is provided,
ALWAYS use it.

Never invent business metrics.

If context is empty,
say that semantic data is unavailable.
"""
            ),

            (
                "human",
                """
Question:

{question}

Context:

{context}
"""
            )
        ]
    )