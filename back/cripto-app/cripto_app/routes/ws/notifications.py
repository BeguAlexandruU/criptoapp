from fastapi import APIRouter, Depends, HTTPException, status, WebSocket, WebSocketDisconnect
from cripto_app.db.models import Notification
from cripto_app.db.crud import CrudBase
from cripto_app.db.database import get_db
from typing import Annotated, List
from sqlalchemy.orm import Session

DBD = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/notify",
    tags=["ws_notifications"],
    responses={404: {"description": "Not found"}},
)

crud = CrudBase(Notification)

@router.websocket("/ws")
async def websocket_notify(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        await websocket.close()