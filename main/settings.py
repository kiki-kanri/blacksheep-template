import apps.example

from apps.example.middlewares.example import example_middleware


INSTALLED_APPS = [
    apps.example
]

MIDDLEWARES = [
    example_middleware
]
