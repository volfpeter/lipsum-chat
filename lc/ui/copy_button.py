from htmy import Snippet

from .utils import replace_py_extension


def copy_button() -> Snippet:
    """
    Copy button.

    It must be within an AlpineJS component that has a `copy()` action and a `copied` state,
    and it attempts to copy the text content of the element (within the AlpineJS component)
    that has the `x_ref="clipboardContent"` attribute.
    """
    return Snippet(replace_py_extension(__file__))
