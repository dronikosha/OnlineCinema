from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/video/(?P<room_name>[-\w]+)/$', consumer.VideoRoomConsumer.as_asgi()),

]
