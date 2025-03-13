from fastapi import FastAPI, HTTPException

from lc.authenticator import Authenticator
from lc.pages.chat_page import chat_page
from lc.pages.index_page import index_page
from lc.pages.profile_page import profile_page
from lc.ui.navbar import ChatPageKey, chat_page_keys

from .htmy import htmy


def add_routes(app: FastAPI, *, auth: Authenticator) -> None:
    from lc.chat.api import make_api as make_chat_api
    from lc.user.auth_api import make_api as make_auth_api

    app.include_router(make_auth_api(auth, htmy))
    app.include_router(make_chat_api(htmy))

    @app.get("/ack", response_model=None)
    async def ack() -> None:
        """Just to have something to HTMX can call to trigger actions."""
        ...

    @app.get("/profile")
    @htmy.page(profile_page)
    async def me() -> None:
        """Profile page."""
        ...

    @app.get("/")
    @htmy.page(index_page)
    async def index() -> None:
        """Index page."""
        ...

    @app.get("/{page}")
    @htmy.page(chat_page)
    async def pages(page: ChatPageKey | str = "home") -> ChatPageKey:
        if page in chat_page_keys:
            return page  # type: ignore[return-value]

        raise HTTPException(status_code=404)
