from collections.abc import Callable
from typing import Awaitable, TypeAlias

from fastapi import Request, Response

FastAPIMiddlewareNextFunction: TypeAlias = Callable[[Request], Awaitable[Response]]
FastAPIMiddlewareFunction: TypeAlias = Callable[
    [Request, FastAPIMiddlewareNextFunction], Awaitable[Response]
]
