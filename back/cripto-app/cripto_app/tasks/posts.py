
from cripto_app.db.auth import users
from cripto_app.db.crud import CrudBase
from cripto_app.db.database import SessionLocal
from cripto_app.db.models import  User
from cripto_app.ws.ws import WSManager
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import asyncio


def task_broadcast_new_post(
  title: str, 
  message: str, 
  type_notification: str,
  status: int,
  created_at: str
  ):
    try:
      print(f"\nChanall Broadcasts: {WSManager.active_connections}")
      
      WSManager.broadcast(
          {
              "title": title,
              "description": message, 
              "type": type_notification, 
              "status": status,
              "created_at": created_at
          }, 
          "back_end"
      )

    except Exception as err:
        raise HTTPException(status_code=404, detail=f"Internal error: {err}")