from typing import Dict, List

from fastapi import WebSocket

# from services.service_utils.auth_utils import ws_access_token

CONNECTIONS = {}

class ConnectionManagerWS:
    # INITIALIZE THE LIST AND CONNECTION

    def __init__(self):
        """example:
        [{
        "channel_id":[Websocket]
        0370643958
        }]
        """
        self.active_connections: Dict[str, List[WebSocket]] = CONNECTIONS

    # CONNECT TO WEBSOCKET AND APPEND TO THE LIST
    async def connect(self, websocket: WebSocket, channel_id: str):
        await websocket.accept()
        
        connections = self.active_connections
        if connections.get(channel_id):
            connections[channel_id].append(websocket)
        else:
            connections[channel_id] = [websocket]

        count = self.connection_count(channel_id=channel_id)

        ws_channel = connections[channel_id]
        for ws in ws_channel:
            ws: WebSocket = ws
            await ws.send_json({"connection_count": count})

    # PURGE WEBSOCKET LIST STORE
    async def disconnect(self, channel_id: str, websocket: WebSocket):
        if self.active_connections.get(channel_id):
            self.active_connections[channel_id].remove(websocket)
            count = self.connection_count(channel_id=channel_id)
            ws_channel = self.active_connections[channel_id]
            for ws in ws_channel:
                ws: WebSocket = ws
                await ws.send_json({"connection_count": count})

    def connection_count(self, channel_id: str):
        connection = self.active_connections
        if connection.get(channel_id):
            return len(connection[channel_id])

    # Send a retry message to a user WebSocket
    async def broadcast(
        self, channel_id: str, message: str, sender: str
    ):
        connections = self.active_connections
        if connections.get(channel_id):
            ws_channel = connections[channel_id]

            for ws in ws_channel:
                ws: WebSocket = ws
                # if ws != not_send:
                await ws.send_json(
                        {
                            "message": message,
                            "sender": sender,
                        }
                    )

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(
            {
                "message": message,
                "sender": "you",
            }
        )
    
    async def receive(self, websocket: WebSocket):
        # data = await websocket.receive_text()
        return await websocket.receive_text()
    

WSManager = ConnectionManagerWS()