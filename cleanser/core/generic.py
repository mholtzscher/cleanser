"""Common generic methods for cleaning text."""
import re
import string
from cleanser.core import Base

RE_WHITESPACE = re.compile(r"\s+")
RE_EMOJI = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
URL_REGEX = re.compile(
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)


class Generic(Base):
    """Common generic methods for cleaning text."""

    def whitespaces(self):
        """Removes extra spaces, tabs, and newlines from text."""
        self.text = RE_WHITESPACE.sub(" ", self.text).strip()
        return self

    def emojis(self):
        """Removes emojis from text."""
        self.text = RE_EMOJI.sub("", self.text)
        return self

    def urls(self):
        """Removes urls from text."""
        self.text = URL_REGEX.sub("", self.text)
        return self

    def char(self, char: str, replacement: str = ""):
        """Removes all occurences of char from text."""
        if not char or len(char) > 1:
            raise ValueError("char parameter can only be 1 character")
        self.text = self.text.replace(char, replacement)
        return self

    def word(self, word: str, replacement: str = ""):
        """Removes all occurences of given word from text."""
        if not word:
            raise ValueError("word parameter cannot be empty or None")
        self.text = self.text.replace(word, replacement)
        return self

    def double_punctuation(self):
        """Removes occurences of double punctuation with single instance of char"""
        punctuation = ".,?!:;*"
        for punc in punctuation:
            pattern = "\\" + punc + "{2,}"
            self.text = re.sub(pattern, punc, self.text)
        return self

    def punctuation(self, subset: list = None, replacement: str = ""):
        """Removes all occurences punctuation from text"""
        punctuation = subset or string.punctuation
        for punc in punctuation:
            self.text = self.text.replace(punc, replacement)
        return self
