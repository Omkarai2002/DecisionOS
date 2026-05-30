from abc import ABC, abstractmethod

from app.llm.openai_provider import (
    OpenAIProvider
)

from app.schemas.agent_output import (
    AgentOutput
)


class BaseAgent(ABC):

    def __init__(self):

        self.llm = OpenAIProvider()

    @property
    @abstractmethod
    def agent_name(self) -> str:
        pass

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        pass
    def run(
        self,
        user_query: str,
        clarification: str = "",
        peer_context: str = "",
        response_model=AgentOutput
    ):

        full_prompt = f"""
        User scenario:
        {user_query}
        """

        if clarification:

            full_prompt += f"""

            User clarification:
            {clarification}
            """

        if peer_context:

            full_prompt += f"""

            Peer agent opinions:

            {peer_context}

            IMPORTANT:

            You are NOT a passive observer.

            Your responsibility is to:

            1. Identify flawed assumptions
            in other agents.

            2. Explicitly disagree where
            appropriate.

            3. Defend your own reasoning.

            4. Update confidence ONLY if
            another agent makes a stronger
            argument.

            5. Mention WHICH agents you
            disagree with.

            Be intellectually honest but
            critical.

            Avoid generic summaries.

            Think like a specialist
            defending your perspective.
            """

        result = self.llm.invoke(
            system_prompt=self.system_prompt,
            user_prompt=full_prompt,
            response_model=response_model
        )

        return result