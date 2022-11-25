from blacksheep import Application
from mongoengine import connect

from instance.config import DATABASES, SIGNING_KEY
from .settings import INSTALLED_APPS, MIDDLEWARES


def connect_db():
    connect(DATABASES['default'])


def install_apps(blacksheep_app: Application):
    for app in INSTALLED_APPS:
        blacksheep_app.register_controllers(app.controllers)

    blacksheep_app.middlewares += MIDDLEWARES


def create_app():
    blacksheep_app = Application()
    blacksheep_app.use_sessions(SIGNING_KEY)

    install_apps(blacksheep_app)

    return blacksheep_app
