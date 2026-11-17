from pydantic import BaseModel


class ModelResponseStats (BaseModel): 
    content_len: int
    content_nbr_names: int
    content_nbr_struct: int 
    content_nbr_correct_names: int 
    content_nbr_incorrect_names: int 




