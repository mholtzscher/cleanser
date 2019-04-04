import pytest
import string
from cleanser import Cleanser


def test_basic():
    text = string.punctuation
    expected = ""
    assert Cleanser(text).punctuation().text == expected


def test_multiple():
    text = "Python, is awesome?**!#$%^&*()"
    expected = "Python is awesome"
    assert Cleanser(text).punctuation().text == expected


def test_subset():
    text = "Python, is awesome?**!#$%^&*()"
    expected = "Python, is awesome?!#$%&("
    assert Cleanser(text).punctuation(subset="*^)").text == expected


def test_empty_subset():
    text = "Python, is awesome?**!#$%^&*()"
    expected = "Python is awesome"
    assert Cleanser(text).punctuation(subset=[]).text == expected


def test_replacement():
    text = "Python is awesome??"
    expected = "Python is awesome**"
    assert Cleanser(text).punctuation(replacement="*").text == expected


def test_replacement_multiple():
    text = "?Python?^() is awesome?!#"
    expected = "*Python**** is awesome***"
    assert Cleanser(text).punctuation(replacement="*").text == expected
