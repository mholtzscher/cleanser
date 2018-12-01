from cleanser import Cleanser
import pytest


def test_basic():
    text = "&gt; You should look at cars."
    expected = "> You should look at cars."
    assert Cleanser(text).unescape_html().text == expected


@pytest.mark.parametrize(
    "text,expected",
    [("Less &lt; than", "Less < than"), ("Greater &gt; than", "Greater > than")],
)
def test_patterns(text, expected):
    assert Cleanser(text).unescape_html().text == expected
