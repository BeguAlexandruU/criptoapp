from pydantic import BaseModel, Field
from datetime import datetime

class WalletCreate(BaseModel):
    id_user    : str
    id_product : int
    status     : int = Field(default=0)

class WalletBase(BaseModel):
    id        : int
    id_user   : str
    id_product: int
    status     : int
    start_date : datetime
    end_date   : datetime
    