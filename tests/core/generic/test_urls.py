from cleanser.core.generic import urls
import pytest


def test_basic():
    text = "You should look at https://google.com"
    assert urls(text) == "You should look at "


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
    assert urls(text) == expected
