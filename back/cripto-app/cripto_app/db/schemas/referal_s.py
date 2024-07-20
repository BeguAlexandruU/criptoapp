from pydantic import BaseModel, Field, UUID4
from typing import Union

class ReferalCreate(BaseModel):
    id_parent: UUID4
    id_child : UUID4

class ReferalBase(BaseModel):
    id: int
    id_parent: UUID4
    id_child : UUID4
    