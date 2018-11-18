"""Common methods for cleaning text."""
import re

WHITESPACE = re.compile(r"\s+")
RE_EMOJI = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
URL_REGEX = re.compile(
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)


def url(text: str) -> str:
    """Removes urls from text."""
    return URL_REGEX.sub("", text)


def emoji(text: str) -> str:
    """Removes emojis from text."""
    return RE_EMOJI.sub("", text)


def whitespace(text: str) -> str:
    """Removes extra spaces, tabs, and newlines from text."""
    return WHITESPACE.sub(" ", text).strip()
