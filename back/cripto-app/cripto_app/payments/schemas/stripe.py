from pydantic import BaseModel, EmailStr, Field

class Customer(BaseModel):
    name: str=Field(max_length=30),
    email: EmailStr