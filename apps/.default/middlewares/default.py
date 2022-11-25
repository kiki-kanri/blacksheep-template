from blacksheep import Request, Response
from typing import Awaitable, Callable


async def default_middleware(
    request: Request,
    handler: Callable[[Request], Awaitable[Response]]
):
    response = await handler(request)
    return response
