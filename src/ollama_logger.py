import json
import re
from typing import Any

from pathlib import Path
from datetime import datetime

from ollama import Message

from src.ollama_services import OllamaService
from src.models.ollama_chat_prompt import OllamaChatPrompt

from src.models.ollama_chat_response import OllamaChatResponse

from src.models.model_params import ModelParam

class OllamaLogger:
    "Send N prompt and store responses in a file"

    def __init__(self, file_path_str: str):
        self.file_path = Path(file_path_str)

    def log_chats(
        self,
        model_name: str,
        prompt_text: str,
        number_samples: int, 
        model_param: ModelParam,
        filename: str | None,
        fileprefix: str | None
    ):
        service = OllamaService(model_name)
        prompt = OllamaChatPrompt(role="user", content=prompt_text)

        samples : list[Any] = []
        options = model_param.model_dump() if model_param else None

        print("inference_param=", options)
        for _ in range(number_samples):

            service_resp = service.send_chat(
                message= Message(role=prompt.role, content=prompt.content),
                options=options)

            response = OllamaChatResponse.from_chat_response(response=service_resp)
            samples.append({
                "prompt":prompt.model_dump(), 
                "options": options,
                "response":response.model_dump()
            })

        # save the samples
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        if filename is None:
            filename = f"{model_name}-{timestamp}-x{number_samples}"
            filename = re.sub(r'[<>:"/\\|?*]', "_", filename)
        
        if fileprefix is not None:
            filename = fileprefix + filename

        file_data_path = f"{self.file_path}/{filename}.jsonl"
        options_path =  f"{self.file_path}/{filename}.json"
        
        print(file_data_path)
        with open(file_data_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(samples, ensure_ascii=False))
            f.write("\n")

        with open(options_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(options, ensure_ascii=False))
            f.write("\n")