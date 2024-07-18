from pydantic import BaseModel

class DemoOrderCreate(BaseModel):
    id_user   : str
    price     : int 
    order_type: int

class DemoOrderBase(BaseModel):
    id     : int
    id_user   : str
    price     : int 
    order_type: int
    