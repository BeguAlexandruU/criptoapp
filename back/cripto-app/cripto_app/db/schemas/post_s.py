from pydantic import BaseModel, Field
from typing import Union

class PostCreate(BaseModel):
    title: str=Field(default="Title")
    description: str=Field(...,example="Title")
    post_type: int
    status: int

class PostBase(BaseModel):
    id: int
    title: str
    description: str
    post_type: int
    status: int
    