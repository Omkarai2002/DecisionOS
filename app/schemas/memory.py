from pydantic import (
    BaseModel,
    Field
)

from typing import Literal

class MemoryCreate(BaseModel):

    memory_type: Literal["preference","episodic","behaviour"]

    category: Literal["career","finance","health","social","time"]

    content: str

    importance_score: float = Field(
        ge=0.0,
        le=1.0,
        default=0.5
    )