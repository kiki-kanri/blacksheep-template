import orjson

from blacksheep import Application
from blacksheep.plugins import json
from blacksheep.server.controllers import APIController, Controller
from mongoengine import connect

from instance.config import DATABASES, SIGNING_KEY
from library.utils import import_attribute
from .settings import INSTALLED_APPS, MIDDLEWARES


def connect_db():
    connect(**DATABASES['default'])


def install_apps(blacksheep_app: Application):
    for app_name in INSTALLED_APPS:
        controllers: list[APIController | Controller] = import_attribute(
            f'apps.{app_name}.controllers'
        )

        blacksheep_app.register_controllers(controllers)

    for middleware_path in MIDDLEWARES:
        middleware = import_attribute(middleware_path)
        blacksheep_app.middlewares.append(middleware)


def setup_orjson():
    # Setup orjson
    def serialize(value) -> str:
        return orjson.dumps(value).decode('utf8')

    json.use(dumps=serialize, loads=orjson.loads)


def create_app():
    blacksheep_app = Application()
    blacksheep_app.use_sessions(SIGNING_KEY)

    connect_db()
    setup_orjson()

    install_apps(blacksheep_app)

    return blacksheep_app
