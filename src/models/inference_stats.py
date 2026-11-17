from pydantic import BaseModel

from src.models.basic_stats import BasicStats

class InferenceStats(BaseModel):
    duration_stats : BasicStats
    inference_tokens_stats : BasicStats
    inference_tokens_eval_time : BasicStats

