from pydantic import BaseModel

class ModelParam(BaseModel):
    temperature: float | None = None
    top_k: int | None = None
    top_p: float  | None = None
    seed: int  | None = None

    def __str__(self) -> str:

        return f"t:{self.temperature}, k:{self.top_k}, p:{self.top_p}, s:{self.seed}"

