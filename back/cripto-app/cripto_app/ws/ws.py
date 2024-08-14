from typing import Dict, List
from fastapi import WebSocket, Depends
from starlette.websockets import WebSocketState
from typing import Annotated
from cripto_app.db.database import get_db
from sqlalchemy.orm import Session
from cripto_app.db.crud import CrudBase
from cripto_app.db.models import Post, Notification
import json

CONNECTIONS = {}
DBD = Annotated[Session, Depends(get_db)]

class ConnectionManagerWS:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = CONNECTIONS

    async def connect(self, websocket: WebSocket, channel_id: str, scope: str, db:DBD):
        await websocket.accept()
        
        connections = self.active_connections
        if connections.get(channel_id):
            connections[channel_id].append(websocket)
        else:
            connections[channel_id] = [websocket]

        match scope:
            case "notification":
                res = await CrudBase(Notification).read_all(db)
                res_json = [{"title": ob.title,
                            "message": ob.message, 
                            "type": ob.type, 
                            "status": ob.status
                            } for ob in res]
            case "post":
                res = await CrudBase(Post).read_all(db)
                res_json = [{"title": ob.title,
                            "description": ob.description, 
                            "type": ob.type, 
                            "status": ob.status
                            } for ob in res]
        
        for obj in res_json:
            # print(obj.dict())
            await websocket.send_json(obj)

        # await websocket.send_json(res_json)
        # await websocket.send_json({"message": res_json, "sender": "you"})

    async def disconnect(self, channel_id: str, websocket: WebSocket):
        if self.active_connections.get(channel_id):
            self.active_connections[channel_id].remove(websocket)
            count = self.connection_count(channel_id=channel_id)
            await self.send_connection_count(channel_id, count)

    def connection_count(self, channel_id: str):
        connection = self.active_connections
        if connection.get(channel_id):
            return len(connection[channel_id])
        return 0

    async def send_connection_count(self, channel_id: str, count: int):
        connections = self.active_connections
        if connections.get(channel_id):
            ws_channel = connections[channel_id]
            for ws in ws_channel:
                if ws.application_state == WebSocketState.CONNECTED:
                    await ws.send_json({"connection_count": count})

    async def broadcast(self, channel_id: str, message: str, sender: str):
        connections = self.active_connections
        if connections.get(channel_id):
            ws_channel = connections[channel_id]
            for ws in ws_channel:
                if ws.application_state == WebSocketState.CONNECTED:
                    await ws.send_json(message)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        if websocket.application_state == WebSocketState.CONNECTED:
            await websocket.send_json({"message": message, "sender": "you"})

    async def receive(self, websocket: WebSocket):
        data = await websocket.receive_text()
        return data
        

WSManager = ConnectionManagerWS()