from htmy import Component, Context, component, html

from lc.ui.dialog import dialog
from lc.ui.t_function import TFunction

_dialog_id = "login-dialog"


def _login_form(label: str) -> Component:
    """Login form component factory."""
    return html.div(
        html.label(label),
        html.input_(
            type="text",
            name="username",
            autofocus="",
            required="",
            minlength="3",
            pattern="[a-zA-Z0-9]{3,42}",
            class_="grow input validator",
        ),
        class_="flex items-center gap-2",
    )


@component
async def login_dialog(login_url: str, ctx: Context) -> Component:
    """Login dialog component."""
    t = TFunction.from_context(ctx)
    return dialog(
        {
            "id": _dialog_id,
            "title": await t("login_dialog.title"),
            "close": await t("login_dialog.close"),
            "content": _login_form(await t("login_dialog.username")),
            "submit": html.button(
                await t("login_dialog.submit"),
                class_="btn btn-primary",
                hx_post=login_url,
                hx_target="closest dialog",
                hx_swap="delete",
                hx_include=f"#{_dialog_id} input",
                hx_trigger="click, keyup[keyCode==13] from:input",
            ),
        }
    )
