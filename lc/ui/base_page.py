from htmy import ComponentType, Slots, Snippet

from .utils import replace_py_extension


def base_page(*content: ComponentType) -> Snippet:
    """Page component factory."""
    return Snippet(replace_py_extension(__file__), Slots({"content": content}))
