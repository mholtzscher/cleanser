"""Utilities for cleaning text."""
import re

REDDIT_MENTIONS = re.compile(r"/?u/\S+")
REDDIT_SUBREDDITS = re.compile(r"/?r/\S+")
WHITESPACE = re.compile(r"\s\s+")


def reddit_mentions(text: str) -> str:
    """Removes reddit user mentions from text."""
    return REDDIT_MENTIONS.sub("", text)


def reddit_subreddits(text: str) -> str:
    """Removes reddit user mentions from text."""
    return REDDIT_SUBREDDITS.sub("", text)


def urls(text: str) -> str:
    """Removes urls from text."""
    return text


def whitespace(text: str) -> str:
    """Removes extra spaces, tabs, and newlines from text."""
    return WHITESPACE.sub(" ", text).strip()
