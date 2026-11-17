import pandas as pd
import json
import numpy as np
from typing import Any

from pydantic import BaseModel
from pathlib import Path

from src.models.model_params import ModelParam
from src.models.ollama_chat_response import OllamaChatResponse


class ParamResponsesFile(BaseModel):
    file_path: str = ""
    options_file_name: str = ""
    responses_file_name: str = ""
    options: ModelParam
    responses: list[OllamaChatResponse]

class ResponseFloatValues(BaseModel):
    file_name: str = ""
    options: ModelParam | None = None
    value_name: str = ""
    values: list[float] = []

class ParamResponsesFilesLoader(BaseModel):
    param_responses: list[ParamResponsesFile] = []

    def get_param_responses_dict(self) -> list[dict[str, ParamResponsesFile]]:
        param_dict : list[dict[str, ParamResponsesFile]] = []

        param_dict = [pr.model_dump() for pr in self.param_responses]
        return param_dict

    def get_response_duration(self, file_name: str) -> ResponseFloatValues:
        durations = self.get_responses_durations()
        resp_iter = iter([d for d in durations if d.file_name == file_name])

        resp = next(resp_iter, None)

        if resp is None:
            return ResponseFloatValues(file_name='not in param_responses')
        
        return resp
     
    def get_responses_durations_dict(self) -> list[dict[str, Any]]:
        return [ dur.model_dump() for dur in self.get_responses_durations()]
     
    def get_responses_durations(self) ->  list[ResponseFloatValues]:

        resp_values: list[ResponseFloatValues] = []

        for param_resp_file in self.param_responses:
            durations = [response.duration for response in param_resp_file.responses]
            duration = [
                duration / 1_000_000 / 60
                for duration in durations
                if duration is not None
            ]
            resp_values.append(
                ResponseFloatValues(
                    file_name=param_resp_file.responses_file_name,
                    options=param_resp_file.options,
                    value_name="duration",
                    values=duration,
                )
            )

        return resp_values

    def _load_options_file(self, options_file_path: Path) -> ModelParam:
        with open(options_file_path, "r") as f:
            return ModelParam(**json.load(f))

    def load_param_response_files(self, folder_path: str, file_names: list[str]):

        folder = Path(folder_path)

        for file in file_names:
            options_file_path = folder / (file + ".json")
            responses_file_path = folder / (file + ".jsonl")

            if options_file_path.exists():
                options: ModelParam = self._load_options_file(
                    options_file_path=options_file_path
                )
            else:
                print("missing=", options_file_path)
                break

            if responses_file_path.exists():
                df = pd.read_json(responses_file_path)
                responses = [OllamaChatResponse(**resp) for resp in df["response"]]

            else:
                print("missing=", options_file_path)
                break

            self.param_responses.append(
                ParamResponsesFile(
                    file_path=folder_path,
                    options_file_name=Path(options_file_path).name,
                    responses_file_name=Path(responses_file_path).name,
                    options=options,
                    responses=responses,
                )
            )
