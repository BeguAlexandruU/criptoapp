
from cripto_app.db.auth import users
from cripto_app.db.crud import CrudBase
from cripto_app.db.database import SessionLocal
from cripto_app.db.models import  User
from cripto_app.ws.ws import WSManager
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import asyncio


async def task_broadcast_new_post(
  title: str, 
  message: str, 
  type_notification: str,
  status: int
  ):
    try:
      # users_crud = CrudBase(User)
      # async with SessionLocal() as db:
      #   all_users = await users_crud.read_all(db)
      
      print(f"\nChanall Broadcasts: {WSManager.active_connections}")
      
      await WSManager.broadcast(
          {
              "title": title,
              "description": message, 
              "type": type_notification, 
              "status": status
          }, 
          "back_end"
      )
      # print(f"\nPost send to broadcast for user {user.id}")
        
      
    except Exception as err:
        raise HTTPException(status_code=404, detail=f"Internal error: {err}")