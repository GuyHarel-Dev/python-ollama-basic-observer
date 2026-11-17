from src.ollama_services import OllamaService
from ollama import Message

svc = OllamaService("gemma3:1b")

msg = Message(role="user", content="hello are you there?")
resp = svc.send_chat(message=msg, options=None)

print("resp=", resp)

"""

"""