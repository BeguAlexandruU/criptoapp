from pydantic import UUID4, BaseModel

class DemoOrderCreate(BaseModel):
    id_user   : UUID4
    price     : int 
    order_type: int

class DemoOrderBase(BaseModel):
    id     : UUID4
    id_user   : UUID4
    price     : int 
    order_type: int
    