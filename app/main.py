"""
The main entry point (application instance).

Primarily for deployment.
"""

from .app import make_app

app = make_app()
