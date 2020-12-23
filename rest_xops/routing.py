# @Time    : 2019/3/13 10:56
# @Author  : xufqing
from apps.websocket.jwt_auth import TokenAuthMiddleware
from channels.routing import URLRouter, ProtocolTypeRouter
from django.urls import path
from apps.websocket.consumers.console import ConsoleMsgConsumer

application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddleware(
        URLRouter([
            path(r"websocket/console", ConsoleMsgConsumer),
        ])
    )
})