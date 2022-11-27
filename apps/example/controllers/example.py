from blacksheep import Request
from blacksheep.server.controllers import APIController, get


class Example(APIController):
    @classmethod
    def route(cls):
        return '/api'

    @get('/')
    async def hello_world(request: Request):
        return 'Hello World!'
