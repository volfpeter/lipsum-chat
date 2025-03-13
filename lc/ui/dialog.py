from typing import TypedDict

from htmy import Component, Slots, Snippet

from .utils import replace_py_extension


class DialogProps(TypedDict):
    id: str
    title: str
    close: str
    content: Component
    submit: Component


def dialog(props: DialogProps) -> Snippet:
    """Dialog component factory."""
    return Snippet(
        replace_py_extension(__file__),
        Slots({"content": props["content"], "submit": props["submit"]}),
        text_processor=lambda text, _: text.format(
            id=props["id"],
            title=props["title"],
            close=props["close"],
        ),
    )
