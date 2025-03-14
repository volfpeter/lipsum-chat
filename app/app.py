"""
App factory and configuration.
"""

from fastapi import FastAPI

from lc.authenticator import Authenticator
from lc.ui.t_function import TFunction

from .api import add_routes
from .exception_handlers import add_exception_handlers
from .htmy import htmy
from .i18n import i18n


def make_app() -> FastAPI:
    # Create the app and the necessary utilities.
    app = FastAPI()
    auth = Authenticator()

    # Add the auth middleware.
    app.middleware("http")(auth.middleware)

    # Register the htmy context processors.
    htmy.request_processors.extend(
        (
            # Authenticator
            auth.htmy_context_processor,
            # Translation function
            lambda r: TFunction(i18n, r.headers.get("Language-Selection-Not-Supported", "en")).to_context(),
        )
    )

    # Register exception handlers.
    add_exception_handlers(app)

    # Register all routes.
    add_routes(app, auth=auth)

    return app
