from pydantic import BaseModel, Field
from typing import Union

class ProductCreate(BaseModel):
    title       : str=Field(...,example="Product title")
    description : str=Field(...,example="Some description")
    status      : int
    duration    : int

class ProductBase(BaseModel):
    id: int
    title       : str
    description : str
    status      : int
    duration    : int
    