
from pydantic import BaseModel
from typing import Any

from ollama import ChatResponse

class OllamaChatResponse (BaseModel):
    
    model: str | None = None
    created_at: str  | None = None

    duration: int  | None = None
    prompt_tokens: int | None = None
    prompt_tokens_eval_time: int | None = None
    inference_tokens: int | None = None
    inference_tokens_eval_time: int | None = None
    
    role: str | None = None
    content: str | None = None

    generated_token_log_probabilities: Any # sequence of token text, float probalilities

    @classmethod
    def from_chat_response(cls, response: ChatResponse):
        return cls(
            model = response.model,
            created_at = response.created_at,
            duration=response.total_duration,
            prompt_tokens=response.prompt_eval_count,
            prompt_tokens_eval_time=response.prompt_eval_duration,
            inference_tokens=response.eval_count,
            inference_tokens_eval_time=response.eval_duration,
            role = response.message.role,
            content = response.message.content,
            generated_token_log_probabilities = 0
        )
