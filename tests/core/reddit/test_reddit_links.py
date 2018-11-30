from cleanser import Cleanser
import pytest


def test_basic():
    text = "You should look at [Google](https://google.com)"
    expected = "You should look at "
    assert Cleanser(text).reddit_links().text == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("[Google](https://google.com)", ""),
        ("[Google](http://www.google.com)", ""),
        ("[Google](https://www.google.com)", ""),
        ("[Google](http://github.com)", ""),
    ],
)
def test_patterns(text, expected):
    assert Cleanser(text).reddit_links().text == expected
