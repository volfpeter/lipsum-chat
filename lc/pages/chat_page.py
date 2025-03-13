from htmy import Component, Context, component, html

from lc.ui.chat_bubble import chat_bubble
from lc.ui.chat_container import chat_container, chat_container_ref
from lc.ui.chat_input import chat_input
from lc.ui.navbar import ChatPageKey
from lc.ui.t_function import TFunction

from .page import page


@component
async def chat_page(key: ChatPageKey, ctx: Context) -> Component:
    t = TFunction.from_context(ctx)
    return page(
        html.div(
            chat_container(
                chat_bubble(await t(f"chat_page.{key}.hi")),
                chat_bubble(await t(f"chat_page.{key}.message")),
                chat_bubble(await t(f"chat_page.{key}.question")),
                # hx-swap=beforeend show:bottom should work on the chat input, but
                # it doesn't, so we trigger scroll to bottom manually.
                **{"hx-on:htmx:after-settle": "this.scroll(undefined, this.scrollHeight)"},
            ),
            chat_input(
                {
                    "hx-post": f"/chat/{key}",
                    "hx-target": chat_container_ref,
                    "hx-swap": "beforeend",
                }
            ),
            class_="flex flex-col px-6 gap-2 h-full w-full overflow-hidden",
        ),
    )
