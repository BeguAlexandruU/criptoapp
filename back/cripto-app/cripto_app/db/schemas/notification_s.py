from pydantic import BaseModel, Field
from typing import Union

class NotificationCreate(BaseModel):
    id_user: int
    id_post: int
    status : int = Field(default=0)

class NotificationBase(BaseModel):
    id: int
    id_user: int
    id_post: int
    status : int
    