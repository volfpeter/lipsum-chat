from htmy import ComponentType, PropertyValue, html


def centered(*children: ComponentType, class_: str = "", **props: PropertyValue) -> html.div:
    """
    Component factory that centers its children both horizontally and vertically.
    """
    return html.div(
        *children,
        class_=f"flex flex-col items-center justify-center h-full w-full gap-4 {class_}",
        **props,
    )
