from htmy import Snippet

from .utils import replace_py_extension


def copy_button() -> Snippet:
    """
    Copy button.

    It must be within an AlpineJS component that has a `copy()` action and a `copied` state.
    """
    return Snippet(replace_py_extension(__file__))
