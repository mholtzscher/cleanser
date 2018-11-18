from cleanser.core.generic import url
import pytest


def test_basic():
    text = "You should look at https://google.com"
    assert url(text) == "You should look at "


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
    assert url(text) == expected
