from cripto_app.payments.stripe import StripeClient
from cripto_app.settings import STRIPE_SECRET_KEY
from fastapi import APIRouter, Depends, HTTPException, status
from cripto_app.db.models import Product
from cripto_app.db.crud import CrudBase
from cripto_app.db.schemas.product_s import ProductBase, ProductCreate
from cripto_app.db.database import get_db
from typing import Annotated, List
from sqlalchemy.orm import Session

DBD = Annotated[Session, Depends(get_db)]
Stripe = StripeClient(STRIPE_SECRET_KEY)

router = APIRouter(
    prefix="/product",
    tags=["product"],
    responses={404: {"description": "Not found"}},
)

crud = CrudBase(Product)

@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all(db: DBD):
    res = await crud.read_all(db)
    return res

@router.get("/{item_id}", status_code=status.HTTP_200_OK)
async def get_by_id(item_id: int, db: DBD):
    res = await crud.read(db, item_id)
    if not res:
        raise HTTPException(status_code=404, detail="Item not found")
    return res

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_entity(entity: ProductCreate, db: DBD):

    # product = Stripe.create_product(entity.title, entity.description)
    # if product is None:
    #     raise HTTPException(status_code=404, detail="Error creating stripe product")
    
    # price = Stripe.create_price(entity.price, entity.duration, product.id)
    # if price is None:
    #     raise HTTPException(status_code=404, detail="Error creating stripe price")
    
    # entity.id_stripe_product = product.id
    # entity.id_stripe_price = price.id

    res = await crud.create(db, entity)
    return res

@router.put("/update", status_code=status.HTTP_200_OK)
async def update_entity(entity: ProductBase, db: DBD):
    existing_item = await crud.read(db, entity.id)
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    res = await crud.update(db, existing_item, entity)
    return res

@router.delete("/remove/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_entity(item_id: int, db: DBD):
    existing_item = await crud.read(db, item_id)
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    await crud.delete(db, item_id)
    return {"detail": "Item removed successfully"}
