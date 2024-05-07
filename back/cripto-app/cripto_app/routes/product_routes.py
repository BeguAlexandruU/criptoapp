from fastapi import APIRouter, Depends, status
from cripto_app.db.models import Product
from cripto_app.db.crud import CrudBase
from cripto_app.db.schemas.product_s import ProductCreate
from cripto_app.db.database import get_db
from typing import Annotated, List
from sqlalchemy.orm import Session

DBD = Annotated[Session, Depends(get_db)]

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

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_entity(entity: ProductCreate, db: DBD):
    res = await crud.create(db, entity)
    return res

