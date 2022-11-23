from blacksheep import Application
from blacksheep.server.controllers import APIController, Controller

from instance.config import INSTALLED_APPS, SIGNING_KEY
from library.utils import import_attribute


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
