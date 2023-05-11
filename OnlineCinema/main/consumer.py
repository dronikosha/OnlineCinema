from channels.generic.websocket import AsyncWebsocketConsumer
import json


class VideoRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connect')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'video_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data['type']
        
        if message_type == 'pause':
            position = data['position']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'pause_video',
                    'position': position,
                    'clientId': data['clientId']
                }
            )
        
        elif message_type == 'start':
            position = data['position']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'start_video',
                    'position': position,
                    'clientId': data['clientId']
                }
            )

    async def pause_video(self, event):
        position = event['position']
        print('pause_video', event)
        await self.send(text_data=json.dumps({
            'type': 'pause',
            'position': position,
            'clientId': event['clientId']
        }))
        
    async def start_video(self, event):
        position = event['position']
        print('start_video', event)
        await self.send(text_data=json.dumps({
            'type': 'start',
            'position': position,
            'clientId': event['clientId']
        }))
