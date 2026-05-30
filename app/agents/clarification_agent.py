from app.agents.base_agent import (
    BaseAgent
)


class ClarificationAgent(BaseAgent):

    @property
    def agent_name(self):
        return "career"

    @property
    def system_prompt(self):

        return """
        You generate ONE clarification
        question when agents disagree.

        Goal:

        Resolve ambiguity in decision-making.

        Rules:

        1. Ask exactly ONE question

        2. Question must help resolve
        agent disagreement

        3. Be concise

        4. Focus on priorities,
        tradeoffs, or missing context

        Examples:

        - What matters more:
          salary or work-life balance?

        - Are you comfortable
          with startup risk?

        - Is short-term stability
          more important than
          long-term growth?
          If peer opinions are provided:

            1. Review disagreements

            2. Challenge assumptions

            3. Update confidence if needed

            4. Return thoughtful rebuttal
   
        """