import re

REDDIT_MENTIONS = re.compile(r"/?u/\S+")
REDDIT_SUBREDDITS = re.compile(r"/?r/\S+")
WHITESPACE = re.compile(r"\s\s+")


def reddit_mentions(text: str) -> str:
    return REDDIT_MENTIONS.sub("", text)


def reddit_subreddits(text: str) -> str:
    return REDDIT_SUBREDDITS.sub("", text)


def urls(text: str) -> str:
    return "None"


def whitespace(text: str) -> str:
    return WHITESPACE.sub(" ", text).strip()
