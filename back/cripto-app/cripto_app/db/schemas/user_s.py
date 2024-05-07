from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    firstname: str=Field(...,example="John")
    lastname : str=Field(...,example="Watson")
    email    : str=Field(...,example="JohnWatson@mail.com")
    ref_code : int
    id_ref   : int
    password : str

class UserBase(BaseModel):
    id: int
    firstname: str
    lastname : str
    email    : str
    ref_code : int
    id_ref   : int
    password : str
    
    