import re

REDDIT_MENTIONS = re.compile(r"/?u/\S+")
REDDIT_SUBREDDITS = re.compile(r"/?r/\S+")
WHITESPACE = re.compile(r"\s\s+")
RE_EMOJI = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
URL_REGEX = re.compile(
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)
