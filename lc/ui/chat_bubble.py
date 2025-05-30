from typing import Literal

from htmy import ComponentType, html

from .copy_button import copy_button

Speaker = Literal["user", "assistant"]

_bubble_classes: dict[Speaker, str] = {
    "user": "chat-bubble chat-bubble-info",
    "assistant": "chat-bubble chat-bubble-success",
}
_chat_classes: dict[Speaker, str] = {
    "assistant": "chat chat-start",
    "user": "chat chat-end",
}


def chat_bubble(*parts: ComponentType, speaker: Speaker = "assistant") -> html.div:
    """Multi-line chat bubble component factory."""
    return html.div(
        html.div(*parts, class_=_bubble_classes[speaker]),
        class_=f"flex flex-col chat {_chat_classes[speaker]}",
    )


def chat_bubble_with_clipboard(*parts: ComponentType, speaker: Speaker = "assistant") -> html.div:
    """Multi-line chat bubble component factory with clipboard support."""
    return html.div(
        html.div(
            html.div(*parts, x_ref="clipboardContent"),
            copy_button(),
            class_=f"{_bubble_classes[speaker]} grid grid-cols-[1fr_max-content] gap-2",
        ),
        x_data="clipboard",
        class_=f"flex flex-col chat {_chat_classes[speaker]}",
    )
