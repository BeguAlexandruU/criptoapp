from pydantic import UUID4, BaseModel, Field
from datetime import datetime

class WalletCreate(BaseModel):
    id_user   : UUID4
    id_product: UUID4
    # id_stripe_subscription: str
    status     : int
    start_date : datetime
    end_date   : datetime

class WalletBase(BaseModel):
    id        : UUID4
    id_user   : UUID4
    id_product: UUID4
    # id_stripe_subscription: str
    status     : int
    start_date : datetime
    end_date   : datetime
    