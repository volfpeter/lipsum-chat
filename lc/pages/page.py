from htmy import ComponentType, Context, component, html

from lc.ui.base_page import base_page
from lc.ui.navbar import navbar
from lc.ui.t_function import TFunction
from lc.user.model import User


def login_button(title: str) -> html.button:
    return html.button(
        title,
        hx_get="/auth/login-dialog",
        hx_target="#dialogs",
        class_="btn btn-primary",
    )


@component
async def page(content: ComponentType, ctx: Context) -> ComponentType:
    """
    Page with navbar.
    """
    user: User | None = ctx.get("user")
    t = TFunction.from_context(ctx)

    user_menu: ComponentType
    if user is None:
        user_menu = login_button(await t("page.button.login"))
    else:
        user_menu = user.user_menu()

    return base_page(
        html.div(
            navbar(user_menu),
            html.div(content, class_="flex flex-col h-full overflow-auto"),
            class_="flex flex-col h-full w-full p-4 gap-8 lg:w-5xl",  # 5xl is the lg breakpoint width
        )
    )
