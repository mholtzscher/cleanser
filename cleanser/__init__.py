"""Utilities for cleaning text."""
import re
from cleanser.regex import (
    URL_REGEX,
    REDDIT_MENTIONS,
    REDDIT_SUBREDDITS,
    REDDIT_QUOTES,
    WHITESPACE,
    RE_EMOJI,
)


def reddit_mentions(text: str) -> str:
    """Removes reddit user mentions from text."""
    return REDDIT_MENTIONS.sub("", text)


def reddit_subreddits(text: str) -> str:
    """Removes reddit user mentions from text."""
    return REDDIT_SUBREDDITS.sub("", text)


def reddit_quotes(text: str) -> str:
    """Removes reddit quotes from test."""
    return REDDIT_QUOTES.sub("", text)


def urls(text: str) -> str:
    """Removes urls from text."""
    return URL_REGEX.sub("", text)


def emoji(text: str) -> str:
    """Removes emojis from text."""
    return RE_EMOJI.sub("", text)


def whitespace(text: str) -> str:
    """Removes extra spaces, tabs, and newlines from text."""
    return WHITESPACE.sub(" ", text).strip()


def cleanse(text: str) -> str:
    """Apply all cleansers to text."""
    text = reddit_mentions(text)
    text = reddit_subreddits(text)
    text = urls(text)
    text = emoji(text)
    text = whitespace(text)
    return text
