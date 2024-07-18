from pydantic import BaseModel, Field
from typing import Union

class ReferalCreate(BaseModel):
    id_parent: str
    id_child : str
    id_level : int

class ReferalBase(BaseModel):
    id: int
    id_parent: str
    id_child : str
    id_level : int
    