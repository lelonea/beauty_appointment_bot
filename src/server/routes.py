from aiohttp import web
from server.views import health_check

urls = [
    web.get("/", health_check),
]
