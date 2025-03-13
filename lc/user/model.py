from datetime import UTC, datetime

from htmy import Context, component, html
from pydantic import BaseModel, Field

from lc.ui.t_function import TFunction


class LoginForm(BaseModel):
    username: str = Field(min_length=3, max_length=42, pattern=r"^[a-zA-Z0-9]+$")


class User(BaseModel):
    username: str
    logged_in_at: str = Field(default_factory=lambda: datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S (UTC)"))

    @component.context_only_method
    async def user_menu(self, ctx: Context) -> html.details:
        """User menu component."""
        t = TFunction.from_context(ctx)

        return html.details(
            html.summary(self.username, class_="btn btn-primary"),
            html.ul(
                html.li(html.a(await t("user.user_menu.logout"), href="/auth/logout")),
                class_="menu dropdown-content text-error rounded-box z-1 w-auto px-0 shadow-sm",
            ),
            class_="dropdown",
            hx_boost="true",
        )
