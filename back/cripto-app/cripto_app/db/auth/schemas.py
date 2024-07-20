import uuid
from fastapi_users import schemas
from typing import Union
from pydantic import UUID4, validator

class UserCreate(schemas.BaseUserCreate):
    ref_code_parent: Union[UUID4, str] = ''
    
    # Validation of the ref_code_parent field
    @validator('ref_code_parent', pre=True, always=True)
    def check_uuid_or_empty(cls, v):
        if v == '':
            return v
        try:
            return UUID4(v)
        except ValueError:
            raise ValueError('ref_code_parent must be a valid UUID4 or an empty string')
        
class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass

