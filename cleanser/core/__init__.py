"""Common functions and classes for all core classes."""


class Base:
    """Base class for all cleansers"""

    def __init__(self):
        self._text = None

    @property
    def text(self) -> str:
        """Property for text that is being cleansed"""
        return self._text

    @text.setter
    def text(self, value: str):
        """Property setter for text that is being cleansed"""
        self._text = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text!r})"

    def __str__(self) -> str:
        return f"{self.text}"
