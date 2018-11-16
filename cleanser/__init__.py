"""Utilities for cleaning text."""
import re
from cleanser.core.reddit import reddit_mentions, reddit_quotes, reddit_subreddits


def reddit(
    text: str, mentions: bool = True, subreddits: bool = True, quotes: bool = True
) -> str:
    if mentions:
        text = reddit_mentions(text)
    if subreddits:
        text = reddit_subreddits(text)
    if quotes:
        text = reddit_quotes(quotes)
    return text
