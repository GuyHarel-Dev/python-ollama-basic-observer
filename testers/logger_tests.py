
from src.ollama_logger import OllamaLogger
from src.models.model_params import ModelParam

from prompts.IDENTIFY_INFO import IDENTIFY_PDF_TEXT
from documents.FICTIVE_LAMP_RECEIT_PDF_TEXT import FICTIVE_LAMP_RECEIT_PDF_TEXT

data_path = "C:/GH-ORDI/DATA/Data-Model-Observability"

def test_3_samples():
    #prompt = str.format(IDENTIFY_PDF_TEXT, FICTIVE_LAMP_RECEIT_PDF_TEXT)

    prompt = IDENTIFY_PDF_TEXT.format(text=FICTIVE_LAMP_RECEIT_PDF_TEXT)
    param = ModelParam(temperature=0.0, top_k=0, top_p=0, seed= 0)
    sampler = OllamaLogger(data_path) 
    sampler.log_chats("gemma3:1b", prompt, 3, param, filename=None, fileprefix=None)

    pass

def log_two_params():
    """
    temperature=0.8, top_k=40, top_p=0.9, seed=None serai ollama default
    temperature=0.4, top_k=20, top_p=0.45, seed=None

    """
    prompt = IDENTIFY_PDF_TEXT.format(text=FICTIVE_LAMP_RECEIT_PDF_TEXT)

    no_samples = 100
    sampler = OllamaLogger(data_path) 

    # sample2 with param 0
    params = ModelParam(temperature=0.8, top_k=40, top_p=0.9, seed=None)
    sampler.log_chats("gemma3:1b", prompt, no_samples, params, filename=None, fileprefix=None)

    # samples with param 1
    params = ModelParam(temperature=0.4, top_k=20, top_p=0.45, seed=None)
    sampler.log_chats("gemma3:1b", prompt, no_samples, params, filename=None, fileprefix=None)

    pass

def log_two_params_2():
    "prend 30 minutes"
    """
    temperature=0.2, top_k=10, top_p=0.22, seed=None
    temperature=0.1, top_k=5, top_p=0.11, seed=None
    
    """
    prompt = IDENTIFY_PDF_TEXT.format(text=FICTIVE_LAMP_RECEIT_PDF_TEXT)

    no_samples = 100
    sampler = OllamaLogger(data_path) 

    # sample2 with param 0
    params = ModelParam(temperature=0.2, top_k=10, top_p=0.22, seed=None)
    sampler.log_chats("gemma3:1b", prompt, no_samples, params, filename=None, fileprefix=None)

    # samples with param 1
    params = ModelParam(temperature=0.1, top_k=5, top_p=0.11, seed=None)
    sampler.log_chats("gemma3:1b", prompt, no_samples, params, filename=None, fileprefix=None)

    pass


if __name__ == "__main__":
    #log_two_params()  # total 8 mins
    #test_3_samples()
    #test_read()
    log_two_params_2()
    pass
