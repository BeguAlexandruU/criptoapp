import re
from typing import Dict, List
from cripto_app.db.auth.users import verify_jwt_token
from fastapi import WebSocket, Depends
from starlette.websockets import WebSocketState
from typing import Annotated
from cripto_app.db.database import get_db
from sqlalchemy.orm import Session
from cripto_app.db.crud import CrudBase
from cripto_app.db.models import Post, Notification
import json
from jwt.exceptions import DecodeError
CONNECTIONS = {}
DBD = Annotated[Session, Depends(get_db)]

class ConnectionManagerWS:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = CONNECTIONS

    async def connect(self, websocket: WebSocket, scope: str, db:DBD,token:str):
        await websocket.accept()
        
        # connections = self.active_connections
        # if connections.get(channel_id):
        #     connections[channel_id].append(websocket)
        # else:
        #     connections[channel_id] = [websocket]
        
        try:
            user = verify_jwt_token(token)
            id_user = user["sub"]
            channel_id = id_user
            connections = self.active_connections
            if connections.get(channel_id):
                connections[channel_id].append(websocket)
            else:
                connections[channel_id] = [websocket]
            # await websocket.send_json({"message": f"{id}","data": user, "sender": "you"})
        except DecodeError as err:
            await websocket.send_json({"message": "Error: Invalid token", "sender": "you"})
            await websocket.close()
            return False
        except Exception as err:
            await websocket.send_json({"message": f"Error: {err}", "sender": "you"})
            await websocket.close()
            return False

        return True


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

    async def broadcast(self, message: dict, scope: str):
        try:
            connections = self.active_connections
            for channel_id, ws_channel in connections.items():
                print(f"\nBroadcast send to {channel_id}")
                for ws in ws_channel:
                    if ws.client_state == WebSocketState.CONNECTED:
                        await ws.send_json(message)
                    else:
                        ws_channel.remove(ws)
            print(f"\nBroadcast send to all")
        except Exception as err:
            print(f"Error: {err}")

    async def send_personal_message(self, message: str, websocket: WebSocket):
        if websocket.application_state == WebSocketState.CONNECTED:
            await websocket.send_json({"message": message, "sender": "you"})

    async def receive(self, websocket: WebSocket,scope:str, db:DBD, token:str):
        data = await websocket.receive_text()
        
        # match scope:
        #     case "notification":
        #         res = await CrudBase(Notification).read_all(db)
        #         res_json = [{"title": ob.title,
        #                     "message": ob.message, 
        #                     "type": ob.type, 
        #                     "status": ob.status
        #                     } for ob in res]
        #     case "post":
        #         res = await CrudBase(Post).read_all(db)
        #         res_json = [{"title": ob.title,
        #                     "description": ob.description, 
        #                     "type": ob.type, 
        #                     "status": ob.status
        #                     } for ob in res]
        
        # for obj in res_json:
        #     if websocket.client_state == WebSocketState.CONNECTED:
        #         await websocket.send_json(obj)
        #     else:
        #         break
        
        # return data
        

WSManager = ConnectionManagerWS()