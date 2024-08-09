from pydantic import UUID4, BaseModel, Field

class PostCreate(BaseModel):
    title: str=Field(default="Title")
    description: str=Field(...,example="Title")
    type: str
    status: int

class PostBase(BaseModel):
    id: UUID4
    title: str
    description: str
    type: str
    status: int
    