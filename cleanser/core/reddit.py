"""Utilities specifically for cleaning text from Reddit."""
import re

REDDIT_MENTIONS = re.compile(r"/?u/\S+")
REDDIT_SUBREDDITS = re.compile(r"/?r/\S+")
REDDIT_QUOTES = re.compile(r"^\>.*$", flags=re.MULTILINE)
REDDIT_BOLD_ITALICS = re.compile(r"\*+")
REDDIT_CODE = re.compile(r"\`")
REDDIT_SUPERSCRIPT = re.compile(r"\^")


def reddit_mentions(text: str) -> str:
    """Removes reddit user mentions from text."""
    return REDDIT_MENTIONS.sub("", text)


def reddit_subreddits(text: str) -> str:
    """Removes reddit subreddit mentions from text."""
    return REDDIT_SUBREDDITS.sub("", text)


def reddit_quotes(text: str) -> str:
    """Removes reddit quotes from text."""
    return REDDIT_QUOTES.sub("", text)


def reddit_bold_italics(text: str) -> str:
    """Removes reddit bolding and italics from text."""
    return REDDIT_BOLD_ITALICS.sub("", text)


def reddit_code(text: str) -> str:
    """Removes reddit code formatting from text."""
    return REDDIT_CODE.sub("", text)


def reddit_superscript(text: str) -> str:
    """Removes reddit superscript formatting from text."""
    return REDDIT_SUPERSCRIPT.sub("", text)
