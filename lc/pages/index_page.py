from typing import Any

from htmy import Component

from lc.ui.md import markdown
from lc.ui.utils import replace_py_extension

from .page import page


def index_page(_: Any) -> Component:
    """
    Component factory for the index page.
    """
    return page(markdown(replace_py_extension(__file__, "md")))
