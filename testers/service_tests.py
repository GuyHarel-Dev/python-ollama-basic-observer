
import json

from ollama import Message, ChatResponse

from src.ollama_services import OllamaService

def service_test():

    msg = Message(role="user", content="hello there")
    svc = OllamaService("gemma3:1b")
    resp = svc.chat([msg])
    
    print(resp)
    
if __name__ == "__main__":
    service_test()
    
