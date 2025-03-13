from typing import Literal, get_args

from fasthx.htmy import CurrentRequest
from htmy import Component, Context, Slots, Snippet, component, html

from .t_function import TFunction
from .utils import replace_py_extension

# Chat page keys in the order in which they should appear in the navbar.
ChatPageKey = Literal["coffee", "beer"]
chat_page_keys = get_args(ChatPageKey)

# Page keys in the order in which they should appear in the navbar.
PageKey = Literal[
    "home",
    ChatPageKey,
    "profile",
]

page_keys = get_args(PageKey)
page_urls: dict[PageKey, str] = {
    "home": "/",
    "coffee": "/coffee",
    "beer": "/beer",
    "profile": "/profile",
}
"""Page key to URL mapping."""


def _get_button_style(key: str, current_path: str) -> str:
    """Returns the button style for the given key and path."""
    current_path = current_path.strip("/")
    if current_path == "":
        current_path = "home"

    base_style = "btn btn-ghost"
    return f"{base_style} btn-active" if current_path == key else base_style


@component
async def nav_item(key: PageKey, ctx: Context) -> html.li:
    """A single item in the navbar."""
    request = CurrentRequest.from_context(ctx)
    t = TFunction.from_context(ctx)
    return html.li(
        html.a(
            await t(f"navbar.{key}"),
            href=page_urls[key],
            class_=_get_button_style(key, request.url.path),
        )
    )


def navbar(nav_action: Component = "") -> Snippet:
    """Navbar component factory."""
    return Snippet(
        replace_py_extension(__file__),
        Slots(
            {
                "nav-items": [nav_item(key) for key in page_keys],
                "nav-action": nav_action,
            }
        ),
    )
