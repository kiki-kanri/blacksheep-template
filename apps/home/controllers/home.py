from blacksheep.server.controllers import APIController, get


class Home(APIController):
    @classmethod
    def route(cls):
        return ''

    @get('/')
    async def home():
        return 'Hello, world!'
