from typing import (
    Literal,
    Optional
)

from pydantic import (
    BaseModel,
    Field
)


class MemoryExtraction(
    BaseModel
):

    should_store: bool

    memory_type: Optional[
        Literal[
            "preference",
            "episodic",
            "behavior"
        ]
    ] = None

    category: Optional[
        Literal[
            "career",
            "finance",
            "health",
            "social",
            "time"
        ]
    ] = None

    content: Optional[str] = None

    importance_score: Optional[
        float
    ] = Field(
        default=0.5,
        ge=0.0,
        le=1.0
    )