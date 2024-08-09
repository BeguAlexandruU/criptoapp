from pydantic import UUID4, BaseModel

class CardCreate(BaseModel):
    id_user: UUID4
    sold   : int 
    nr_ref : int

class CardBase(BaseModel):
    id     : UUID4
    id_user: UUID4
    sold   : int 
    nr_ref : int
    