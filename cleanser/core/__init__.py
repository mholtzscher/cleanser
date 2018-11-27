class Base:
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, v):
        self._text = v

    def __repr__(self):
        return f"{self.__class__.__name__}({self.text!r})"

    def __str__(self):
        return f"{self.text}"
