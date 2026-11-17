from src.ollama_logger import OllamaLogger

from src.prompts.IDENTIFY_INFO import IDENTIFY_PDF_TEXT
from src.documents.FICTIVE_LAMP_RECEIT_PDF_TEXT import FICTIVE_LAMP_RECEIT_PDF_TEXT

def test_read():
    logger = OllamaLogger("data/log") 
    logger.retreive_samples("gemma3_1b-2026-08-06_10-46-30-x3.jsonl")
        
def sample_identify_pdf_text(num:int):
    prompt = IDENTIFY_PDF_TEXT.format(text=FICTIVE_LAMP_RECEIT_PDF_TEXT)

    logger = OllamaLogger("data/log") 
    logger.log_chats("gemma3:1b", prompt, num)

def sample_identify_pdf_text(num:int, options: dict, filename: str = None):
    prompt = IDENTIFY_PDF_TEXT.format(text=FICTIVE_LAMP_RECEIT_PDF_TEXT)

    logger = OllamaLogger("data/log") 
    logger.log_chats("gemma3:1b", prompt, num, options, filename)
    
if __name__ == "__main__":
    sample_identify_pdf_text(5, {"temperature": 0.8})
    #test_read()
