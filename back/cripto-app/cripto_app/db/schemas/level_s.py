from pydantic import BaseModel

class LevelCreate(BaseModel):
    nr_level: int
    debit   : int

class LevelBase(BaseModel):
    id: int
    nr_level: int
    debit   : int
    