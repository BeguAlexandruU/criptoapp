from pydantic import BaseModel, Field

class AdminCreate(BaseModel):
    firstname: str=Field(...,example="John")
    lastname : str=Field(...,example="Watson")
    username : str=Field(...,example="AnonimousUser")
    sold     : int
    password : str

class AdminBase(BaseModel):
    id: int
    firstname: str
    lastname : str
    username : str
    token : str
    sold     : int
    password : str
    