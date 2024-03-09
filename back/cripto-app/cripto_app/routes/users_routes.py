from fastapi import APIRouter, Depends, status, HTTPException
from cripto_app.db.models import User
from cripto_app.db.crud import CrudBase
from cripto_app.db.schemas.user_s import UserCreate
from cripto_app.db.database import get_db
from typing import Annotated, List
from sqlalchemy.orm import Session

DBD = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

crud = CrudBase(User)

@router.get("/all", status_code=status.HTTP_200_OK)
async def read_users(db: DBD):
    users = await crud.read_all(db)
    return users

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_users(user: UserCreate, db: DBD):
    users = await crud.create(db, user)
    return users
