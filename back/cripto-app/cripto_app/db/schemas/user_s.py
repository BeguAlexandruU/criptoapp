from pydantic import BaseModel
from typing import Union

class UserCreate(BaseModel):
    username: str
    email: Union[str, None]
    token: str

class UserBase(BaseModel):
    id: int 
    username: str
    email: Union[str, None]
    token: str