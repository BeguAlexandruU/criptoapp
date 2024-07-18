from pydantic import BaseModel

class CardCreate(BaseModel):
    id_user: str
    sold   : int 
    nr_red : int

class CardBase(BaseModel):
    id     : int
    id_user: str
    sold   : int 
    nr_red : int
    