
from django.urls import re_path,path
from .consumers import *

websocket_urlpatterns = [
 
    # path('ws/sc/', MySyncConsumer.as_asgi()),
    path('ws/asc/',MyAsyncConsumer.as_asgi())
 
]
