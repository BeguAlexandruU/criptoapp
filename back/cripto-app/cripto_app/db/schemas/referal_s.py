from pydantic import BaseModel, Field, UUID4

class ReferalCreate(BaseModel):
    id_parent: UUID4
    id_child : UUID4

class ReferalBase(BaseModel):
    id: UUID4
    id_parent: UUID4
    id_child : UUID4
    