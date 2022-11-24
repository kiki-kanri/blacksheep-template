from blacksheep.server.controllers import APIController, get


class Example(APIController):
    @classmethod
    def route(cls):
        return ''

    @get('/')
    async def hello_world():
        return 'Hello, world!'
