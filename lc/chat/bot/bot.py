import random

from htmy import ComponentSequence

from lc.ui.navbar import ChatPageKey

from .beer_corpus import sentences as beer
from .beer_corpus import word_sets as beer_word_sets
from .coffee_corpus import sentences as coffee
from .coffee_corpus import word_sets as coffee_word_sets
from .utils import weights_for_message


def get_response(message: str, *, corpus: ChatPageKey) -> ComponentSequence:
    if corpus == "beer":
        sentences, word_sets = beer, beer_word_sets
    elif corpus == "coffee":
        sentences, word_sets = coffee, coffee_word_sets
    else:
        raise ValueError(f"Unknown corpus: {corpus}")

    return random.choices(  # noqa: S311
        sentences,
        weights_for_message(message, word_sets=word_sets),
        k=random.randint(2, 7),  # noqa: S311
    )
