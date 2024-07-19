from pydantic import BaseModel, Field
from typing import Union

class NotificationCreate(BaseModel):
    id_user: str
    title : str = Field(max_length=30,example="title")
    message : str = Field(max_length=255,example="message")
    type : str = Field(default="notification")
    status : int = Field(default=0)

class NotificationBase(BaseModel):
    id: int
    id_user: str
    title : str = Field(max_length=30,example="title")
    message : str = Field(max_length=255,example="message")
    type : str = Field(default="notification")
    status : int = Field(default=0)