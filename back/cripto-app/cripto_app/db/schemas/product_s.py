from typing import Optional
from pydantic import UUID4, BaseModel, Field

class ProductCreate(BaseModel):
    # id_stripe_product: Optional[str]= ''
    # id_stripe_price: Optional[str]= ''
    title       : str=Field(...,example="Product title")
    description : str=Field(...,example="Some description")
    price       : float=Field(default=0)
    isHidden    : bool=Field(default=True)
    duration    : int

class ProductBase(BaseModel):
    id: UUID4
    # id_stripe_product: str
    # id_stripe_price: str
    title       : str
    description : str
    price       : float
    isHidden    : bool
    duration    : int
    