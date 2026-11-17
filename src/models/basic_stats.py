from pydantic import BaseModel

class BasicStats(BaseModel):
    min: float
    max : float
    mean: float
    std: float