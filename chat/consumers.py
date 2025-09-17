import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatSocket(AsyncWebsocketConsumer):
    async def connector(self):
        await self.connect()

    # async def disconnect(self):
        # pass

    async def receive(self,text_data):
        print(text_data)

    async def send(self):
        await self.send(json.dumps({"Message":"Hello front"}))