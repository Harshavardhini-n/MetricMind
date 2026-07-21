from langchain_core.prompts import ChatPromptTemplate

from app.agent.system_prompt import SYSTEM_PROMPT


def build_prompt():

    return ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", "{question}")
        ]
    )