from blacksheep import Request, Response
from typing import Awaitable, Callable


async def example_middleware(
    request: Request,
    handler: Callable[[Request], Awaitable[Response]]
):
    print(request)
    response = await handler(request)
    print(response)
    return response
