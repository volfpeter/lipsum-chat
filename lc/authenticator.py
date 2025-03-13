from fastapi import HTTPException, Request, Response
from htmy import Context
from pydantic import ValidationError

from .fastapi import FastAPIMiddlewareNextFunction
from .user.model import User


class Authenticator:
    """
    Authenticator with cookie-based login.

    It requires its middleware to be added to the FastAPI app.

    The authenticator also provides an `htmy` request processor that (if used)
    automatically adds the current user (may be `None`) to `htmy` rendering
    contexts under the `user` key.
    """

    __slots__ = ()

    def login(self, user: User, response: Response) -> Response:
        """Logs in the given user."""
        response.set_cookie("user", user.model_dump_json())
        return response

    def logout(self, response: Response) -> Response:
        """Logs out the current user."""
        response.delete_cookie("user")
        return response

    def current_user(self, request: Request) -> User | None:
        """FastAPI dependency that returns the current user."""
        return getattr(request.state, "user", None)

    async def middleware(self, request: Request, call_next: FastAPIMiddlewareNextFunction) -> Response:
        """
        FastAPI middleware that sets the `request.state.user` attribute to the current user.
        """
        cookie = request.cookies.get("user")
        if cookie:
            try:
                user: User | None = User.model_validate_json(cookie)
                request.state.user = user
            except ValidationError as e:
                raise HTTPException(status_code=401, detail="Invalid authentication token.") from e

        return await call_next(request)

    def htmy_context_processor(self, request: Request) -> Context:
        """
        `htmy` context processor that adds the current user to the rendering context.
        """
        return {"user": self.current_user(request)}

    def requires_anonymus(self, request: Request) -> None:
        """
        FastAPI dependency that raises an `HTTPException` if there is a logged in user.
        """
        user = self.current_user(request)
        if user is not None:
            HTTPException(status_code=403, detail="Forbidden")

    def requires_user(self, request: Request) -> User:
        """
        FastAPI dependency that returns the current user or raises an
        `HTTPException` if there is no logged in user.
        """
        user = self.current_user(request)
        if user is None:
            HTTPException(status_code=401, detail="Unauthorized")

        return user  # type: ignore[return-value]
