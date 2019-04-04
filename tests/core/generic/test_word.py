import pytest
from cleanser import Cleanser


def test_basic():
    text = "Java is awesome."
    expected = " is awesome."
    assert Cleanser(text).word("Java").text == expected


def test_multiple():
    text = "Python is awesome and NLP is awesome."
    expected = "Python is  and NLP is ."
    assert Cleanser(text).word("awesome").text == expected


def test_empty_word():
    text = "**Python** is awesome."
    with pytest.raises(ValueError):
        Cleanser(text).word("")


def test_none_word():
    text = "**Python** is awesome."
    with pytest.raises(ValueError):
        Cleanser(text).word(None)


def test_replacement():
    text = "Java is awesome!!"
    expected = "Python is awesome!!"
    assert Cleanser(text).word("Java", replacement="Python").text == expected


def test_replacement_multiple():
    text = "Java is awesome and Java is fast."
    expected = "Python is awesome and Python is fast."
    assert Cleanser(text).word("Java", replacement="Python").text == expected
