from src.ollama_logger import OllamaLogger

from src.models.model_params import ModelParam

class OllamaObserver():
    "Observe effects of inference param changes"
    pass

    def observe_temperature(self, model:str, data_path:str, prompt:str, no_samples:int, params: list[ModelParam]):
        self.logger = OllamaLogger(data_path) 

        for param in params:
            self.logger.log_chats(model, prompt, no_samples, param, filename=None, fileprefix=None) 



"""

"""
