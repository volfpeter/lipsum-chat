from htmy import Component, Context, component, html

from .base_page import base_page
from .centered import centered
from .navbar import page_urls
from .t_function import TFunction


@component.context_only
async def not_found(ctx: Context) -> Component:
    t = TFunction.from_context(ctx)
    return base_page(
        centered(
            html.h1(
                await t("not_found.title"),
                class_="text-2xl font-semibold",
            ),
            html.p(await t("not_found.message"), class_="text-lg"),
            html.a(
                await t("not_found.navigate_home"),
                href=page_urls["home"],
                class_="btn btn-soft btn-primary",
            ),
        )
    )
