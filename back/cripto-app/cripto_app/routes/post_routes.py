from fastapi import APIRouter, Depends, status, HTTPException
from cripto_app.db.models import Post
from cripto_app.db.crud import CrudBase
from cripto_app.db.schemas.post_s import PostCreate, PostBase
from cripto_app.db.database import get_db
from typing import Annotated, List
from sqlalchemy.orm import Session

DBD = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/post",
    tags=["post"],
    responses={404: {"description": "Not found"}},
)

crud = CrudBase(Post)

@router.get("/all", status_code=status.HTTP_200_OK)
async def read_posts(db: DBD):
    posts = await crud.read_all(db)
    return posts

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, db: DBD):
    posts = await crud.create(db, post)
    return posts

