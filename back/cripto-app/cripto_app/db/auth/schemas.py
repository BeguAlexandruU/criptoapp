import uuid
from fastapi_users import schemas
from typing import Optional, Union
from pydantic import UUID4, Field, validator

class UserCreate(schemas.BaseUserCreate):
    name: str= Field(max_length=60, default="John Stethem")
    ref_code_parent: Union[UUID4, str] = ''
    # id_stripe_customer: Optional[str]= ''
    
    @validator('ref_code_parent', pre=True, always=True)
    def check_uuid_or_empty(cls, v):
        if v == '':
            return v
        try:
            return UUID4(v)
        except ValueError:
            raise ValueError('ref_code_parent must be a valid UUID4 or an empty string')
        
class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str
    # id_stripe_customer: str
    ref_code: str
    ref_code_parent: str

class UserUpdate(schemas.BaseUserUpdate):
    name: str
    # id_stripe_customer: str
    ref_code: str
    ref_code_parent: str

