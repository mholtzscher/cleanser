"""Utilities for cleaning text."""
import re
from cleanser.core.reddit import reddit_mentions, reddit_quotes, reddit_subreddits
from cleanser.core.generic import whitespace


def reddit(
    text: str,
    mentions: bool = True,
    subreddits: bool = True,
    quotes: bool = True,
    whitespaces: bool = True,
) -> str:
    """Removes common Reddit elements from text."""
    if mentions:
        text = reddit_mentions(text)
    if subreddits:
        text = reddit_subreddits(text)
    if quotes:
        text = reddit_quotes(quotes)
    if whitespaces:
        text = whitespace(text)
    return text
