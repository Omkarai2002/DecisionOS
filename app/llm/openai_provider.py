from openai import OpenAI
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential
)

from app.core.config import settings


class OpenAIProvider:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        self.model = settings.OPENAI_MODEL

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(
            multiplier=1,
            min=2,
            max=10
        )
    )
    def invoke(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model
    ):

        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            response_format=response_model
        )

        return response.choices[
            0
        ].message.parsed