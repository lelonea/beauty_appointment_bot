from aiohttp import web

from .routes import urls


def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(urls)
    return app
