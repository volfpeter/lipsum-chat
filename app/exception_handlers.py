from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse

from lc.ui.base_page import base_page
from lc.ui.not_found import not_found

from .htmy import htmy


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(401)
    @app.exception_handler(403)
    @app.exception_handler(404)
    async def handle_not_found(request: Request, _: HTTPException) -> HTMLResponse:
        return HTMLResponse(await htmy.render_component(base_page(not_found()), request))
