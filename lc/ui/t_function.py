from typing import Any

from htmy import ContextAware
from htmy.i18n import I18n


class TFunction(ContextAware):
    """
    `htmy` `ContextAware` translation function.
    """

    __slots__ = (
        "_i18n",
        "_lang",
    )

    def __init__(self, i18n: I18n, lang: str | None = None):
        """
        Initialization.

        Arguments:
            i18n: The `I18n` instance to use.
            lang: The language to use. If not provided, `en` will be used.
        """
        self._i18n = i18n
        self._lang = lang or "en"

    async def __call__(self, key: str, **kwargs: Any) -> str:
        """
        Returns the translation for the given key.

        Arguments:
            key: The translation key.
            **kwargs: The translation arguments for string formatting.
        """
        result = await self._i18n.get("en", key, **kwargs)
        if isinstance(result, str):
            return result

        raise ValueError("Only string resources are supported here.")
