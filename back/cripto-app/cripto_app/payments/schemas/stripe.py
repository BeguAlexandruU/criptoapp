from pydantic import BaseModel, EmailStr, Field

class Customer(BaseModel):
    name: str = Field(..., max_length=60)
    email: EmailStr