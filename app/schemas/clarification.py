from pydantic import BaseModel


class ClarificationQuestion(
    BaseModel
):
    question: str