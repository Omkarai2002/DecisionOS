from typing import List, Literal

from pydantic import (
    BaseModel,
    Field
)


class AgentOutput(BaseModel):

    agent_name: Literal[
        "finance",
        "health",
        "career",
        "social",
        "time"
    ]

    vote: Literal[
        "accept",
        "reject",
        "neutral"
    ]

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1"
    )

    reasoning: List[str]

    risks: List[str]

    missing_information: List[str]