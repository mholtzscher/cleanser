from cleanser import Cleanser
import pytest


def test_basic():
    text = "You should look at https://google.com"
    expected = "You should look at "
    assert Cleanser(text).urls().text == expected


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
    assert Cleanser(text).urls().text == expected
