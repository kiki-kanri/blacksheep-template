from blacksheep import Request
from blacksheep.server.controllers import get

from library.controller import BaseAPIController


class Example(BaseAPIController):
    @classmethod
    def route(cls):
        return ''

    @get('/')
    async def hello_world(self, request: Request):
        return 'Hello, world!'
