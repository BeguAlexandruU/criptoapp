from email import message
from fastapi import APIRouter, Depends, HTTPException, status,BackgroundTasks
from cripto_app.db.models import Post
from cripto_app.db.crud import CrudBase
from cripto_app.db.schemas.post_s import PostBase, PostCreate
from cripto_app.db.database import get_db
from typing import Annotated, List
from sqlalchemy.orm import Session
from cripto_app.ws.ws import WSManager
from fastapi.responses import StreamingResponse
from cripto_app.tasks.notifications import task_create_all_notifications


DBD = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/post",
    tags=["post"],
    responses={404: {"description": "Not found"}},
)

crud = CrudBase(Post)

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
async def create_post(entity: PostCreate, bg_tasks: BackgroundTasks, db: DBD):
    bg_tasks.add_task(task_create_all_notifications, title=entity.title, message=entity.description, type_notification=entity.type)
    
    res = await crud.create(db, entity)
    await WSManager.broadcast("ssssss", {"title": entity.title,
                            "description": entity.description, 
                            "type": entity.type, 
                            "status": entity.status
                            }, 
                            "back_end")
    return res

@router.put("/update", status_code=status.HTTP_200_OK)
async def update_entity(entity: PostBase, db: DBD):
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

