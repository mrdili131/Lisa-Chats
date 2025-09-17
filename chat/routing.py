from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('ws/chat/<str:chat_name>/',consumers.ChatSocket.as_asgi())
]