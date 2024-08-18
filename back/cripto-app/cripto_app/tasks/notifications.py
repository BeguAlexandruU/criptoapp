
from cripto_app.db.auth import users
from cripto_app.db.crud import CrudBase
from cripto_app.db.database import SessionLocal
from cripto_app.db.models import Notification, User
from cripto_app.db.schemas.notification_s import NotificationCreate
from fastapi import HTTPException
from fastapi.responses import JSONResponse

async def create_notification(entity: NotificationCreate):
    try:
      notify_crud = CrudBase(Notification)
      async with SessionLocal() as db:
          await notify_crud.create(db, entity)
    except Exception as err:
        raise HTTPException(status_code=404, detail=f"Internal error: {err}")

async def task_create_all_notifications(
    title: str,
    message: str,
    type_notification: str
  ):
    try:
      users_crud = CrudBase(User)
      async with SessionLocal() as db:
        all_users = await users_crud.read_all(db)
        
      for user in all_users:
          entity = NotificationCreate(
            id_user=user.id,
            title=title,
            type=type_notification,
            message=message
          )
          await create_notification(entity)
          print(f"Notification created for user {user.id}")
          # await asyncio.sleep(10)
        
      return JSONResponse(
          content={
            "detail": "Notifications created successfully",
            "time_execution": "0.0001"
            }, 
          status_code=201
        )
    except Exception as err:
        raise HTTPException(status_code=404, detail=f"Internal error: {err}")
    