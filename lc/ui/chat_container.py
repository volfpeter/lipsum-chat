from htmy import ComponentType, PropertyValue, html

_chat_container_id = "chat-container"
chat_container_ref = f"#{_chat_container_id}"


def chat_container(*children: ComponentType, **props: PropertyValue) -> html.div:
    return html.div(
        *children,
        id=_chat_container_id,
        class_="flex flex-col grow gap-1 px-6 overflow-y-auto",
        **props,
    )
