from typing import List, Literal

from pydantic import (
    BaseModel,
    Field
)


class RebuttalOutput(
    BaseModel
):

    agent_name: Literal[
        "finance",
        "health",
        "career",
        "social",
        "time"
    ]

    rebuttal_points: List[str]

    updated_confidence: float = Field(
            ge=0.0,
            le=1.0
        )

    disagreement_with: List[str]