from pydantic import BaseModel

class OllamaChatPrompt (BaseModel): 
    role: str
    content: str


   