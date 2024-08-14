from fastapi import APIRouter, Depends, HTTPException, status, WebSocket, WebSocketDisconnect
from cripto_app.db.models import Notification
from cripto_app.db.crud import CrudBase
from cripto_app.db.database import get_db
from typing import Annotated, List
from sqlalchemy.orm import Session
from cripto_app.ws.ws import WSManager

DBD = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/ws",
    tags=["ws_notifications"],
    responses={404: {"description": "Not found"}},
)

crud = CrudBase(Notification)

@router.websocket("/notification")
async def websocket_notify(websocket: WebSocket, db:DBD):
    await WSManager.connect(websocket, "e5trhfgngrwe4t5rtfbggewret", "notification", db)

    try:
        while True:
            
            await WSManager.receive(websocket)
            # await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        await websocket.close()

@router.websocket("/post")
async def websocket_notify(websocket: WebSocket, db:DBD):
    await WSManager.connect(websocket, "ssssss", "post", db)

    try:
        while True:
            
            await WSManager.receive(websocket)
            # await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        await websocket.close()

