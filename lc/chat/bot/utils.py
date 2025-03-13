import re

_splitter = re.compile(r"[^a-z0-9]+")


def make_word_sets(sentences: tuple[str, ...]) -> tuple[set[str], ...]:
    """
    Returns a tuple of sets of words from the given sentences.

    The order of the sets matches the order of the sentences.
    """
    return tuple(set(re.split(_splitter, sentence.lower())) for sentence in sentences)


def weights_for_message(sentence: str, *, word_sets: tuple[set[str], ...]) -> tuple[float, ...]:
    """
    Returns a tuple of weights for the given sentence.
    """
    words = set(re.split(_splitter, sentence.lower()))
    return tuple(1 + len(words & word_set) * 29 for word_set in word_sets)
