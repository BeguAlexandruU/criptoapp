from datetime import datetime, timedelta
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from cripto_app.db.models import Product, Wallet
from cripto_app.db.crud import CrudBase
from cripto_app.db.schemas.wallet_s import WalletBase, WalletCreate
from cripto_app.db.database import get_db
from typing import Annotated, List
from sqlalchemy import select, text
from sqlalchemy.orm import Session
from cripto_app.db.auth.users import current_active_user
from cripto_app.db.auth.schemas import UserRead

DBD = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/wallet",
    tags=["wallet"],
    responses={404: {"description": "Not found"}},
)

crud = CrudBase(Wallet)

@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all(db: DBD):
    res = await crud.read_all(db)
    return res

@router.get("/user", status_code=status.HTTP_200_OK)
async def get_by_user(db: DBD, user: UserRead = Depends(current_active_user)):

    stmt = select(Wallet.status, Wallet.start_date, Wallet.end_date, Product.title, Product.description).where(Wallet.id_user == str(user.id)).join(Product, Wallet.id_product == Product.id)
    result = await db.execute(stmt)

    db_obj = result.mappings().all()

    return db_obj

@router.get("/{item_id}", status_code=status.HTTP_200_OK)
async def get_by_id(item_id: int, db: DBD):
    res = await crud.read(db, item_id)
    if not res:
        raise HTTPException(status_code=404, detail="Item not found")
    return res

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_entity(entity: WalletCreate, db: DBD, user: UserRead = Depends(current_active_user)):

    product = await CrudBase(Product).read(db, entity.id_product)

    # Convert WalletCreate to a dictionary
    entity_dict = entity.dict()
    
    # Add the new field
    entity_dict['id'] = uuid.uuid4()
    entity_dict['id_user'] = str(user.id)
    entity_dict['start_date'] = datetime.now()
    entity_dict['end_date'] = datetime.now() + timedelta(days=product.duration)

    # Convert the dictionary to WalletBase
    entity: WalletBase = WalletBase(**entity_dict)

    print(entity.__dict__)

    res = await crud.create(db, entity)
    return res


@router.put("/update", status_code=status.HTTP_200_OK)
async def update_entity(entity: WalletBase, db: DBD):
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
