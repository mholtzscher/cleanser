import re

REDDIT_MENTIONS = re.compile(r"/?u/\S+")
REDDIT_SUBREDDITS = re.compile(r"/?r/\S+")
REDDIT_QUOTES = re.compile(r"^\>.*$", flags=re.MULTILINE)


def reddit_mentions(text: str) -> str:
    """Removes reddit user mentions from text."""
    return REDDIT_MENTIONS.sub("", text)


def reddit_subreddits(text: str) -> str:
    """Removes reddit subreddit mentions from text."""
    return REDDIT_SUBREDDITS.sub("", text)


def reddit_quotes(text: str) -> str:
    """Removes reddit quotes from test."""
    return REDDIT_QUOTES.sub("", text)
