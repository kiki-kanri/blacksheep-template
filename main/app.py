from blacksheep import Application
from blacksheep.server.controllers import APIController, Controller
from mongoengine import connect

from instance.config import DATABASES, INSTALLED_APPS, SIGNING_KEY
from library.utils import import_attribute


def connect_db():
    connect(DATABASES['default'])


def install_apps(app: Application):
    for app_name in INSTALLED_APPS:
        controllers: list[APIController | Controller] = import_attribute(
            f'apps.{app_name}.controllers'
        )

        app.register_controllers(controllers)


def create_app():
    app = Application()
    app.use_sessions(SIGNING_KEY)

    install_apps(app)

    return app
