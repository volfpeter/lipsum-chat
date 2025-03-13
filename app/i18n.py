from pathlib import Path

from htmy.i18n import I18n

_locale_dir = Path(__file__).parent.parent / "locale"

i18n = I18n(_locale_dir)
