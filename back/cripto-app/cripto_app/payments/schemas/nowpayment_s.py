from pydantic import UUID4, BaseModel

class InvoiceRequerements(BaseModel):
    product_id: UUID4