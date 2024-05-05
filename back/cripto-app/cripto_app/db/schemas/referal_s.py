from pydantic import BaseModel, Field
from typing import Union

class ReferalCreate(BaseModel):
    id_parent: int
    id_child : int
    id_level : int

class ReferalBase(BaseModel):
    id: int
    id_parent: int
    id_child : int
    id_level : int
    