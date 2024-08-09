from pydantic import UUID4, BaseModel

class LevelCreate(BaseModel):
    nr_level: int
    debit   : int

class LevelBase(BaseModel):
    id: UUID4
    nr_level: int
    debit   : int
    