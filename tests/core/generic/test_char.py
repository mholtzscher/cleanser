import pytest
from cleanser import Cleanser


def test_basic():
    text = "*Python* is awesome."
    expected = "Python is awesome."
    assert Cleanser(text).char("*").text == expected


def test_multiple():
    text = "Python is awesome??"
    expected = "Python is awesome"
    assert Cleanser(text).char("?").text == expected


def test_multiple_chars():
    text = "**Python** is awesome."
    with pytest.raises(ValueError):
        Cleanser(text).char("??")


def test_empty_char():
    text = "**Python** is awesome."
    with pytest.raises(ValueError):
        Cleanser(text).char("")


def test_none_char():
    text = "**Python** is awesome."
    with pytest.raises(ValueError):
        Cleanser(text).char(None)


def test_replacement():
    text = "Python is awesome??"
    expected = "Python is awesome**"
    assert Cleanser(text).char("?", replacement="*").text == expected


def test_replacement_multiple():
    text = "?Python? is awesome??"
    expected = "*Python* is awesome**"
    assert Cleanser(text).char("?", replacement="*").text == expected
