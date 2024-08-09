from pydantic import UUID4, BaseModel, Field
from datetime import datetime

class WalletCreate(BaseModel):
    id_user    : str | UUID4
    id_product : UUID4
    status     : int = Field(default=0)

class WalletBase(BaseModel):
    id        : UUID4
    id_user   : UUID4
    id_product: UUID4
    status     : int
    start_date : datetime
    end_date   : datetime
    