from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter

from django.core.asgi import get_asgi_application

from main.routing import websocket_urlpatterns


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineCinema.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        websocket_urlpatterns
    ),
})