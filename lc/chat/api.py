from typing import Annotated

from fastapi import APIRouter, Form
from fasthx.htmy import HTMY
from htmy import Component, Text

from lc.ui.chat_bubble import chat_bubble, chat_bubble_with_clipboard
from lc.ui.chat_container import chat_container_ref
from lc.ui.chat_input import chat_input
from lc.ui.md import markdown
from lc.ui.navbar import ChatPageKey

from .bot import get_response
from .model import Message


def make_api(htmy: HTMY) -> APIRouter:
    api = APIRouter(prefix="/chat")

    @api.post("/{key}", response_model=None)
    @htmy.page(lambda result: result)
    async def chat(message: Annotated[Message, Form()], key: ChatPageKey) -> Component:
        return (
            chat_bubble(markdown(Text(message.message)), speaker="user"),
            chat_bubble_with_clipboard(*get_response(message.message, corpus=key)),
            chat_input(
                {
                    "hx-swap-oob": "true",
                    "hx-post": f"/chat/{key}",
                    "hx-target": chat_container_ref,
                    "hx-swap": "beforeend",
                }
            ),
        )

    return api
