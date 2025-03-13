from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from fastapi import APIRouter, Depends, Form, Response
from fasthx.htmy import HTMY

from lc.ui.login_dialog import login_dialog
from lc.user.model import User

from .model import LoginForm

if TYPE_CHECKING:
    from lc.authenticator import Authenticator

_hx_redirect_home: dict[str, str] = {"HX-Redirect": "/", "HX-Push-URL": "true"}


def make_api(auth: Authenticator, htmy: HTMY) -> APIRouter:
    api_prefix = "/auth"
    api = APIRouter(prefix=api_prefix)

    @api.get("/login-dialog")
    @htmy.hx(login_dialog)
    async def get_login_dialog() -> str:
        return f"{api_prefix}/login"

    @api.post("/login", dependencies=[Depends(auth.requires_anonymus)])
    async def login(data: Annotated[LoginForm, Form()]) -> Response:
        user = User(username=data.username)
        return auth.login(
            user,
            Response(
                status_code=200,
                headers=_hx_redirect_home,
            ),
        )

    @api.get("/logout", dependencies=[Depends(auth.requires_user)])
    async def logout() -> Response:
        return auth.logout(
            Response(status_code=200, headers=_hx_redirect_home),
        )

    return api
