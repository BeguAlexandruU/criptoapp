from fastapi import APIRouter, Depends, HTTPException, Query, status, WebSocket, WebSocketDisconnect
from cripto_app.db.models import Notification
from cripto_app.db.crud import CrudBase
from cripto_app.db.database import get_db
from typing import Annotated, List
from sqlalchemy.orm import Session
from cripto_app.ws.ws import WSManager

DBD = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/ws",
    tags=["ws_routes"],
    responses={404: {"description": "Not found"}},
)

crud = CrudBase(Notification)

@router.websocket("/notification")
async def websocket_notify(websocket: WebSocket, db:DBD, token: str = Query(...)):
    if await WSManager.connect(websocket, "notification", db, token) == False:
        return

    try:
        while True:
            await WSManager.receive(websocket,"notification",db,token)
    except WebSocketDisconnect:
        await websocket.close()

@router.websocket("/post")
async def websocket_notify(websocket: WebSocket, db:DBD, token: str = Query(...)):
    if await WSManager.connect(websocket, "post", db, token) == False:
        return

    try:
        while True:
            await WSManager.receive(websocket,"post",db,token)
    except WebSocketDisconnect:
        await websocket.close()

