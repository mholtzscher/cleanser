"""Utilities for cleaning text."""
import re
from cleanser.core.reddit import (
    reddit_mentions,
    reddit_quotes,
    reddit_subreddits,
    reddit_bold_italics,
    reddit_code,
    reddit_superscript,
    reddit_headers,
    reddit_strikethrough,
)
from cleanser.core.generic import whitespace, url, emoji


def purify_reddit(
    text: str,
    mentions: bool = True,
    subreddits: bool = True,
    quotes: bool = True,
    bold_italics: bool = True,
    code: bool = True,
    superscript: bool = True,
    headers: bool = True,
    strikethrough: bool = True,
) -> str:
    """Removes common Reddit elements from text."""
    if mentions:
        text = reddit_mentions(text)
    if subreddits:
        text = reddit_subreddits(text)
    if quotes:
        text = reddit_quotes(text)
    if bold_italics:
        text = reddit_bold_italics(text)
    if code:
        text = reddit_code(text)
    if superscript:
        text = reddit_superscript(text)
    if headers:
        text = reddit_headers(text)
    if strikethrough:
        text = reddit_strikethrough(text)
    return text


def purify(
    text: str,
    whitespaces: bool = True,
    urls: bool = True,
    emojis: bool = True,
    reddit: bool = False,
    **kwargs
) -> str:
    """Cleanses text and purifies it."""
    if whitespaces:
        text = whitespace(text)
    if urls:
        text = url(text)
    if emojis:
        text = emoji(text)
    if reddit:
        text = purify_reddit(text, **kwargs)
    return text
