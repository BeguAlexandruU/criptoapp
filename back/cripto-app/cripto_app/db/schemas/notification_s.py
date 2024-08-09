from pydantic import UUID4, BaseModel, Field

class NotificationCreate(BaseModel):
    id_user: UUID4
    title : str = Field(max_length=30,example="title")
    message : str = Field(max_length=255,example="message")
    type : str = Field(default="notification")
    status : int = Field(default=0)

class NotificationBase(BaseModel):
    id: UUID4
    id_user: UUID4
    title : str = Field(max_length=30,example="title")
    message : str = Field(max_length=255,example="message")
    type : str = Field(default="notification")
    status : int = Field(default=0)