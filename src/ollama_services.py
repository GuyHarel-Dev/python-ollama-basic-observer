from ollama import Client, Message, ChatResponse
from typing import Any


class OllamaService:
    "Send prompt and receive response"

    def __init__(self, model_name: str):
        self.client = Client()
        self.model_name = model_name

    def send_chat(
        self, message: Message, options: dict[str, Any] | None
    ) -> ChatResponse:

        response = self.client.chat( # pyright: ignore[reportUnknownMemberType]  
            model=self.model_name, messages=[message], options=options
        )
        return response


"""


"""
