from pydantic import BaseModel, Field
from typing import Union

class ProductCreate(BaseModel):
    title       : str=Field(...,example="Product title")
    description : str=Field(...,example="Some description")
    price       : float=Field(default=0)
    status      : int=Field(default=0)
    duration    : int

class ProductBase(BaseModel):
    id: int
    title       : str
    description : str
    price       : float
    status      : int
    duration    : int
    