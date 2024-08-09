from pydantic import UUID4, BaseModel, Field

class ProductCreate(BaseModel):
    title       : str=Field(...,example="Product title")
    description : str=Field(...,example="Some description")
    price       : float=Field(default=0)
    status      : int=Field(default=0)
    duration    : int

class ProductBase(BaseModel):
    id: UUID4
    title       : str
    description : str
    price       : float
    status      : int
    duration    : int
    