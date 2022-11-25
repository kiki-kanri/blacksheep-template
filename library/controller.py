from blacksheep import text
from blacksheep.server.controllers import APIController


class BaseAPIController(APIController):
    error = text('error', 500)
    error_422 = text('', 444)
    not_found_empty = text('', 404)
    success = text('success')
