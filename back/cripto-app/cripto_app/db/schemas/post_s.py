from pydantic import BaseModel, Field
from typing import Union

class PostCreate(BaseModel):
    title: str=Field(default="Title")
    description: str=Field(...,example="Title")
    type: str
    status: int

class PostBase(BaseModel):
    id: int
    title: str
    description: str
    type: str
    status: int
    