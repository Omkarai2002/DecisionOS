from app.llm.openai_provider import (
    OpenAIProvider
)

from app.schemas.memory_extraction import (
    MemoryExtraction
)


class MemoryExtractor:

    def __init__(self):

        self.llm = (
            OpenAIProvider()
        )

    def extract_memory(
        self,
        user_message: str
    ):

        system_prompt = """
        You are a Memory Extraction Agent.

        Your job:

        Determine whether
        a user message contains
        important long-term memory.

        Store ONLY:

        1. preferences

        Example:
        "learning matters more
        than stability"

        2. episodic experiences

        Example:
        "my last startup
        burned me out"

        3. behavior patterns

        Example:
        "I keep ignoring
        health advice"

        Ignore:

        greetings
        casual conversation
        temporary facts
        noise

        Compress memories into
        short meaningful statements.
        """

        result = self.llm.invoke(
            system_prompt=
                system_prompt,

            user_prompt=
                user_message,

            response_model=
                MemoryExtraction
        )

        return result