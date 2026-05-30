from typing import (
    Dict,
    List,
    Optional,
    TypedDict
)


class AgentResponse(TypedDict):
    agent_name: str
    vote: str
    confidence: float
    reasoning: List[str]


class AgentState(TypedDict):

    user_query: str

    messages: List[str]

    agent_outputs: List[AgentResponse]

    rebuttals: List[Dict]

    final_decision: Dict

    clarification_question: Optional[str]

    user_clarification: Optional[str]

    negotiation_round: int