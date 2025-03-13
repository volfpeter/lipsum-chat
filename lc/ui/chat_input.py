from htmy import Component, Context, Properties, component, html

from lc.ui.t_function import TFunction

_chat_input_id = "chat-input"
_hx_trigger = f"keyup[keyCode==13&&!shiftKey] consume from:#{_chat_input_id}"


@component
async def chat_input(props: Properties, ctx: Context) -> Component:
    """
    Chat input component.
    """
    t = TFunction.from_context(ctx)
    return html.textarea(
        id=_chat_input_id,
        name="message",
        placeholder=await t("chat_input.prompt"),
        class_="textarea w-full m-2",
        autofocus="",
        rows=3,
        **props,
        hx_trigger=_hx_trigger,
    )
