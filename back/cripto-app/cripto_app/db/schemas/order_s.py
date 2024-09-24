from pydantic import UUID4, BaseModel

class OrderCreate(BaseModel):
    id_user   : UUID4
    id_product: UUID4
    amount    : str 
    currency  : str 
    payment_amount: str 
    payer_currency: str

class OrderBase(BaseModel):
    id     : UUID4
    id_user   : UUID4
    id_product: UUID4
    status    : str 
    type      : str 
    amount    : str 
    currency  : str 
    payment_amount: str 
    payer_currency: str
    