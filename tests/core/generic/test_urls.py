from cleanser import Cleanser
import pytest


def test_basic():
    text = "You should look at https://google.com"
    assert Cleanser(text).url().text == "You should look at "


@pytest.mark.parametrize(
    "text,expected",
    [
        ("https://google.com", ""),
        ("http://www.google.com", ""),
        ("https://www.google.com", ""),
        ("http://github.com", ""),
    ],
)
def test_patterns(text, expected):
    assert Cleanser(text).url().text == expected
