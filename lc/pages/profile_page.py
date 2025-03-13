from typing import Any

from htmy import Component, Context, component, html

from lc.ui.centered import centered
from lc.ui.t_function import TFunction
from lc.user.model import User

from .page import page


@component
async def profile_page(_: Any, ctx: Context) -> Component:
    user: User | None = ctx.get("user")
    t = TFunction.from_context(ctx)

    return page(
        centered(
            html.div(
                html.label(await t("profile_page.username"), class_="font-semibold"),
                html.label(user.username if user else await t("profile_page.anonymus")),
                html.label(await t("profile_page.logged_in_at"), class_="font-semibold"),
                html.label(
                    user.logged_in_at if user else await t("profile_page.not_logged_in"),
                    class_="text-warning" if user is None else None,
                ),
                class_="grid grid-cols-[max-content_1fr] gap-4",
            )
        )
    )
