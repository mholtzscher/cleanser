"""Utilities for cleaning text."""
import re
from cleanser.core.reddit import reddit_mentions, reddit_quotes, reddit_subreddits
from cleanser.core.generic import whitespace, url, emoji


def _purify_reddit(
    text: str, mentions: bool = True, subreddits: bool = True, quotes: bool = True
) -> str:
    """Removes common Reddit elements from text."""
    if mentions:
        text = reddit_mentions(text)
    if subreddits:
        text = reddit_subreddits(text)
    if quotes:
        text = reddit_quotes(text)
    return text


def purify(
    text: str,
    whitespaces: bool = True,
    urls: bool = True,
    emojis: bool = True,
    reddit: bool = False,
    **kwargs
) -> str:
    if whitespaces:
        text = whitespace(text)
    if urls:
        text = url(text)
    if emojis:
        text = emoji(text)
    if reddit:
        text = _purify_reddit(text, **kwargs)
    return text
